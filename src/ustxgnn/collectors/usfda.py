"""US 本國藥證收集器（NEW_COUNTRY_SOP Phase 5：collectors/{cc}fda.py）。

2026-11-06 起改用依成分比對（用戶核准），跟 scripts/rebuild_licenses_by_ingredient.py 共用
collectors/us_license_match.py 的同一套規則，新收的證據包直接是依成分比對的結果：
- FDA 核准申請：openFDA Drugs@FDA（data/raw/drugsfda_openfda.zip），每個申請號一筆；只有暫定核准的申請不收。
- OTC monograph／未核准類別的 NDC 列名產品：openFDA NDC（data/raw/ndc_openfda.zip；沒有時退回 data/raw/us_fda_drugs.json），
  不是 FDA 核准，另外計數（listed_total），最多列 20 筆（listing: true）。
- 複方（drug 以「;」分隔多個成分）要成分組合完全相同；單方收含本藥的產品。
- 兩個 zip 都不在本機時從 openFDA 下載（同 rebuild 腳本）。

舊做法（依 DrugBank ID 對 NDC 產品列、截 20 筆）會把複方頁算進「只含其中一個成分」的產品，已停用。
回傳格式與 TwTxGNN 的 TFDACollector 相同（found / records / total_matches / package_insert），另加 listed_total、applications_total；
drug_bundle.py 與 drug_evidence_pack.py 不需要改。
"""

import csv
import re
import unicodedata
from pathlib import Path

from . import us_license_match as lm
from .base import BaseCollector, CollectorResult

PROJECT_ROOT = Path(__file__).resolve().parents[3]
RAW = PROJECT_ROOT / "data" / "raw"
INGREDIENT_COLS = ("normalized_ingredient", "標準化成分")
SUCCESS_COLS = ("mapping_success", "映射成功")


def _norm(text) -> str:
    text = unicodedata.normalize("NFKD", str(text or "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


class LocalFDACollector(BaseCollector):
    """US 藥證查詢：依成分比對 Drugs@FDA 申請號與 NDC 列名產品。"""

    source_name = "local_fda"

    def __init__(self, drugsfda_zip: Path | None = None, ndc_zip: Path | None = None, legacy_ndc_json: Path | None = None):
        self.drugsfda_zip = Path(drugsfda_zip or RAW / "drugsfda_openfda.zip")
        self.ndc_zip = Path(ndc_zip or RAW / "ndc_openfda.zip")
        self.legacy_ndc_json = Path(legacy_ndc_json or RAW / "us_fda_drugs.json")
        self._index = None
        self._db = None

    def _prepare(self):
        if self._index is not None:
            return
        if not self.drugsfda_zip.exists():
            lm.download(lm.DRUGSFDA_URL, self.drugsfda_zip)
        if not self.ndc_zip.exists() and not self.legacy_ndc_json.exists():
            lm.download(lm.NDC_URL, self.ndc_zip)
        self._index = lm.LicenseIndex.from_files(self.drugsfda_zip, self.ndc_zip, self.legacy_ndc_json)

    def _drugbank_ids(self, drug: str) -> set:
        """證據包的 drugbank_ids 欄（只供參考，不參與許可證比對）：drug_mapping.csv 與 drugbank_vocab.csv 的英文名對照"""
        if self._db is None:
            self._db = {}
            mp = PROJECT_ROOT / "data" / "processed" / "drug_mapping.csv"
            if mp.exists():
                with open(mp, encoding="utf-8-sig", newline="") as f:
                    reader = csv.DictReader(f)
                    cols = reader.fieldnames or []
                    ing_col = next((c for c in INGREDIENT_COLS if c in cols), None)
                    ok_col = next((c for c in SUCCESS_COLS if c in cols), None)
                    for row in reader:
                        db = str(row.get("drugbank_id", "") or "").strip().upper()
                        if db and ing_col and (not ok_col or str(row.get(ok_col)).strip().lower() in ("true", "1", "yes")):
                            self._db.setdefault(_norm(row[ing_col]), set()).add(db)
            vocab = PROJECT_ROOT / "data" / "external" / "drugbank_vocab.csv"
            if vocab.exists():
                with open(vocab, encoding="utf-8-sig", newline="") as f:
                    for row in csv.DictReader(f):
                        self._db.setdefault(_norm(row.get("drug_name")), set()).add(str(row.get("drugbank_id", "")).upper())
        ids = set(self._db.get(_norm(drug), set()))
        m = re.fullmatch(r"\s*(DB\d{5})\s*", str(drug or ""), re.I)
        if m:
            ids.add(m.group(1).upper())
        return ids

    def search(self, drug: str, disease: str | None = None, drugbank_id: str | None = None) -> CollectorResult:
        query = {"drug": drug, "disease": disease}
        try:
            self._prepare()
            data, mode = self._index.match(drug)
            ids = self._drugbank_ids(drug)
            if drugbank_id:
                ids.add(str(drugbank_id).upper())
            data.update({
                "drugbank_ids": sorted(ids),
                "match_mode": mode,
                "rebuilt": self._index.label(),
                "package_insert": {"warnings": [], "contraindications": [], "dosage": "", "special_populations": []},
            })
            return self._make_result(query=query, data=data, success=True)
        except Exception as e:  # noqa: BLE001 — 與其他 collector 一致：失敗時回 not found 並帶錯誤
            return self._make_result(query=query, data={"found": False, "records": []}, success=False, error_message=str(e))

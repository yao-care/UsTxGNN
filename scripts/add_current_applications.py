"""每週補收：openFDA 現行 Drugs@FDA／NDC 有、證據包還沒收的本藥 FDA 申請號（2026-11-25，用戶決定第五輪第 2、3 條；全程不用 AI）。

背景：證據包 tfda.records 是 2026-11-05～06 scripts/rebuild_licenses_by_ingredient.py 依成分重建的（openFDA Drugs@FDA 2026-11-06 版），
每週許可證排程只更新既有申請號的狀態，之後才核准的申請（例 2026-11 的新 ANDA）不會進證據包。
這支照同一套比對規則（src/ustxgnn/collectors/us_license_match.py 的 LicenseIndex.match，跟重建、collectors/usfda.py 相同，不放寬）
重算本藥對到的申請號，證據包還沒有的補一筆：
- 只補 FDA 申請號（NDA／ANDA／BLA）；OTC monograph／未核准類別的 NDC 列名產品不是 FDA 核准，不在這支處理（列名數照舊由重建維護）。
- 只加不刪：證據包已有、現行比對不到的申請號不動（狀態由每週排程照 Drugs@FDA／Purple Book／NDC 更新）。
- 紀錄欄位照 LicenseIndex.match 的 app_rec（品名、成分、劑型、途徑、持有人、首次核准日、狀態、source）；另記 added＝補收日、
  added_by＝本程式與規則說明。插入位置照重建的排序鍵（有效在前、成分數少的在前、申請號），既有紀錄的順序不動。
- applications_total、total_matches 各加補收筆數；Us 的申請號沒有筆數上限（重建時全部存進 records），所以沒有「只算張數」的情形。
可重複執行（已有的申請號不重複補）。
用法（repo 根目錄）：python3 scripts/add_current_applications.py [--download] [--dry-run] [--report out.tsv] [頁 ...]
  --download：先重新下載 openFDA Drugs@FDA、NDC 全量檔到 data/raw（不給就用 data/raw 裡的；scripts/license_adapter.py 每週排程也會存同兩份）
"""
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data/raw"
ZIP = RAW / "drugsfda_openfda.zip"
NDC_ZIP = RAW / "ndc_openfda.zip"
sys.path.insert(0, str(ROOT / "src"))
from ustxgnn.collectors import us_license_match as lm  # noqa: E402

RULE = "same rule as scripts/rebuild_licenses_by_ingredient.py (us_license_match.LicenseIndex.match)"


def _key(r):
    st = str(r.get("status") or "")
    inactive = st.endswith(lm.SUFFIX) or st.endswith(" (License revoked in Purple Book)")
    n = len([x for x in str(r.get("ingredients") or "").split("; ") if x]) or 99
    return (inactive, n, str(r.get("license_id") or ""))


def insert(recs, new):
    """new 依重建的排序鍵插進申請號紀錄裡（列名紀錄在最後），既有紀錄順序不動"""
    for r in sorted(new, key=_key):
        k = _key(r)
        pos = next((i for i, x in enumerate(recs) if x.get("listing") or _key(x) > k), len(recs))
        recs.insert(pos, r)
    return recs


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    if "--download" in argv:
        lm.download(lm.DRUGSFDA_URL, ZIP)
        lm.download(lm.NDC_URL, NDC_ZIP)
    if not ZIP.exists():
        raise SystemExit(f"找不到 {ZIP}（先跑 scripts/restore_data.sh 或加 --download）")
    idx = lm.LicenseIndex.from_files(ZIP, NDC_ZIP, RAW / "us_fda_drugs.json")
    today = date.today().isoformat()
    out, n_b, n_r = [], 0, 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        tf = b.get("tfda")
        if not isinstance(tf, dict):
            continue
        inn = (b.get("drug") or {}).get("inn") or page.replace("_", " ")
        data, mode = idx.match(inn)
        have = {str(r.get("license_id") or "").strip() for r in tf.get("records") or []}
        have |= {str(r.get("license_id") or "").strip() for r in tf.get("excluded_records") or []}
        new = [r for r in data["records"] if not r.get("listing") and r["license_id"] not in have]
        if not new:
            continue
        for r in new:
            r["added"] = today
            r["added_by"] = f"scripts/add_current_applications.py ({RULE}; Drugs@FDA {idx.updated})"
        n_b += 1
        n_r += len(new)
        out.append(f"{page}\t{mode}\t{len(new)}\t" + ";".join(f"{r['license_id']}|{r['brand_name_en']}|{r['ingredients']}|{r['status']}" for r in new))
        if dry:
            continue
        tf["records"] = insert(list(tf.get("records") or []), new)
        tf["applications_total"] = int(tf.get("applications_total") or 0) + len(new)
        tf["total_matches"] = int(tf.get("total_matches") or 0) + len(new)
        tf["found"] = True
        f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tmode\tadded\tapplications\n" + "\n".join(out) + "\n", encoding="utf-8")
    print(f"Drugs@FDA {idx.updated}、NDC {idx.ndc_updated}：{'（試跑）' if dry else ''}補收 {n_b} 個證據包 {n_r} 個申請號")


if __name__ == "__main__":
    main(sys.argv[1:])

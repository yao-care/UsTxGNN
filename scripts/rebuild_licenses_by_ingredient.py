"""US 依成分重建證據包的許可證紀錄（2026-11-05，用戶核准；全程不用 AI；做法比照 Za／Kr／My）。

原收集器（2026-11-05 前的 collectors/usfda.py）依 DrugBank ID 對 NDC 產品列、截 20 筆，複方頁會把「只含其中一個成分」的產品算進來
（例：10 成分順勢療法複方頁的「許可」是 balsalazide、pemetrexed 等單方產品），概覽寫成 Marketed；
單方頁也只收到 NDC 產品列裡的一兩個申請號（mycophenolic acid 只有 1 張已停產的 ANDA，Myfortic 與其他 ANDA 都沒收）。

比對規則在 src/ustxgnn/collectors/us_license_match.py（collectors/usfda.py 新收證據包也用同一套）：
openFDA Drugs@FDA 的申請號＋openFDA NDC 的列名產品（OTC monograph／未核准類別，另計 listed_total）；複方要成分組合完全相同；
只有暫定核准的申請不收。
2026-11-06 起 NDC 改用 openFDA NDC 全量檔（每次重建前重新下載，存 data/raw/ndc_openfda.zip），不再用 2026-03 的 us_fda_drugs.json；
成分裡括號內的「;」不再當分隔。

寫回證據包 tfda：records、listed_total、applications_total、total_matches 整批換掉（原紀錄來源錯配，留著會把別的藥算進來），
drugbank_ids、package_insert 等其他欄位保留。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--skip-download] [--dry-run] [--report out.tsv] [頁 ...]
  --skip-download：用 data/raw 裡已存的 drugsfda_openfda.zip、ndc_openfda.zip（沒有 ndc_openfda.zip 時退回 us_fda_drugs.json）
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
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
import license_adapter as ad  # noqa: E402
from ustxgnn.collectors import us_license_match as lm  # noqa: E402

assert lm.DRUGSFDA_URL == ad.URL and lm.SUFFIX == ad.SUFFIX


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    if "--skip-download" not in argv:
        lm.download(lm.DRUGSFDA_URL, ZIP)
        lm.download(lm.NDC_URL, NDC_ZIP)
    idx = lm.LicenseIndex.from_files(ZIP, NDC_ZIP, RAW / "us_fda_drugs.json")
    if not dry and "--skip-download" not in argv:
        # 申請號的狀態檔（license_refresh 用）跟著同一份 Drugs@FDA 更新
        (RAW / "drugsfda_appl_status.json").write_text(json.dumps(idx.appl_status, ensure_ascii=False, indent=1), encoding="utf-8")
    stamp = f"{date.today().isoformat()} {idx.label()}"
    out, n_changed, n_found, n_empty = [], 0, 0, 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("tfda") or {}
        inn = (b.get("drug") or {}).get("inn") or page.replace("_", " ")
        data, mode = idx.match(inn)
        recs = [r for r in data["records"] if not r.get("listing")]
        old_ids = sorted({str(r.get("license_id") or "") for r in reg.get("records") or [] if lm.APPL.match(str(r.get("license_id") or ""))})
        new_ids = sorted(r["license_id"] for r in recs)
        nv = sum(1 for r in recs if not r["status"].endswith(lm.SUFFIX))
        old_l = reg.get("listed_total", "")
        out.append(f"{page}\t{mode}\t{len(old_ids)}\t{len(new_ids)}\t{nv}\t{old_l}\t{data['listed_total']}\t{len(set(old_ids) - set(new_ids))}\t"
                   f"{';'.join(sorted(set(old_ids) - set(new_ids))[:15])}\t{';'.join(sorted(set(new_ids) - set(old_ids))[:15])}")
        n_found += data["found"]
        n_empty += not data["found"]
        same = all(reg.get(k) == data[k] for k in data)
        if not same:
            n_changed += 1
            b["tfda"] = dict(reg, **data, rebuilt=stamp)
            if not dry:
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tmode\told_applications\tnew_applications\tnew_active\told_listings\tlistings\tdropped\tdropped_ids\tadded_ids\n"
                             + "\n".join(out) + "\n", encoding="utf-8")
    print(f"Drugs@FDA {idx.updated}：{len(idx.apps)} 個申請號（暫定核准不收 {len(idx.tentative)}）、NDC（{idx.ndc_updated}）列名產品 {len(idx.listings)}；"
          f"改 {n_changed} 個證據包（有紀錄 {n_found}、查無 {n_empty}）")


if __name__ == "__main__":
    main(sys.argv[1:])

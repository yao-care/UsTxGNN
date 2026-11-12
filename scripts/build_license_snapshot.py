#!/usr/bin/env python3
"""產生許可證快照 snapshots/us_licenses.json.gz（2026-11-12 建，本站查核機制；比照 TwTxGNN snapshots/tfda_licenses.json.gz）。

為什麼要有這支：
  藥物頁的許可證表、概覽表的狀態列與張數列是程式依證據包（data/bundles，放在 Release）與事實層
  （.claude/cache/license_facts，dump_license_facts 依證據包算）產生的。gate（scripts/check_seo_docs.py）要在沒有
  data/ 的環境（GitHub Actions 的 Pages 建置、clone 下來的 repo）也能驗證頁面上的號碼屬於本藥、程式表沒被改、
  狀態列與張數列跟事實一致，所以把驗證要用的部分存成快照放進 git。

內容（鍵＝藥物頁檔名去 .md）：
  facts：事實層那一筆（market_status、total、valid、cancelled、partial、licenses{申請號: valid|cancelled} …）
  rows：scripts/sync_license_tables.rows_of 依證據包＋事實層算出的表格列（最多 20 列，程式表就是取前 N 列）
  total：申請號數＋NDC 列名產品數（SHOW 句與張數列用的同一個數字）
  own：本藥擁有的申請號（NDA／ANDA／BLA＋6 碼）與 NDC 列名產品碼（「NDC <碼>」）
  meta：產生日、證據包來源（Release tag 與 tfda.records 的 source）、比對規則所在檔案

什麼時候跑：證據包或事實層變了之後（每週許可證排程 license-refresh.yml、依成分重建 license-rebuild.yml 都在改頁後跑，
並把 snapshots/ 跟 docs/ 一起 commit）。用法（repo 根目錄，先還原 data/ 並在工作目錄跑 dump_license_facts）：
  python3 scripts/build_license_snapshot.py --ws <工作目錄> [--release-tag data-YYYYMMDD-HHMMSS]
"""
import datetime as dt
import gzip
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import sync_license_tables as S  # noqa: E402

OUT = ROOT / "snapshots" / "us_licenses.json.gz"


def own_ids(tf):
    out = set()
    for r in tf.get("records") or []:
        if r.get("listing"):
            k = str(r.get("product_ndc") or "").strip()
            if k:
                out.add(f"NDC {k}")
        else:
            k = str(r.get("license_id") or "").strip()
            if S.APPL.fullmatch(k):
                out.add(k)
    return sorted(out)


def build(ws, tag=""):
    fs = S.facts(ws)
    if not fs:
        sys.exit(f"找不到事實層 {Path(ws) / '.claude/cache/license_facts' / (S.SITE + '.json')}（先跑 dump_license_facts）")
    drugs, src = {}, Counter()
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        head = page.read_text(encoding="utf-8", errors="replace")[:3000]
        if "layout: id_redirect" in head or 'http-equiv="refresh"' in head:
            continue
        key, b = S.bundle_for(page)
        if b is None:
            continue
        tf = b.get("tfda") or {}
        fc = fs.get(key) or fs.get(page.stem)
        rows, total = S.rows_of(tf, fc)
        for r in tf.get("records") or []:
            if r.get("source"):
                src[r["source"]] += 1
        drugs[page.stem] = {"bundle": key, "facts": fc, "rows": rows[:20], "total": total, "own": own_ids(tf)}
    meta = {"built": dt.date.today().isoformat(), "release_tag": tag, "pages": len(drugs),
            "record_sources": dict(src.most_common(5)),
            "rule": "表格列：scripts/sync_license_tables.py rows_of；事實層：tools/txgnn/.claude/dump_license_facts_20261021.py"}
    OUT.parent.mkdir(exist_ok=True)
    raw = json.dumps({"meta": meta, "drugs": drugs}, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    with gzip.GzipFile(OUT, "wb", mtime=0) as fh:  # mtime=0：內容相同時檔案位元組相同，不會每次都產生 diff
        fh.write(raw)
    print(f"許可證快照：{len(drugs)} 頁 → {OUT.relative_to(ROOT)}（{OUT.stat().st_size // 1024} KB）")


if __name__ == "__main__":
    a = sys.argv[1:]
    ws = a[a.index("--ws") + 1]
    tag = a[a.index("--release-tag") + 1] if "--release-tag" in a else ""
    if not re.fullmatch(r"(data-[\w-]+)?", tag):
        sys.exit("--release-tag 要是 data-… 的 tag")
    build(ws, tag)

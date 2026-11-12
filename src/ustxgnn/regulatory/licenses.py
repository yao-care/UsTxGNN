"""藥物頁許可證資訊的驗證（2026-11-12 建，本站查核機制；比照 TwTxGNN 的 gate 第 6 項）。

依 snapshots/us_licenses.json.gz（scripts/build_license_snapshot.py 產生）檢查，不需要 data/：
  1. 「## US Market Information」段落裡出現的申請號（表格與正文）都屬於本藥（快照 own）；
     正文明說是別的藥（「… as a standalone drug」）的不算（同 scripts/sync_license_tables.py needs_resync 規則 3）。
  2. 程式區塊（<!-- licenses:begin --> … <!-- licenses:end -->）＝依快照重算的結果：表頭、列＝快照 rows 的前 N 列
     （N 介於 min(5, 列數) 與 20 之間）、SHOW 句的 n／m 正確（總數多於列數時才有）；沒有任何申請號或列名時是 NONE_LINE。
     表頭是程式表頭卻沒有標記，也算錯（程式區塊要能被辨認）。
  3. 概覽表的狀態列與張數列＝事實層的寫法：用本站 tools/txgnn/.claude/check_drug_page.py 的 marketed_text／
     not_marketed_text／unknown_status_text／not_reg_text／count_text（checker M1／M4 的同一套函式）。
  4. 表格列寫的狀態不得跟事實相反（checker row_status_conflicts）。
修法：資料變了→跑每週排程（或 scripts/sync_license_tables.py＋scripts/build_license_snapshot.py）；
正文提到的號碼、狀態不對→寫查核紀錄（docs/_data/drug_reviews.json）再跑 scripts/apply_drug_reviews.py。
"""
from __future__ import annotations

import gzip
import importlib.util
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SNAP = ROOT / "snapshots" / "us_licenses.json.gz"
SITE = "UsTxGNN"


def _load(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


@lru_cache(maxsize=None)
def S():
    return _load("us_sync_license_tables", ROOT / "scripts" / "sync_license_tables.py")


@lru_cache(maxsize=None)
def CK():
    return _load("us_check_drug_page", ROOT / "tools" / "txgnn" / ".claude" / "check_drug_page.py")


@lru_cache(maxsize=None)
def snapshot() -> dict:
    if not SNAP.exists():
        return {}
    return json.loads(gzip.open(SNAP).read().decode("utf-8"))


def _section(lines):
    s = S()
    if s.SEC not in lines:
        return None, None
    a = lines.index(s.SEC) + 1
    b = next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))
    return a, b


def _tables(lines):
    out, cur = [], []
    for ln in lines + [""]:
        if ln.startswith("|"):
            cur.append(ln)
        elif cur:
            out.append(cur)
            cur = []
    return out


def _rows(tbl):
    return [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in tbl[2:]]


def expected_status(fc):
    ck, lang = CK(), CK().LANG.get(SITE, "en")
    ms, v, n, partial = fc.get("market_status"), fc.get("valid"), fc.get("total"), fc.get("partial")
    if ms == "Marketed":
        return ck.marketed_text(SITE, lang, v, n, partial, fc)
    if ms == "Approved, not marketed":
        return ck.not_marketed_text(SITE, lang, fc)
    if ms == "Status unknown" and SITE in ck.UNKNOWN_ST:
        return ck.unknown_status_text(SITE, lang, fc)
    if ms == "Not marketed" and SITE in ck.VET_ONLY:
        return ck.not_reg_text(SITE, lang, fc)
    return None


def page_problems(stem: str, text: str) -> list[str]:
    snap = snapshot().get("drugs") or {}
    e = snap.get(stem)
    if e is None:
        return []  # 快照沒有的頁（沒有證據包）：不驗
    s, ck = S(), CK()
    body = re.sub(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", "", text, flags=re.S)
    lines = body.replace("\r\n", "\n").split("\n")
    errs = []
    own = set(e["own"])
    a, b = _section(lines)
    if a is not None:
        sec = lines[a:b]
        for ln in sec:
            if not ln.startswith("|") and s.OTHER_DRUG.search(ln):
                continue
            bad = sorted({m.group(1) + m.group(2) for m in s.APPL.finditer(ln)} - own)
            if bad:
                errs.append(f"市場段落的申請號不屬於本藥：{', '.join(bad[:5])}")
        has_b, has_e = s.BEGIN in sec, s.END in sec
        if has_b != has_e:
            errs.append("程式區塊標記不成對")
        if has_b and has_e:
            i, j = sec.index(s.BEGIN), sec.index(s.END)
            blk = [x for x in sec[i + 1:j] if x.strip()]
            if not e["rows"]:
                if blk != [s.NONE_LINE]:
                    errs.append("程式區塊應為「查無申請號或列名」一句（快照沒有任何申請號或列名）")
            else:
                tb = [x for x in blk if x.startswith("|")]
                show = [x for x in blk if not x.startswith("|")]
                n = len(tb) - 2
                if not tb or tb[0].strip() != s.HEAD or tb[1].strip() != s.SEP.strip():
                    errs.append("程式區塊的表頭不是程式表頭")
                elif tb[2:] != e["rows"][:n]:
                    k = next((k for k, (x, y) in enumerate(zip(tb[2:], e["rows"])) if x != y), min(n, len(e["rows"])))
                    errs.append(f"程式表第 {k + 1} 列跟快照重算的結果不同（程式表被手改或資料已更新：跑 scripts/sync_license_tables.py）")
                elif not (min(5, len(e["rows"])) <= n <= 20):
                    errs.append(f"程式表列數 {n} 不在 {min(5, len(e['rows']))}–20 之間")
                want = [s.SHOW.format(n=n, m=e["total"])] if e["total"] > n else []
                if [x.strip() for x in show] != want:
                    errs.append(f"程式區塊的 SHOW 句應為「{want[0] if want else '（無）'}」")
        elif any(x.strip() == s.HEAD for x in sec):
            errs.append("程式表沒有程式區塊標記（跑 python3 scripts/sync_license_tables.py --mark-existing）")
    fc = e.get("facts")
    if fc:
        all_rows = [r for t in _tables(lines) for r in _rows(t)]
        st = ck.status_row(SITE, all_rows)
        want_s = expected_status(fc)
        if st is not None and want_s and st[1] != want_s:
            errs.append(f"狀態列「{st[1][:50]}」≠ 事實層寫法「{want_s}」")
        cr = ck.count_row(SITE, all_rows)
        if cr is not None and (fc.get("total") is not None or fc.get("partial")):
            want_c = ck.count_text(SITE, ck.LANG.get(SITE, "en"), fc)
            if cr[1] != want_c:
                errs.append(f"張數列「{cr[1][:50]}」≠ 事實層寫法「{want_c}」")
        lic = {ck.mv2.norm_id(k): v for k, v in (fc.get("licenses") or {}).items()}
        if a is not None:
            for t in _tables(lines[a:b]):
                for code, d in ck.row_status_conflicts(SITE, _rows(t), lic):
                    errs.append(f"許可證表列的狀態跟事實相反：{d}")
    return errs


def site_problems(drugs_dir: Path | None = None) -> list[str]:
    drugs_dir = drugs_dir or ROOT / "docs" / "_drugs"
    if not snapshot():
        return ["找不到 snapshots/us_licenses.json.gz（跑 scripts/build_license_snapshot.py）"]
    out = []
    for f in sorted(drugs_dir.glob("*.md")):
        t = f.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' in t[:3000] or re.search(r"^layout:\s*id_redirect", t[:3000], re.M):
            continue
        out += [f"{f.name}：{x}" for x in page_problems(f.stem, t)]
    return out


if __name__ == "__main__":
    errs = site_problems()
    for x in errs[:50]:
        print("  ✗", x)
    print(f"許可證檢查：{'✗' if errs else '✓'} {len(errs)} 項")
    sys.exit(1 if errs else 0)

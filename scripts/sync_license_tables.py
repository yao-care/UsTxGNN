"""藥物頁「US Market Information」的許可證表由程式依證據包重排（2026-11-06，用戶決定；全程不用 AI、不改寫正文）。

起因：依成分重建（scripts/rebuild_licenses_by_ingredient.py）後，概覽表的狀態列、張數列已改成依成分比對的結果，
但許可證表還是舊收集器（依 DrugBank ID 對 NDC 產品列）時由模型寫的，列了不屬於本藥的申請號
（例：procaine 頁列 NDA050138 Bicillin C-R、potassium 頁列 5 張 potassium citrate 的 ANDA、sodium_acetate 頁列 pemetrexed）。
表格、張數列、狀態列要來自同一套比對結果，所以表格整張換成程式產生的：

- 欄位：Application / NDC | Product | Holder | Dosage form | Status
- 列：證據包 tfda.records 的順序（rebuild 的排序：有效申請在前、單方產品在前、號碼；接著是 OTC monograph／未核准類別的
  NDC 列名產品）；每個申請號一列，列名產品以 NDC 產品碼一列。
- 狀態：申請號照事實層（.claude/cache/license_facts，和狀態列、張數列同一份）的 valid／cancelled：
  有效＝「Valid」、全部產品停產＝「Discontinued in Drugs@FDA」；列名產品＝「NDC listing, no FDA application (<NDC 類別>)」。
- 列數：原表列數與 min(5, 總數) 取大，最多 20；總數（申請號數＋列名產品數，和張數列、狀態列的數字相同）多於列數時，
  表下加一句 SHOW（「Showing N of M entries …」）。新資料沒有任何申請號或列名產品時，表格換成 NONE_LINE 一句。
- 段落裡沒有表格的頁不新增表格。

哪些頁要重排（--rebuild，依成分重建時；規則寫在 needs_resync）：
  1. 表格已經是本程式產生的（表頭＝HEAD）——每次重建都照新資料重排；
  2. 表格裡有不屬於本藥的申請號（NDA／ANDA／BLA＋6 碼，不在證據包的申請號裡）；
  3. 段落正文點名本藥的申請號、但那個號碼不屬於本藥（只算沒有「另一個藥名＋as a standalone／standalone drug」這類
     明說是別的藥的句子；例：soybean_oil 頁「three allergenic-extract BLAs」）；
  4. 表格列寫的狀態跟事實層相反（號碼格夾著狀態字「NDA208743 (cancelled)」、或別欄「Not specified (valid)」；2026-11-06 起，
     判斷用 checker .claude/check_drug_page.py 的 row_status_conflicts，checker 的 M1 也擋同一種寫法）；
  5. 這次重建跟上次的證據包相比，申請號集合有變（2026-11-06，用戶決定；例 chlorpheniramine、codeine、pseudoephedrine
     多了申請號，表格卻沒觸發 1–4 而留著舊寫法）。--changed <json> 由 scripts/license_rebuild_run.py 依重建前後的證據包產生
     （{證據包鍵: {"added": [...], "dropped": [...]}}）；每次依成分重建都照這條比。
每週許可證更新（scripts/license_adapter.py 的 sync_tables）：狀態有變的藥照同一套重排（resync_tables），只改表格與 SHOW 句。
表格重排後，正文跟新事實矛盾的句子由 .claude/delete_license_sentences.py（規則＋人工清單 scripts/license_sentence_fixes.json）刪，
本程式不刪句。

用法（repo 根目錄，先在工作目錄跑 dump_license_facts）：
  python3 scripts/sync_license_tables.py --ws <工作目錄> [--dry-run] [--report out.tsv] [--changed apps_changed.json] [頁 ...]
"""
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "UsTxGNN"
SEC = "## US Market Information"
HEAD = "| Application / NDC | Product | Holder | Dosage form | Status |"
SEP = "|------|------|------|------|------|"
SHOW = "Showing {n} of {m} entries (FDA applications first, active before discontinued; NDC listings without an FDA application last)."
SHOW_RX = re.compile(r"^Showing \d+ of \d+ entries \(FDA applications first, active before discontinued; NDC listings without an FDA application last\)\.$")
NONE_LINE = "No FDA application or NDC Directory listing matching this drug was found in the data compiled for this report."
APPL = re.compile(r"\b(NDA|ANDA|BLA)\s*(\d{6})\b")
SUFFIX = " (Discontinued in Drugs@FDA)"  # 與 src/ustxgnn/collectors/us_license_match.py 相同
# 正文明說號碼是別的藥（例「Arsenic Trioxide as a standalone drug … NDA 021248」「Canakinumab as a standalone biologic … BLA 125319」）
OTHER_DRUG = re.compile(r"\bstandalone\b|\bas a separate\b", re.I)


def facts(ws):
    p = Path(ws) / ".claude/cache/license_facts" / f"{SITE}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def page_for(key):
    for stem in (key, key.replace("_", "-")):
        p = ROOT / "docs/_drugs" / f"{stem}.md"
        if p.exists():
            return p
    return None


def bundle_for(page):
    for key in (page.stem, page.stem.replace("-", "_")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return key, json.loads(f.read_text(encoding="utf-8"))
    return None, None


def _cell(x, n=70):
    """表格格子：「|」換成「/」、空白合併；太長時在字界截斷並加「…」"""
    s = " ".join(str(x or "").replace("|", "/").split())
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0] if " " in s[:n] else s[:n]
    return cut.rstrip(" ,;/-") + "…"


def _cap(x):
    x = _cell(x, 60)
    return x[:1].upper() + x[1:].lower() if x.isupper() else x


def rows_of(tf, fc):
    """證據包 tfda → (表格列, 總數)。總數＝申請號數＋列名產品數（和張數列、狀態列同一套）"""
    lic = (fc or {}).get("licenses") or {}
    out, seen = [], set()
    for r in tf.get("records") or []:
        if r.get("listing"):
            k = str(r.get("product_ndc") or "").strip()
            if not k or ("L" + k) in seen:
                continue
            seen.add("L" + k)
            cat = str(r.get("status") or "").strip().lower().replace("otc", "OTC")
            st = f"NDC listing, no FDA application ({cat})" if cat else "NDC listing, no FDA application"
            form = _cap(r.get("dosage_form")) or "Not recorded"
            out.append(f"| NDC {k} | {_cell(r.get('brand_name_en')) or 'Not recorded'} | {_cell(r.get('manufacturer'), 60) or 'Not recorded'} | {form} | {st} |")
            continue
        k = str(r.get("license_id") or "").strip()
        if not APPL.fullmatch(k) or k in seen:
            continue
        seen.add(k)
        s = lic.get(k) or ("cancelled" if str(r.get("status") or "").endswith(SUFFIX) else "valid")
        st = "Valid" if s == "valid" else "Discontinued in Drugs@FDA"
        form = "; ".join(x for x in (_cap(r.get("dosage_form")), _cap(r.get("route")).lower()) if x) or "Not recorded"
        out.append(f"| {k} | {_cell(r.get('brand_name_en')) or 'Not recorded'} | {_cell(r.get('manufacturer'), 60) or 'Not recorded'} | {form} | {st} |")
    n_app = int(tf.get("applications_total") if tf.get("applications_total") is not None else sum(1 for x in seen if not x.startswith("L")))
    n_lst = int(tf.get("listed_total") if tf.get("listed_total") is not None else sum(1 for x in seen if x.startswith("L")))
    return out, n_app + n_lst


def section(lines):
    """(段落開始, 段落結束, 表格第一行, 表格最後一行)；沒有段落或表格時對應值為 None"""
    if SEC not in lines:
        return None, None, None, None
    a = lines.index(SEC) + 1
    b = next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        return a, b, None, None
    x = y = tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    return a, b, x, y


def own_apps(tf):
    return {str(r.get("license_id") or "").strip() for r in tf.get("records") or [] if not r.get("listing")}


def app_sets(bundles_dir):
    """證據包目錄 → {證據包鍵: 申請號集合}（tfda.records 裡的 NDA／ANDA／BLA；列名產品不算）。重建前後各取一次比對（規則 5）"""
    out = {}
    for f in sorted(Path(bundles_dir).glob("*/drug_bundle.json")):
        tf = json.loads(f.read_text(encoding="utf-8")).get("tfda") or {}
        out[f.parent.name] = sorted(i for i in own_apps(tf) if APPL.fullmatch(i))
    return out


def apps_changed(after, *befores):
    """重建後的申請號集合跟（任一個）比較基準不同的證據包 → {鍵: {"added", "dropped"}}；基準裡沒有的鍵（新藥）不算"""
    out = {}
    for k, now in after.items():
        for before in befores:
            if before is None or k not in before or set(before[k]) == set(now):
                continue
            d = out.setdefault(k, {"added": set(), "dropped": set()})
            d["added"] |= set(now) - set(before[k])
            d["dropped"] |= set(before[k]) - set(now)
    return {k: {"added": sorted(v["added"]), "dropped": sorted(v["dropped"])} for k, v in sorted(out.items())}


def needs_resync(lines, tf, conflicts=None, changed=None):
    """重建時要重排的理由（空字串＝不用）。conflicts：表格列 → [(代碼, 說明)]，用 checker 的 row_status_conflicts（同一套判斷）；
    changed：這次重建申請號集合有變時為 {"added": [...], "dropped": [...]}（規則 5）"""
    a, b, x, y = section(lines)
    if x is None:
        return ""
    if lines[x].strip() == HEAD:
        return "程式產生的表格"
    if changed is not None:
        add, drop = changed.get("added") or [], changed.get("dropped") or []
        return "重建時申請號有變：" + "；".join(x for x in (
            ("新增 " + ", ".join(add[:8]) + (f" 等 {len(add)} 個" if len(add) > 8 else "")) if add else "",
            ("移除 " + ", ".join(drop[:8]) + (f" 等 {len(drop)} 個" if len(drop) > 8 else "")) if drop else "") if x)
    own = own_apps(tf)
    bad = sorted({m.group(1) + m.group(2) for l in lines[x:y + 1] for m in APPL.finditer(l)} - own)
    if bad:
        return "表格列了不屬於本藥的申請號：" + ", ".join(bad[:8])
    if conflicts:
        rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines[x + 2:y + 1]]
        hit = conflicts(rows)
        if hit:
            return "表格列的狀態字跟事實層不一致：" + "；".join(d for _, d in hit[:3])
    for l in lines[a:b]:
        if l.startswith("|") or OTHER_DRUG.search(l):
            continue
        bad = sorted({m.group(1) + m.group(2) for m in APPL.finditer(l)} - own)
        if bad:
            return "段落正文點名不屬於本藥的申請號：" + ", ".join(bad[:8])
    return ""


def render(lines, tf, fc):
    """重排段落裡的表格與 SHOW 句；回傳新的 lines（沒有表格時原樣）"""
    a, b, x, y = section(lines)
    if x is None:
        return lines
    rows, total = rows_of(tf, fc)
    after = lines[y + 1:b]
    si = next((k for k, l in enumerate(after) if SHOW_RX.match(l.strip())), None)
    if si is not None:  # 舊的 SHOW 句先拿掉（連同前面的空行），下面依新資料重加
        del after[si]
        if si > 0 and not after[si - 1].strip():
            del after[si - 1]
    if not rows:
        return lines[:x] + [NONE_LINE] + after + lines[b:]
    old_rows = max(0, y - x - 1)
    nrows = min(20, max(old_rows, min(5, len(rows))))
    table = [HEAD, SEP] + rows[:nrows]
    if total > nrows:
        after = ["", SHOW.format(n=min(nrows, len(rows)), m=total)] + after
    return lines[:x] + table + after + lines[b:]


def _load_checker(ws):
    """工作目錄的 .claude/check_drug_page.py（row_status_conflicts：checker 擋「表格列狀態字跟事實相反」的同一套判斷）；舊版沒有就不查"""
    import importlib.util
    p = Path(ws) / ".claude/check_drug_page.py"
    if not p.exists():
        return None
    s = importlib.util.spec_from_file_location("check_drug_page", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m if hasattr(m, "row_status_conflicts") else None


def resync_page(page, tf, fc):
    raw = page.read_bytes().decode("utf-8")
    crlf = "\r\n" in raw[:500]
    t = raw.replace("\r\n", "\n")
    if "layout: id_redirect" in t[:3000] or 'http-equiv="refresh"' in t[:3000]:
        return None, crlf
    new = "\n".join(render(t.split("\n"), tf, fc))
    new = re.sub(r"\n{3,}", "\n\n", new)
    return (new if new != t else None), crlf


def _write(page, new, crlf):
    page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))


def resync_tables(bundles, ws=None):
    """每週許可證更新用（scripts/license_adapter.py 的 sync_tables）：bundles＝這輪證據包狀態有變的藥。
    只重排表格與 SHOW 句，不刪句、不動其他行。回傳 [(頁, 欄位, 前值, 後值)]"""
    fs = facts(ws or ROOT.parent)
    out = []
    for key in sorted(set(bundles)):
        page = page_for(key)
        bf = ROOT / "data/bundles" / key / "drug_bundle.json"
        if page is None or not bf.exists():
            continue
        tf = json.loads(bf.read_text(encoding="utf-8")).get("tfda") or {}
        if not rows_of(tf, None)[0]:
            continue  # 沒有任何申請號或列名產品：表格換成 NONE_LINE 是正文改動，只在依成分重建時做
        old = page.read_bytes().decode("utf-8").replace("\r\n", "\n").split("\n")
        new, crlf = resync_page(page, tf, fs.get(key) or fs.get(page.stem))
        if new is None:
            continue
        _write(page, new, crlf)
        for l in difflib.unified_diff(old, new.split("\n"), lineterm="", n=0):
            if l[:1] in "+-" and not l.startswith(("+++", "---")) and l[1:].strip():
                out.append((page.stem, "許可證表（依證據包重排）", l[1:] if l[0] == "-" else "", l[1:] if l[0] == "+" else ""))
    return out


def main(argv):
    ws = Path(argv[argv.index("--ws") + 1])
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    chg_f = argv[argv.index("--changed") + 1] if "--changed" in argv else None
    only = {a for a in argv if not a.startswith("--") and a not in (str(ws), rep, chg_f)}
    changed = json.loads(Path(chg_f).read_text(encoding="utf-8")) if chg_f else {}
    fs = facts(ws)
    ck = _load_checker(ws)
    log, n = [], 0
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        key, b = bundle_for(page)
        if b is None:
            continue
        tf = b.get("tfda") or {}
        t = page.read_bytes().decode("utf-8").replace("\r\n", "\n")
        if "layout: id_redirect" in t[:3000] or 'http-equiv="refresh"' in t[:3000]:
            continue
        fc = fs.get(key) or fs.get(page.stem) or {}
        lic = {ck.mv2.norm_id(k): s for k, s in (fc.get("licenses") or {}).items()} if ck else {}
        why = needs_resync(t.split("\n"), tf, (lambda rows: ck.row_status_conflicts(SITE, rows, lic)) if ck else None, changed.get(key))
        if not why:
            continue
        new, crlf = resync_page(page, tf, fs.get(key) or fs.get(page.stem))
        rows, total = rows_of(tf, fs.get(key))
        log.append((page.stem, why, str(total), "改" if new is not None else "不變"))
        if new is not None:
            n += 1
            if not dry:
                _write(page, new, crlf)
    if rep:
        Path(rep).write_text("頁\t理由\t總數（申請號＋列名）\t結果\n" + "\n".join("\t".join(x) for x in log) + "\n", encoding="utf-8")
    print(f"許可證表重排：{n} 頁（檢查到 {len(log)} 頁需要依新資料重排）")


if __name__ == "__main__":
    main(sys.argv[1:])

"""藥物頁「US Market Information」的許可證表由程式依證據包重排（2026-11-06，用戶決定；全程不用 AI、不改寫正文）。

起因：依成分重建（scripts/rebuild_licenses_by_ingredient.py）後，概覽表的狀態列、張數列已改成依成分比對的結果，
但許可證表還是舊收集器（依 DrugBank ID 對 NDC 產品列）時由模型寫的，列了不屬於本藥的申請號
（例：procaine 頁列 NDA050138 Bicillin C-R、potassium 頁列 5 張 potassium citrate 的 ANDA、sodium_acetate 頁列 pemetrexed）。
表格、張數列、狀態列要來自同一套比對結果，所以表格整張換成程式產生的：

- 欄位：Application / NDC | Product | Holder | Dosage form | Status
- 列：證據包 tfda.records 的順序（rebuild 的排序：有效申請在前、單方產品在前、號碼；接著是 OTC monograph／未核准類別的
  NDC 列名產品）；每個申請號一列，列名產品以 NDC 產品碼一列。
- 狀態：申請號照事實層（.claude/cache/license_facts，和狀態列、張數列同一份）的 valid／cancelled：
  有效＝「Valid」、全部產品停產＝「Discontinued in Drugs@FDA」、Purple Book 許可已撤銷（Drugs@FDA 沒有的 BLA，紀錄 status
  以 REVOKED 結尾；2026-11-17）＝「License revoked in Purple Book」；列名產品＝「NDC listing, no FDA application (<NDC 類別>)」。
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

程式區塊標記（2026-11-12 起，本站查核機制）：程式產生的表格（連同 SHOW 句，或 NONE_LINE）前後各一行
「<!-- licenses:begin -->」「<!-- licenses:end -->」（前後空行），讓查核紀錄、刪句工具與 gate 分得出哪些字是程式寫的。
render 每次都重畫這兩行；--mark-existing 只替表頭＝HEAD 的現有程式表補標記、不改內容。
gate（scripts/check_seo_docs.py）依 snapshots/us_licenses.json.gz 檢查程式表＝快照重算的結果（src/ustxgnn/regulatory/licenses.py）。

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
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
APPL = re.compile(r"\b(NDA|ANDA|BLA)\s*(\d{6})\b")
SUFFIX = " (Discontinued in Drugs@FDA)"  # 與 src/ustxgnn/collectors/us_license_match.py 相同
REVOKED = " (License revoked in Purple Book)"  # 與 scripts/license_adapter.py 相同（Drugs@FDA 沒有的 BLA，2026-11-17）
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
        rs = str(r.get("status") or "")
        s = lic.get(k) or ("cancelled" if rs.endswith((SUFFIX, REVOKED)) else "valid")
        st = "Valid" if s == "valid" else "License revoked in Purple Book" if rs.endswith(REVOKED) else "Discontinued in Drugs@FDA"
        form = "; ".join(x for x in (_cap(r.get("dosage_form")), _cap(r.get("route")).lower()) if x) or "Not recorded"
        out.append(f"| {k} | {_cell(r.get('brand_name_en')) or 'Not recorded'} | {_cell(r.get('manufacturer'), 60) or 'Not recorded'} | {form} | {st} |")
    n_app = int(tf.get("applications_total") if tf.get("applications_total") is not None else sum(1 for x in seen if not x.startswith("L")))
    n_lst = int(tf.get("listed_total") if tf.get("listed_total") is not None else sum(1 for x in seen if x.startswith("L")))
    return out, n_app + n_lst


def strip_marks(lines):
    """拿掉程式區塊標記行（連同緊接在後的空行），重畫前用"""
    return [l for l in lines if l.strip() not in (BEGIN, END)]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


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


def _before(lines, x):
    """表格前的行，去掉結尾的空行後補一個空行（標記行前面要空行）"""
    head = list(lines[:x])
    while head and not head[-1].strip():
        head.pop()
    return head + [""]


def _after(after):
    """表格（或 SHOW 句）後的行：開頭的空行去掉，END 之後補一個空行"""
    after = list(after)
    while after and not after[0].strip():
        after.pop(0)
    return [""] + after


# 2026-11-24 第三輪（用戶決定，比照 JpTxGNN 第二輪）：公開頁沒有「## US Market Information」段落、但證據包有申請號或列名產品的，
# 補一個段落放程式表（列數同新表規則：最多 5 列，其餘寫 SHOW 句）。位置：「## Safety Considerations」之前；沒有就
# 「## Conclusion and Next Steps」「## Review Log」「## Disclaimer」之前。known_use_pages 以前退回英文寫的「## Market information」
# 標題（dexchlorpheniramine）改成本站標題、表照常換成程式表。noindex 頁與證據包沒有紀錄的頁不補。
ALT_SEC = "## Market information"
ADD_BEFORE = ("Safety Considerations", "Conclusion and Next Steps", "Review Log", "Disclaimer")


def is_public(text):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    return not re.search(r"^noindex:\s*true", fm, re.M)


def needs_section(text):
    lines = text.replace("\r\n", "\n").split("\n")
    return SEC not in lines and is_public(text)


def add_section(lines, tf):
    """段落標題＋空表頭（之後由 render 換成程式表）；不補時原樣回傳"""
    if SEC in lines or not rows_of(tf, None)[0]:
        return lines
    if ALT_SEC in lines:
        lines = list(lines)
        lines[lines.index(ALT_SEC)] = SEC
        return lines
    heads = {m.group(1): i for i, l in enumerate(lines) for m in [re.match(r"^## (.+?)\s*$", l)] if m}
    at = next((heads[h] for h in ADD_BEFORE if h in heads), None)
    if at is None:
        return lines
    k = at - 1
    while k > 0 and not lines[k].strip():
        k -= 1
    if lines[k].strip() == "<!-- review:begin log -->":  # 查核紀錄段的標題在 log 區塊裡：段落放在區塊之前
        at = k
    return lines[:at] + [SEC, "", HEAD, SEP, ""] + lines[at:]


def render(lines, tf, fc):
    """重排段落裡的表格與 SHOW 句，前後加程式區塊標記；回傳新的 lines（沒有表格時原樣）"""
    lines = strip_marks(lines)
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
        return _before(lines, x) + wrap([NONE_LINE]) + _after(after) + lines[b:]
    old_rows = max(0, y - x - 1)
    nrows = min(20, max(old_rows, min(5, len(rows))))
    block = [HEAD, SEP] + rows[:nrows]
    if total > nrows:
        block += ["", SHOW.format(n=min(nrows, len(rows)), m=total)]
    return _before(lines, x) + wrap(block) + _after(after) + lines[b:]


def mark_existing(lines):
    """表頭＝HEAD 的現有程式表（連同緊接的 SHOW 句）補上標記，內容一字不改；已有標記或不是程式表就原樣"""
    if BEGIN in lines:
        return lines
    a, b, x, y = section(lines)
    if x is None or lines[x].strip() != HEAD:
        if a is not None and x is None and NONE_LINE in lines[a:b]:
            k = lines.index(NONE_LINE, a)
            return _before(lines, k) + wrap([NONE_LINE]) + _after(lines[k + 1:b]) + lines[b:]
        return lines
    block = lines[x:y + 1]
    rest = lines[y + 1:b]
    k = 0
    while k < len(rest) and not rest[k].strip():
        k += 1
    if k < len(rest) and SHOW_RX.match(rest[k].strip()):
        block += ["", rest[k]]
        rest = rest[k + 1:]
    return _before(lines, x) + wrap(block) + _after(rest) + lines[b:]


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
    ls = t.split("\n")
    if needs_section(t):
        ls = add_section(ls, tf)
    new = "\n".join(render(ls, tf, fc))
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


def _snap_facts():
    """snapshots/us_licenses.json.gz 的 facts（頁 stem → 事實層那一筆）；沒有快照就是空的"""
    import gzip
    p = ROOT / "snapshots" / "us_licenses.json.gz"
    if not p.exists():
        return {}
    d = json.loads(gzip.open(p).read().decode("utf-8")).get("drugs") or {}
    return {k: v.get("facts") for k, v in d.items() if v.get("facts")}


def run(only=None, dry=False, ws=None):
    """已有程式區塊（BEGIN…END）的頁，依證據包（data/bundles）＋事實層重排程式許可證表，回傳改到的頁檔名（xxx.md）。
    2026-11-24（用戶決定「許可證張數與狀態不再每週過期」）：scripts/build_license_snapshot.py 寫完快照、scripts/apply_drug_reviews.py
    （非 --check）結尾都會呼叫，讓所有程式表（不只這輪狀態有變的藥）都跟著證據包與快照。
    事實層：給 ws 用 <ws>/.claude/cache/license_facts，否則用快照的 facts。沒有 data/bundles 的環境（gate、只有快照）什麼都不做。
    沒有任何申請號或列名產品時不換成 NONE_LINE（那是正文改動，只在依成分重建時做；同 resync_tables）。
    只動程式區塊（表格列、SHOW 句、標記），不動其他行。"""
    if not (ROOT / "data/bundles").is_dir():
        return []
    only = {x[:-3] if str(x).endswith(".md") else x for x in only} if only else None
    fs = facts(ws) if ws else _snap_facts()
    out = []
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        raw = page.read_bytes().decode("utf-8")
        if BEGIN not in raw and not needs_section(raw):
            continue
        key, b = bundle_for(page)
        if b is None:
            continue
        tf = b.get("tfda") or {}
        if not rows_of(tf, None)[0]:
            continue
        new, crlf = resync_page(page, tf, fs.get(key) or fs.get(page.stem))
        if new is None:
            continue
        out.append(page.name)
        if not dry:
            _write(page, new, crlf)
    return out


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊（BEGIN…END）移植到新頁的市場段落，取代新頁模型寫的
    第一張表（連同緊接的 SHOW 句）；新頁段落沒有表時接在段落第一段之後。舊頁沒有程式區塊就原樣回傳新頁。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = strip_marks(new_text.split("\n"))
    a, b, x, y = section(lines)
    if a is None:
        return new_text
    if x is None:
        k = next((k for k in range(a + 1, b) if not lines[k].strip() and lines[k - 1].strip()), a)
        out = lines[:k] + [""] + blk + [""] + lines[k:]
    else:
        rest = lines[y + 1:b]
        k = 0
        while k < len(rest) and not rest[k].strip():
            k += 1
        if k < len(rest) and SHOW_RX.match(rest[k].strip()):
            rest = rest[k + 1:]
        out = _before(lines, x) + blk + _after(rest) + lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


# ---- 2026-11-24（用戶決定，第二輪）：AI 自由格式許可證表全部換成程式表（--migrate） ----
# 市場段落裡還是模型寫的許可證表（表頭 Authorization Number…／Licence…）的頁，第一張表換成程式表；段落裡沒有表的公開頁在段落第一段後補程式表。
# 換表時一併拿掉只講「舊表列了幾筆／下面列了幾筆／清單可能不完整」的句子（CAPTION_D：段落內任何位置；CAPTION_P：只限緊鄰舊表的上一行／下一行），
# 查核紀錄的更正文字與錨點所在的句子不動；段落裡第二張同樣表頭的 AI 許可證表（ferumoxytol 重複一次）一併拿掉。
# 錨在拿掉的文字上、新頁面也找不到的查核紀錄標 superseded（紀錄保留）。
NUMW = r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty)"
CAPTION_D = re.compile(
    r"^\*?(?:"
    rf"(?:Only )?(?:the )?(?:first |main )?{NUMW}?\s*(?:main |representative )?(?:ones |entries |authori[sz]ations |licen[cs]es |records )?(?:are |is )?(?:listed|shown)(?: below| above| here)?"
    rf"|(?:The )?{NUMW} (?:main |representative )?(?:ones |entries |authori[sz]ations |licen[cs]es |records )?(?:below )?are (?:representative|listed|shown)(?: below| above| here)?"
    rf"|The (?:first |main )?{NUMW}? ?(?:main )?(?:ones|entries|authori[sz]ations|licen[cs]es|records) are (?:listed|shown)(?: below| above| here)?"
    rf"|The main ones are (?:shown|listed) below"
    rf"|Up to {NUMW} are listed below"
    rf"|The table shows (?:the first )?{NUMW}(?: of them| licen[cs]es)?"
    rf"|The list below shows {NUMW} of (?:them|the {NUMW} licen[cs]es on record|the licen[cs]es on record(?: and may be partial)?)"
    rf"|The list shows {NUMW} of (?:at least )?{NUMW} records(?: and may be partial)?"
    rf"|Showing {NUMW} of {NUMW} records; the list may be partial"
    rf"|{NUMW} examples|Main records|Examples"
    r"|The records compiled for this report are listed below and may be partial"
    r"|Only part of the licen[cs]e list is held in the data; the list may be incomplete"
    r"|No licen[cs]e table can be (?:generated|displayed)"
    r")\s*[.:]\*?$", re.I)
CAPTION_P = re.compile(
    r"^\*?(?:The |This )?(?:licen[cs]e |authori[sz]ation |record )?(?:list|records|licen[cs]e records|list of (?:records|approvals))(?: below)?"
    r"(?: compiled for this report)? (?:may be|is) (?:partial|incomplete)\.\*?$", re.I)
SPLIT = re.compile(r"(?<=[.!?:])\s+(?=[A-Z*\[(\"])")
AI_HEAD = re.compile(r"^\|\s*(?:Authori[sz]ation Number|Licen[cs]e)\s*\|")
SUPERSEDED_BY = "Program-generated license table (scripts/sync_license_tables.py, 2026-11-24, from Drugs@FDA / NDC Directory data)"


def _trim(line, protect, pats):
    """行裡整句符合 pats 的說明句拿掉：回 (新行, 拿掉的句子)"""
    if not line.strip() or line.startswith(("|", "#", "<!--", "---", ">", "-", "*  ")):
        return line, []
    out, gone = [], []
    for x in SPLIT.split(line.strip()):
        if any(p and (x.strip() in p or p in x) for p in protect):
            out.append(x)
            continue
        if any(q.match(x.strip()) for q in pats):
            gone.append(x.strip())
            continue
        out.append(x)
    return (" ".join(out), gone) if gone else (line, [])


def migrate_text(t, tf, fc, protect=(), add_missing=False):
    """回 (新內容或 None, 拿掉的文字)。只動市場段落：第一張 AI 許可證表換成程式表、說明句、重複的第二張 AI 表"""
    lines = strip_marks(t.split("\n"))
    if BEGIN in t:
        return None, ""
    a, b, x, y = section(lines)
    if a is None:
        return None, ""
    rows, total = rows_of(tf, fc)
    gone = []
    if x is None:
        if not add_missing or not rows:
            return None, ""
        k = next((k for k in range(a + 1, b) if not lines[k].strip() and lines[k - 1].strip()), b)
        nrows = min(20, min(5, len(rows)))
        block = [HEAD, SEP] + rows[:nrows] + (["", SHOW.format(n=nrows, m=total)] if total > nrows else [])
        lines = lines[:k] + [""] + wrap(block) + [""] + lines[k:]
    else:
        if not AI_HEAD.match(lines[x]):
            return None, ""
        gone += lines[x:y + 1]
        # 緊鄰舊表的上一行／下一行：只講清單可能不完整的句子
        for k0, step in ((x - 1, -1), (y + 1, 1)):
            k = k0
            while a <= k < b and not lines[k].strip():
                k += step
            if a <= k < b:
                nl, cap = _trim(lines[k], protect, (CAPTION_P, CAPTION_D))
                if cap:
                    lines[k] = nl
                    gone += cap
        # 第二張同表頭的 AI 許可證表（重複）
        tb2 = [k for k in range(y + 1, b) if AI_HEAD.match(lines[k])]
        for k in reversed(tb2):
            e = k
            while e + 1 < b and lines[e + 1].startswith("|"):
                e += 1
            gone += lines[k:e + 1]
            del lines[k:e + 1]
        if not rows:
            lines = _before(lines, x) + wrap([NONE_LINE]) + _after(lines[y + 1:]) 
        else:
            old_rows = max(0, y - x - 1)
            nrows = min(20, max(old_rows, min(5, len(rows))))
            block = [HEAD, SEP] + rows[:nrows] + (["", SHOW.format(n=min(nrows, len(rows)), m=total)] if total > nrows else [])
            lines = _before(lines, x) + wrap(block) + _after(lines[y + 1:])
    # 段落內（程式區塊外）講舊表顯示筆數的句子
    a, b, _, _ = section(lines)
    i0, i1 = lines.index(BEGIN, a), lines.index(END, a)
    for k in range(a, b):
        if i0 <= k <= i1:
            continue
        nl, cap = _trim(lines[k], protect, (CAPTION_D,))
        if cap:
            lines[k] = nl
            gone += cap
    new = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    return (new if new != t else None), "\n".join(gone)


def _protect():
    out = {}
    f = ROOT / "docs/_data/drug_reviews.json"
    for r in json.loads(f.read_text(encoding="utf-8")).get("records", []):
        if r.get("status"):
            continue
        out.setdefault(r["file"][:-3], []).extend(x.strip() for x in (r.get("replacement"), r.get("anchor")) if x and x.strip())
    return out


def supersede(removed_by_page, today=None):
    """--migrate 後：錨在拿掉的文字上、新頁面上也找不到的查核紀錄標 superseded（紀錄保留）。回傳標記的 id"""
    import datetime as dt
    data = ROOT / "docs/_data/drug_reviews.json"
    doc = json.loads(data.read_text(encoding="utf-8"))
    today = today or dt.date.today().isoformat()
    marked = []
    for r in doc["records"]:
        stem = r["file"][:-3]
        gone = removed_by_page.get(stem)
        if not gone or r.get("status") or r.get("action") not in ("correct", "annotate", "rereview"):
            continue
        page = (ROOT / "docs/_drugs" / r["file"]).read_text(encoding="utf-8")
        page = re.sub(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", "", page, flags=re.S)
        page = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), "", page, flags=re.S)
        keys = [x for x in (r.get("anchor"), r.get("replacement"), r.get("claim")) if x and x.strip()]
        loc = r.get("anchor") or (r.get("replacement") if r["action"] == "correct" else r.get("claim")) or r.get("claim")
        if loc and loc.strip() and loc in page:
            continue
        gl = [g.strip() for g in gone.split("\n") if g.strip()]
        if any(k.strip() in gone or any(g in k for g in gl) for k in keys):
            r["status"] = "superseded"
            r["superseded_by"] = SUPERSEDED_BY
            r["superseded_on"] = today
            marked.append(r["id"])
    if marked:
        data.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return marked


def migrate(argv):
    dry = "--dry-run" in argv
    ws = Path(argv[argv.index("--ws") + 1]) if "--ws" in argv else None
    only = {a for a in argv if not a.startswith("--") and (ws is None or a != str(ws))}
    fs = facts(ws) if ws else _snap_facts()
    prot = _protect()
    removed, n, add = {}, 0, 0
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        raw = page.read_bytes().decode("utf-8")
        crlf = "\r\n" in raw[:500]
        t = raw.replace("\r\n", "\n")
        h = t[:3000]
        if "layout: id_redirect" in h or 'http-equiv="refresh"' in h:
            continue
        key, b = bundle_for(page)
        if b is None:
            continue
        public = not re.search(r"^noindex:\s*true", h, re.M)
        new, gone = migrate_text(t, b.get("tfda") or {}, fs.get(key) or fs.get(page.stem), prot.get(page.stem, ()), add_missing=public)
        if new is None:
            continue
        n += 1
        if not gone:
            add += 1
        removed[page.stem] = gone
        if dry:
            print(f"== {page.stem}\n" + "\n".join("  - " + g for g in gone.split("\n") if g and not g.startswith("|")))
        else:
            _write(page, new, crlf)
    print(f"AI 許可證表換成程式表：{n} 頁（其中補表 {add} 頁）")
    if not dry:
        ids = supersede(removed)
        print(f"錨在舊表／說明句上的查核紀錄標 superseded：{len(ids)} 筆 {ids[:20]}")
    return removed


def main(argv):
    if "--migrate" in argv:
        migrate(argv)
        return
    if "--mark-existing" in argv:
        n = 0
        for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
            raw = page.read_bytes().decode("utf-8")
            crlf = "\r\n" in raw[:500]
            t = raw.replace("\r\n", "\n")
            if "layout: id_redirect" in t[:3000] or 'http-equiv="refresh"' in t[:3000]:
                continue
            new = re.sub(r"\n{3,}", "\n\n", "\n".join(mark_existing(t.split("\n"))))
            if BEGIN in new and BEGIN not in t:  # 只寫入真的補了標記的頁（不為了空行正規化改檔）
                n += 1
                if "--dry-run" not in argv:
                    _write(page, new, crlf)
        print(f"程式區塊標記：補上 {n} 頁")
        return
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

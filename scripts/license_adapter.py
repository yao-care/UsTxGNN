"""US（FDA Drugs@FDA）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：openFDA 的 Drugs@FDA 全量檔 https://download.open.fda.gov/drug/drugsfda/drug-drugsfda-0001-of-0001.json.zip（免金鑰）：
  results[].application_number（NDA／ANDA／BLA＋6 碼）、products[].marketing_status（Prescription／Over-the-counter／Discontinued／None (Tentative Approval)）。
  （2026-10-30 起不用 fda.gov/media/89850：fda.gov 會把 GitHub runner 的 IP 判成濫用。）
證據包紀錄 license_id 是 NDA／ANDA／BLA＋6 碼申請號，status 是 NDC 的 marketing category（NDA、ANDA…）。
只處理 NDA／ANDA／BLA 申請號；OTC monograph（M…）、未核准類別等沒有申請號的紀錄不在 Drugs@FDA，不處理。
對應：該申請所有產品都是 Discontinued → status＝「<原類別> (Discontinued in Drugs@FDA)」（reviewer 的 discontinu 字樣算註銷）；
仍有處方或 OTC 產品 → 還原為原類別；只有 4（暫定核准）→ 不動。新檔沒有的申請號保留原狀態。
2026-11-17（用戶要求確認「新資料查不到」的申請號）：openFDA Drugs@FDA 只收 CDER 的申請，CBER 的 BLA（疫苗、血液製劑、過敏原、
細胞與基因治療）與少數 NDC 上引用、Drugs@FDA 沒有的舊 ANDA 號碼都不在檔內（11-17 排程 135 張，91 張 BLA）。
Drugs@FDA 沒有的申請號另查兩份 FDA 現行清單（Drugs@FDA 有的照舊只看 Drugs@FDA）：
  1. Purple Book 月檔（purplebooksearch.fda.gov/downloads 最新一期 CSV；CDER＋CBER 的生物製劑許可，欄位 Marketing Status、Licensure）：
     許可全部 Revoked／Voluntarily Revoked、沒有 Rx／OTC 產品 → status＝「<原類別> (License revoked in Purple Book)」（revok 字樣算註銷）；
     有 Rx／OTC 而且 Licensed 的產品 → 還原原類別；全部 Disc 但仍 Licensed → 跟 Drugs@FDA 全部停產同樣處理（SUFFIX）；其他不動。
  2. openFDA NDC Directory（download.open.fda.gov/drug/ndc，現行列名產品，application_number 欄）：有現行成品列名（finished、
     marketing_end_date 空白或未到）→ 還原原類別（Purple Book 沒有的才看這份）。NDC 列名不是核准狀態，列名都已結束時不推定註銷。
  兩份都是選用：下載失敗就略過（只少了這部分的涵蓋，不影響 Drugs@FDA 的判定）。三份都沒有的申請號照舊保留原狀態、列為查不到，
  不推定註銷（Drugs@FDA 不含 CBER，Purple Book 不含部分過敏原 BLA，NDC 列名不等於許可），所以本站沒有 confirmed_absent。
  OTC monograph（M0xx／part 3xx）等沒有申請號的紀錄不受影響（record_id 只認 NDA／ANDA／BLA）。
"""
import io
import json
import re
import time
import zipfile

import requests

RAW_FILE = "raw/drugsfda_appl_status.json"
URL = "https://download.open.fda.gov/drug/drugsfda/drug-drugsfda-0001-of-0001.json.zip"  # openFDA；fda.gov 會把 GitHub runner 判成濫用
SUFFIX = " (Discontinued in Drugs@FDA)"
APPL = re.compile(r"^(NDA|ANDA|BLA)(\d{6})$")
REVOKED = " (License revoked in Purple Book)"   # scripts/sync_license_tables.py 依這個字尾寫表格狀態
PB_PAGE = "https://purplebooksearch.fda.gov/downloads"
PB_MIN = 500       # Purple Book 的 BLA 少於這個數＝下載或格式有問題，略過
NDC_URL = "https://download.open.fda.gov/drug/ndc/drug-ndc-0001-of-0001.json.zip"
NDC_MIN = 8000     # 有現行列名的申請號少於這個數＝下載或格式有問題，略過


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=300, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
            r.raise_for_status()
            z = zipfile.ZipFile(io.BytesIO(r.content))
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    data = json.loads(z.read(z.namelist()[0]))
    out = []
    for x in data.get("results", []):
        a = (x.get("application_number") or "").strip()
        st = sorted({(p.get("marketing_status") or "").strip() for p in x.get("products") or []})
        if APPL.match(a) and st:
            out.append({"appl": a, "ids": st})
    have = {r["appl"] for r in out}
    pb = _fetch_purplebook()
    out += [r for r in pb if r["appl"] not in have]
    have |= {r["appl"] for r in pb}
    out += [r for r in _fetch_ndc() if r["appl"] not in have]
    return out


def _get(url, timeout=300):
    last = None
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=timeout, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
            r.raise_for_status()
            return r
        except Exception as e:
            last = e
            time.sleep(10 * (attempt + 1))
    raise last


MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]


def _fetch_purplebook():
    """Purple Book 最新月檔 → [{appl: BLAnnnnnn, ids: [「<Marketing Status>|<Licensure>」…], src: purplebook}]；失敗回空清單"""
    import csv
    try:
        page = _get(PB_PAGE, 120).text
        cands = []
        for m in re.finditer(r'(https://[^"\']+/PurpleBook/(\d{4})/purplebook-search-(\w+)-data-download\.csv)', page):
            mo = m.group(3).lower()
            if mo in MONTHS:
                cands.append((int(m.group(2)), MONTHS.index(mo), m.group(1)))
        if not cands:
            raise RuntimeError("下載頁找不到月檔 CSV")
        url = max(cands)[2]
        rows = list(csv.reader(io.StringIO(_get(url, 180).content.decode("utf-8", errors="replace"))))
    except Exception as e:
        print(f"Purple Book 下載失敗，略過（Drugs@FDA 沒有的 BLA 維持原狀態）：{e}")
        return []
    head = next((r for r in rows if "BLA Number" in r and "Licensure" in r), None)
    if not head:
        print("Purple Book 找不到表頭，略過")
        return []
    ib, im, il = head.index("BLA Number"), head.index("Marketing Status"), head.index("Licensure")
    st = {}
    for r in rows:
        if len(r) > max(ib, im, il) and r[ib].strip().isdigit():
            st.setdefault("BLA" + r[ib].strip().zfill(6), set()).add(f"{r[im].strip()}|{r[il].strip()}")
    if len(st) < PB_MIN:
        print(f"Purple Book 只有 {len(st)} 個 BLA，疑似格式改變，略過")
        return []
    return [{"appl": a, "ids": sorted(v), "src": "purplebook"} for a, v in st.items()]


def _fetch_ndc():
    """openFDA NDC Directory → 有現行成品列名的申請號 [{appl, ids: ["NDC listed"], src: ndc}]；失敗回空清單"""
    try:
        z = zipfile.ZipFile(io.BytesIO(_get(NDC_URL).content))
        data = json.loads(z.read(z.namelist()[0])).get("results", [])
    except Exception as e:
        print(f"openFDA NDC 下載失敗，略過（Drugs@FDA 沒有的申請號維持原狀態）：{e}")
        return []
    today = time.strftime("%Y%m%d")
    ok = {(x.get("application_number") or "").strip() for x in data
          if x.get("finished") and (x.get("marketing_end_date") or "99999999") >= today}
    ok = {a for a in ok if APPL.match(a)}
    if len(ok) < NDC_MIN:
        print(f"openFDA NDC 只有 {len(ok)} 個申請號，疑似格式改變，略過")
        return []
    return [{"appl": a, "ids": ["NDC listed"], "src": "ndc"} for a in sorted(ok)]


def validate(new, old):
    p = []
    if len(new) < 15000:
        p.append(f"只解析出 {len(new)} 個申請號，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    idx = {}
    for r in new:  # fetch() 的順序：Drugs@FDA、Purple Book（Drugs@FDA 沒有的）、NDC（前兩份都沒有的）
        s = set(r["ids"])
        src = r.get("src")
        if src == "purplebook":
            mk = {x.split("|")[0].rstrip("*") for x in s}
            lic = {x.split("|")[1] for x in s}
            if all("Revoked" in x for x in lic) and not mk & {"Rx", "OTC"}:
                v = "revoked"
            elif any(x.split("|")[0] in ("Rx", "OTC") and x.endswith("|Licensed") for x in s):
                v = "active"
            elif mk == {"Disc"} and lic == {"Licensed"}:
                v = "discontinued"
            else:
                v = "other"
        elif src == "ndc":
            v = "active"
        else:
            v = "active" if s & {"Prescription", "Over-the-counter"} else "discontinued" if s == {"Discontinued"} else "other"
        idx.setdefault(r["appl"], v)
    return idx


def record_id(rec):
    k = str(rec.get("license_id") or "").strip()
    return k if APPL.match(k) else ""


def update(rec, new):
    old = rec.get("status") or ""
    base = old
    for suf in (SUFFIX, REVOKED):
        if base.endswith(suf):
            base = base[: -len(suf)]
    want = (base + SUFFIX if new == "discontinued" else base + REVOKED if new == "revoked"
            else base if new == "active" else old)
    if want == old:
        return False
    rec["status"] = want
    return True


# 每週許可證更新（license_refresh_20261029.py 3b 自我檢查）另外允許改的非表格行：許可證表下程式產生的「Showing N of M entries …」
# （狀態有變、表格重排後要跟著改）與它前後的空行。寫法與 scripts/sync_license_tables.py 的 SHOW 相同。
# 2026-11-12 起程式表前後有 <!-- licenses:begin/end --> 標記（本站查核機制），重排時會重畫，也要允許。
PAGE_NOTE = (r"^(Showing \d+ of \d+ entries \(FDA applications first, active before discontinued; "
             r"NDC listings without an FDA application last\)\.|<!-- licenses:(begin|end) -->)$")


def sync_tables(site_root, bundles):
    """狀態有變的藥：「US Market Information」的許可證表依證據包重排（有效在前），狀態照事實層；SHOW 句跟著改
    （2026-11-06，用戶決定；規則見 scripts/sync_license_tables.py 的 resync_tables）。回傳 [(頁, 欄位, 前值, 後值)]"""
    import importlib.util
    from pathlib import Path
    p = Path(site_root) / "scripts/sync_license_tables.py"
    s = importlib.util.spec_from_file_location("sync_license_tables", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m.resync_tables(bundles, ws=Path(site_root).parent)

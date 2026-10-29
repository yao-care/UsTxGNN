"""US（FDA Drugs@FDA）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：openFDA 的 Drugs@FDA 全量檔 https://download.open.fda.gov/drug/drugsfda/drug-drugsfda-0001-of-0001.json.zip（免金鑰）：
  results[].application_number（NDA／ANDA／BLA＋6 碼）、products[].marketing_status（Prescription／Over-the-counter／Discontinued／None (Tentative Approval)）。
  （2026-10-30 起不用 fda.gov/media/89850：fda.gov 會把 GitHub runner 的 IP 判成濫用。）
證據包紀錄 license_id 是 NDA／ANDA／BLA＋6 碼申請號，status 是 NDC 的 marketing category（NDA、ANDA…）。
只處理 NDA／ANDA／BLA 申請號；OTC monograph（M…）、未核准類別等沒有申請號的紀錄不在 Drugs@FDA，不處理。
對應：該申請所有產品都是 Discontinued → status＝「<原類別> (Discontinued in Drugs@FDA)」（reviewer 的 discontinu 字樣算註銷）；
仍有處方或 OTC 產品 → 還原為原類別；只有 4（暫定核准）→ 不動。新檔沒有的申請號保留原狀態。
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
    return out


def validate(new, old):
    p = []
    if len(new) < 15000:
        p.append(f"只解析出 {len(new)} 個申請號，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    idx = {}
    for r in new:
        s = set(r["ids"])
        idx[r["appl"]] = "active" if s & {"Prescription", "Over-the-counter"} else "discontinued" if s == {"Discontinued"} else "other"
    return idx


def record_id(rec):
    k = str(rec.get("license_id") or "").strip()
    return k if APPL.match(k) else ""


def update(rec, new):
    old = rec.get("status") or ""
    base = old[: -len(SUFFIX)] if old.endswith(SUFFIX) else old
    want = base + SUFFIX if new == "discontinued" else base if new == "active" else old
    if want == old:
        return False
    rec["status"] = want
    return True

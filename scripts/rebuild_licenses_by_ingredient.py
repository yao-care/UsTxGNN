"""US 依成分重建證據包的許可證紀錄（2026-11-05，用戶核准；全程不用 AI；做法比照 Za／Kr／My）。

原收集器（collectors/usfda.py）依 DrugBank ID 對 NDC 產品列、截 20 筆，複方頁會把「只含其中一個成分」的產品算進來
（例：10 成分順勢療法複方頁的「許可」是 balsalazide、pemetrexed 等單方產品），概覽寫成 Marketed；
單方頁也只收到 NDC 產品列裡的一兩個申請號（mycophenolic acid 只有 1 張已停產的 ANDA，Myfortic 與其他 ANDA 都沒收）。

1. 來源
   - FDA 核准申請：openFDA 的 Drugs@FDA 全量檔（license_adapter.URL，重建前重新下載，存 data/raw/drugsfda_openfda.zip；
     --skip-download 用已存的檔）。每個申請號（NDA／ANDA／BLA）的產品成分（products[].active_ingredients）與上市狀態。
     狀態：有處方或 OTC 產品＝有效（原類別，例「NDA」）；全部產品 Discontinued＝「<類別> (Discontinued in Drugs@FDA)」；
     只有暫定核准（None (Tentative Approval)）的申請不能上市，不收（列進報告）。
   - Drugs@FDA 沒有的申請號（CBER 的 BLA 等）與 OTC monograph／未核准類別的產品：本站 NDC 產品清單 data/raw/us_fda_drugs.json
     （process_fda_data.py 從 FDA NDC Directory 產生）。前者照 NDC 的類別當有效申請；後者是「列名」（listing），不是 FDA 核准，
     另外計數（listed_total），不算有效申請。
2. 比對（成分名先去掉鹽類／酯類／水合物字尾；整個成分名都是鹽類字時保留原名，例 sodium chloride）
   - 複方頁（證據包 drug.inn 以「;」分隔多個成分）：產品的成分組合要跟本頁完全相同才收。
   - 單方頁：產品成分含本藥就收（含複方產品，與原收集器相同）；「-ic acid」與「-ate」視為同一成分
     （mycophenolic acid＝mycophenolate sodium、valproic acid＝valproate）。頁名本身帶鹽類時只收同一個鹽。
3. 寫回證據包 tfda：records＝全部申請號（每個申請號一筆，有效的排前面、單方產品排前面）＋最多 20 筆列名產品
   （listing: true）；listed_total＝列名產品數（不重複 NDC 產品碼）；total_matches＝申請號數＋listed_total；
   原紀錄整批換掉（原紀錄來源錯配，留著會把別的藥算進來）。
   reviewer._local_regulatory 依 listing 欄位把申請號與列名分開算（概覽「FDA 核准申請 X／N；OTC monograph／未核准列名 K」）。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--skip-download] [--dry-run] [--report out.tsv] [頁 ...]
"""
import io
import json
import re
import sys
import zipfile
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data/raw"
ZIP = RAW / "drugsfda_openfda.zip"
sys.path.insert(0, str(ROOT / "scripts"))
import license_adapter as ad  # noqa: E402

SALT = (r"hydrochloride|hcl|hydrobromide|besylate|besilate|maleate|mesylate|mesilate|tartrate|bitartrate|fumarate|hemifumarate|succinate|"
        r"citrate|acetate|diacetate|dipropionate|propionate|valerate|butyrate|phosphate|sulfate|sulphate|nitrate|lactate|gluconate|palmitate|"
        r"hydrate|monohydrate|dihydrate|trihydrate|tetrahydrate|pentahydrate|hexahydrate|heptahydrate|sesquihydrate|hemihydrate|anhydrous|hydrous|"
        r"sodium|potassium|calcium|magnesium|disodium|dipotassium|cilexetil|axetil|medoxomil|dihydrochloride|bromide|chloride|iodide|"
        r"tosylate|edisylate|pamoate|embonate|stearate|oleate|mandelate|camsylate|xinafoate|furoate|aceponate|hyclate|trometamol|tromethamine|"
        r"arginine|lysine|meglumine|olamine|erbumine|tert butylamine|benzathine|procaine|esylate|napadisilate|hemisulfate|bisulfate|"
        r"monosodium|trisodium|usp|nf|decanoate|enanthate|cypionate|undecanoate|oxalate|dimeglumine|diphosphate|"
        r"macrocrystalline|microcrystalline|ultramicrocrystalline|microsize|ultramicrosize|micronized|glacial|kit")
SALT_RX = re.compile(r"\b(" + SALT + r")\b")
HYD_RX = re.compile(r"\b(hydrate|monohydrate|dihydrate|trihydrate|tetrahydrate|pentahydrate|hexahydrate|heptahydrate|sesquihydrate|hemihydrate|"
                    r"anhydrous|hydrous|usp|nf|macrocrystalline|microcrystalline|ultramicrocrystalline|microsize|ultramicrosize|micronized|glacial)\b")
SYN = {"acetaminophen": ["paracetamol"], "paracetamol": ["acetaminophen"], "epinephrine": ["adrenaline"], "norepinephrine": ["noradrenaline"],
       "aspirin": ["acetylsalicylic acid"], "acetylsalicylic acid": ["aspirin"], "nitroglycerin": ["glyceryl trinitrate"],
       "glyceryl trinitrate": ["nitroglycerin"], "secretin human": ["secretin synthetic human"],
       "telotristat ethyl": ["telotristat etiprate"]}  # Xermelo：telotristat ethyl 以 etiprate 鹽上市
APPL = ad.APPL
LISTING_CAT = re.compile(r"^(OTC MONOGRAPH|UNAPPROVED|EMERGENCY USE)", re.I)
MAX_LISTING_RECORDS = 20


def norm(x):
    t = re.sub(r"\([^)]*\)", " ", str(x or "").lower())  # CAMPHOR (NATURAL)、HYALURONIDASE (HUMAN RECOMBINANT)
    t = re.sub(r"(?<=[a-z0-9]{2})-[a-z]{4}\s*$", "", t)  # 生物相似藥的 4 字母字尾（ustekinumab-auub、ropeginterferon alfa-2b-njft）
    t = re.sub(r"^(fam|ado)-", "", t)  # fam-trastuzumab deruxtecan、ado-trastuzumab emtansine
    t = re.sub(r"\bhcl\b", "hydrochloride", t)
    t = " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())
    if t.startswith("insulin "):  # INSULIN SUSP ISOPHANE RECOMBINANT HUMAN → insulin human
        t = " ".join(w for w in t.split() if w not in ("recombinant", "susp", "isophane"))
    return t


def base(x, keep_salt=False):
    t = norm(x)
    s = " ".join((HYD_RX if keep_salt else SALT_RX).sub(" ", t).split())
    return s or " ".join(HYD_RX.sub(" ", t).split()) or t  # 整個名字都是鹽類字（sodium chloride）→ 保留原名


def acid_ate(t):
    """-ic acid ↔ -ate（只用在單方頁）"""
    out = {t}
    if t.endswith("ic acid"):
        out.add(t[:-7] + "ate")
    elif t.endswith("ate") and " " not in t:
        out.add(t[:-3] + "ic acid")
    return out


QUAL = re.compile(r"^(dibasic|monobasic|tribasic|conjugated|esterified|glacial|chorionic|macrocrystalline|microcrystalline|ultramicrocrystalline|"
                  r"microsize|ultramicrosize|micronized|heptahydrate|anhydrous|monohydrate|dihydrate|usp|nf|c-14|kr-81m|fe-59)\b", re.I)


def split_ings(s, fda_name=False):
    """「;」分隔的成分；Drugs@FDA 的單一成分欄有時寫成「A, B AND C」，拆開（逗號後是型態字的不拆：SODIUM PHOSPHATE, DIBASIC）"""
    out = []
    for x in re.split(r";", str(s or "")):
        x = x.strip()
        if not x:
            continue
        if not fda_name:
            out.append(x)
            continue
        parts = []
        for frag in re.split(r",\s*(?:and\s+)?|\s+and\s+", x, flags=re.I):
            frag = frag.strip()
            if not frag:
                continue
            if parts and QUAL.match(frag):
                parts[-1] += ", " + frag
            else:
                parts.append(frag)
        out += parts
    return out


def loose(c):
    """寬鬆比對鍵（精確比不到時才用）：拿掉所有括號內容（含巢狀、不成對的括號）、鹽類字，只留字母與數字
    （1,3-BISUREA＝1,3-BIS-UREA、BENZOPYRENE＝BENZO(A)PYRENE 類寫法差異）"""
    t = str(c or "").lower()
    while re.search(r"\([^()]*\)", t):
        t = re.sub(r"\([^()]*\)", " ", t)
    t = t.replace("(", " ").replace(")", " ")
    if not SALT_RX.sub(" ", norm(t)).strip():
        return ""  # 只有鹽類字的成分（NDC 複方裡單獨列的 SODIUM）：證據包 drug.inn 會拿掉，寬鬆比對也不算
    return re.sub(r"[^a-z0-9]", "", base(t))


def loose_key(ings):
    return frozenset(x for x in (loose(c) for c in ings) if x)


def prefix_match(pa, qa):
    """兩組寬鬆鍵一一對應，每對相等或一方是另一方的開頭（至少 6 字母）"""
    if len(pa) != len(qa):
        return False
    rest = sorted(qa)
    for x in sorted(pa, key=len, reverse=True):
        y = next((y for y in rest if x == y or min(len(x), len(y)) >= 6 and (x.startswith(y) or y.startswith(x))), None)
        if y is None:
            return False
        rest.remove(y)
    return True


def combo_key(ings):
    """複方的成分組合：每個成分去掉鹽類／水合物字尾（證據包 drug.inn 已是去鹽類的寫法，例「ACETAMINOPHEN; CODEINE」）；
    整個名字都是鹽類字的成分保留原名（sodium phosphate 與 potassium phosphate 不會變成同一個）"""
    return frozenset(base(c) for c in ings)


def single_terms(inn):
    full = norm(inn)
    salt_named = base(full) != base(full, keep_salt=True)
    b = base(full, keep_salt=salt_named)
    out = set()
    for t in {b} | set(SYN.get(b, [])):
        out |= acid_ate(t)
    return {t for t in out if len(t) >= 3}, salt_named


def load_drugsfda(download):
    if download:
        r = requests.get(ad.URL, timeout=300, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
        r.raise_for_status()
        ZIP.write_bytes(r.content)
    z = zipfile.ZipFile(ZIP)
    d = json.loads(z.read(z.namelist()[0]))
    res = d.get("results") or []
    if len(res) < 15000:
        raise SystemExit(f"Drugs@FDA 只解析出 {len(res)} 個申請號，疑似格式改變")
    return res, (d.get("meta") or {}).get("last_updated", "")


def first_approval(x):
    ds = [s.get("submission_status_date") or "" for s in x.get("submissions") or [] if s.get("submission_type") == "ORIG" and s.get("submission_status") == "AP"]
    return min(ds) if ds else ""


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    dfda, updated = load_drugsfda("--skip-download" not in argv)
    # 申請號的狀態檔（license_refresh 用）跟著同一份 Drugs@FDA 更新
    st = []
    apps = {}  # appl → dict
    tentative = set()
    for x in dfda:
        a = (x.get("application_number") or "").strip()
        prods = x.get("products") or []
        if not APPL.match(a) or not prods:
            continue
        ms = {(p.get("marketing_status") or "").strip() for p in prods}
        st.append({"appl": a, "ids": sorted(ms)})
        if ms <= {"None (Tentative Approval)", ""}:
            tentative.add(a)
            continue
        active = bool(ms & {"Prescription", "Over-the-counter"})
        kind = APPL.match(a).group(1)
        pl = []
        for p in prods:
            if (p.get("marketing_status") or "").startswith("None"):
                continue
            ings = [y for i in p.get("active_ingredients") or [] if i.get("name") for y in split_ings(i["name"], fda_name=True)]
            if ings:
                pl.append({"ings": ings, "brand": p.get("brand_name") or "", "form": p.get("dosage_form") or "",
                           "route": p.get("route") or "", "active": (p.get("marketing_status") or "") in ("Prescription", "Over-the-counter")})
        if not pl:
            continue
        apps[a] = {"appl": a, "kind": kind, "active": active, "sponsor": x.get("sponsor_name") or "", "date": first_approval(x), "products": pl,
                   "status": kind if active else kind + ad.SUFFIX}
    if not dry and "--skip-download" not in argv:
        (RAW / "drugsfda_appl_status.json").write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    ndc = json.loads((RAW / "us_fda_drugs.json").read_text(encoding="utf-8"))
    in_dfda = set(apps)
    listings = {}
    for r in ndc:
        a = str(r.get("ApplNo") or "").strip()
        ings = split_ings(r.get("ActiveIngredient"))
        if not ings:
            continue
        cat = str(r.get("MarketingCategory") or "").strip()
        if APPL.match(a):
            if a in in_dfda or a in tentative:
                continue
            e = apps.setdefault(a, {"appl": a, "kind": APPL.match(a).group(1), "active": True, "sponsor": r.get("Manufacturer") or "",
                                    "date": str(r.get("ApprovalDate") or ""), "products": [], "status": cat or APPL.match(a).group(1),
                                    "source": "NDC Directory (not in Drugs@FDA)"})
            e["products"].append({"ings": ings, "brand": r.get("DrugName") or "", "form": r.get("Form") or "", "route": r.get("Route") or "", "active": True})
        elif LISTING_CAT.match(cat) or not a or a.lower() == "nan" or not APPL.match(a):
            k = str(r.get("ProductNDC") or "").strip()
            if k and k not in listings:
                listings[k] = {"ndc": k, "id": a if a and a.lower() != "nan" else "", "cat": cat, "ings": ings, "brand": r.get("DrugName") or "",
                               "form": r.get("Form") or "", "maker": r.get("Manufacturer") or ""}
    # 索引：單方用成分主體（含鹽／不含鹽），複方用成分組合
    by_ing = {}
    by_combo = {}
    for a, e in apps.items():
        for i, p in enumerate(e["products"]):
            by_combo.setdefault(combo_key(p["ings"]), set()).add(a)
            for c in p["ings"]:
                for keep in (False, True):
                    by_ing.setdefault((base(c, keep_salt=keep), keep), set()).add(a)
    by_loose, by_loose_combo, lst_loose, lst_loose_combo = {}, {}, {}, {}
    for a, e in apps.items():
        for p in e["products"]:
            by_loose_combo.setdefault(loose_key(p["ings"]), set()).add(a)
            for c in p["ings"]:
                by_loose.setdefault(loose(c), set()).add(a)
    lst_ing, lst_combo = {}, {}
    for k, e in listings.items():
        lst_loose_combo.setdefault(loose_key(e["ings"]), set()).add(k)
        for c in e["ings"]:
            lst_loose.setdefault(loose(c), set()).add(k)
        lst_combo.setdefault(combo_key(e["ings"]), set()).add(k)
        for c in e["ings"]:
            for keep in (False, True):
                lst_ing.setdefault((base(c, keep_salt=keep), keep), set()).add(k)
    out, n_changed, n_found, n_empty = [], 0, 0, 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("tfda") or {}
        inn = (b.get("drug") or {}).get("inn") or page.replace("_", " ")
        ings = split_ings(inn)
        if len(ings) > 1:
            ck = combo_key(ings)
            hit_a, hit_l = set(by_combo.get(ck, set())), set(lst_combo.get(ck, set()))
            terms, mode, salt_named = {",".join(sorted(ck))}, "combo", False
            if not hit_a and not hit_l:  # 精確比不到：寬鬆鍵相同，再不行就逐一比「每個成分相等或互為開頭」
                lk = loose_key(ings)
                hit_a, hit_l = set(by_loose_combo.get(lk, set())), set(lst_loose_combo.get(lk, set()))
                if not hit_a and not hit_l:
                    hit_a = {a for kk, aa in by_loose_combo.items() if len(kk) == len(lk) and prefix_match(lk, kk) for a in aa}
                    hit_l = {x for kk, xx in lst_loose_combo.items() if len(kk) == len(lk) and prefix_match(lk, kk) for x in xx}
                if hit_a or hit_l:
                    mode = "combo-loose"
        else:
            terms, salt_named = single_terms(ings[0] if ings else inn)
            hit_a, hit_l = set(), set()
            for t in terms:
                hit_a |= by_ing.get((t, salt_named), set())
                hit_l |= lst_ing.get((t, salt_named), set())
            mode = "single"
            if not hit_a and not hit_l and not salt_named:
                for t in terms:
                    hit_a |= by_loose.get(loose(t), set())
                    hit_l |= lst_loose.get(loose(t), set())
                if hit_a or hit_l:
                    mode = "single-loose"
        old_ids = sorted({str(r.get("license_id") or "") for r in reg.get("records") or [] if APPL.match(str(r.get("license_id") or ""))})

        def app_rec(a):
            e = apps[a]
            ps = [p for p in e["products"] if mode == "combo" and combo_key(p["ings"]) == combo_key(ings)
                  or mode == "single" and any((base(c, keep_salt=salt_named) in terms) for c in p["ings"])
                  or mode == "single-loose" and any(loose(c) in {loose(t) for t in terms} for c in p["ings"])] or e["products"]
            ps = sorted(ps, key=lambda p: (not p["active"], len(p["ings"])))
            p = ps[0]
            return {"license_id": a, "brand_name_zh": p["brand"], "brand_name_en": p["brand"], "ingredients": "; ".join(p["ings"]), "indication": "",
                    "dosage_form": p["form"], "manufacturer": e["sponsor"], "license_holder": e["sponsor"], "approval_date": e["date"], "expiry_date": "",
                    "status": e["status"], "route": p["route"], "source": e.get("source") or f"Drugs@FDA (openFDA {updated})",
                    "_sort": (not e["active"], min(len(q["ings"]) for q in ps), a)}
        recs = sorted((app_rec(a) for a in hit_a), key=lambda r: r["_sort"])
        for r in recs:
            r.pop("_sort")
        lk = sorted(hit_l, key=lambda k: (len(listings[k]["ings"]), k))
        lrecs = [{"license_id": listings[k]["id"] or "Not applicable", "product_ndc": k, "brand_name_zh": listings[k]["brand"], "brand_name_en": listings[k]["brand"],
                  "ingredients": "; ".join(listings[k]["ings"]), "indication": "", "dosage_form": listings[k]["form"], "manufacturer": listings[k]["maker"],
                  "license_holder": listings[k]["maker"], "approval_date": "", "expiry_date": "", "status": listings[k]["cat"], "listing": True,
                  "source": "FDA NDC Directory listing (no FDA application)"} for k in lk[:MAX_LISTING_RECORDS]]
        new = dict(reg, found=bool(recs or lrecs), records=recs + lrecs, total_matches=len(recs) + len(hit_l), listed_total=len(hit_l),
                   applications_total=len(recs), rebuilt="2026-11-05 by ingredient (Drugs@FDA + NDC Directory listings)")
        new_ids = sorted(r["license_id"] for r in recs)
        nv = sum(1 for r in recs if not r["status"].endswith(ad.SUFFIX))
        out.append(f"{page}\t{mode}\t{len(old_ids)}\t{len(new_ids)}\t{nv}\t{len(hit_l)}\t{len(set(old_ids) - set(new_ids))}\t"
                   f"{';'.join(sorted(set(old_ids) - set(new_ids))[:15])}\t{';'.join(sorted(set(new_ids) - set(old_ids))[:15])}")
        n_found += bool(recs or lrecs)
        n_empty += not (recs or lrecs)
        if new != reg:
            n_changed += 1
            b["tfda"] = new
            if not dry:
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tmode\told_applications\tnew_applications\tnew_active\tlistings\tdropped\tdropped_ids\tadded_ids\n" + "\n".join(out) + "\n",
                             encoding="utf-8")
    print(f"Drugs@FDA {updated}：{len(apps)} 個申請號（暫定核准不收 {len(tentative)}）、NDC 列名產品 {len(listings)}；"
          f"改 {n_changed} 個證據包（有紀錄 {n_found}、查無 {n_empty}）")


if __name__ == "__main__":
    main(sys.argv[1:])

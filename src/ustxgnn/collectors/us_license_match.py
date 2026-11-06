"""US 依成分比對 FDA 申請號與 NDC 列名產品（2026-11-05 起，用戶核准；全程不用 AI）。

scripts/rebuild_licenses_by_ingredient.py（整批重建證據包）與 collectors/usfda.py（之後新收的證據包）共用這一套，
兩邊的比對結果一定相同。

1. 來源
   - FDA 核准申請：openFDA 的 Drugs@FDA 全量檔（DRUGSFDA_URL，存 data/raw/drugsfda_openfda.zip）。
     每個申請號（NDA／ANDA／BLA）的產品成分（products[].active_ingredients）與上市狀態。
     狀態：有處方或 OTC 產品＝有效（原類別，例「NDA」）；全部產品 Discontinued＝「<類別> (Discontinued in Drugs@FDA)」；
     只有暫定核准（None (Tentative Approval)）的申請不能上市，不收。
   - NDC 產品清單：openFDA 的 NDC 全量檔（NDC_URL，存 data/raw/ndc_openfda.zip；2026-11-06 起取代 2026-03 下載的
     data/raw/us_fda_drugs.json，那份仍留給對照與預測用）。只取成品（finished），結束上市日已過的不收。
     Drugs@FDA 沒有的申請號（CBER 的 BLA 等）照 NDC 的類別當有效申請；OTC monograph／未核准類別的產品是「列名」
     （listing），不是 FDA 核准，另外計數（listed_total），不算有效申請。
2. 比對（成分名先去掉鹽類／酯類／水合物字尾；整個成分名都是鹽類字時保留原名，例 sodium chloride）
   - 成分以「;」分隔；括號裡的「;」不算分隔（HYDROLYSED MARINE COLLAGEN (ENZYMATIC; 2000 MW) 是一個成分；
     openFDA 的 NDC 檔會把它拆成兩筆，這裡接回來）。
   - 複方（drug.inn 以「;」分隔多個成分）：產品的成分組合要跟本頁完全相同才收。
   - 單方：產品成分含本藥就收（含複方產品）；「-ic acid」與「-ate」視為同一成分
     （mycophenolic acid＝mycophenolate sodium、valproic acid＝valproate）。名稱本身帶鹽類時只收同一個鹽。
   - 別名只收同一個物質的不同寫法（SYN：單方的藥名別名；SAME_SUBSTANCE：同一個 FDA UNII 的成分寫法，單方與複方都適用；每筆附依據）。
3. 結果：records＝全部申請號（每個申請號一筆，有效的排前面、單方產品排前面）＋最多 20 筆列名產品（listing: true）；
   listed_total＝列名產品數（不重複 NDC 產品碼）；applications_total＝申請號數；total_matches＝兩者相加。
   reviewer._local_regulatory 依 listing 欄位把申請號與列名分開算（概覽「FDA 核准申請 X／N；OTC monograph／未核准列名 K」）。
"""
import json
import re
import time
import zipfile
from datetime import date
from pathlib import Path

DRUGSFDA_URL = "https://download.open.fda.gov/drug/drugsfda/drug-drugsfda-0001-of-0001.json.zip"  # 與 scripts/license_adapter.py 相同
NDC_URL = "https://download.open.fda.gov/drug/ndc/drug-ndc-0001-of-0001.json.zip"
SUFFIX = " (Discontinued in Drugs@FDA)"  # 與 scripts/license_adapter.py 相同
APPL = re.compile(r"^(NDA|ANDA|BLA)(\d{6})$")
UA = {"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"}

SALT = (r"hydrochloride|hcl|hydrobromide|besylate|besilate|maleate|mesylate|mesilate|tartrate|bitartrate|fumarate|hemifumarate|succinate|"
        r"citrate|acetate|diacetate|dipropionate|propionate|valerate|butyrate|phosphate|sulfate|sulphate|nitrate|lactate|gluconate|palmitate|"
        r"hydrate|monohydrate|dihydrate|trihydrate|tetrahydrate|pentahydrate|hexahydrate|heptahydrate|sesquihydrate|hemihydrate|anhydrous|hydrous|"
        r"sodium|potassium|calcium|magnesium|disodium|dipotassium|cilexetil|axetil|medoxomil|dihydrochloride|bromide|chloride|iodide|"
        r"tosylate|edisylate|pamoate|embonate|stearate|oleate|mandelate|camsylate|xinafoate|furoate|aceponate|hyclate|trometamol|tromethamine|"
        r"arginine|lysine|meglumine|olamine|erbumine|tert butylamine|benzathine|procaine|esylate|napadisilate|hemisulfate|bisulfate|"
        r"monosodium|trisodium|usp|nf|decanoate|enanthate|cypionate|undecanoate|oxalate|dimeglumine|diphosphate|"
        r"macrocrystalline|microcrystalline|ultramicrocrystalline|microsize|ultramicrosize|micronized|glacial|kit|"
        # 2026-11-06 補（用戶核准，逐筆查 FDA GSRS；GSRS 的 ACTIVE MOIETY 都是母藥）：
        # ERYTHROMYCIN ETHYLSUCCINATE（UNII 1014KSJ86F）、ERYTHROMYCIN LACTOBIONATE（33H58I7GLQ）→ Erythromycin 63937KV33D（E.E.S.、Erythrocin）；
        # Treprostinil Diolamine（H1FKG90039）→ Treprostinil RUM6K67ESG（Orenitram）；
        # Nilotinib D-tartrate（8URQ2WD9KN）→ Nilotinib F41401512X（NDA218922，NDC 列名成分寫 NILOTINIB）。
        # 「d tartrate」是 D-tartrate 經 norm() 去連字號後的寫法。polistirex 不放這裡，見 SAME_SUBSTANCE。
        r"ethylsuccinate|lactobionate|diolamine|d tartrate")
SALT_RX = re.compile(r"\b(" + SALT + r")\b")
HYD_RX = re.compile(r"\b(hydrate|monohydrate|dihydrate|trihydrate|tetrahydrate|pentahydrate|hexahydrate|heptahydrate|sesquihydrate|hemihydrate|"
                    r"anhydrous|hydrous|usp|nf|macrocrystalline|microcrystalline|ultramicrocrystalline|microsize|ultramicrosize|micronized|glacial)\b")
# 別名：只收同一個物質的不同寫法
SYN = {"acetaminophen": ["paracetamol"], "paracetamol": ["acetaminophen"], "epinephrine": ["adrenaline"], "norepinephrine": ["noradrenaline"],
       "aspirin": ["acetylsalicylic acid"], "acetylsalicylic acid": ["aspirin"], "nitroglycerin": ["glyceryl trinitrate"],
       "glyceryl trinitrate": ["nitroglycerin"], "secretin human": ["secretin synthetic human"],
       "telotristat ethyl": ["telotristat etiprate"]}  # Xermelo：telotristat ethyl 以 etiprate 鹽上市
# 不是別名（查證過、不要再併）：
# - polyethylene glycol 3500 ≠ polyethylene glycol 3350（2026-11-06 查證）：FDA GSRS 是兩個物質，UNII 不同
#   （PEG 3500＝FVS1AZD90Y，數量平均分子量 3500；PEG 3350＝G2M7P15E5P，重量平均分子量 3015–3685，USP monograph），
#   RxNorm 成分也不同（1312707 vs 221147）。https://gsrs.ncats.nih.gov/ginas/app/beta/substances/FVS1AZD90Y 、
#   https://gsrs.ncats.nih.gov/ginas/app/beta/substances/G2M7P15E5P
#   GSRS 兩者的黏度規格也不同（PEG 3500 87–123 cSt、PEG 3350 76–110 cSt，98.9 °C 水溶液）。
#   NDC 裡唯一把成分編成 PEG 3500（UNII FVS1AZD90Y）的是 Mylan 的 51079-306（DailyMed setid 219bcbc4-b84a-4209-9f34-ef2b0ef0d273，
#   2026-04-08 版）；它的品名、標籤文字都寫 Polyethylene Glycol 3350, USP，申請號 ANDA078915 在 Drugs@FDA 的成分也是 PEG 3350。
#   這是該仿單的成分編碼跟品名不一致，不是同物異名；照規則仍不併（申請號以 Drugs@FDA 的成分為準）。
# 同一物質（同一個 FDA UNII）的不同成分寫法，單方與複方都適用（norm() 最後一步換成同一個寫法；2026-11-06，用戶核准，逐筆查 FDA GSRS）。
# 只收 GSRS 同一筆物質紀錄裡列出的名稱；不同 UNII（例：同屬不同部位、不同立體異構物）不收。
SAME_SUBSTANCE = {
    # FDA GSRS UNII I76KB35JEV（PULSATILLA VULGARIS WHOLE，Ranunculaceae Pulsatilla vulgaris Mill.，部位 whole）的名稱裡有
    # ANEMONE PULSATILLA、ANEMONE PULSATILLA L.、ANEMONE PULSATILLA WHOLE、PULSATILLA VULGARIS、PULSATILLA VULGARIS MILL.：
    # 植物學同物異名（Anemone pulsatilla L.＝Pulsatilla vulgaris Mill.），同一個 UNII。
    # https://gsrs.ncats.nih.gov/ginas/app/beta/substances/I76KB35JEV （2026-11-06 查）。
    # 例：VARICO HP（NDC 43857-0341）2026-03 的 NDC 列名寫 ANEMONE PULSATILLA，現行列名寫 PULSATILLA VULGARIS WHOLE（openFDA unii 欄同為 I76KB35JEV）。
    # PULSATILLA VULGARIS TOP（UNII 4F1D271XW0，部位 top）是另一個物質，不併。
    "anemone pulsatilla": "pulsatilla vulgaris whole", "anemone pulsatilla l": "pulsatilla vulgaris whole",
    "anemone pulsatilla whole": "pulsatilla vulgaris whole", "pulsatilla vulgaris": "pulsatilla vulgaris whole",
    "pulsatilla vulgaris mill": "pulsatilla vulgaris whole",
    # Drugs@FDA 把 Increlex（BLA021839）的成分寫成 MECASERMIN RECOMBINANT；它的 openFDA unii＝7GR9I2683O（GSRS MECASERMIN），
    # NDC 列名（15054-1040、71863-216）與 DailyMed（setid a8b27a1b-a611-4f91-ad22-76d4b390c3ae）成分都寫 MECASERMIN（2026-11-06 查）。
    # MECASERMIN RINFABATE（UNII NZ8M50KKRG，Iplex）是另一個物質，不併。
    "mecasermin recombinant": "mecasermin",
    # DEXTROMETHORPHAN POLISTIREX（Delsym NDA018658、ANDA091135 等）：GSRS 是 concept，SUBSTANCE->SUB_CONCEPT Dextromethorphan
    # （UNII 7355X3ROTS）；Delsym 的 openFDA substance_name＝DEXTROMETHORPHAN（DailyMed setid e3e1d126-76c2-4776-8ce0-449625b7e6ba）。
    "dextromethorphan polistirex": "dextromethorphan",
    # 其他藥的 polistirex（樹脂複合物，2026-11-06 用戶決定查證後併；逐藥別名，不做成通用鹽類字）。FDA GSRS 都是 concept，
    # SUBSTANCE->SUB_CONCEPT 指向母藥：
    #   CHLORPHENIRAMINE POLISTIREX → Chlorpheniramine（UNII 3U6IO1965U）
    #   HYDROCODONE POLISTIREX → HYDROCODONE（6YKS4Y3WQ7）
    #   CODEINE POLISTIREX → Codeine anhydrous（UX6OWY2V7J）
    #   PSEUDOEPHEDRINE POLISTIREX → Pseudoephedrine（7CUC9DDI9F）
    # 另：hydrocodone／chlorpheniramine polistirex 緩釋懸液 ANDA091632 的 openFDA substance_name＝HYDROCODONE BITARTRATE、CHLORPHENIRAMINE
    # MALEATE（unii NO70W886KK、V1Q0O9OJ9Z），NDC 列名（63629-2303 等）同；DailyMed setid 25f400d9-1d6e-4d38-8f0d-98d471eba73b。
    # Tussionex、Tuzistra XR、Penntuss、Codeprex、Pseudo-12 在 Drugs@FDA 都已停產，openFDA／DailyMed 沒有成分資料，依 GSRS 判定。
    # PHENYLPROPANOLAMINE POLISTIREX（Corsym NDA018050，已停產）：GSRS 查無此物質、openFDA／DailyMed 也沒有，查證不了，不併。
    "chlorpheniramine polistirex": "chlorpheniramine", "hydrocodone polistirex": "hydrocodone",
    "codeine polistirex": "codeine", "pseudoephedrine polistirex": "pseudoephedrine",
    # ZINC SULFATE＝ZINC SULFATE, UNSPECIFIED FORM（2026-11-06，用戶決定）：FDA GSRS 的「ZINC SULFATE」是 UNII 89DS0H96TB
    # （ZINC SULFATE, UNSPECIFIED FORM，mixture）底下的名稱；Apotex 的 zinc sulfate 注射劑 ANDA218059 在 Drugs@FDA 成分寫 ZINC SULFATE，
    # 同一申請的 NDC 列名（60505-6260、60505-6261）寫 ZINC SULFATE, UNSPECIFIED FORM。
    # https://gsrs.ncats.nih.gov/ginas/app/beta/substances/89DS0H96TB
    # 換成「zinc sulfate」（不是反過來）：base() 會把 sulfate 當鹽類字拿掉，換成 zinc sulfate 才跟其他鋅鹽的單方比對規則一致。
    "zinc sulfate unspecified form": "zinc sulfate",
}
# 不是同一物質（查證過、不要再併）：
# - 5-METHYLTETRAHYDROFOLIC ACID（UNII TYK22LML8F）≠ LEVOMEFOLATE CALCIUM（UNII A9R10K3F2F）（2026-11-06 查 GSRS）：
#   TYK22LML8F 是 6 位未定構型的差向異構物混合物（stereochemistry EPIMERIC，2 個立體中心只定 1 個），活性部分是它自己；
#   levomefolate calcium 是 (6S) 單一異構物的鈣鹽，活性部分是 LEVOMEFOLIC ACID（UNII 8S95DH25XC）；
#   GSRS 還把 TYK22LML8F 登記成 levomefolate calcium 的雜質（PARENT->IMPURITY）。不是同一活性部分的鹽類。
#   https://gsrs.ncats.nih.gov/ginas/app/beta/substances/TYK22LML8F 、https://gsrs.ncats.nih.gov/ginas/app/beta/substances/A9R10K3F2F
#   影響：Prenate Essential（NDC 75854-313）、Prenate Elite（75854-314）現行列名把 5-MTHF 改寫成 LEVOMEFOLATE CALCIUM，對應的
#   alpha-tocopherol 複方頁維持查無列名；Prenate Elite 另把 .BETA.-CAROTENE（UNII 01YAE03M7J）改成 VITAMIN A（UNII 81G40H8B0T，也不同）。
#   Prenate DHA（75854-312）現行列名多了 LEVOMEFOLATE CALCIUM 一個成分，不是改寫法，成分組合不同。
LISTING_CAT = re.compile(r"^(OTC MONOGRAPH|UNAPPROVED|EMERGENCY USE)", re.I)
MAX_LISTING_RECORDS = 20
QUAL = re.compile(r"^(dibasic|monobasic|tribasic|conjugated|esterified|glacial|chorionic|macrocrystalline|microcrystalline|ultramicrocrystalline|"
                  r"microsize|ultramicrosize|micronized|heptahydrate|anhydrous|monohydrate|dihydrate|usp|nf|c-14|kr-81m|fe-59)\b", re.I)


# 重組人類玻尿酸酶（2026-11-06，用戶決定）：FDA GSRS UNII 743QUY4VD8「Hyaluronidase (Human Recombinant)」（名稱含 HYALURONIDASE RECOMBINANT
# HUMAN；hyaluronidase-oysk／-fihj／-qvfc／-tqjs／-ocsq／-nvhy／-lpuj／-zzxf 等是它的 SUB_CONCEPT）跟 Amphadase 的 HYALURONIDASE
# （UNII 8KOG53Z5EM，牛源）不是同一物質：Hylenex（BLA021859，openFDA unii 743QUY4VD8）與含重組酶的組合產品（Herceptin Hylecta、
# Rituxan Hycela、Darzalex Faspro…）都不算 hyaluronidase 頁。這些寫法一律換成同一個鍵 RECOMBINANT_HYALURONIDASE，
# 不能經括號刪除或 4 字母字尾刪除變回「hyaluronidase」。https://gsrs.ncats.nih.gov/ginas/app/beta/substances/743QUY4VD8 、
# https://gsrs.ncats.nih.gov/ginas/app/beta/substances/8KOG53Z5EM （2026-11-06 查）
RECOMBINANT_HYALURONIDASE = "hyaluronidase human recombinant"
_RECOMB_HYAL = re.compile(r"hyaluronidase(\s*\(\s*human\s+recombinant\s*\)|\s+recombinant\s+human|\s+human\s+recombinant|-[a-z]{4})")


def _recomb_hyal(x):
    return bool(_RECOMB_HYAL.fullmatch(" ".join(str(x or "").lower().split())))


def norm(x):
    if _recomb_hyal(x):
        return RECOMBINANT_HYALURONIDASE
    t = re.sub(r"\([^)]*\)", " ", str(x or "").lower())  # CAMPHOR (NATURAL)
    t = re.sub(r"(?<=[a-z0-9]{2})-[a-z]{4}\s*$", "", t)  # 生物相似藥的 4 字母字尾（ustekinumab-auub、ropeginterferon alfa-2b-njft）
    # fam-trastuzumab deruxtecan、ado-trastuzumab emtansine、ziv-aflibercept（2026-11-06：GSRS 的 ZIV-AFLIBERCEPT 是 Aflibercept
    # UNII 15C2VL427D 的 SUB_CONCEPT；Zaltrap BLA125418 的 openFDA unii＝15C2VL427D，NDC 列名成分寫 AFLIBERCEPT）
    t = re.sub(r"^(fam|ado|ziv)-", "", t)
    t = re.sub(r"\bhcl\b", "hydrochloride", t)
    t = " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())
    if t.startswith("insulin "):  # INSULIN SUSP ISOPHANE RECOMBINANT HUMAN → insulin human
        t = " ".join(w for w in t.split() if w not in ("recombinant", "susp", "isophane"))
    return SAME_SUBSTANCE.get(t, t)


def base(x, keep_salt=False):
    t = norm(x)
    s = " ".join((HYD_RX if keep_salt else SALT_RX).sub(" ", t).split())
    return s or " ".join(HYD_RX.sub(" ", t).split()) or t  # 整個名字都是鹽類字（sodium chloride）→ 保留原名


def acid_ate(t):
    """-ic acid ↔ -ate（只用在單方）"""
    out = {t}
    if t.endswith("ic acid"):
        out.add(t[:-7] + "ate")
    elif t.endswith("ate") and " " not in t:
        out.add(t[:-3] + "ic acid")
    return out


def _semicolon_split(s):
    """以「;」分隔，括號裡的「;」不算（前一段左括號比右括號多、後一段把它關上時接回去）"""
    parts = [p for p in str(s or "").split(";")]
    out = []
    for p in parts:
        if out and out[-1].count("(") > out[-1].count(")") and p.count(")") > p.count("("):
            out[-1] += ";" + p
        else:
            out.append(p)
    return out


def split_ings(s, fda_name=False):
    """「;」分隔的成分（也收 list）；Drugs@FDA 的單一成分欄有時寫成「A, B AND C」，拆開（逗號後是型態字的不拆：SODIUM PHOSPHATE, DIBASIC）"""
    if isinstance(s, (list, tuple)):
        s = "; ".join(str(x) for x in s if x)
    out = []
    for x in _semicolon_split(s):
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
    if _recomb_hyal(c):
        return re.sub(r"[^a-z0-9]", "", RECOMBINANT_HYALURONIDASE)
    t = str(c or "").lower()
    while re.search(r"\([^()]*\)", t):
        t = re.sub(r"\([^()]*\)", " ", t)
    t = t.replace("(", " ").replace(")", " ")
    if not SALT_RX.sub(" ", norm(t)).strip():
        return ""  # 只有鹽類字的成分（NDC 複方裡單獨列的 SODIUM）：證據包 drug.inn 會拿掉，寬鬆比對也不算
    return re.sub(r"[^a-z0-9]", "", base(t))


def loose_key(ings):
    """寬鬆組合鍵＋成分數。只有鹽類字的成分（寬鬆鍵是空的，例 POTASSIUM SULFATE、SODIUM）改用精確鍵「=<base>」，不能丟掉
    （丟掉會讓「ARGININE; LIDOCAINE」跟單方 lidocaine 同鍵、「MAGNESIUM SULFATE; POTASSIUM SULFATE; SODIUM」對到所有只含鹽類的產品）"""
    return frozenset(loose(c) or "=" + base(c) for c in ings), len(ings)


def bare_ion(c):
    """NDC 複方裡單獨列的一個鹽類字（SODIUM、POTASSIUM）：證據包 drug.inn 會拿掉"""
    return not loose(c) and len(norm(c).split()) == 1


def product_loose_keys(ings):
    """產品的寬鬆鍵：完整的一組；有單獨列的鹽類字時，另加拿掉它們的一組（本頁 drug.inn 已拿掉時對得上）"""
    out = {loose_key(ings)}
    req = [c for c in ings if not bare_ion(c)]
    if req and len(req) < len(ings):
        out.add(loose_key(req))
    return out


def _pair(x, y):
    """本頁寬鬆鍵 x 對產品寬鬆鍵 y：相等；或都不是精確鍵、至少 6 字母、一方是另一方的開頭；
    或 x 是單獨一個鹽類字（drug.inn 把「SODIUM SULFATE」寫成「SODIUM」）、y 是以它開頭的只含鹽類字成分"""
    if x == y:
        return True
    if x[:1] != "=" != y[:1]:
        return min(len(x), len(y)) >= 6 and (x.startswith(y) or y.startswith(x))
    return x[:1] == "=" == y[:1] and " " not in x and y.startswith(x + " ")


def prefix_match(pk, qk):
    """本頁與產品的寬鬆鍵（成分數相同）一一對應（_pair）"""
    (pa, pn), (qa, qn) = pk, qk
    if pn != qn or len(pa) != len(qa):
        return False
    rest = sorted(qa)
    for x in sorted(pa, key=len, reverse=True):
        y = next((y for y in rest if _pair(x, y)), None)
        if y is None:
            return False
        rest.remove(y)
    return True


def combo_key(ings):
    """複方的成分組合：每個成分去掉鹽類／水合物字尾；整個名字都是鹽類字的成分保留原名"""
    return frozenset(base(c) for c in ings)


# 本身就是藥、也常當鹽類字的有機鹼（SALT 裡有）：單方頁的名字就是它時，「PROCAINE HYDROCHLORIDE」要算本藥
# （base() 會把整個名字當鹽類字而對不上）；「PENICILLIN G PROCAINE」「IBUPROFEN LYSINE」不算
ORGANIC_BASES = {"procaine", "arginine", "lysine", "tromethamine", "trometamol", "meglumine"}


def org_base(c):
    """去掉鹽類字但保留 ORGANIC_BASES 的寫法：PROCAINE HYDROCHLORIDE → procaine"""
    t = re.sub(SALT_RX, lambda m: m.group(0) if m.group(0) in ORGANIC_BASES else " ", norm(c))
    return " ".join(HYD_RX.sub(" ", t).split())


def single_terms(inn):
    full = norm(inn)
    salt_named = base(full) != base(full, keep_salt=True)
    b = base(full, keep_salt=salt_named)
    out = set()
    for t in {b} | set(SYN.get(b, [])):
        out |= acid_ate(t)
    return {t for t in out if len(t) >= 3}, salt_named


def download(url, path):
    import requests

    for attempt in range(4):
        try:
            r = requests.get(url, timeout=300, headers=UA)
            r.raise_for_status()
            zipfile.ZipFile(__import__("io").BytesIO(r.content)).testzip()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_bytes(r.content)


def _read_zip_json(path):
    z = zipfile.ZipFile(path)
    return json.loads(z.read(z.namelist()[0]))


def load_drugsfda(path):
    d = _read_zip_json(path)
    res = d.get("results") or []
    if len(res) < 15000:
        raise SystemExit(f"Drugs@FDA 只解析出 {len(res)} 個申請號，疑似格式改變")
    return res, (d.get("meta") or {}).get("last_updated", "")


def load_ndc(path, today=None):
    """openFDA NDC 全量檔 → 本模組的產品列（只取成品、結束上市日未過的；同一 product_ndc 只留一筆）"""
    d = _read_zip_json(path)
    res = d.get("results") or []
    if len(res) < 50000:
        raise SystemExit(f"NDC 只解析出 {len(res)} 筆，疑似格式改變")
    today = today or date.today().strftime("%Y%m%d")
    out, seen = [], set()
    for x in res:
        k = str(x.get("product_ndc") or "").strip()
        if not x.get("finished") or not k or k in seen:
            continue
        end = str(x.get("marketing_end_date") or "")
        if end and end < today:
            continue
        ings = split_ings([i.get("name") for i in x.get("active_ingredients") or []])
        if not ings:
            continue
        seen.add(k)
        out.append({"ndc": k, "appl": str(x.get("application_number") or "").strip(), "cat": str(x.get("marketing_category") or "").strip(),
                    "ings": ings, "brand": x.get("brand_name") or x.get("generic_name") or "", "form": x.get("dosage_form") or "",
                    "route": ", ".join(x.get("route") or []), "maker": x.get("labeler_name") or "", "date": str(x.get("marketing_start_date") or "")})
    return out, (d.get("meta") or {}).get("last_updated", "")


def load_ndc_legacy(path):
    """舊的 data/raw/us_fda_drugs.json（process_fda_data.py 從 NDC 文字檔產生）→ 產品列；只在沒有 ndc_openfda.zip 時備用"""
    out = []
    for r in json.loads(Path(path).read_text(encoding="utf-8")):
        ings = split_ings(r.get("ActiveIngredient"))
        if ings:
            a = str(r.get("ApplNo") or "").strip()
            out.append({"ndc": str(r.get("ProductNDC") or "").strip(), "appl": "" if a.lower() == "nan" else a, "cat": str(r.get("MarketingCategory") or "").strip(),
                        "ings": ings, "brand": r.get("DrugName") or "", "form": r.get("Form") or "", "route": r.get("Route") or "",
                        "maker": r.get("Manufacturer") or "", "date": str(r.get("ApprovalDate") or "")})
    return out, "us_fda_drugs.json"


def first_approval(x):
    ds = [s.get("submission_status_date") or "" for s in x.get("submissions") or [] if s.get("submission_type") == "ORIG" and s.get("submission_status") == "AP"]
    return min(ds) if ds else ""


class LicenseIndex:
    def __init__(self, dfda, updated, ndc_rows, ndc_updated=""):
        self.updated, self.ndc_updated = updated, ndc_updated
        self.appl_status = []  # 申請號狀態檔（license_refresh 用）
        apps, tentative = {}, set()
        for x in dfda:
            a = (x.get("application_number") or "").strip()
            prods = x.get("products") or []
            if not APPL.match(a) or not prods:
                continue
            ms = {(p.get("marketing_status") or "").strip() for p in prods}
            self.appl_status.append({"appl": a, "ids": sorted(ms)})
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
                       "status": kind if active else kind + SUFFIX}
        in_dfda = set(apps)
        listings = {}
        for r in ndc_rows:
            a, cat, ings = r["appl"], r["cat"], split_ings(r["ings"])  # 已拆好的 list 再過一次也一樣
            if APPL.match(a):
                if a in in_dfda or a in tentative:
                    continue
                e = apps.setdefault(a, {"appl": a, "kind": APPL.match(a).group(1), "active": True, "sponsor": r["maker"], "date": r["date"],
                                        "products": [], "status": cat or APPL.match(a).group(1), "source": "NDC Directory (not in Drugs@FDA)"})
                e["products"].append({"ings": ings, "brand": r["brand"], "form": r["form"], "route": r["route"], "active": True})
            elif LISTING_CAT.match(cat) or not a or not APPL.match(a):
                k = r["ndc"]
                if k and k not in listings:
                    listings[k] = {"ndc": k, "id": a, "cat": cat, "ings": ings, "brand": r["brand"], "form": r["form"], "maker": r["maker"]}
        self.apps, self.tentative, self.listings = apps, tentative, listings
        self.by_ing, self.by_combo, self.by_loose, self.by_loose_combo = {}, {}, {}, {}
        for a, e in apps.items():
            for p in e["products"]:
                self.by_combo.setdefault(combo_key(p["ings"]), set()).add(a)
                for lk in product_loose_keys(p["ings"]):
                    self.by_loose_combo.setdefault(lk, set()).add(a)
                for c in p["ings"]:
                    self.by_loose.setdefault(loose(c), set()).add(a)
                    for keep in (False, True):
                        self.by_ing.setdefault((base(c, keep_salt=keep), keep), set()).add(a)
                    if org_base(c) in ORGANIC_BASES:
                        self.by_ing.setdefault((org_base(c), "org"), set()).add(a)
        self.lst_ing, self.lst_combo, self.lst_loose, self.lst_loose_combo = {}, {}, {}, {}
        for k, e in listings.items():
            for lk in product_loose_keys(e["ings"]):
                self.lst_loose_combo.setdefault(lk, set()).add(k)
            self.lst_combo.setdefault(combo_key(e["ings"]), set()).add(k)
            for c in e["ings"]:
                self.lst_loose.setdefault(loose(c), set()).add(k)
                for keep in (False, True):
                    self.lst_ing.setdefault((base(c, keep_salt=keep), keep), set()).add(k)
                if org_base(c) in ORGANIC_BASES:
                    self.lst_ing.setdefault((org_base(c), "org"), set()).add(k)

    @classmethod
    def from_files(cls, drugsfda_zip, ndc_zip=None, legacy_ndc_json=None):
        dfda, updated = load_drugsfda(drugsfda_zip)
        if ndc_zip and Path(ndc_zip).exists():
            rows, nu = load_ndc(ndc_zip)
        else:
            rows, nu = load_ndc_legacy(legacy_ndc_json)
        return cls(dfda, updated, rows, nu)

    def label(self):
        return f"by ingredient (Drugs@FDA {self.updated} + NDC Directory {self.ndc_updated} listings)"

    def match(self, inn):
        """inn＝證據包 drug.inn（複方以「;」分隔）→ (tfda 欄位, 比對方式)"""
        ings = split_ings(inn)
        if len(ings) > 1:
            ck = combo_key(ings)
            hit_a, hit_l = set(self.by_combo.get(ck, set())), set(self.lst_combo.get(ck, set()))
            terms, mode, salt_named = {",".join(sorted(ck))}, "combo", False
            lk = loose_key(ings)
            if not hit_a and not hit_l:  # 精確比不到：寬鬆鍵相同，再不行就逐一比「每個成分相等或互為開頭」
                hit_a, hit_l = set(self.by_loose_combo.get(lk, set())), set(self.lst_loose_combo.get(lk, set()))
                if not hit_a and not hit_l:
                    hit_a = {a for kk, aa in self.by_loose_combo.items() if prefix_match(lk, kk) for a in aa}
                    hit_l = {x for kk, xx in self.lst_loose_combo.items() if prefix_match(lk, kk) for x in xx}
                if hit_a or hit_l:
                    mode = "combo-loose"
        else:
            terms, salt_named = single_terms(ings[0] if ings else inn)
            hit_a, hit_l = set(), set()
            for t in terms:
                hit_a |= self.by_ing.get((t, salt_named), set())
                hit_l |= self.lst_ing.get((t, salt_named), set())
                if t in ORGANIC_BASES and not salt_named:
                    hit_a |= self.by_ing.get((t, "org"), set())
                    hit_l |= self.lst_ing.get((t, "org"), set())
            mode = "single"
            if not hit_a and not hit_l and not salt_named:
                for t in {loose(t) for t in terms} - {""}:  # 整個名字都是鹽類字（procaine、arginine）時寬鬆鍵是空的，不比
                    hit_a |= self.by_loose.get(t, set())
                    hit_l |= self.lst_loose.get(t, set())
                if hit_a or hit_l:
                    mode = "single-loose"

        def app_rec(a):
            e = self.apps[a]
            ps = [p for p in e["products"] if mode == "combo" and combo_key(p["ings"]) == combo_key(ings)
                  or mode == "single" and any((base(c, keep_salt=salt_named) in terms or org_base(c) in terms & ORGANIC_BASES) for c in p["ings"])
                  or mode == "single-loose" and any(loose(c) in {loose(t) for t in terms} - {""} for c in p["ings"])] or e["products"]
            ps = sorted(ps, key=lambda p: (not p["active"], len(p["ings"])))
            p = ps[0]
            return {"license_id": a, "brand_name_zh": p["brand"], "brand_name_en": p["brand"], "ingredients": "; ".join(p["ings"]), "indication": "",
                    "dosage_form": p["form"], "manufacturer": e["sponsor"], "license_holder": e["sponsor"], "approval_date": e["date"], "expiry_date": "",
                    "status": e["status"], "route": p["route"], "source": e.get("source") or f"Drugs@FDA (openFDA {self.updated})",
                    "_sort": (not e["active"], min(len(q["ings"]) for q in ps), a)}
        recs = sorted((app_rec(a) for a in hit_a), key=lambda r: r["_sort"])
        for r in recs:
            r.pop("_sort")
        L = self.listings
        lk = sorted(hit_l, key=lambda k: (len(L[k]["ings"]), k))
        lrecs = [{"license_id": L[k]["id"] or "Not applicable", "product_ndc": k, "brand_name_zh": L[k]["brand"], "brand_name_en": L[k]["brand"],
                  "ingredients": "; ".join(L[k]["ings"]), "indication": "", "dosage_form": L[k]["form"], "manufacturer": L[k]["maker"],
                  "license_holder": L[k]["maker"], "approval_date": "", "expiry_date": "", "status": L[k]["cat"], "listing": True,
                  "source": "FDA NDC Directory listing (no FDA application)"} for k in lk[:MAX_LISTING_RECORDS]]
        data = {"found": bool(recs or lrecs), "records": recs + lrecs, "total_matches": len(recs) + len(hit_l), "listed_total": len(hit_l),
                "applications_total": len(recs)}
        return data, mode

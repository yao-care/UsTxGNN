"""依成分比對（us_license_match）的規則測試：rebuild 腳本與 collectors/usfda.py 共用。"""
from ustxgnn.collectors import us_license_match as lm


def _app(appl, ings, status="Prescription"):
    return {"application_number": appl, "sponsor_name": "X", "submissions": [],
            "products": [{"brand_name": appl, "dosage_form": "TABLET", "route": "ORAL", "marketing_status": status,
                          "active_ingredients": [{"name": i} for i in ings]}]}


def _ndc(code, ings, cat="OTC MONOGRAPH DRUG", appl="M012"):
    return {"ndc": code, "appl": appl, "cat": cat, "ings": ings, "brand": code, "form": "CREAM", "route": "TOPICAL", "maker": "Y", "date": ""}


DFDA = [
    _app("NDA000001", ["ACETAMINOPHEN", "CODEINE PHOSPHATE"]),
    _app("ANDA000002", ["ACETAMINOPHEN"]),
    _app("ANDA000003", ["ACETAMINOPHEN"], status="Discontinued"),
    _app("ANDA000004", ["ACETAMINOPHEN"], status="None (Tentative Approval)"),
    _app("NDA000005", ["LIDOCAINE"]),
]
NDC = [
    _ndc("1-1", ["4-METHYLBENZYLIDENE CAMPHOR", "HYDROLYSED MARINE COLLAGEN (ENZYMATIC", "2000 MW)"]),
    _ndc("1-2", ["ACETAMINOPHEN"]),
    _ndc("1-3", ["ACETAMINOPHEN"], cat="ANDA", appl="ANDA000002"),  # Drugs@FDA 已有的申請號不重算
]
IDX = lm.LicenseIndex(DFDA, "2026-11-05", NDC, "2026-11-05")


def test_semicolon_inside_parentheses_is_one_ingredient():
    assert lm.split_ings("A; COLLAGEN (ENZYMATIC; 2000 MW); B") == ["A", "COLLAGEN (ENZYMATIC; 2000 MW)", "B"]
    assert lm.split_ings(["COLLAGEN (ENZYMATIC", "2000 MW)"]) == ["COLLAGEN (ENZYMATIC; 2000 MW)"]


def test_combo_requires_identical_ingredient_set():
    d, mode = IDX.match("ACETAMINOPHEN; CODEINE")
    assert mode == "combo" and [r["license_id"] for r in d["records"]] == ["NDA000001"]


def test_single_counts_applications_and_listings_separately_without_tentative():
    d, _ = IDX.match("ACETAMINOPHEN")
    ids = [r["license_id"] for r in d["records"] if not r.get("listing")]
    assert set(ids) == {"NDA000001", "ANDA000002", "ANDA000003"}  # 暫定核准 ANDA000004 不收
    assert ids[-1] == "ANDA000003"  # 已停產排後面
    assert d["applications_total"] == 3 and d["listed_total"] == 1 and d["total_matches"] == 4


def test_combo_listing_with_parenthesised_semicolon():
    d, _ = IDX.match("4-METHYLBENZYLIDENE CAMPHOR; HYDROLYSED MARINE COLLAGEN")
    assert d["applications_total"] == 0 and d["listed_total"] == 1 and d["found"]


def test_salt_word_component_is_not_dropped():
    d, _ = IDX.match("ARGININE; LIDOCAINE")
    assert not d["found"]


def test_organic_base_single_page_matches_its_salts_only():
    idx = lm.LicenseIndex([_app("ANDA000010", ["PROCAINE HYDROCHLORIDE"], status="Discontinued"),
                           _app("NDA000011", ["PENICILLIN G PROCAINE"])], "", [], "")
    d, _ = idx.match("PROCAINE")
    assert [r["license_id"] for r in d["records"]] == ["ANDA000010"]


def test_same_substance_alias_matches_combo_both_ways():
    # FDA GSRS UNII I76KB35JEV：ANEMONE PULSATILLA＝PULSATILLA VULGARIS WHOLE（2026-11-06）
    idx = lm.LicenseIndex([], "", [_ndc("43857-0341", ["ACTIVATED CHARCOAL", "PULSATILLA VULGARIS WHOLE", "ZINC"], cat="UNAPPROVED HOMEOPATHIC", appl="")], "")
    d, mode = idx.match("ACTIVATED CHARCOAL; ANEMONE PULSATILLA; ZINC")
    assert mode == "combo" and d["listed_total"] == 1
    # 不同部位（PULSATILLA VULGARIS TOP，UNII 4F1D271XW0）不併
    idx = lm.LicenseIndex([], "", [_ndc("2-1", ["ACTIVATED CHARCOAL", "PULSATILLA VULGARIS TOP", "ZINC"], cat="UNAPPROVED HOMEOPATHIC", appl="")], "")
    assert not idx.match("ACTIVATED CHARCOAL; ANEMONE PULSATILLA; ZINC")[0]["found"]


def test_mthf_is_not_levomefolate():
    # GSRS：5-METHYLTETRAHYDROFOLIC ACID（TYK22LML8F，差向異構物混合物）≠ LEVOMEFOLATE CALCIUM（A9R10K3F2F）
    idx = lm.LicenseIndex([], "", [_ndc("75854-313", ["FOLIC ACID", "LEVOMEFOLATE CALCIUM"], cat="UNAPPROVED DRUG OTHER", appl="")], "")
    assert not idx.match("FOLIC ACID; 5-METHYLTETRAHYDROFOLIC ACID")[0]["found"]

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


def test_salts_and_names_of_same_active_moiety_2026_11_06():
    # GSRS ACTIVE MOIETY 是母藥：ethylsuccinate／lactobionate（erythromycin）、diolamine（treprostinil）、D-tartrate（nilotinib）；
    # ziv-aflibercept＝aflibercept；MECASERMIN RECOMBINANT＝mecasermin；DEXTROMETHORPHAN POLISTIREX＝dextromethorphan
    idx = lm.LicenseIndex([_app("NDA050207", ["ERYTHROMYCIN ETHYLSUCCINATE"]), _app("NDA050609", ["ERYTHROMYCIN LACTOBIONATE"]),
                           _app("NDA203496", ["TREPROSTINIL DIOLAMINE"]), _app("NDA218922", ["NILOTINIB D-TARTRATE"]),
                           _app("BLA125418", ["ZIV-AFLIBERCEPT"]), _app("BLA021839", ["MECASERMIN RECOMBINANT"]),
                           _app("NDA018658", ["DEXTROMETHORPHAN POLISTIREX"]), _app("NDA000099", ["MECASERMIN RINFABATE"]),
                           _app("NDA019111", ["CHLORPHENIRAMINE POLISTIREX; HYDROCODONE POLISTIREX"])], "", [], "")
    ids = lambda inn: {r["license_id"] for r in idx.match(inn)[0]["records"]}  # noqa: E731
    assert ids("ERYTHROMYCIN") == {"NDA050207", "NDA050609"}
    assert ids("TREPROSTINIL") == {"NDA203496"} and ids("NILOTINIB") == {"NDA218922"}
    assert ids("AFLIBERCEPT") == {"BLA125418"} and ids("MECASERMIN") == {"BLA021839"}  # rinfabate 不併
    assert ids("DEXTROMETHORPHAN") == {"NDA018658"}
    assert ids("CHLORPHENIRAMINE") == {"NDA019111"}  # 2026-11-06 查證後併（GSRS SUB_CONCEPT）
    assert ids("ERYTHROMYCIN LACTOBIONATE") == {"NDA050609"}  # 名稱帶鹽類時只收同一個鹽


def test_recombinant_hyaluronidase_is_not_hyaluronidase():
    # GSRS：Hyaluronidase (Human Recombinant) 743QUY4VD8（含 hyaluronidase-oysk 等）≠ HYALURONIDASE 8KOG53Z5EM（2026-11-06 用戶決定）
    idx = lm.LicenseIndex([_app("BLA021665", ["HYALURONIDASE"]), _app("BLA021859", ["HYALURONIDASE RECOMBINANT HUMAN"]),
                           _app("BLA761106", ["TRASTUZUMAB AND HYALURONIDASE-OYSK"]),
                           _app("BLA761064", ["HYALURONIDASE (HUMAN RECOMBINANT)", "RITUXIMAB"])], "", [], "")
    ids = lambda inn: {r["license_id"] for r in idx.match(inn)[0]["records"]}  # noqa: E731
    assert ids("HYALURONIDASE") == {"BLA021665"}
    assert ids("TRASTUZUMAB") == {"BLA761106"}  # 組合產品仍算 trastuzumab
    assert ids("HYALURONIDASE (HUMAN RECOMBINANT); RITUXIMAB") == {"BLA761064"}


def test_zinc_sulfate_is_unspecified_form():
    # GSRS：ZINC SULFATE 是 89DS0H96TB（ZINC SULFATE, UNSPECIFIED FORM）的名稱
    idx = lm.LicenseIndex([_app("ANDA218059", ["ZINC SULFATE"])], "", [_ndc("2-2", ["ZINC SULFATE, UNSPECIFIED FORM", "TETRAHYDROZOLINE HYDROCHLORIDE"])], "")
    assert {r["license_id"] for r in idx.match("ZINC SULFATE, UNSPECIFIED FORM")[0]["records"] if not r.get("listing")} == {"ANDA218059"}
    assert idx.match("TETRAHYDROZOLINE HYDROCHLORIDE; ZINC SULFATE")[0]["listed_total"] == 1

"""藥物頁許可證表依證據包重排（scripts/sync_license_tables.py）的規則測試。"""
import importlib.util
import re
from pathlib import Path

_p = Path(__file__).resolve().parents[1] / "scripts/sync_license_tables.py"
_s = importlib.util.spec_from_file_location("sync_license_tables", _p)
st = importlib.util.module_from_spec(_s)
_s.loader.exec_module(st)

TF = {"applications_total": 2, "listed_total": 1, "records": [
    {"license_id": "ANDA000001", "brand_name_en": "PROCAINE HYDROCHLORIDE", "manufacturer": "HOSPIRA", "dosage_form": "INJECTABLE",
     "route": "INJECTION", "status": "ANDA (Discontinued in Drugs@FDA)"},
    {"license_id": "NDA000002", "brand_name_en": "NOVOCAIN", "manufacturer": "X", "dosage_form": "INJECTABLE", "route": "INJECTION", "status": "NDA"},
    {"license_id": "M017", "product_ndc": "1-1", "listing": True, "brand_name_en": "NUMB", "manufacturer": "Y", "dosage_form": "OINTMENT",
     "status": "OTC MONOGRAPH DRUG"}]}
PAGE = ["## US Market Information", "", "| Authorization Number | Product Name | Dosage Form | Approved Indication |", "|---|---|---|---|",
        "| NDA050138 | BICILLIN C-R | Injection | Not specified (valid) |", "", "## Safety Considerations"]


def test_foreign_application_triggers_resync_and_table_follows_facts():
    assert st.needs_resync(PAGE, TF).startswith("表格列了不屬於本藥的申請號")
    out = st.render(PAGE, TF, {"licenses": {"ANDA000001": "cancelled", "NDA000002": "valid"}})
    rows = [l for l in out if l.startswith("| ")][1:]
    assert out[2] == st.HEAD and "NDA050138" not in "\n".join(out)
    assert rows[0].startswith("| ANDA000001 ") and rows[0].endswith("| Discontinued in Drugs@FDA |")
    assert rows[1].endswith("| Valid |") and rows[2].startswith("| NDC 1-1 |") and "no FDA application" in rows[2]
    assert not any(st.SHOW_RX.match(l) for l in out)  # 3 列全部顯示，不加 SHOW 句
    assert st.needs_resync(out, TF) == "程式產生的表格"
    assert st.render(out, TF, {"licenses": {"ANDA000001": "cancelled", "NDA000002": "valid"}}) == out  # 重跑不變


def test_show_line_and_none_line():
    big = dict(TF, applications_total=40)
    out = st.render(PAGE, big, {})
    assert any(re.match(r"^Showing 3 of 41 entries", l) for l in out)
    out = st.render(PAGE, {"records": [], "applications_total": 0, "listed_total": 0}, {})
    assert st.NONE_LINE in out and not any(l.startswith("|") for l in out)


def test_other_drug_standalone_note_is_not_a_trigger():
    page = PAGE[:2] + ["Arsenic Trioxide as a standalone drug is marketed in the US (Trisenox, NDA 021248)."] + PAGE[1:]
    page = [l for l in page if "NDA050138" not in l]
    assert st.needs_resync(page, TF) == ""


def test_row_status_conflict_triggers_resync():
    page = PAGE[:4] + ["| NDA000002 (cancelled) | NOVOCAIN | Injection | Not specified |"] + PAGE[5:]
    tf = dict(TF)
    hits = lambda rows: [("M1", r[0]) for r in rows if "(cancelled)" in r[0]]  # noqa: E731（checker 的 row_status_conflicts 代用）
    assert st.needs_resync(page, tf) == ""
    assert st.needs_resync(page, tf, hits).startswith("表格列的狀態字跟事實層不一致")

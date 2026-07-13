---
layout: default
title: Daunorubicin
parent: 僅模型預測 (L5)
nav_order: 574
evidence_level: L5
indication_count: 10
---

# Daunorubicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Daunorubicin: From Acute Leukemia to Hodgkin's Lymphoma

## One-Sentence Summary

Daunorubicin is a first-generation anthracycline antibiotic established as a cornerstone treatment for acute myeloid leukemia (AML) and acute lymphoblastic leukemia (ALL).
The TxGNN model predicts it may be effective for **Hodgkin's Lymphoma**,
with **50 clinical trials** and **20 publications** currently supporting this direction.
Direct daunorubicin evidence in lymphoma is limited to an early-phase study using the liposomal formulation, while strong class-level evidence derives from doxorubicin-containing anthracycline regimens that are the standard of care for this disease.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute leukemia (AML/ALL) — known pharmacological use; no FDA license records found in dataset |
| Predicted New Indication | Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L2 |
| US Market Status | Not found in dataset (possible data gap — Cerubidine® is historically FDA-approved for acute leukemia) |
| Number of NDAs | 0 records retrieved |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the dataset. Based on established pharmacology, daunorubicin is an anthracycline antibiotic that exerts its antitumor effect through two complementary mechanisms: intercalation into the DNA double helix, which physically blocks DNA replication and transcription, and inhibition of topoisomerase II, which prevents the re-ligation of DNA strands after topoisomerase-induced strand breakage. This ultimately results in accumulation of DNA double-strand breaks and apoptosis of rapidly proliferating cells. Generation of reactive oxygen species (ROS) further amplifies cytotoxic damage.

The mechanistic link to Hodgkin's Lymphoma is direct and well-established at the drug-class level. The standard frontline regimen for HL — ABVD (Adriamycin/doxorubicin, Bleomycin, Vinblastine, Dacarbazine) — is built on doxorubicin, a structural analog of daunorubicin that differs only by a C-14 hydroxyl group. Both agents share the same anthracycline scaffold, topoisomerase II inhibition, and DNA intercalation mechanism. Reed-Sternberg cells, the hallmark malignant cells of classical HL, are highly proliferative and constitutively activate NF-κB signaling — a pathway shown to be directly disrupted by doxorubicin/etoposide combinations in HL cell lines (PMID 32053083). Daunorubicin shares this NF-κB-disrupting potential.

Importantly, liposomal daunorubicin (DaunoXome) has already been tested directly in relapsed/refractory lymphoma patients (PMID 9387047): at a dose of 120 mg/m², 1 complete response and 2 partial responses were observed in 9 evaluable patients, with a favorable cardiac safety profile. The TxGNN model's prediction therefore reflects both the molecular topology of daunorubicin in the knowledge graph (proximity to doxorubicin and established lymphoma treatment nodes) and biologically coherent class-level translatability.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01712490](https://clinicaltrials.gov/study/NCT01712490) | Phase 3 | Completed | 1,334 | Pivotal trial: Brentuximab vedotin + AVD (doxorubicin-containing) vs ABVD in advanced classical HL; established A+AVD as a new frontline standard with improved modified PFS |
| [NCT00049595](https://clinicaltrials.gov/study/NCT00049595) | Phase 3 | Completed | 552 | BEACOPP escalated ×4 + baseline ×4 versus ABVD ×8 in Stage III/IV HL; confirmed doxorubicin-containing regimens as backbone for advanced HL |
| [NCT04685616](https://clinicaltrials.gov/study/NCT04685616) | Phase 3 | Recruiting | 1,042 | RADAR trial: PET response-adapted A2VD vs ABVD ± involved-site RT in Stage IA/IIA HL; international multicentre design, completion expected 2032 |
| [NCT03755804](https://clinicaltrials.gov/study/NCT03755804) | Phase 2 | Active, not recruiting | 232 | cHOD17: Pediatric risk- and response-adapted therapy for classical HL using BEABOVP (low/intermediate risk) and BV+etoposide+prednisone+doxorubicin (high risk) |
| [NCT06377566](https://clinicaltrials.gov/study/NCT06377566) | Phase 2 | Recruiting | 71 | BV-AVD (brentuximab vedotin + doxorubicin, vinblastine, dacarbazine) in newly diagnosed early-stage bulky HL; PET-adapted and MTV-guided approach |
| [NCT03527628](https://clinicaltrials.gov/study/NCT03527628) | Phase 2 | Unknown | 220 | ACVD + Brentuximab Vedotin in PET-2 positive advanced-stage HL after 2 ABVD cycles; aims to improve long-term disease control in high-risk patients |
| [NCT03517137](https://clinicaltrials.gov/study/NCT03517137) | Phase 2 | Active, not recruiting | 150 | Very early PET-adapted BV-containing regimens in advanced HL; assesses whether treatment adaptation by early FDG-PET improves efficacy while minimizing toxicity |
| [NCT01534078](https://clinicaltrials.gov/study/NCT01534078) | Phase 2 | Completed | 34 | Brentuximab vedotin + AVD in non-bulky limited-stage HL; seeks to eliminate radiation therapy and reduce bleomycin exposure |
| [NCT00398554](https://clinicaltrials.gov/study/NCT00398554) | Phase 2 | Completed | 16 | VECOPA combination (etoposide, cyclophosphamide, vincristine, prednisone, adriamycin) in young male patients with intermediate/advanced HL; pediatric therapy optimization pilot |
| [NCT02191930](https://clinicaltrials.gov/study/NCT02191930) | Phase 2 | Completed | 70 | Brentuximab vedotin or B-CAP in older (≥60 years) newly diagnosed classical HL patients; evaluated ORR and 3-year PFS in a population often underrepresented in HL trials |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39413375](https://pubmed.ncbi.nlm.nih.gov/39413375/) | 2024 | Phase 3 RCT | N Engl J Med | Nivolumab + AVD (doxorubicin-containing) in advanced-stage classical HL; PD-1 blockade combined with anthracycline backbone improves outcomes vs historical ABVD benchmarks |
| [35830649](https://pubmed.ncbi.nlm.nih.gov/35830649/) | 2022 | Phase 3 follow-up | N Engl J Med | 5-year OS analysis of A+AVD vs ABVD in Stage III/IV HL; confirmed long-term OS benefit with BV + doxorubicin combination, establishing anthracyclines as irreplaceable in HL backbone |
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | Phase I/II | Investig New Drugs | **Direct daunorubicin evidence:** Liposomal daunorubicin (DaunoXome) in 19 relapsed/refractory lymphoma patients; 40 mg/m² q14d showed no responses; 120 mg/m² q21d achieved 1 CR + 2 PR in 9 patients; no clinical cardiac deterioration at higher dose |
| [378369](https://pubmed.ncbi.nlm.nih.gov/378369/) | 1979 | Historical Analysis | Cancer Treat Rep | **Direct daunorubicin comparison:** Comparative analysis of daunorubicin and adriamycin (doxorubicin) roles and limitations in cancer treatment; early evidence establishing differential activity of these two anthracyclines across tumor types |
| [36271128](https://pubmed.ncbi.nlm.nih.gov/36271128/) | 2022 | Retrospective Cohort | Sci Rep | Interim FDG-PET/CT after 2 ABVD cycles predicted outcomes in 245 de novo HL patients; iPET2-negative patients had significantly better PFS and OS, validating response-adapted anthracycline-based therapy |
| [35843924](https://pubmed.ncbi.nlm.nih.gov/35843924/) | 2022 | Cohort / Milestone Review | Prilozi (MAN) | Longitudinal analysis of HL management over decades; documents dramatic improvement in survival rates correlated with introduction of doxorubicin-based combination regimens |
| [28365830](https://pubmed.ncbi.nlm.nih.gov/28365830/) | 2017 | Review | Curr Oncol Rep | Current role of radiotherapy in early-stage HL within risk-adapted and response-adapted frameworks; contextualizes anthracycline chemotherapy as the primary active partner in combined modality therapy |
| [32053083](https://pubmed.ncbi.nlm.nih.gov/32053083/) | 2020 | Translational | Anti-Cancer Agents | Benzisothiazolone derivatives showed NF-κB inhibition and cytotoxicity in L428 HL cells (constitutively NF-κB active); synergistic effects with doxorubicin and etoposide confirmed — mechanistically relevant to anthracycline activity in HL |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | Review | Gan To Kagaku Ryoho | Review of hematologic tumor treatment milestones; explicitly notes daunorubicin + cytarabine development enabled AML cure, while ABVD became standard for advanced HL based on randomized data |
| [21774715](https://pubmed.ncbi.nlm.nih.gov/21774715/) | 2011 | Editorial | N Engl J Med | "Hodgkin's lymphoma — the great teacher": perspective on how HL research shaped modern oncology, including the central role of doxorubicin-containing combination chemotherapy in transforming survival outcomes |

---

## US Market Information

No FDA license records were retrieved for daunorubicin in the current dataset (`total_licenses: 0`). This likely reflects a data collection gap: daunorubicin hydrochloride (Cerubidine®, Bedford Laboratories/Pfizer) has been FDA-approved since the 1970s for remission induction in AML and ALL. The absence of records in this dataset should not be interpreted as lack of regulatory approval.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | No records retrieved in dataset | — | — |

---

## Cytotoxicity

Daunorubicin is a conventional cytotoxic anthracycline antibiotic (antineoplastic agent). It is structurally and mechanistically classified alongside doxorubicin as a Type II topoisomerase poison with intercalating and ROS-generating properties.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline (Type IIA topoisomerase inhibitor / DNA intercalator) |
| Myelosuppression Risk | **High** — Dose-limiting toxicity is myelosuppression; nadir typically at days 10–14 post-infusion; neutropenia, thrombocytopenia, and anemia are common and expected; growth factor support is routinely required in combination regimens |
| Emetogenicity Classification | Moderate to High — Daunorubicin at standard doses (45–60 mg/m²) requires prophylactic antiemetic therapy including 5-HT₃ antagonist ± NK₁ receptor antagonist |
| Monitoring Items | CBC with differential (nadir days 10–14), liver function tests (biliary excretion — dose reduction required for bilirubin >1.2 mg/dL), renal function, serial cardiac function assessment (LVEF by echocardiogram or MUGA) prior to and during treatment; cumulative lifetime daunorubicin dose limit ~550 mg/m² (lower with prior mediastinal RT or cardiac risk factors) |
| Handling Protection | **Yes** — Must be handled under cytotoxic drug handling regulations; preparation in a certified biological safety cabinet by trained pharmacy personnel; use of PPE (gloves, gown, face shield); disposal per RCRA hazardous waste standards |

---

## Safety Considerations

Safety data from the TFDA package insert (warnings and contraindications) and drug–drug interaction database are not available in the current dataset. Based on the drug class profile:

- **Cardiotoxicity**: Cumulative dose-dependent cardiomyopathy is the most clinically significant long-term risk; irreversible congestive heart failure may occur at lifetime cumulative doses >550 mg/m² (lower threshold with prior cardiac disease or mediastinal radiation). LVEF monitoring is mandatory.
- **Vesicant risk**: Daunorubicin is a potent vesicant; extravasation causes severe local tissue necrosis requiring immediate management.
- **Secondary malignancies**: As a topoisomerase II inhibitor, risk of therapy-related AML (t-AML) with characteristic 11q23 rearrangements has been documented, particularly with prolonged or high cumulative exposure.

For complete warnings, contraindications, and drug interaction information, please refer to the current Cerubidine® package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials confirm that anthracyclines (specifically doxorubicin) are foundational to curative treatment of Hodgkin's Lymphoma at the class level, and a direct Phase I/II study of liposomal daunorubicin in relapsed/refractory lymphoma demonstrated objective responses at 120 mg/m², establishing proof-of-concept for this specific agent. However, doxorubicin is already the established standard within ABVD and A+AVD regimens, meaning daunorubicin's repurposing value lies primarily in scenarios where doxorubicin is contraindicated (severe cardiac dysfunction) or as an alternative formulation (e.g., liposomal daunorubicin with favorable cardiac profile).

**To proceed, the following is needed:**

- **Mechanism of action documentation**: Retrieve full MOA data from DrugBank (DB00694) to formally confirm topoisomerase II inhibition and DNA intercalation as actionable mechanisms in Reed-Sternberg cells
- **Head-to-head pharmacological comparison**: Clarify differential tissue distribution, cardiac toxicity profile, and relative potency of daunorubicin vs. doxorubicin in lymphoma models, given the structural difference (C-14 hydroxyl)
- **Liposomal formulation assessment**: Evaluate whether liposomal daunorubicin (DaunoXome, where available) offers a clinically meaningful cardiac-sparing advantage for HL patients ineligible for standard doxorubicin
- **Regulatory status verification**: Confirm current US FDA approval status, NDA numbers, and label indications for daunorubicin HCl to address the dataset gap
- **TFDA package insert review**: Obtain warnings, contraindications, and DDI data to complete safety profiling (Blocking data gap DG001)
- **Niche population identification**: Define the specific HL patient subpopulation (e.g., pre-existing cardiomyopathy, prior anthracycline exposure) where daunorubicin substitution would provide clinical added value over doxorubicin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


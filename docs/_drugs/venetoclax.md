---
layout: default
title: Venetoclax
parent: 僅模型預測 (L5)
nav_order: 1286
evidence_level: L5
indication_count: 10
---

# Venetoclax
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

# Venetoclax (DB11581): A BCL-2 Inhibitor with a Multi-Indication Prediction Portfolio

## One-Sentence Summary

Venetoclax is a selective BCL-2 inhibitor; this evidence pack does not contain confirmed original-indication or TFDA label data for the Taiwan market (drug is currently **not marketed** in Taiwan, 0 licenses), so the "from → to" framing used for single-indication reports does not apply cleanly here. Instead, TxGNN generated **10 candidate indications** for this drug, with wildly varying evidence quality — ranging from a well-supported, guideline-relevant signal for **acute myeloid leukemia (AML)** (50+ trials, 20+ publications, Phase 3 RCTs) down to a single unsupported prediction for **malignant spiradenoma** (zero trials, zero literature). Because of this spread, the report below evaluates the portfolio as a whole and flags data-quality concerns (including a likely ontology-mislabeling issue in the Hodgkin lymphoma entry) rather than presenting one indication as "the" prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — TFDA label and original indication data are a **Blocking data gap (DG001)**; background pharmacology indicates venetoclax is an internationally used BCL-2 inhibitor (CLL/SLL, AML), but this is not confirmed in-dataset |
| Predicted New Indication | 10 candidates (multi-indication pack); top-ranked by TxGNN score: *CLL/SLL with IGHV somatic hypermutation* — but the most clinically actionable is *myeloid leukemia (AML)* (Rank 4) |
| TxGNN Prediction Score | Rank 1: 99.55% · Rank 4 (AML): 99.47% · range across portfolio: 99.08%–99.55% |
| Evidence Level | Highly variable: **L1** (AML) down to **L5** (malignant spiradenoma) — see portfolio table below |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | **Indication-specific** — Proceed with Guardrails (AML); Research Question (CML, follicular lymphoma, CLL/SLL subtypes); **Hold** (Hodgkin lymphoma, metastatic neoplasm, Ewing sarcoma, malignant spiradenoma) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from DrugBank is marked as a data gap (DG002) in this pack. Based on the mechanistic rationale embedded in the individual predictions, venetoclax is a **selective, orally bioavailable BCL-2 antagonist** that restores apoptosis in malignant cells that depend on BCL-2 overexpression for survival — the "BH3-mimetic" mechanism. This is consistent across nearly every candidate in this portfolio, since BCL-2 dependency is a shared vulnerability across many B-cell and myeloid malignancies.

**Portfolio Overview (all 10 candidates):**

| Rank | Predicted Indication | Score | Evidence Level | Decision Stage | Recommendation | Key Note |
|------|----------------------|-------|-----------------|-----------------|-----------------|----------|
| 4 | Myeloid leukemia (AML) | 99.47% | **L1** | S3 | **Proceed with Guardrails** | Core, already-validated venetoclax use (FDA-approved combo with azacitidine/LDAC); strongest evidence in the pack |
| 5 | Chronic myelogenous leukemia, BCR-ABL1+ (CML) | 99.36% | L2 | S2 | Research Question | Stem-cell-eradication hypothesis on top of TKI therapy; Phase 2 trials only |
| 7 | Follicular lymphoma | 99.15% | L2 | S2 | Research Question | t(14;18)-driven BCL-2 overexpression is a strong mechanistic fit; multiple Phase 1/2 combos, no Phase 3 yet |
| 1 | CLL/SLL (IGHV-mutated subtype) | 99.55% | L4 | S1 | Research Question | Mechanistically sound (CLL is a core BCL-2-dependent malignancy) but **zero trials/literature for this specific IGHV subtype** in the pack |
| 2 | Pre-germinal-center CLL/SLL | 99.55% | L4 | S1 | Research Question | Same as above; only supporting literature is a descriptive BCR-biology review, not efficacy data |
| 10 | AML with t(8;21) translocation | 99.08% | L4 | S1 | Research Question | Reasonable extrapolation from the AML entry above, but zero trials/literature specific to this cytogenetic subtype |
| 6 | Ewing sarcoma | 99.21% | L4 | S0 | Hold | Preclinical rationale only (BCL-2/BCL-XL dependency in some cell lines); **zero clinical trials** |
| 3 | Hodgkin lymphoma | 99.51% | L4 | S0 | **Hold** | ⚠️ **Likely ontology mislabeling** — all 50 trials and 20 papers listed actually describe *non*-Hodgkin lymphoma (CLL/MCL/DLBCL/FL); no genuine classical Hodgkin lymphoma evidence is present |
| 8 | Metastatic neoplasm | 99.14% | L4 | S0 | **Hold** | Non-specific KG node; cited evidence spans breast cancer, AML, ALL, neuroblastoma — not an actionable single indication |
| 9 | Malignant spiradenoma | 99.12% | **L5** | S0 | **Hold** | Zero trials, zero literature; prediction-only with no biological or clinical corroboration |

**Interpretation:** The pack's own rationale text for AML explicitly notes this is "not a hypothesis" — venetoclax + azacitidine/LDAC is already a validated, guideline-endorsed first-line AML regimen internationally. Since Taiwan market status shows "not marketed" and original indication is a data gap, this most plausibly reflects a **jurisdictional gap** (drug not yet registered locally) rather than a genuinely novel biological hypothesis. In contrast, several other entries (Hodgkin lymphoma, metastatic neoplasm, malignant spiradenoma) look like **knowledge-graph noise** — either mislabeled evidence linkage or prediction with no supporting signal at all — and should not be advanced without independent verification.

---

## Clinical Trial Evidence (Lead Candidate: Myeloid Leukemia / AML)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03573024](https://clinicaltrials.gov/study/NCT03573024) | Phase 2 | Active, not recruiting | 36 | Venetoclax + azacitidine in newly diagnosed non-elderly (18–59) AML |
| [NCT07486479](https://clinicaltrials.gov/study/NCT07486479) | Phase 3 | Not yet recruiting | 204 | RCT: venetoclax + azacitidine + mitoxantrone liposome vs. idarubicin + cytarabine ("3+7") in newly diagnosed AML |
| [NCT06046313](https://clinicaltrials.gov/study/NCT06046313) | Phase 2 | Recruiting | 120 | Prolonged ultra-low-dose decitabine + venetoclax in elderly/high-risk AML and MDS |
| [NCT06782542](https://clinicaltrials.gov/study/NCT06782542) | Phase 2 | Recruiting | 16 | Olutasidenib + venetoclax + azacitidine in IDH1-mutated newly diagnosed AML |
| [NCT05520567](https://clinicaltrials.gov/study/NCT05520567) | Phase 1/2 | Active, not recruiting | 70 | Gilteritinib + venetoclax + azacitidine in FLT3-mutated AML unfit for intensive induction |
| [NCT05317494](https://clinicaltrials.gov/study/NCT05317494) | N/A (real-world) | Recruiting | 100 | Non-interventional study of venetoclax as first-line therapy in intensive-chemo-ineligible AML (Greece) |
| [NCT04824924](https://clinicaltrials.gov/study/NCT04824924) | Phase 2 | Unknown | 100 | Venetoclax + low-dose HHT + G-CSF + azacitidine in elderly unfit newly diagnosed AML |
| [NCT03844815](https://clinicaltrials.gov/study/NCT03844815) | Phase 1 | Active, not recruiting | 26 | Venetoclax + 10-day decitabine regimen safety/tolerability in AML |

---

## Literature Evidence (Lead Candidate: AML)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34329576](https://pubmed.ncbi.nlm.nih.gov/34329576/) | 2021 | Cohort, single-arm Phase 2 | The Lancet Haematology | Venetoclax + cladribine/idarubicin/cytarabine (CLIA) in newly diagnosed AML/high-risk MDS, patients ≤65 years |
| [35046058](https://pubmed.ncbi.nlm.nih.gov/35046058/) | 2022 | Cohort | Clinical Cancer Research | Venetoclax + azacitidine efficacy/safety in treatment-naïve IDH1/2-mutant AML |
| [37599456](https://pubmed.ncbi.nlm.nih.gov/37599456/) | 2024 | Network meta-analysis | Journal of Chemotherapy | Indirect comparison: venetoclax+azacitidine vs. ivosidenib/enasidenib in unfit IDH1/2-mutant AML; VEN-AZA showed superior OS |
| [39303729](https://pubmed.ncbi.nlm.nih.gov/39303729/) | 2024 | Single-arm Phase 2 | The Lancet Haematology | Decitabine + venetoclax + ponatinib in advanced-phase Ph+ CML and Ph+ AML |
| [37925935](https://pubmed.ncbi.nlm.nih.gov/37925935/) | 2023 | Review | Biomedicine & Pharmacotherapy | Summary of venetoclax mono/combination efficacy across AML preclinical and clinical studies |
| [31203996](https://pubmed.ncbi.nlm.nih.gov/31203996/) | 2019 | Review | Best Practice & Research Clinical Haematology | Overview of venetoclax-based therapies within the broader new-drug landscape for AML |
| [32031033](https://pubmed.ncbi.nlm.nih.gov/32031033/) | 2020 | Review | Leukemia & Lymphoma | Venetoclax + HMA/LDAC established as new frontline standard of care in older/unfit AML |
| [39246164](https://pubmed.ncbi.nlm.nih.gov/39246164/) | 2024 | Review | Expert Review of Hematology | Relapse and resistance patterns after venetoclax-based AML therapy; second-line strategies |

---

## Taiwan Market Information

Venetoclax currently has **no marketing authorization recorded in Taiwan** (market status: 未上市 / Not Marketed; 0 licenses on file). No license table can be generated from this dataset.

---

## Cytotoxicity

Venetoclax's indications across this portfolio are predominantly hematologic malignancies (leukemia, lymphoma), and it is a well-established antineoplastic/targeted oncology agent, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — selective BCL-2 (BH3-mimetic) inhibitor; not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | High — neutropenia is a common, sometimes dose-limiting toxicity, particularly in combination regimens (e.g., + azacitidine/decitabine); thrombocytopenia also reported |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (regular); tumor lysis syndrome labs during initiation/dose ramp-up (potassium, phosphate, calcium, uric acid, creatinine); renal and hepatic function |
| Handling Protection | Yes — despite being an oral targeted agent, venetoclax is classified as a hazardous antineoplastic drug and requires handling per institutional cytotoxic/hazardous drug protocols, especially given tumor lysis syndrome risk requiring structured dose ramp-up |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are not available in this dataset — TFDA label retrieval is a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Indication-Specific — Proceed with Guardrails (AML only); Hold on the majority of remaining candidates**

**Rationale:**
- The AML candidate (Rank 4) is backed by L1 evidence, including a Phase 3 RCT and an established, internationally used venetoclax + hypomethylating-agent regimen — this is the only candidate in the portfolio warranting active progression.
- CML and follicular lymphoma (Ranks 5 and 7) have plausible mechanistic rationale and multiple Phase 1/2 trials but no Phase 3 confirmation — appropriate to track as research questions, not to advance to development.
- The Hodgkin lymphoma (Rank 3), metastatic neoplasm (Rank 8), and malignant spiradenoma (Rank 9) entries show serious data-quality issues (apparent ontology mislabeling, non-specific KG nodes, or zero supporting evidence) and should **not** be treated as genuine repurposing signals without manual re-validation of the underlying knowledge graph edges.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/international label data — safety warnings, contraindications, DDI — before any S1 safety pre-assessment can begin.
- Resolve DG002 (High): confirm venetoclax's original indication and MOA via DrugBank API to correctly frame this as a market-entry/registration gap rather than a purely novel repurposing hypothesis.
- Re-audit the Hodgkin lymphoma prediction's KG edges — the evidence attached to it does not match the labeled disease and should be corrected or removed upstream.
- If pursuing the AML pathway for the Taiwan market, this is functionally a **new drug registration** question (given 0 existing licenses), not a repurposing question — recommend routing to regulatory/registration workflow rather than repurposing evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


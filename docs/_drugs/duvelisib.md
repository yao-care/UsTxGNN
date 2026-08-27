---
layout: default
title: Duvelisib
parent: 僅模型預測 (L5)
nav_order: 637
evidence_level: L5
indication_count: 10
---

# Duvelisib
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

Using the drug-repurposing report template as instructed. Key data-quality issue up front: `predicted_indications[0]` (rank 1, "Hodgkins lymphoma") is the required focus disease per the template rules, but the evidence pack's own `repurposing_rationale` for that entry states this is very likely a disease-ontology mapping artifact — none of the 11 trials or 16 papers actually enroll classical Hodgkin lymphoma patients; they're all CLL/SLL/NHL. I'm reporting this transparently rather than reframing it as a clean positive signal.

---

# Duvelisib: From CLL/SLL to Hodgkin's Lymphoma

## One-Sentence Summary

Duvelisib (DrugBank DB11952) is a dual PI3K-δ/γ inhibitor originally developed for relapsed/refractory Chronic Lymphocytic Leukemia (CLL) / Small Lymphocytic Lymphoma (SLL), later expanded to follicular lymphoma — per literature in this evidence pack, not a Taiwan license (the drug is currently **not marketed in Taiwan**).
The TxGNN model's top-ranked prediction is **Hodgkin's Lymphoma**, supported on paper by **11 clinical trials** and **16 publications**.
On review, however, every one of those trials and papers actually enrolls non-Hodgkin lymphoma (NHL), CLL/SLL, or mixed lymphoid-malignancy populations — none specifically targets classical Hodgkin lymphoma, so this top prediction is best treated as a probable disease-label mapping error rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia (CLL) / Small Lymphocytic Lymphoma (SLL) (per literature; not a TFDA-licensed indication — drug not marketed in Taiwan) |
| Predicted New Indication | Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Taiwan Market Status (TFDA) | 未上市 (Not marketed) |
| Number of NDAs/Licenses | 0 |
| Recommended Decision | Hold |

**Note on the evidence set:** a lower-ranked candidate in this same pack — "B-cell neoplasm" (rank 9, score 99.80%) — carries much stronger evidence (Evidence Level L1, includes the pivotal Phase 3 DUO trial NCT02004522, decision stage S3, recommendation "Proceed with Guardrails"). Per its own rationale, that entry essentially restates duvelisib's already-known CLL/SLL/follicular lymphoma activity rather than a new indication. It is not a repurposing candidate, but it is worth flagging separately from the Hodgkin lymphoma prediction reviewed below.

## Why is This Prediction Reasonable?

Duvelisib is a first-in-class oral dual inhibitor of PI3K-δ and PI3K-γ, blocking B-cell receptor (BCR) downstream signaling — a pathway central to indolent B-cell malignancies such as CLL/SLL and follicular lymphoma (per literature PMID 30430368, PMID 28388280). Detailed structured MOA data was not returned from DrugBank in this evidence pack (Data Gap DG002); the mechanism above is reconstructed from the literature evidence attached to these predictions.

Mechanistically, this pathway dependency does not extend cleanly to **classical Hodgkin lymphoma**: the malignant Reed-Sternberg cells in classical Hodgkin lymphoma typically lose BCR expression and are instead driven by constitutive JAK/STAT and NF-κB signaling, which is only indirectly related to PI3K-δ/γ inhibition. Consistent with this, a line-by-line review of the 11 trials and 16 papers attached to this prediction found that every one addresses indolent/aggressive non-Hodgkin lymphoma, CLL/SLL, mantle cell lymphoma, or T-cell lymphoma — not classical Hodgkin lymphoma. The most plausible explanation is that TxGNN's underlying disease ontology grouped a broadly-named "lymphoma" node in a way that pulled in this high similarity score without genuine target-specific evidence.

Because of this, the mechanistic rationale for duvelisib in classical Hodgkin lymphoma specifically should be treated as **unconfirmed** pending disease-ontology verification, not as a supported hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04038359](https://clinicaltrials.gov/study/NCT04038359) | Phase 2 | Completed | 103 | Compared two duvelisib dosing schedules (with dose holidays) in indolent non-Hodgkin lymphoma (iNHL) — not classical Hodgkin lymphoma |
| [NCT05065866](https://clinicaltrials.gov/study/NCT05065866) | Phase 1 | Completed | 14 | Duvelisib + BMS-986345 in broad lymphoid malignancies; no Hodgkin-specific cohort |
| [NCT02640833](https://clinicaltrials.gov/study/NCT02640833) | Phase 1b/2 | Withdrawn | 0 | Planned duvelisib + venetoclax in R/R CLL/SLL/NHL; withdrawn, no data generated |
| [NCT04836832](https://clinicaltrials.gov/study/NCT04836832) | Phase 1 | Withdrawn | 0 | Planned duvelisib + acalabrutinib in R/R indolent NHL (DUAL trial); withdrawn |
| [NCT04379167](https://clinicaltrials.gov/study/NCT04379167) | Phase 2 | Unknown | 140 | Single-arm study of a different PI3K inhibitor (YY-20394) in R/R follicular NHL; status unknown, not duvelisib-specific |
| [NCT01871675](https://clinicaltrials.gov/study/NCT01871675) | Phase 1b | Completed | 48 | IPI-145 (duvelisib) + rituximab/bendamustine in lymphoma/CLL — NHL population |
| [NCT02576275](https://clinicaltrials.gov/study/NCT02576275) | Phase 3 | Withdrawn | 0 | Planned duvelisib + R-bendamustine vs placebo in previously-treated indolent NHL; withdrawn before enrollment |
| [NCT05923502](https://clinicaltrials.gov/study/NCT05923502) | N/A (real-world) | Not yet recruiting | 200 | Planned real-world observational study of duvelisib in NHL; not yet started |
| [NCT05044039](https://clinicaltrials.gov/study/NCT05044039) | Phase 1 | Active, not recruiting | 42 | Duvelisib post-CAR-T to improve CAR-T persistence; mechanism study, not Hodgkin-specific |
| [NCT04803201](https://clinicaltrials.gov/study/NCT04803201) | Phase 2 | Suspended | 170 | Duvelisib-CHOP vs alternative regimens in untreated CD30-negative peripheral T-cell lymphoma; suspended |

None of the above trials enroll a classical Hodgkin lymphoma population; all relevance gradings in the source data are "C" (low relevance to the stated indication).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36685572](https://pubmed.ncbi.nlm.nih.gov/36685572/) | 2022 | Systematic review/meta-analysis | Frontiers in Immunology | Meta-analysis of duvelisib safety/efficacy across relapsed/refractory lymphoid neoplasms (CLL/NHL); does not isolate classical Hodgkin lymphoma |
| [31490009](https://pubmed.ncbi.nlm.nih.gov/31490009/) | 2019 | Phase 1b trial | American Journal of Hematology | Duvelisib + rituximab ± bendamustine in NHL/CLL; disease-specific expansion cohorts were NHL/CLL, not Hodgkin lymphoma |
| [29191916](https://pubmed.ncbi.nlm.nih.gov/29191916/) | 2018 | Phase 1 trial | Blood | First-in-human dose-escalation in 210 patients with advanced hematologic malignancies; established MTD 75 mg BID |
| [28017967](https://pubmed.ncbi.nlm.nih.gov/28017967/) | 2017 | Mechanistic/translational | Leukemia | Duvelisib alters apoptotic regulators, sensitizing CLL cells to venetoclax — CLL-focused |
| [36882482](https://pubmed.ncbi.nlm.nih.gov/36882482/) | 2023 | Preclinical | Scientific Reports | PI3Kγ/δ role in mantle cell lymphoma (a non-Hodgkin B-cell lymphoma) proliferation/migration |
| [30799261](https://pubmed.ncbi.nlm.nih.gov/30799261/) | 2019 | Review | The Lancet Oncology | Overview of duvelisib in indolent non-Hodgkin lymphoma |
| [31580408](https://pubmed.ncbi.nlm.nih.gov/31580408/) | 2019 | Review | Am J Health-Syst Pharm | Summary of targeted therapies approved for B- and T-cell lymphomas |
| [33616890](https://pubmed.ncbi.nlm.nih.gov/33616890/) | 2021 | Review | Drugs | Novel therapy approaches in follicular lymphoma (an NHL subtype) |
| [32356174](https://pubmed.ncbi.nlm.nih.gov/32356174/) | 2020 | Review | Curr Treat Options Oncol | PI3K inhibitors as targeted therapy across lymphoma broadly |
| [32658557](https://pubmed.ncbi.nlm.nih.gov/32658557/) | 2020 | Review | Future Oncology | Copanlisib (a related PI3K inhibitor) in non-Hodgkin lymphoma |

As with the trials, none of these publications address classical Hodgkin lymphoma specifically.

## Taiwan Market Information (TFDA)

Duvelisib currently has **0 TFDA licenses** and is **not marketed in Taiwan** (market_status: 未上市). No NDA/license records are available to summarize.

## Cytotoxicity

Duvelisib is an antineoplastic agent (PI3K-δ/γ inhibitor used to treat hematologic malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (dual PI3K-δ/γ inhibitor) — not a conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Not available in this evidence pack — pending TFDA package insert (Data Gap DG001, Blocking severity) |
| Emetogenicity Classification | Not available in this evidence pack — pending TFDA package insert (Data Gap DG001) |
| Monitoring Items | Not available in this evidence pack — pending TFDA package insert (Data Gap DG001) |
| Handling Protection | Not available in this evidence pack — pending TFDA package insert (Data Gap DG001) |

## Safety Considerations

Please refer to the package insert for safety information. TFDA warnings/contraindications (Data Gap DG001) and DDI data (query returned "not found") are not yet available in this evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Hodgkin's lymphoma, 99.94% score) is not supported by disease-specific evidence — all 11 trials and 16 papers attached to it involve non-Hodgkin lymphoma, CLL/SLL, or mixed lymphoid malignancies, indicating a likely disease-ontology mapping error rather than a genuine signal. Combined with a Blocking-severity data gap on TFDA warnings/contraindications and the drug's unmarketed status in Taiwan, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- TFDA package insert retrieval and parsing (resolves DG001, currently blocking safety review)
- DrugBank MOA confirmation (resolves DG002)
- Disease-ontology validation to determine whether the TxGNN "Hodgkins lymphoma" node was correctly mapped, or should be re-run against a corrected disease vocabulary
- If repurposing is still of interest, direct clinical or preclinical evidence in a genuine classical Hodgkin lymphoma population (JAK/STAT- or NF-κB-relevant models), since none currently exists in this pack
- Separately, Taiwan market-entry/licensing assessment, since duvelisib has 0 TFDA licenses today
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


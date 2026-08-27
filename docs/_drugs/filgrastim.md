---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 707
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim (recombinant human G-CSF) is a well-established supportive-care agent used to stimulate neutrophil production and mobilize hematopoietic stem cells; a specific approved-indication text was not available in this evidence pack. The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but the **14 clinical trials** and **1 publication** returned by the search are largely indirect (general hematopoietic stem cell transplant / mobilization studies), with none directly testing filgrastim as treatment for this platelet-specific condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from license data (drug not marketed in this jurisdiction, 0 licenses on file); publicly known use is chemotherapy-induced neutropenia / stem cell mobilization |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.9976% (rank 171) |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa`: Data Gap). Based on known public information, filgrastim is a recombinant human granulocyte colony-stimulating factor (G-CSF) that stimulates proliferation and differentiation of neutrophil precursors and is also used off-label to mobilize hematopoietic stem/progenitor cells into peripheral blood ahead of collection for transplant.

"Primary release disorder of platelets" refers to a platelet secretion/granule-release defect rather than a neutrophil disorder. The mechanistic overlap between G-CSF's myeloid-lineage action and platelet granule-release physiology is not well established, and the evidence pack does not provide a direct mechanistic rationale linking the two.

The clinical trials returned for this indication are overwhelmingly hematopoietic stem cell transplantation (HSCT) protocols for hematologic malignancies, aplastic anemia, or autoimmune disease, in which G-CSF (filgrastim) is typically used as a supportive stem-cell mobilization agent rather than as a treatment directed at a platelet release disorder. The single literature result concerns G-CSF's effect on mobilizing lymphocyte subsets in healthy donors — again tangential to the predicted disease. Taken together, this is best characterized as circumstantial/indirect evidence rather than direct support for the prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor HSCT for hematologic malignancies; G-CSF context indirect, not platelet-disorder specific |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs. unselected autologous HSCT in MCL/DLBCL; survival endpoint, not platelet release |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Autologous HSCT vs. best available therapy for treatment-resistant MS |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Post-transplant cyclophosphamide GVHD prophylaxis in mismatched unrelated donor PBSCT |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT using busulfan/fludarabine/TBI |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Cryopreserved HLA-mismatched unrelated donor bone marrow + PTCy |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir/valganciclovir for CMV reactivation prevention in lung injury/respiratory failure; not a G-CSF efficacy study |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic blood stem cell transplant in pediatric sarcomas |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Dapansutrile for moderate COVID-19 with cytokine release syndrome; no apparent filgrastim link |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Dose-finding of post-transplant cyclophosphamide + sirolimus + MMF for GVHD prophylaxis |

*Note: none of the above trials directly evaluate filgrastim as a treatment for a platelet release disorder; all are general HSCT/supportive-care protocols surfaced by the search.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Mechanistic/cohort study | Frontiers in Immunology | G-CSF mobilization in healthy donors preferentially mobilizes specific lymphocyte subsets; does not directly address platelet release disorders |

---

## US Market Information

No license records are available — filgrastim is currently not marketed in this jurisdiction per the evidence pack (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not available in this evidence pack; note that TFDA label warnings/contraindications are flagged as a **Blocking** data gap for safety pre-screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication lacks direct clinical or mechanistic support — all 14 retrieved trials are general HSCT/mobilization protocols and the single literature result addresses lymphocyte mobilization, not platelet release physiology. Combined with a missing MOA record and a blocking safety data gap (no TFDA label data), the evidence does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (Blocking gap DG001)
- Confirmed mechanism of action data (DG002) to properly assess mechanistic plausibility for a platelet-release disorder
- Direct preclinical or clinical evidence connecting G-CSF/filgrastim pharmacology to platelet granule-release defects
- Re-query of clinical trial/literature databases using disease-specific synonyms (e.g., platelet secretion defect, storage pool disease) to rule out a search-term mismatch before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


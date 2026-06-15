---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive NSCLC to Fibromatosis, Gingival

## One-Sentence Summary

Brigatinib (Alunbrig) is a next-generation anaplastic lymphoma kinase (ALK) inhibitor extensively validated for ALK-positive non-small-cell lung cancer (NSCLC), as confirmed by the large volume of Phase 3 clinical trial literature retrieved in this evidence pack.
The TxGNN model predicts it may have potential in **Fibromatosis, Gingival**, with a prediction score of 99.89%;
however, **no clinical trials and no supporting publications** have been identified for this specific indication, and the mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive NSCLC (inferred from retrieved literature; no US FDA license records found in database) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | Not marketed (no license records retrieved) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on the extensive clinical literature retrieved during evidence collection, Brigatinib is a selective inhibitor of ALK (anaplastic lymphoma kinase) and ROS1 tyrosine kinases, with additional inhibitory activity against mutant EGFR, FAK, IGF-1R, and a documented but weak inhibitory effect on PDGFRβ. Its clinical efficacy in ALK-positive NSCLC has been rigorously established through multiple Phase 3 randomized controlled trials — most notably the ALTA-1L trial comparing Brigatinib to crizotinib in first-line ALK-positive NSCLC, as well as the ALTA-3 trial in the post-crizotinib setting.

Gingival fibromatosis is a benign fibrous overgrowth of the gingival tissue, most commonly driven by SOS1 gene mutations or dysregulation of the PDGFR/FGFR signaling axis. This disease does not involve ALK rearrangements or ROS1 fusions — the primary oncogenic targets of Brigatinib — creating a fundamental mechanistic disconnect. The only theoretical bridge between Brigatinib and this condition is its incidental, mild PDGFRβ inhibitory activity, which has not been explored in any preclinical gingival fibromatosis model or clinical observation.

This prediction is most likely a structural artifact of the TxGNN knowledge graph, where node proximity between gingival tissue-associated gene signatures and kinase pathway hubs may generate spurious cross-disease associations. Without any supporting experimental or clinical evidence, and with no established mechanistic pathway linking Brigatinib to gingival fibromatosis biology, this prediction currently has no actionable basis for development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No approved license records were retrieved from the database. Please note that Brigatinib (Alunbrig) is known to be FDA-approved in the United States for ALK-positive NSCLC on the basis of the clinical trial evidence retrieved in this pack; the absence of records may reflect a data collection limitation in the current pipeline.

---

## Cytotoxicity

Brigatinib is an antineoplastic agent (ALK/ROS1/EGFR tyrosine kinase inhibitor) approved for malignant NSCLC treatment.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — next-generation ALK/ROS1/EGFR tyrosine kinase inhibitor |
| Myelosuppression Risk | Low to moderate (less pronounced than conventional cytotoxics; anemia, neutropenia, and thrombocytopenia have been reported) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests, renal function, creatine phosphokinase (CPK), blood pressure, heart rate, blood glucose, pulmonary function (high risk of early-onset ILD/pneumonitis within the first 7 days of treatment) |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key safety data (TFDA package insert warnings and contraindications) and drug interaction data were not retrievable during evidence collection and represent a **blocking data gap** (DG001). Brigatinib is associated with known class-specific risks including early-onset interstitial lung disease/pneumonitis, hypertension, bradycardia, CPK elevation, and visual disturbances. These must be reviewed from the full prescribing information before any clinical application is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.89%), the mechanistic link between Brigatinib's established targets (ALK/ROS1/EGFR/FAK) and the SOS1/PDGFR/FGFR-driven pathobiology of gingival fibromatosis is essentially absent. The prediction is L5 — model prediction only, with zero supporting preclinical or clinical studies — and the repurposing rationale is most likely a knowledge graph node-proximity artifact rather than a biologically grounded signal.

**To proceed, the following is needed:**
- Establishment of a plausible mechanistic hypothesis (e.g., whether PDGFRβ inhibition can functionally suppress fibroblast proliferation in gingival fibromatosis tissue)
- Preclinical evaluation in gingival fibromatosis cell lines or patient-derived fibroblast models
- Retrieval of Brigatinib's full kinase inhibition profile from DrugBank to confirm secondary target relevance (DG002)
- Download and parsing of the TFDA/FDA package insert to resolve the blocking safety data gap (DG001) before any further evaluation stage

---

> **Reviewer's Note — Secondary Predictions with Higher Clinical Signal:**
> While the top TxGNN-ranked prediction (fibromatosis, gingival) lacks mechanistic support, two lower-ranked predictions carry substantially more compelling evidence and may merit prioritized evaluation:
>
> - **Rank 10 — NF2-Related Schwannomatosis (remapped from "Leukomelanoderma syndrome"):** Evidence Level L3. A 2024 *NEJM* pilot case series (PMID 38904277) and a 2021 preclinical + clinical observation study (PMID 34264955) demonstrate tumor shrinkage via FAK/multi-kinase inhibition independent of ALK. One fatal TLS case (PMID 34987411) requires safety monitoring protocol design. Recommended stage: S2 — Research Question.
> - **Rank 7 — Lung Germ Cell Tumor / ALK-Driven Neuroendocrine Tumors:** Evidence Level L4. Preclinical data supports Brigatinib activity in ALK-mutant neuroblastoma; a 2024 LCNEC case report with EML4-ALK fusion (PMID 39395329) and a 2021 pheochromocytoma case with ALK fusion (PMID 34371380) provide clinical signals. Recommended stage: S1 — safety pre-screening before concept validation study design.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


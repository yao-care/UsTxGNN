---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 747
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: From EGFR-Mutant Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

> Gefitinib is an EGFR (HER1) tyrosine kinase inhibitor known for treating EGFR-mutation-positive non-small cell lung cancer (NSCLC).
> The TxGNN model's top-ranked prediction for this drug is **Fibromatosis, Gingival**, with a prediction score of **99.89%**,
> but this candidate currently has **0 clinical trials** and **0 publications** supporting it — the evidence pack itself flags no known mechanistic connection between EGFR inhibition and this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | EGFR-mutant Non-Small Cell Lung Cancer (NSCLC) — inferred from mechanistic rationale text embedded in the evidence pack; formal Taiwan license record unavailable (data gap) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Market Status (Taiwan) | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for gefitinib is flagged as a data gap in this evidence pack (DG002). However, other candidate entries in the same pack consistently describe gefitinib as an EGFR (HER1) tyrosine kinase inhibitor, approved for EGFR-mutation-positive NSCLC — this is well-established background knowledge for this drug and is corroborated repeatedly across the pack's own rationale text.

For the top-ranked candidate, **Fibromatosis, Gingival**, the evidence pack's own repurposing rationale states this condition is primarily associated with connective-tissue overgrowth and hereditary fibrotic mechanisms, with no known connection to EGFR inhibition. No clinical trials, ICTRP trials, or PubMed literature were found linking gefitinib to this disease. This candidate appears to reflect the TxGNN model's raw prediction score rather than any mechanistic or clinical signal — consistent with its assigned Evidence Level L5 and Hold recommendation.

By contrast, two lower-ranked candidates in this same pack — **lung hilum carcinoma** (rank 5) and **pulmonary sulcus neoplasm** (rank 8) — are anatomical subtypes of NSCLC and align directly with gefitinib's already-approved mechanism; both reached decision stage S1 ("Research Question"). These may warrant separate evaluation (see Conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Cytotoxicity

Gefitinib is an EGFR-targeted small-molecule tyrosine kinase inhibitor used in non-small cell lung cancer, meeting the antineoplastic classification criteria.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR/HER1 tyrosine kinase inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — TKIs of this class are not classically myelosuppressive; formal hematologic toxicity data is a data gap (DrugBank query returned no MOA/toxicity detail) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (hepatotoxicity); chest imaging/pulmonary function for interstitial lung disease (per literature PMID [22076388](https://pubmed.ncbi.nlm.nih.gov/22076388/)); ECG/QTc (per PMID [34474028](https://pubmed.ncbi.nlm.nih.gov/34474028/) and PMID [37258113](https://pubmed.ncbi.nlm.nih.gov/37258113/)); skin examination for acneiform eruption (per PMID [18931563](https://pubmed.ncbi.nlm.nih.gov/18931563/)); CBC |
| Handling Protection | Oral formulation, targeted small molecule — does not require IV cytotoxic handling precautions, but institutional oncology-drug handling policy should still be followed; please refer to the package insert for confirmation |

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings, contraindications, and DDI data are currently unavailable — flagged as a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Fibromatosis, Gingival) has a high TxGNN score but no clinical trials, no literature, and no plausible mechanistic link per the evidence pack itself — this is a model-score-only signal (L5) with no basis for further action.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action record from DrugBank (DG002)
- Consider separately evaluating **lung hilum carcinoma** and **pulmonary sulcus neoplasm** from this same evidence pack — both are NSCLC anatomical subtypes with mechanistic continuity to gefitinib's approved use and reached decision stage S1 ("Research Question"), unlike the Fibromatosis, Gingival candidate reported here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


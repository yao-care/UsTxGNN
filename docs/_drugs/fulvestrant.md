---
layout: default
title: Fulvestrant
parent: 僅模型預測 (L5)
nav_order: 742
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

# Fulvestrant: From ER-Positive Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

Fulvestrant is a selective estrogen receptor degrader (SERD), established in clinical use for ER-positive/HER2-negative breast cancer (referenced repeatedly in the prediction rationale, though no formal indication text is on file). The TxGNN model predicts it may be effective for **HIV infectious disease**, with a very high prediction score (**99.91%**) but **zero clinical trials** and only **1 tangentially related publication** — and the model's own rationale states there is no known antiviral mechanism for fulvestrant.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ER-positive, HER2-negative breast cancer (inferred from mechanism context embedded in the prediction rationale; no formal regulatory indication text is available — the drug has no US licenses on file) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for fulvestrant is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded in the prediction rationale, fulvestrant is a selective estrogen receptor degrader/antagonist (SERD), with established efficacy in ER-positive breast cancer via estrogen receptor downregulation.

For the top-ranked prediction, HIV infectious disease, the model's own rationale explicitly states there is **no known mechanistic link**: fulvestrant has no antiviral pharmacological basis and no direct connection to HIV or HTLV-1 infection biology. The sole supporting publication (PMID 40343334) is a multi-omics analysis of HTLV-1-associated myelopathy that does not mention fulvestrant directly, and its relevance has not yet been formally assessed ("pending").

Given the very high TxGNN score paired with the complete absence of mechanistic or clinical support, this prediction most likely reflects a knowledge-graph association (e.g., shared pathway nodes or ontology proximity) rather than a pharmacologically plausible repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Multi-omics/Genomics Analysis (preprint, Research Square) | Research square | Multi-cohort cross-omics study of HTLV-1-associated myelopathy (HAM), a neglected retroviral neuroinflammatory disease; identifies disease mechanisms and therapeutic targets, but does not specifically evaluate fulvestrant. Relevance to this drug not yet confirmed. |

## US Market Information

Fulvestrant is not currently marketed in the US under this evidence pack's data — 0 licenses/NDAs are on file.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN confidence score but is classified as Evidence Level L5 (model prediction only) — there are no clinical trials, no mechanistically relevant literature, and the rationale itself concludes there is no plausible pharmacological basis linking fulvestrant to HIV infection. This does not meet the threshold to advance past initial screening.

**To proceed, the following is needed:**
- TFDA/FDA labeling data — warnings, contraindications (currently a Blocking data gap, DG001; required before any S1 safety review)
- Confirmed mechanism-of-action data for fulvestrant (High-severity data gap, DG002)
- Literature or preclinical data specifically evaluating estrogen-receptor pathway involvement in HIV/retroviral pathogenesis
- Drug-drug interaction data (current DDI query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


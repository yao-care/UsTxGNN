---
layout: default
title: Lorlatinib
parent: Model Prediction Only (L5)
nav_order: 871
evidence_level: L5
indication_count: 10
---

# Lorlatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Lorlatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Lorlatinib is an oral ALK/ROS1 tyrosine kinase inhibitor, marketed in the US as Lorbrena for ALK-positive non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis** (score 99.81%), but there are **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive NSCLC (taken from the drug's literature, since the US license records contain no indication text) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 license records (all under a single NDA, NDA210868) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on known information, lorlatinib is a brain-penetrant, third-generation ALK/ROS1 kinase inhibitor. Its efficacy in ALK-positive NSCLC is well established, including Phase 3 CROWN trial data.

We could not identify a mechanistic link to gingival fibromatosis. Gingival fibromatosis is a fibrous overgrowth of the gums, either hereditary or drug-induced. It is not a known ALK- or ROS1-driven condition. The high TxGNN score reflects graph-based association only, and no biological rationale, similarity to the original indication, or route compatibility has been established.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210868 | Lorbrena (3 listings: Pfizer Laboratories Div Pfizer Inc ×2, U.S. Pharmaceuticals) | Film-coated tablet (oral) | — |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanism. It is graded L5 (model prediction only). Among the other TxGNN candidates for lorlatinib, only lung hilum carcinoma has a mechanistic rationale, a single neoadjuvant case report in ALK-positive lung cancer, and it also remains at the research-question level.

**To proceed, the following is needed:**
- A mechanistic hypothesis linking ALK/ROS1 inhibition to gingival fibromatosis, plus a targeted literature search and preclinical evidence
- Mechanism of action (MOA) data from DrugBank
- FDA package insert warnings and contraindications
- The approved indication text from the US license records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


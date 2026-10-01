---
layout: default
title: Dinutuximab
parent: Model Prediction Only (L5)
nav_order: 611
evidence_level: L5
indication_count: 4
---

# Dinutuximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Dinutuximab: From High-Risk Neuroblastoma to Vertebral Anomalies with Variable Endocrine and T-Cell Dysfunction

## One-Sentence Summary

Dinutuximab is an anti-GD2 monoclonal antibody, originally used to treat high-risk neuroblastoma.
The TxGNN model predicts it may be effective for **vertebral anomalies and variable endocrine and T-cell dysfunction**, a rare developmental syndrome.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | High-risk neuroblastoma |
| Predicted New Indication | Vertebral anomalies and variable endocrine and T-cell dysfunction |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125516) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the database. Dinutuximab is a chimeric anti-GD2 antibody. It kills GD2-expressing tumor cells through antibody-dependent cellular cytotoxicity (ADCC) and complement-dependent cytotoxicity (CDC). Its efficacy in neuroblastoma is established.

The link to the predicted indication is weak. The predicted condition is a rare developmental syndrome, and no GD2-driven pathology is known for it. The 99.42% score (model rank 13,469) is a statistical association in the knowledge graph, not a demonstrated biological rationale. Without a target-related mechanism, the prediction should be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| BLA125516 | Unituxin (United Therapeutics Corporation) | Injection |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (monoclonal antibody, anti-GD2); not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature, and no plausible mechanistic link. It relies only on the model score, which is not enough to justify further investment.

**To proceed, the following is needed:**
- A mechanistic hypothesis showing GD2 involvement in this syndrome, such as GD2 expression in the affected tissues
- Preclinical or case-level evidence supporting any activity in this condition
- Package insert safety data (warnings and contraindications), which are needed for any safety screening
- Mechanism of action data from DrugBank

**Related note:** Within the same TxGNN output, **ganglioneuroblastoma** (rank 2, score 99.39%) has much stronger support. It has 7 registered trials, including a recruiting Phase 3 study (NCT06172296, n=478), a completed randomized Phase 2 trial (NCT01767194, n=73), and one published RCT (PMID 28549783). It is an Evidence Level L2 candidate with a "Proceed with Guardrails" recommendation. The trials and publication refer to neuroblastoma, not ganglioneuroblastoma specifically, so GD2 expression in the more differentiated histology should be verified. It is a better candidate for priority evaluation than the rank 1 prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Fostamatinib
parent: Model Prediction Only (L5)
nav_order: 740
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Fostamatinib: predicted new indication Autosomal thrombocytopenia with normal platelets (evidence level L5). Approved use: Thrombocytopenia due to immune destruction"
monitor_inn: "FOSTAMATINIB"
predicted_indications: ["non-syndromic esophageal malformation"]
---

# Fostamatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Fostamatinib: From Immune Thrombocytopenia to Autosomal Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Fostamatinib was originally used to treat thrombocytopenia caused by immune destruction of platelets.
The TxGNN model predicts it may be effective for **autosomal thrombocytopenia with normal platelets**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thrombocytopenia due to immune destruction |
| Predicted New Indication | Autosomal thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fostamatinib is a prodrug of R406, a spleen tyrosine kinase (SYK) inhibitor. Its efficacy in immune thrombocytopenia comes from blocking Fc-receptor-mediated platelet destruction by macrophages.

The predicted indication is a heritable form of thrombocytopenia. Such conditions are presumably driven by defects in platelet production or function rather than by immune-mediated clearance. SYK inhibition therefore has no clear link to the likely underlying disease process. The two conditions share only the label "low platelet count".

The high TxGNN score (99.45%) probably reflects network proximity to the thrombocytopenia concept in the knowledge graph rather than a validated mechanistic rationale. It should be treated as a hypothesis-generating signal only.

A second prediction, **non-syndromic esophageal malformation** (score 99.05%), was also generated. No credible mechanistic link was identified. Esophageal malformations are structural defects arising during embryonic development, and an immune-cell kinase inhibitor has no apparent role in correcting them. The high score is likely a knowledge-graph artifact. No trials or literature support it, and use in a neonatal or pediatric population would raise safety questions that current data do not address.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209299 | TAVALISSE (Rigel Pharmaceuticals, Inc.) | Tablet (oral) | Not listed in the data compiled; status: cancelled |

## Safety Considerations

- **Drug Interactions**: The interaction query completed with 100 recorded interactions. The first 20 are listed below. Of these, 1 is rated Major and the rest Moderate.
  - **Major**: Clarithromycin
  - **Moderate (selected)**:
    - Acid suppressants: rabeprazole, omeprazole, dexlansoprazole, cimetidine
    - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
    - Others: alosetron, alvimopan, aprepitant, dolasetron, dronabinol, eliglustat, empagliflozin, loperamide, pioglitazone, morphine

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions are supported only by the model score (evidence level L5), with no clinical trials or literature. The SYK-inhibition mechanism has no clear link to either a heritable platelet disorder or a congenital esophageal malformation. The US market status is also "Cancelled only".

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data, to support or refute any mechanistic link
- Evidence that the predicted thrombocytopenia involves a SYK-dependent pathway, for example preclinical or mechanistic studies
- A literature and trial search specific to the predicted indications
- Review of the interaction profile, particularly the Major interaction with clarithromycin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


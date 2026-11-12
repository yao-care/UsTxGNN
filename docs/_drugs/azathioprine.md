---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 434
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-12
description: "Azathioprine: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "AZATHIOPRINE"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "WHIM syndrome", "granulomatous disease, chronic, autosomal recessive, 5", "osteoarthritis", "granulomatous disease with defect in neutrophil chemotaxis", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Azathioprine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Azathioprine: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome
{: .text-alpha }

## One-Sentence Summary

Azathioprine is an oral immunosuppressant that was originally used for rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental disorder.
This prediction currently has **0 clinical trials** and **0 publications** supporting it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 7 of 9) |
| Number of FDA Applications | 9 (active: 7) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, azathioprine is a purine antimetabolite immunosuppressant, and its efficacy in immune-mediated disease is established.

For this particular prediction, however, no mechanistic link is evident. The predicted condition is a rare developmental and skeletal disorder with no inflammatory or immune-mediated basis that azathioprine's immunosuppression could target.

The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trials or literature support it. It should be treated as a hypothesis-generating signal, not as evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

<!-- review:begin us-lic-20261106-azathioprine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "All four authorizations are single-ingredient oral tablets, and all are cancelled." Removed: it described the products as single-ingredient or combination products in a way that did not match the FDA ingredient data (Drugs@FDA and the NDC Directory as of 2026-11-06). Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-azathioprine-1 -->

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA077621 | Azathioprine (NuCare Pharmaceuticals) | Tablet | Not specified (valid) |
| ANDA074069 | Azathioprine (Amneal Pharmaceuticals NY) | Tablet | Not specified (valid) |
| ANDA208687 | Azathioprine (Ascend Laboratories) | Tablet | Not specified (valid) |
| ANDA075252 | Azasan (Salix Pharmaceuticals) | Tablet | Not specified (valid) |

---

## Safety Considerations

- **Disease associations flagged as contraindications** (from a drug-disease knowledge graph, not from label text): pancreatitis, thrombocytopenia, anemia (including macrocytic anemia), impaired renal function, infectious disease (including fungal infections and dermatophytosis), lymphoma (including primary CNS lymphoma, lymphosarcoma, and hepatosplenic T-cell lymphoma), and hepatic vein thrombosis (Budd-Chiari syndrome).
- **Drug interactions**: 100 interactions were identified. The moderate-level ones are the aminosalicylates mesalazine, balsalazide, olsalazine, and sulfasalazine. Zinc salts (acetate, gluconate, sulfate) are minor. Many other entries, such as aspirin, metformin, omeprazole, and doxycycline, have an unclassified severity level.
- Azathioprine is myelosuppressive and immunosuppressive, which is a concern in disorders without an immune-driven mechanism.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature, and no plausible mechanism. The toxicity profile of immunosuppression is hard to justify in a developmental disorder.

**To proceed, the following is needed:**
- Mechanistic evidence linking purine antimetabolite immunosuppression to the pathology of this syndrome
- Preclinical or case-level data showing any benefit
- Detailed mechanism of action data
- Package insert warnings and contraindications for a formal safety review
- A decision on whether the IBD and UC predictions should be evaluated as separate candidates

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "All four authorizations are single-ingredient oral tablets, and all are cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


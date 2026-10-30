---
layout: default
title: Plerixafor
parent: Model Prediction Only (L5)
nav_order: 1056
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "PLERIXAFOR"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis", "vulvar melanoma (disease)", "myeloid leukemia"]
description: "Plerixafor: predicted new indication CMM7 (evidence level L5). Approved use: Not recorded in the local data"
---

# Plerixafor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Plerixafor: CMM7
{: .text-alpha }

## One-Sentence Summary

> The TxGNN model predicts it may be effective for **indolent plasma cell myeloma** (smoldering myeloma), with a very high score.
> However, there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | CMM7 |
| TxGNN Prediction Score | 0.9934 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 8 of 9) |
| Number of FDA Applications | 9 (valid: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from the drug database is not available. Pharmacology data compiled for this report show that plerixafor targets **CXCR4** and also interacts with **ACKR3**. The CXCR4/CXCL12 axis anchors plasma cell myeloma cells in the bone marrow niche, so blocking it could in theory release them from that protective environment.

The high score is plausibly driven by the drug's closeness to an established myeloma-related use: stem cell mobilisation in multiple myeloma before autologous transplantation. That use is supportive care for transplant, not treatment of the myeloma itself.

There is no rationale for treating indolent (smoldering) disease with a mobilising agent. No trials or publications were found for this subtype, so this is a model prediction only and should be read cautiously.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for indolent plasma cell myeloma.

---

## Literature Evidence

Currently no related literature available for indolent plasma cell myeloma.

---

## US Market Information

The data did not include approved-indication text. The five shown are the original brand NDA and four generic ANDAs.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022311 | Mozobil (Sanofi-Aventis U.S. LLC) | Injection, solution | Not provided (valid) |
| ANDA215334 | Plerixafor (Amneal) | Injection, solution | Not provided (valid) |
| ANDA217560 | Plerixafor (Camber) | Injection, solution | Not provided (valid) |
| ANDA205182 | Plerixafor (Dr. Reddy's) | Solution | Not provided (valid) |
| ANDA208980 | Plerixafor (Zydus) | Injection | Not provided (valid) |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: thrombocytopenia, impaired renal function, and leukemia.
- **Target interactions**: The interaction data list only pharmacological targets (CXCR4 and ACKR3), not drug–drug interactions.

Please refer to the package insert for key warnings and formal contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials, no literature, and no clear rationale for using a mobilising agent in indolent myeloma. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Preclinical or clinical evidence that CXCR4 blockade has any role in indolent or smoldering myeloma
- Mechanism-of-action data and label-based warnings and contraindications
- Confirmation of the current US regulatory status of plerixafor products
- Optional: a lower-ranked prediction, **myeloid leukemia** (score 0.9902), has 25 registered trials and 20 publications. Many of these are Phase 1 and Phase 1/2 studies of plerixafor as a chemosensitiser with chemotherapy. It is rated L2 and would be a more evidence-supported direction to evaluate in a separate report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


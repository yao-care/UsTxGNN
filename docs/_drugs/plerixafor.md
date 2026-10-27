---
layout: default
title: Plerixafor
parent: Model Prediction Only (L5)
nav_order: 1056
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Plerixafor: predicted new indication Indolent plasma cell myeloma (evidence level L5). Approved use: Plasma cell myeloma"
monitor_inn: "PLERIXAFOR"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis", "vulvar melanoma (disease)", "myeloid leukemia"]
---

# Plerixafor
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

## Plerixafor: From Plasma Cell Myeloma to Indolent Plasma Cell Myeloma
{: .text-alpha }

## One-Sentence Summary

> Plerixafor (AMD3100, Mozobil) is a CXCR4 antagonist used to mobilise hematopoietic stem cells, and the knowledge graph links it to plasma cell myeloma.
> The TxGNN model predicts it may be effective for **indolent plasma cell myeloma** (smoldering myeloma), with a very high score.
> However, there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasma cell myeloma (from the knowledge graph; no approved-indication text was available in the US license records) |
| Predicted New Indication | Indolent plasma cell myeloma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations in the data) |
| Number of NDAs | 9 authorizations (1 NDA and 8 ANDAs), all cancelled |
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

All nine US authorizations are cancelled. The data did not include approved-indication text. The five shown are the original brand NDA and four generic ANDAs.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022311 | Mozobil (Sanofi-Aventis U.S. LLC) | Injection, solution | Not provided (cancelled) |
| ANDA215334 | Plerixafor (Amneal) | Injection, solution | Not provided (cancelled) |
| ANDA217560 | Plerixafor (Camber) | Injection, solution | Not provided (cancelled) |
| ANDA205182 | Plerixafor (Dr. Reddy's) | Solution | Not provided (cancelled) |
| ANDA208980 | Plerixafor (Zydus) | Injection | Not provided (cancelled) |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: thrombocytopenia, impaired renal function, and leukemia.
- **Target interactions**: The interaction data list only pharmacological targets (CXCR4 and ACKR3), not drug–drug interactions.

Please refer to the package insert for key warnings and formal contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials, no literature, and no clear rationale for using a mobilising agent in indolent myeloma. The evidence level is L5 (model prediction only). All US authorizations are also cancelled.

**To proceed, the following is needed:**
- Preclinical or clinical evidence that CXCR4 blockade has any role in indolent or smoldering myeloma
- Mechanism-of-action data and label-based warnings and contraindications
- Confirmation of the current US regulatory status of plerixafor products
- Optional: a lower-ranked prediction, **myeloid leukemia** (score 99.02%), has 25 registered trials and 20 publications. Many of these are Phase 1 and Phase 1/2 studies of plerixafor as a chemosensitiser with chemotherapy. It is rated L2 and would be a more evidence-supported direction to evaluate in a separate report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


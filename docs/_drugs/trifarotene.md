---
layout: default
title: Trifarotene
parent: Model Prediction Only (L5)
nav_order: 1260
evidence_level: L5
indication_count: 2
---

# Trifarotene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Trifarotene: From Acne Vulgaris to Zinc, Elevated Plasma

## One-Sentence Summary

Trifarotene is a topical retinoid marketed in the US as AKLIEF cream. It is generally known as a treatment for acne vulgaris, although the dataset does not list an original indication.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but there are **0 clinical trials** and **0 publications** behind this prediction.
Elevated plasma zinc is a laboratory finding rather than a treatable disease, so the high score is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne vulgaris (from general pharmacology; the dataset's approved indication text is empty) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. From general pharmacology, trifarotene is a topical selective retinoic acid receptor gamma (RAR-gamma) agonist, and its efficacy in acne vulgaris is established.

**This prediction is not mechanistically plausible.** Elevated plasma zinc is a laboratory finding with no therapeutic target. Trifarotene has no known role in zinc homeostasis. The high score (0.994) likely reflects retinoid–zinc associations in the knowledge graph rather than any clinical signal. The absence of evidence here reflects a lack of plausibility as well as a lack of studies.

The second-ranked prediction, PAPA syndrome (pyogenic arthritis, pyoderma gangrenosum and acne), is only weakly and indirectly linked. A topical RAR-gamma agonist could at best help the acne lesions. It is unlikely to affect the IL-1-driven arthritis or pyoderma gangrenosum. It also has a high score (99.32%) but no trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211527 | AKLIEF (Galderma Laboratories, L.P.) | Cream (topical) | Not specified in the dataset |

---

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature and no credible mechanism. Elevated plasma zinc is not a treatable disease, so the high score is probably an artifact.

**To proceed, the following is needed:**
- A plausible biological link between RAR-gamma agonism and zinc handling. Without it, this candidate should not advance.
- The FDA package insert warnings and contraindications (a blocking gap for safety screening).
- Mechanism of action data from DrugBank.
- Route compatibility assessment, since trifarotene is available only as a topical cream.
- For the PAPA syndrome prediction, any follow-up would be hypothesis-generating only and limited to the acne component. It needs supporting clinical data first.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


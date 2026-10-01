---
layout: default
title: Difluprednate
parent: Model Prediction Only (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
---

# Difluprednate
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

# Difluprednate: From Ocular Inflammation to Familial Adrenal Hypoplasia with Absent Pituitary Luteinizing Hormone

## One-Sentence Summary

Difluprednate is a potent corticosteroid marketed in the US as an ophthalmic emulsion (brand name Durezol). The source data does not list an approved indication, so ocular inflammation is inferred from the formulation.
The TxGNN model predicts it may be useful for **familial adrenal hypoplasia with absent pituitary luteinizing hormone**, but this prediction has **0 clinical trials** and **0 publications** behind it.
It rests on the model score alone, and the mechanistic rationale does not hold up.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data (ocular inflammation inferred from the ophthalmic emulsion formulation) |
| Predicted New Indication | Familial adrenal hypoplasia with absent pituitary luteinizing hormone |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 (1 NDA and 10 ANDA-type authorizations) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Difluprednate is a potent synthetic glucocorticoid, and its anti-inflammatory effect is well established in eye inflammation. The high TxGNN score most likely reflects knowledge-graph links between glucocorticoids and adrenal-related pathways, not a therapeutic relationship.

The predicted condition is a congenital deficiency of adrenal and pituitary function. Treating it requires systemic hormone replacement, which is a different problem from suppressing local inflammation. A potent topical ophthalmic corticosteroid is not a plausible therapy for it. Systemic absorption could also suppress the hypothalamic-pituitary-adrenal (HPA) axis, which would worsen the underlying condition.

In short, the prediction is a model artifact, not a mechanistically supported repurposing opportunity.

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
| NDA022212 | DUREZOL (Sandoz Inc) | Emulsion | Not listed in source data |
| ANDA211776 | Difluprednate (Cipla USA Inc.) | Emulsion | Not listed in source data |
| ANDA213774 | Difluprednate (Alembic Pharmaceuticals Limited) | Emulsion | Not listed in source data |
| ANDA219441 | Difluprednate (Leading Pharma, LLC) | Emulsion | Not listed in source data |
| ANDA219441 | Difluprednate (Caplin Steriles Limited) | Emulsion | Not listed in source data |

Only 5 of the 11 authorizations are listed here.

---

## Safety Considerations

Please refer to the package insert for safety information.

One point comes from the rationale text: as a potent corticosteroid, difluprednate can suppress the HPA axis with systemic absorption. This is a concern for the predicted adrenal indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it (L5), and a topical ophthalmic corticosteroid is not a plausible treatment for a congenital adrenal and pituitary deficiency. HPA-axis suppression could also do harm.

**Other candidates in the same evidence pack:**
Among the other predicted indications, only **iris disease** (rank 10) has supporting evidence. It has Phase 3 trials, including NCT00407056, an open-label study of 0.05% difluprednate in severe anterior uveitis. That trial is small (n=20) and single-arm, and it is close to on-label use rather than true repurposing. The Phase 3 RCT support for it is partly unconfirmed, because two trial records have truncated titles or do not name the drug. Seborrheic dermatitis and necrobiosis lipoidica are flagged as research questions on class-level evidence only.

**To proceed, the following is needed:**
- Confirm the original approved indication from the FDA label.
- Obtain package insert warnings and contraindications.
- Obtain mechanism of action data from DrugBank.
- Take no further action on this indication unless independent clinical or mechanistic evidence emerges.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


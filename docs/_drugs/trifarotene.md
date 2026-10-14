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

# Trifarotene: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Trifarotene is a topical retinoid originally used to treat acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (acne vulgaris) |
| Predicted New Indication | Elevated plasma zinc |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorization) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on general knowledge of the drug class, trifarotene is a topical retinoid that acts on retinoic acid receptors (RARα, RARβ and RARγ are listed as its targets), and it is best known as an RAR-γ-selective agonist. It is applied as a 0.005% cream, and its high metabolic instability suggests limited systemic exposure.

Its efficacy in acne is established: it completed Phase 3 trials and received FDA approval in October 2019. However, no credible mechanistic link to elevated plasma zinc was identified. Elevated plasma zinc is a metabolic or laboratory finding (for example, from excess supplementation or disordered zinc homeostasis). It is not a disease process known to be modulated by retinoic acid receptor signalling. The high score (0.994) probably reflects indirect network associations, such as retinoid and zinc co-involvement in skin and vitamin A biology, rather than a validated target relationship. Topical use with minimal systemic exposure further weakens the case for any systemic metabolic effect.

The model's second-ranked prediction, **pyogenic arthritis–pyoderma gangrenosum–acne (PAPA) syndrome** (score 99.32%), has only a weak, indirect link. PAPA is an autoinflammatory disorder driven by PSTPIP1 mutations and excess IL-1β. Because acne is one component of the syndrome, trifarotene could at most serve as an adjunct for the skin acne manifestation. There is no evidence that it affects the arthritis, the pyoderma gangrenosum or the core inflammatory drivers. Standard management relies on corticosteroids and IL-1 or TNF inhibitors. No trials or literature were found for this indication either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211527 (cancelled) | AKLIEF (Galderma Laboratories, L.P.) | Cream (topical) | Not listed in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: No drug–drug interactions with other medicines were identified. The interaction query returned only pharmacological target records: trifarotene binds retinoic acid receptors α (RARA), β (RARB) and γ (RARG).
- **Systemic exposure**: Trifarotene is highly metabolically unstable and is expected to have limited systemic exposure when applied topically.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5), and no plausible mechanistic link between a topical retinoid and elevated plasma zinc. The high TxGNN score alone does not justify moving forward. The PAPA syndrome prediction is also weak, and at best would support an adjunct role for the acne component.

**To proceed, the following is needed:**
- Mechanism of action data to allow a proper mechanistic analysis
- FDA package insert warnings and contraindications, which are required before any safety screening
- Evidence that RAR signalling influences zinc homeostasis, before pursuing elevated plasma zinc
- Route compatibility assessment, since the drug is available only as a topical cream and any systemic indication would need a different route
- For PAPA syndrome, a focused review of whether topical trifarotene has a role as an adjunct for the acne manifestation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


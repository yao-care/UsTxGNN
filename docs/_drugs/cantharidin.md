---
layout: default
title: Cantharidin
parent: Model Prediction Only (L5)
nav_order: 491
evidence_level: L5
indication_count: 1
monitor_inn: "CANTHARIDIN"
predicted_indications: ["amenorrhea (disease)"]
last_modified_at: 2026-10-31
description: "Cantharidin: predicted new indication Amenorrhea (evidence level L5). Approved use: No approved indication text is recorded in the license data"
---

# Cantharidin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Cantharidin: From Topical Skin Treatment to Amenorrhea
{: .text-alpha }

## One-Sentence Summary

Cantharidin is a natural-product vesicant used topically on the skin (for example, for warts and molluscum contagiosum).
The TxGNN model predicts it may be effective for **amenorrhea**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text is recorded in the license data (pharmacology data describes topical use for warts and molluscum contagiosum) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Based on known pharmacology, cantharidin inhibits protein phosphatase 2A (PPP2CA) and protein phosphatase 1 (PPP1CA). Disrupting cell-to-cell connections in the skin is how it produces blisters, and PP2A inhibition has also been linked to its anti-cancer activity in laboratory studies.

None of this has an established link to the hormonal and reproductive-axis processes behind amenorrhea. The only support for this prediction is the high TxGNN model (deep learning) score. In addition, cantharidin is highly toxic when taken systemically (renal, gastrointestinal, and genitourinary toxicity), which argues against any plausible systemic use. Until a biological rationale is shown, the prediction should be treated as a computational artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212905 | YCANTH (Verrica Pharmaceuticals Inc.) | Solution | Not recorded (status: valid) |

## Safety Considerations

- **Drug Targets (pharmacology interactions):** Cantharidin inhibits protein phosphatase 2 catalytic subunit alpha (PPP2CA) and protein phosphatase 1 catalytic subunit alpha (PPP1CA). No drug-drug interactions with other medicines were identified in the compiled data.
- **Systemic Toxicity:** Cantharidin is a vesicant, and systemic exposure is associated with renal, gastrointestinal, and genitourinary toxicity.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score behind it: no clinical trials, no literature, and no plausible mechanistic link between a topical PP2A-inhibiting vesicant and amenorrhea. Systemic toxicity further weakens any case for use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (FDA label) for safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- A biological rationale connecting PP2A/PP1 inhibition to reproductive-axis pathology
- Route and formulation compatibility assessment, given that the only known use is topical
- Any preclinical or clinical evidence for amenorrhea
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


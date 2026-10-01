---
layout: default
title: Ivabradine
parent: Model Prediction Only (L5)
nav_order: 820
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ivabradine: From Chronic Heart Failure to Hypertrichosis

## One-Sentence Summary

Ivabradine is a heart-rate-lowering drug that blocks the HCN channel (the "funny" current, If) in the heart's pacemaker cells.
The TxGNN model predicts it may be effective for **hypertrichosis** (excessive hair growth) with a very high score, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model prediction only, and no plausible biological rationale has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied license data (ivabradine is a heart-rate-lowering agent, generally used in chronic heart failure) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed licenses shown are ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied dataset. Ivabradine is generally known as an HCN channel (If current) inhibitor, which slows the resting heart rate. Its established role is cardiovascular.

No link between HCN inhibition and hair-growth biology was identified. Hypertrichosis is not a recognized effect of ivabradine, and the drug has no evident role in treating it. The high score (0.998) is most likely a knowledge-graph proximity artifact, not independent biological evidence.

The other top predictions point the same way. Ambras-type hypertrichosis and isolated hair shaft abnormalities sit close to the hypertrichosis node in the graph. The remaining predictions (a periodontal malformation syndrome, a Dandy-Walker syndrome, nephrogenic syndrome of inappropriate antidiuresis) have no identified connection to HCN inhibition either. All six predictions are model output only, with no supporting trials.

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
| ANDA214051 | Ivabradine (Golden State Medical Supply) | Tablet, film coated | Not provided in source data |
| ANDA213442 | Ivabradine (Zydus Pharmaceuticals USA) | Tablet | Not provided in source data |
| ANDA214051 | Ivabradine (Ingenus Pharmaceuticals) | Tablet, film coated | Not provided in source data |
| ANDA215238 | Ivabradine (Alembic Pharmaceuticals Inc.) | Tablet, film coated | Not provided in source data |
| ANDA215238 | Ivabradine (Alembic Pharmaceuticals Limited) | Tablet, film coated | Not provided in source data |

Twenty licenses are on record in total, and the five above are shown. All are oral formulations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no drug-specific literature, and no plausible mechanistic link between HCN inhibition and hair-growth biology. The evidence level is L5 (model prediction only), so it does not justify further investment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism of action data (MOA) and a documented mechanistic hypothesis linking HCN inhibition to hair-follicle biology
- Any preclinical or clinical signal for ivabradine in hair-growth disorders (none currently exists)
- Original approved indication text for the US licenses, to complete the original-to-new indication comparison

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Liothyronine
parent: Model Prediction Only (L5)
nav_order: 863
evidence_level: L5
indication_count: 10
---

# Liothyronine
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

# Liothyronine: From Thyroid Hormone Replacement to Renal Hypodysplasia/Aplasia

## One-Sentence Summary

Liothyronine is a synthetic form of the thyroid hormone triiodothyronine (T3), marketed in the US as oral tablets. The TxGNN model predicts it may be effective for **renal hypodysplasia/aplasia**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US label data provided (liothyronine is a thyroid hormone) |
| Predicted New Indication | Renal hypodysplasia/aplasia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Liothyronine is a direct thyroid hormone receptor agonist. Thyroid hormone plays a general role in kidney development, which is probably why the knowledge graph links it to this condition.

The link is weak, though. Renal hypodysplasia/aplasia is a structural congenital anomaly, meaning the kidney fails to form properly. No evidence supports postnatal liothyronine treatment for such a condition, and a drug given after birth is unlikely to reverse a structural defect. The high score is more likely a knowledge-graph artifact from shared developmental gene or phenotype associations than a real therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA091382 | liothyronine sodium (Sun Pharmaceutical Industries) | Tablet | Not listed in source data |
| ANDA214803 | Liothyronine sodium (A-S Medication Solutions) | Tablet | Not listed in source data |
| ANDA200295 | Liomny (Sigmapharm Laboratories) | Tablet | Not listed in source data |
| ANDA211510 | Liothyronine Sodium (Teva Pharmaceuticals USA) | Tablet | Not listed in source data |
| ANDA090097 | Liothyronine Sodium (Golden State Medical Supply) | Tablet | Not listed in source data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or literature. A pharmacological benefit for a structural congenital kidney anomaly is also biologically implausible. It should not advance beyond the model-prediction stage.

Among the other top-ranked predictions for liothyronine, only nodular goiter has a plausible, though indirect, mechanistic rationale (TSH suppression). It is a better candidate for further review.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications from the FDA label
- Any preclinical or clinical evidence that thyroid hormone affects the pathology of renal hypodysplasia/aplasia
- Approved indication text for the US licenses, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


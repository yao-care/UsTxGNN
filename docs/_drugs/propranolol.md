---
layout: default
title: Propranolol
parent: Model Prediction Only (L5)
nav_order: 1092
evidence_level: L5
indication_count: 6
---

# Propranolol
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

# Propranolol: From Beta-Blocker Therapy to Distal Myopathy, Tateyama Type

## One-Sentence Summary

Propranolol is a non-selective beta-adrenergic blocker that is widely marketed in the US as generic products.
The TxGNN model predicts it may be effective for **distal myopathy, Tateyama type**, a rare muscle disease.
This prediction is model-only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed products are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Propranolol is known to be a non-selective beta-adrenergic blocker, and it is marketed as extended-release capsules, tablets and an oral solution.

For this indication, the data show **no clear mechanistic link**. Nothing connects beta-blockade to the pathophysiology of this rare distal myopathy. The high score (0.994; rank 13,770) reflects a graph-based association in the TxGNN knowledge graph and is not backed by any biological or clinical evidence.

This prediction should be treated as a computational signal only. Without a plausible mechanism, trials or literature, it does not justify moving into clinical evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA078703 | Propranolol hydrochloride | Capsule, extended release | AvKARE |
| ANDA070322 | Propranolol Hydrochloride | Tablet | Amici Pharmaceuticals LLC |
| ANDA071972 | Propranolol Hydrochloride | Tablet | Amneal Pharmaceuticals NY LLC |
| ANDA070322 | Propranolol Hydrochloride | Tablet | American Health Packaging |
| ANDA070979 | Propranolol Hydrochloride | Solution | Atlantic Biologicals Corp. |

Approved indication text is not included in the supplied data. Only 5 of the 20 authorizations are listed above.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone. There are no trials, no literature and no plausible mechanism linking beta-blockade to this myopathy, so the evidence stays at L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any mechanistic or preclinical rationale linking beta-adrenergic signaling to this myopathy
- Consider prioritizing other predictions for this drug. Cirrhotic cardiomyopathy (5 publications) and cardiomyopathy (3 trials, 19 publications) are both at L3 and carry a "Research Question" recommendation. Cirrhotic cardiomyopathy needs a safety-first review because non-selective beta-blockers may impair circulatory and renal function in advanced cirrhosis. For cardiomyopathy, no efficacy RCT is supplied and the subtype matters.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


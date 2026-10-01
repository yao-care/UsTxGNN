---
layout: default
title: Eplerenone
parent: Model Prediction Only (L5)
nav_order: 662
evidence_level: L5
indication_count: 5
---

# Eplerenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Eplerenone: From Its Approved Indications to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Eplerenone is a marketed oral tablet in the US, but the record does not state its original indications.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**,
but **0 clinical trials** and **0 publications** currently support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the record (approved indication text is empty in all listed licenses) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 19 (the listed licenses are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Eplerenone's original indications are also not recorded, so the link between its existing use and the predicted indication cannot be judged from the supplied data.

As general background, not derived from the supplied data, eplerenone is a selective mineralocorticoid receptor antagonist. Mineralocorticoid receptor signaling has been proposed to contribute to pulmonary vascular remodeling and right-heart fibrosis, which would make the prediction biologically plausible. This link is hypothesis-level and unverified here.

The high score (0.995) may partly reflect graph proximity to hypertension-related nodes rather than a disease-specific mechanism. The other top predictions (malignant hypertensive renal disease, malignant renovascular hypertension, Braddock syndrome) are also supported by the model score alone. For pulmonary hypertension owing to lung disease and/or hypoxia (rank 2), the 20 retrieved publications are generic hypoxia papers. They cover brain aging, cancer biology, altitude and multiple sclerosis, and none mentions eplerenone or pulmonary hypertension. This looks like keyword matching, so that literature count should not be treated as real evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA214663 | Eplerenone (Rising Pharma Holdings) | Tablet | Not listed |
| ANDA207842 | Eplerenone (Proficient Rx) | Coated tablet | Not listed |
| ANDA207842 | Eplerenone (Westminster Pharmaceuticals) | Coated tablet | Not listed |
| ANDA207842 | Eplerenone (AvKARE) | Coated tablet | Not listed |

All products are oral (tablet, coated tablet or film-coated tablet).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (L5), with no trials and no drug-specific literature. Mechanism of action, original indications and safety data are all missing, so the candidate cannot yet move beyond the initial stage.

**To proceed, the following is needed:**
- The FDA package insert, including warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data and original indications, for example from DrugBank
- A targeted search for eplerenone or mineralocorticoid receptor antagonist studies in pulmonary hypertension
- A safety evaluation in the target population, including hyperkalemia and renal function
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Triamterene
parent: Model Prediction Only (L5)
nav_order: 1258
evidence_level: L5
indication_count: 6
---

# Triamterene
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

# Triamterene: From Potassium-Sparing Diuretic Therapy to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic that has been marketed in the US for many years as oral capsules.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
This is a model-only prediction (evidence level L5) and should be put on hold.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied US label data (class: potassium-sparing diuretic) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 9 US licenses (NDA and ANDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Triamterene is known as a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC). It lowers blood pressure through natriuresis (sodium excretion), so a plausible link to hypertensive disease exists.

Malignant hypertensive renal disease is severe, accelerated hypertension with kidney involvement. A diuretic's volume and blood pressure effects are mechanistically relevant, but this is a general rationale, not a specific one. Severe hypertension with renal injury is a clinical emergency usually managed with other approaches, and no data in this pack show triamterene being used for it.

The high score (0.9989) is a computational signal only. The related prediction, malignant renovascular hypertension, has an identical score, which suggests a shared graph-based signal rather than independent support. Hyperkalemia risk in impaired renal function is a major safety concern for this potassium-sparing drug in a kidney-disease setting.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA013174 | Dyrenium | Capsule | Advanz Pharma (US) Corp. |
| NDA013174 | Triamterene | Capsule | Prasco Laboratories |
| ANDA211581 | Triamterene | Capsule | Bryant Ranch Prepack |
| ANDA211581 | Triamterene | Capsule | TRUPHARMA LLC |

Approved indication text was not available in the supplied records. All products are oral capsules.

## Safety Considerations

- **Renal impairment:** Hyperkalemia risk is a key concern when a potassium-sparing diuretic is used in patients with kidney disease, which is directly relevant to this predicted indication.
- **Drug interactions:** No interaction records were found in the queried data.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials or literature for this drug-disease pair. The safety profile (hyperkalemia in renal impairment) is unfavorable for the proposed setting.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications, approved indications) to complete safety screening
- Mechanism of action data from DrugBank
- A targeted literature and trial search for triamterene in severe or malignant hypertension with renal involvement
- A hyperkalemia risk assessment for patients with reduced kidney function

**Note on other predictions:** Among the other predicted indications, *chronic pulmonary heart disease* has four dated, indirect publications (1976–1991) on diuretics in heart failure and cardiopulmonary disease (evidence level L4, "Research Question"). It may be a better candidate for further exploration than the indication above. The two pulmonary hypertension predictions are supported only by keyword matches on "hypoxia," with no relevant evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


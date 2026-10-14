---
layout: default
title: Trandolapril
parent: Model Prediction Only (L5)
nav_order: 1247
evidence_level: L5
indication_count: 6
---

# Trandolapril
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

# Trandolapril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Trandolapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but currently there are **0 clinical trials** and **0 publications** directly supporting this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 3 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, trandolapril is an angiotensin-converting enzyme (ACE) inhibitor. By blocking the renin-angiotensin-aldosterone system (RAAS), it lowers blood pressure and reduces pressure within the kidney's filtering units (intraglomerular pressure). This is biologically plausible for kidney injury caused by severe hypertension.

The predicted indication is closely related to the approved one. Malignant hypertensive renal disease is a kidney complication of severe hypertension, so this is more a subtype extension of the hypertension indication than true repurposing. The high prediction score (0.999) is not backed by any trials or literature in the data compiled for this report.

Other predictions from the same model run include malignant renovascular hypertension, two forms of pulmonary hypertension, Braddock syndrome, and chronic pulmonary heart disease. All are rated L4–L5 and Hold. The pulmonary hypertension and chronic pulmonary heart disease predictions are supported only by indirect preclinical work (cardiac hypertrophy regression, hypoxia-induced coronary vasospasm, and vascular function in rats with chronic heart failure). Malignant renovascular hypertension is mechanistically relevant (renin-dependent), but carries a known risk of acute renal function decline in bilateral renal artery stenosis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078438 | Trandolapril (Rising Pharma Holdings, Inc.) | Tablet | Not listed (status: cancelled) |
| ANDA077522 | Trandolapril (Lupin Pharmaceuticals, Inc.) | Tablet | Not listed (status: cancelled) |
| ANDA078508 | Trandolapril (Epic Pharma, LLC) | Tablet | Not listed (status: cancelled) |

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: Trandolapril is linked to contraindication or caution signals for kidney disease, liver disease, angioedema (including hereditary and RAAS-blocker-induced forms), neutropenia/agranulocytosis, aortic stenosis, hypertrophic cardiomyopathy, renal artery obstruction, hypotensive disorder, heart failure, atrioventricular block, and ventricular tachycardia, among others. Kidney disease and renal artery obstruction are especially relevant to the predicted renal and renovascular indications.
- **Drug Interactions**: 100 interactions were found. Major-level interactions include **potassium citrate** and **potassium bicarbonate** (risk of hyperkalaemia). Moderate-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, glimepiride, chlorpropamide), acetylsalicylic acid, morphine, bupropion, and dronabinol.

Please also refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No clinical trials or literature were found for malignant hypertensive renal disease, and no valid US authorization is currently active. Official label safety information has not yet been reviewed, and the knowledge graph signals kidney-related cautions.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search specific to ACE inhibitors in malignant hypertensive nephropathy
- Clarification of the cancelled US market status, including whether the cancellations are commercial or safety-related
- Assessment of renal safety, especially in renal artery stenosis, and hyperkalaemia monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


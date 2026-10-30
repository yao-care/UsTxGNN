---
layout: default
title: Captopril
parent: Model Prediction Only (L5)
nav_order: 494
evidence_level: L5
indication_count: 3
monitor_inn: "CAPTOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
last_modified_at: 2026-10-30
description: "Captopril: predicted new indication malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Captopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Captopril: ACE inhibitor → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Captopril is an angiotensin-converting enzyme (ACE) inhibitor that lowers blood pressure by acting on the renin-angiotensin system. The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**. This prediction currently has **no registered clinical trials** and **1 publication**, which is a diagnostic case report rather than a treatment study, so the evidence is thin.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9928 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 5) |
| Number of FDA Applications | at least 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Captopril is generally known as an ACE inhibitor: it blocks the conversion of angiotensin I to angiotensin II, which reduces vasoconstriction and aldosterone release.

The renin-angiotensin system is thought to play a central role in malignant hypertension and the kidney injury that accompanies it. This gives a plausible mechanistic reason for the prediction. However, this is a biological rationale only. The one retrieved publication does not test whether captopril treats the condition, so the high score remains a computational prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case report | Clinical Nuclear Medicine | A positive captopril renography (a diagnostic test) in a patient with renin-dependent hypertension. CT showed intact renal arteries but a large chromophobe renal cell carcinoma, and hypertension resolved after nephrectomy. It does not assess captopril as a treatment. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212809 | Captopril (Bryant Ranch Prepack) | Tablet | Not recorded |
| ANDA074505 | Captopril (Golden State Medical Supply, Inc.) | Tablet | Not recorded |
| ANDA074677 | captopril (Method Pharmaceuticals LLC) | Tablet | Not recorded |
| ANDA074477 | Captopril (Solco Healthcare US, LLC) | Tablet | Not recorded |
| ANDA074737 | Captopril (Camber Pharmaceuticals, Inc.) | Tablet | Not recorded |

The licence list may be partial.

## Safety Considerations

No package-insert warnings or contraindications are available in the data compiled for this report. Please refer to the package insert for full safety information.

**Drug Interactions**: 100 interactions were recorded. The ones listed here are mostly moderate:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
- Antidiabetic drugs: metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, chlorpropamide, acetohexamide
- Others: bupropion, morphine, acetylsalicylic acid, dronabinol
- Minor: aluminum hydroxide, calcium carbonate

The data also flag conditions that need caution with this drug, including kidney disease, liver disease, angioedema (including hereditary forms), pancreatitis, neutropenia/agranulocytosis, aortic stenosis, hypotension, systemic lupus erythematosus, diabetic ketoacidosis and potassium deficiency. These are not taken from label text and should be checked against the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9928), and the renin-angiotensin mechanism is plausible. However, there are no clinical trials, and the only publication is a diagnostic case report that does not study treatment. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Studies that directly test captopril for malignant hypertensive renal disease (clinical trials or treatment-focused observational studies)
- Mechanism-of-action data
- Package-insert warnings and contraindications for a safety review
- Licence indication text for the US products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


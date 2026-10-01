---
layout: default
title: Captopril
parent: Model Prediction Only (L5)
nav_order: 494
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Captopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Captopril is a marketed oral ACE inhibitor antihypertensive. The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but this rests on the model score alone. There are **0 registered clinical trials** and **1 publication**, a diagnostic case report that does not test captopril as treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (captopril is a marketed antihypertensive; the label text in the source data is blank) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L4 (mechanistic rationale only; no supporting treatment study) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all shown listings are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Captopril is known to be an ACE inhibitor. It blocks angiotensin II formation, which lowers vasoconstriction and pressure inside the kidney's filtering units.

Malignant hypertension damages the kidney through severe, renin-driven pressure injury (malignant nephrosclerosis). Blocking the renin-angiotensin-aldosterone system (RAAS) is therefore biologically plausible. This is a theoretical link, not something the retrieved evidence demonstrates.

It is also unclear whether this counts as true repurposing. Captopril is already an antihypertensive, so this may be an extension of an existing use. The pack does not list the original indication, which makes it hard to judge how far the new indication departs from it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case report (diagnostic) | Clin Nucl Med | A patient had a positive captopril renography but no renal artery stenosis. The cause was a large chromophobe renal cell carcinoma, and renin-dependent hypertension resolved after nephrectomy. Captopril was used as a diagnostic tool, not as treatment. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212809 | Captopril (Bryant Ranch Prepack) | Tablet | Not stated in source data |
| ANDA074505 | Captopril (Golden State Medical Supply) | Tablet | Not stated in source data |
| ANDA074677 | Captopril (Method Pharmaceuticals) | Tablet | Not stated in source data |
| ANDA074505 | Captopril (Hikma Pharmaceuticals USA) | Tablet | Not stated in source data |
| ANDA074677 | Captopril (Amici Pharmaceuticals) | Tablet | Not stated in source data |

All listed products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information.

The pack notes one class-level concern from a related prediction: ACE inhibitors can cause acute renal failure in bilateral renal artery stenosis or a solitary kidney. No drug interactions were found in the queried database.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.28%) is a prediction only. No trials exist, and the single paper is a diagnostic case report with no therapeutic support. It is also unclear whether this is genuine repurposing.

Among the other predictions, malignant renovascular hypertension (same score, more literature, and a stronger mechanistic fit) is the better candidate to follow up. Its evidence is still mostly indirect (diagnostic and review papers).

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which are currently blocking the safety screen
- The drug's original indication and MOA data (e.g., from DrugBank)
- Clinical or observational evidence of captopril used as treatment in malignant hypertensive nephropathy
- A renal safety plan for patients with renal artery stenosis or a solitary kidney
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


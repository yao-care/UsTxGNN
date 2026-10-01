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

# Trandolapril: From ACE Inhibitor Therapy to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Trandolapril is an ACE inhibitor marketed in the US as generic oral tablets, but the record contains no approved-indication text.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 (all listed licenses are ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Trandolapril belongs to the ACE inhibitor class, which blocks the renin-angiotensin-aldosterone system (RAAS). The record lists no original indications, so the high TxGNN score cannot be checked against the drug's labeled use.

Malignant hypertension and its renal injury plausibly involve RAAS activation, so RAAS blockade is biologically reasonable. This is a class-level rationale only. No trial or literature data directly support it.

TxGNN also ranks several related conditions highly: malignant renovascular hypertension, several forms of pulmonary hypertension, Braddock syndrome and chronic pulmonary heart disease. For renovascular hypertension, ACE inhibitors can cause hemodynamic harm in bilateral renal artery stenosis, so safety needs separate review. The only drug-specific finding across the whole set is a 1996 rat study of long-term trandolapril in chronic heart failure (PMID 8989645), which is preclinical evidence for the chronic pulmonary heart disease prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA078438 | Trandolapril | Tablet | Rising Pharma Holdings, Inc. |
| ANDA077522 | Trandolapril | Tablet | Lupin Pharmaceuticals, Inc. |
| ANDA078508 | Trandolapril | Tablet | Epic Pharma, LLC |
| ANDA078438 | Trandolapril | Tablet | Bryant Ranch Prepack |
| ANDA077522 | Trandolapril | Tablet | Lupin Pharmaceuticals, Inc. |

Only the oral tablet route is listed. The record contains no approved-indication text.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were available in the record.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score (99.92%) and a class-level RAAS rationale. There are no trials or literature for malignant hypertensive renal disease, and the record has no MOA, original-indication or safety data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data and the drug's labeled indications, to check the prediction against known use
- A targeted search for trandolapril or ACE inhibitor studies in malignant hypertension and hypertensive nephropathy
- For chronic pulmonary heart disease, confirmation of PMID 8989645 from the full text, since only the abstract was supplied
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


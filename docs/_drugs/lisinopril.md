---
layout: default
title: Lisinopril
parent: Model Prediction Only (L5)
nav_order: 864
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From Hypertension to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor that is already marketed in the US as an antihypertensive.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but **no clinical trials and no publications** were retrieved for this indication, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (from the pack's rationale text; the license indication text is empty) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lisinopril is an ACE inhibitor. It is established in cardiovascular use, and mechanistically it may be applicable to myocardial infarction.

ACE inhibition reduces angiotensin II-mediated remodeling and afterload, which is plausible after a heart attack. However, lisinopril's labeled use in acute MI is not evidence for this specific anatomical subtype. Posteroinferior MI has an identical score (99.90%), which suggests both come from the same graph neighborhood and are not independent findings. Septal MI is closely related and scores 99.88%. The high score most likely reflects a general MI association in the knowledge graph.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The pack shows 20 licenses in total. The five main ones are listed below. Approved-indication text was not provided for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076180 | Lisinopril | Tablet | Proficient Rx LP |
| ANDA075903 | Lisinopril | Tablet | XLCare Pharmaceuticals Inc. |
| ANDA075903 | Lisinopril | Tablet | Legacy Pharmaceutical Packaging, LLC |
| NDA019777 | Zestril | Tablet | Upsher-Smith Laboratories, LLC |
| NDA019777 | Zestril | Tablet | Upsher-Smith Laboratories, LLC |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or literature for this subtype. It is also a subtype of a condition lisinopril is already labeled for, so the repurposing value is low. Among the other ten predictions, chronic pulmonary heart disease (rank 9) has the most supporting evidence. It is rated L3 with two lisinopril-specific clinical reports (PMID 14524095 and PMID 17047621), although their design and size are unverified.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking data gap; safety screening cannot start without them)
- Mechanism of action data from DrugBank
- A subtype-specific search for posterolateral MI trials and literature, including whether existing MI evidence already covers it
- Consideration of moving the chronic pulmonary heart disease candidate forward first. This requires full-text appraisal of the two lisinopril reports, including bias, hypotension and renal function
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


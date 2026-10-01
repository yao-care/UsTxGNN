---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 1101
evidence_level: L5
indication_count: 5
---

# Quinapril
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

# Quinapril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Quinapril is an ACE inhibitor marketed in the US for hypertension. The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are currently **0 clinical trials** and **0 publications** supporting this specific pair. The prediction rests on the model score and mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (the US license records supplied no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all generic ANDA authorizations) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Quinapril is an ACE inhibitor. Detailed mechanism-of-action data was not supplied, but the class effect is well known: it blocks the conversion of angiotensin I to angiotensin II, lowering vasoconstriction and aldosterone-driven fluid retention.

Renovascular hypertension is driven largely by activation of the renin-angiotensin system. This makes ACE inhibition biologically plausible, and it is close to quinapril's existing use in hypertension. The very high TxGNN score (99.86%) is probably partly explained by that existing hypertension link, so it should not be read as independent confirmation.

Two cautions apply. First, ACE inhibitors can cause acute renal function decline in bilateral renal artery stenosis or stenosis of a solitary kidney, which is exactly the setting of renovascular hypertension. Second, "malignant" hypertension is a hypertensive emergency, and an oral ACE inhibitor is not an established acute therapy for it.

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
| ANDA078457 | Quinapril | Tablet | Cipla USA Inc. |
| ANDA077690 | Quinapril | Tablet | Lupin Pharmaceuticals, Inc. |
| ANDA205823 | Quinapril | Tablet | Solco Healthcare US, LLC |
| ANDA077690 | Quinapril | Tablet | BluePoint Laboratories |

Approved indication text was not supplied in the source records. Only oral tablet forms (including film-coated tablets) are listed, and 4 distinct entries are shown from the 20 authorizations.

---

## Safety Considerations

- **Renal risk (from the prediction rationale):** ACE inhibitors carry a known risk of acute renal function decline in bilateral renal artery stenosis or stenosis of a solitary kidney. Renal function and potassium monitoring would be essential in any follow-up.
- **Drug Interactions:** No interaction records were found in the queried source.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-based only (L5), with no supporting trials or literature for this disease. The mechanism is plausible, but the renal safety concern in renal artery stenosis is significant. An oral ACE inhibitor is also not an established therapy for malignant hypertension, which is an emergency.

The other top predictions have the same evidence gap:
- **Malignant hypertensive renal disease:** no trials or literature.
- **Pulmonary hypertension (two entries):** the 20 retrieved papers are general hypoxia articles that do not address quinapril or ACE inhibitors.
- **Braddock syndrome:** no clear mechanistic rationale.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism-of-action data from DrugBank
- A targeted literature search on ACE inhibitors in renovascular and malignant hypertension
- A safety review for patients with renal artery stenosis, including renal function and potassium monitoring
- Confirmation of the original US-labeled indications

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


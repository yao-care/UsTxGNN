---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 809
evidence_level: L5
indication_count: 4
---

# Irbesartan
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

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB) marketed in the US as generic oral tablets. The supplied licence records do not state its approved indication, but ARBs of this class are used for hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (all licence indication fields are empty) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed below are ANDAs, i.e. generic approvals) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (the MOA field is a data gap). Irbesartan is known to be an angiotensin II type 1 receptor blocker. Renin-angiotensin system (RAS) activation plausibly contributes to renovascular hypertension, so the prediction is biologically coherent.

The predicted indication is a severe form of hypertension, which is at least in the same disease family as the drug's usual use. There are several reasons for caution:
- ARBs carry a known caution in renal artery stenosis, because they can reduce renal function.
- Malignant hypertension is a hypertensive emergency, usually managed with parenteral agents rather than oral ARBs.
- No trials or literature were supplied, so the support is model prediction plus general pharmacology.

The model also produced three related predictions with similar scores. Malignant hypertensive renal disease (99.31%) has the same score as this one, which suggests duplicate or closely related ontology nodes rather than independent signals. The two pulmonary hypertension predictions (99.25%) also share one score. The 20 records retrieved for the hypoxia-related pulmonary hypertension prediction cover hypoxia biology in general (brain aging, cancer, altitude) and never mention irbesartan or ARBs, so they look like keyword matches, not drug-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA202910 | Irbesartan | Tablet | AvPAK |
| ANDA203071 | Irbesartan | Tablet | A-S Medication Solutions |
| ANDA091236 | Irbesartan | Tablet | Alembic Pharmaceuticals Inc. |
| ANDA202910 | Irbesartan | Tablet | Bryant Ranch Prepack |
| ANDA203071 | Irbesartan | Tablet | Solco Healthcare U.S., LLC |

Approved indication text was not supplied for any of these licences. Available forms are oral tablets and film-coated tablets.

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records (0 interactions found), which does not confirm absence of interactions.
- **Class caution (from general pharmacology, not a supplied label)**: ARBs can reduce renal function in renal artery stenosis, which is directly relevant to renovascular hypertension.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.31%), but the evidence level is L5. There are no trials or publications for this drug-disease pair. The renal artery stenosis caution and the emergency nature of malignant hypertension work against a simple oral-ARB use case.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (currently a blocking gap)
- Mechanism of action data from DrugBank
- A targeted search for irbesartan or ARB studies in renovascular and malignant hypertension
- Confirmation of whether the two malignant hypertension predictions are duplicate ontology nodes
- A route and setting assessment, since oral tablets may not suit a hypertensive emergency

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


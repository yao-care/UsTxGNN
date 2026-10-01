---
layout: default
title: Acebutolol
parent: Model Prediction Only (L5)
nav_order: 64
evidence_level: L5
indication_count: 2
---

# Acebutolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Acebutolol: From Beta-Blocker Therapy to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Acebutolol is an oral beta-blocker (a cardioselective beta-1 blocker with mild intrinsic sympathomimetic activity). The labelled indication text is not included in the source record.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**.
This prediction has **0 clinical trials** and **0 publications** directly supporting it, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 10 (all listed licenses are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known drug-class information, acebutolol is a cardioselective beta-1 blocker. Beta-1 blockade reduces renin release, which lowers blood pressure. Hypertension-driven kidney injury is plausibly relevant to that effect.

Malignant hypertensive renal disease is a severe form of hypertension affecting the kidney. It is a subtype of a use already established for the drug class, not a new mechanism. The link is inferred from class pharmacology, not from data in the record.

There is also a practical concern. Malignant hypertension is a hypertensive emergency and is usually managed with parenteral agents. An oral capsule beta-blocker is not an obvious fit. Route compatibility and similarity to the original indication have not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this indication.

For context, the second-ranked prediction, malignant renovascular hypertension (same score, 99.10%), has one indirect record. [PMID 768911](https://pubmed.ncbi.nlm.nih.gov/768911/) is a 1975 open clinical study in *La Nouvelle presse medicale*. In it, 50 hypertensive patients received acebutolol alone or with other agents for one year. Treatment was rated good or moderate in 74% of patients and failed in 26%. The abstract also mentions renovascular hypertension, but the record does not show that it addresses the malignant subtype.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074007 | Acebutolol Hydrochloride (Golden State Medical Supply, Inc.) | Capsule | Not provided in source data |
| ANDA074007 | Acebutolol Hydrochloride (ANI Pharmaceuticals, Inc.) | Capsule | Not provided in source data |
| ANDA075047 | Acebutolol Hydrochloride (AvKARE) | Capsule | Not provided in source data |
| ANDA075047 | Acebutolol Hydrochloride (AvPAK) | Capsule | Not provided in source data |
| ANDA075047 | Acebutolol Hydrochloride (Amneal Pharmaceuticals of New York LLC) | Capsule | Not provided in source data |

Only the oral route (capsule) is available.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the source data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a high model score behind it, with no direct clinical trials or publications. Malignant hypertension is normally treated with parenteral agents, so an oral beta-blocker is a questionable fit. The lack of package insert safety data also blocks progression past the first screening stage.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (this blocks safety screening)
- Detailed mechanism of action data (MOA)
- Direct clinical evidence for acebutolol in malignant hypertension or hypertensive kidney injury
- A route-compatibility assessment (oral capsule versus the emergency setting)
- A review of how the prediction relates to the drug's labelled indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


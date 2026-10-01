---
layout: default
title: Zinc Chloride
parent: Model Prediction Only (L5)
nav_order: 1306
evidence_level: L5
indication_count: 3
---

# Zinc Chloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Zinc Chloride: From Zinc Products (Indication Not Recorded) to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Zinc chloride is marketed in the US as an injectable zinc product, among other forms, but the source data record no approved indication text.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.
Its third-ranked prediction, dry eye syndrome, has **2 completed trials**, both of limited relevance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available US license data |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 license records (includes NDA, ANDA and unnumbered entries) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Zinc chloride is a zinc salt sold in several forms in the US, including injection, pellets, tablets, spray, liquid and gel. No approved indication text was captured, so the link between its original use and the new indication cannot be assessed from these data.

One speculative link is zinc's role as a cofactor for antioxidant enzymes such as superoxide dismutase (SOD). Oxidative stress is thought to contribute to retinal microvascular damage in diabetic retinopathy, so this could be relevant. No retrieved trial or publication supports it. The 0.993 TxGNN score reflects knowledge-graph patterns only and is not evidence of efficacy.

The model's other top predictions are Sjögren syndrome (99.18%) and dry eye syndrome (99.18%). Both are ocular surface or exocrine conditions. Zinc's roles in immune regulation, epithelial integrity and antioxidant activity are possible, unverified explanations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

For reference, the third-ranked prediction, **dry eye syndrome**, has two completed trials. Neither clearly tests zinc chloride itself:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02951910](https://clinicaltrials.gov/study/NCT02951910) | Phase 4 | Completed | 20 | Effect of zinc-hyaluronate (a zinc-hyaluronate complex made with zinc chloride) on ocular surface sensation in dry eye. Relevance grade B: indirect evidence because the agent is a different formulation, and the sample is small. |
| [NCT01541891](https://clinicaltrials.gov/study/NCT01541891) | Phase 2 | Completed | 30 | PRO-148 ophthalmic solution vs Systane in mild-to-moderate dry eye. Relevance grade C: the data do not say whether PRO-148 contains zinc, so relevance is unconfirmed. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The data record no approved indication text for any license. Dosage forms listed across all records are injection, injection solution, pellet, tablet, soluble tablet, spray, liquid and gel.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018959 | ZINC (Hospira, Inc.) | Injection, solution | Not stated in source data |
| ANDA212007 | Zinc Chloride (Exela Pharma Sciences, LLC) | Injection | Not stated in source data |
| Number not listed | Zincum Muriaticum (Hahnemann Laboratories, Inc.) | Pellet | Not stated in source data |
| Number not listed | Zincum Muriaticum (Hahnemann Laboratories, Inc.) | Pellet | Not stated in source data |
| Number not listed | Zincum Muriaticum (Hahnemann Laboratories, Inc.) | Pellet | Not stated in source data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The diabetic retinopathy prediction rests on a model score alone, with no trials, no literature and no mechanism data (L5). The only nearby signal is in dry eye, and it is indirect: one zinc-hyaluronate study and one trial of unknown composition. Package insert safety information has not been obtained, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the US zinc chloride products (blocking for safety screening)
- Mechanism of action data (for example from DrugBank) to test the zinc, oxidative stress and retinal microvascular link
- A literature and trial search specific to zinc and diabetic retinopathy
- For dry eye, confirmation of the PRO-148 composition and a trial using zinc chloride or a clearly defined zinc salt
- Route compatibility assessment, since ocular or retinal delivery is not covered by the current US forms (injection, oral, pellet, spray, liquid, gel)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


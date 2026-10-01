---
layout: default
title: Diltiazem
parent: Model Prediction Only (L5)
nav_order: 609
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Diltiazem: From Cardiovascular Use to Obsolete Susceptibility to Ischemic Stroke

## One-Sentence Summary

Diltiazem is a calcium channel blocker sold in the US in oral extended-release and injectable forms. The TxGNN model predicts it may be relevant to **obsolete susceptibility to ischemic stroke**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the record (the approved indication text of the listed licenses is empty) |
| Predicted New Indication | obsolete susceptibility to ischemic stroke |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge (not from this dataset), diltiazem is an L-type calcium channel blocker. Its vasodilatory and blood-pressure-lowering effects could plausibly relate to stroke risk, but this dataset offers no evidence to verify that link.

The predicted disease name is also an obsolete ontology term. "Susceptibility to ischemic stroke" is a vague concept rather than a defined clinical indication. Before any evidence search or review, it should be mapped to a current term, such as ischemic stroke prevention. The similarity between the original and new indications is still pending, because no original indications were recorded.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA216968 | Diltiazem Hydrochloride | Capsule, extended release | Not listed |
| ANDA074617 | Diltiazem Hydrochloride | Injection, solution | Not listed |
| ANDA075116 | Diltiazem Hydrochloride | Capsule, extended release | Not listed |
| ANDA212317 | Diltiazem Hydrochloride | Capsule, extended release | Not listed |
| ANDA208783 | Diltiazem Hydrochloride | Capsule, extended release | Not listed |

Other US dosage forms include tablets (film-coated and extended-release), coated extended-release capsules, and lyophilized powder for injection.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug in the dataset.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model prediction score (L5). There are no trials or publications, and the predicted disease term is obsolete and ill-defined. The evidence is not enough to move forward.

**To proceed, the following is needed:**
- Map the obsolete disease term to a current one (for example, ischemic stroke prevention)
- Search trials and literature under the mapped term
- Obtain mechanism of action data from DrugBank
- Obtain the package insert warnings and contraindications (currently a blocking gap for safety screening)
- Confirm the approved indications for the US licenses
- Assess route compatibility (oral vs. injectable) once the indication is defined
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Midodrine
parent: Model Prediction Only (L5)
nav_order: 927
evidence_level: L5
indication_count: 10
---

# Midodrine
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

# Midodrine: From Orthostatic Hypotension to Variably Protease-Sensitive Prionopathy

## One-Sentence Summary

Midodrine is an oral drug used to raise blood pressure in symptomatic orthostatic hypotension.
The TxGNN model predicts it may be effective for **variably protease-sensitive prionopathy**, a rare prion disease.
Currently **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Symptomatic orthostatic hypotension (the indication text is blank in the US license records) |
| Predicted New Indication | Variably protease-sensitive prionopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. From the pharmacology review, midodrine is a prodrug. Its active metabolite, desglymidodrine, is a selective peripheral alpha-1 adrenergic agonist that raises vascular tone and blood pressure.

That mechanism does not plausibly connect to variably protease-sensitive prionopathy. This is a neurodegenerative prion disease driven by abnormal prion protein. Midodrine does not cross the blood-brain barrier significantly and has no known effect on prion biology. The high TxGNN score is a knowledge-graph association only. It has no clinical or literature support, and the prediction should be treated as a likely model artifact.

For context, the same run also produced a prediction that does have evidence behind it: **hypotensive disorder** (rank 4). It has 9 linked clinical trials and 20 publications, and would be graded L1. However, it is essentially the drug's established use rather than true repurposing, and it is not the prediction evaluated in this report. Other top-ranked predictions (such as ADHD, sinoatrial node disease and sinoatrial block) also lack support. For the last two, midodrine's reflex bradycardia is a safety concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212774 | Midodrine Hydrochloride (Bryant Ranch Prepack) | Tablet | Not listed in license record |
| ANDA217271 | Midodrine Hydrochloride (First Nation Group, LLC) | Tablet | Not listed in license record |
| ANDA207169 | Midodrine Hydrochloride (Bryant Ranch Prepack) | Tablet | Not listed in license record |
| ANDA214734 | Midodrine Hydrochloride (Alembic Pharmaceuticals Inc.) | Tablet | Not listed in license record |
| ANDA212543 | Midodrine Hydrochloride (TruPharma, LLC) | Tablet | Not listed in license record |

All 20 authorizations are oral tablets. The five above are the first five in the record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5). There is also no plausible mechanism linking a peripheral alpha-1 agonist to a prion disease. Based on current evidence, this candidate should not advance.

**To proceed, the following is needed:**
- Any mechanistic or preclinical evidence linking alpha-1 adrenergic agonism to prion pathology
- The FDA package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- Redirecting effort to the hypotensive disorder prediction, after checking that midodrine is the actual intervention arm in each linked trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


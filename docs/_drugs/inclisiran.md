---
layout: default
title: Inclisiran
parent: Model Prediction Only (L5)
nav_order: 794
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: From LDL-C Lowering to Potassium Deficiency Disease

## One-Sentence Summary

Inclisiran is a PCSK9-targeting siRNA marketed in the US as LEQVIO to lower LDL cholesterol.
The TxGNN model predicts it may be effective for **potassium deficiency disease**, with a very high score of 99.93%.
However, there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | LDL-C lowering (the license record has no indication text) |
| Predicted New Indication | Potassium deficiency disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Inclisiran is a small interfering RNA that silences PCSK9 to lower LDL-C, and it is administered as a subcutaneous injection.

The prediction is not mechanistically plausible on current information. PCSK9 silencing and LDL-C lowering have no known role in potassium handling or electrolyte balance. Potassium deficiency is typically driven by renal or gastrointestinal losses, medications, or inadequate intake, none of which is a target of this drug.

The high TxGNN score (0.9993, rank 2520) reflects patterns in the knowledge graph rather than clinical or literature support. It should be treated as a hypothesis-generating signal, not evidence of efficacy.

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
| NDA214012 | LEQVIO (Novartis Pharmaceuticals Corporation) | Injection, solution | Not listed in the record |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, registry, or literature evidence for potassium deficiency disease, and no plausible mechanistic link between PCSK9 silencing and potassium homeostasis. The prediction stays at L5.

The other top-10 predictions are also L5 and Hold. Two Phase 3 inclisiran trials (NCT06597019 and NCT06597006, in pediatric familial hypercholesterolemia) were matched to "aortic malformation". They appear to be lipid-lowering studies unrelated to that indication, so they do not change this assessment.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data (for example, from DrugBank)
- A documented biological rationale linking PCSK9 silencing to potassium regulation, plus any preclinical or observational signal
- Confirmation of the approved indication text for NDA214012
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


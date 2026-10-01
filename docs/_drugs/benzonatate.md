---
layout: default
title: Benzonatate
parent: Model Prediction Only (L5)
nav_order: 449
evidence_level: L5
indication_count: 2
---

# Benzonatate
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

# Benzonatate: From Cough Suppression to Cauda Equina Syndrome

## One-Sentence Summary

Benzonatate is an oral, ester-type local anesthetic marketed in the US as a cough suppressant. The Evidence Pack does not list an approved indication, so this is based on general knowledge.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Evidence Pack (general knowledge: symptomatic relief of cough) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (listed licenses are ANDAs, i.e., generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general knowledge, benzonatate blocks voltage-gated sodium channels in peripheral stretch receptors, which dampens the cough reflex.
A sodium-channel effect on nerve root pain or neuropathic symptoms is one possible link to cauda equina syndrome. This link is speculative.

Cauda equina syndrome is a compressive surgical emergency. A symptomatic sodium-channel blocker would not address the underlying pathology. The 99.66% score comes from graph-based prediction alone, with no trials or literature behind it. Mechanistic similarity to the original indication is still pending assessment.

The second-ranked prediction is **obsolete neurogenic bladder (disease)**, with a score of 99.39%. Local anesthetics can in principle dampen bladder afferent signaling, which is loosely plausible. However, there is no clinical or literature evidence for oral benzonatate here. The disease term is obsolete in the ontology and should be mapped to a current term (e.g., neurogenic detrusor overactivity) before further evaluation.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040682 (Redpharm Drug) | Benzonatate | Capsule, liquid filled | Not provided |
| ANDA202765 (RemedyRepack) | Benzonatate | Capsule | Not provided |
| ANDA081297 (Golden State Medical Supply) | Benzonatate | Capsule | Not provided |
| ANDA081297 (NuCare Pharmaceuticals) | Benzonatate | Capsule | Not provided |
| ANDA040597 (A-S Medication Solutions) | Benzonatate | Capsule | Not provided |

All listed products are oral. There are 20 licenses in total; the table shows the first 5.

## Safety Considerations

Please refer to the package insert for safety information.

One caution from the prediction rationale: benzonatate has known overdose risks (seizures, arrhythmia, CNS effects). These would need assessment in a neurologically impaired population.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. No clinical trials or publications support it, and the proposed mechanism does not fit a compressive surgical emergency.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (this blocks safety screening)
- Mechanism of action data (e.g., from DrugBank)
- The approved indication text from the label
- Mapping of "obsolete neurogenic bladder" to a current disease term
- Any preclinical, mechanistic, or clinical evidence that links oral benzonatate to nerve root or bladder-related symptoms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


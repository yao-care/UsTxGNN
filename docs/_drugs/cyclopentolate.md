---
layout: default
title: Cyclopentolate
parent: Model Prediction Only (L5)
nav_order: 555
evidence_level: L5
indication_count: 3
---

# Cyclopentolate
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

# Cyclopentolate: From Original Indication (Not Recorded) to Cauda Equina Syndrome

## One-Sentence Summary

Cyclopentolate is marketed in the US as topical solution/drops, but the regulatory data provided does not record an approved indication.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
but **0 clinical trials** and **0 publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the provided regulatory data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 (all ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology (not from the provided data), cyclopentolate is generally known as a muscarinic antagonist formulated for topical use. Any link to the predicted indication would therefore be indirect, for example through anticholinergic control of neurogenic bladder symptoms.

Cauda equina syndrome is caused by compression of the lower spinal nerve roots and needs urgent surgical decompression. An anticholinergic could at most relieve some symptoms and would not treat the cause. A topical eye-drop product is also a poor fit for a neurosurgical emergency. The rationale is weak, and the 0.995 score should be read as a model signal, not as evidence of efficacy.

The other two top TxGNN predictions are obsolete neurogenic bladder (99.40%) and irritable bowel syndrome (99.27%). Both are also L5 with no trials or literature, and both would depend on systemic anticholinergic exposure.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040075 | Cyclopentolate Hydrochloride (Bausch & Lomb) | Solution/Drops | Not listed |
| ANDA084110 | Cyclogyl (Alcon) | Solution/Drops | Not listed |
| ANDA084108 | Cyclogyl (Alcon) | Solution/Drops | Not listed |
| ANDA084110 | Cyclopentolate Hydrochloride (Sandoz) | Solution | Not listed |
| ANDA084109 | Cyclogyl (Alcon) | Solution/Drops | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (L5), and the mechanism is not documented. The predicted indication is a surgical emergency that a topical anticholinergic would not address.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data, for example from DrugBank
- The approved indication text, to establish the original indication
- Route and formulation feasibility assessment (systemic or intravesical use is not covered by current data)
- Mapping of "obsolete neurogenic bladder" to a current disease term before any follow-up
- Preclinical or clinical evidence for any of the predicted indications, in order to move beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


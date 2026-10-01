---
layout: default
title: Zonisamide
parent: Model Prediction Only (L5)
nav_order: 1312
evidence_level: L5
indication_count: 10
---

# Zonisamide
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

# Zonisamide: From Epilepsy (Partial Seizures) to Tourette Syndrome

## One-Sentence Summary

Zonisamide is an oral antiseizure drug, used mainly as an add-on treatment for partial seizures.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, partial seizures (inferred from the literature, since the US license records supplied have no indication text) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations in total (NDA and ANDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Zonisamide is a marketed antiseizure drug. It is generally described as blocking voltage-gated sodium channels and T-type calcium channels and modulating glutamate/GABA signaling. One possible link to Tourette syndrome is that this could dampen cortico-striatal hyperexcitability, which is thought to underlie tics. This link is speculative and rests on the prediction alone.

The relationship between epilepsy and Tourette syndrome is indirect. Both are neurological conditions involving abnormal neuronal circuit activity, which is likely why the knowledge graph places them close together. No study in the supplied data tests zonisamide in tic disorders.

One caution comes from the literature. A pragmatic review of antiseizure-medication-induced obsessive-compulsive and tic disorder ([PMID 36005856](https://pubmed.ncbi.nlm.nih.gov/36005856/), 2022) appeared in the retrieved records. It raises a possible tic-related safety signal rather than a benefit, and it needs to be checked before any further work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020789 | Zonegran | Capsule | Advanz Pharma (US) Corp. |
| ANDA077651 | Zonisamide | Capsule | Glenmark Pharmaceuticals Inc., USA |
| ANDA077634 | Zonisamide | Capsule | Sun Pharmaceutical Industries, Inc. |
| ANDA077645 | Zonisamide | Capsule | Aurobindo Pharma Limited |
| ANDA077634 | Zonisamide | Capsule | Direct_Rx |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the supplied data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score (99.85%), with no trials, no literature and a mechanistic link that is speculative. A tic-related safety signal for antiseizure drugs also needs to be checked.

**To proceed, the following is needed:**
- A targeted literature and trial search for zonisamide in Tourette syndrome and tic disorders
- The US package insert, to confirm the approved indication, warnings and contraindications
- Detailed mechanism of action data from DrugBank
- A review of the tic and obsessive-compulsive adverse-effect signal (PMID 36005856)

Note: other predictions for this drug in the same record have stronger support than Tourette syndrome. Absence epilepsy is graded L3 (Proceed with Guardrails) and manic bipolar affective disorder is graded L2 (Research Question). These may be better candidates for prioritization.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Mercuric Iodide
parent: Model Prediction Only (L5)
nav_order: 902
evidence_level: L5
indication_count: 10
---

# Mercuric Iodide
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

# Mercuric Iodide: From an Unspecified Original Indication to Ventricular Tachycardia

## One-Sentence Summary

Mercuric iodide is an inorganic mercury salt. The only U.S. record is a cancelled homeopathic pellet product, and no approved indication is documented.
The TxGNN model predicts it may be effective for **ventricular tachycardia**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
It is a purely computational result, and mercury compounds are known to be cardiotoxic.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text available |
| Predicted New Indication | Ventricular tachycardia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Mercuric iodide is a toxic inorganic mercury salt with no known antiarrhythmic activity, and no approved indication is recorded for it, so its relationship to the predicted indication cannot be established.

The high TxGNN score most likely reflects network proximity among arrhythmia-related nodes in the knowledge graph, not a pharmacological rationale. Mercury compounds are generally associated with causing arrhythmia and cardiac toxicity rather than treating it. On the data compiled for this report, the prediction is not mechanistically supported.

Other top-ranked predictions are also cardiac rhythm or conduction disorders, and none has clinical or literature support:

| Rank | Predicted Disease | TxGNN Score | Evidence Level |
|-----|------|------|------|
| 2 | Bundle branch block (obsolete term) | 99.99% | L5 |
| 3 | Multifocal atrial tachycardia | 99.98% | L5 |
| 4 | His bundle tachycardia | 99.98% | L5 |
| 5 | Periodic paralysis with transient compartment-like syndrome | 99.98% | L5 |
| 6 | Arrhythmogenic right ventricular cardiomyopathy | 99.98% | L5 |
| 7 | Idiopathic neonatal atrial flutter | 99.97% | L5 |
| 8 | Incessant infant ventricular tachycardia | 99.97% | L5 |
| 9 | Catecholaminergic polymorphic ventricular tachycardia | 99.97% | L5 |
| 10 | Atrial fibrillation | 99.96% | L5 |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available (cancelled) | Mercurius Iodatus Ruber (Hahnemann Laboratories, Inc.) | Pellet | Not specified |

## Safety Considerations

- **Drug Interactions**: No interaction records were found.
- **Toxicity context**: Mercury compounds are recognized cardiac and neurotoxicants. Use in neonates and infants (as in ranks 7 and 8) is not defensible without evidence.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5), with no clinical trials or publications. There is no documented mechanism, the only U.S. license is cancelled, and mercury's known cardiotoxicity argues against use in arrhythmia. The risk-benefit profile is unfavorable.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank)
- FDA package insert warnings and contraindications for a formal safety screen
- Preclinical evidence that the compound has any antiarrhythmic effect at non-toxic exposure
- Route and formulation compatibility assessment, which is currently pending
- Independent literature review confirming a plausible biological link before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


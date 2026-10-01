---
layout: default
title: Verapamil
parent: Model Prediction Only (L5)
nav_order: 1287
evidence_level: L5
indication_count: 7
---

# Verapamil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Verapamil: From Hypertension to Obsolete Bundle Branch Block

## One-Sentence Summary

Verapamil is an L-type calcium channel blocker marketed in the US as injection and oral tablets and capsules, and it is already used as an antihypertensive.
The TxGNN model predicts it may be effective for **obsolete bundle branch block**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.
The disease term is flagged as obsolete, so the high score may be an ontology artifact. There is also a mechanistic safety concern.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records (the approved indication text is blank). Hypertension is taken from the Evidence Pack's rationale notes. |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (the five examples in the data are all ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Verapamil is an L-type calcium channel blocker, and its efficacy in cardiovascular conditions such as hypertension is established. Its known pharmacology is to lower vascular resistance and slow conduction through the atrioventricular (AV) node.

That pharmacology argues against the prediction rather than for it. A bundle branch block is a conduction disorder. Slowing AV nodal conduction is not an obvious treatment for it, and verapamil's labeling lists high-grade AV block as a contraindication or caution. The disease term itself is marked obsolete, so the 99.62% score may reflect how the ontology is structured rather than a real drug-disease relationship.

The prediction has no trials or literature behind it. Mechanistic plausibility is weak, and there is a possible safety conflict.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA213232 | Verapamil Hydrochloride | Injection, solution | Caplin Steriles Limited |
| ANDA206173 | Verapamil Hydrochloride | Tablet | Nivagen Pharmaceuticals, Inc. |
| ANDA206173 | Verapamil Hydrochloride | Tablet | REMEDYREPACK INC. |
| ANDA211370 | Verapamil Hydrochloride | Injection | Armas Pharmaceuticals Inc. |

Other dosage forms on the US market include extended-release tablets, extended-release capsules, delayed-release capsules, and film-coated tablets.

---

## Safety Considerations

- **Conduction concern**: The Evidence Pack's analysis notes that verapamil labeling lists high-grade AV block as a contraindication or caution. This is directly relevant to a conduction-disorder indication.
- **Drug interactions**: No interaction records were found in the query.

Please refer to the package insert for the full set of warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials or literature. The target disease term is obsolete, and verapamil's AV-nodal-slowing effect conflicts with a conduction-disorder indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- A check of what the obsolete disease term maps to in current ontologies, to see whether the score is an artifact
- A documented pathophysiologic rationale and any case-level evidence

**Other predictions in the same pack:** Predictions for malignant hypertensive renal disease and malignant renovascular hypertension are more mechanistically plausible. Both are extensions of verapamil's existing antihypertensive effect, and both are rated "Research Question". Both still lack direct clinical evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Doxercalciferol
parent: Model Prediction Only (L5)
nav_order: 625
evidence_level: L5
indication_count: 1
---

# Doxercalciferol
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

# Doxercalciferol: From Secondary Hyperparathyroidism in CKD to Vitamin D Deficiency

## One-Sentence Summary

Doxercalciferol is a synthetic vitamin D2 analog. Its known labeled use is secondary hyperparathyroidism in chronic kidney disease (CKD), which comes from the pack's rationale text, not from the license data.
The TxGNN model predicts it may be effective for **obsolete vitamin D deficiency** (an outdated ontology label), but currently **0 clinical trials** and **0 publications** support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Secondary hyperparathyroidism in CKD (not listed in the license records provided) |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 (all shown authorizations are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Doxercalciferol is a prodrug of vitamin D2 (ergocalciferol). The liver converts it by 25-hydroxylation into 1α,25-dihydroxyvitamin D2, which activates the vitamin D receptor. Unlike some other vitamin D products, it does not need a second activation step in the kidney. Structured mechanism data is not available in the pack, so this description comes from the pack's rationale text.

A link to vitamin D deficiency is biologically plausible because the drug acts on the vitamin D pathway. This is the likely reason for the very high TxGNN score.

There is a caveat. The predicted disease label is an obsolete ontology term, so the prediction may be a knowledge-graph artifact rather than a truly new indication. The term should be mapped to a current disease concept, such as vitamin D deficiency, and compared with the labeled indication before any further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA210452 | Doxercalciferol | Injection | Dr. Reddy's Laboratories Inc |
| ANDA213717 | Doxercalciferol | Injection, solution | Eugia US LLC |
| ANDA215810 | Doxercalciferol | Injection, solution | Alembic Pharmaceuticals Inc. |
| ANDA211670 | Doxercalciferol | Injection, solution | Meitheal Pharmaceuticals Inc. |
| ANDA205360 | Doxercalciferol | Capsule | Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc. |

These are 5 of 14 authorizations. Both injectable and oral (capsule) forms are marketed. Approved indication text was not included in the license records.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials or publications. The predicted disease is an obsolete label that may overlap with the drug's existing vitamin D pathway use rather than represent a new indication.

**To proceed, the following is needed:**
- Map "obsolete vitamin D deficiency" to a current disease concept and confirm it is distinct from the labeled indication
- Obtain the FDA package insert (approved indications, warnings, contraindications), which blocks safety screening
- Obtain structured mechanism of action data from DrugBank
- Search for clinical trials and literature under the updated disease term
- Assess route compatibility (injectable and oral forms) for the target use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Sotagliflozin
parent: Model Prediction Only (L5)
nav_order: 1177
evidence_level: L5
indication_count: 10
monitor_inn: "SOTAGLIFLOZIN"
predicted_indications: ["opsismodysplasia", "diabetes mellitus (disease)", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "autoimmune oophoritis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Sotagliflozin
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

# Sotagliflozin: From Type 1 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Sotagliflozin is an oral dual SGLT1/SGLT2 inhibitor, originally used to improve blood sugar control in type 1 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia.
**No clinical trials** and **no publications** currently support this prediction, so it rests on the graph-based model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 1 diabetes mellitus (including diabetic ketoacidosis-related conditions) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for sotagliflozin is not available in the data compiled for this report. Its known drug targets are sodium/glucose cotransporter 1 (SGLT1, intestine) and sodium/glucose cotransporter 2 (SGLT2, kidney). Blocking these two transporters delays intestinal glucose absorption and increases urinary glucose excretion, which lowers blood sugar independently of insulin.

Opsismodysplasia is a rare skeletal dysplasia caused by mutations in *INPPL1* (SHIP2 deficiency). We found no plausible mechanistic link between SGLT1/SGLT2 inhibition and this pathway. The two conditions are biologically unrelated: one is a metabolic disease of glucose control, the other a genetic disorder of bone development.

The very high TxGNN score (99.61%) is a graph-based prediction only. It most likely reflects network proximity in the knowledge graph rather than a true biological relationship. Without supporting trials or literature, this prediction should be treated as a computational hypothesis, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA216203 | INPEFA (Lexicon Pharmaceuticals, Inc.) | Tablet | Not listed (status: cancelled) |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature, or mechanistic support (Evidence Level L5). The biology of opsismodysplasia (*INPPL1*/SHIP2 deficiency) has no known connection to SGLT1/SGLT2 inhibition. The only US authorization is also listed as cancelled.

**To proceed, the following is needed:**
- Preclinical evidence, such as cell or animal models, showing that SGLT inhibition affects the SHIP2/INPPL1 pathway or skeletal development
- Detailed mechanism-of-action data for sotagliflozin
- FDA package insert warnings and contraindications, which are currently missing
- Confirmation of the drug's current US marketing and authorization status

**Note on other predictions:** Among the other predictions for this drug, only "diabetes mellitus" (rank 2) has substantial support: multiple completed Phase 3 trials in type 1 and type 2 diabetes. It sits very close to the drug's original indication, so it is better seen as confirmation within that indication than as true repurposing. Its main safety guardrail would be ketone monitoring to reduce the risk of diabetic ketoacidosis in type 1 diabetes. The remaining predictions have no supporting evidence and no plausible mechanistic link.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


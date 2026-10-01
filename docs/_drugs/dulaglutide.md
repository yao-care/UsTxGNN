---
layout: default
title: Dulaglutide
parent: Model Prediction Only (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
---

# Dulaglutide
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

# Dulaglutide: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Dulaglutide is a once-weekly injectable GLP-1 receptor agonist, originally used to treat type 2 diabetes.
The TxGNN model predicts it may be effective for **Opsismodysplasia**, a rare skeletal dysplasia, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction is model-only and is not supported by any biological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the source data lists no approved indication text; this is from general drug knowledge) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 (all under BLA125469) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Dulaglutide is a GLP-1 receptor agonist that enhances glucose-dependent insulin secretion from pancreatic beta cells. Its efficacy in type 2 diabetes is established.

The prediction is **not** mechanistically well supported. Opsismodysplasia is a rare skeletal dysplasia linked to *INPPL1*, and GLP-1 receptor agonism has no established role in chondrocyte or bone-growth pathways. The high score most likely reflects proximity in the knowledge graph, not biology.

The other nine predicted indications share the same weakness:

- **Stiff person syndrome (classic and focal)**, scores 97.05%: autoimmune GABAergic disease. The graph link probably comes from its co-occurrence with type 1 diabetes.
- **Thiamine-responsive dysfunction syndrome**, 96.81%: a link through glucose metabolism is conceivable, but it would not address the transporter defect.
- **Localized lipodystrophies (drug-induced, centrifugal, pressure-induced, idiopathic)**, 94.99%–95.62%: probably artifacts of the association between injectable diabetes drugs and injection-site lipodystrophy. Dulaglutide is itself a subcutaneous injectable.
- **Pancreatic agenesis**, 95.55%: implausible, because the drug needs beta cells to act and they are absent in this condition.
- **Autoimmune oophoritis**, 69.57%: no established immunomodulatory role, and it has the lowest score of the set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The 5 main entries below are among 11 total authorizations. All 11 fall under one biologics license (BLA125469). The source data gives no approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| BLA125469 | Trulicity | Injection, solution | Eli Lilly and Company |
| BLA125469 | TRULICITY | Injection, solution | A-S Medication Solutions |
| BLA125469 | Trulicity | Injection, solution | A-S Medication Solutions |
| BLA125469 | Trulicity | Injection, solution | A-S Medication Solutions |
| BLA125469 | Trulicity | Injection, solution | A-S Medication Solutions |

The drug is available only as an injectable.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interaction records were found in the source data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5): there are no clinical trials or publications, and no plausible mechanistic link between GLP-1 receptor agonism and opsismodysplasia. The high score most likely reflects knowledge-graph adjacency. The other nine predicted indications have the same weakness.

**To proceed, the following is needed:**
- Confirm the original indication and mechanism of action from DrugBank or the package insert
- Package insert warnings and contraindications, which are needed for safety screening
- Preclinical or mechanistic evidence linking GLP-1 receptor signaling to *INPPL1*-related skeletal biology
- Any registered trials or case reports; none exist at present

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


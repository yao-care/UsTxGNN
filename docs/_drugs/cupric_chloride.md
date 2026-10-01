---
layout: default
title: Cupric Chloride
parent: Model Prediction Only (L5)
nav_order: 552
evidence_level: L5
indication_count: 3
---

# Cupric Chloride
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

# Cupric Chloride: From Copper Supplementation to Primary Release Disorder of Platelets

## One-Sentence Summary

Cupric chloride is an injectable copper source, a trace-element supplement marketed in the US.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone, and the mechanistic link is speculative.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cupric chloride is a source of copper, an essential trace element used as a cofactor supplement. Copper is a cofactor for enzymes such as lysyl oxidase, so copper-dependent processes could in theory affect platelet function.

No direct mechanistic or clinical link to platelet granule release defects is established in the available data. The high graph score most likely reflects network proximity through generic metal or hemostasis nodes, not a specific pharmacological rationale.

TxGNN also predicted two other platelet-related conditions, and neither has any supporting evidence:
- **Pseudo-von Willebrand disease** (score 99.25%): this is a genetic gain-of-function defect in the platelet receptor GP1BA. Copper supplementation has no plausible action on it, so it is likely a graph artifact.
- **Thrombocytopenia due to immune destruction** (score 99.02%): copper deficiency can cause low blood counts, mainly anemia and neutropenia, and occasionally low platelets. Correcting a deficiency is not the same as treating autoimmune platelet destruction (such as ITP), and there is no evidence that copper modulates that process.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA216113 | Cupric Chloride (Somerset Therapeutics) | Injection |
| ANDA212071 | Cupric Chloride (Exela Pharma Sciences) | Injection, solution |
| ANDA217626 | Cupric Chloride (Archis Pharma) | Injection, solution |
| ANDA217287 | Cupric Chloride (Amneal Pharmaceuticals) | Injection, solution |
| NDA018960 | Copper (Hospira) | Injection, solution |

The record reports 6 authorizations in total; 5 are listed above. All are injectable products.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it and no established mechanism. The high score looks like a graph artifact rather than a pharmacological signal. The pseudo-von Willebrand disease link is especially implausible because it is a genetic receptor defect.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block any safety screening
- Mechanism of action data, for example from the DrugBank API
- Original approved indication text, which is empty in the current US license records
- A literature search on copper and platelet function or platelet disorders
- A clear mechanistic hypothesis for at least one predicted indication, such as platelet abnormalities linked to copper deficiency, before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


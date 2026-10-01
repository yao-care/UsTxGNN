---
layout: default
title: Pioglitazone
parent: Model Prediction Only (L5)
nav_order: 1047
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Pioglitazone: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is an oral insulin-sensitizing drug (a PPAR-gamma agonist) marketed in the US and widely used for type 2 diabetes. The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia. This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes (general drug knowledge; the US license records in the pack contain no indication text) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed are ANDA generic approvals) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Pioglitazone is known to act through PPAR-gamma, improving insulin sensitivity. Its efficacy in type 2 diabetes is well established.

The link to the predicted indication is weak. Opsismodysplasia is a rare skeletal dysplasia (INPPL1-related). PPAR-gamma insulin sensitization has no known bearing on its pathophysiology. The high score most likely reflects proximity in the knowledge graph, not biological evidence, and no clinical or literature support was found. This prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA200268 | Pioglitazone Hydrochloride (A-S Medication Solutions) | Tablet | Not listed in the record |
| ANDA207806 | Pioglitazone (Solco Healthcare LLC) | Tablet | Not listed in the record |
| ANDA200268 | Pioglitazone (Proficient Rx LP) | Tablet | Not listed in the record |
| ANDA200268 | Pioglitazone (Rising Pharma Holdings, Inc.) | Tablet | Not listed in the record |
| ANDA200268 | Pioglitazone (NuCare Pharmaceuticals, Inc.) | Tablet | Not listed in the record |

Only the oral tablet form is recorded.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the mechanistic link to opsismodysplasia is not credible. Package insert safety information is also still missing.

**To proceed, the following is needed:**
- Any disease-specific preclinical evidence (for example, models of INPPL1-related skeletal dysplasia) showing a plausible role for PPAR-gamma modulation
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications
- Consideration of the other ranked predictions. Only pancreatic agenesis (rank 9) has retrieved literature, and that is indirect (L4) and covers type 2 diabetes, not the predicted disease. Its mechanistic fit is also poor.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


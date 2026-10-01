---
layout: default
title: Lebrikizumab
parent: Model Prediction Only (L5)
nav_order: 841
evidence_level: L5
indication_count: 10
---

# Lebrikizumab
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

# Lebrikizumab: From Atopic Dermatitis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Lebrikizumab is an anti-IL-13 monoclonal antibody marketed in the US as EBGLYSS, used for moderate-to-severe atopic dermatitis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe atopic dermatitis (the license records have no indication text, so this comes from the pack's mechanistic notes) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 97.94% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 records (both BLA761306) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank field. Lebrikizumab is a high-affinity antibody that binds IL-13. It blocks IL-4Rα/IL-13Rα1 heterodimer signaling, a core pathway in type 2 inflammation.

This link is weak. Diabetic retinopathy is driven mainly by VEGF, hyperglycemia-induced vascular injury, and inflammation. IL-13 is not a recognized driver, and no known mechanism connects IL-13 blockade to retinal microvascular disease. The high TxGNN score reflects a graph-based association only.

Two further points limit the prediction:
- **Route:** Lebrikizumab is a subcutaneous injection. Route compatibility with a retinal indication has not been assessed.
- **Same-disease prediction:** The plain "diabetic retinopathy" prediction (rank 3) has no trials or publications either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761306 | EBGLYSS (Eli Lilly and Company) | Injection, solution | Not listed in the record |

The record appears twice with identical content.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Other Predicted Indications (for context)

| Predicted Indication | Evidence Level | Decision | Note |
|------|------|------|------|
| Dermatitis | L1 | Proceed with Guardrails | Label confirmation, not new repurposing. Phase 3 RCTs (ADvocate1/2, ADhere) and long-term data exist for atopic dermatitis only. Do not extend to other dermatitis subtypes without separate evidence. |
| Psoriasis | L4 | Hold | Retrieved trials and papers concern atopic dermatitis, matched by keyword only. A 2026 case report describes lebrikizumab-induced psoriasis. |
| Drug-induced osteoporosis, HER2-positive breast carcinoma, and 5 others | L5 | Hold | Graph prediction only, no supporting studies. |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, severe nonproliferative diabetic retinopathy, has only a model score. It has no trials, no literature, and no plausible IL-13 mechanism. Diabetic retinopathy is a VEGF- and vascular-driven disease.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence linking IL-13 signaling to diabetic retinopathy
- Detailed mechanism of action data from DrugBank
- Package insert warnings and contraindications (blocking data gap DG001)
- Route and ocular safety assessment for a retinal indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


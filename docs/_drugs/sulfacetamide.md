---
layout: default
title: Sulfacetamide
parent: 僅模型預測 (L5)
nav_order: 1185
evidence_level: L5
indication_count: 10
---

# Sulfacetamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sulfacetamide: From Antibacterial Use to Postinfectious Vasculitis

## One-Sentence Summary

> Sulfacetamide is a sulfonamide-class antibacterial (folate-synthesis inhibitor); no approved indication record is currently on file for this product.
> The TxGNN model predicts it may be effective for **Postinfectious Vasculitis**,
> but currently **0 clinical trials** and **0 publications** support this specific direction — the prediction is model-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (drug currently not marketed; no approved-indication text available in regulatory data) |
| Predicted New Indication | Postinfectious Vasculitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for sulfacetamide is not available in the evidence pack (flagged as a High-severity data gap). Based on known pharmacology, sulfacetamide is a sulfonamide antibacterial that competitively inhibits para-aminobenzoic acid (PABA), blocking bacterial folate synthesis — a mechanism historically applied to topical/ophthalmic and dermatologic bacterial infections.

Postinfectious vasculitis, however, is an immune-complex-mediated inflammatory disease, not a bacterial infection per se. Per the evidence pack's own rationale, sulfacetamide's antibacterial mechanism has **no direct pathophysiological connection** to vasculitic immune-complex disease — this ranking is driven purely by knowledge-graph embedding similarity, with no supporting clinical trial or literature evidence identified.

Given the absence of any real-world evidence and a mechanistically weak rationale, this specific candidate should be treated as a hypothesis-generating signal only, not a basis for clinical consideration at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are marked as a Blocking data gap — this prevents the candidate from entering the safety pre-screen (S1) stage until the label is retrieved and parsed.)*

---

## Other Predicted Indications Worth Noting

The top-ranked prediction by TxGNN score has the weakest evidentiary support in this evidence pack. Among the 10 candidates evaluated, **otitis externa** (rank 3) stands out with substantially stronger real-world evidence and a coherent mechanistic rationale (sulfacetamide is a known historical component of trimethoprim-sulfacetamide-polymyxin B ear drops):

| Rank | Disease | Evidence Level | Trials | Literature | Recommendation |
|------|---------|----------------|--------|------------|-----------------|
| 1 | Postinfectious vasculitis | L5 | 0 | 0 | Hold |
| 3 | **Otitis externa** | **L2** | 0 | 4 (incl. 2 RCTs) | **Proceed with Guardrails** |
| 10 | Parasitic eyelid infestation | L4 | 0 | 1 | Research Question |

If the goal is to identify the most defensible repurposing candidate for sulfacetamide rather than strictly the top TxGNN-ranked disease, otitis externa merits priority follow-up over postinfectious vasculitis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (postinfectious vasculitis) is supported only by TxGNN embedding similarity (L5) with zero clinical trials or literature, and the mechanistic link is explicitly assessed as weak/absent in the evidence pack itself. Additionally, a Blocking data gap (missing TFDA label warnings/contraindications) prevents even a preliminary safety screen.

**To proceed, the following is needed:**
- Retrieve and parse TFDA label (warnings/contraindications) — currently Blocking (DG001)
- Obtain confirmed mechanism-of-action data via DrugBank API (DG002)
- If pursuing repurposing for sulfacetamide, redirect evaluation toward **otitis externa** (rank 3), which has an L2 evidence base including two RCTs on trimethoprim-sulfacetamide-polymyxin B ear drops
- If postinfectious vasculitis is still of interest, commission a targeted literature/mechanism review before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Activated Charcoal Arsenic Triiodide Arsenic Triox
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Arsenic Triiodide Arsenic Triox
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Multi-Component Compound Mixture (Arsenic Trioxide et al.): Insufficient Evidence for Repurposing Evaluation

## One-Sentence Summary

This candidate is a 12-component compound mixture — including arsenic compounds (arsenic trioxide, arsenic triiodide), a heavy metal element (gold), egg phospholipids, and eight botanical extracts — consistent with a homeopathic or traditional medicine formulation rather than a defined single-entity pharmaceutical.
The TxGNN model generated **no repurposing predictions** for this compound, and the product holds **zero US or Taiwan market authorizations**.
With no original indication on record, no predicted indication, and all safety data absent, a meaningful drug repurposing evaluation is not currently feasible.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None identified by TxGNN |
| TxGNN Prediction Score | Not available |
| Evidence Level | Below L5 — no predictions generated |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Compound Profile and Evaluation Context

This candidate comprises the following 12 declared ingredients:

| # | Ingredient | Category |
|---|-----------|---------|
| 1 | Activated Charcoal | Adsorbent / Detoxifying agent |
| 2 | Arsenic Triiodide | Inorganic arsenic salt |
| 3 | Arsenic Trioxide | Inorganic arsenic compound (known antineoplastic at therapeutic doses) |
| 4 | Artemisia Vulgaris Root | Botanical (mugwort) |
| 5 | Chionanthus Virginicus Bark | Botanical (fringe tree) |
| 6 | Corallium Rubrum Exoskeleton | Marine-origin material (red coral) |
| 7 | Egg Phospholipids | Lipid excipient / nutritional component |
| 8 | Gold | Heavy metal element |
| 9 | Morella Cerifera Root Bark | Botanical (bayberry) |
| 10 | Ornithogalum Umbellatum | Botanical (star of Bethlehem) |
| 11 | Petroselinum Crispum | Botanical (parsley) |
| 12 | Sanguinaria Canadensis Root | Botanical (bloodroot) |

This ingredient profile is characteristic of a **homeopathic or complex traditional medicine preparation**. TxGNN is designed to evaluate single-entity drugs or defined molecular entities mapped through DrugBank. Because this product has **no DrugBank ID**, could not be mapped to the knowledge graph, and contains multiple pharmacologically unrelated substances, the model returned no predictions. This is an expected and appropriate null result for a product of this nature, not a data pipeline failure.

There is no established single mechanism of action, no standard indication, and no regulatory approval pathway that applies to this compound as a whole.

---

## Cytotoxicity Note

> **Applicable due to the presence of Arsenic Trioxide**, which at therapeutic concentrations is a recognized cytotoxic antineoplastic agent (approved for acute promyelocytic leukemia, APL).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Mixed: contains one conventional cytotoxic component (arsenic trioxide); remaining ingredients are not classified as cytotoxic |
| Myelosuppression Risk | Cannot be determined for the compound as a whole; arsenic trioxide monotherapy carries moderate myelosuppression risk |
| Emetogenicity Classification | Cannot be determined for the compound as a whole |
| Monitoring Items | If arsenic-containing, monitoring of QTc interval, hepatic and renal function, electrolytes (potassium, magnesium), and complete blood count would be standard for the arsenic component |
| Handling Protection | Arsenic compounds require cytotoxic handling precautions; the combined formulation should be treated with equivalent caution until classified otherwise |

---

## Safety Considerations

Safety data for this compound as a whole is not available. The absence of any market authorization means no approved package insert or formal safety labeling exists for review.

Given the presence of **arsenic-containing ingredients**, the following general cautions are recognized in the medical literature:
- Arsenic trioxide is associated with **QT prolongation and risk of fatal arrhythmia**
- Hepatotoxicity and peripheral neuropathy have been reported with arsenic compounds
- Sanguinaria canadensis (bloodroot) contains sanguinarine, which carries mucosal toxicity risk

Formal safety profiling via DrugBank API, TFDA package insert review, and DDI screening should be completed before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is a multi-component mixture for which TxGNN cannot generate meaningful repurposing predictions due to the absence of a DrugBank ID, no approved indication, and no mechanism-of-action data. The compound's heterogeneous ingredients — ranging from arsenic compounds to botanical extracts — make it structurally incompatible with the current single-entity repurposing pipeline.

**To proceed, the following is needed:**

- **Clarify the product identity**: Determine whether this is a registered homeopathic product, a compounded preparation, or an experimental formulation; obtain a precise formulation with concentrations for each ingredient
- **Decompose into individual components**: If repurposing research is the goal, evaluate arsenic trioxide separately (DrugBank: DB01169) as it has an established indication and active clinical trial record (APL and potentially other hematologic malignancies)
- **Obtain DrugBank mapping**: At minimum for arsenic trioxide and sanguinaria canadensis, which have the highest pharmacological activity
- **Safety baseline**: Complete TFDA package insert review (if any component is registered), toxicology literature review for arsenic compounds, and full DDI screening for each active ingredient individually
- **Regulatory classification**: Determine whether this compound is classified as a homeopathic medicine, traditional medicine, or compounded drug in the target jurisdiction — this determines which evidence standards apply
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


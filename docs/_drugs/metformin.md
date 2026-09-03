---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 905
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Metformin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

> Metformin is a well-established first-line therapy for type 2 diabetes mellitus, though this specific evidence pack does not contain sourced regulatory or mechanism-of-action data confirming that.
> The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**,
> but currently **0 clinical trials** and **0 publications** support this direction — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` and `original_moa` are both data gaps). Metformin is widely known as a first-line type 2 diabetes therapy, but this is general background knowledge, not sourced from the pack. |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed (0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` is a data gap). Based on general knowledge, metformin activates AMPK and suppresses hepatic gluconeogenesis, a pathway well established for glycemic control — this is consistent with the mechanistic notes recorded against each predicted indication in this pack, even though the formal MOA field was not populated.

The predicted indication, Classic Stiff Person Syndrome, is an autoimmune neurological disorder driven by anti-GAD65 antibodies that disrupt GABAergic neurotransmission. The evidence pack's own rationale is explicit that **no known biological mechanism connects metformin's AMPK/insulin-sensitizing pathway to this autoimmune/GABAergic pathology**. It further flags that the near-identical top score for "focal stiff limb syndrome" (a regional variant of the same disease spectrum) suggests TxGNN may be clustering these diseases together via shared diabetes-comorbidity nodes in the knowledge graph, rather than detecting a genuine pharmacological relationship.

In short, this is a high-confidence *model* prediction with no corroborating mechanistic, clinical, or literature evidence identified so far. It should be treated as a hypothesis-generating signal rather than a mechanistically grounded lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Metformin currently has **no market authorizations on file** in this evidence pack (market status: Not Marketed, 0 licenses). No product/dosage-form data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields in this evidence pack — key warnings, contraindications, and drug-drug interactions — are recorded as data gaps or "not found.")*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by an L5-level TxGNN model score, with zero clinical trials, zero literature, and the evidence pack's own analysis noting no identifiable mechanistic link to the autoimmune/GABAergic pathology of stiff person syndrome. Combined with the absence of regulatory or safety data for this jurisdiction, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for metformin (currently a data gap)
- Preclinical or mechanistic studies exploring any link between AMPK/insulin-sensitizing pathways and anti-GAD65/GABAergic neurotransmission
- TFDA-equivalent label data (warnings, contraindications) — currently blocking per `DG001`
- Any real-world or case-level evidence (even off-label reports) for metformin use in stiff person syndrome spectrum disorders
- Regulatory pathway assessment, since the drug is currently not marketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


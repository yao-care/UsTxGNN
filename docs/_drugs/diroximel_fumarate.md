---
layout: default
title: Diroximel Fumarate
parent: 僅模型預測 (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
---

# Diroximel Fumarate
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

# Diroximel Fumarate: From Unspecified Original Indication to Diabetic Cataract (Predicted)

## One-Sentence Summary

> Diroximel fumarate (DrugBank ID: DB14783) is a monomethyl fumarate prodrug; however, its originally approved indication is not documented in this evidence pack.
> The TxGNN model predicts it may be effective for **Diabetic Cataract**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only hypothesis with no direct evidentiary backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.9993% (KG rank #58) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for diroximel fumarate is not available in the evidence pack (flagged as a High-severity data gap). Based on the information available in the TxGNN model's own rationale, diroximel fumarate is a **monomethyl fumarate prodrug** that is understood to activate the **Nrf2/ARE (nuclear factor erythroid 2–related factor 2 / antioxidant response element) pathway**, an antioxidant and anti-inflammatory signaling cascade.

The proposed mechanistic link to diabetic cataract is that cataract formation in diabetic patients involves lens oxidative stress and polyol-pathway metabolite accumulation, both of which are theoretically modulated by Nrf2 pathway activation. However, this is a **plausibility argument derived from pathway biology, not an established pharmacological relationship** — no preclinical or clinical data connect diroximel fumarate to any ocular or lens-related indication.

It is also notable that several other top-ranked predictions for this drug (e.g., tetanic cataract, craniostenosis cataract) have documented mechanistic implausibility per the model's own rationale, suggesting the knowledge-graph may be clustering diverse cataract subtypes together as a node-similarity artifact rather than identifying a genuine pharmacological signal. This raises caution about over-interpreting the "diabetic cataract" ranking as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Diroximel fumarate is **not currently marketed** in this jurisdiction — no NDA/BLA license records are available (total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: TFDA/FDA label warnings and contraindications, as well as drug–drug interaction data, could not be retrieved for this drug (query status: not found). This is flagged internally as a **Blocking** data gap — safety-related decisions cannot proceed until label data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN model scoring (L5, evidence level with no clinical trials or literature), and the mechanistic rationale is speculative pathway-level reasoning rather than direct evidence. Combined with the absence of confirmed original indication, mechanism of action, and safety/label data, this candidate is not ready to advance beyond the model-prediction stage.

**To proceed, the following is needed:**
- Confirmed original indication and regulatory history for diroximel fumarate (currently missing from this evidence pack)
- Verified mechanism of action from DrugBank or primary literature (currently a data gap)
- TFDA/FDA label data — warnings, contraindications, and drug interaction profile (currently a **Blocking** data gap preventing safety pre-assessment)
- Preclinical or clinical evidence specifically evaluating fumarate-class compounds in diabetic cataract or related ocular conditions
- Clarification on whether the cluster of similarly-ranked cataract subtypes (tetanic, craniostenosis, nuclear senile, cortical, etc.) reflects a genuine signal or a knowledge-graph artifact, before committing further evaluation resources to this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


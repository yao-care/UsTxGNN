---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 1047
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pioglitazone: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

> Pioglitazone is a thiazolidinedione (PPAR-γ agonist) insulin sensitizer, historically used in the management of type 2 diabetes mellitus.
> The TxGNN model's top-ranked prediction suggests possible relevance to **Opsismodysplasia**, a rare skeletal dysplasia,
> but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags no known biological mechanism connecting the two.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from supporting literature in this evidence pack; no formal regulatory license record available — see below) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for pioglitazone is not available in this evidence pack. Based on the supporting literature that is present, pioglitazone belongs to the thiazolidinedione (TZD) class of PPAR-γ agonists, functioning as an insulin sensitizer with established efficacy in type 2 diabetes and documented effects on adipocyte differentiation and fat redistribution.

For the top-ranked candidate, **opsismodysplasia**, the model's own rationale is explicit that there is **no known mechanistic link**: this is a rare skeletal dysplasia caused by *INPPL1* (SHIP2-related) gene mutations, and it has no established connection to the PPAR-γ pathway. The rationale text attributes the high TxGNN score to knowledge-graph embedding similarity rather than biological plausibility.

Notably, several **lower-ranked** candidates in this evidence pack (e.g., drug-induced localized lipodystrophy, centrifugal lipodystrophy, idiopathic localized lipodystrophy) have a more coherent mechanistic story — PPAR-γ's known role in adipocyte differentiation and fat distribution — but these also currently lack clinical trial or literature evidence. Given this, the top-ranked prediction (opsismodysplasia) should be treated as a low-confidence, mechanism-agnostic signal rather than a biologically grounded repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: 9 general pharmacology/clinical review papers on pioglitazone and TZDs in type 2 diabetes were retrieved under a different candidate indication — pancreatic agenesis — but none address opsismodysplasia specifically.)*

---

## US Market Information

Pioglitazone is currently **not marketed** under this jurisdiction's regulatory database, with 0 registered license records. No product/dosage-form information is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (opsismodysplasia) has no supporting clinical trials or literature, and the model's own mechanistic rationale finds no biological link between pioglitazone's PPAR-γ agonism and this disease's INPPL1-driven pathology — the score is most likely a knowledge-graph artifact rather than a genuine signal.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: obtain FDA/TFDA label warnings and contraindications before any S1 safety review can proceed
- Resolve **DG002 (High)**: obtain confirmed mechanism-of-action data via DrugBank to properly assess mechanistic relevance
- If pursuing repurposing further, consider redirecting evaluation toward candidates with clearer mechanistic rationale in this same evidence pack — particularly the lipodystrophy-related indications (ranks 5–8), where PPAR-γ's role in adipocyte biology offers a plausible rationale, even though clinical/literature evidence is currently absent for those as well
- If opsismodysplasia is to be pursued regardless, a dedicated preclinical/mechanistic study would be required to establish biological plausibility before any clinical evidence-gathering is justified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


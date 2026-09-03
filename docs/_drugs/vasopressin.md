---
layout: default
title: Vasopressin
parent: 僅模型預測 (L5)
nav_order: 1285
evidence_level: L5
indication_count: 2
---

# Vasopressin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Vasopressin: From Unrecorded Original Indication to Congenital Prothrombin Deficiency

## One-Sentence Summary

> Vasopressin (DrugBank ID DB00067) has no recorded original indication or mechanism-of-action data in this evidence pack, and it currently holds no marketing authorization in Taiwan (未上市).
> The TxGNN model predicts potential efficacy for **Congenital Prothrombin Deficiency**, but this is supported only by **0 clinical trials** and **3 indirectly related publications** (case reports/review) —
> and the repurposing rationale itself flags a likely drug/disease entity-confusion issue that significantly weakens the credibility of this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indication recorded in this evidence pack |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for vasopressin is not available in this evidence pack (`original_moa: [Data Gap]`). Without an established MOA, it is not possible to build a direct mechanistic link between vasopressin and congenital prothrombin (Factor II) deficiency.

More importantly, the repurposing rationale supplied with this candidate flags a critical concern: the cited literature actually discusses **desmopressin (DDAVP)** — a selective V2-receptor analog of vasopressin — which promotes release of von Willebrand factor (vWF) and Factor VIII, not vasopressin itself. In addition, the disease context in the literature (Factor V/VIII deficiency, acquired hemophilia A) differs from the predicted target (congenital prothrombin/Factor II deficiency), which sits further downstream in the common coagulation pathway and has no established relationship to vWF/FVIII release mechanisms.

This double mismatch — drug (vasopressin vs. desmopressin) and disease (FV/FVIII deficiency vs. prothrombin deficiency) — suggests the high TxGNN score may reflect a knowledge-graph node confusion between vasopressin and desmopressin rather than a genuine pharmacological signal. This substantially weakens the case for treating this as a credible mechanistic hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Reviews acquired hemophilia A (autoantibodies against Factor VIII); does not discuss vasopressin or prothrombin deficiency directly |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | Rinsho Ketsueki (Jpn J Clin Hematol) | DDAVP administration in a patient with congenital combined Factor V and Factor VIII deficiency |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | Rinsho Ketsueki (Jpn J Clin Hematol) | Cesarean section managed with Factor VIII concentrate replacement in a pregnant patient with combined FV/FVIII deficiency |

**Note:** None of the above literature discusses vasopressin (as opposed to desmopressin) or congenital prothrombin (Factor II) deficiency specifically; relevance to this candidate is indirect at best.

---

## US Market Information

This drug currently holds no marketing authorization in Taiwan (市場狀態：未上市). No license records are available in this evidence pack (`total_licenses: 0`).

---

## Additional Predicted Indication (Not Prioritized)

The evidence pack also includes a second, lower-ranked candidate: **drug-induced osteoporosis** (TxGNN score 99.62%, Evidence Level **L5**, recommendation **Hold**). This candidate has **no supporting clinical trials or literature** and no known mechanistic pathway linking vasopressin's known receptor activity (V1a/V1b/V2) to bone metabolism. It is a model-prediction-only hypothesis and requires independent mechanistic validation before any further evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and drug interaction data are marked as a Blocking data gap in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence base for the top prediction (congenital prothrombin deficiency) is weak — Evidence Level L4, zero clinical trials, and only 3 indirectly relevant case reports/review articles.
- The repurposing rationale itself identifies a likely drug-entity confusion (vasopressin vs. desmopressin) and disease-target mismatch (Factor V/VIII deficiency vs. prothrombin deficiency), undermining mechanistic plausibility.
- A Blocking data gap (TFDA label warnings/contraindications, DG001) prevents this candidate from entering safety pre-assessment (S1).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/original market label warnings and contraindications before any S1 safety pre-assessment
- Resolve DG002: retrieve vasopressin MOA via DrugBank API to enable a legitimate mechanistic assessment
- Clarify whether the TxGNN prediction stems from a vasopressin/desmopressin node confusion in the knowledge graph; consider re-running the prediction with disambiguated drug entities
- Conduct an independent literature review specific to vasopressin (not desmopressin) in coagulation disorders
- If pursuing the prothrombin deficiency indication, obtain mechanistic studies specifically linking vasopressin (not its analogs) to Factor II regulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Miglitol
parent: 僅模型預測 (L5)
nav_order: 928
evidence_level: L5
indication_count: 10
---

# Miglitol
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

# Miglitol: From Type 2 Diabetes Mellitus to Type 1 Diabetes Mellitus (Insulin Adjunct)

> **Note on candidate selection**: This evidence pack lists 10 TxGNN-predicted indications for miglitol. The top 9 (by raw TxGNN score, e.g. *focal stiff limb syndrome*, *classic stiff person syndrome*) have **zero clinical trial or literature support** and are flagged by the model's own rationale as likely knowledge-graph artifacts (indirect paths through diabetes-comorbidity nodes, not direct pharmacology). Only **Type 1 Diabetes Mellitus** (rank 10) has real supporting evidence and a non-Hold recommendation. This report focuses on that candidate as the only actionable one in the pack.

## One-Sentence Summary

Miglitol is an alpha-glucosidase inhibitor originally used to control postprandial hyperglycemia in type 2 diabetes. The TxGNN model — and a body of older clinical literature — suggests it may also be useful as an **adjunct to insulin therapy in Type 1 Diabetes Mellitus**, with **7 clinical trials** (1 directly relevant, Phase 3) and **16 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (postprandial glycemic control) — general pharmacological knowledge; no Taiwan/US regulatory license data available |
| Predicted New Indication | Type 1 Diabetes Mellitus (adjunct to insulin) |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L2 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Miglitol is an alpha-glucosidase inhibitor: it delays intestinal breakdown and absorption of complex carbohydrates, blunting the postprandial blood glucose spike. This mechanism does not depend on residual insulin secretion, which is why it is pharmacologically plausible in Type 1 Diabetes Mellitus (T1DM) as well as Type 2.

In T1DM, exogenous insulin dosing often fails to fully control the sharp postprandial glucose rise, even with intensive insulin therapy. Adding an alpha-glucosidase inhibitor like miglitol slows carbohydrate absorption, flattening this peak and — in several of the studies below — reducing the insulin dose needed around meals and the associated risk of post-meal hypoglycemia from over-correction.

This is not a novel mechanistic hypothesis: the same drug class (miglitol, and its research-era compounds BAY-m-1099/BAY-o-1248) has been studied as an insulin adjunct in insulin-dependent diabetes since the late 1980s, well before TxGNN's prediction. The model's high score here reflects a real, previously documented off-label pattern rather than a purely novel signal — unlike the other 9 predictions in this pack, which the model's own rationale identifies as indirect knowledge-graph paths with no supporting pharmacology.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00213109](https://clinicaltrials.gov/study/NCT00213109) | Phase 3 | Completed | N/A | Open-label trial evaluating efficacy and safety of miglitol in insulin-treated Type 1 Diabetes patients. Directly relevant, but open-label (non-placebo-controlled), which limits evidence strength. |

Six additional trials were returned by the search (NCT02475499, NCT02476760, NCT02456428, NCT06449235, NCT03492580, NCT01697592) but were assessed as **not relevant** — they study incretin-based drugs, canagliflozin, or omarigliptin in Type 2 diabetes, not miglitol in T1DM, and are excluded from this table.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21869539](https://pubmed.ncbi.nlm.nih.gov/21869539/) | 2011 | Cohort | Endocrine Journal | Miglitol 25→50mg TID added to intensive insulin therapy in 11 T1DM patients; assessed effect on insulin dose, weight, hypoglycemia, and incretin response. |
| [24843410](https://pubmed.ncbi.nlm.nih.gov/24843410/) | 2010 | Cohort/Combination therapy | J Diabetes Investigation | Combination of miglitol + insulin in T1DM; addresses uncontrolled postprandial glucose rise despite intensive insulin therapy. |
| [2180090](https://pubmed.ncbi.nlm.nih.gov/2180090/) | 1990 | Clinical study (placebo-controlled) | S Afr Med J | 50mg miglitol vs placebo in 11 insulin-dependent diabetics; significantly lowered post-meal glucose increments (p<0.001). |
| [2663321](https://pubmed.ncbi.nlm.nih.gov/2663321/) | 1989 | Clinical study (single-blind, placebo) | Diabetes Research | Miglitol (BAY-m-1099) vs placebo in 13 insulin-dependent diabetics; significantly reduced postprandial glucose AUC (p<0.01). |
| [3311550](https://pubmed.ncbi.nlm.nih.gov/3311550/) | 1987 | Clinical study | Clin Pharmacol Ther | Miglitol (BAY-m-1099) reduced meal-time insulin requirements in IDDM patients. |
| [2060451](https://pubmed.ncbi.nlm.nih.gov/2060451/) | 1991 | Crossover study | Diabetes Care | Alpha-glucosidase inhibition (miglitol) evaluated as adjunct to insulin, including timing of insulin administration relative to meals. |
| [3130257](https://pubmed.ncbi.nlm.nih.gov/3130257/) | 1988 | Clinical study | Eur J Clin Invest | Two alpha-glucosidase inhibitors (including miglitol precursor BAYm1099) evaluated for glycemic control and insulin requirements in IDDM. |
| [3277827](https://pubmed.ncbi.nlm.nih.gov/3277827/) | 1988 | Clinical study | Diabetes Res Clin Pract | Two alpha-glucosidase inhibitors (including BAY m 1099/miglitol) improved postprandial metabolic control in insulin-dependent diabetics. |
| [3520133](https://pubmed.ncbi.nlm.nih.gov/3520133/) | 1986 | Clinical study | Klinische Wochenschrift | BAYo1248 and BAYm1099 (miglitol) significantly improved postprandial glucose tolerance and reduced insulin requirements vs placebo. |
| [3286168](https://pubmed.ncbi.nlm.nih.gov/3286168/) | 1988 | Clinical study | Diabetes Res Clin Pract | Evaluated timing of preprandial insulin combined with alpha-glucosidase inhibition (BAY-m-1099/miglitol) in IDDM. |

Six further publications (PMID 8261749, 11460577, 12073790, 33268615, 20307399, 3653827) were returned but were either general reviews not specific to miglitol, studies of unrelated drugs (e.g. SGLT2 inhibitors), or lacked usable abstract content — excluded from the table above.

---

## US Market Information

Miglitol currently has **no marketing license on record** for this jurisdiction (market status: 未上市 / Not Marketed, 0 NDAs). No product/dosage form data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism (delayed carbohydrate absorption, insulin-independent) is directly applicable to T1DM, and this use is backed by one completed Phase 3 open-label trial plus ~10 supportive clinical studies spanning 1986–2011 — sufficient for L2 evidence. However, most of the supportive literature is decades old, uses miglitol's pre-approval code name (BAY-m-1099), and no contemporary placebo-controlled RCT or formal safety/MOA documentation is available.

**To proceed, the following is needed:**
- TFDA/FDA package insert data — key warnings, contraindications, and DDI profile (currently a blocking data gap)
- Formal, current mechanism-of-action documentation from DrugBank or equivalent
- A contemporary placebo-controlled RCT of miglitol as insulin adjunct in T1DM, given the existing evidence base predates modern insulin therapy standards
- Clarification of regulatory pathway, since miglitol currently has no license status in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


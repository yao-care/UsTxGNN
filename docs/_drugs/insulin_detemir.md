---
layout: default
title: Insulin Detemir
parent: 僅模型預測 (L5)
nav_order: 798
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin Detemir: From Diabetes Mellitus (Insulin-Dependent) to Type 1 Diabetes Mellitus

## One-Sentence Summary

> Insulin detemir is a long-acting basal insulin analog used for insulin replacement therapy in diabetes mellitus. The TxGNN model's top-ranked prediction is **Type 1 Diabetes Mellitus**, supported by **50 clinical trials** and **19 publications** — but this is not a novel repurposing signal: the evidence itself shows type 1 diabetes is insulin detemir's **already-established, on-label use**, not a new indication. This candidate should be treated as a data-quality/model-artifact case rather than a genuine repurposing opportunity, and the remaining nine TxGNN candidates (ranks 2–10) are mechanistically weak or unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this dataset (data gap) — insulin detemir is a long-acting basal insulin analog for diabetes mellitus (type 1 and type 2) |
| Predicted New Indication | Type 1 Diabetes Mellitus *(flagged as the drug's original indication, not a true new use — see caveat below)* |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## ⚠ Important Caveat on This Prediction

The evidence pack's own rationale for the top-ranked prediction explicitly states this is **not a genuine repurposing candidate**:

> "此為 insulin detemir（長效基礎胰島素類似物）之原始核准適應症，非真正意義上的老藥新用" — *This is insulin detemir's original approved indication, not true drug repurposing.*

Type 1 diabetes is the condition insulin detemir was developed and approved to treat. The TxGNN model surfaced it as a top prediction because the drug-disease relationship is strongly embedded in the knowledge graph — not because it represents a new therapeutic opportunity. The large clinical trial and literature base below confirms an **established use**, not an emerging hypothesis.

Of the other nine TxGNN candidates in this evidence pack, none has clinical trial or literature support: eight are rated L5 (model prediction only, recommendation "Hold"), two of those (drug-induced localized lipodystrophy, pressure-induced localized lipoatrophy) are flagged in the rationale as likely **reversed-direction artifacts** (insulin injection is a known *cause* of these conditions, not a treatment), and two rare-disease candidates (thiamine-responsive dysfunction syndrome, pancreatic agenesis) are L4 mechanistic extensions with no dedicated studies.

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data (`original_moa`) is marked as a data gap in this dataset. However, the evidence pack's rationale field describes the mechanism: insulin detemir binds the insulin receptor, and its myristic acid (C14 fatty acid) side chain allows reversible albumin binding, which slows subcutaneous absorption and produces a stable, prolonged basal insulin effect. This provides steady basal glucose control that directly substitutes for the absolute insulin deficiency characteristic of type 1 diabetes.

Because type 1 diabetes is the pathology insulin detemir was designed to treat, the "predicted new indication" and the drug's original indication are the same condition. The reasoning that would normally justify a repurposing hypothesis (shared pathway, adjacent disease biology) does not apply here — there is no repurposing logic to evaluate, only confirmation of on-label mechanism-of-action fit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Randomized, multinational crossover trial comparing hypoglycemia frequency: insulin detemir + aspart vs. NPH + aspart in basal-bolus T1D regimens |
| [NCT00184665](https://clinicaltrials.gov/study/NCT00184665) | Phase 3 | Completed | 501 | 2-year efficacy/safety comparison of detemir vs. NPH insulin in T1D (HbA1c, hypoglycemia, antibodies) |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | Completed | 752 | 6-month multicenter comparison of detemir (2400 nmol/mL formulation) vs. NPH in basal-bolus T1D regimen |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Randomized trial of detemir vs. NPH (both with aspart) in pregnant women with T1D |
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Phase 3 | Terminated | 596 | Inhaled mealtime insulin vs. subcutaneous aspart, both combined with detemir, in T1D (pulmonary safety focus) |
| [NCT00604344](https://clinicaltrials.gov/study/NCT00604344) | Phase 3 | Completed | 401 | 48-week Japanese trial comparing detemir and NPH human insulin in basal-bolus regimen |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | Completed | 347 | Efficacy/safety comparison of detemir vs. NPH in children and adolescents with T1D |
| [NCT00542399](https://clinicaltrials.gov/study/NCT00542399) | Phase 4 | Completed | 50 | Once- vs. twice-daily detemir dosing in children/adolescents with T1D |
| [NCT00537303](https://clinicaltrials.gov/study/NCT00537303) | Phase 4 | Completed | 296 | Step-wise addition of insulin aspart to once-daily detemir plus oral antidiabetics |
| [NCT02922179](https://clinicaltrials.gov/study/NCT02922179) | N/A (Observational) | Completed | 103,951 | Large real-world descriptive study of long- and intermediate-acting insulin users |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT non-inferiority trial: insulin degludec vs. detemir (both + aspart) in pregnant women with T1D |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review / Network Meta-analysis | Value Health | Comparative efficacy/safety of basal insulin regimens in adults with T1D |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Ultra-long-acting insulin analogues for people with T1D |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematic Review / Meta-analysis | Pol Arch Med Wewn | Detemir vs. NPH insulin in T1D: glycemic control outcomes |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Review / Meta-analysis | Clin Ther | Efficacy and tolerability of degludec vs. other long-acting basal insulins (incl. detemir) in T1D/T2D |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Insulin detemir: review of use in T1D and T2D management |
| [15691219](https://pubmed.ncbi.nlm.nih.gov/15691219/) | 2005 | Review | BioDrugs | Spotlight on insulin detemir in T1D and T2D |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Insulin detemir in the treatment of T1D and T2D |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | Update on treatment of T1D and T2D, focused on insulin detemir |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatr Drugs | Insulin analog preparations (incl. detemir) in children/adolescents with T1D |

---

## US Market Information

No marketing authorization records are present in this dataset. `taiwan_regulatory.total_licenses = 0` and `licenses` is empty, consistent with the recorded market status of **Not Marketed** in this jurisdiction. No product/NDA table can be constructed from available data.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this evidence pack — notably `DG001`, a **Blocking** severity gap on TFDA label warnings/contraindications, which prevents any S1 safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Type 1 diabetes mellitus is supported by an extensive Phase 3 RCT and systematic-review base (L1), but this reflects insulin detemir's **existing approved use**, not a validated new indication — so "proceed" here means proceeding with the understanding that no genuine repurposing opportunity exists in the top-ranked candidate, and the guardrail is against mistaking model rank for novelty. The nine other TxGNN candidates in this pack (ranks 2–10) do not clear the evidence bar: eight are L5/Hold with no trial or literature support, two are flagged as probable reversed-direction (adverse-effect) artifacts, and two rare-disease candidates are speculative mechanistic extensions only.

**To proceed, the following is needed:**
- Resolve `DG001` (Blocking): obtain TFDA label warnings/contraindications before any safety pre-assessment can occur
- Resolve `DG002` (High): obtain formal DrugBank MOA data to properly ground mechanism-based candidate scoring
- Populate `drug.original_indications` so future TxGNN runs can auto-detect and exclude "already-approved indication" false positives like this one
- If genuine repurposing signal is the goal, deprioritize rank 1 and instead investigate whether any lower-ranked candidates (e.g., pancreatic agenesis, thiamine-responsive dysfunction syndrome) warrant targeted literature/trial searches beyond the mechanistic extrapolation already provided
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


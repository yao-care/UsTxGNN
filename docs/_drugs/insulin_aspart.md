---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 796
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin aspart (DrugBank DB01306) is a rapid-acting insulin analog used for glycemic control in diabetes mellitus. The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus**, supported by **10+ clinical trials** and **20 publications** currently on record. Note: the evidence pack itself flags this as likely *not* a true "old drug, new use" case — type 1 diabetes is almost certainly already a standard approved indication for insulin aspart; the `original_indications` field is empty due to a data gap (DG002), so this should be confirmed against the actual product label rather than treated as a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (data gap, DG002) — literature evidence indicates insulin aspart is a rapid-acting insulin analog already used for glycemic control in type 1 and type 2 diabetes mellitus |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| Taiwan (TFDA) Market Status | 未上市 (Not Marketed) |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity data gap). Based on known information, insulin aspart is a rapid-acting insulin analog; its efficacy in glycemic control for diabetes mellitus has been proven, and mechanistically it directly binds the insulin receptor to promote peripheral glucose utilization.

Type 1 diabetes mellitus is a disease of absolute insulin deficiency due to autoimmune β-cell destruction. Physiologic insulin replacement — including rapid-acting analogs like aspart used as prandial/bolus insulin in basal-bolus regimens — is the established standard of care for this condition. The mechanistic link is therefore direct and non-speculative, not an indirect or exploratory repurposing hypothesis.

However, this reframes the nature of the "prediction": since `original_indications` is empty in this evidence pack, it is unclear whether type 1 diabetes is already an approved indication for this product elsewhere. Given that virtually all commercial insulin aspart products (e.g., NovoRapid/NovoLog) are already indicated for type 1 diabetes, this candidate likely represents a data-completeness gap rather than a genuine new-indication opportunity, and should be verified against the actual product label before being treated as a repurposing case.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01992588](https://clinicaltrials.gov/study/NCT01992588) | Phase 1 | Completed | 48 | PK/PD comparison of FIAsp (faster-acting insulin aspart) vs. insulin aspart as CSII bolus in T1DM |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Multinational crossover RCT: insulin detemir+aspart vs. NPH+aspart on hypoglycemia frequency in T1DM basal-bolus regimen |
| [NCT03143816](https://clinicaltrials.gov/study/NCT03143816) | Phase 4 | Completed | 60 | Real-life pilot comparing prandial insulin aspart vs. Technosphere inhaled insulin in T1DM |
| [NCT00542399](https://clinicaltrials.gov/study/NCT00542399) | Phase 4 | Completed | 50 | Once- vs. twice-daily insulin detemir with Novorapid (aspart) as mealtime insulin in pediatric T1DM |
| [NCT01774565](https://clinicaltrials.gov/study/NCT01774565) | NA | Completed | 43 | Closed-loop glucose control comparing faster insulin aspart vs. standard insulin aspart |
| [NCT07068295](https://clinicaltrials.gov/study/NCT07068295) | Phase 1 | Completed | 65 | PK/PD/safety of a novel fast-acting insulin vs. insulin aspart via insulin pump |
| [NCT01194258](https://clinicaltrials.gov/study/NCT01194258) | Phase 2 | Completed | 132 | Double-blind crossover: Lispro-PH20/Aspart-PH20 vs. insulin lispro for prandial control |
| [NCT05653050](https://clinicaltrials.gov/study/NCT05653050) | NA | Completed | 26 | Closed-loop glucose control with ultra-rapid insulin vs. standard pump therapy in adolescents with T1DM |
| [NCT03959514](https://clinicaltrials.gov/study/NCT03959514) | Phase 1 | Completed | 18 | Glucose clamp PK/PD/safety comparison of AT247 vs. NovoRapid® vs. Fiasp® in T1DM |
| [NCT00097071](https://clinicaltrials.gov/study/NCT00097071) | Phase 3 | Completed | 299 | Safety and efficacy of insulin aspart (NovoLog®) vs. insulin lispro via CSII in children/adolescents with T1DM |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT (Phase 3a) | Lancet | ONWARDS 6: once-weekly insulin icodec vs. once-daily degludec, both as part of a basal-bolus (aspart) regimen, in T1DM |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT trial: degludec vs. detemir, both combined with insulin aspart, in pregnant women with T1DM |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | RCT/Systematic Review | Diabetes & Metabolism | Efficacy and safety of rapid-acting insulin aspart vs. regular human insulin in T1DM/T2DM |
| [18710361](https://pubmed.ncbi.nlm.nih.gov/18710361/) | 2008 | RCT | Expert Opin Pharmacother | Biphasic insulin aspart 30 for treatment of type 1 diabetes mellitus |
| [40129237](https://pubmed.ncbi.nlm.nih.gov/40129237/) | 2025 | RCT (crossover) | Diabetes Obes Metab | Faster-acting insulin aspart vs. insulin aspart in T1DM with non-automated pump + CGM |
| [37804858](https://pubmed.ncbi.nlm.nih.gov/37804858/) | 2023 | RCT | Lancet Diabetes Endocrinol | CopenFast: faster aspart vs. insulin aspart in T1DM/T2DM during pregnancy and post-delivery |
| [37404205](https://pubmed.ncbi.nlm.nih.gov/37404205/) | 2023 | RCT (double-blind crossover) | Diabetes Technol Ther | Faster vs. standard insulin aspart with hybrid automated insulin delivery in youth with T1DM |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | Type 1 Diabetes: A Review — disease overview and insulin-based management |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treatments in Endocrinology | Spotlight on insulin aspart in type 1 and 2 diabetes mellitus |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Insulin aspart: a review of its use in the management of type 1 and 2 diabetes mellitus |

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or DDI data are currently on record for this candidate — TFDA label data is a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clinical and literature evidence for insulin aspart in type 1 diabetes is extensive and meets L1 evidence criteria (multiple completed Phase 3 RCTs, e.g., NCT01697657, NCT00097071). However, the product is not currently marketed in Taiwan (0 TFDA licenses), TFDA label safety data is a Blocking gap (DG001), and MOA/original-indication data are missing (DG002) — so this cannot be treated as a confirmed novel repurposing case without further verification.

**To proceed, the following is needed:**
- TFDA-approved package insert (warnings, contraindications, DDI) — Blocking gap, must resolve before any safety review (DG001)
- DrugBank-sourced MOA confirmation (DG002)
- Confirmation of the drug's actual approved original indication(s), to determine whether "Type 1 Diabetes Mellitus" is a genuine new indication or already standard labeling elsewhere
- Regulatory pathway assessment for Taiwan market entry (currently 未上市, 0 licenses)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


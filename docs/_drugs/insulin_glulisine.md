---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 800
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Diabetes Mellitus to Type 1 Diabetes Mellitus (Core Indication, Not a Novel Repurposing Signal)

## One-Sentence Summary

Insulin Glulisine (DrugBank DB01309) is a rapid-acting insulin analogue used for glycemic control in diabetes mellitus. The TxGNN model's top-ranked prediction is **Type 1 Diabetes Mellitus**, which is important to flag upfront: this is not a novel repurposing hypothesis but the drug's own core approved use — the model correctly identified the drug-disease relationship, supported by **~50 clinical trials** and **19 publications**, including several direct Phase 3 pivotal trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license records in evidence pack; drug is currently unmarketed in this jurisdiction) — clinically, insulin glulisine's core use is mealtime glycemic control in diabetes mellitus |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this evidence pack (marked as a data gap). Based on known pharmacology, insulin glulisine is a rapid-acting human insulin analogue (modified at positions B3-Lys and B29-Glu) designed to mimic physiological prandial insulin release, providing faster onset and shorter duration of action than regular human insulin.

The relationship between the "original indication" and the "predicted new indication" here requires an important caveat: the repurposing rationale in the evidence pack explicitly notes that Type 1 Diabetes Mellitus is not a repurposing hypothesis at all — it is insulin's core, label-defining use. The `original_indications` field is empty due to a data gap (this drug is also not currently marketed under the jurisdiction covered by this evidence pack), which caused the pipeline to surface T1DM as a "new" prediction. The high TxGNN score (99.55%) should be read as the knowledge graph correctly recovering a well-established drug-disease relationship, not as discovery of a novel therapeutic use.

Because T1DM is characterized by absolute endogenous insulin deficiency, exogenous rapid-acting insulin replacement is mechanistically direct and not an extrapolation — this is reflected in the very large, high-quality body of Phase 3 evidence below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07070752](https://clinicaltrials.gov/study/NCT07070752) | Phase 3 | Completed | 224 | Non-inferior immunogenicity, efficacy and safety of a glulisine biosimilar (GP40321) vs. Apidra® SoloStar® in T1DM patients |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | Completed | 485 | Compared efficacy, safety and hypoglycemia frequency of insulin glulisine vs. insulin lispro in T1/T2DM patients also using insulin glargine |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | Completed | 142 | 26-week efficacy (HbA1c change) and safety study of insulin glulisine with insulin glargine in T1DM |
| [NCT01194258](https://clinicaltrials.gov/study/NCT01194258) | Phase 2 | Completed | 132 | Crossover safety/efficacy comparison of prandial insulin formulations including glulisine-class rapid-acting insulins in basal-bolus therapy for T2DM |
| [NCT01594060](https://clinicaltrials.gov/study/NCT01594060) | Phase 4 | Completed | 36 | Real-world basal-bolus regimen (including glulisine) vs. sliding-scale insulin in hospitalized non-critically ill diabetic patients |
| [NCT02509429](https://clinicaltrials.gov/study/NCT02509429) | Phase 2 | Completed | 24 | Closed-loop (artificial pancreas) insulin therapy vs. pump therapy for nocturnal hypoglycemia reduction in children with T1DM |
| [NCT01159353](https://clinicaltrials.gov/study/NCT01159353) | Phase 1 | Completed | 37 | Pharmacodynamic/pharmacokinetic comparison of insulin glulisine vs. insulin aspart post-meal in obese T2DM subjects |
| [NCT02914886](https://clinicaltrials.gov/study/NCT02914886) | Phase 4 | Completed | 14 | Investigated whether zinc-free insulin glulisine reduces injection-site lipoatrophy in T1DM patients on insulin pump therapy |
| [NCT03495908](https://clinicaltrials.gov/study/NCT03495908) | N/A | Completed | 136 | Efficacy/safety of regular human insulin vs. rapid-acting insulin (incl. glulisine) via V-Go wearable delivery device in T2DM |
| [NCT02814123](https://clinicaltrials.gov/study/NCT02814123) | Phase 2 | Completed | 28 | Closed-loop co-administration of fast-acting insulin (glulisine) with pramlintide for 24-hour glucose regulation in T1DM inpatients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Hormone and Metabolic Research | Pivotal multinational RCT (n=683) comparing insulin glulisine to insulin lispro in adults with T1DM — established efficacy/safety basis for approval |
| [41366610](https://pubmed.ncbi.nlm.nih.gov/41366610/) | 2026 | Phase III RCT | Diabetes, Obesity & Metabolism | Biosimilar insulin glulisine (T-Glu) vs. originator: immunogenicity, efficacy, and safety in T1DM |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technology & Therapeutics | Randomized 3-way crossover comparing glulisine, aspart and lispro via CSII pump in T1DM, evaluating catheter occlusion rates |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | Comparative Study | Diabetes, Obesity & Metabolism | Efficacy and safety of insulin glulisine vs. lispro in Japanese T1DM patients on glargine basal therapy |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | Comparative Study | Diabetes Technology & Therapeutics | 26-week pediatric trial: comparable efficacy/safety of glulisine vs. lispro in basal-bolus regimen for T1DM children |
| [23425652](https://pubmed.ncbi.nlm.nih.gov/23425652/) | 2013 | Comparative Study | Endocrine Practice | Glulisine vs. aspart for breakfast postprandial glucose control in children with T1DM on MDI |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Comparative Study | Acta Diabetologica | Real-world CSII pump comparison of glulisine vs. lispro/aspart in T1DM, evaluating HbA1c, FBG and hypoglycemia/DKA rates |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Comprehensive review of insulin glulisine's pharmacology and clinical use across diabetes populations |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Cohort | Pediatrics International | 1-year efficacy/safety of glulisine via CSII in 20 children with T1DM |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | PK/PD Study | Diabetes Care | Pharmacokinetics, prandial glucose control and safety of glulisine vs. regular human insulin in pediatric T1DM |

---

## US Market Information

No licenses or authorizations are on record for this drug in the current evidence pack (market status: 未上市 / Not Marketed; total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields in this evidence pack — key warnings, contraindications, and drug interaction data — are marked as data gaps.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for insulin glulisine in Type 1 Diabetes Mellitus is extensive and high quality (L1, multiple completed Phase 3 RCTs including a 2026 biosimilar trial), but this reflects confirmation of the drug's established, label-defining use rather than a genuine repurposing signal — the "original indication" field was empty due to a data gap, not because T1DM is a new application.

**To proceed, the following is needed:**
- TFDA-equivalent package insert warnings/contraindications (currently a Blocking data gap — required before any S1 safety pre-assessment)
- Confirmed original indication and license records, since the drug is currently listed as unmarketed in this jurisdiction
- Formal mechanism of action (MOA) documentation from DrugBank
- Re-classification review: confirm with the study team whether "Type 1 Diabetes Mellitus" should be excluded from repurposing consideration given it is the drug's core indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


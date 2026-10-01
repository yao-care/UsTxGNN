---
layout: default
title: Insulin Aspart
parent: Model Prediction Only (L5)
nav_order: 796
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Insulin Aspart: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin aspart is a rapid-acting insulin analog used for mealtime glycemic control in diabetes.
The TxGNN model predicts it for **type 1 diabetes mellitus**, with **43 clinical trials** and **19 publications** retrieved in this direction.
This is closer to confirmation of standard care than true repurposing: the pack has no label text for the original indication, so that use is taken from general knowledge, not from the pack.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Type 1 diabetes mellitus |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 (multiple completed Phase 3 trials, though some are only partly aspart-specific) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (listed authorizations are BLAs) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the pack. Insulin aspart is a rapid-acting insulin analog. In type 1 diabetes, autoimmune destruction of pancreatic beta cells causes insulin deficiency. Injected aspart replaces the missing mealtime insulin, so the mechanistic link is direct.

The prediction therefore mostly reflects an established use, not a new one. The pack's `original_indications` field is empty and its MOA is a data gap. This should be fixed before release.

The evidence is also uneven in how specific it is to aspart:
- **Strongest aspart-specific evidence:** the Phase 3 trials of aspart in insulin pumps (NCT00097071, NCT01109316), the Phase 4 head-to-head trial against inhaled insulin (NCT03143816), and the Phase 1 PK/PD study of faster aspart (NCT01992588).
- **Weaker evidence:** several trials have truncated titles, so aspart's role in them (bolus background versus study drug) cannot be confirmed from the input.

## Clinical Trial Evidence

The pack lists 43 trials. The 10 most relevant are shown below. Summaries come from the registry text, and the pack contains no efficacy results for these trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00097071](https://clinicaltrials.gov/study/NCT00097071) | Phase 3 | Completed | 299 | Safety and efficacy of insulin aspart vs insulin lispro in insulin pumps in children and adolescents with T1DM |
| [NCT01109316](https://clinicaltrials.gov/study/NCT01109316) | Phase 3 | Completed | 132 | Crossover study of insulin lispro vs insulin aspart in pump reservoirs in T1DM |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Detemir + aspart vs NPH + aspart, comparing hypoglycemia frequency in T1DM (aspart as bolus) |
| [NCT03143816](https://clinicaltrials.gov/study/NCT03143816) | Phase 4 | Completed | 60 | Prandial insulin aspart vs Technosphere inhaled insulin in T1DM on multiple daily injections |
| [NCT01992588](https://clinicaltrials.gov/study/NCT01992588) | Phase 1 | Completed | 48 | PK/PD of faster-acting insulin aspart (FIAsp) vs insulin aspart as a bolus in T1DM pump users |
| [NCT03436498](https://clinicaltrials.gov/study/NCT03436498) | Phase 1 | Completed | 45 | Pump safety (infusion set occlusions) of SAR341402 vs NovoLog in adults with T1DM |
| [NCT01464099](https://clinicaltrials.gov/study/NCT01464099) | Phase 1 | Completed | 24 | Bioequivalence of NovoLog 100 U/mL vs 200 U/mL formulations in T1DM |
| [NCT04759144](https://clinicaltrials.gov/study/NCT04759144) | N/A | Completed | 27 | Hybrid closed-loop with faster aspart vs standard aspart in young children with T1DM |
| [NCT03579615](https://clinicaltrials.gov/study/NCT03579615) | N/A | Completed | 18 | Closed-loop control with faster-acting aspart vs aspart in adults with T1DM |
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Phase 3 | Terminated | 596 | Inhaled mealtime insulin (AERx) vs subcutaneous aspart, both with detemir, in T1DM |

## Literature Evidence

The pack lists 19 publications. The 10 most relevant are shown below, with RCTs first. Where only the abstract objective is available, that is what is summarized.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40129237](https://pubmed.ncbi.nlm.nih.gov/40129237/) | 2025 | RCT | Diabetes Obes Metab | Double-blind crossover of faster aspart vs aspart in adults with T1D on non-automated pump plus CGM |
| [37404205](https://pubmed.ncbi.nlm.nih.gov/37404205/) | 2023 | RCT | Diabetes Technol Ther | Faster vs standard aspart with hybrid automated insulin delivery in 30 active youths with T1D |
| [37804858](https://pubmed.ncbi.nlm.nih.gov/37804858/) | 2023 | RCT | Lancet Diabetes Endocrinol | CopenFast: faster aspart vs aspart on fetal growth in pregnancy and post-delivery (T1D or T2D) |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: degludec vs detemir, both with aspart, in pregnant women with T1D |
| [36633505](https://pubmed.ncbi.nlm.nih.gov/36633505/) | 2023 | RCT | Diabetes Obes Metab | Pramlintide/insulin A21G co-formulation (ADO09) improved postprandial glucose and time in range vs aspart in T1D |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: icodec vs degludec in a basal-bolus regimen in T1D (indirect for aspart) |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | Systematic review | Diabetes Metab | Efficacy and safety of insulin aspart vs regular human insulin in T1DM and T2DM |
| [35746893](https://pubmed.ncbi.nlm.nih.gov/35746893/) | 2023 | Meta-analysis | Diabetes Metab J | Fast-acting aspart vs aspart in insulin pumps for T1DM |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Review of insulin aspart in T1DM and T2DM: lower HbA1c than regular insulin when given immediately before meals |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | General review of type 1 diabetes (not aspart-specific) |

## US Market Information

The pack lists 20 licenses in total. Four distinct main authorizations are shown. Approved-indication text is not available in the pack.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA020986 | NOVOLOG | Injection, solution | A-S Medication Solutions |
| BLA020986 | Insulin Aspart | Injection, solution | REMEDYREPACK INC. |
| BLA761325 | MERILOG | Injection, solution | Sanofi-Aventis U.S. LLC |
| BLA021172 | Insulin Aspart Protamine and Insulin Aspart | Injection, suspension | REMEDYREPACK INC. |

## Safety Considerations

- **Injection-site reactions:** Localized lipodystrophy at injection sites is a known adverse effect of injected insulin. It appears among the model's predicted associations (drug-induced localized lipodystrophy) and is more likely a safety signal than a therapeutic use.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Completed Phase 3 and Phase 4 trials, plus RCTs and systematic reviews, support aspart in T1DM, and the mechanism is direct insulin replacement. However, this is an established use, not new repurposing. Safety data are missing, and several trials cannot be confirmed as aspart-specific.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (flagged as a blocking gap, DG001)
- Mechanism of action data from DrugBank (DG002)
- Original indication label text
- Confirmation of aspart's role in trials with truncated titles (e.g., NCT01697657)
- Reclassification of this candidate as standard-care confirmation in the pack

**Other predictions in the pack:**
- Permanent neonatal diabetes mellitus has the only other supporting evidence (L4). It rests on a single non-aspart-specific review, and some genetic subtypes respond to sulfonylureas, so it is a research question.
- The remaining eight predictions are L5 with no trials or literature. They should be held, and drug-induced localized lipodystrophy should be reclassified as an adverse-effect link.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


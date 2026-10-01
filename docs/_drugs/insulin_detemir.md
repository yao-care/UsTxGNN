---
layout: default
title: Insulin Detemir
parent: Model Prediction Only (L5)
nav_order: 798
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin Detemir: From Basal Insulin Therapy to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin detemir (Levemir) is a long-acting basal insulin analogue for diabetes. The TxGNN model predicts **type 1 diabetes mellitus (T1DM)** as its top indication, but this is the drug's established on-label use, not a true repurposing discovery. The prediction is backed by 50 registered clinical trials, including many completed Phase 3 trials, and 19 publications.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Type 1 diabetes mellitus |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 (multiple completed Phase 3 RCTs) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 entries, all under BLA021536 |
| Recommended Decision | Proceed with Guardrails |

The database has no original-indication text (the approved indication fields are empty), so the original indication is omitted. This is a database gap that should be corrected.

---

## Why is This Prediction Reasonable?

Detemir is a soluble, long-acting human insulin analogue acylated with a 14-carbon fatty acid. It binds the insulin receptor and replaces the endogenous insulin that is missing in T1DM. The fatty acid lets it bind reversibly to albumin, which slows absorption and gives a prolonged, consistent effect of up to 24 hours (PMID 15516157). Detailed MOA data are not available in the record itself.

T1DM is characterized by absolute insulin deficiency, so basal insulin replacement is the standard mechanistic fit. The prediction is therefore correct, but it should be labeled as **on-label use** rather than a repurposing discovery.

The other nine predictions (ranks 2–10) are weak. Most reflect knowledge-graph comorbidity or adverse-effect associations, not therapeutic mechanisms (details in the Conclusion).

---

## Clinical Trial Evidence

The record lists 50 trials. The 10 most relevant T1DM trials are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00184665](https://clinicaltrials.gov/study/NCT00184665) | Phase 3 | Completed | 501 | 2-year efficacy and safety comparison of detemir vs NPH in T1DM (HbA1c, hypoglycemia, weight, antibodies) |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | Completed | 752 | 6-month open-label comparison of detemir vs NPH in T1DM on a basal-bolus regimen |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Detemir vs NPH (with aspart) in pregnant women with T1DM |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | Completed | 347 | Detemir vs NPH in children and adolescents with T1DM |
| [NCT00623194](https://clinicaltrials.gov/study/NCT00623194) | Phase 3 | Completed | 146 | 52-week extension in children aged 3–17, assessing safety and antibody development |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Randomized cross-over comparing hypoglycemia frequency, detemir vs NPH, in well-controlled T1DM |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | Completed | 114 | Detemir + aspart vs NPH + aspart in adults with T1DM |
| [NCT00184639](https://clinicaltrials.gov/study/NCT00184639) | Phase 3 | Completed | 71 | Detemir vs Semilente MC in children, adolescents and young adults with T1DM |
| [NCT00313742](https://clinicaltrials.gov/study/NCT00313742) | Phase 4 | Completed | 51 | Effect of exercise on glucose decline with detemir, glargine or NPH in T1DM |
| [NCT00542399](https://clinicaltrials.gov/study/NCT00542399) | Phase 4 | Completed | 50 | Once- vs twice-daily detemir in children and adolescents with T1DM |

The record also includes large observational safety studies (n = 480 to 5,926) and Phase 1 pharmacokinetic studies. Those are not listed here.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: open-label non-inferiority trial of degludec vs detemir (with aspart) in pregnant women with T1DM |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematic review / meta-analysis | Pol Arch Med Wewn | Detemir vs NPH in T1DM; benefits on glycemic control were not confirmed by all studies |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Network meta-analysis | Value Health | Relative efficacy and safety of basal insulin regimens in adults with T1DM |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Cochrane review | Cochrane Database Syst Rev | (Ultra-)long-acting insulin analogues in T1DM, focusing on complications and hypoglycemia |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic review / meta-analysis | Clin Ther | Degludec vs other long-acting analogues (glargine, detemir) in T1D and T2D |
| [30666772](https://pubmed.ncbi.nlm.nih.gov/30666772/) | 2019 | Pooled RCT analysis | Pediatr Diabetes | Hyperglycemia and ketosis rates with degludec vs detemir in pediatric T1D, from two randomized trials |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Detemir is more predictable and consistent than NPH, with less intrapatient variability |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Detemir has lower PK variability than NPH or ultralente and can reduce hypoglycemia risk, especially nocturnal |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | Detemir provides effective therapy in T1D and T2D with a lower hypoglycemia rate |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatr Drugs | Insulin analogues, including detemir, in children and adolescents with T1DM |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA 021536 | Levemir / LEVEMIR | Injection, solution | A-S Medication Solutions |

The three listed entries share this authorization number and manufacturer. Approved indication text was not supplied.

---

## Safety Considerations

- **Package insert data are missing** from this record. Warnings and contraindications were not supplied, and no drug interactions were found.
- Standard basal-insulin cautions still apply: **hypoglycemia** and **injection-site reactions**, including lipohypertrophy and lipoatrophy.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Detemir has multiple completed Phase 3 RCTs in T1DM across adults, children and pregnancy, plus systematic reviews and a Cochrane review, so the evidence is strong (L1). The record is on-label use, not a repurposing discovery, and should be labeled as such.

Other predictions:
- **Pancreatic agenesis** (rank 7, Research Question): basal insulin replacement is mechanistically plausible, but no trials or literature were supplied and detemir labeling is not established for neonates.
- **Ranks 2–6 and 9** (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, stiff person syndrome and its focal variant, centrifugal lipodystrophy): Hold. These reflect comorbidity or pathway associations, not therapeutic mechanisms.
- **Ranks 8 and 10** (drug-induced localized lipodystrophy, pressure-induced localized lipoatrophy): Hold. These are known insulin adverse effects, so they are safety concerns, not indications.

**To proceed, the following is needed:**
- Parse the US package insert (BLA021536) for warnings, contraindications and approved indications. This is a blocking data gap.
- Correct the empty original-indication and MOA fields in the database.
- Label the record as on-label use.
- For pancreatic agenesis, run a neonatal-specific dosing and safety review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


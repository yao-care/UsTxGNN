---
layout: default
title: Sotagliflozin
parent: 僅模型預測 (L5)
nav_order: 1177
evidence_level: L5
indication_count: 10
---

# Sotagliflozin
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

# Sotagliflozin: From Diabetes Glycemic Control to Cardiorenal Protection in Diabetes Mellitus

## One-Sentence Summary

Sotagliflozin is a dual SGLT1/SGLT2 inhibitor whose core, well-established use is glycemic control in diabetes mellitus (Type 1 and Type 2).
The TxGNN model's highest-scoring prediction in this batch — **diabetes mellitus** — is strongly supported by **60+ clinical trials** (including the landmark SCORED and SOLOIST-WHF Phase 3 outcome trials) and **20 publications**, extending the evidence base beyond glycemic control into **cardiovascular and renal protection**.
Nine other model-predicted indications in this batch (e.g., opsismodysplasia, stiff person syndrome, lipodystrophies) scored comparably high but have **zero supporting clinical trials or literature** and are flagged Hold — these appear to be model artifacts rather than credible repurposing signals.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in this evidence pack (no regulatory license data available); mechanistic evidence indicates diabetes mellitus glycemic control as the drug's core/original use |
| Predicted New Indication | Diabetes Mellitus (disease) — with expanded cardiorenal protection evidence |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Sotagliflozin is a dual inhibitor of SGLT1 (intestinal) and SGLT2 (renal). Intestinal SGLT1 inhibition reduces glucose absorption and delays incretin degradation, while renal SGLT2 inhibition promotes urinary glucose excretion. This dual mechanism directly targets glycemic regulation as well as downstream cardiovascular and renal risk pathways — meaning diabetes mellitus is not a novel "old-drug-new-use" target for this compound, but rather a validation of its core pharmacology.

What is genuinely notable in the evidence is the **extension beyond simple glycemic control**: large outcome trials such as SCORED (NCT03315143, N=10,584, Type 2 diabetes with CKD/CV risk) and SOLOIST-WHF (NCT03521934, N=1,222, Type 2 diabetes with recent worsening heart failure) demonstrate benefit on cardiovascular death, heart failure hospitalization, and renal outcomes — independent of and beyond HbA1c reduction. A Phase 4 trial (NCT05562063, SOTA-P-CARDIA) even tested sotagliflozin in HFpEF patients **without diabetes**, and ongoing Phase 3 work (NCT06217302) is evaluating renal protection specifically in Type 1 diabetes with diabetic kidney disease.

Because sotagliflozin also inhibits intestinal SGLT1, a mechanism distinct from selective SGLT2 inhibitors, it carries a class-differentiated diabetic ketoacidosis (DKA) risk signal in Type 1 diabetes populations, reflected in multiple dedicated ketone-monitoring trials (see Clinical Trial Evidence below).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03315143](https://clinicaltrials.gov/study/NCT03315143) | Phase 3 | Terminated | 10,584 | SCORED: sotagliflozin vs placebo on CV death/HF hospitalization/urgent HF visits in T2D with CKD and CV risk factors |
| [NCT03521934](https://clinicaltrials.gov/study/NCT03521934) | Phase 3 | Terminated | 1,222 | SOLOIST-WHF: sotagliflozin vs placebo on CV death and HF events in T2D patients after recent worsening heart failure |
| [NCT02531035](https://clinicaltrials.gov/study/NCT02531035) | Phase 3 | Completed | 1,405 | inTandem3: net clinical benefit of sotagliflozin as adjunct to insulin in Type 1 diabetes |
| [NCT03332771](https://clinicaltrials.gov/study/NCT03332771) | Phase 3 | Completed | 954 | inTandem2-style T2D trial: non-inferiority to glimepiride on HbA1c reduction plus weight/SBP benefit |
| [NCT02421510](https://clinicaltrials.gov/study/NCT02421510) | Phase 3 | Completed | 782 | inTandem1: sotagliflozin as adjunct therapy in T1D with inadequate control on insulin |
| [NCT03351478](https://clinicaltrials.gov/study/NCT03351478) | Phase 3 | Completed | 770 | Superiority vs placebo (and comparison with empagliflozin) on HbA1c reduction in T2D on DPP4i ± metformin |
| [NCT03285594](https://clinicaltrials.gov/study/NCT03285594) | Phase 3 | Completed | 571 | Efficacy/safety in T2D inadequately controlled on basal insulin ± oral antidiabetics |
| [NCT06217302](https://clinicaltrials.gov/study/NCT06217302) | Phase 3 | Recruiting | 150 | Evaluating whether sotagliflozin slows kidney function decline in T1D with moderate-severe diabetic kidney disease |
| [NCT02926937](https://clinicaltrials.gov/study/NCT02926937) | Phase 3 | Completed | 399 | Monotherapy superiority vs placebo on HbA1c reduction in T2D |
| [NCT05562063](https://clinicaltrials.gov/study/NCT05562063) | Phase 4 | Completed | 88 | SOTA-P-CARDIA: sotagliflozin in HFpEF patients **without** diabetes, testing benefit independent of glycemic status |

Additional safety-focused trials worth noting: [NCT07421518](https://clinicaltrials.gov/study/NCT07421518), [NCT06147232](https://clinicaltrials.gov/study/NCT06147232), and [NCT07325201](https://clinicaltrials.gov/study/NCT07325201) are dedicated to continuous ketone monitoring for DKA risk mitigation in Type 1 diabetes patients on SGLT inhibitors — a class-specific safety signal relevant to this drug's dual SGLT1/2 mechanism.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33200891](https://pubmed.ncbi.nlm.nih.gov/33200891/) | 2021 | RCT (Tier 1) | New England Journal of Medicine | SCORED trial: sotagliflozin reduces CV events in diabetes with chronic kidney disease |
| [33200892](https://pubmed.ncbi.nlm.nih.gov/33200892/) | 2021 | RCT (Tier 1) | New England Journal of Medicine | SOLOIST-WHF trial: sotagliflozin safe/effective when initiated soon after worsening heart failure |
| [38277468](https://pubmed.ncbi.nlm.nih.gov/38277468/) | 2024 | Secondary Analysis | Clinical Journal of the American Society of Nephrology | Reconciled SCORED data confirm kidney/albuminuria benefit of sotagliflozin in T2D+CKD |
| [38141092](https://pubmed.ncbi.nlm.nih.gov/38141092/) | 2024 | Meta-analysis (Tier 2) | Journal of Nephrology | Meta-analysis confirms safety/efficacy of sotagliflozin in T2D with concomitant CKD |
| [36782093](https://pubmed.ncbi.nlm.nih.gov/36782093/) | 2023 | RCT | Diabetes, Obesity & Metabolism | Efficacy and safety of sotagliflozin in T2D with stage 3 chronic kidney disease |
| [38768620](https://pubmed.ncbi.nlm.nih.gov/38768620/) | 2024 | Systematic Review (Tier 2) | Lancet Diabetes & Endocrinology | SGLT2 inhibitors (incl. sotagliflozin) reduce HF outcomes/CV death across the cardiometabolic disease spectrum |
| [38179304](https://pubmed.ncbi.nlm.nih.gov/38179304/) | 2023 | Network Meta-analysis | Frontiers in Endocrinology | Comparative CV benefit of 5 SGLT2 inhibitors incl. sotagliflozin in T2D with heart failure history |
| [34545668](https://pubmed.ncbi.nlm.nih.gov/34545668/) | 2022 | Systematic Review/Meta-analysis | Diabetes, Obesity & Metabolism | Overall efficacy and safety of sotagliflozin in Type 2 diabetes |
| [40545438](https://pubmed.ncbi.nlm.nih.gov/40545438/) | 2025 | Comprehensive Review | Chinese Journal of Applied Physiology | Detailed review of dual SGLT1/SGLT2 mechanism and clinical benefits in T1D and T2D |
| [40228542](https://pubmed.ncbi.nlm.nih.gov/40228542/) | 2025 | Preclinical | Drug Research | Animal model data suggest potential benefit in non-alcoholic fatty liver disease, alone or with linagliptin |

---

## US Market Information

Sotagliflozin currently has **no marketing authorizations** on record in this jurisdiction (market status: Not Marketed, 0 licenses). No product-level license data (NDA numbers, dosage forms, approved indication text) is available in this evidence pack.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-drug interactions) were not available in this evidence pack.

**Evidence-derived safety signal:** Multiple ongoing trials (NCT07421518, NCT06147232, NCT07325201) are specifically designed around continuous ketone monitoring to mitigate diabetic ketoacidosis (DKA) risk in Type 1 diabetes patients using SGLT inhibitors — a known class effect that is particularly relevant given sotagliflozin's additional SGLT1 inhibition.

Please refer to the package insert for complete safety information once available.

---

## Note on Other TxGNN Predictions in This Batch

This batch's single highest-scoring prediction (**opsismodysplasia**, 99.61%) and eight further high-scoring predictions (thiamine-responsive dysfunction syndrome, stiff person syndrome variants, autoimmune oophoritis, and four lipodystrophy subtypes) all carry **zero clinical trials, zero literature, Evidence Level L5, and a Hold recommendation**. Per the underlying rationale text, none of these have a plausible mechanistic link to SGLT1/2 inhibition. These should not be pursued without independent preclinical or mechanistic justification.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The diabetes mellitus prediction is backed by L1-level evidence (multiple completed Phase 3 RCTs plus two landmark outcome trials, SCORED and SOLOIST-WHF, published in NEJM). However, this largely reflects the drug's core pharmacology rather than a novel repurposing signal, and the drug is currently unmarketed in this jurisdiction with no regulatory license data on file — hence guardrails rather than an unqualified Go.

**To proceed, the following is needed:**
- Confirm original approved indication and regulatory history (original_indications and market license data are currently gaps)
- Obtain formal package insert / label data for warnings, contraindications, and DKA risk in Type 1 diabetes populations
- Obtain detailed MOA documentation from DrugBank to replace the current data gap
- Do not advance opsismodysplasia or the other eight L5/Hold predictions without new mechanistic or preclinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


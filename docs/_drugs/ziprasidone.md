---
layout: default
title: Ziprasidone
parent: 僅模型預測 (L5)
nav_order: 1310
evidence_level: L5
indication_count: 10
---

# Ziprasidone
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

# Ziprasidone: From Schizophrenia/Bipolar Disorder to Major Affective Disorder

## One-Sentence Summary

> Ziprasidone is an atypical antipsychotic originally used for schizophrenia and bipolar I disorder (mania), though it currently holds no valid marketing license in Taiwan.
> The TxGNN model's strongest evidence-backed prediction is that it may be effective for **Major Affective Disorder** (bipolar depression / adjunctive treatment of major depressive disorder),
> with **29 clinical trials** and **20 publications** currently supporting this direction — including two completed Phase 3 RCTs.

*Note: This evidence pack generated 10 TxGNN candidate indications for ziprasidone. Eight of them (e.g., hydranencephaly, X-linked myopia, congenital disorder of glycosylation) have no biological plausibility and zero supporting evidence (Evidence Level L5, all "Hold"), so they are excluded from this report. Major Affective Disorder is the only candidate with substantive clinical evidence; Tourette syndrome (rank 7, L3, "Research Question") is a secondary, lower-confidence candidate worth separate future tracking.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia; Bipolar I Disorder (acute mania) — based on internationally established approvals; no TFDA license record exists to confirm this for Taiwan |
| Predicted New Indication | Major Affective Disorder (bipolar depression / MDD adjunctive therapy) |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L1 |
| Market Status | ✗ Not Marketed (Taiwan) |
| Number of NDAs (Taiwan) | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is currently a data gap for this evidence pack. Based on the pharmacological profile referenced in the trial/literature evidence, ziprasidone acts as a 5-HT2A/D2 receptor antagonist with additional 5-HT1A partial agonism and SNRI-like reuptake inhibition — a receptor profile that is mechanistically distinct from most other second-generation antipsychotics and gives it inherent antidepressant-like activity in addition to its antipsychotic effect.

Ziprasidone's original approved uses (schizophrenia, bipolar I mania) sit on the same disease spectrum as "major affective disorder," which encompasses bipolar depression and treatment-resistant major depressive disorder. The serotonergic/dopaminergic mechanism that controls psychotic and manic symptoms is pharmacologically continuous with the mechanism proposed for mood-stabilizing and antidepressant-augmenting effects, making this a biologically coherent extension rather than a mechanistically distant repurposing hypothesis.

It is worth flagging directly: the evidence pack's own rationale notes that this "new indication" substantially overlaps with ziprasidone's existing international label (bipolar depression add-on, adjunctive MDD treatment already studied and, in some markets, labeled). This means the TxGNN signal here is best understood as confirming known pharmacology and supporting a Taiwan market-entry / label-extension case, rather than uncovering a genuinely novel indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00483548](https://clinicaltrials.gov/study/NCT00483548) | Phase 3 | Completed | 298 | 6-week double-blind, placebo-controlled add-on trial of ziprasidone with lithium/valproate/lamotrigine in Bipolar I Depression |
| [NCT00141271](https://clinicaltrials.gov/study/NCT00141271) | Phase 3 | Completed | 536 | Randomized, double-blind, fixed/flexible-dose, placebo-controlled study of oral ziprasidone in outpatients with Bipolar I Depression |
| [NCT02305823](https://clinicaltrials.gov/study/NCT02305823) | Phase 4 | Completed | 203 | Real-world head-to-head effectiveness of aripiprazole, quetiapine, and ziprasidone in first-episode non-affective psychosis |
| [NCT01053429](https://clinicaltrials.gov/study/NCT01053429) | N/A | Completed | 3391 | Post-marketing pharmacovigilance study evaluating safety/efficacy of ziprasidone (Zeldox) 20–80 mg across the real-world population |
| [NCT00622739](https://clinicaltrials.gov/study/NCT00622739) | Phase 4 | Completed | 28 | Open-label pilot comparing rapid vs. slow dose titration of ziprasidone in pediatric bipolar disorder |
| [NCT01168674](https://clinicaltrials.gov/study/NCT01168674) | Phase 4 | Completed | 49 | Predictors of response to ziprasidone augmentation in Major Depressive Disorder, double-blind placebo-controlled crossover |
| [NCT01113541](https://clinicaltrials.gov/study/NCT01113541) | Phase 3 | Terminated | 13 | Open-label study of ziprasidone's impact on metabolic syndrome risk factors in bipolar patients (terminated, small sample) |
| [NCT02075047](https://clinicaltrials.gov/study/NCT02075047) | Phase 3 | Terminated | 171 | Randomized, double-blind, placebo-controlled trial of ziprasidone in pediatric/adolescent Bipolar I Disorder (manic/mixed), terminated |
| [NCT00650611](https://clinicaltrials.gov/study/NCT00650611) | Phase 2 | Completed | 63 | 27-week open-label safety/tolerability study of oral ziprasidone in children/adolescents with bipolar I, schizophrenia, or schizoaffective disorder |
| [NCT00705185](https://clinicaltrials.gov/study/NCT00705185) | N/A | Completed | 120 | Exploratory biomarker study measuring effects of ziprasidone monotherapy on serum/plasma markers in Major Depressive Disorder |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27835715](https://pubmed.ncbi.nlm.nih.gov/27835715/) | 2017 | RCT | J Clin Psychiatry | Randomized, double-blind, placebo-controlled study of ziprasidone augmentation of escitalopram in MDD — cardiac, endocrine, metabolic, motoric effects |
| [26085041](https://pubmed.ncbi.nlm.nih.gov/26085041/) | 2015 | RCT | Am J Psychiatry | Efficacy results of ziprasidone augmentation of escitalopram in adults with nonpsychotic unipolar MDD unresponsive to 8 weeks of escitalopram |
| [28749091](https://pubmed.ncbi.nlm.nih.gov/28749091/) | 2018 | RCT (subanalysis) | J Clin Psychiatry | Efficacy of ziprasidone augmentation of escitalopram specifically on cognitive symptoms of MDD |
| [24815673](https://pubmed.ncbi.nlm.nih.gov/24815673/) | 2014 | RCT | Int Clin Psychopharmacol | 12-week randomized, double-blind, placebo-controlled sequential parallel comparison trial of ziprasidone monotherapy in MDD, with/without psychomotor symptoms |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Meta-analysis/NMA | J Affect Disord | Network meta-analysis comparing efficacy/discontinuation of augmentation agents (including ziprasidone) in treatment-resistant depression |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Meta-analysis | J Psychopharmacol | Comparative efficacy/tolerability of antidepressant + second-generation antipsychotic combinations vs. esketamine vs. lithium in MDD |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic review/meta-analysis | Psychol Med | Efficacy and safety/tolerability of antipsychotics (monotherapy and adjunctive) in adult MDD |
| [35993319](https://pubmed.ncbi.nlm.nih.gov/35993319/) | 2022 | Systematic review/NMA | Psychol Med | Efficacy and acceptability of second-generation antipsychotics as augmentation in unipolar depression |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia-Pac Psychiatry | Review of SGAs (including ziprasidone) as antidepressant augmentation agents, receptor-profile rationale |
| [26619770](https://pubmed.ncbi.nlm.nih.gov/26619770/) | 2015 | Review | Am J Psychiatry | Focused review: adjunctive ziprasidone in major depression and status of adjunctive atypical antipsychotics |

---

## US Market Information

Ziprasidone currently holds **no valid TFDA marketing license in Taiwan** (`taiwan_regulatory.total_licenses = 0`, market status "未上市"/Not Marketed). No license records are available to summarize brand names, dosage forms, or approved indication text.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently data gaps in this evidence pack — flagged as `DG001`, a **Blocking** severity gap requiring TFDA label retrieval before any S1 safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (NCT00483548, n=298; NCT00141271, n=536) plus a large post-marketing surveillance study (n=3391) and 20 supporting publications — including several RCTs and meta-analyses — establish solid, reproducible evidence (L1) that ziprasidone is effective in bipolar depression and as MDD augmentation. However, this indication substantially overlaps with the drug's existing international approved label rather than being a novel repurposing finding, and the drug is not currently marketed in Taiwan, so this is better framed as a market-entry/label-extension case than a de novo repurposing bet.

**To proceed, the following is needed:**
- Retrieve TFDA (or reference-market) package insert warnings and contraindications (`DG001`, blocking) before any safety pre-assessment
- Obtain formal DrugBank/regulatory MOA documentation (`DG002`) to replace the receptor-profile inference used in this report
- Clarify Taiwan regulatory pathway given zero current licenses (new NDA vs. import drug registration)
- Given known QTc-prolongation concerns with ziprasidone as a drug class, confirm cardiac monitoring requirements once official safety data is available
- Separately track Tourette syndrome (L3, pilot study + case reports) as a lower-priority research question, not a current guardrail candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


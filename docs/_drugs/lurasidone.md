---
layout: default
title: Lurasidone
parent: Model Prediction Only (L5)
nav_order: 878
evidence_level: L5
indication_count: 10
---

# Lurasidone
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

# Lurasidone: From Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lurasidone is an atypical antipsychotic. The literature in the Evidence Pack describes its US uses as schizophrenia and bipolar I depression, but the license records supplied no indication text.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, with **14 clinical trials** and **18 publications** retrieved for this direction.
Nearly all of this evidence concerns bipolar I *depression*, which is already a labeled use. No study directly shows efficacy in acute mania.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (from literature; US license records carry no indication text) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 (multiple completed Phase 3 RCTs, but in bipolar depression rather than mania) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (the 5 listed are generic ANDAs) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the dataset. Based on general pharmacology, lurasidone is an atypical antipsychotic. It antagonizes D2, 5-HT2A and 5-HT7 receptors and is a partial agonist at 5-HT1A. This profile is consistent with mood-stabilizing and antidepressant effects in bipolar disorder.

Schizophrenia and bipolar disorder are both major psychiatric illnesses treated with overlapping antipsychotic drugs. The predicted "manic bipolar affective disorder" label sits in the same disease family as the bipolar I depression indication that lurasidone already carries in the US.

**Caveat:** The Phase 3 program covers bipolar I depression in adults and children, as monotherapy and adjunctive to lithium or valproate. A 2020 expert review (PMID 31957501) states that lurasidone has not been studied in patients with mania or bipolar psychosis. The prediction is therefore best read as supporting bipolar disorder broadly, not acute mania specifically. Confirm the target phenotype before treating this as a true repurposing signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01986101](https://clinicaltrials.gov/study/NCT01986101) | Phase 3 | Completed | 525 | Randomized, double-blind, placebo-controlled study of SM-13496 (lurasidone) in bipolar I depression |
| [NCT02046369](https://clinicaltrials.gov/study/NCT02046369) | Phase 3 | Completed | 350 | 6-week placebo-controlled flexible-dose study in children and adolescents with bipolar I depression |
| [NCT01358357](https://clinicaltrials.gov/study/NCT01358357) | Phase 3 | Completed | 965 | Lurasidone adjunctive to lithium or divalproex for preventing recurrence in bipolar I disorder |
| [NCT01575561](https://clinicaltrials.gov/study/NCT01575561) | Phase 3 | Completed | 377 | 12-week open-label extension of lurasidone adjunctive to lithium or divalproex; long-term safety and tolerability |
| [NCT01914393](https://clinicaltrials.gov/study/NCT01914393) | Phase 3 | Completed | 702 | 104-week open-label extension in pediatric patients; long-term safety and effectiveness |
| [NCT01986114](https://clinicaltrials.gov/study/NCT01986114) | Phase 3 | Completed | 495 | Long-term efficacy and safety of SM-13496 in bipolar I disorder |
| [NCT02731612](https://clinicaltrials.gov/study/NCT02731612) | Phase 3 | Completed | 100 | Placebo-controlled adjunctive lurasidone for cognition in euthymic bipolar I/II patients |
| [NCT04383691](https://clinicaltrials.gov/study/NCT04383691) | Phase 3 | Terminated | 124 | 6-week placebo-controlled flexible-dose study in bipolar I depression; stopped early |
| [NCT06433635](https://clinicaltrials.gov/study/NCT06433635) | Phase 4 | Active, not recruiting | 2726 | Pragmatic sequential trial comparing cariprazine, quetiapine, lurasidone and aripiprazole/escitalopram in bipolar depression |
| [NCT01932541](https://clinicaltrials.gov/study/NCT01932541) | Phase 4 | Withdrawn | 0 | Planned open-label lurasidone study for mania in children and adolescents; never enrolled |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39557452](https://pubmed.ncbi.nlm.nih.gov/39557452/) | 2024 | Systematic review / dose-response meta-analysis | BMJ Ment Health | Examines the lurasidone dose-response relationship for efficacy, acceptability and metabolic/endocrine profile in bipolar depression |
| [37595997](https://pubmed.ncbi.nlm.nih.gov/37595997/) | 2023 | Network meta-analysis | Lancet Psychiatry | Compares efficacy and tolerability of drug treatments for acute bipolar depression in adults |
| [33177610](https://pubmed.ncbi.nlm.nih.gov/33177610/) | 2021 | Systematic review / network meta-analysis | Mol Psychiatry | Compares antipsychotics and mood stabilizers in the maintenance phase of bipolar disorder |
| [31957501](https://pubmed.ncbi.nlm.nih.gov/31957501/) | 2020 | Review | Expert Opin Pharmacother | Reviews lurasidone pharmacology and major RCTs; notes it is approved for bipolar I depression but has not been studied in mania |
| [29536616](https://pubmed.ncbi.nlm.nih.gov/29536616/) | 2018 | Guideline | Bipolar Disord | CANMAT/ISBD 2018 guidelines for managing bipolar disorder |
| [34599629](https://pubmed.ncbi.nlm.nih.gov/34599629/) | 2021 | Guideline | Bipolar Disord | CANMAT/ISBD recommendations for bipolar disorder with mixed presentations |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | Overview of diagnosis and treatment of bipolar disorder |
| [36472471](https://pubmed.ncbi.nlm.nih.gov/36472471/) | 2022 | Review | J Child Adolesc Psychopharmacol | Treatment algorithms for manic/mixed and depressed episodes in pediatric bipolar disorder |
| [39243127](https://pubmed.ncbi.nlm.nih.gov/39243127/) | 2024 | Review | Med Sci Monit | Narrative review of newer antipsychotics and mood stabilizers, including lurasidone, in bipolar disorder and schizophrenia |
| [24170243](https://pubmed.ncbi.nlm.nih.gov/24170243/) | 2014 | Commentary | Am J Psychiatry | "Lurasidone and bipolar disorder" (no abstract available) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA212244 | lurasidone hydrochloride | Tablet, film coated | Ascend Laboratories, LLC |
| ANDA213248 | Lurasidone Hydrochloride | Tablet, film coated | Alembic Pharmaceuticals Inc. |
| ANDA208058 | Lurasidone Hydrochloride | Tablet, film coated | Heritage Pharma Labs Inc. d/b/a Avet Pharmaceuticals Inc. |
| ANDA218174 | Lurasidone Hydrochloride | Tablet, film coated | Camber Pharmaceuticals, Inc. |
| ANDA208028 | Lurasidone Hydrochloride | Tablet, film coated | Exelan Pharmaceuticals Inc. |

The drug is marketed only as oral tablets (film coated, coated and plain). There are 20 licenses in total.

## Safety Considerations

Please refer to the package insert for safety information. The interaction query returned no records.

Antipsychotic-induced weight gain and metabolic effects are a known class concern. A dose-response meta-analysis (PMID 39557452) evaluated lurasidone's metabolic and endocrine profile.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 RCTs and extension studies support lurasidone in bipolar I disorder, and meta-analyses and guidelines back this. That evidence addresses bipolar depression, which is already a labeled use. It does not show efficacy in acute manic or mixed episodes, and the only mania-specific trial (NCT01932541) was withdrawn.

The other nine predicted indications (ranks 2–10, such as retinal dystrophy, myopia and hydranencephaly) rest on the model score alone. They have no trials and no plausible mechanism, so they are rated L5 / Hold.

**To proceed, the following is needed:**
- Decide whether the target is bipolar depression (already labeled) or acute mania (unsupported); if mania, a dedicated trial or mania-specific data is required
- Package insert warnings and contraindications from the FDA label, needed for safety screening
- Detailed mechanism-of-action data from DrugBank
- Metabolic monitoring plan (weight, glucose, lipids) and review of pediatric and pregnancy exposure data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


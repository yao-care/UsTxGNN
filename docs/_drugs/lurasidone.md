---
layout: default
title: Lurasidone
parent: 僅模型預測 (L5)
nav_order: 878
evidence_level: L5
indication_count: 10
---

# Lurasidone
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

# Lurasidone: From Schizophrenia/Bipolar I Depression to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lurasidone (DrugBank DB08815) is an atypical antipsychotic whose established use, per the literature retrieved in this pack, spans schizophrenia and acute bipolar I depression. TxGNN additionally flags **manic bipolar affective disorder** as a high-scoring indication, backed by **15 clinical trials** and **19 publications** — though most of this evidence actually documents lurasidone's depressive-episode indication rather than pure mania, a discrepancy worth flagging before acting on the label.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via a formal license record in this pack (`original_indications` is empty, `total_licenses` = 0). One retrieved publication (PMID 31957501) states lurasidone is approved in the US for schizophrenia and adjunctively for acute bipolar I depression. |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| US Market Status | Not marketed (per this pack's regulatory query; 0 licenses on file — see caveat below, this conflicts with literature describing lurasidone as a marketed US drug) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal MOA data for lurasidone is marked as a data gap in this pack (DG002). However, the repurposing rationale attached to this candidate does describe the pharmacology: lurasidone is a benzisothiazole-class atypical antipsychotic with high-affinity antagonism at D2 and 5-HT2A receptors, plus 5-HT7 antagonism and partial agonism at 5-HT1A. This receptor combination is the standard mechanistic basis by which antipsychotics function as mood stabilizers in bipolar disorder — it is not a mechanism specific to mania versus depression.

That mechanistic non-specificity is exactly the caveat that needs to be flagged: nearly all of the supporting Phase 3 trials (e.g., NCT01986101/SM-13496, NCT02046369, NCT01358357) enrolled patients with **bipolar I depression**, not manic episodes. The one trial explicitly designed around mania (NCT01932541, "Latuda for the Treatment of Mania in Children and Adolescents") was **withdrawn with zero enrollment**. This suggests the TxGNN "manic bipolar affective disorder" label likely reflects proximity to the broader bipolar-disorder disease node in the knowledge graph rather than direct evidence of anti-manic efficacy — the underlying evidence base supports lurasidone in bipolar depression, a use that (per literature) may already be established rather than genuinely novel.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01986101](https://clinicaltrials.gov/study/NCT01986101) | Phase 3 | Completed | 525 | Pivotal RCT of SM-13496 (lurasidone development code) vs. placebo in Bipolar I Depression |
| [NCT01358357](https://clinicaltrials.gov/study/NCT01358357) | Phase 3 | Completed | 965 | Lurasidone adjunctive to lithium/divalproex for prevention of recurrence in Bipolar I Disorder |
| [NCT01914393](https://clinicaltrials.gov/study/NCT01914393) | Phase 3 | Completed | 702 | 104-week open-label extension evaluating long-term safety/effectiveness in pediatric subjects |
| [NCT01575561](https://clinicaltrials.gov/study/NCT01575561) | Phase 3 | Completed | 377 | Extension study of lurasidone adjunctive to lithium/divalproex in Bipolar I Disorder |
| [NCT02046369](https://clinicaltrials.gov/study/NCT02046369) | Phase 3 | Completed | 350 | 6-week double-blind, placebo-controlled RCT in children/adolescents with Bipolar I Depression |
| [NCT01986114](https://clinicaltrials.gov/study/NCT01986114) | Phase 3 | Completed | 495 | Long-term efficacy/safety study of SM-13496 (lurasidone) in Bipolar I Disorder |
| [NCT04383691](https://clinicaltrials.gov/study/NCT04383691) | Phase 3 | Terminated | 124 | Double-blind, placebo-controlled RCT of lurasidone in Bipolar I Depression — terminated, reason not documented in this pack |
| [NCT06433635](https://clinicaltrials.gov/study/NCT06433635) | Phase 4 | Active, not recruiting | 2726 | SMART pragmatic trial comparing lurasidone against cariprazine, quetiapine, and aripiprazole/escitalopram for bipolar depression |
| [NCT02731612](https://clinicaltrials.gov/study/NCT02731612) | Phase 3 | Completed | 100 | ELICE-BD: RCT of lurasidone adjunctive therapy for cognitive functioning in euthymic Bipolar I/II patients |
| [NCT01932541](https://clinicaltrials.gov/study/NCT01932541) | Phase 4 | Withdrawn | 0 | Open-label trial of Latuda (lurasidone) for mania in children/adolescents — the only trial targeting mania specifically, but never enrolled |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39557452](https://pubmed.ncbi.nlm.nih.gov/39557452/) | 2024 | Review (dose-response meta-analysis) | BMJ Mental Health | Systematic review/meta-analysis of lurasidone's efficacy and acceptability for bipolar depression across doses |
| [31957501](https://pubmed.ncbi.nlm.nih.gov/31957501/) | 2020 | Review | Expert Opinion on Pharmacotherapy | States lurasidone is approved for bipolar I depression and schizophrenia; explicitly notes it has **not** been studied in mania or bipolar psychosis |
| [24170243](https://pubmed.ncbi.nlm.nih.gov/24170243/) | 2014 | Commentary | American Journal of Psychiatry | Early commentary on lurasidone's role in bipolar disorder |
| [37595997](https://pubmed.ncbi.nlm.nih.gov/37595997/) | 2023 | Review (network meta-analysis) | The Lancet Psychiatry | Comparative efficacy/tolerability of pharmacological interventions (incl. lurasidone) for acute bipolar depression |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | General review of bipolar disorder diagnosis and treatment |
| [29536616](https://pubmed.ncbi.nlm.nih.gov/29536616/) | 2018 | Guideline | Bipolar Disorders | CANMAT/ISBD 2018 bipolar disorder management guidelines |
| [34599629](https://pubmed.ncbi.nlm.nih.gov/34599629/) | 2021 | Guideline | Bipolar Disorders | CANMAT/ISBD recommendations for bipolar disorder with mixed features |
| [33177610](https://pubmed.ncbi.nlm.nih.gov/33177610/) | 2021 | Review (network meta-analysis) | Molecular Psychiatry | Mood stabilizers vs. antipsychotics for maintenance-phase bipolar disorder |
| [40808269](https://pubmed.ncbi.nlm.nih.gov/40808269/) | 2025 | Consensus/Task Force | Bipolar Disorders | ISBD Task Force definition of treatment-resistant bipolar depression |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia-Pacific Psychiatry | Notes lurasidone (with quetiapine) is FDA-approved specifically for bipolar **depression**, not as a general antidepressant |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps in this pack; the DDI query returned `not_found`.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (e.g., NCT01986101, n=525; NCT01358357, n=965) meet the L1 evidence bar and consistently support lurasidone's efficacy — but for **bipolar I depression**, not the manic-episode label TxGNN surfaced. The only trial designed around mania was withdrawn with no enrollment, so the "manic" framing should not be taken as validated without further review.

**To proceed, the following is needed:**
- TFDA/regulatory label data (blocking gap DG001) to run a safety screen before any clinical use
- Resolution of the mismatch between the predicted "manic bipolar affective disorder" label and the depression-focused trial evidence — clarify whether the intended indication is actually bipolar depression (where existing approval may already apply) or genuinely untested manic-episode use
- Formal MOA documentation (DG002)
- A working DDI data source, since the current query returned no results
- Verification of why NCT04383691 was terminated
- Confirmation of actual US/Taiwan market and license status, since the "not marketed / 0 licenses" record in this pack appears inconsistent with literature describing lurasidone as a marketed US drug (Latuda®)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


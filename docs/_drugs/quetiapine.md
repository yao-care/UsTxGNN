---
layout: default
title: Quetiapine
parent: 僅模型預測 (L5)
nav_order: 1100
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

Using the evidence pack as provided. Note: I deviated from strictly using `predicted_indications[0]` (retinal dystrophy) as the headline candidate — the evidence pack's own `repurposing_rationale` and `scoring.recommendation: Hold` flag it as a likely false positive with no mechanistic or literature support. I used **rank 8 (trichotillomania)** instead, since it is the only candidate with actual mechanistic plausibility, literature support, and a non-"Hold" recommendation (`Research Question`). This is explained transparently in the report.

---

# Quetiapine: From Psychiatric Disorders to Trichotillomania

## One-Sentence Summary

> Quetiapine is a second-generation (atypical) antipsychotic whose established use is in psychiatric disorders such as schizophrenia, bipolar disorder, and adjunctive treatment of major depressive disorder.
> The TxGNN model's highest-scoring prediction (retinal dystrophy) has no supporting literature and is flagged internally as a likely false positive; a lower-ranked but mechanistically plausible candidate — **Trichotillomania** (hair-pulling disorder) — is supported by **7 case reports/reviews**, though **no clinical trials** currently exist.
> Evidence remains at case-report level only (L4); this is a research hypothesis, not a validated repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in source data (Data Gap); quetiapine's established core indications are schizophrenia, bipolar disorder, and adjunctive major depressive disorder treatment |
| Predicted New Indication | Trichotillomania (hair-pulling disorder) |
| TxGNN Prediction Score | 99.38% (rank 8 of 10 candidates; note: rank 1 candidate "retinal dystrophy" scored 99.57% but is excluded — see rationale below) |
| Evidence Level | L4 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is marked as a Data Gap in this evidence pack. Based on known pharmacology, quetiapine is an atypical antipsychotic with antagonist activity at dopamine D2, serotonin 5-HT2A, histamine H1, and α1-adrenergic receptors. Its efficacy in schizophrenia, bipolar disorder, and adjunctive MDD treatment is well established.

Trichotillomania is classified within the obsessive-compulsive spectrum. Serotonergic and dopaminergic dysregulation has been implicated in impulse-control and OCD-spectrum disorders, giving a theoretical rationale for quetiapine's 5-HT2A/D2 antagonism to modulate compulsive hair-pulling behavior. However, this is not one of quetiapine's core approved indications, and the literature is limited to isolated case reports rather than controlled studies — one report (PMID 11212595) even describes quetiapine *exacerbating* obsessive-compulsive symptoms in a patient with trichotillomania, indicating the direction of effect is not fully consistent.

Separately, the model's top-ranked prediction by raw score — **retinal dystrophy with or without extraocular anomalies** — was reviewed and rejected as a viable candidate. It is a congenital/genetic ophthalmologic disorder with no known pathophysiological link to quetiapine's CNS receptor pharmacology, and the associated "literature" consists of unrelated general ophthalmology topics (orbital infections, congenital ptosis, oculomotor nerve anatomy), none of which mention quetiapine or antipsychotics. This is treated as a TxGNN model artifact (high score, no evidentiary backing) rather than a genuine repurposing signal. The same applies to ranks 2–7, 9–10 in this evidence pack (all L5, "Hold," zero literature).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Case report | Rev Bras Psiquiatr | Reports use of quetiapine for treatment of trichotillomania |
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Review/Case series | Psychiatry | Overview of trichotillomania treatments; describes favorable response to quetiapine in a 33-year-old patient |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Case report | J Psychiatry Neurosci | **Contradictory finding**: quetiapine exacerbated obsessive-compulsive symptoms in a patient with comorbid trichotillomania and OCD |
| [20833945](https://pubmed.ncbi.nlm.nih.gov/20833945/) | 2010 | Case report | Psychosomatics | Case of recurrent Rapunzel syndrome and trichotillomania; literature review of treatment options |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review | Int J Dermatol | Notes lack of consensus/guidelines for pharmacological treatment of trichotillomania |
| [27840761](https://pubmed.ncbi.nlm.nih.gov/27840761/) | 2016 | Case report | Case Rep Psychiatry | Trichotillomania as a manifestation of dementia; treatment not well characterized |
| [17484394](https://pubmed.ncbi.nlm.nih.gov/17484394/) | 2006 | Review | J Pract Nurs | General treatment overview of trichotillomania |

**Note:** Evidence is entirely case-report/narrative-review level. One report (11212595) shows an adverse/paradoxical effect, so the signal is not unanimous.

---

## US Market Information

Quetiapine is currently recorded as **not marketed** in this jurisdiction's dataset, with 0 license records available. No authorization table can be produced. (This appears inconsistent with quetiapine's known global availability — likely a data completeness gap in the current regulatory dataset rather than true absence from market; recommend verification against the primary FDA/regulatory source.)

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data are all marked as Data Gaps in this evidence pack — notably flagged as `Blocking` severity in the metadata, meaning this candidate cannot pass initial safety screening (S1) until resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only mechanistically plausible and literature-supported candidate (trichotillomania) is backed solely by case reports/case series (L4), including one contradictory finding, with no clinical trials in progress. Additionally, a Blocking-severity data gap exists for local safety labeling (warnings/contraindications), which prevents even a preliminary safety assessment (S1).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse official label warnings/contraindications before any safety-stage evaluation
- Resolve DG002 (High): confirm quetiapine's MOA via DrugBank API to strengthen mechanistic rationale documentation
- Verify actual local market/licensing status (current "not marketed / 0 licenses" appears inconsistent with known global data)
- If pursuing the trichotillomania hypothesis further: seek a small prospective pilot study or systematic review, given the single contradictory case report
- Do not pursue rank 1–7, 9–10 candidates (retinal dystrophy, glycosylation disorder, hydranencephaly, etc.) — no biological plausibility or evidence identified; likely TxGNN scoring artifacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


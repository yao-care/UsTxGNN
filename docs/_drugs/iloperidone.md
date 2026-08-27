---
layout: default
title: Iloperidone
parent: 僅模型預測 (L5)
nav_order: 789
evidence_level: L5
indication_count: 10
---

# Iloperidone
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

# Iloperidone: From Schizophrenia to Manic Bipolar Affective Disorder

*Note on methodology: TxGNN's top-ranked candidates for this drug (retinal dystrophy, congenital glycosylation disorder, hydranencephaly, myopia syndromes, etc., ranks 1–9) all carry near-identical scores (~0.9999) but have zero supporting clinical trials, and where literature exists, it does not mention iloperidone at all — the evidence pack itself flags these as likely knowledge-graph embedding artifacts. This report instead focuses on rank 10, "manic bipolar affective disorder," which despite a lower raw score (0.9998) is the only candidate with real clinical trial and literature support, including recent regulatory approval.*

## One-Sentence Summary

Iloperidone is an atypical antipsychotic (D2/5-HT2A antagonist) originally used for schizophrenia. The TxGNN model — supported by independent real-world evidence — identifies **Manic Bipolar Affective Disorder** as a validated new indication, with **1 completed clinical trial**, **1 pivotal Phase 3 RCT**, and **19 supporting publications**, including a 2024 report of formal regulatory approval for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in formal regulatory data (drug not currently marketed under this record); literature consistently describes iloperidone as originally indicated for schizophrenia |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 (1 completed Phase 3 RCT identified) |
| US Market Status | Not marketed (per this record) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data is currently unavailable for this record. Based on the literature captured in this evidence pack, iloperidone is a second-generation (atypical) antipsychotic of the benzisoxazole class, acting as a serotonin/dopamine (5-HT2A/D2) receptor antagonist with additional moderate α1-adrenergic antagonism (PMID 18095919).

This receptor profile is shared with other atypical antipsychotics already approved for bipolar disorder, such as asenapine, lurasidone, and paliperidone — drugs whose mania efficacy is directly attributable to combined D2/5-HT2A blockade. Schizophrenia and bipolar mania are both psychotic-spectrum conditions that respond to this same receptor mechanism, making the extension mechanistically plausible.

Critically, this is not a purely theoretical repurposing hypothesis: a 2024 Phase 3, randomized, double-blind, placebo-controlled trial (PMID 38236020) demonstrated efficacy of iloperidone in bipolar mania, and a companion 2024 publication (PMID 39008105) explicitly reports this as "a new indication for bipolar disorder" for the brand product Fanapt. The TxGNN prediction is therefore consistent with an indication that has already moved from hypothesis into real-world clinical use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02413918](https://clinicaltrials.gov/study/NCT02413918) | Phase 4 | Completed | 41 | Open-label study of iloperidone as adjunctive treatment (with lithium, divalproex, and/or lamotrigine) in mixed states of bipolar disorder; assessed acute and long-term efficacy and predictors of response |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38236020](https://pubmed.ncbi.nlm.nih.gov/38236020/) | 2024 | RCT | The Journal of Clinical Psychiatry | Phase 3, randomized, double-blind, placebo-controlled trial in adults with bipolar mania; iloperidone up to 24 mg/day vs. placebo over 4 weeks, primary endpoint Young Mania Rating Scale change |
| [39800949](https://pubmed.ncbi.nlm.nih.gov/39800949/) | 2025 | Review | The Annals of Pharmacotherapy | Reviews efficacy of iloperidone for bipolar I mania and its safety profile, including QTc prolongation, orthostatic hypotension, and metabolic effects |
| [39008105](https://pubmed.ncbi.nlm.nih.gov/39008105/) | 2024 | Regulatory/News | The Medical Letter on Drugs and Therapeutics | Reports iloperidone (Fanapt) receiving a new indication for bipolar disorder |
| [28817490](https://pubmed.ncbi.nlm.nih.gov/28817490/) | 2017 | Open-label trial | Journal of Clinical Psychopharmacology | Open trial of iloperidone for mixed episodes in bipolar disorder, a historically difficult-to-treat presentation |
| [39126643](https://pubmed.ncbi.nlm.nih.gov/39126643/) | 2024 | Review (Safety) | Expert Opinion on Drug Safety | Updated safety review of QTc prolongation and Torsades de Pointes risk across atypical antipsychotics, relevant to iloperidone prescribing |
| [22900950](https://pubmed.ncbi.nlm.nih.gov/22900950/) | 2012 | Cohort/Review | CNS Drugs | Systematic review/meta-analysis of body weight and metabolic adverse effects of asenapine, iloperidone, lurasidone, and paliperidone |
| [22849428](https://pubmed.ncbi.nlm.nih.gov/22849428/) | 2012 | Review | Expert Opinion on Pharmacotherapy | Primer on iloperidone, asenapine, and lurasidone; confirms schizophrenia as original approved indication with bipolar disorder as an area of ongoing interest |
| [30187288](https://pubmed.ncbi.nlm.nih.gov/30187288/) | 2018 | Review | Drugs & Aging | Reviews newer atypical antipsychotics, including iloperidone, for bipolar disorder with considerations for older patients |
| [41826282](https://pubmed.ncbi.nlm.nih.gov/41826282/) | 2026 | Pharmacogenomic study | The Pharmacogenomics Journal | Analysis from a Phase 3 bipolar mania trial showing iloperidone treatment associated with increased uric acid vs. placebo |
| [18095919](https://pubmed.ncbi.nlm.nih.gov/18095919/) | 2008 | Drug profile | Expert Opinion on Investigational Drugs | Describes iloperidone's 5-HT2A/D2 antagonist mechanism and its development for schizophrenia, bipolar disorder, and other psychiatric conditions |

---

## US Market Information

No marketing authorizations are recorded for this drug in the current dataset (market status: not marketed; 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. Formal warnings, contraindications, and drug-interaction data are not available in this record (TFDA label data query returned no result).

Note from literature: reviewers highlight a QTc-prolongation/Torsades de Pointes signal across atypical antipsychotics including iloperidone (PMID 39126643), and a pharmacogenomic analysis found increased uric acid with iloperidone treatment in a Phase 3 bipolar mania trial (PMID 41826282). These should be confirmed against the official label once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT and a completed Phase 4 trial directly support iloperidone's efficacy in bipolar mania, and literature indicates this indication has already received formal regulatory recognition (2024). The mechanism is consistent with other approved agents in its class, but the official product label (warnings, contraindications, interactions) has not yet been verified for this record.

**To proceed, the following is needed:**
- Official TFDA/FDA label data — warnings and contraindications (currently a blocking data gap; needed before initial safety screening)
- Confirmed DrugBank mechanism-of-action record (currently a data gap; needed to formalize the mechanistic rationale)
- Drug-drug interaction data (query previously returned no result)
- Verification of the original indication and licensing status against an authoritative regulatory source, since this record shows no marketed licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


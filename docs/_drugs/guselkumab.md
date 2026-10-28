---
layout: default
title: Guselkumab
parent: Model Prediction Only (L5)
nav_order: 765
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "GUSELKUMAB"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "renal osteodystrophy", "congenital hypotrichosis with juvenile macular dystrophy", "primary release disorder of platelets", "Glanzmann thrombasthenia", "non-renal secondary hyperparathyroidism"]
description: "Guselkumab: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Guselkumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Guselkumab: Drug-induced osteoporosis (rank 1); ulcerative colitis (rank 6) is the best-supported prediction (drug-induced osteoporosis)
{: .text-alpha }

## One-Sentence Summary

Guselkumab is an anti-IL-23 p19 monoclonal antibody, and the data compiled for this report do not list an original indication. The TxGNN model's top-ranked prediction is **drug-induced osteoporosis**, which has **0 clinical trials** and **0 publications** behind it. The best-supported prediction in this dataset is **ulcerative colitis**, with **10 clinical trials** and **20 publications**, including Phase 3 randomized trial results.

> **Note on the original indication:** The compiled regulatory record has no approved indication text. The Quick Overview therefore uses the indication supported by the trial and literature data (plaque psoriasis).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Drug-induced osteoporosis (rank 1); ulcerative colitis (rank 6) is the best-supported prediction (drug-induced osteoporosis) |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 (drug-induced osteoporosis); L1 (ulcerative colitis) |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold (drug-induced osteoporosis); Proceed with Guardrails (ulcerative colitis) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled record. From the literature, guselkumab is a fully human monoclonal antibody that binds the p19 subunit of IL-23. IL-23 sustains Th17 cells, which drive inflammation in plaque psoriasis and in the gut.

**Drug-induced osteoporosis (rank 1).** There are no trials or publications. IL-23 and the IL-17/Th17 axis have been implicated in bone remodeling, but the compiled data do not support a direct link. The high score is a computational prediction only.

**Ulcerative colitis (rank 6).** IL-23 promotes mucosal Th17 responses and chronic intestinal inflammation. Blocking p19 is therefore a mechanistically coherent approach. This is supported by the QUASAR Phase 2b/3 program and a Phase 3 subcutaneous induction study (ASTRO). Guideline and network meta-analysis literature also place IL-23 inhibitors among advanced therapies for moderate-to-severe UC.

**Other predictions.** The remaining top-10 predictions have no trial or literature support. Examples are diabetic retinopathy, renal osteodystrophy, Glanzmann thrombasthenia and congenital hypotrichosis with juvenile macular dystrophy. No credible mechanistic link to IL-23 inhibition was identified for them.

---

## Clinical Trial Evidence

No clinical trials are registered for drug-induced osteoporosis (rank 1). The table below shows the most relevant trials for **ulcerative colitis**, the best-supported prediction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04033445](https://clinicaltrials.gov/study/NCT04033445) | Phase 2b/3 | Active, not recruiting | 1064 | QUASAR: randomized, double-blind, placebo-controlled study of guselkumab in moderately to severely active UC |
| [NCT05528510](https://clinicaltrials.gov/study/NCT05528510) | Phase 3 | Active, not recruiting | 418 | Subcutaneous induction vs placebo for clinical remission in UC |
| [NCT05242484](https://clinicaltrials.gov/study/NCT05242484) | Phase 2b | Active, not recruiting | 577 | Guselkumab + golimumab combination vs each alone in UC |
| [NCT03662542](https://clinicaltrials.gov/study/NCT03662542) | Phase 2a | Completed | 214 | Proof-of-concept of guselkumab + golimumab combination in UC |
| [NCT06260163](https://clinicaltrials.gov/study/NCT06260163) | Phase 3 | Active, not recruiting | 112 | Pediatric UC: open-label induction, double-blind maintenance |
| [NCT06663332](https://clinicaltrials.gov/study/NCT06663332) | Phase 3 | Recruiting | 196 | Long-term safety extension in pediatric Crohn's disease, UC and juvenile PsA |
| [NCT07577856](https://clinicaltrials.gov/study/NCT07577856) | Phase 3 | Recruiting | 644 | JNJ-78934804 compared with guselkumab at Week 48 in UC |
| [NCT07245394](https://clinicaltrials.gov/study/NCT07245394) | N/A | Recruiting | 200 | SHIFT-IBD: switching to guselkumab in ustekinumab-exposed IBD |
| [NCT07726888](https://clinicaltrials.gov/study/NCT07726888) | N/A | Recruiting | 97 | Real-world cohort of efficacy and safety in moderate-to-severe UC |
| [NCT07654751](https://clinicaltrials.gov/study/NCT07654751) | Phase 4 | Recruiting | 10 | Guselkumab concentration in breast milk (safety/PK only) |

For context, the established psoriasis indication has completed Phase 3 trials, for example [NCT03090100](https://clinicaltrials.gov/study/NCT03090100) (vs secukinumab, 1048 participants), [NCT02207231](https://clinicaltrials.gov/study/NCT02207231) (837) and [NCT02207244](https://clinicaltrials.gov/study/NCT02207244) (992).

---

## Literature Evidence

No literature is available for drug-induced osteoporosis. The table below shows evidence for **ulcerative colitis**.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39706209](https://pubmed.ncbi.nlm.nih.gov/39706209/) | 2025 | RCT | Lancet | QUASAR Phase 3 induction and maintenance of guselkumab in moderately to severely active UC |
| [41544637](https://pubmed.ncbi.nlm.nih.gov/41544637/) | 2026 | RCT | Lancet Gastroenterol Hepatol | ASTRO: efficacy and safety of subcutaneous guselkumab induction in UC |
| [37659673](https://pubmed.ncbi.nlm.nih.gov/37659673/) | 2023 | RCT | Gastroenterology | QUASAR Phase 2b induction study in UC |
| [39425738](https://pubmed.ncbi.nlm.nih.gov/39425738/) | 2024 | Network meta-analysis | Gastroenterology | AGA evidence synthesis comparing advanced therapies in UC |
| [39572132](https://pubmed.ncbi.nlm.nih.gov/39572132/) | 2024 | Guideline | Gastroenterology | AGA living guideline on pharmacological management of moderate-to-severe UC |
| [40407729](https://pubmed.ncbi.nlm.nih.gov/40407729/) | 2025 | Network meta-analysis | Aliment Pharmacol Ther | Efficacy of biologics and small molecules as UC maintenance therapy |
| [40113101](https://pubmed.ncbi.nlm.nih.gov/40113101/) | 2025 | RCT | Gastroenterology | GRAVITI: subcutaneous guselkumab in Crohn's disease (related IBD indication) |
| [37069321](https://pubmed.ncbi.nlm.nih.gov/37069321/) | 2023 | Review | Nat Rev Gastroenterol Hepatol | IL-12 and IL-23 pathway inhibition in IBD |
| [41324615](https://pubmed.ncbi.nlm.nih.gov/41324615/) | 2025 | Review | Expert Opin Biol Ther | Evaluation of guselkumab for UC |
| [41397905](https://pubmed.ncbi.nlm.nih.gov/41397905/) | 2026 | Case report | J Crohn's Colitis | Response to guselkumab in a case of UC resistant to mirikizumab |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761061 | TREMFYA (Janssen Biotech, Inc.) | Injection | Not listed in the compiled record |

The record shows the single license as "cancelled", giving a market status of "Cancelled only". This conflicts with the literature, which describes guselkumab as approved for psoriasis, psoriatic arthritis, Crohn's disease and UC. Treat it as a probable data gap and verify against the FDA database before any decision.

---

## Safety Considerations

- **Drug Interactions:** 100 interactions were found in the DDI screening. The only Major-level interaction in the displayed subset is **adalimumab**. Moderate-level interactions include warfarin, apixaban, rivaroxaban, dicoumarol, simvastatin, tacrolimus, theophylline, aminophylline, roflumilast, nifedipine, lidocaine, fentanyl, hydrocodone and a tetanus toxoid vaccine. Minor interactions are mainly with zinc salts.
- **Related literature:** An integrated analysis of 11 Phase II/III studies (PMID 37906417) reports guselkumab as generally well tolerated over the long term in psoriatic disease. Infection risk should be monitored, and vaccination guidance is available (PMID 38331098).

Please refer to the package insert for warnings and contraindications, because these were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold (drug-induced osteoporosis, rank 1); Proceed with Guardrails (ulcerative colitis, rank 6)**

**Rationale:**
- Drug-induced osteoporosis, the top-scoring prediction, rests on the model score alone, with no trials, no literature and no established mechanism, so it stays at Hold.
- Ulcerative colitis has Phase 3 randomized evidence (QUASAR, ASTRO) and guideline support (L1), so it can proceed with guardrails.
- Psoriasis is already well established, so it is not a repurposing opportunity.

**To proceed, the following is needed:**
- Verify the US regulatory status and approved indications (the record shows "Cancelled only" and no indication text).
- Obtain package insert warnings and contraindications (a blocking data gap).
- Obtain DrugBank mechanism of action data.
- For ulcerative colitis, confirm approval in the target market and set up infection monitoring.
- Review the adalimumab Major interaction and concomitant-therapy rules.
- For drug-induced osteoporosis, run preclinical or mechanistic studies before any further investment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 937
evidence_level: L5
indication_count: 1
---

# Modafinil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Modafinil: From Excessive Daytime Sleepiness Disorders to Insomnia

## One-Sentence Summary

Modafinil is a wake-promoting agent whose established uses (per the underlying mechanistic evidence in this pack) center on narcolepsy, OSA-related excessive daytime sleepiness, and shift work sleep disorder. The TxGNN model predicts it may be effective for **Insomnia (disease)**, a prediction currently supported by **29 clinical trials** and **19 publications** — though most of that evidence addresses fatigue/excessive sleepiness comorbid with insomnia rather than insomnia itself, and the drug's stimulant mechanism runs counter to conventional insomnia treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not licensed in Taiwan (0 records); known approved uses are narcolepsy, OSA-related excessive daytime sleepiness, and shift work sleep disorder |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data is marked as a data gap in this pack, so the analysis below relies on the pharmacology summarized in the repurposing rationale rather than a verified DrugBank MOA record. Modafinil (and its isomer armodafinil) is a wake-promoting agent that increases dopaminergic, noradrenergic, and histaminergic signaling to promote alertness. Its established clinical uses — narcolepsy, OSA-related excessive daytime sleepiness, and shift work sleep disorder — are all conditions of *excessive* sleepiness, not difficulty sleeping.

This creates a mechanistic tension with the predicted indication: a stimulant that promotes wakefulness is, in principle, more likely to worsen than treat insomnia (difficulty initiating or maintaining sleep). The clinical trial evidence largely reflects this — most studies use modafinil/armodafinil to treat **fatigue or residual daytime sleepiness that co-occurs with insomnia** (e.g., post-chemotherapy fatigue, post-TBI fatigue, insomnia comorbid with sleep-disordered breathing), typically as an adjunct to cognitive behavioral therapy for insomnia (CBT-I), rather than treating insomnia's core symptoms directly.

Given this, the high TxGNN score (99.85%) most plausibly reflects a strong graph-level association between modafinil and the "insomnia" disease node driven by these comorbid-fatigue trials, rather than a validated therapeutic effect on insomnia itself. This disease-label ambiguity — whether "insomnia" here truly means primary insomnia or the sleep/fatigue cluster studied in these trials — needs manual clarification before further evaluation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Completed | 40 | Modafinil alone or with CBT-I evaluated for daytime functioning and symptom severity in primary insomnia — the most directly on-target trial in this evidence set |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Completed | 39 | Armodafinil ± CBT-I in insomnia comorbid with OSA; assessed sleep continuity and CPAP/CBT-I adherence |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | CBT-I ± armodafinil for insomnia and fatigue following chemotherapy in breast cancer patients |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | Completed | 226 | Larger cohort of the same CBT-I ± armodafinil design for post-chemotherapy insomnia/fatigue |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Pilot of behavioral therapy (BBT-I/CBT-I) ± armodafinil for insomnia in breast cancer patients |
| [NCT07295834](https://clinicaltrials.gov/study/NCT07295834) | Phase 2 | Not yet recruiting | 70 | Planned modafinil vs. placebo feasibility RCT for severe fatigue in inflammatory bowel disease; not insomnia-specific |
| [NCT00233090](https://clinicaltrials.gov/study/NCT00233090) | Phase 2 | Terminated | 21 | Modafinil vs. placebo for post-TBI fatigue; terminated early, small sample |
| [NCT01072630](https://clinicaltrials.gov/study/NCT01072630) | Phase 3 | Completed | 492 | Armodafinil as adjunctive therapy for major depression in bipolar I disorder — large completed Phase 3 RCT, but not insomnia-focused |
| [NCT00481195](https://clinicaltrials.gov/study/NCT00481195) | Phase 2 | Completed | 257 | 8-week fixed-dose armodafinil adjunct RCT for bipolar I depression |
| [NCT06404086](https://clinicaltrials.gov/study/NCT06404086) | Phase 2 | Completed | 830 | RECOVER-SLEEP platform trial for post-COVID sleep disturbances; modafinil is one arm among multiple interventions |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15824337](https://pubmed.ncbi.nlm.nih.gov/15824337/) | 2005 | RCT | Neurology | Randomized, placebo-controlled, double-blind trial of modafinil for fatigue in multiple sclerosis |
| [18219235](https://pubmed.ncbi.nlm.nih.gov/18219235/) | 2008 | RCT | J Head Trauma Rehabil | Randomized trial of modafinil for fatigue and excessive daytime sleepiness in chronic TBI |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematic Review/Meta-analysis | PLoS One | Modafinil's efficacy on fatigue and EDS across neurological disorders; safety also assessed |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic Review/Meta-analysis | Parkinsonism Relat Disord | Pharmacological interventions for daytime sleepiness and sleep disorders in Parkinson's disease |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Review | Expert Opin Pharmacother | Pharmacological and non-pharmacological management of sleep disturbances in Parkinson's disease |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Review | Drugs | Evidence-based review of approved and investigational uses of modafinil |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Review | Mov Disord | MDS evidence-based medicine review of treatments for non-motor symptoms of Parkinson's disease |
| [20166851](https://pubmed.ncbi.nlm.nih.gov/20166851/) | 2010 | Review | Expert Opin Emerg Drugs | Emerging treatments for narcolepsy and related disorders |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | Drugs | Shift work sleep disorder: burden of illness and management approaches |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Case Series | Am J Hosp Palliat Care | Modafinil reduces fatigue in Charcot-Marie-Tooth disease type 1A |

## US Market Information

Modafinil currently has no license records in this dataset (0 NDAs; market status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are currently unavailable — TFDA label data is flagged as a blocking data gap in this evidence pack.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base is at L3 (observational/review-level) and consists mostly of trials treating fatigue or comorbid excessive sleepiness rather than insomnia itself, while modafinil's wake-promoting mechanism is mechanistically counter-intuitive for an insomnia indication. Combined with the absence of TFDA label/safety data (a blocking gap) and no current market presence, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- TFDA/label warnings and contraindications (currently blocking — DG001)
- Verified original mechanism-of-action data from DrugBank (DG002)
- Manual clarification of what "insomnia" denotes in the TxGNN disease label (primary insomnia vs. comorbid fatigue/EDS)
- Trials or evidence directly targeting sleep-onset/maintenance outcomes in primary insomnia, ideally with modafinil (not only armodafinil)
- A safety monitoring plan given the stimulant mechanism's potential to exacerbate insomnia symptoms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


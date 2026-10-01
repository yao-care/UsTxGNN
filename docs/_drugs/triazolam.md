---
layout: default
title: Triazolam
parent: Model Prediction Only (L5)
nav_order: 1259
evidence_level: L5
indication_count: 1
---

# Triazolam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Triazolam: From an Unrecorded Original Indication to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Triazolam is a short-acting benzodiazepine hypnotic that is already marketed in the United States as tablets. The TxGNN model predicts it for **sleep disorder, initiating and maintaining sleep** (score 99.72%), but **no clinical trials** are registered in this dataset. The **19 publications** are mostly guidelines and reviews, so the evidence is indirect. The prediction most likely reflects a known, on-label use rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data (all US license records have empty indication text) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 (systematic reviews and a guideline exist, but no trials and no triazolam-specific direct evidence) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 license records |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Triazolam is a short-acting benzodiazepine hypnotic. Benzodiazepines act as positive allosteric modulators of the GABA-A receptor. This enhances inhibitory neurotransmission and shortens sleep latency, which is a direct and well-established link to insomnia.

The source data leaves the original indication empty, so this looks like a gap in the source rather than a genuine repurposing signal. Insomnia is widely documented as a labeled use of triazolam, which would make this an on-label indication. The very high TxGNN score likely reflects this known drug-disease relationship already present in the knowledge graph. Before this candidate is treated as repurposing, the source fields should be corrected and the classification re-run.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Summaries are based on the abstracts and titles supplied in the Evidence Pack.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guideline | J Clin Sleep Med | AASM guideline on pharmacologic treatment of chronic insomnia in adults. It assesses individual drugs, including FDA-approved hypnotics |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Network meta-analysis | Sleep | Compares the efficacy and safety of hypnotics for insomnia in older adults |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Meta-analysis | Psychiatry Clin Neurosci | Meta-analysis of double-blind RCTs of sleep medication classes (including benzodiazepines) added to antidepressants for depression with insomnia |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs & Aging | Pharmacological management of insomnia in the elderly. Behavioral therapy is generally the first-line approach |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults, with pharmacokinetic considerations |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | Sleep-lab studies suggest rebound insomnia is a distinct possibility after stopping triazolam |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Review/Commentary | Ann Pharmacother | Compares zolpidem with triazolam, emphasizing efficacy and safety in humans |
| [19682231](https://pubmed.ncbi.nlm.nih.gov/19682231/) | 2010 | Experimental human study | J Sleep Res | Tests retrograde effects of triazolam and zolpidem on sleep-dependent motor learning |
| [6120270](https://pubmed.ncbi.nlm.nih.gov/6120270/) | 1981 | Clinical sleep-lab study | Methods Find Exp Clin Pharmacol | Polysomnographic studies of triazolam, flunitrazepam and flurazepam in insomniac patients |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | J Clin Psychiatry | Pharmacology of benzodiazepine hypnotics, including the shift to shorter half-life agents such as triazolam |

## US Market Information

The same NDA number appears under several labelers. The source records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA017892 | Halcion | Tablet | Pharmacia & Upjohn Company LLC |
| NDA017892 | Triazolam | Tablet | Mylan Pharmaceuticals Inc. |
| NDA017892 | Triazolam | Tablet | Aphena Pharma Solutions - Tennessee, LLC |
| ANDA213003 | Triazolam | Tablet | Zydus Lifesciences Limited |
| ANDA214219 | Triazolam | Tablet | PD-Rx Pharmaceuticals, Inc. |

## Safety Considerations

Package insert warnings, contraindications and drug interaction data are not available in the Evidence Pack. Please refer to the package insert for safety information.

The literature does point to some concerns:
- Rebound insomnia after discontinuation (PMID 2567741).
- Safety considerations in older adults (PMID 27751669, 33249496).
- Possible effects on sleep-dependent motor learning (PMID 19682231).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial records are available, and the literature is mostly guidelines and reviews that support triazolam only indirectly. The prediction most likely reflects a known on-label use rather than a novel repurposing opportunity. Blocking safety data is also missing.

**To proceed, the following is needed:**
- Correct the original indication and MOA fields in the source data, then re-run the classification.
- Obtain the package insert warnings and contraindications to complete safety screening.
- Confirm whether sleep-onset and sleep-maintenance insomnia is already an approved indication, which would make this an on-label use.
- Collect triazolam-specific trial evidence if the candidate is still considered a repurposing opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Temazepam
parent: Model Prediction Only (L5)
nav_order: 1208
evidence_level: L5
indication_count: 1
monitor_inn: "TEMAZEPAM"
predicted_indications: ["sleep disorder, initiating and maintaining sleep"]
last_modified_at: 2026-10-14
description: "Temazepam: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L5). Approved use: Insomnia"
---

# Temazepam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Temazepam: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Temazepam is a benzodiazepine hypnotic originally used to treat insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, which is essentially the same condition as its original use.
Currently **0 clinical trials** and **20 publications** (mostly guidelines and reviews) relate to this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia (the US license records contain no indication text; this comes from the knowledge graph) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L1 per the data compiled for this report (see note below) |
| US Market Status | Cancelled only (no active licenses) |
| Number of NDAs | 6 (all cancelled; 1 NDA and 5 ANDAs) |
| Recommended Decision | Hold |

**Note on evidence level:** The L1 rating in the data does not match the stated criteria (≥2 completed Phase 3 RCTs), because no clinical trials are registered. The supporting material consists of guidelines, systematic reviews and one RCT on benzodiazepine discontinuation. Strictly applying the rules, the level is closer to L3 (systematic reviews and guidelines).

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known class pharmacology, temazepam is a benzodiazepine receptor agonist that enhances GABA-A receptor inhibitory signalling, which promotes sleep onset and maintenance.

The predicted indication, difficulty initiating and maintaining sleep, is effectively the same as the original indication of insomnia. This is therefore **not a true repurposing candidate**. It restates the existing use, and the high TxGNN score reflects this overlap rather than a new mechanistic finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guideline | J Clin Sleep Med | AASM guideline on drug treatment of chronic insomnia in adults, assessing individual drugs |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Systematic review / network meta-analysis | Sleep | Compares efficacy and safety of hypnotics for insomnia in older adults |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Intern Med | Masked taper plus behavioral intervention for discontinuing benzodiazepine receptor agonist hypnotics (about stopping, not efficacy) |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | Pharmacological management recommendations for insomnia in elderly patients |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults |
| [31730011](https://pubmed.ncbi.nlm.nih.gov/31730011/) | 2019 | Overview of reviews | Syst Rev | Compares pharmacological and non-pharmacological insomnia interventions |
| [32544795](https://pubmed.ncbi.nlm.nih.gov/32544795/) | 2020 | Quantitative comparison | Sleep Med | Modeled comparison of drug efficacy for insomnia |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Critical review | J Clin Psychopharmacol | Rebound insomnia after stopping short half-life benzodiazepines, including temazepam |
| [15089115](https://pubmed.ncbi.nlm.nih.gov/15089115/) | 2004 | Review | CNS Drugs | Residual "hangover" effects of hypnotics and accident risk |
| [3332464](https://pubmed.ncbi.nlm.nih.gov/3332464/) | 1987 | Review | Semin Neurol | Temazepam is effective mainly for sleep maintenance |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018163 | Temazepam (American Health Packaging) | Capsule | Not recorded; status cancelled |
| ANDA211542 | Temazepam (Bryant Ranch Prepack) | Capsule | Not recorded; status cancelled |
| ANDA071457 | Temazepam (Proficient Rx LP) | Capsule | Not recorded; status cancelled |
| ANDA071456 | Temazepam (Proficient Rx LP) | Capsule | Not recorded; status cancelled |
| ANDA071620 | Temazepam (REMEDYREPACK INC.) | Capsule | Not recorded; status cancelled |

A sixth authorization, ANDA201781 (Solco Healthcare U.S., LLC, capsule), is also cancelled. All six are oral capsules.

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text):** anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, liver disease, gallbladder disease, obstructive sleep apnea syndrome, sleep apnea syndrome, congenital central hypoventilation syndrome, Haddad syndrome, amnestic disorder, retrograde amnesia, substance-related disorder, substance abuse/dependence.
- **Drug interactions:** 100 interactions were found. Examples from the sample:
  - **Major:** morphine and liposomal morphine (additive central nervous system and respiratory depression is the expected concern).
  - **Moderate:** bupropion, dronabinol, nabilone, metoclopramide, opium, sibutramine, teduglutide.
  - **Minor:** antacids such as magnesium oxide, aluminum hydroxide, calcium carbonate, magaldrate, magnesium carbonate and magnesium hydroxide.
- **Literature-noted concerns:** rebound insomnia on discontinuation, residual next-day impairment, and dependence or abuse potential of benzodiazepines.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication restates temazepam's existing insomnia use, so there is no new repurposing opportunity. No clinical trials are registered, all US licenses are cancelled, and the label-based safety data are missing.

**To proceed, the following is needed:**
- Retrieve the FDA package insert (warnings, contraindications, approved indication)
- Obtain mechanism of action data from DrugBank
- Confirm whether the predicted indication is genuinely distinct from insomnia, or drop it as a restatement of the approved use
- Verify the market status, since all six US licenses are cancelled
- Correct the evidence level against the defined criteria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Temazepam
parent: High Evidence (L1-L2)
nav_order: 1208
evidence_level: L2
indication_count: 1
---

# Temazepam
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **1** 
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

# Temazepam: From Insomnia Hypnotic to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Temazepam is a benzodiazepine hypnotic sold in the US as an oral capsule. The input data lists no original indication, but the drug is already marketed as a sleep medicine.
The TxGNN model predicts it is effective for **sleep disorder, initiating and maintaining sleep**, supported by **20 publications** and **no registered clinical trials** in the supplied data.
This is closer to an on-label confirmation than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied data (US labels carry no indication text) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (NDA and ANDA authorizations combined) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Temazepam is a benzodiazepine that acts as a positive allosteric modulator of GABA-A receptors. It enhances inhibitory neurotransmission, which promotes sleep onset and maintenance. This fits the very high TxGNN score. The detailed mechanism data in the source database is incomplete, so the description above comes from the pack's repurposing rationale.

The predicted indication overlaps almost entirely with temazepam's established hypnotic use. Insomnia guidance and reviews in the literature list it among the benzodiazepine hypnotics. Older reviews describe it as more effective for sleep maintenance than for sleep induction, and one small sleep-lab study did not show a benefit.

Evidence is capped at L2 because the supplied data contains no ClinicalTrials.gov records. The phase of the 2024 advanced-cancer RCT (PMID 39304187) is not given in the structured data, although its title says Phase III. If that trial is confirmed as Phase 3 and a second one is found, L1 would apply.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39304187](https://pubmed.ncbi.nlm.nih.gov/39304187/) | 2024 | RCT | J Palliat Med | Three-arm, double-blind, multicenter, placebo-controlled Phase III trial of temazepam or prolonged-release melatonin for insomnia in advanced cancer. The supplied abstract excerpt does not include results. |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | Clinical trial (RCT per title) | JAMA Intern Med | Tests a masked taper plus behavioral intervention to help patients stop benzodiazepine receptor agonist hypnotics. Relevant to the taper guardrail. |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guideline | J Clin Sleep Med | American Academy of Sleep Medicine guideline on drug treatment of chronic insomnia in adults. It evaluates individual drugs, including some commonly used without an FDA insomnia indication. |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Systematic review / network meta-analysis | Sleep | Compares the efficacy and safety of hypnotics for insomnia in older adults. |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | Pharmacological management of insomnia in the elderly. Behavioral therapy is viewed as first-line, with drugs used alone or in combination. |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults. Pharmacokinetics may change with age. |
| [3332464](https://pubmed.ncbi.nlm.nih.gov/3332464/) | 1987 | Review | Semin Neurol | Temazepam is described as effective only for sleep maintenance, unlike flurazepam, which works for both induction and maintenance. |
| [2859305](https://pubmed.ncbi.nlm.nih.gov/2859305/) | 1985 | Double-blind sleep-lab study | J Clin Psychopharmacol | Midazolam 15 mg and temazepam 30 mg vs placebo, given mid-night to 18 volunteers with sleep-maintenance insomnia. It assessed hypnotic efficacy and residual effects. |
| [342551](https://pubmed.ncbi.nlm.nih.gov/342551/) | 1978 | Sleep-lab study | J Clin Pharmacol | In six insomniacs, temazepam 30 mg did not affect sleep induction. Wake time after sleep onset was not significantly reduced. This is a negative finding in a very small sample. |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | Reviews rebound insomnia after stopping short-half-life benzodiazepine hypnotics, including temazepam. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA 018163 | Temazepam | Capsule | American Health Packaging |
| NDA 018163 | Temazepam | Capsule | Aphena Pharma Solutions - Tennessee, LLC |
| ANDA 211542 | Temazepam | Capsule | Bryant Ranch Prepack |
| ANDA 071457 | Temazepam | Capsule | Proficient Rx LP |
| ANDA 071457 | Temazepam | Capsule | Bryant Ranch Prepack |

## Safety Considerations

Structured warning and contraindication fields are not available, and no drug interactions were found in the query. Please refer to the package insert for full safety information.

Guardrails noted in the evidence pack's rationale:
- **Dependence and withdrawal risk**
- **Next-day sedation**
- **Falls and cognitive impairment in older adults** (Beers-type concerns)
- **Short-term use only**, with a planned taper (see PMID 39374004)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Temazepam is a marketed hypnotic, so the prediction is essentially an on-label confirmation. It has a very high TxGNN score, a guideline, systematic reviews and a recent placebo-controlled RCT. Dependence, sedation, and fall risk in older adults call for restrictions.

**To proceed, the following is needed:**
- The package insert warnings and contraindications, which are currently missing and block the safety screening step
- Confirmation of the phase and results of the 2024 advanced-cancer RCT (PMID 39304187)
- ClinicalTrials.gov records, to test whether the evidence level can rise to L1
- Correction of the upstream record: the original indication and mechanism of action are missing for a drug already approved for insomnia
- A short-duration and taper plan, with special attention to older adults
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


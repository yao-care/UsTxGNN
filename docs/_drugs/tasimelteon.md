---
layout: default
title: Tasimelteon
parent: Model Prediction Only (L5)
nav_order: 1201
evidence_level: L5
indication_count: 10
---

# Tasimelteon
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

# Tasimelteon: From Circadian Rhythm Disorders to Insomnia

> **Note on candidate selection:** The Evidence Pack's rank 1 prediction (bilateral parasagittal parieto-occipital polymicrogyria) has no trials, no literature, and no plausible mechanism. It is most likely a knowledge-graph artifact. This report therefore covers rank 2, **insomnia**, the only prediction with substantial clinical evidence. The other predictions are all L5 (motor neuron and skeletal disorders) or L4 (endogenous depression, review-level literature only).

## One-Sentence Summary

Tasimelteon is a melatonin MT1/MT2 receptor agonist already marketed in the US for circadian rhythm disorders.
The TxGNN model predicts it may be effective for **insomnia**, with **4 clinical trials** (2 Phase 3 RCTs) and **6 review articles** supporting this direction.
No efficacy outcome data are included in the supplied record, so the evidence is promising but unconfirmed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Circadian rhythm disorders (per the Evidence Pack rationale; the license records contain no indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L2 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (2 NDAs and 3 ANDAs) |
| Recommended Decision | Hold |

**Evidence level note:** The Evidence Pack labels this L1. Under the L1–L5 rules, L1 requires at least 2 *completed* Phase 3 RCTs. Only one is completed (NCT00548340); the other (NCT06953869) is still recruiting. I have therefore rated it L2.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the DrugBank fields supplied. Based on the literature, tasimelteon is a dual MT1/MT2 melatonin receptor agonist. These receptors are densely expressed in the suprachiasmatic nucleus, the brain's circadian pacemaker. Activating them can shift circadian phase and promote sleep. Reviews (PMID 24228714, 19557144) describe tasimelteon as a high-affinity, nonselective MT1/MT2 agonist. They also note that this mechanism differs fundamentally from GABAergic hypnotics.

Insomnia and circadian rhythm disorders are closely related sleep-wake problems. Melatonergic agents mainly favor sleep initiation and reset the clock to phases that allow persistent sleep. That makes insomnia a direct mechanistic extension of the drug's existing use. A Phase 3 trial (NCT00548340) tested the drug in primary insomnia, and a pediatric insomnia Phase 3 trial is now recruiting. Because the drug is already marketed, its general safety profile is known.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06953869](https://clinicaltrials.gov/study/NCT06953869) | Phase 3 | Recruiting | 420 | Double-blind, randomized, placebo-controlled study of daily oral tasimelteon in pediatric insomnia disorder. No results yet; expected completion 2028-01. |
| [NCT00548340](https://clinicaltrials.gov/study/NCT00548340) | Phase 3 | Completed | 322 | Multicenter, randomized, double-blind, placebo-controlled trial of VEC-162 (tasimelteon) at 20 and 50 mg/day for 5 weeks in primary insomnia. Outcome data are not in the supplied record. |
| [NCT03291041](https://clinicaltrials.gov/study/NCT03291041) | Phase 2 | Completed | 25 | Proof-of-concept study of tasimelteon vs. placebo in jet lag disorder. Adjacent to insomnia; the small sample limits inference. |
| [NCT05922995](https://clinicaltrials.gov/study/NCT05922995) | Early Phase 1 | Terminated | 20 | Open-label pilot of 20 mg tasimelteon in REM behavior disorder, with insomnia questionnaires as secondary measures. No control arm; low informational value. |

## Literature Evidence

All available publications are reviews; no primary RCT publications were returned.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25207602](https://pubmed.ncbi.nlm.nih.gov/25207602/) | 2014 | Review | Int J Mol Sci | Reviews the efficacy and safety of melatonin receptor agonists (ramelteon, prolonged-release melatonin, agomelatine, tasimelteon) in insomnia, depression, and circadian sleep-wake disorders. |
| [19557144](https://pubmed.ncbi.nlm.nih.gov/19557144/) | 2009 | Review | Neuropsychiatr Dis Treat | Melatonergic hypnotic effects act through MT1/MT2 receptors in the suprachiasmatic nucleus. They favor sleep initiation and clock resetting, unlike GABAergic hypnotics. |
| [24228714](https://pubmed.ncbi.nlm.nih.gov/24228714/) | 2014 | Review | J Med Chem | Tasimelteon is among the most advanced MT1/MT2 agonists in clinical evaluation. Covers ligands, models, and therapeutic potential. |
| [35585820](https://pubmed.ncbi.nlm.nih.gov/35585820/) | 2023 | Review | Curr Drug Saf | Discusses melatonin and tasimelteon in Alzheimer's disease, where insomnia is a common feature. Only tangentially relevant. |
| [22010042](https://pubmed.ncbi.nlm.nih.gov/22010042/) | 2011 | Review | Ther Adv Neurol Disord | Melatonin and analogs for sleep disorders and neuroprotection in Parkinson's disease. Tangential. |
| [22167135](https://pubmed.ncbi.nlm.nih.gov/22167135/) | 2011 | Review | Neuro Endocrinol Lett | Sleep and circadian disruption in obesity and the possible value of melatonin. Tangential. |

## US Market Information

The license records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA205677 | Hetlioz | Capsule | Vanda Pharmaceuticals Inc. |
| NDA214517 | Hetlioz | Suspension | Vanda Pharmaceuticals Inc. |
| ANDA211654 | Tasimelteon | Capsule | Amneal Pharmaceuticals NY LLC |
| ANDA211601 | Tasimelteon | Capsule, gelatin coated | Teva Pharmaceuticals, Inc. |
| ANDA211607 | Tasimelteon | Capsule | Apotex Corp. |

## Safety Considerations

Please refer to the package insert for safety information. Warnings and contraindications could not be retrieved, and no drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism fits well and two Phase 3 RCTs exist, but only one is completed and its results are not in the supplied record. The supporting literature is review-level only. Missing package insert safety data is a blocking gap for safety screening.

**To proceed, the following is needed:**
- Retrieve the results of NCT00548340 (primary endpoints, sleep onset latency, safety) and confirm the exact population studied.
- Confirm the full title and target population of NCT06953869, and monitor its readout (expected 2028).
- Obtain package insert warnings and contraindications from the FDA website.
- Obtain mechanism-of-action data from DrugBank.
- Confirm route and formulation compatibility (capsule vs. suspension) for the target population, especially pediatrics.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Solriamfetol
parent: Model Prediction Only (L5)
nav_order: 1173
evidence_level: L5
indication_count: 10
---

# Solriamfetol
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

# Solriamfetol: From Narcolepsy to Attention Deficit Hyperactivity Disorder

## One-Sentence Summary

Solriamfetol is a wake-promoting drug, originally used to treat excessive daytime sleepiness in narcolepsy and obstructive sleep apnea.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**,
with **5 clinical trials** (including 3 Phase 3 trials) and **6 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy (other listed indications: narcolepsy-cataplexy syndrome, obstructive sleep apnea syndrome, and several central nervous system disorders) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (see note below) |
| US Market Status | Cancelled only (the single NDA is listed as cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* Under the strict rule (≥2 completed Phase 3 RCTs), only one completed Phase 3 RCT (NCT05972044) is registered, and its results have not been verified. The other completed trial is a small Phase 2/3 pilot, which has a published report. The L1 level assigned in the compiled data should therefore be read cautiously; a conservative reading would be L2.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the drug's known pharmacology, solriamfetol is a dopamine and norepinephrine reuptake inhibitor (DNRI). Its efficacy in excessive daytime sleepiness is established, and mechanistically it may be applicable to ADHD.

Enhancing dopamine and norepinephrine signaling in prefrontal circuits is the established basis of ADHD drug treatment (for example methylphenidate and atomoxetine). Narcolepsy and ADHD also share attention and arousal problems, which makes the link biologically plausible. This mechanistic link comes from general pharmacology, not from the supplied data.

Other predicted indications are much weaker. Insomnia is only indirectly related (the drug is wake-promoting, so any benefit would be on daytime symptoms). The ADHD inattentive subtype is covered by the ADHD evidence. The remaining predictions, such as faciodigitogenital syndrome, chondromyxoid fibroma, and variably protease-sensitive prionopathy, have no supporting evidence and no plausible mechanism.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05972044](https://clinicaltrials.gov/study/NCT05972044) | Phase 3 | Completed | 516 | FOCUS: randomized, double-blind, placebo-controlled trial in adults with ADHD; results should be verified |
| [NCT04839562](https://clinicaltrials.gov/study/NCT04839562) | Phase 2/3 | Completed | 66 | Double-blind placebo-controlled pilot in adults aged 18-65 with ADHD |
| [NCT07717892](https://clinicaltrials.gov/study/NCT07717892) | Phase 3 | Recruiting | 468 | 6-week placebo-controlled trial in adolescents aged 12 to <18; no results yet |
| [NCT07717879](https://clinicaltrials.gov/study/NCT07717879) | Phase 3 | Recruiting | 468 | 6-week placebo-controlled trial in children aged 6 to <12; no results yet |
| [NCT07773883](https://clinicaltrials.gov/study/NCT07773883) | Phase 3 | Enrolling by invitation | 300 | Open-label long-term safety study in children and adolescents |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37819836](https://pubmed.ncbi.nlm.nih.gov/37819836/) | 2023 | RCT | J Clin Psychiatry | Remote, randomized, double-blind, placebo-controlled 6-week dose-optimization pilot (75 or 150 mg) in adults with ADHD, examining effects and tolerability |
| [33870884](https://pubmed.ncbi.nlm.nih.gov/33870884/) | 2022 | Review | CNS Spectrums | Review of solriamfetol for ADHD (no abstract available) |
| [40986064](https://pubmed.ncbi.nlm.nih.gov/40986064/) | 2025 | Review | Expert Opin Pharmacother | Phase III pipeline for ADHD, noting need for alternatives to stimulants and non-stimulants |
| [38771653](https://pubmed.ncbi.nlm.nih.gov/38771653/) | 2024 | Review | Expert Opin Pharmacother | Recent advances in ADHD drug treatment beyond stimulants |
| [41621729](https://pubmed.ncbi.nlm.nih.gov/41621729/) | 2026 | Review | Pharmacol Ther | Pharmacological, neuromodulatory, and psychotherapeutic options for adult ADHD |
| [34534876](https://pubmed.ncbi.nlm.nih.gov/34534876/) | 2021 | Review | Epilepsy Behav | Drugs for epilepsy patients with excessive daytime sleepiness, noting ADHD as a comorbid cause |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211230 | SUNOSI (Axsome Therapeutics, Inc.) | Film-coated tablet (oral) | Not specified in the compiled data; status: cancelled |

## Safety Considerations

- **Drug Interactions:** 35 interactions were identified. The one rated Major is **methylene blue**. The others shown are rated Moderate and are mainly sympathomimetic or adrenergic agents, including epinephrine, ephedrine, pseudoephedrine, phenylephrine, isoprenaline, mazindol, isometheptene, and beta-agonists such as salbutamol, formoterol, olodaterol, vilanterol, pirbuterol, and orciprenaline, plus ophthalmic naphazoline and oxymetazoline. Additive effects on blood pressure and heart rate are the likely concern.
- **Other considerations:** Because of its noradrenergic action, cardiovascular effects (heart rate and blood pressure) need monitoring, especially in younger patients and anyone with a history of heart disease.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial and a completed Phase 2/3 pilot in adults, along with a published placebo-controlled pilot, support the ADHD direction. Three further Phase 3 trials in children and adolescents are under way. However, efficacy results from the Phase 3 trial have not been verified, and the US NDA is cancelled.

**To proceed, the following is needed:**
- Verified results from the Phase 3 adult trial (NCT05972044)
- Results from the pediatric and adolescent Phase 3 trials (NCT07717892, NCT07717879) and the long-term safety study (NCT07773883)
- Package insert warnings and contraindications, which are currently missing and are a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- A cardiovascular monitoring plan, plus a review of the abuse and misuse potential relevant to ADHD populations
- Clarification of the cancelled US market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


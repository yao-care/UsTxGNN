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

# Solriamfetol: From Excessive Daytime Sleepiness (Narcolepsy/OSA) to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Solriamfetol is a wake-promoting dopamine and norepinephrine reuptake inhibitor. It is marketed in the US as SUNOSI, and the supplied literature describes it as approved for excessive daytime sleepiness in narcolepsy and obstructive sleep apnea.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, with **2 completed clinical trials** (one Phase 3, one Phase 2/3) and **5 relevant publications** supporting this direction.
No trial results were supplied, so efficacy is not yet confirmed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Excessive daytime sleepiness in narcolepsy or OSA (from PMID 34606437; the US license records supplied contain no indication text) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license records (both NDA211230) |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note:* The Evidence Pack labels this indication L1. Under the stated rules, L1 needs two completed Phase 3 RCTs. Only one completed Phase 3 trial (NCT05972044) and one completed Phase 2/3 pilot (NCT04839562) are listed, and neither has supplied results. L2 is therefore the more defensible level until the Phase 3 outcome is confirmed.

## Why is This Prediction Reasonable?

Solriamfetol is a dopamine and norepinephrine reuptake inhibitor. Detailed mechanism-of-action data from DrugBank is not available in the supplied record, so this description comes from the Pack's rationale and the published literature. Catecholaminergic modulation of attention and executive function is the basis of established ADHD pharmacology, including stimulants and norepinephrine-acting non-stimulants.

The original indication is daytime sleepiness, and ADHD is an attention and executive-function disorder, so the two are different conditions. They share a plausible pharmacological route: enhancing dopamine and norepinephrine signalling to improve wakefulness and attention. A published review (PMID 40986064) also lists new ADHD strategies aimed at alternative neurobiological mechanisms beyond classic stimulants. This is the setting in which solriamfetol has been studied.

The biological link is plausible, but it remains a hypothesis until the Phase 3 results are reviewed. Because solriamfetol is stimulant-like, cardiovascular effects and abuse potential must be assessed before any further progression.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05972044](https://clinicaltrials.gov/study/NCT05972044) | Phase 3 | Completed (2023-07 to 2025-03) | 516 | FOCUS: multi-center, randomized, double-blind, placebo-controlled trial of solriamfetol in adults with ADHD. Results were not supplied. |
| [NCT04839562](https://clinicaltrials.gov/study/NCT04839562) | Phase 2/3 | Completed (2021-08 to 2023-01) | 66 | Double-blind, placebo-controlled pilot in adults aged 18-65 with ADHD. Results were not supplied. The related publication (PMID 37819836) reports 60 participants. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [37819836](https://pubmed.ncbi.nlm.nih.gov/37819836/) | 2023 | RCT | J Clin Psychiatry | Remote, randomized, double-blind, placebo-controlled 6-week dose-optimization trial (75 mg or 150 mg) in 60 adults with DSM-5 ADHD. It tested whether solriamfetol has a favorable effect and tolerability pattern. The supplied abstract is truncated, so outcomes are not available. |
| [38771653](https://pubmed.ncbi.nlm.nih.gov/38771653/) | 2024 | Review | Expert Opin Pharmacother | Reviews ADHD drug advances beyond stimulants. Stimulants share similar adverse effects and carry misuse and dependence risk, which motivates non-stimulant options. |
| [40986064](https://pubmed.ncbi.nlm.nih.gov/40986064/) | 2025 | Review | Expert Opin Pharmacother | Reviews Phase III ADHD pipeline drugs. Many patients respond only partially to current treatments or worry about side effects, which drives interest in new mechanisms. |
| [41621729](https://pubmed.ncbi.nlm.nih.gov/41621729/) | 2026 | Review | Pharmacol Ther | Synthesizes pharmacological, neuromodulatory and psychotherapeutic options for adult ADHD. Adult ADHD is common and has high comorbidity and functional impact. |
| [33870884](https://pubmed.ncbi.nlm.nih.gov/33870884/) | 2022 | Review | CNS Spectrums | Review titled "Solriamfetol for attention deficit hyperactivity disorder." No abstract was supplied. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211230 | SUNOSI (Axsome Therapeutics, Inc.) | Film-coated tablet (oral) | Not listed in the supplied record. Published literature describes excessive daytime sleepiness in narcolepsy or OSA. |

The supplied data contains two license records with the same NDA number and details, so only one row is shown.

## Safety Considerations

Please refer to the package insert for safety information.

Based on the Pack's mechanistic assessment, the following points need attention:
- **Cardiovascular:** Blood pressure and heart rate monitoring is required because of noradrenergic reuptake inhibition.
- **Abuse potential:** A stimulant-related abuse-potential review is needed for use in ADHD.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed 516-patient Phase 3 placebo-controlled trial and a completed Phase 2/3 pilot directly test solriamfetol in adult ADHD, and the mechanism fits established ADHD pharmacology. However, no efficacy or safety results were supplied, so the decision cannot move beyond guarded progression yet.

**To proceed, the following is needed:**
- Primary and secondary outcome results from NCT05972044 (FOCUS) and NCT04839562, and the full results of the published pilot (PMID 37819836)
- The FDA package insert warnings and contraindications, which are currently blocking the safety screening
- Detailed mechanism-of-action data from DrugBank
- A cardiovascular monitoring plan and an abuse-potential and misuse-risk review for the ADHD population
- Confirmation of the US approved indication text for NDA211230

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


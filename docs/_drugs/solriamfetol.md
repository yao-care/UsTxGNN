---
layout: default
title: Solriamfetol
parent: 僅模型預測 (L5)
nav_order: 1173
evidence_level: L5
indication_count: 10
---

# Solriamfetol
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

# Solriamfetol: From Excessive Daytime Sleepiness to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

Solriamfetol is a dopamine/norepinephrine reuptake inhibitor originally used to treat excessive daytime sleepiness associated with narcolepsy and obstructive sleep apnea. The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**, with a **completed Phase 3 RCT (n=516)** plus a supporting Phase 2/3 pilot study and **6 related publications** currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in local regulatory license data; supporting literature (PMID 34606437) notes solriamfetol is approved in the US/EU for excessive daytime sleepiness associated with narcolepsy or obstructive sleep apnea |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Market Status | Not Marketed (0 licenses on file) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for solriamfetol is not available in the regulatory record (Data Gap DG002). Based on the supporting evidence collected for this candidate, solriamfetol is classified as a dopamine/norepinephrine reuptake inhibitor (DNRI), acting on the same monoaminergic system targeted by first-line ADHD medications such as methylphenidate and amphetamines.

Its original indication — excessive daytime sleepiness in narcolepsy and obstructive sleep apnea — reflects a wake-promoting, pro-catecholaminergic pharmacology. Since core ADHD symptoms (inattention, hypoactive arousal) are also thought to involve dopaminergic/noradrenergic dysregulation in fronto-striatal circuits, the mechanistic rationale for repurposing to ADHD is considered high. This is further supported by the fact that the strongest evidence in this evidence pack — a completed, randomized, double-blind, placebo-controlled Phase 3 trial (FOCUS study) — was designed specifically to test this hypothesis in adults with ADHD.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05972044](https://clinicaltrials.gov/study/NCT05972044) | Phase 3 | Completed | 516 | FOCUS trial — multi-center, randomized, double-blind, placebo-controlled study assessing efficacy and safety of solriamfetol in adults with ADHD; the key confirmatory trial for this indication |
| [NCT04839562](https://clinicaltrials.gov/study/NCT04839562) | Phase 2/3 | Completed | 66 | Double-blind, placebo-controlled pilot study of solriamfetol in adults (18–65) with ADHD; results published (PMID 37819836) and served as the basis for the subsequent Phase 3 trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37819836](https://pubmed.ncbi.nlm.nih.gov/37819836/) | 2023 | RCT | J Clin Psychiatry | 6-week dose-optimization (75mg/150mg) double-blind placebo-controlled pilot trial in 60 adults with DSM-5 ADHD; favorable pattern of effects and tolerability observed |
| [41621729](https://pubmed.ncbi.nlm.nih.gov/41621729/) | 2026 | Review | Pharmacology & Therapeutics | Comprehensive review of pharmacological, neuromodulatory, and psychotherapeutic interventions for adult ADHD |
| [40986064](https://pubmed.ncbi.nlm.nih.gov/40986064/) | 2025 | Review | Expert Opin Pharmacother | Review of potential ADHD treatments with a focus on agents in Phase 3 trials |
| [38771653](https://pubmed.ncbi.nlm.nih.gov/38771653/) | 2024 | Review | Expert Opin Pharmacother | Reviews non-stimulant options moving beyond traditional ADHD stimulant therapy |
| [33870884](https://pubmed.ncbi.nlm.nih.gov/33870884/) | 2022 | Review/Commentary | CNS Spectrums | Early commentary proposing solriamfetol as a candidate for ADHD treatment |
| [34534876](https://pubmed.ncbi.nlm.nih.gov/34534876/) | 2021 | Review | Epilepsy & Behavior | Discusses drugs for excessive daytime sleepiness/attentional deficits in patients with epilepsy; indirect relevance to ADHD-related attentional mechanisms |

---

## Market Information

No marketing authorization records were found in the available regulatory dataset. Solriamfetol currently holds **0 licenses** and is classified as **not marketed** in this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in the current evidence pack (flagged as Blocking Data Gap DG001 — TFDA label warnings/contraindications must be sourced before any S1 safety pre-assessment can proceed).

Note for downstream evaluation: because solriamfetol is a norepinephrine reuptake inhibitor, its cardiovascular effects (heart rate/blood pressure elevation) should be specifically assessed in any ADHD population with comorbid cardiovascular risk, even though this was not part of the current data pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed, adequately powered Phase 3 RCT (NCT05972044, n=516) plus a supporting completed Phase 2/3 pilot with published positive results (PMID 37819836) constitute L1-level evidence with a mechanistically coherent rationale (shared monoaminergic target with first-line ADHD agents). However, the complete absence of local safety labeling data and the drug's not-marketed status in this jurisdiction warrant a guarded rather than unconditional "Go."

**To proceed, the following is needed:**
- TFDA/local regulatory label — warnings and contraindications (Blocking, DG001)
- Detailed mechanism of action documentation from DrugBank (High priority, DG002)
- Confirmation of regulatory pathway given current "not marketed" / 0-license status
- Cardiovascular safety monitoring plan specific to ADHD populations, given the drug's noradrenergic activity
- Final published results/full manuscript of the FOCUS Phase 3 trial (currently only summary-level data available)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


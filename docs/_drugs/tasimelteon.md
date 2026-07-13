---
layout: default
title: Tasimelteon
parent: 僅模型預測 (L5)
nav_order: 620
evidence_level: L5
indication_count: 10
---

# Tasimelteon
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

# Tasimelteon: From Non-24-Hour Sleep-Wake Disorder to Insomnia

## One-Sentence Summary

Tasimelteon is a selective MT1/MT2 melatonin receptor agonist, originally approved by the FDA for Non-24-Hour Sleep-Wake Disorder (Non-24) in totally blind individuals.
The TxGNN model predicts it may be effective for **Insomnia**, with **4 clinical trials** (including 2 completed Phase 3 studies) and **6 publications** currently supporting this direction.

> **Note on candidate selection:** TxGNN rank 1 (bilateral parasagittal parieto-occipital polymicrogyria, score 99.48%) is classified as L5/Hold due to absent mechanistic linkage and zero supporting evidence. This report focuses on rank 2 (insomnia, score 99.47%), which carries L1 evidence and the highest decision stage (S3), representing the most actionable repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Non-24-Hour Sleep-Wake Disorder |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| US Market Status | No records found in regulatory database |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on known information, Tasimelteon is a selective melatonin receptor agonist (MT1/MT2) that acts on the suprachiasmatic nucleus (SCN) — the brain's master circadian pacemaker. By binding MT1 and MT2 receptors in the SCN, it phase-shifts the circadian clock, reduces sleep onset latency, and re-entrains the biological sleep-wake cycle to the 24-hour day.

Non-24-Hour Sleep-Wake Disorder and insomnia share a common mechanistic root: dysregulation of circadian timing. Non-24 represents an extreme failure to entrain to the light-dark cycle, while general insomnia frequently involves circadian phase misalignment and blunted melatonin rhythm. Because Tasimelteon acts upstream at the circadian pacemaker rather than as a sedative-hypnotic, it is mechanistically plausible that the same receptor-level action would improve sleep onset and maintenance in primary insomnia patients.

This prediction is strongly reinforced by two lines of evidence. First, a completed Phase 3 RCT (NCT00548340, n=322) directly compared Tasimelteon versus placebo in patients with primary insomnia — the highest grade of human clinical evidence. Second, the FDA-approved comparator ramelteon (also an MT1/MT2 agonist, approved 2005) is already indicated for insomnia, providing same-class proof-of-concept. A large ongoing Phase 3 pediatric trial (NCT06953869, n=420) further signals continued investment in this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00548340](https://clinicaltrials.gov/study/NCT00548340) | Phase 3 | Completed | 322 | Multicenter double-blind RCT comparing Tasimelteon 20 mg and 50 mg vs. placebo over 5 weeks in primary insomnia — the highest-grade direct evidence for this indication |
| [NCT06953869](https://clinicaltrials.gov/study/NCT06953869) | Phase 3 | Recruiting | 420 | Multicenter double-blind RCT of Tasimelteon vs. placebo in pediatric insomnia; large-scale ongoing trial, expected completion January 2028 |
| [NCT03291041](https://clinicaltrials.gov/study/NCT03291041) | Phase 2 | Completed | 25 | Double-blind proof-of-concept study in jet lag disorder (proxy circadian misalignment model); indirectly supports sleep-onset efficacy via circadian resetting mechanism |
| [NCT05922995](https://clinicaltrials.gov/study/NCT05922995) | Early Phase 1 | Terminated | 20 | Open-label pilot in REM Behavior Disorder assessing insomnia symptom scores (ISI, PSQI); terminated early with limited enrollment — safety reference only, low methodological weight |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25207602](https://pubmed.ncbi.nlm.nih.gov/25207602/) | 2014 | Narrative Review | Int J Mol Sci | Reviewed efficacy and safety of four melatonin receptor agonists (including Tasimelteon) for insomnia and circadian disorders; highlighted complementary mechanisms across the drug class |
| [24228714](https://pubmed.ncbi.nlm.nih.gov/24228714/) | 2014 | Review | J Med Chem | Comprehensive MT1/MT2 receptor pharmacology review; positioned Tasimelteon as a high-affinity non-selective agonist, distinguishing it from sedative-hypnotics for sleep-wake disorder applications |
| [19557144](https://pubmed.ncbi.nlm.nih.gov/19557144/) | 2009 | Review | Neuropsychiatr Dis Treat | Compared melatoninergic agonists vs. classical hypnotics for insomnia; reported Tasimelteon reduced sleep onset latency in Phase 2/3 trials with a favorable adverse-effect profile |
| [35585820](https://pubmed.ncbi.nlm.nih.gov/35585820/) | 2023 | Review | Curr Drug Saf | Discussed Tasimelteon's role in Alzheimer's-associated insomnia and neurodegenerative sleep disruption; contextualizes potential beyond Non-24 |
| [22010042](https://pubmed.ncbi.nlm.nih.gov/22010042/) | 2011 | Review | Ther Adv Neurol Disord | Examined melatonin agonists in Parkinson's disease sleep disorders; Tasimelteon discussed as mechanistically relevant to REM-related insomnia components |
| [22167135](https://pubmed.ncbi.nlm.nih.gov/22167135/) | 2011 | Review | Neuro Endocrinol Lett | Linked circadian rhythm disruption in obesity with insomnia pathophysiology; proposed melatonin receptor agonists as resynchronizing agents for metabolic-comorbid insomnia |

---

## US Market Information

No FDA authorization records for Tasimelteon were retrieved in the regulatory database query (2026-03-25, result count: 0). The regulatory data gap (DG001) — covering package insert warnings and contraindications — is classified as **Blocking** severity.

For reference: Tasimelteon is commercially available in the United States under the brand name **Hetlioz** (Vanda Pharmaceuticals), FDA-approved for Non-24-Hour Sleep-Wake Disorder. Verification against the official FDA database is recommended before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields (key warnings, contraindications, drug-drug interactions) were returned as data gaps or not found in the 2026-03-25 query. Obtaining the full TFDA/FDA package insert is a **Blocking** prerequisite (DG001) before safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 double-blind RCT (NCT00548340, n=322) directly supports Tasimelteon for primary insomnia at L1 evidence level, and the FDA-approved class comparator ramelteon demonstrates that MT1/MT2 agonism is a validated mechanism for this indication. The ongoing pediatric Phase 3 trial (NCT06953869, n=420) further confirms industry confidence in this repurposing direction.

**To proceed, the following is needed:**

- **[Blocking]** Obtain full FDA/TFDA package insert to complete safety evaluation (warnings, contraindications, special population precautions) — Data Gap DG001
- **[High]** Retrieve DrugBank MOA documentation for mechanistic linkage analysis — Data Gap DG002
- **[Required]** Drug-drug interaction profile — current DDI query returned no records; manual lookup or clinical pharmacology review required
- **[Monitoring]** Await results from NCT06953869 (pediatric Phase 3, expected completion January 2028) to support pediatric indication extension
- **[Strategic]** Confirm US FDA regulatory pathway: if targeting insomnia as a new indication, assess whether a supplemental NDA or 505(b)(2) pathway is appropriate given the existing Non-24 approval
- **[Regulatory]** Evaluate Taiwan market entry feasibility given current zero-license status in TFDA database
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


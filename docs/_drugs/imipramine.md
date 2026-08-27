---
layout: default
title: Imipramine
parent: 僅模型預測 (L5)
nav_order: 792
evidence_level: L5
indication_count: 7
---

# Imipramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Imipramine: From Depression to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

> Imipramine is a classic tricyclic antidepressant (TCA), historically established for the treatment of major depressive disorder.
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> with **1 clinical trial** and **20 publications** currently associated with this direction — though most of the literature predates modern RCT standards.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (based on imipramine's established TCA classification; no original-indication or license data was returned in this Evidence Pack) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on known pharmacological classification, imipramine is a tricyclic antidepressant (TCA) that inhibits reuptake of norepinephrine and, to a lesser extent, serotonin at the synapse; its efficacy in major depressive disorder is well established, and mechanistically it may be applicable to ADHD through modulation of prefrontal noradrenergic/dopaminergic signaling.

ADHD pathophysiology is linked to dysregulated catecholamine (norepinephrine/dopamine) signaling in the prefrontal cortex — the same system TCAs act on. Before the approval of atomoxetine (a selective norepinephrine reuptake inhibitor), imipramine and desipramine were used clinically as second-line, non-stimulant options for ADHD, particularly in children who did not respond to stimulants such as methylphenidate.

The literature base supporting this link is largely historical (1980s–2000s), consisting of small clinical studies, EEG/P300 biomarker studies, and narrative reviews rather than modern randomized controlled trials. This supports a plausible mechanistic rationale but not a current, high-confidence efficacy signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03220308](https://clinicaltrials.gov/study/NCT03220308) | NA | Completed | 103 | Tested an 8-week mindfulness training program (plus parallel mindful parenting) vs. care-as-usual in children with ADHD. This is a behavioral intervention trial and does **not** test imipramine directly (relevance grade C — low direct relevance to the drug). |

No clinical trial in this Evidence Pack directly evaluates imipramine for ADHD.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9465283](https://pubmed.ncbi.nlm.nih.gov/9465283/) | 1996 | Cohort | Clinical EEG (electroencephalography) | In stimulant (pemoline) poor-responders with ADHD, prolonged P300 latency predicted poor response to subsequent imipramine treatment. |
| [18304665](https://pubmed.ncbi.nlm.nih.gov/18304665/) | 2008 | Cohort | Int J Psychophysiology | Imipramine's effect on EEG in stimulant-non-responsive children with ADHD; imipramine is described as a widely used option when stimulants fail. |
| [6849467](https://pubmed.ncbi.nlm.nih.gov/6849467/) | 1983 | Clinical study | American Journal of Psychiatry | Early report titled "Imipramine for attention deficit disorder" (abstract not available). |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Review | Expert Opinion on Drug Safety | Reviews non-stimulant ADHD treatments; notes tricyclics including desipramine/imipramine as second-line options after atomoxetine. |
| [17078784](https://pubmed.ncbi.nlm.nih.gov/17078784/) | 2006 | Cohort | Expert Rev Neurotherapeutics | Discusses norepinephrine reuptake inhibitors (desipramine, imipramine) alongside atomoxetine as ADHD treatment options, using P300 topography to guide treatment choice. |
| [31776871](https://pubmed.ncbi.nlm.nih.gov/31776871/) | 2019 | Review | CNS Drugs | Systematic review of clinically significant drug-drug interactions for ADHD pharmacotherapy agents. |
| [1974836](https://pubmed.ncbi.nlm.nih.gov/1974836/) | 1990 | Review | Clinical Pharmacy | General review of ADHD epidemiology, diagnosis, and pharmacotherapy. |
| [10790990](https://pubmed.ncbi.nlm.nih.gov/10790990/) | 1999 | Review | Evidence Report/Technology Assessment | Evidence assessment of pharmacological and non-pharmacological ADHD interventions in children and adults. |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Frontiers in Psychiatry | Meta-review of antidepressant efficacy/tolerability/suicidality in children and adolescents, including ADHD as one of several indications assessed. |
| [25295451](https://pubmed.ncbi.nlm.nih.gov/25295451/) | 2014 | Review | Einstein (São Paulo) | General review evaluating therapeutic regimens for ADHD. |

10 additional lower-tier records (case-level platelet-binding pharmacology studies, drug-interaction case notes, and comorbidity reviews) are available in the Evidence Pack but are omitted here as lower priority.

---

## US Market Information

No marketing authorizations are on file for this candidate in the current dataset — `taiwan_regulatory.total_licenses = 0` and market status is recorded as **Not Marketed**. No NDA number, product name, or approved indication text is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were returned for this candidate (DDI query status: not found).

Note: TFDA/FDA label warnings and contraindications are flagged as a **Blocking** data gap (DG001) in this Evidence Pack — this must be resolved before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug currently has no marketing authorization on file (0 licenses), label-level safety data is a Blocking gap that prevents safety pre-screening, and the ADHD evidence base (L3) consists almost entirely of retrospective/cohort studies and narrative reviews from the 1980s–2000s rather than modern controlled trials. The signal is mechanistically plausible but not yet actionable.

**To proceed, the following is needed:**
- TFDA/FDA package insert warnings and contraindications (Blocking gap DG001)
- Confirmed mechanism of action / pharmacology detail (High-priority gap DG002)
- Modern RCT or systematic review data specifically evaluating imipramine (or TCA class) for ADHD
- Completed drug-drug interaction database query (currently not_found)
- Clarification of current US marketing/regulatory status if a repurposing pathway is to be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Imipramine
parent: Model Prediction Only (L5)
nav_order: 792
evidence_level: L5
indication_count: 7
---

# Imipramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Imipramine: From Depression to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Imipramine is a tricyclic antidepressant that has been marketed for many years. The TxGNN model predicts it may be useful for **attention deficit-hyperactivity disorder (ADHD)**. Support is limited: **1 registered clinical trial** (which does not test imipramine) and **18 publications**, mostly reviews and small older studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (general knowledge of the drug class; the approved-indication text was not provided in the data) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 (reviews and small clinical studies; no completed Phase 3 RCT) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed authorizations are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, imipramine inhibits reuptake of norepinephrine and serotonin. Noradrenergic modulation is a plausible route to ADHD symptom benefit.

Non-stimulant options for ADHD include noradrenergic agents. The literature describes imipramine and desipramine (its metabolite) as non-selective norepinephrine reuptake inhibitors that can be effective when stimulants fail (PMID 17078784, PMID 15794722). This gives the prediction some credibility beyond the model score.

The 99.90% score is a computational output, not clinical evidence. Tricyclic cardiovascular and anticholinergic safety concerns in children would need to be addressed before any development.

Other predictions for imipramine are weaker. The ADHD inattentive subtype is a subtype of the same condition and has no evidence of its own. Obsessive-compulsive disorder has some older clinical papers, but imipramine is generally considered less effective than clomipramine there. The remaining predictions (for example faciodigitogenital syndrome and chondromyxoid fibroma) have no plausible mechanistic link.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03220308](https://clinicaltrials.gov/study/NCT03220308) | Not applicable | Completed | 103 | Tests 8-week mindfulness training for children with ADHD plus mindful parenting for parents, against care-as-usual. It does not test imipramine, so it gives no drug-specific evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Front Psychiatry | Assesses efficacy, tolerability and suicidality of antidepressants in children and adolescents across several disorders, including ADHD. |
| [10790990](https://pubmed.ncbi.nlm.nih.gov/10790990/) | 1999 | Review | Evid Rep Technol Assess (Summ) | Evidence report on short- and long-term effectiveness and safety of drug and non-drug ADHD treatments. |
| [17078784](https://pubmed.ncbi.nlm.nih.gov/17078784/) | 2006 | Clinical study | Expert Rev Neurother | Notes that non-selective norepinephrine reuptake inhibitors (desipramine, imipramine) can be effective in ADHD; uses P300 topography to guide treatment choice. |
| [18304665](https://pubmed.ncbi.nlm.nih.gov/18304665/) | 2008 | Not classified | Int J Psychophysiol | Examines EEG effects of imipramine in children with ADHD who did not respond to stimulants. |
| [9465283](https://pubmed.ncbi.nlm.nih.gov/9465283/) | 1996 | Not classified | Clin EEG | In 17 ADHD children who responded poorly to pemoline and were treated with imipramine, prolonged P300 latency predicted poor imipramine response. |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Not classified | Expert Opin Drug Saf | Reviews the safety of non-stimulant ADHD agents; lists imipramine and desipramine as possible options after stimulants. |
| [6849467](https://pubmed.ncbi.nlm.nih.gov/6849467/) | 1983 | Not classified | Am J Psychiatry | Report on imipramine for attention deficit disorder (no abstract available). |
| [2258453](https://pubmed.ncbi.nlm.nih.gov/2258453/) | 1990 | Not classified | J Clin Psychopharmacol | Retrospective study of 36 children with ADHD; carbamazepine may influence plasma imipramine and desipramine concentrations. |
| [1974836](https://pubmed.ncbi.nlm.nih.gov/1974836/) | 1990 | Review | Clin Pharm | General review of ADHD and the role of pharmacotherapy. |
| [31776871](https://pubmed.ncbi.nlm.nih.gov/31776871/) | 2019 | Review | CNS Drugs | Overview of pharmacokinetic drug-drug interactions for ADHD agents. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040903 | Imipramine Hydrochloride (PD-Rx Pharmaceuticals) | Tablet, film coated | Not provided |
| ANDA040751 | Imipramine Hydrochloride (Proficient Rx) | Tablet | Not provided |
| ANDA091099 | Imipramine Pamoate (Hikma) | Capsule | Not provided |
| ANDA090442 | Imipramine Hydrochloride (Lupin) | Tablet, film coated | Not provided |
| ANDA040751 | Imipramine Hydrochloride (Oxford Pharmaceuticals) | Tablet | Not provided |

All listed products are oral.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is plausible and some older small studies address imipramine in ADHD. However, there is no drug-specific registered trial, no completed Phase 3 RCT, and the label safety data are missing. Imipramine's cardiovascular and anticholinergic risks in children are a further concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Full-text review of the imipramine-specific ADHD studies (PMIDs 18304665, 9465283, 6849467) to judge efficacy and dosing
- A pediatric safety assessment, including cardiac monitoring and drug interactions such as carbamazepine
- Comparison against approved ADHD options (stimulants, atomoxetine) to define where imipramine would fit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


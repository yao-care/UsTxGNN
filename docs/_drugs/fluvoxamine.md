---
layout: default
title: Fluvoxamine
parent: 僅模型預測 (L5)
nav_order: 732
evidence_level: L5
indication_count: 10
---

# Fluvoxamine
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

# Fluvoxamine: From Obsessive-Compulsive Disorder to Paranoid Personality Disorder

## One-Sentence Summary

Fluvoxamine is a selective serotonin reuptake inhibitor (SSRI) with pharmacology (5-HT reuptake inhibition, sigma-1 receptor agonism) that underlies its established use in obsessive-compulsive disorder and related anxiety-spectrum conditions, as reflected throughout the trial and literature evidence in this pack. The TxGNN model's top-ranked prediction for this drug is **Paranoid Personality Disorder**, but this candidate is currently supported by **0 clinical trials** and only **2 indirect publications**, neither of which evaluated fluvoxamine as a treatment for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via a US marketing license (none on file); trial/literature evidence in this pack consistently identifies Obsessive-Compulsive Disorder (OCD) as fluvoxamine's core approved use |
| Predicted New Indication | Paranoid Personality Disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for fluvoxamine is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the literature captured here, fluvoxamine is a selective serotonin reuptake inhibitor with additional sigma-1 receptor agonist activity (PMID 20373470), and this pharmacology underlies its well-documented efficacy in OCD, social anxiety disorder, panic disorder/agoraphobia, and major depression — conditions that dominate the clinical trial and publication record for this drug.

For Paranoid Personality Disorder specifically, no mechanistic or clinical rationale is presented in the evidence pack. The two literature hits returned are only tangentially related: one is a cross-sectional study of personality traits in body dysmorphic disorder patients (a subset of whom happened to be enrolled in a fluvoxamine trial for BDD, not personality disorder) (PMID 10929788), and the other is an unrelated review of psychiatric side effects of interferon-alpha therapy (PMID 11686052). Neither studied fluvoxamine as a treatment for paranoid personality disorder.

Notably, this same TxGNN score (0.99997) and evidence pattern repeats across ranks 187–190 (paranoid, schizotypal, histrionic, and schizoid personality disorder), suggesting the model is scoring a cluster of personality-disorder nodes similarly — likely reflecting graph proximity within the psychiatric-disease network rather than a disease-specific mechanistic signal for paranoid personality disorder.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cross-sectional study | Comprehensive Psychiatry | Assessed personality traits/disorders in body dysmorphic disorder patients (26 of 148 had participated in a fluvoxamine trial for BDD); not a treatment study for personality disorder |
| [11686052](https://pubmed.ncbi.nlm.nih.gov/11686052/) | 2001 | Review | L'Encéphale | Reviews psychiatric complications (including personality disorders) induced by interferon-alpha therapy; unrelated to fluvoxamine |

## US Market Information

No US marketing authorization is currently on file (0 NDAs; drug status recorded as not marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (paranoid personality disorder) has no supporting clinical trials and only two indirect, non-therapeutic literature references; the apparent TxGNN signal likely reflects proximity within a personality-disorder node cluster rather than a genuine mechanistic or clinical repurposing hypothesis.

**To proceed, the following is needed:**
- Fluvoxamine mechanism-of-action documentation (DG002, High severity)
- FDA/TFDA label warnings and contraindications, currently blocking safety review (DG001, Blocking severity)
- A targeted literature/clinical search connecting fluvoxamine's serotonergic and sigma-1 pharmacology to paranoid personality disorder specifically, rather than personality traits in comorbid conditions
- Preclinical or exploratory clinical data before this candidate can advance past Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


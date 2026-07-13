---
layout: default
title: Desipramine
parent: 僅模型預測 (L5)
nav_order: 584
evidence_level: L5
indication_count: 8
---

# Desipramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Desipramine: From Major Depressive Disorder to Attention Deficit Hyperactivity Disorder (Inattentive Type)

## One-Sentence Summary

Desipramine is a tricyclic antidepressant (TCA) in the norepinephrine reuptake inhibitor (NRI) class, historically used for major depressive disorder and documented as a second-line agent for broader ADHD. The TxGNN model predicts it may be effective for **Attention Deficit Hyperactivity Disorder, Inattentive Type** with a score of 99.81%; however, **no clinical trials and no publications** specifically addressing this ADHD subtype have been identified to date.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (historical use; no US FDA records retrieved in current query) |
| Predicted New Indication | Attention Deficit Hyperactivity Disorder, Inattentive Type |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | Not Found (0 records retrieved) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not available in this dataset. Based on established pharmacological knowledge, Desipramine is a tricyclic antidepressant that functions primarily as a selective norepinephrine reuptake inhibitor (NRI). By blocking the norepinephrine transporter (NET), it elevates norepinephrine availability in the prefrontal cortex — a brain region that governs executive function, working memory, and sustained attention. This is the same central mechanism by which Atomoxetine operates; Atomoxetine is a selective NRI approved as a first-line non-stimulant ADHD treatment, and this mechanistic parallel lends biological credibility to Desipramine's predicted utility in ADHD.

The theoretical fit for the inattentive subtype is particularly notable. NRI-dominant pharmacology preferentially improves attentional and cognitive symptoms over hyperactive-impulsive symptoms, meaning the inattentive presentation is arguably the more mechanistically appropriate target compared to the combined or hyperactive-impulsive subtypes. Historical clinical literature on the broader ADHD category (rank 2 in this Evidence Pack) further supports the NRI rationale: multiple systematic reviews and a Cochrane meta-review (PMID 25238582) document that tricyclic antidepressants including Desipramine were used as second-line ADHD treatments, and a 1994 review (PMID 8032506) explicitly lists Desipramine as a reasonable second choice when stimulants fail.

The gap between the well-supported broader ADHD prediction and the subtype-specific prediction is therefore not one of mechanism, but of clinical evidence granularity. The TxGNN model's high-confidence prediction (99.81%) for the inattentive subtype is mechanistically coherent; the absence of subtype-specific studies is a data gap, not a refutation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Desipramine in ADHD (Inattentive Type).

---

## Literature Evidence

Currently no related literature available specifically for Desipramine in ADHD (Inattentive Type).

> **Context note:** For the closely related indication of ADHD (general), 15 publications were identified, including a Cochrane systematic review of TCAs in ADHD (PMID 25238582), a Cochrane review of ADHD with comorbid tic disorders (PMID 29944175), and a 2020 meta-review of antidepressants in children and adolescents (PMID 32982805). These publications collectively document Desipramine's historical use in ADHD but do not stratify by subtype.

---

## US Market Information

No US FDA license records were retrieved for Desipramine in the current dataset (0 NDAs returned). Users are advised to verify current regulatory status directly via the FDA's Drugs@FDA portal, as Desipramine (brand name Norpramin®) has historically been available in the US market for the treatment of depression.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for clinical teams:** Although formal warning and contraindication data were not retrievable in this query cycle, Desipramine is a TCA and carries class-level risks that should be reviewed prior to any clinical application, particularly: (1) cardiac conduction effects (QTc prolongation risk), (2) pediatric suicide risk warnings common to antidepressants, and (3) anticholinergic adverse effects. These are especially relevant given the pediatric ADHD population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The NRI mechanism provides a coherent biological basis for this prediction, and Desipramine's historical use in ADHD is documented in multiple systematic reviews. However, no direct evidence — from clinical trials or targeted literature — exists specifically for the inattentive subtype, the precise indication predicted here. With an evidence level of L5, a Hold is appropriate until subtype-specific or at minimum subgroup-stratified data can be identified.

**To proceed, the following is needed:**

- **Subtype-specific evidence search:** Conduct a targeted literature search for Desipramine or TCA outcomes stratified by ADHD subtype (inattentive vs. combined vs. hyperactive-impulsive); existing ADHD studies may contain extractable subgroup data
- **Mechanism of action documentation:** Retrieve formal MOA data from DrugBank (remediation: DrugBank API, tagged DG002 / High severity) to strengthen the mechanistic rationale document
- **US regulatory status verification:** Confirm current FDA approval status, retrieve full prescribing information (NDA number, current labeling), and check for any post-market safety updates
- **Cardiac safety review:** Given the pediatric ADHD context, obtain and evaluate QTc-related data and any existing cardiovascular safety findings for Desipramine
- **Atomoxetine benchmarking:** Position Desipramine against the approved NRI standard (Atomoxetine) in terms of NET selectivity, tolerability, and pediatric safety to identify whether a clinical advantage or distinct niche exists for the inattentive subtype specifically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


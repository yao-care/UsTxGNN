---
layout: default
title: Levomilnacipran
parent: 僅模型預測 (L5)
nav_order: 856
evidence_level: L5
indication_count: 6
---

# Levomilnacipran
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Levomilnacipran: From Major Depressive Disorder to Melancholia

## One-Sentence Summary

> Levomilnacipran is a serotonin-norepinephrine reuptake inhibitor (SNRI) already established for adult **Major Depressive Disorder (MDD)**. TxGNN evaluated six candidate indications for this drug; the highest-evidence signal points to **Melancholia** (a clinical subtype of MDD), supported by **0 dedicated clinical trials** but **20 general MDD-related publications**. The drug's single top-ranked TxGNN prediction (infantile torticollis) is flagged by the model's own rationale as biologically implausible and is excluded from the primary recommendation below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (MDD), adults (per literature evidence in this pack; not independently confirmed by a Taiwan/US license record) |
| Predicted New Indication | Melancholia (melancholic-featured depression) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

### All TxGNN-Predicted Indications for This Drug

| Rank | Disease | Score | Evidence Level | Stage | Recommendation |
|------|---------|-------|-----------------|-------|-----------------|
| 1 | Benign paroxysmal torticollis of infancy | 99.53% | L5 | S0 | Hold (model itself flags as likely knowledge-graph noise) |
| 2 | Agoraphobia | 99.53% | L4 | S1 | Research Question |
| 3 | Dysthymic disorder | 99.24% | L4 | S1 | Research Question |
| 4 | **Melancholia** | 99.20% | L3 | S2 | **Proceed with Guardrails** |
| 5 | Neurotic depression | 99.20% | L3 | S2 | Proceed with Guardrails |
| 6 | Neurotic disorder | 99.19% | L5 | S0 | Hold |

Melancholia and neurotic depression are functionally the same clinical concept (melancholic/severe depressive subtypes) and are treated together below as the drug's most defensible repurposing signal.

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available for this candidate (`original_moa: [Data Gap]`). However, the literature evidence collected for this pack fills that gap: levomilnacipran is the more pharmacologically active enantiomer of milnacipran, and functions as an SNRI with high affinity for both norepinephrine (Ki ≈ 92.2 nM) and serotonin (Ki ≈ 11.2 nM) transporters (PMID 23499664-class data reflected in PMID 40875503, *J Clin Psychiatry* 2025), with potent, dose-dependent inhibition of NE reuptake distinguishing it from more serotonin-selective SNRIs like duloxetine.

Melancholia and "neurotic depression" are not independent disease entities — they are clinical subtypes/older nosological terms within the MDD spectrum for which levomilnacipran already holds its core approval. Because the pharmacological target (5-HT/NE reuptake) is identical across MDD and its melancholic subtype, the mechanistic rationale for efficacy is strong. What is missing is *subtype-specific* trial evidence: all literature retrieved for this pack studies levomilnacipran in MDD populations broadly (including a pediatric Phase 3 program and network meta-analyses against other second-generation antidepressants), with no trial specifically enrolling or stratifying by melancholic features.

By contrast, the model's #1-ranked prediction — benign paroxysmal torticollis of infancy — has no plausible mechanistic link (a pediatric vestibular/ion-channel disorder vs. an adult SNRI) and zero supporting trials or literature; its own rationale text identifies it as likely knowledge-graph noise, which is why it is not used as the headline indication despite having the highest raw TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for melancholia or neurotic depression specifically.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38700708](https://pubmed.ncbi.nlm.nih.gov/38700708/) | 2024 | RCT | J Child Adolesc Psychopharmacol | Two Phase 3, double-blind, placebo/active-controlled trials of levomilnacipran ER in pediatric (7–17y) MDD |
| [29197738](https://pubmed.ncbi.nlm.nih.gov/29197738/) | 2018 | Network Meta-analysis | J Affect Disord | Compares efficacy/safety of levomilnacipran, vilazodone, and vortioxetine against other second-generation antidepressants in MDD |
| [40172868](https://pubmed.ncbi.nlm.nih.gov/40172868/) | 2025 | RCT | JAMA Psychiatry | Real-world comparison of esketamine + SSRI vs. + SNRI (incl. levomilnacipran) in treatment-resistant depression |
| [40875503](https://pubmed.ncbi.nlm.nih.gov/40875503/) | 2025 | Pharmacology (human study) | J Clin Psychiatry | Confirms levomilnacipran potently inhibits both NE and 5-HT reuptake across its therapeutic dose range, unlike duloxetine |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Systematic Review/Network Meta-analysis | Molecular Psychiatry | Efficacy/tolerability of antidepressants (incl. levomilnacipran) in MDD maintenance-phase treatment |
| [31509357](https://pubmed.ncbi.nlm.nih.gov/31509357/) | 2019 | Review | Prim Care Companion CNS Disord | Narrative review of MOA, PK, and efficacy; proposes unique benefit for MDD fatigue symptom cluster |
| [37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/) | 2023 | Guideline | Clin Pharmacol Ther | CPIC pharmacogenetics guideline for SNRI/SSRI antidepressants including levomilnacipran |
| [41135546](https://pubmed.ncbi.nlm.nih.gov/41135546/) | 2025 | Systematic Review | Lancet | Network meta-analysis ranking antidepressants (incl. levomilnacipran) by cardiometabolic side-effects |
| [33549697](https://pubmed.ncbi.nlm.nih.gov/33549697/) | 2021 | Systematic Review | Prog Neuropsychopharmacol Biol Psychiatry | Meta-analysis of GI side effects across second-generation antidepressants in MDD |
| [27508501](https://pubmed.ncbi.nlm.nih.gov/27508501/) | 2016 | Review | Psychother Psychosom | Critical review of safety/tolerability of newer antidepressants including levomilnacipran |

---

## US Market Information

No marketing authorizations are on file in this dataset (`total_licenses: 0`, market status: Not Marketed). This should be independently verified against the current FDA label before any regulatory action.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: this pack has an unresolved **Blocking** data gap (DG001 — TFDA/FDA label warnings and contraindications not yet retrieved), which by definition prevents this candidate from clearing initial safety screening (S1) regardless of indication.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Melancholia / neurotic depression only — the other four TxGNN candidates in this pack should remain at Hold or Research Question)

**Rationale:**
Melancholia and neurotic depression are subtypes within levomilnacipran's already-approved MDD indication, and the SNRI mechanism is directly applicable; however, no subtype-specific clinical trial exists, so evidence remains L3 (general MDD literature, not indication-specific).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the drug's label warnings/contraindications before any S1 safety pre-assessment can proceed
- Resolve DG002 (High): confirm authoritative MOA record via DrugBank API (currently inferred from literature only)
- Obtain or commission trial data stratified by melancholic-feature status within MDD populations
- Verify current US/Taiwan marketing and licensing status independently, since this pack shows zero authorizations on file
- Do not advance ranks 1 and 6 (torticollis, neurotic disorder) — no mechanistic plausibility or evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Nortriptyline
parent: 僅模型預測 (L5)
nav_order: 977
evidence_level: L5
indication_count: 2
---

# Nortriptyline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Nortriptyline: From Unspecified Indication to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

> Nortriptyline is a tricyclic antidepressant (TCA); its original approved indication is not recorded in this evidence pack.
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> with **0 registered clinical trials** but **20 supporting publications** (including 1 completed controlled trial), currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (original_indications and original_moa both flagged as data gaps) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action documentation is not available in this evidence pack (flagged as a High-severity data gap). However, the model-supplied mechanistic rationale indicates that nortriptyline is a tricyclic antidepressant (TCA) that primarily inhibits norepinephrine (NE) reuptake, with secondary inhibition of serotonin (5-HT) reuptake. This is consistent with literature context in the evidence pack — for example, a PET imaging study (PMID 24345533) confirms nortriptyline's role as a NET-selective TCA in the treatment of depression, while noting NET's relevance to both depression and ADHD.

ADHD pathophysiology is understood to involve prefrontal cortex norepinephrine/dopamine system hypofunction. Because nortriptyline's NE reuptake inhibition mechanism parallels that of atomoxetine (an approved non-stimulant ADHD therapy), the pharmacological rationale for repurposing is plausible. Notably, several publications in this pack highlight nortriptyline's specific advantage in ADHD patients with comorbid tic disorder or Tourette's syndrome, since — unlike central stimulants — it does not appear to exacerbate tics (PMID 8428873, PMID 8444763).

This mechanism does carry a known limitation: TCAs have established cardiac conduction effects (QTc prolongation risk), which is a key consideration for pediatric use and is addressed further below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11052409](https://pubmed.ncbi.nlm.nih.gov/11052409/) | 2000 | RCT | J Child Adolesc Psychopharmacol | Controlled study of nortriptyline efficacy and tolerability in pediatric ADHD |
| [22700161](https://pubmed.ncbi.nlm.nih.gov/22700161/) | 2012 | RCT | Pediatr Nephrol | Randomized double-blind controlled trial of nortriptyline for enuresis in children with ADHD |
| [25238582](https://pubmed.ncbi.nlm.nih.gov/25238582/) | 2014 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic review of tricyclic antidepressants for ADHD in children/adolescents |
| [15064003](https://pubmed.ncbi.nlm.nih.gov/15064003/) | 2004 | Review | Psychiatr Clin North Am | Reviews nonstimulant ADHD treatments; notes nortriptyline among established noradrenergic TCA options, limited by narrow therapeutic index and cardiovascular toxicity |
| [22303520](https://pubmed.ncbi.nlm.nih.gov/22303520/) | 2012 | Review | Ann Clin Psychiatry | CANMAT task force recommendations for managing mood disorders with comorbid adult ADHD |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Review | Expert Opin Drug Saf | Safety review of non-stimulant ADHD agents including TCAs |
| [7807071](https://pubmed.ncbi.nlm.nih.gov/7807071/) | 1995 | Systematic Review | J Nerv Ment Dis | Systematic assessment of tricyclic antidepressants in adult ADHD |
| [8444763](https://pubmed.ncbi.nlm.nih.gov/8444763/) | 1993 | Case series | J Am Acad Child Adolesc Psychiatry | Chart review of 58 ADHD cases treated with nortriptyline |
| [8428873](https://pubmed.ncbi.nlm.nih.gov/8428873/) | 1993 | Cohort | J Am Acad Child Adolesc Psychiatry | Nortriptyline in children with ADHD and comorbid tic disorder/Tourette's syndrome |
| [4075308](https://pubmed.ncbi.nlm.nih.gov/4075308/) | 1985 | Cohort | Clin Neuropharmacol | Early report on nortriptyline in attention deficit disorder |

---

## US Market Information

No license records available (`total_licenses: 0`, market status: 未上市/Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed controlled trial (PMID 11052409) plus a Cochrane systematic review and consistent mechanistic/cohort evidence support ADHD as a biologically plausible repurposing direction for nortriptyline, particularly in patients with comorbid tic disorders — meeting the L2 evidence bar. However, a second predicted subtype indication, "ADHD, inattentive type," has no supporting trials or literature (evidence level L5, decision stage S0) and should remain on **Hold**.

**To proceed, the following is needed:**
- **TFDA label warnings/contraindications** (Blocking data gap — required before this candidate can enter S1 safety review)
- **Official DrugBank mechanism-of-action documentation** (High priority — currently only model-inferred rationale is available)
- Confirmation of Taiwan registration/licensing pathway, as nortriptyline currently holds no active license (0 NDAs, 未上市)
- A cardiac safety monitoring plan (baseline and follow-up ECG) given the TCA class QTc-prolongation risk, especially for pediatric ADHD use
- Additional controlled trial evidence in adult ADHD populations, as existing RCT evidence is limited to pediatric patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


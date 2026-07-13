---
layout: default
title: Thiothixene
parent: 僅模型預測 (L5)
nav_order: 642
evidence_level: L5
indication_count: 10
---

# Thiothixene
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

# Thiothixene: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Thiothixene (brand name: Navane) is a thioxanthene-class first-generation antipsychotic with established efficacy in schizophrenia, acting via high-potency D2 dopamine receptor blockade.
The TxGNN model's top prediction assigns it potential for **Retinal Dystrophy with or without Extraocular Anomalies** (score 99.99%), yet **no clinical trials or published literature** currently support this direction (Evidence Level L5).
Of note, the 10th-ranked prediction — **manic bipolar affective disorder** — carries substantially more real-world evidence, including 20 publications and multiple controlled comparison trials that directly studied thiothixene in acute mania.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia / Psychotic Disorders |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug. Based on known pharmacology, Thiothixene belongs to the thioxanthene class of first-generation antipsychotics. Its efficacy in treating schizophrenia and acute psychotic episodes was established over decades of clinical use, and it operates as a high-potency D2 dopamine receptor antagonist that suppresses mesolimbic dopamine transmission to control positive psychotic symptoms.

Retinal dystrophy with or without extraocular anomalies encompasses a heterogeneous group of inherited retinal degenerations (commonly caused by mutations in genes such as RPGR and CRB1) that lead to progressive photoreceptor loss. There is no established mechanistic connection between D2 receptor blockade and photoreceptor protection or repair of genetic retinal defects. In fact, phenothiazine-class antipsychotics — which are structurally related to thioxanthenes — are known to carry a risk of pigmentary retinopathy at high doses, suggesting the drug's effect on the retina may be adverse rather than therapeutic.

The very high TxGNN score (99.99%) most likely reflects network proximity between dopaminergic pathway nodes and retinal neuron nodes within the knowledge graph, rather than a biologically meaningful therapeutic relationship. This prediction is best understood as a knowledge graph topology artifact, not a clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-perfect TxGNN score, there is zero clinical or preclinical evidence linking thiothixene to retinal dystrophy, the mechanistic connection is implausible (D2 blockade has no established role in photoreceptor protection or inherited retinal degeneration), and the drug is no longer marketed in the US. This prediction most likely reflects a knowledge graph artifact and does not constitute a viable repurposing hypothesis at this time.

**To proceed, the following is needed:**
- Preclinical evidence (cell-based or animal models) demonstrating any neuroprotective effect of thiothixene or D2 antagonism in photoreceptor degeneration
- A mechanistic rationale explaining how D2 receptor blockade could benefit an inherited degenerative retinal condition
- Full mechanistic profile (data gap DG002) to enable proper target overlap analysis against retinal dystrophy disease nodes

---

> **Alternative of Higher Interest — Manic Bipolar Affective Disorder (Rank 10)**
>
> Among all 10 TxGNN predictions for Thiothixene, **manic bipolar affective disorder** (TxGNN score 99.95%, Evidence Level L2) is the most evidence-supported candidate. The dopamine hyperactivity hypothesis of mania directly aligns with thiothixene's D2 antagonism mechanism — the same rationale underlying haloperidol's established use in acute mania. Key supporting publications include:
>
> | PMID | Year | Type | Journal | Key Findings |
> |------|------|------|---------|-------------|
> | [3280617](https://pubmed.ncbi.nlm.nih.gov/3280617/) | 1988 | Controlled comparison trial (RCT-level) | J Clin Psychopharmacol | Double-blind trial: thiothixene vs. chlorpromazine in 29 manic patients on lithium — both comparably effective; thiothixene profile may allow faster dose escalation |
> | [6145189](https://pubmed.ncbi.nlm.nih.gov/6145189/) | 1984 | Controlled comparison trial | Prog Neuropsychopharmacol Biol Psychiatry | Double-blind: thiothixene vs. haloperidol for rapid tranquilization in manic and schizophrenic patients — both effective; thiothixene showed favorable effects on anergia |
> | [3711026](https://pubmed.ncbi.nlm.nih.gov/3711026/) | 1986 | Controlled comparison trial | J Clin Psychiatry | Thiothixene vs. loxapine for rapid tranquilization — significant clinical improvement on CGI and BPRS scales with both drugs across 58 acutely disturbed psychotic patients |
> | [11249804](https://pubmed.ncbi.nlm.nih.gov/11249804/) | 2000 | Review | Bipolar Disord | Review of latency of antipsychotic response in acute mania — relevant context for thiothixene's speed of action |
> | [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Systematic review | J Clin Psychiatry | Systematic review of typical and atypical antipsychotic efficacy for anxiety in bipolar disorder and major depression |
> | [2106533](https://pubmed.ncbi.nlm.nih.gov/2106533/) | 1990 | Clinical trial | J Clin Psychopharmacol | Retrospective review of adjunctive clonazepam in 20 bipolar patients — neuroleptics (including thiothixene) used as maintenance comparator |
> | [5725619](https://pubmed.ncbi.nlm.nih.gov/5725619/) | 1968 | Early clinical study | Psychosomatics | Early report on antipsychotic and antidepressant properties of thiothixene |
> | [5662268](https://pubmed.ncbi.nlm.nih.gov/5662268/) | 1968 | Pilot study | Can Psychiatr Assoc J | Pilot study of thiothixene in the treatment of mania |
> | [19164500](https://pubmed.ncbi.nlm.nih.gov/19164500/) | 2010 | Case report | J Psychopharmacol | Adverse event report (spontaneous ejaculation) in bipolar patient — contextual reference to thiothixene's known sexual side effect profile |
> | [3571177](https://pubmed.ncbi.nlm.nih.gov/3571177/) | 1987 | Case report (adverse event) | J Clin Psychiatry | Priapism associated with thiothixene, chlorpromazine, and thioridazine — safety signal relevant to bipolar management context |
>
> **However**, this direction has limited clinical utility today: thiothixene is no longer marketed in the US, it carries a less favorable side effect profile (extrapyramidal symptoms, tardive dyskinesia risk) compared to modern atypical antipsychotics, and approved alternatives for bipolar mania already exist. A separate focused evaluation report for this indication would be warranted if there is a specific formulary or access reason to revisit thiothixene.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


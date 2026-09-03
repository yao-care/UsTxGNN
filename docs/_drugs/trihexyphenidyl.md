---
layout: default
title: Trihexyphenidyl
parent: 僅模型預測 (L5)
nav_order: 1263
evidence_level: L5
indication_count: 10
---

# Trihexyphenidyl
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

Using no skill (report-writing task, direct template compliance — no matching skill needed).

# Trihexyphenidyl: From Parkinsonism to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

> Trihexyphenidyl is a central anticholinergic agent historically used to manage Parkinsonism and drug-induced extrapyramidal symptoms (inferred from mechanistic evidence text; formal indication/MOA records are a data gap).
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> but this is currently supported by **0 clinical trials** and only **1 loosely related publication**, and the model's own mechanistic rationale argues *against* plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (no license records); pharmacologically an anticholinergic historically used for Parkinsonism / drug-induced extrapyramidal symptoms, per mechanistic text in the evidence |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US/Taiwan Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available from DrugBank (flagged as a High-severity data gap). Based on the descriptive text accompanying the TxGNN prediction, trihexyphenidyl is understood to be a central M1 muscarinic receptor antagonist that reduces striatal cholinergic activity, an action traditionally used to relieve extrapyramidal symptoms such as Parkinsonism and drug-induced dystonia.

There is **no established mechanistic pathway** connecting this anticholinergic action to the core symptoms of ADHD (inattention/hyperactivity). In fact, the evidence pack's own repurposing rationale states the opposite: anticholinergic drugs are more likely to *cause* cognitive side effects such as memory and attention impairment, which would work against — not for — an ADHD indication. The single supporting literature entry (a case series on tic disorder with dystonia) does not discuss ADHD directly.

Taken together, this prediction should be treated as a statistical association from the knowledge graph rather than a mechanistically or clinically grounded signal at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Case series (Tier 3) | Movement Disorders | Describes a clinical series of primary tic disorder co-occurring with dystonia; does not directly address ADHD or trihexyphenidyl efficacy in ADHD. |

---

## US Market Information

The drug is currently **not marketed** and no license/NDA records are available in the evidence pack (total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available; TFDA label/warning retrieval is flagged as a **Blocking** data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is minimal (evidence level L5, decision stage S0) — no clinical trials and only a single, indirectly relevant case series support this indication. The model's own mechanistic rationale actively argues against plausibility, since anticholinergic agents are more commonly associated with cognitive impairment than with symptomatic improvement in ADHD.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (currently a Blocking data gap — required before any safety pre-assessment)
- Confirmed mechanism of action from DrugBank or primary literature
- Preclinical or clinical studies directly evaluating trihexyphenidyl in ADHD populations
- A safety/monitoring plan addressing anticholinergic cognitive side effects if this candidate is ever advanced
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


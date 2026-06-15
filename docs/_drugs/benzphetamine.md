---
layout: default
title: Benzphetamine
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 4
---

# Benzphetamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

The skill confirms this is a standard TxGNN pipeline task. Now let me generate the evaluation report based on the Evidence Pack.

---

# BENZPHETAMINE: From Obesity to Hypervitaminosis

## One-Sentence Summary

Benzphetamine is a sympathomimetic amine anorectic, originally used for short-term management of exogenous obesity in adults.
The TxGNN model predicts it may be effective for **Hypervitaminosis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction is based solely on knowledge graph topology and should be interpreted with caution.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Obesity (short-term appetite suppression; no US license record found in this dataset) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacology, benzphetamine is a sympathomimetic amine of the amphetamine class that acts centrally as a norepinephrine-dopamine releasing agent (NDRA), suppressing appetite through stimulation of the hypothalamic satiety center. Its established use is short-term adjunctive treatment of exogenous obesity.

Hypervitaminosis refers to toxicity caused by excessive accumulation of fat-soluble vitamins (primarily vitamins A and D), most commonly from supplement overuse or fortified food exposure. The condition is mechanistically driven by lipid metabolism dysregulation, hepatic storage overload, and receptor-mediated signaling disturbance — none of which have a known direct causal relationship with catecholaminergic signaling.

The TxGNN knowledge graph rationale suggests a possible connection via shared metabolic network nodes, where sympathomimetic-driven metabolic changes may superficially overlap with vitamin metabolism pathways in the graph structure. However, this is assessed as a likely false-positive signal: the mechanistic bridge between NDRA pharmacology and hypervitaminosis pathophysiology is tenuous, and no biological hypothesis justifies therapeutic use. **This prediction should not be taken as a repurposing candidate without substantial preclinical validation.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No US NDA records were found for Benzphetamine in this dataset. Benzphetamine was historically marketed in the United States under the brand name **Didrex** (Pharmacia) as a Schedule III controlled substance for short-term obesity management, but the brand has been discontinued. Generic formulations may have existed; however, no active license records are captured in the current data pipeline output.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Benzphetamine belongs to the amphetamine class and carries well-known class-level risks including cardiovascular stimulation (elevated heart rate and blood pressure), CNS stimulation, abuse/dependence potential, and contraindication in patients with cardiovascular disease, hyperthyroidism, glaucoma, or history of drug abuse. These risks should be factored into any repurposing evaluation, even in the absence of structured safety data in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high mathematical score (99.98%) to the benzphetamine → hypervitaminosis prediction, but this is a purely model-driven signal with zero supporting clinical trials, zero published literature, and a mechanistic rationale that is biologically implausible. The predicted indication (hypervitaminosis) is a toxicity state, not a target for pharmacological intervention with a sympathomimetic agent.

**To proceed, the following would be needed:**

- Detailed MOA data from DrugBank to formally assess any pathway overlap with vitamin metabolism
- Preclinical hypothesis generation: identify any plausible biological mechanism by which NDRA activity could influence vitamin A/D metabolism or receptor signaling
- Expert panel review to rule out ontology artifact (false-positive KG node connection) as the source of this prediction
- Re-evaluation with next-ranking indications (#2–#4) to determine if any alternative predicted indication carries stronger mechanistic plausibility
- US FDA label retrieval for Benzphetamine to complete safety profiling before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


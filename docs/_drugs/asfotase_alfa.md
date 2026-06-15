---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

以下是根據 Evidence Pack 產生的評估報告：

---

# Asfotase Alfa: From Hypophosphatasia to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies

## One-Sentence Summary

Asfotase alfa (Strensiq®) is a recombinant tissue-nonspecific alkaline phosphatase (TNSALP) enzyme replacement therapy, originally developed and approved for hypophosphatasia (HPP) — a rare inherited disorder in which TNSALP deficiency leads to toxic accumulation of inorganic pyrophosphate (PPi) and consequent failure of bone and tooth mineralization.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**, yet with **0 clinical trials** and **0 publications** currently supporting this specific direction, the prediction rests entirely on graph-level inference with no supporting biological or clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypophosphatasia (HPP) — perinatal/infantile/juvenile-onset |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | Not marketed (0 licenses on record) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Asfotase alfa is a recombinant fusion protein comprising the catalytic domain of human TNSALP, the Fc region of human IgG1 for extended half-life, and a deca-aspartate peptide tail for targeted bone mineral binding. In HPP, loss-of-function mutations in the *ALPL* gene eliminate TNSALP activity, causing extracellular PPi to accumulate. PPi is a potent inhibitor of hydroxyapatite crystal formation; TNSALP supplementation restores PPi hydrolysis, re-enables physiological bone and tooth mineralization, and prevents the life-threatening respiratory and neurological complications of severe HPP.

Mitochondrial OXPHOS disorders due to nuclear DNA anomalies arise from an entirely distinct mechanism: mutations in nuclear-encoded structural or assembly-factor genes disable one or more respiratory chain complexes (I–V), impairing oxidative phosphorylation and ATP generation at the inner mitochondrial membrane. The mechanistic overlap with TNSALP biology is negligible. Elevated extracellular PPi could theoretically exert indirect effects on mitochondrial membrane potential in a reductive-stress context, but no such pathway has been demonstrated in vivo, and TNSALP supplementation cannot correct nuclear gene mutations, rescue respiratory chain complex assembly, or restore cellular ATP production.

The high TxGNN score most likely reflects graph-level proximity in the knowledge network: asfotase alfa and OXPHOS disorders both belong to the rare metabolic disease neighbourhood, sharing phenotypic nodes such as skeletal abnormalities, multisystem involvement, and childhood onset. This is a well-recognised source of false positives in network-based repurposing models. Without a credible mechanistic hypothesis or any preclinical signal, this candidate should be considered a **knowledge graph artifact** rather than a biologically actionable prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Asfotase alfa currently has no licenses recorded in this dataset (0 authorizations on file).

> **Discrepancy note**: Asfotase alfa (Strensiq®, Alexion/AstraZeneca) received FDA approval on 23 October 2015 for perinatal/infantile-onset and juvenile-onset HPP, and EMA approval on 28 August 2015. The absence of records in this Evidence Pack likely reflects a gap in the data pipeline rather than the actual regulatory status. Prescribers should consult current FDA prescribing information (NDA 125513) for authoritative labeling.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns an exceptionally high score (99.95%), the mechanistic pathway connecting TNSALP enzyme replacement to mitochondrial respiratory chain dysfunction caused by nuclear DNA mutations is not scientifically supportable — asfotase alfa cannot correct genetic defects, restore respiratory chain complex assembly, or compensate for cellular energy failure. There is zero clinical trial or literature evidence for this indication, placing it squarely at evidence level L5 (model prediction only).

**To proceed, the following would be needed:**
- A plausible mechanistic hypothesis demonstrating how extracellular PPi hydrolysis could modulate mitochondrial OXPHOS function (currently absent)
- Preclinical data (in vitro cellular models or animal models of OXPHOS disorder) showing any measurable biological effect of asfotase alfa on respiratory chain activity or ATP production
- Expert review by a mitochondrial medicine specialist to formally assess biological plausibility before any clinical investigation is considered
- Resolution of the regulatory data gap: confirm current FDA/TFDA approval and labeling status and retrieve full safety information from the official package insert
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


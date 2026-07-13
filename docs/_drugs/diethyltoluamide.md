---
layout: default
title: Diethyltoluamide
parent: 僅模型預測 (L5)
nav_order: 605
evidence_level: L5
indication_count: 8
---

# Diethyltoluamide
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

# DIETHYLTOLUAMIDE (DEET): From Insect Repellent to Insomnia

## One-Sentence Summary

DIETHYLTOLUAMIDE (DEET) is a widely used insect repellent, registered as a consumer pesticide rather than a pharmaceutical drug, with no approved therapeutic indication on record. The TxGNN model assigns it the highest predicted score for **Insomnia** (99.67%), yet there are **0 clinical trials** and **0 publications** supporting this direction. Mechanistic analysis of all 8 top-ranked predictions suggests these are knowledge graph structural false positives rather than viable repurposing candidates.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Insect repellent (consumer pesticide; no pharmaceutical indication on record) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (as a pharmaceutical drug) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

DEET (N,N-Diethyl-meta-toluamide) exerts its known biological action by activating TRPA1 channels in arthropod olfactory neurons, causing insects to avoid treated hosts. It is not a traditional pharmaceutical agent and carries no approved human therapeutic indication. Its pharmacological footprint in humans is largely defined by its toxicity profile — at high doses it produces CNS adverse effects including seizures, agitation, and ataxia — effects that are the **opposite** of sleep promotion.

For insomnia, effective drugs act on GABA-A receptors (benzodiazepines, z-drugs), histamine H₁ receptors (doxylamine), the orexin system (suvorexant), or the melatonin pathway. DEET has no known positive modulatory activity at any of these targets, nor on the adenosine system that accumulates sleep pressure. The available mechanistic rationale therefore does **not** support the insomnia prediction.

The same pattern holds across all 8 top-ranked predictions in this evidence pack. Notably, ranks 4–6 are three different coagulation disorder diagnoses whose TxGNN scores converge within 0.0004 of each other — a hallmark signature of knowledge graph neighbourhood clustering producing co-elevated false positives rather than genuine pharmacological signals. This report therefore treats all 8 predictions as requiring disqualification pending artifact analysis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

DIETHYLTOLUAMIDE holds no NDA, BLA, or equivalent pharmaceutical approval in the United States. It is regulated by the US Environmental Protection Agency (EPA) as a pesticide active ingredient for consumer insect repellent products, which falls entirely outside the FDA drug approval pathway.

---

## All Predicted Indications — Artifact Assessment

Because all 8 predictions share the same evidence level (L5) and each carries a mechanistic rationale arguing against biological plausibility, a summary table is provided to support triage decisions.

| Rank | Predicted Indication | Score | Key Artifact Signal |
|------|----------------------|-------|---------------------|
| 1 | Insomnia | 99.67% | No GABAergic / adenosine mechanism; known CNS stimulant toxicity contradicts prediction |
| 2 | ADHD, inattentive type | 99.57% | Weak AChE inhibition does not address dopamine/NE deficit; cholinergic crisis risk |
| 3 | Specific developmental disorder | 99.44% | Animal data shows DEET impairs neurodevelopment — negative direction from therapeutic target |
| 4 | Factor 5 excess / thrombosis | 99.16% | No coagulation factor V modulation; likely coagulation-node cluster artifact |
| 5 | Antithrombin deficiency type 2 | 99.16% | Score differs from rank 4 by only 0.00002; cluster artifact confirmed |
| 6 | Heparin cofactor 2 deficiency | 99.12% | Third consecutive coagulation disorder; score convergence ≈ 0.0004 across all three |
| 7 | Migraine disorder | 99.07% | TRPA1 activation is a nociceptive stimulus — may aggravate rather than relieve migraine |
| 8 | ADHD (broad diagnostic code) | 99.06% | Duplicate of rank 2 from ontology node split; score gap of 0.005 further reduces confidence |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every one of the 8 TxGNN-predicted indications for DEET is unsupported by clinical or literature evidence (all L5), and the accompanying mechanistic analysis actively contradicts biological plausibility in each case. The prediction output exhibits multiple red flags for systematic knowledge graph artifacts — near-identical score clusters across a coagulation disease group, duplicated ADHD ontology entries, and CNS toxicity that runs opposite to predicted therapeutic directions. DEET is not a pharmaceutical compound and lacks a regulatory development pathway as a drug.

**To proceed, the following is needed:**

- **Artifact filtering**: Computational re-analysis to distinguish KG topological false positives from any residual biologically plausible signal before any indication is re-prioritized
- **Basic pharmacological profiling**: In vitro binding assays at human CNS targets (GABA-A, orexin, adenosine) and coagulation cascade components to empirically ground or refute the model's predictions
- **MOA data** (DG002): Retrieve full DrugBank mechanism-of-action record to characterise DEET's human off-target activity map
- **Safety reassessment**: If any indication survives artifact filtering, a formal neurotoxicity risk assessment at therapeutic-dose exposures is mandatory before clinical translation is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


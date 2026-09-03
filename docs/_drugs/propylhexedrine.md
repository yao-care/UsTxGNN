---
layout: default
title: Propylhexedrine
parent: 僅模型預測 (L5)
nav_order: 1094
evidence_level: L5
indication_count: 10
---

# Propylhexedrine
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

# Propylhexedrine: From Nasal Congestion to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

Propylhexedrine is an indirect-acting sympathomimetic amine traditionally used as an over-the-counter nasal decongestant (e.g., inhaler form for nasal congestion). The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**, but currently **no clinical trials** and **no supporting literature** exist for this specific drug-indication pair — the prediction rests solely on structural/mechanistic similarity within the knowledge graph.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nasal congestion (OTC decongestant; no formal indication record in evidence pack) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, propylhexedrine is an indirect-acting sympathomimetic amine, structurally related to amphetamine, that promotes release of norepinephrine (and to a lesser extent dopamine) from presynaptic nerve terminals. Its traditional OTC use is as a nasal decongestant, exploiting local vasoconstriction (α1-adrenergic effect) rather than central stimulant effects.

The mechanistic rationale for ADHD stems from the fact that ADHD is commonly treated with stimulant medications (e.g., amphetamine, methylphenidate) that act by increasing synaptic norepinephrine and dopamine availability — a mechanism class propylhexedrine shares structurally. However, propylhexedrine has never been studied or approved for CNS/behavioral indications, and its clinical pharmacokinetics, dosing, and CNS penetration for this purpose are not established. This is a knowledge-graph structural-similarity inference (TxGNN score 99.97%, rank 1277) rather than an evidence-based signal — there are zero clinical trials or publications directly linking propylhexedrine to ADHD.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

No license or NDA records are available in the evidence pack. Propylhexedrine's regulatory status is recorded as **Not Marketed**, with **0 total licenses** on file.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Warnings, contraindications, and drug interaction data are currently unavailable (flagged as a Blocking data gap — TFDA label/contraindication data — in the source evidence pack), which prevents completion of a formal initial safety assessment (S1 stage).*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by knowledge-graph structural similarity (Evidence Level L5) with zero clinical trials and zero literature directly linking propylhexedrine to ADHD. Combined with a Blocking-severity data gap on TFDA warnings/contraindications and a High-severity gap on mechanism of action, there is currently insufficient basis to advance this candidate beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA (or equivalent regulatory) label data — warnings, contraindications — to complete the S1 safety screen
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Preclinical or pharmacokinetic data establishing CNS bioavailability relevant to ADHD
- Identification of any real-world/off-label use signals or case reports as a starting evidence base before considering formal trial design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


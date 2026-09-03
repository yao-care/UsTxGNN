---
layout: default
title: Phentermine
parent: 僅模型預測 (L5)
nav_order: 1040
evidence_level: L5
indication_count: 4
---

# Phentermine
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

# Phentermine: From Appetite Suppression to Hypervitaminosis

## One-Sentence Summary

> Phentermine is a sympathomimetic amine typically used as an appetite suppressant, though no confirmed original indication is documented in this evidence pack.
> The TxGNN model predicts a possible link to **Hypervitaminosis**,
> but currently **0 clinical trials** and **0 publications** support this direction — the prediction is model-output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no `original_indications` or license data provided) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for phentermine (marked as a data gap). Based on the model's own rationale text, phentermine is understood as a sympathomimetic amine that promotes central norepinephrine release, historically associated with appetite suppression — but this has not been confirmed against a documented original indication in this evidence pack.

For the top-ranked prediction, hypervitaminosis, there is no known metabolic or toxicological mechanism connecting phentermine's central nervous system stimulant activity to vitamin-overdose pathology. The evidence pack's own repurposing rationale explicitly flags this: the high TxGNN score likely reflects **node proximity in the knowledge graph rather than a true biological mechanism**. The same caveat applies to the other ranked candidates (16p11.2 microdeletion syndrome, hypertelorism, frontorhiny) — all are structural/genetic disorders with no plausible pharmacological link to a sympathomimetic amine, and several involve obsolete or rare ontology terms that are more likely graph noise than genuine signal.

In short, this is a pure model-prediction case (L5) with no mechanistic, clinical, or literature support. None of the four ranked candidates should be treated as biologically credible without independent validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are not available in this evidence pack.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5), with zero clinical trials or literature evidence, and the model's own rationale suggests the top candidate association is likely an artifact of knowledge-graph proximity rather than genuine biology. The drug is also not currently marketed (0 licenses), and core safety data (MOA, TFDA warnings/contraindications) are missing — this is a **Blocking** data gap that prevents any S1 safety evaluation.

**To proceed, the following is needed:**
- Confirmed original indication and regulatory license data for phentermine
- Mechanism of action (MOA) data (currently a High-severity data gap)
- TFDA label warnings/contraindications (currently a Blocking-severity data gap)
- Independent mechanistic or preclinical evidence linking phentermine to hypervitaminosis before considering escalation beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


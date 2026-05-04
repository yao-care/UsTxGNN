---
layout: default
title: Acetaminophen Butalbital
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 0
---

# Acetaminophen Butalbital
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Acetaminophen + Butalbital: Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

Acetaminophen + Butalbital is a combination analgesic-barbiturate product, classically used for tension-type headaches in markets where it is approved (e.g., the United States under brand names such as Fioricet/Fiorinal).
The TxGNN model returned **no predicted new indications** for this combination, and the drug is **not currently marketed in Taiwan**, meaning no regulatory baseline exists for this jurisdiction.
The overall evidence base for repurposing evaluation is **insufficient at this time**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tension-type headache (based on global market knowledge; no Taiwan license found) |
| Predicted New Indication | None (TxGNN returned no candidates) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model returned no predictions |
| US Market Status | Not marketed in Taiwan (0 licenses on record) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, **Acetaminophen** acts as a centrally and peripherally acting analgesic/antipyretic (inhibiting prostaglandin synthesis), while **Butalbital** is a short-acting barbiturate that produces CNS depression and muscle relaxation, contributing to headache relief through sedation and vascular smooth muscle relaxation.

The combination's efficacy is well established in tension-type headaches and analgesic-associated headache syndromes in markets such as the United States, but it carries significant dependency and rebound headache risks due to the barbiturate component.

Because TxGNN returned zero repurposing candidates for this combination, **no mechanistic bridge to a new indication can be constructed at this stage**. Repurposing evaluation cannot proceed without at minimum one candidate indication for analysis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for a repurposing indication (TxGNN predicted no new indications).

---

## Literature Evidence

Currently no related literature available for a repurposing indication (TxGNN predicted no new indications).

---

## US Market Information

This drug combination has **no registered licenses in Taiwan**. No authorization table can be generated.

> For reference: In the United States, Acetaminophen + Butalbital ± Caffeine products (e.g., Fioricet, Fiorinal) have been marketed for tension headache, but these approvals are not reflected in the Taiwan TFDA database for this query.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** All safety fields (warnings, contraindications, drug interactions) returned data gaps in this Evidence Pack. Drug interaction data was also not found in the DDI query. Given that Butalbital is a **barbiturate** with known CNS depressant effects, clinicians should be aware of:
> - Potential for physical dependence and withdrawal
> - Additive CNS depression with alcohol, opioids, benzodiazepines
> - Hepatotoxicity risk from Acetaminophen in overdose or hepatic impairment
>
> These are general pharmacological considerations, not derived from structured data in this pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN returned no repurposing candidates for this combination, and the drug has no Taiwan regulatory baseline, no MOA data, and no safety data in this Evidence Pack — making a formal repurposing evaluation impossible at this stage.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001**: Retrieve TFDA package insert PDF to extract warnings and contraindications (severity: Blocking)
- **Resolve Data Gap DG002**: Query DrugBank API for MOA data (severity: High)
- **Re-run TxGNN** on individual components (Acetaminophen alone, Butalbital alone) to determine whether the combination's null result reflects a model limitation or a genuine absence of repurposing signal
- **Confirm jurisdictional scope**: Determine whether US NDA data (Fioricet/Fiorinal) should be incorporated as a surrogate regulatory baseline
- **Assess individual component candidates**: Acetaminophen has extensive repurposing literature (e.g., anti-inflammatory, antipyretic adjunct); evaluating components separately may yield actionable signals
- Once candidate indications are identified, re-generate the Evidence Pack with populated `predicted_indications` to proceed to a full L1–L5 evidence review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Acetaminophen Caffeine Pyrilamine
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 0
---

# Acetaminophen Caffeine Pyrilamine
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

# Acetaminophen / Caffeine / Pyrilamine: Drug Repurposing Evaluation Report

## One-Sentence Summary

Acetaminophen / Caffeine / Pyrilamine is a well-known over-the-counter combination used for analgesia, antipyresis, and antihistamine relief (commonly found in cold and menstrual pain products).
The TxGNN model returned **no predicted new indications** for this combination, likely because the drug combination lacks a mapped DrugBank ID in the knowledge graph.
Without predictions or regulatory registration data, this candidate currently **cannot be evaluated** through the standard repurposing workflow.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | — |
| Evidence Level | Not evaluable (no predictions in system) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why Evaluation Cannot Proceed

This combination drug consists of three components:

- **Acetaminophen (Paracetamol)**: Centrally-acting analgesic and antipyretic; inhibits prostaglandin synthesis in the CNS.
- **Caffeine**: Methylxanthine; potentiates the analgesic effect of acetaminophen by approximately 40% (adjuvant role), increases alertness via adenosine receptor antagonism.
- **Pyrilamine (Mepyramine)**: First-generation H1-antihistamine; provides antiallergic and mild sedative effects.

This combination is pharmacologically rational for treating headache, fever, and allergy-related symptoms. However, the TxGNN pipeline requires a mapped **DrugBank ID** to traverse the knowledge graph and generate repurposing candidates. Since `drugbank_id` is null in this Evidence Pack, the model could not locate this combination as a single entity in the graph.

> The absence of predictions reflects a **data pipeline issue**, not necessarily a lack of repurposing potential for the individual components.

---

## Clinical Trial Evidence

Currently no related clinical trials registered under this specific combination in the Evidence Pack.

---

## Literature Evidence

Currently no related literature available in the Evidence Pack.

---

## Taiwan Market Information

This drug combination has **0 registered licenses** in Taiwan and is currently **not marketed**. No authorization records are available to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Safety data (warnings, contraindications, drug-drug interactions) could not be retrieved for this combination entry. Individual component safety profiles should be consulted separately via DrugBank or official prescribing information:
> - Acetaminophen: hepatotoxicity risk at high doses; interactions with warfarin and alcohol
> - Caffeine: CNS stimulation; caution in anxiety disorders and cardiovascular disease
> - Pyrilamine: anticholinergic effects; CNS depression; avoid in elderly and patients with urinary retention or glaucoma

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produced no repurposing predictions because the combination lacks a mapped DrugBank ID, making knowledge graph traversal impossible. Without predictions, there is no scientifically grounded repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

- **Resolve DrugBank mapping**: Determine whether to evaluate each component (Acetaminophen, Caffeine, Pyrilamine) individually rather than as a fixed combination; retrieve individual DrugBank IDs (`DB00316`, `DB00201`, `DB01237` respectively)
- **Re-run TxGNN pipeline** using individual component IDs to generate per-component repurposing predictions
- **Retrieve MOA data** from DrugBank API for each component to enable mechanistic plausibility analysis
- **Clarify original indication scope**: Document the combination's approved uses (e.g., tension headache, cold/flu symptoms, dysmenorrhea) in the source regulatory database
- **Confirm regulatory intent**: If the target market is Taiwan, establish whether individual components or the fixed-dose combination is the object of evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


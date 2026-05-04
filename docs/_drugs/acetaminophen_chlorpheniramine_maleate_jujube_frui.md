---
layout: default
title: Acetaminophen Chlorpheniramine Maleate Jujube Frui
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 0
---

# Acetaminophen Chlorpheniramine Maleate Jujube Frui
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

# ACETAMINOPHEN + CHLORPHENIRAMINE MALEATE + JUJUBE FRUIT: No Repurposing Prediction Available

## One-Sentence Summary

This Evidence Pack covers a three-component combination product (acetaminophen, chlorpheniramine maleate, and jujube fruit) that is not currently marketed in any tracked regulatory database and carries no DrugBank ID on record. The TxGNN model returned **no predicted indications** for this combination, as the absence of a DrugBank ID prevents knowledge-graph embedding from generating disease-association scores. A meaningful repurposing evaluation cannot proceed without resolving the upstream data gaps identified below.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No data available |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — no predictions returned |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on publicly known pharmacology, this product combines three distinct agents: **acetaminophen** (analgesic and antipyretic), **chlorpheniramine maleate** (first-generation antihistamine that blocks H₁ receptors), and **jujube fruit** (a traditional East Asian botanical with reported sedative, anxiolytic, and digestive properties). This profile is characteristic of OTC cold-and-allergy combination products found in East Asian markets, but no approved indication is on record in any regulatory database queried.

The TxGNN model relies on a DrugBank ID to anchor a drug node within the heterogeneous knowledge graph. Without that anchor, the model cannot compute drug–disease embedding distances and therefore returns an empty prediction set. This is a pipeline input failure, not a negative prediction result — it means the combination has not been evaluated, not that it has been found ineffective.

Because the combination also lacks a recognized INN entry as a single entity, it is possible that each component exists independently in DrugBank and that splitting the query would yield meaningful repurposing signals for each component separately.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This combination has no DrugBank ID, no market authorization, no TxGNN predictions, and no safety data on record — the minimum inputs required for a repurposing evaluation are all absent.

**To proceed, the following is needed:**

- **Resolve the DrugBank ID issue:** Either locate an existing DrugBank entry for this specific combination, or split the query into three independent evaluations — `DB00316` (acetaminophen), `DB01114` (chlorpheniramine maleate), and a jujube fruit botanical entry — and re-run the TxGNN pipeline for each
- **Retrieve MOA data (DG002):** Query DrugBank API individually for each component to reconstruct a composite mechanism profile
- **Retrieve safety data (DG001):** Download and parse the package insert PDF from any market where this combination or its closest equivalent is authorized, to populate key warnings and contraindications
- **Verify brand identity:** Search regulatory databases under alternative spellings, brand names, or Chinese INN equivalents to confirm whether this combination is registered under a different identifier
- **Re-run the evidence pipeline** after the DrugBank ID is resolved to generate TxGNN predictions, clinical trial matches, and literature links
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


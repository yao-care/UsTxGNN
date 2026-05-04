---
layout: default
title: Activated Charcoal Ammonium Carbonate Antimony Ars
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Ammonium Carbonate Antimony Ars
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

# Multi-Component Archaic Compound: No Repurposing Indication Identified

## One-Sentence Summary

This entry describes an 11-component mixture containing activated charcoal, arsenic trioxide, antimony derivatives, sulfuric acid, and lobelia inflata — a profile consistent with 19th-century pharmacopoeial or homeopathic preparations rather than a modern pharmaceutical entity.
No regulatory approval exists in Taiwan, the compound lacks a DrugBank identifier, and the TxGNN model returned **no predicted new indications**, meaning this compound **cannot proceed to a standard repurposing evaluation at this time**.
Without a resolvable single active ingredient, all downstream evidence scoring is unavailable.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None — TxGNN returned no result |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — no actual studies; no model prediction returned |
| Taiwan Market Status | Not marketed (0 approvals) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The compound is a multi-ingredient mixture that does not correspond to any recognized single pharmaceutical entity in DrugBank or the TxGNN knowledge graph. The TxGNN model requires a resolvable DrugBank node to generate a repurposing score; because no DrugBank ID could be assigned to this mixture, no prediction was produced.

Several individual components do carry pharmacological history worth noting:

- **Activated charcoal** — broad-spectrum gastrointestinal adsorbent, still used in acute poisoning management
- **Arsenic trioxide (As₂O₃)** — the single component with a modern FDA-approved indication: acute promyelocytic leukemia (APL), marketed as Trisenox; however, approval is for a precisely formulated, standalone product, not as part of a mixture
- **Antimony potassium tartrate** — 19th-century emetic and antiparasitic; now largely obsolete and classified as toxic
- **Lobelia inflata** — historical respiratory stimulant containing lobeline, a nicotinic acetylcholine receptor partial agonist; not used in modern medicine
- **Ammonium carbonate / potassium carbonate** — historical expectorants and antacids
- **Sulfuric acid, bromine, chlorine, tin** — industrial or historical reagents with no recognized therapeutic role in combined oral preparations

As a combined formulation, the pharmacological interactions between these 11 components are undefined, and no published clinical data exists for the mixture as a whole.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

This compound has no regulatory licenses on file in Taiwan. No approved indication, dosage form, or product name is available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|-------------|-------------|---------------------|
| — | — | — | No records found |

---

## Safety Considerations

> **Important**: Although structured safety data is unavailable for this mixture, several individual components carry significant known hazards that warrant explicit attention:
>
> - **Arsenic trioxide** — classified as a Group 1 human carcinogen (IARC); acute toxicity includes QTc prolongation, hepatotoxicity, and peripheral neuropathy
> - **Antimony compounds (arsenate and potassium tartrate)** — hepatotoxic and cardiotoxic; antimony trioxide is a possible human carcinogen (IARC Group 2B)
> - **Sulfuric acid** — severe corrosive; causes chemical burns to mucous membranes and the gastrointestinal tract
> - **Bromine and chlorine** — halogen oxidants; pulmonary and mucosal irritants at even low exposures
> - **Tin** — inorganic tin compounds have renal and neurological toxicity at elevated doses
>
> Any future experimental use of this mixture would require a full preclinical toxicological characterization before any human administration can be considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The compound cannot be evaluated for drug repurposing because it cannot be resolved to a single DrugBank entity, carries no regulatory standing in Taiwan, and the TxGNN model returned no predicted indications. Multiple component substances are inherently hazardous without therapeutic justification for their combined use.

**To proceed, the following is needed:**

- **Identify the intended active ingredient**: Clarify whether this mixture corresponds to a named historical formulation (e.g., a 19th-century compound such as Fowler's solution or a homeopathic preparation) and isolate the pharmacologically relevant component
- **Re-run with a single-entity input**: If arsenic trioxide (As₂O₃) is the intended API, run a separate TxGNN query under DrugBank ID DB01169 (Arsenic trioxide / Trisenox) to obtain a legitimate repurposing prediction
- **Obtain MOA data**: Query DrugBank API for the resolved single-entity API
- **Toxicological risk assessment**: Commission a formal toxicology review of all 11 components and their interaction profile before any in vivo or clinical work
- **Regulatory pathway clarification**: Determine whether any regulatory authority has evaluated this mixture and, if so, retrieve the original indication and safety dossier
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


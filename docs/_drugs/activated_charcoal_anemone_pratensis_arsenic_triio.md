---
layout: default
title: Activated Charcoal Anemone Pratensis Arsenic Triio
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Anemone Pratensis Arsenic Triio
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

# Multi-Ingredient Compound (11 Components): Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This submission contains an 11-ingredient compound — including Activated Charcoal, Atropa Belladonna, Arsenic Triiodide, Strychnos Nux-Vomica Seed, and several botanical/mineral components — whose original indication, mechanism of action, and regulatory status are entirely undocumented in the current Evidence Pack. The TxGNN model returned **no predicted indications**, and the drug is **not registered in the US market**. Without a DrugBank ID or any mapped indication, no repurposing analysis can be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 (no predictions, no studies) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No repurposing prediction is available for this compound. The TxGNN knowledge graph requires a valid DrugBank ID to anchor the drug node in the graph — this compound has no DrugBank ID recorded, which explains why no candidate indications were generated.

The 11 listed ingredients span a highly heterogeneous pharmacological space: activated charcoal is an adsorptive agent used in toxicology; atropa belladonna and strychnos nux-vomica contain potent alkaloids (atropine/scopolamine and strychnine, respectively); arsenic triiodide is a heavy metal compound; and lycopodium clavatum and anemone pratensis are botanicals used in traditional/homeopathic medicine. The combination profile is consistent with a **homeopathic or complex traditional preparation**, where individual components may be present in highly diluted form.

Because no unified MOA, no regulatory license, and no mapped indication exist for this compound as a whole, it is not possible to reason about mechanistic applicability to any new indication without substantial additional data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

This compound has no US NDA filings on record. It is not a currently marketed product in the United States.

---

## Safety Considerations

Several components in this compound carry significant standalone toxicity concerns:

- **Arsenic Triiodide** — inorganic arsenic compound; systemic toxicity risk (peripheral neuropathy, hepatotoxicity, QTc prolongation) even at low doses
- **Atropa Belladonna** — source of atropine and scopolamine; anticholinergic toxidrome risk (tachycardia, urinary retention, confusion, hyperthermia)
- **Strychnos Nux-Vomica Seed** — primary source of strychnine; glycine antagonist causing muscular convulsions at low doses
- **Phosphorus** — elemental phosphorus is hepatotoxic

No formal drug–drug interaction data was retrieved. No package insert warnings or contraindications are on file for this compound as a whole.

> ⚠️ Given the presence of multiple highly toxic botanical and inorganic ingredients, any clinical evaluation must be preceded by a full toxicological characterization of the finished formulation, including the actual concentration of each active component.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no usable data for repurposing analysis — no DrugBank ID, no original indication, no TxGNN predictions, no clinical trials, and no literature. The heterogeneous and potentially toxic ingredient profile further elevates the data requirements before any development decision can be made.

**To proceed, the following is needed:**

- **Formulation clarification**: Confirm whether this is a homeopathic preparation (and if so, the dilution level of each ingredient) or a conventional fixed-dose combination
- **DrugBank ID resolution**: Map at least the primary active ingredient(s) to DrugBank to enable TxGNN graph traversal
- **Regulatory history**: Identify any prior approval in any jurisdiction (homeopathic registry, traditional medicine registry, etc.) to establish the original indication and safety context
- **Toxicology assessment**: Quantify actual concentrations of arsenic triiodide, strychnine, and belladonna alkaloids in the finished product
- **MOA documentation**: Define the intended mechanism or therapeutic rationale for the combination before re-submitting for TxGNN analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


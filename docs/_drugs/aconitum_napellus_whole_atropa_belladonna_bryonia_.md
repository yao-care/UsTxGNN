---
layout: default
title: Aconitum Napellus Whole Atropa Belladonna Bryonia 
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Atropa Belladonna Bryonia 
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

# Multi-Component Botanical/Homeopathic Combination: Drug Identity Unresolved — Repurposing Evaluation Not Possible

## One-Sentence Summary

This candidate consists of twelve botanical and homeopathic components (including Atropa belladonna, nitroglycerin, Tanacetum parthenium, and Strychnos nux-vomica), without a unified INN or DrugBank ID.
The TxGNN model returned **no predicted new indications** for this candidate, and the drug is **not currently marketed** in Taiwan.
Without drug identity resolution, mechanism data, or model output, a formal repurposing evaluation cannot be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only) — no output available |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why This Evaluation Cannot Proceed

This candidate is a twelve-component mixture of botanical and homeopathic substances, including:

- **Neurotoxic alkaloid sources**: Aconitum napellus, Atropa belladonna, Gelsemium sempervirens, Strychnos nux-vomica, Spigelia anthelmia
- **Fungal/ergot material**: Claviceps purpurea sclerotium (the source of ergotamine)
- **Conventional small-molecule drug**: Nitroglycerin
- **Herbal/phytomedicine components**: Bryonia alba, Melilotus officinalis, Milk thistle (Silybum marianum), Tanacetum parthenium (feverfew), Sepia officinalis

Because this is a **multi-component mixture without a unified DrugBank ID**, TxGNN's disease–gene–drug knowledge graph cannot resolve it to a single drug node. This explains why `predicted_indications` is empty. There is no single mechanism of action on record.

The presence of nitroglycerin (a vasodilator used in angina) alongside feverfew (historically used for migraine prophylaxis) suggests this may be a **homeopathic or naturopathic proprietary formula**, possibly targeting cardiovascular or headache indications — but this inference is speculative and unsupported by the data provided.

Currently, detailed mechanism of action data is not available. Based on known information, this combination lacks a unified pharmacological class, and no original approved indication could be confirmed from any regulatory source queried.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers**: Several components in this mixture carry significant inherent toxicity concerns even at low doses (e.g., Atropa belladonna contains atropine and scopolamine; Strychnos nux-vomica contains strychnine; Aconitum napellus contains aconitine). Any future clinical use assessment must include dedicated toxicological review of the full formulation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned no repurposing predictions for this candidate, likely because the multi-component mixture cannot be resolved to a single drug node in the knowledge graph. Without a unified drug identity, mechanism of action, safety profile, or regulatory history, no repurposing evaluation is possible at this stage.

**To proceed, the following is needed:**

1. **Drug identity resolution** — Confirm whether this mixture is a registered proprietary product (e.g., a homeopathic OTC product). If so, retrieve its brand name, manufacturer, and primary indication.
2. **DrugBank ID assignment** — Map each active component to its individual DrugBank entry, or identify if the combination has a composite entry.
3. **Mechanism of action data** — Characterize the pharmacological action of each component individually, then assess additive or synergistic effects.
4. **Regulatory verification** — Search TFDA, EMA, and US FDA homeopathic/OTC databases using the brand name (if known) rather than INN strings.
5. **TxGNN re-query by component** — Run TxGNN separately for key single-ingredient components (e.g., nitroglycerin, Tanacetum parthenium) to generate component-level repurposing hypotheses.
6. **Safety data collection** — Obtain the full product monograph or package insert to document known toxicity, contraindications, and drug interactions for the mixture.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


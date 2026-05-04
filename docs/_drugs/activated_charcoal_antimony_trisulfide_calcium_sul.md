---
layout: default
title: Activated Charcoal Antimony Trisulfide Calcium Sul
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Antimony Trisulfide Calcium Sul
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

# ACTIVATED CHARCOAL / ANTIMONY TRISULFIDE / CALCIUM SULFIDE / DAPHNE MEZEREUM BARK / POTASSIUM ARSENITE ANHYDROUS / SEMECARPUS ANACARDIUM JUICE / TOXICODENDRON PUBESCENS LEAF: Repurposing Evaluation Not Feasible

## One-Sentence Summary

This is a seven-component herbal-mineral combination containing substances from Ayurvedic and homeopathic traditions, currently not approved or marketed in Taiwan (or the United States).
The TxGNN pipeline returned **no predicted indications** for this combination, and **no clinical trials or literature** were retrieved.
Evaluation cannot proceed due to missing foundational data including regulatory approvals, mechanism of action, and model predictions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None identified |
| Predicted New Indication | None (no TxGNN output returned) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only (no actual studies via this pipeline) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction is Available

This candidate consists of seven heterogeneous active ingredients spanning multiple pharmacological categories:

- **Activated Charcoal** — a broad-spectrum adsorbent with no specific pharmacological target
- **Antimony Trisulfide** — a heavy-metal sulfide compound with undefined systemic activity
- **Calcium Sulfide** — a mineral historically used in homeopathic skin preparations
- **Daphne Mezereum Bark** — a botanical used in European folk medicine; contains toxic daphnin and mezerein
- **Potassium Arsenite Anhydrous** — an arsenic salt; historically associated with Fowler's Solution, used for various chronic conditions in the 19th century
- **Semecarpus Anacardium Juice** — used in Ayurvedic medicine; contains bhilawanols with reported cytotoxic activity in preclinical studies
- **Toxicodendron Pubescens Leaf** (Eastern Poison Oak) — used in homeopathic preparations at highly diluted doses

The TxGNN knowledge graph model requires a resolvable **DrugBank ID** to embed a compound into its drug-disease graph. Because this combination has no DrugBank registration, the model could not generate a prediction score or candidate indications. No original regulatory indication exists to anchor a repurposing hypothesis.

Currently, detailed mechanism of action data is not available. Based on available information, this appears to be a traditional compound preparation whose individual components span adsorbent, heavy-metal, botanical-alkaloid, and contact-allergen categories. Without a unified MOA or approved indication, a mechanistic bridge to any new indication cannot be established at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this combination.

---

## Literature Evidence

Currently no related literature available through this pipeline for this combination.

---

## Safety Considerations

Several components carry significant intrinsic hazard that warrants attention regardless of indication:

- **Potassium Arsenite Anhydrous**: Arsenic compounds are classified as Group 1 human carcinogens (IARC). Systemic exposure carries risks of peripheral neuropathy, skin malignancies, and haematological toxicity.
- **Daphne Mezereum Bark**: Contains daphnin and mezerein; ingestion may cause severe gastrointestinal toxicity and blistering.
- **Antimony Trisulfide**: Antimony compounds can cause cardiac arrhythmia and hepatotoxicity at systemic doses.
- **Toxicodendron Pubescens Leaf**: Contains urushiol; sensitization risk and severe allergic contact dermatitis.
- **Semecarpus Anacardium Juice**: Contains skin- and mucosa-irritating bhilawanols; reported genotoxic activity in some in vitro models.

Formal drug-drug interaction data were not found (query status: not found). Package insert warnings and contraindications are unavailable because this combination holds no regulatory approval in any identified jurisdiction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This combination lacks the minimum data required for a repurposing evaluation — no approved indication, no DrugBank ID for model embedding, no TxGNN prediction output, and no safety profile from a regulatory source. Several components (arsenic salts, antimony compounds, Daphne mezereum) carry serious toxicity signals that would require extensive safety characterisation before any forward-looking evaluation is appropriate.

**To proceed, the following is needed:**

- Resolve individual components as separate DrugBank entries and run component-level TxGNN predictions independently
- Identify the originating formulation or commercial product (e.g., Ayurvedic patent medicine, homeopathic black salve) to anchor the historical indication
- Conduct a systematic literature review for each active component individually (especially Semecarpus anacardium and Potassium arsenite, which have published preclinical oncology data)
- Obtain a full toxicological profile for arsenic- and antimony-containing fractions before any repurposing hypothesis is advanced
- Determine jurisdictional regulatory status (CDSCO, EMA, FDA homeopathic OTC framework) to assess whether any component has a recognised therapeutic category
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Anamirta Cocculus Whole Datura Stramonium Ferula A
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 0
---

# Anamirta Cocculus Whole Datura Stramonium Ferula A
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

# Multi-Ingredient Herbal/Mineral Complex: No Repurposing Prediction Available

## One-Sentence Summary

This candidate is a nine-ingredient complex product combining herbal, botanical, and mineral substances (including *Datura stramonium*, *Hyoscyamus niger*, silver nitrate, and valerian), with no regulatory registration in Taiwan and no matching DrugBank profile.
The TxGNN model returned **no predicted indications** for this candidate, as the complex multi-ingredient composition cannot be mapped to a single drug node in the knowledge graph.
As a result, no evidence-based repurposing assessment is possible at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Unknown — no registered indications on record |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (below L5: model returned no output) |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

This submission contains **nine distinct active ingredients**, each from different pharmacological origins:

| Ingredient | Known Pharmacological Class |
|---|---|
| Anamirta cocculus (whole) | Homeopathic — GABA-A antagonist (picrotoxin), used for vertigo/motion sickness |
| Datura stramonium | Anticholinergic alkaloids (atropine, scopolamine) |
| Ferula assa-foetida resin | Antispasmodic, traditional carminative |
| Hyoscyamus niger | Anticholinergic (hyoscine/scopolamine source) |
| Oat bran | Dietary fiber, lipid-lowering effect |
| Paeonia officinalis root | Anti-inflammatory, traditional sedative |
| Silver nitrate | Antiseptic, escharotic agent |
| Strychnos ignatii seed | CNS stimulant (strychnine, brucine) |
| Valeriana officinalis (whole) | Sedative, anxiolytic (GABAergic activity) |

TxGNN operates on a **single-drug node** mapped via DrugBank ID. A multi-ingredient preparation of this complexity — spanning homeopathic botanicals, alkaloid plants, a heavy metal salt, and a dietary fiber — cannot be resolved to any individual DrugBank entry. The DrugBank query returned one result but no DrugBank ID was assigned, confirming the mapping failed.

Additionally, several ingredients (e.g., *Strychnos ignatii* containing strychnine, *Datura stramonium* containing atropine-class alkaloids) carry significant **toxicity and narrow therapeutic index concerns** that would ordinarily require dedicated safety data before any repurposing evaluation proceeds.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this multi-ingredient combination.

---

## Literature Evidence

Currently no related literature available for this combination as a unified drug entity.

---

## Taiwan Market Information

This product has **0 registered licenses** with Taiwan FDA. It is not approved or marketed in Taiwan.

---

## Safety Considerations

> Please refer to individual ingredient package inserts and monographs for safety information.

Several ingredients in this complex carry **intrinsic toxicity concerns** that warrant attention even without formal safety data on file:

- **Datura stramonium** and **Hyoscyamus niger**: Source plants for atropine, hyoscine, and scopolamine. Anticholinergic toxidrome risk (tachycardia, mydriasis, urinary retention, CNS effects).
- **Strychnos ignatii seed**: Contains strychnine — a convulsant with a very narrow margin between therapeutic and toxic dose.
- **Silver nitrate**: Caustic and potentially cytotoxic at higher concentrations; risk of argyria with systemic exposure.
- **Anamirta cocculus**: Contains picrotoxin, a GABA-A receptor antagonist; convulsant in overdose.

These ingredients present compounding risks that are not addressed by available data in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate cannot be evaluated through the standard TxGNN repurposing pipeline because the multi-ingredient composition does not resolve to a mappable single-drug node, and the pipeline returned zero predicted indications. Several individual components carry significant safety concerns that have not been characterized for this combination.

**To proceed, the following is needed:**

- **Clarify product identity**: Determine whether this is a homeopathic preparation, a traditional medicine compound, or an investigational combination; obtain the product's approved INN or brand name if available.
- **Disaggregate for analysis**: If repurposing assessment is desired, evaluate each pharmacologically active ingredient separately (particularly *Datura stramonium* alkaloids and *Valeriana officinalis*) through individual TxGNN queries.
- **Resolve DrugBank mapping**: A DrugBank query returned 1 result but no ID was assigned — retrieve and confirm the matched entry.
- **Conduct safety review**: Before any further evaluation, compile toxicity data for the highest-risk ingredients (strychnine, atropine-class alkaloids, silver nitrate).
- **Confirm regulatory intent**: Verify whether Taiwan TFDA registration is being sought, and under which drug category (conventional, herbal, homeopathic).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


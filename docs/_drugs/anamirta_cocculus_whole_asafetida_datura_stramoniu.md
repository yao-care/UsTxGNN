---
layout: default
title: Anamirta Cocculus Whole Asafetida Datura Stramoniu
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 0
---

# Anamirta Cocculus Whole Asafetida Datura Stramoniu
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

# Multi-Component Botanical Preparation: Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This submission contains a nine-component botanical/mineral mixture (including *Datura stramonium*, *Hyoscyamus niger*, *Valeriana officinalis*, silver nitrate, and others) that is not currently marketed in any jurisdiction captured in this dataset.
The TxGNN model **did not generate any repurposing predictions** for this candidate, likely because the complex multi-component formulation could not be mapped to a single DrugBank identifier or a known mechanism of action.
Without a predicted indication, a clinical evidence review, or regulatory history to anchor the analysis, **no repurposing evaluation can be completed at this stage**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no regulatory approval records found |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction only; no actual studies |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN pipeline requires a resolvable DrugBank identifier to anchor the drug node in the knowledge graph. This submission's active substance is a nine-component mixture:

| # | Component | Known Pharmacological Class |
|---|-----------|---------------------------|
| 1 | *Anamirta cocculus* whole | Picrotoxin source (GABA antagonist) |
| 2 | Asafetida | Antispasmodic resin (traditional) |
| 3 | *Datura stramonium* | Tropane alkaloids (anticholinergic) |
| 4 | *Hyoscyamus niger* | Tropane alkaloids (anticholinergic) |
| 5 | Oat bran | Dietary fibre |
| 6 | *Paeonia officinalis* root | Anti-inflammatory phytochemical |
| 7 | Silver nitrate | Antiseptic/caustic mineral |
| 8 | *Strychnos ignatii* seed | Strychnine source (CNS stimulant) |
| 9 | *Valeriana officinalis* whole | Sedative/anxiolytic |

Several components contain potent alkaloids (*Datura*, *Hyoscyamus*, *Strychnos*) that are individually well-characterised but are used here as part of what appears to be a **homeopathic or traditional multi-herb formula**. Homeopathic formulations typically contain ingredients at highly diluted concentrations where standard pharmacokinetic assumptions do not apply, making knowledge-graph drug–disease edge construction unreliable.

Because no single DrugBank ID was returned and no original indication was recorded, the model had no valid starting node and produced zero candidate disease predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No regulatory approvals found in the US or any jurisdiction covered by this dataset.

---

## Safety Considerations

Several components in this mixture carry well-known toxicity profiles that would be relevant if this preparation were to advance:

- **Anticholinergic risk**: *Datura stramonium* and *Hyoscyamus niger* both contain scopolamine and hyoscyamine. Overdose risk is serious and the therapeutic window is narrow.
- **CNS stimulant/convulsant risk**: *Strychnos ignatii* seed contains strychnine and brucine. Even small doses can cause tetanic convulsions.
- **GABA antagonism**: *Anamirta cocculus* contains picrotoxin, a CNS stimulant and convulsant.
- **Caustic mineral**: Silver nitrate is corrosive at non-homeopathic concentrations.

If this is intended as a **homeopathic preparation** (highly diluted), the toxicity concerns above may not apply at the dispensed dose — but this must be confirmed by the submitter before any safety assessment can proceed.

Please refer to individual component monographs and the full prescribing information for detailed safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline could not process this submission because the multi-component nature of the formulation prevented mapping to a DrugBank node, resulting in zero repurposing predictions. Without a predicted indication there is no repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

- [ ] **Clarify formulation type**: Confirm whether this is a homeopathic preparation (with declared dilution levels) or a conventional botanical/polyherbal product — the analytical pathway differs substantially.
- [ ] **Identify the intended primary indication**: Provide the historical or traditional use claim so that a baseline therapeutic area can be established.
- [ ] **Resolve a DrugBank identifier**: If the formulation has a lead active ingredient (e.g., the anticholinergic fraction), map that ingredient to a DrugBank ID so TxGNN can generate predictions.
- [ ] **Obtain regulatory status documentation**: If approved in any jurisdiction under a traditional medicine category, supply the registration number and approved indication text.
- [ ] **Conduct a component-level safety review**: Given the presence of strychnine, tropane alkaloids, and silver nitrate, a toxicology summary for each active component is required before any clinical development discussion.
- [ ] **Re-run TxGNN** after the above data gaps are resolved, targeting a single lead indication per component or the formulation as a whole.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


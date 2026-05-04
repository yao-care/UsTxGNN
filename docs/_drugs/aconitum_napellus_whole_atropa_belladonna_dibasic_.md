---
layout: default
title: Aconitum Napellus Whole Atropa Belladonna Dibasic 
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Atropa Belladonna Dibasic 
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

# Multi-Ingredient Homeopathic/Botanical Complex: Insufficient Data for TxGNN Repurposing Analysis

## One-Sentence Summary

This candidate is a multi-component preparation containing eight botanical and mineral ingredients — including *Aconitum napellus*, *Atropa belladonna*, *Hypericum perforatum*, *Lytta vesicatoria*, and *Spigelia anthelmia* — that is consistent with a classical homeopathic combination formula.
The TxGNN model returned **no repurposing predictions** for this candidate; no predicted indications, supporting clinical trials, or literature are available in the current Evidence Pack.
This report therefore focuses on documenting known data gaps and outlining the minimum information required before a formal repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no approved indications on record |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (no prediction generated; no actual studies identified) |
| Market Status | Not marketed (Taiwan) |
| Number of Approved Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this candidate, so no mechanistic rationale can be formally evaluated at this stage.

This preparation contains eight distinct ingredients spanning classical homeopathic botanical extracts and inorganic mineral salts. The botanical components — *Aconitum napellus*, *Atropa belladonna*, *Hypericum perforatum*, *Lytta vesicatoria*, and *Spigelia anthelmia* — are found in several established homeopathic combination products used historically for neuralgic pain, acute inflammation, and autonomic nervous system complaints. The mineral components (dibasic potassium phosphate, ferrosoferric phosphate, magnesium phosphate dibasic trihydrate) are Schüssler-type tissue salts commonly included as supportive mineral supplements.

Because no DrugBank ID was resolved for this multi-ingredient combination, the TxGNN model — which relies on DrugBank identifiers as anchors in the knowledge graph — could not generate a scored prediction. Individually mapping each of the eight components to their respective DrugBank entries and re-running the pipeline would be the recommended next step to unlock meaningful repurposing predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

This product holds **no current regulatory authorization** on record. No approved licenses were found for this multi-ingredient combination in the queried database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | (None found) | — | — |

---

## Safety Considerations

No official safety warnings or contraindications were retrievable from the current Evidence Pack. Please refer to the package insert for safety information.

As a general reference, individual components carry the following pharmacological-level safety considerations that may be relevant if the formulation is **not** prepared at homeopathic ultra-dilution:

- **Aconitum napellus**: Contains aconitine alkaloids; cardiotoxic and neurotoxic with a narrow therapeutic index. Fatalities have been reported from non-diluted preparations.
- **Atropa belladonna**: Anticholinergic alkaloids (atropine, hyoscine); risk of anticholinergic toxidrome at pharmacological doses.
- **Lytta vesicatoria (Cantharis)**: Source of cantharidin, a potent vesicant and nephrotoxin; strictly regulated or prohibited in pharmacological-dose products in many jurisdictions.
- **Hypericum perforatum**: A well-documented CYP3A4/P-gp inducer; clinically significant drug interactions with antiretrovirals, immunosuppressants, anticoagulants, and oral contraceptives even at herbal supplement doses.

If the intended formulation is homeopathic (≥6C dilution), the toxicological risk from the above components is generally regarded as minimal. Regulatory classification of the preparation should be confirmed before applying these concerns to a safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no repurposing predictions for this candidate because a DrugBank ID could not be resolved for the multi-ingredient combination, and all critical drug-level data — approved indication, mechanism of action, and safety warnings — are currently unavailable. A meaningful repurposing evaluation cannot be conducted without resolving these foundational gaps first.

**To proceed, the following is needed:**

- **Confirm product identity**: Identify the commercial brand name, registered formulation, and the dilution/concentration of each of the eight components, so the preparation type (homeopathic vs. pharmacological-dose botanical) can be established.
- **Resolve DrugBank mapping (DG002)**: Map each individual ingredient to its respective DrugBank ID and re-run the TxGNN prediction on each component separately, then aggregate results.
- **Obtain regulatory package insert (DG001)**: Retrieve TFDA or equivalent authority documentation to establish approved indications, contraindications, and warnings before safety evaluation.
- **Determine regulatory classification**: Confirm whether this product is regulated as a homeopathic drug, botanical supplement, or conventional pharmaceutical — this determines which safety and efficacy standards apply and which repurposing pathways are feasible.
- **Re-run Evidence Pack generation**: After resolving DG001 and DG002, regenerate the Evidence Pack to populate predicted indications, clinical trial evidence, and literature evidence sections.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


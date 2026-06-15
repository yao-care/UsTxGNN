---
layout: default
title: Aluminum Oxide Antimony Potassium Tartrate Baptisi
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 0
---

# Aluminum Oxide Antimony Potassium Tartrate Baptisi
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

# Multi-Ingredient Vaccinia/Herbal Complex: Insufficient Data for Drug Repurposing Analysis

## One-Sentence Summary

This candidate is a complex 12-component product combining homeopathic agents, botanical extracts, and live vaccinia virus antigens, with no established single active ingredient or approved indication in any jurisdiction.
The TxGNN model was unable to generate repurposing predictions due to the absence of a DrugBank identifier and the multi-component nature of the formulation.
Currently, **no clinical trial evidence** and **no literature evidence** are available to support any repurposing direction under the standard pipeline.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available |
| Predicted New Indication | Not available — TxGNN could not process this candidate |
| TxGNN Prediction Score | Not available |
| Evidence Level | N/A (no prediction generated; below L5) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is No Prediction Available?

This product contains 12 declared ingredients spanning four distinct categories:

- **Homeopathic agents**: Mercurius Solubilis, Antimony Potassium Tartrate, Daphne Mezereum Bark
- **Botanical/herbal immunomodulators**: Echinacea Angustifolia, Goldenseal (*Hydrastis canadensis*), Baptisia Tinctoria, Thuja Occidentalis
- **Excipients/carriers**: Aluminum Oxide, Silicon Dioxide, Sodium Chloride
- **Live biological antigens**: Vaccinia Virus, Vaccinia Virus Strain New York City Board of Health (NYCBOH) Live Antigen

The TxGNN knowledge graph operates on individual drug entities mapped to DrugBank identifiers. This multi-ingredient complex has no DrugBank ID assigned, and its heterogeneous composition — spanning highly diluted homeopathic substances, whole-plant botanical extracts, and a live attenuated viral antigen — does not conform to the single-entity pharmacological model that TxGNN requires. Without a valid drug node in the knowledge graph, no disease–drug edge prediction can be produced.

No mechanism of action (MOA) data is available at the compound level. The most pharmacologically distinctive component is the Vaccinia Virus (NYCBOH strain), which is the same strain used in the historical smallpox vaccine (Dryvax/ACAM2000); its presence here alongside immunostimulatory botanicals suggests this may be a homeopathic immune preparation, though no approved indication has been established.

Standard drug repurposing methodology cannot proceed until a primary active ingredient is designated and characterized.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

This product has no approved NDAs or regulatory authorizations on record in any jurisdiction queried.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Vaccinia Virus (live antigen) carries specific contraindications in standard vaccine formulations (immunocompromised individuals, eczema, pregnancy). Should this product be advanced for evaluation, a dedicated safety review for the vaccinia virus component is strongly recommended before any clinical work.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate cannot be evaluated under the standard TxGNN repurposing pipeline because it lacks a DrugBank identifier, has no established indication, and contains a heterogeneous mixture of homeopathic, botanical, and live biological components that cannot be modeled as a single pharmacological entity.

**To proceed, the following is needed:**

- **Identify the lead active component**: Determine whether this is primarily a vaccinia-based immunological product, an herbal immunostimulant, or a homeopathic nosode — each requires a different evaluation framework
- **Assign a DrugBank ID**: Map the primary active ingredient to an existing DrugBank entry, or request a new entry if genuinely novel
- **Obtain MOA data**: Characterize the mechanism of the lead component before attempting repurposing analysis
- **Regulatory filing review**: Confirm whether any jurisdiction (US, EU, Japan, or others) has reviewed this product formulation, and retrieve the package insert if available
- **Disaggregate ingredients**: Consider running TxGNN separately for identifiable pharmacologically active components (e.g., Berberine from Goldenseal, or Vaccinia Virus as a separate entity in oncolytic/immunotherapy context)
- **Homeopathic classification check**: If the product is regulated as a homeopathic remedy (ultra-dilution), conventional pharmacological repurposing methodology may not be applicable, and the evaluation framework should be adjusted accordingly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Antimony Trisulfide Bordetella Pertussis Clostridi
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 0
---

# Antimony Trisulfide Bordetella Pertussis Clostridi
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

# Multi-Component Homeopathic Complex (14 Ingredients): TxGNN Prediction Unavailable

## One-Sentence Summary

This product consists of 14 heterogeneous components — including attenuated pathogens, homeopathic botanicals, inorganic compounds, and a biological material — with no approved indication on record in any jurisdiction.
The TxGNN model was **unable to generate drug repurposing predictions** for this entry due to the absence of a DrugBank ID and the non-standard multi-component nature of the formulation.
No clinical trial or literature evidence specific to this combination was identified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no registered indication found |
| Predicted New Indication | Not available — TxGNN prediction not generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (no prediction generated; model could not process entry) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this product. The root cause is the absence of a DrugBank ID, which is a required input to the TxGNN knowledge graph model. The product's INN field lists 14 disparate components across four distinct categories:

- **Pathogenic antigens**: Bordetella pertussis, Clostridium tetani, Measles virus, Mumps virus, Rubella virus, Poliovirus
- **Homeopathic botanicals**: Daphne mezereum bark, Ledum palustre twig, Thuja occidentalis leafy twig
- **Inorganic / mineral compounds**: Antimony trisulfide, Silicon dioxide, Oyster shell calcium carbonate (crude)
- **Other materials**: Thimerosal (preservative), Human breast tumor cell

This ingredient profile is consistent with a **homeopathic nosode or complex remedy** — a category that is not represented as individual drug entities in DrugBank and is not processable by the TxGNN disease-ontology mapping pipeline.

Without a coherent molecular target or pharmacological mechanism of action, it is not scientifically feasible to construct a repurposing hypothesis, nor to evaluate mechanistic plausibility for any new indication. The TxGNN failure in this case reflects a genuine data-structure incompatibility rather than a mere data gap.

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) was not identified through TFDA or DDI queries for this product.

> **Important note**: The composition of this product warrants particular caution before any clinical evaluation. Specific concerns include:
> - **Thimerosal** (ethylmercury-containing preservative): regulatory limits and special populations (pregnancy, paediatrics) must be assessed
> - **Attenuated/inactivated pathogens** (pertussis, tetanus, measles, mumps, rubella, polio): require biologics-grade safety documentation and cold-chain handling
> - **Human breast tumor cell** material: requires full characterisation of cell origin, sterility, and oncogenic potential per applicable regulatory guidance
> - This product is unregistered; no package insert is available for reference

Please obtain regulatory-grade documentation before any further safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This product cannot be meaningfully evaluated under the TxGNN drug repurposing framework. The multi-component, non-standard formulation has no DrugBank ID, no registered indication, and no TxGNN-generated prediction. All safety fields are data gaps, and the product is not marketed in any tracked jurisdiction.

**To proceed, the following is needed:**

- **Clarify product identity**: Confirm whether this is a homeopathic nosode, an experimental immunological preparation, or a combination biological product, and provide the brand name and regulatory classification
- **Obtain a DrugBank ID**: If a single principal active component exists, identify it and re-submit as an individual drug entry
- **Obtain regulatory documentation**: Secure the package insert, TFDA registration record, or equivalent label from the originating country to establish the approved or proposed indication
- **Conduct biologics-grade safety assessment**: Given the pathogen and human-cell-derived components, standard small-molecule safety review is insufficient; ICH Q5A/Q5D and relevant vaccine safety guidelines should be applied
- **Re-scope the repurposing question**: If the intent is to evaluate one specific component (e.g., Thimerosal or an individual viral antigen) for a new indication, isolate that ingredient and re-submit a single-entity Evidence Pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


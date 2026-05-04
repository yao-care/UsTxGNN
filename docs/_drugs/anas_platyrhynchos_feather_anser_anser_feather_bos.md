---
layout: default
title: Anas Platyrhynchos Feather Anser Anser Feather Bos
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 0
---

# Anas Platyrhynchos Feather Anser Anser Feather Bos
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

# Animal Allergen Multi-Panel Extract: No TxGNN Repurposing Prediction Generated

## One-Sentence Summary

This product is a 15-component allergen extract mixture — comprising 14 animal-derived allergens (duck feather, goose feather, cat hair, dog hair, horse dander, rabbit skin, and others) plus histamine dihydrochloride as a positive control — characteristic of allergy skin-testing panels used in clinical allergy diagnosis and immunotherapy.
No TxGNN repurposing predictions were generated for this product, as no DrugBank ID could be assigned and the product has no registered indications in either Taiwan or the US market.
Without a predicted indication or supporting evidence, a standard drug repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None registered |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model produced no output |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## What Is This Product?

This entry does not correspond to a single pharmaceutical agent. The INN field contains a semicolon-separated list of 15 biological allergen components:

| Component | Source Species | Material Type |
|-----------|---------------|---------------|
| ANAS PLATYRHYNCHOS FEATHER | Mallard duck | Feather |
| ANSER ANSER FEATHER | Goose | Feather |
| BOS TAURUS HAIR | Cattle | Hair |
| CANIS LUPUS FAMILIARIS HAIR | Dog | Hair |
| CAVIA PORCELLUS HAIR | Guinea pig | Hair |
| EQUUS CABALLUS DANDER | Horse | Dander |
| EQUUS CABALLUS HAIR | Horse | Hair |
| FELIS CATUS HAIR | Cat | Hair |
| GALLUS GALLUS FEATHER | Chicken | Feather |
| HISTAMINE DIHYDROCHLORIDE | — | Positive control |
| MESOCRICETUS AURATUS SKIN | Hamster | Skin |
| MUS MUSCULUS HAIR | Mouse | Hair |
| ORYCTOLAGUS CUNICULUS HAIR | Rabbit | Hair |
| ORYCTOLAGUS CUNICULUS SKIN | Rabbit | Skin |
| SUS SCROFA HAIR | Pig | Hair |

This configuration — multiple animal hair/feather/dander allergens combined with histamine dihydrochloride — is typical of an **allergy skin prick test (SPT) panel** or an **allergen-specific immunotherapy (AIT) preparation** used to diagnose and manage allergic sensitisation to animal-derived allergens.

The TxGNN model requires a single drug entity mapped to a DrugBank node. Because this product is a complex multi-allergen mixture with no DrugBank ID (`null`) and no single pharmacological mechanism of action, the prediction pipeline produced no output.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This product cannot be evaluated under the standard TxGNN drug repurposing framework because it is a multi-allergen diagnostic/therapeutic mixture with no DrugBank mapping, no approved indication on record, and no US market registration — the model produced zero predictions.

**To proceed, the following is needed:**

- **Clarify the intended drug entity**: Identify which single active component (e.g., a specific allergen extract or histamine dihydrochloride) should be the subject of a repurposing query, and obtain its DrugBank ID
- **Resolve data gap DG001**: Download the TFDA package insert PDF to extract safety warnings and contraindications
- **Resolve data gap DG002**: Query DrugBank API for mechanism-of-action data for the relevant active component
- **Re-run TxGNN**: After establishing a valid drug–DrugBank ID mapping, re-submit as a single-entity prediction request
- **Confirm product category**: Determine whether this is a diagnostic allergen panel (in vitro or skin test) or an immunotherapy product, as the regulatory and clinical pathway differs substantially between the two
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Aconitum Napellus Whole Arsenic Trioxide Baptisia 
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Arsenic Trioxide Baptisia 
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

# Multi-Component Homeopathic Influenza Complex: No Repurposing Prediction Available

## One-Sentence Summary

This is a 20-component preparation combining influenza viral antigens, botanical homeopathic extracts, and mineral compounds — with no approved indications on record and no DrugBank mapping achievable for the composite formulation.
The TxGNN model was unable to generate any repurposing prediction for this multi-ingredient complex, as the pipeline requires a single INN-mapped active ingredient with a DrugBank ID.
This evaluation cannot proceed until the product is classified, its primary active ingredient is identified, and critical safety data is obtained.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — no predictions, no supporting studies identified |
| Market Status (Taiwan) | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why This Evaluation Cannot Proceed

This product is an unusually complex multi-ingredient formulation that falls into at least three distinct ingredient categories simultaneously, making standard pharmaceutical repurposing analysis inapplicable without prior classification work.

**Category 1 — Influenza and measles viral antigens**: The formulation contains four influenza strain antigens (A/Thailand/8/2022 IVR-237, A/Victoria/4897/2022 IVR-238, B/Austria/1359417/2021 BVR-26, B/Phuket/3073/2013 BVR-1B) plus measles virus. This composition resembles a nosode or homeopathic immunological preparation, but the dilution level is not specified in the Evidence Pack. Whether these are live, attenuated, inactivated, or ultra-dilute antigens fundamentally changes the product's regulatory classification.

**Category 2 — Botanical homeopathic components**: Aconitum napellus (monkshood), Baptisia tinctoria, Chelidonium majus, Echinacea angustifolia, Garlic, Gelsemium sempervirens, Ginkgo, Hamamelis virginiana, Onion (Allium cepa), Strychnos nux-vomica, and Viscum album are well-known homeopathic remedy plants, several of which are acutely toxic at pharmacological (non-dilute) concentrations.

**Category 3 — Mineral and elemental components**: Arsenic trioxide, Mercury, Selenium, and Sodium chloride. Arsenic trioxide is a registered antineoplastic agent (used in AML treatment at pharmacological doses); mercury compounds carry neurotoxicity concerns. In a homeopathic context these are typically present at extreme dilution, but without dilution data this cannot be confirmed.

The TxGNN pipeline requires a single active pharmaceutical ingredient mapped to a DrugBank ID. This composite product has no DrugBank ID assigned, and no single component can represent the whole. The pipeline returned zero predictions as a direct consequence.

---

## Safety Considerations

Several components in this formulation carry significant inherent toxicity profiles that must be evaluated before any clinical application — even in a repurposing context:

- **Arsenic trioxide**: A scheduled cytotoxic agent; carcinogenic and acutely toxic at non-homeopathic doses. Regulatory jurisdictions require specialized handling.
- **Mercury**: Neurotoxic; subject to strict limits in pharmaceutical products under most national pharmacopoeias.
- **Aconitum napellus**: Contains aconitine alkaloids; cardiotoxic and neurotoxic with a narrow therapeutic index at pharmacological doses.
- **Strychnos nux-vomica**: Contains strychnine; a potent convulsant toxic at sub-milligram doses.
- **Gelsemium sempervirens**: Contains gelsemine; neurotoxic, with reported fatalities in non-dilute use.

If the preparation is a classical homeopathic product (e.g., 6C, 30C dilution), the concentrations of the above substances would be below pharmacologically active thresholds. However, the dilution factor is not stated anywhere in the Evidence Pack, and this constitutes a Blocking data gap equivalent to DG001.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This product cannot be evaluated for drug repurposing in its current form. The multi-ingredient, multi-category composition prevents standard TxGNN pipeline processing; no regulatory approval or original indication exists; and the safety profile of several components cannot be assessed without dilution data. Proceeding without resolving these gaps would produce unreliable outputs.

**To proceed, the following is needed:**

1. **Product classification**: Determine whether this is a homeopathic nosode, a combination botanical supplement, a vaccine-adjacent preparation, or a compounded product — each carries a distinct regulatory pathway and evidence standard.
2. **Dilution factor disclosure**: Specify the homeopathic potency (e.g., 6X, 30C) for all toxic components (arsenic trioxide, mercury, aconitum, strychnos, gelsemium) to enable safety assessment.
3. **Primary active ingredient identification**: Select the component(s) to be submitted to the TxGNN pipeline individually (e.g., Arsenic trioxide as DB01169, Echinacea, Ginkgo as separate queries).
4. **Original indication sourcing**: Obtain the product's approved or intended indication from the regulatory authority of origin (not Taiwan FDA, which has no record of this product).
5. **Resolve DG001**: Download and parse the originating market's package insert to extract contraindications and warnings.
6. **Resolve DG002**: Query DrugBank for each individual component to retrieve MOA data.
7. **Re-assess pipeline suitability**: Confirm whether repurposing analysis of a homeopathic multi-ingredient nosode is within scope for TxGNN — the model was trained on conventional single-ingredient pharmaceuticals and may not generate meaningful predictions for this product class regardless of data remediation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


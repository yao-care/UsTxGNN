---
layout: default
title: Antimony Trisulfide Barium Carbonate Bismuth Subni
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 0
---

# Antimony Trisulfide Barium Carbonate Bismuth Subni
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

# Multi-Component Compound (Homeopathic-Type Formulation): Insufficient Data for Drug Repurposing Evaluation

## One-Sentence Summary

This candidate is a complex 13-ingredient compound that appears to be a homeopathic-type preparation, combining botanical extracts (Echinacea, Thuja, Toxicodendron) with inorganic salts, several of which carry significant toxicity concerns (notably mercuric chloride and barium carbonate).
The TxGNN model returned **no predicted indications** for this compound, and the formulation is **not registered in any market**.
Due to the absence of predictions, clinical evidence, and a valid regulatory identity, a meaningful repurposing evaluation cannot be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no regulatory record found) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 (no predictions, no studies identified) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction is Available

The TxGNN model operates on individual, well-characterized drug entities mapped to DrugBank IDs and knowledge-graph nodes. This submission presents a **13-component mixture** with no DrugBank ID, no established brand identity, and no recognised single active ingredient. As a result, the pipeline could not generate a knowledge-graph embedding or produce repurposing candidates.

The ingredient list — which includes botanical homeopathic constituents (*Echinacea angustifolia*, *Thuja occidentalis*, *Toxicodendron pubescens*) alongside inorganic mineral salts — is characteristic of homeopathic poly-pharmacy preparations. Such formulations are typically tested at high dilutions and fall outside the pharmacological parameter space that TxGNN was trained on.

Furthermore, two components in this mixture present immediate toxicological flags that would require resolution before any further analysis:
- **Mercuric Chloride (HgCl₂)**: Acutely nephrotoxic and neurotoxic; heavily regulated or banned in most markets as a pharmaceutical ingredient.
- **Barium Carbonate (BaCO₃)**: Soluble barium salts are cardiac and skeletal muscle toxins; not approved for internal use in most jurisdictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this multi-component formulation as a unified entity.

---

## Literature Evidence

Currently no related literature available for this specific 13-ingredient combination as a unified repurposing candidate.

---

## US Market Information

No US (FDA) authorisations are on record for this compound or any formulation containing this specific ingredient combination.

---

## Safety Considerations

The following safety concerns arise directly from the chemical nature of identified components, even in the absence of a formal package insert:

- **Mercuric Chloride**: Classified as a highly toxic heavy metal compound. Associated with acute tubular necrosis, neurological damage, and gastrointestinal corrosion. Use in pharmaceutical products is prohibited or severely restricted by the FDA, EMA, and most national regulators.
- **Barium Carbonate**: Toxic if ingested; causes hypokalaemia, cardiac arrhythmias, and muscle paralysis. Not approved for systemic therapeutic use.
- **Antimony Trisulfide**: Antimony compounds are known respiratory and gastrointestinal toxins; IARC classifies antimony trioxide as possibly carcinogenic (Group 2B).
- **Toxicodendron pubescens (Poison Oak) Leaf**: Contact allergen; in non-homeopathic concentrations can cause severe contact dermatitis and systemic reactions.
- **Iodine and Phosphoric Acid**: Corrosive at non-trace concentrations; require defined dosage-form controls.

> ⚠️ **Critical Note**: The presence of mercuric chloride and barium carbonate in this formulation represents regulatory blockers in virtually all modern markets. Any development pathway must address the regulatory and toxicological status of these ingredients before proceeding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The compound cannot be evaluated for drug repurposing at this stage because the TxGNN model returned no predictions, no regulatory identity or DrugBank mapping exists, and at least two components (mercuric chloride, barium carbonate) carry acute toxicity profiles that would block regulatory submission in most jurisdictions.

**To proceed, the following is needed:**

1. **Clarify the drug identity**: Determine whether this is a homeopathic preparation (in which case it requires a separate regulatory pathway), a compounded formulation, or an investigational multi-component drug.
2. **Resolve toxic ingredient status**: Provide regulatory justification or dilution data for mercuric chloride and barium carbonate; confirm that concentrations fall within accepted safety limits for the intended route of administration.
3. **Obtain a DrugBank ID or equivalent**: Map the primary active ingredient(s) to a knowledge-graph node to enable TxGNN prediction.
4. **Define original indication**: Without a known therapeutic use, the repurposing framework cannot establish a mechanistic starting point.
5. **Provide MOA data**: Required to assess biological plausibility for any predicted indication.
6. **Conduct a full safety review**: Obtain or reconstruct a package insert equivalent; review all 13 components for drug–drug interactions and contraindications.

---

*This report is generated for research reference only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


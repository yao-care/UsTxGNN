---
layout: default
title: 1 2-Distearoyl-Sn-Glycero-3-Phosphocholine Berberi
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 0
---

# 1 2-Distearoyl-Sn-Glycero-3-Phosphocholine Berberi
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

# Multi-Ingredient Herbal Complex: TxGNN Evaluation — Insufficient Data for Repurposing Analysis

## One-Sentence Summary

This Evidence Pack describes a 19-component multi-ingredient mixture (including yohimbine, berberis vulgaris, saw palmetto, strychnos ignatii seed, and bufo bufo cutaneous gland, among others) with no registered original indication and no DrugBank mapping.
Because TxGNN operates on single-entity drugs with a valid DrugBank ID, **no repurposing predictions could be generated** for this complex mixture.
Without predictions, clinical trial evidence, or safety data on file, this candidate **cannot proceed** to standard repurposing evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None — TxGNN pipeline could not run |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — pipeline incomplete) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why This Candidate Could Not Be Evaluated

The product submitted contains **19 distinct active ingredients** spanning synthetic lipids, botanical extracts, animal gland derivatives, minerals, and alkaloids:

| Category | Ingredients |
|----------|-------------|
| Phospholipid | 1,2-Distearoyl-sn-glycero-3-phosphocholine (DSPC) |
| Botanical extracts | Berberis vulgaris root bark, Chaste tree fruit, Passiflora incarnata flowering top, Pulsatilla montana whole, Saw palmetto, Turnera diffusa leaf, Vanilla bean |
| Animal-derived | Bos taurus ovary, Bos taurus testicle, Bufo bufo cutaneous gland |
| Alkaloids | Yohimbine, Strychnos ignatii seed |
| Minerals / electrolytes | Ferric cation, Iodine, Selenium, Sodium chloride, Zinc valerate dihydrate |
| Excipient | Glycerin |

TxGNN is a **single-entity drug repurposing model** that maps one drug to a DrugBank ID and traverses a biomedical knowledge graph. This product presents two fundamental blocking issues:

1. **No DrugBank ID** — the mixture as a whole has no registered entity in DrugBank, and no individual ingredient was matched to a single canonical identifier.
2. **Multi-ingredient complexity** — repurposing predictions for an undefined fixed-dose combination cannot be meaningfully computed without decomposing each ingredient separately, which would require 19 independent pipelines and a subsequent interaction analysis.

The product also has **no US regulatory history** (0 NDAs, not marketed), which removes the ability to anchor the original indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Although formal safety data is absent from this Evidence Pack, several ingredients in this mixture carry well-documented safety signals that must be reviewed before any clinical development is considered:
>
> - **Yohimbine**: Adrenergic agonist with documented cardiovascular risks (hypertension, tachycardia); multiple known drug interactions including MAO inhibitors and antihypertensives.
> - **Strychnos ignatii seed**: Contains strychnine (a glycine receptor antagonist); narrow therapeutic index; convulsant at supra-therapeutic doses.
> - **Bufo bufo cutaneous gland**: Source of bufadienolides (digitalis-like cardiac glycosides); cardiotoxic in non-homeopathic concentrations.
>
> Whether these ingredients are present in pharmacologically active or homeopathic (sub-therapeutic) concentrations must be clarified before safety review can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is not evaluable by the TxGNN repurposing pipeline in its current form. The product is a complex multi-ingredient mixture with no DrugBank mapping, no original registered indication, no US market approval, and no predicted indications — making evidence-based repurposing analysis impossible at this stage.

**To proceed, the following is needed:**

- **Clarify product identity**: Determine whether this is a homeopathic preparation (with sub-Avogadro dilutions) or a conventional fixed-dose combination; this fundamentally changes the regulatory and scientific pathway.
- **Identify the lead active ingredient**: If repurposing analysis is desired, select a single pharmacologically active component (e.g., yohimbine, berberine from *Berberis vulgaris*, or saw palmetto extract) and re-submit as a standalone candidate with a DrugBank ID.
- **Obtain ingredient concentration data**: Confirm the dose of each component to assess pharmacological versus homeopathic activity levels.
- **Retrieve TFDA / FDA regulatory history**: Search national pharmacopoeias and homeopathic drug databases (e.g., HPUS, HAB) to determine if any component has a registered indication that could anchor a repurposing hypothesis.
- **Resolve safety gaps (DG001, DG002)**: Obtain package insert warnings, contraindications, and MOA data for each active ingredient, particularly yohimbine, strychnine-containing *Strychnos ignatii*, and bufo gland derivatives.
- **Re-run TxGNN per ingredient**: Once individual ingredients are mapped, execute separate prediction pipelines and aggregate results to identify which component (if any) yields a high-confidence repurposing signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


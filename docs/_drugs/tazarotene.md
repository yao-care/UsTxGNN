---
layout: default
title: Tazarotene
parent: Model Prediction Only (L5)
nav_order: 1202
evidence_level: L5
indication_count: 3
monitor_inn: "TAZAROTENE"
predicted_indications: ["seborrheic dermatitis", "seborrheic keratosis", "vulvar inverted follicular keratosis"]
last_modified_at: 2026-10-14
description: "Tazarotene: predicted new indication Seborrheic dermatitis (evidence level L5). Approved use: Psoriasis, parapsoriasis, acne"
---

# Tazarotene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tazarotene: From Psoriasis to Seborrheic Dermatitis
{: .text-alpha }

## One-Sentence Summary

Tazarotene is a topical retinoid, originally used to treat psoriasis, parapsoriasis, and acne.
The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**,
but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis, parapsoriasis, acne |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of NDAs | 11 (all cancelled; includes both NDAs and ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tazarotene is a topical retinoid (a RAR-beta/gamma agonist). Its efficacy in psoriasis and acne is established, and mechanistically it may be applicable to seborrheic dermatitis.

Retinoids normalize keratinocyte differentiation and reduce proliferation and inflammation. Psoriasis is a hyperproliferative, inflammatory skin disease. Seborrheic dermatitis also involves scaling and inflammation, so a shared mechanistic basis is plausible.

This link is a hypothesis only. No trials or literature were found to support it. Topical retinoids can cause irritation, and seborrheic dermatitis commonly affects the face, so tolerability is a potential concern.

Other predictions from the model include seborrheic keratosis (score 0.9951) and vulvar inverted follicular keratosis (score 0.9938). Seborrheic keratosis has two related publications, described below. Vulvar inverted follicular keratosis has no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for seborrheic dermatitis.

## Literature Evidence

Currently no related literature available for seborrheic dermatitis.

For reference, the second-ranked prediction, seborrheic keratosis, has two indirect publications. Only titles and partial abstracts were available, so it is not confirmed whether tazarotene showed efficacy in them:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36215682](https://pubmed.ncbi.nlm.nih.gov/36215682/) | 2023 | Systematic review | J Dermatolog Treat | Reviews efficacy and safety of topical treatments for seborrheic keratoses (26 reports included) |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Cohort | Int J Dermatol | Compares standard cryosurgery with topical calcipotriene, tazarotene, and imiquimod for seborrheic keratoses |

## US Market Information

The drug is marketed, with 11 valid licenses. Approved indication text was not available. Five main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021184 | TAZORAC | Cream | Not available (valid) |
| NDA020600 | Tazorac | Gel | Not available (valid) |
| NDA211882 | Arazlo | Lotion | Not available (valid) |
| NDA202428 | tazarotene | Aerosol, foam | Not available (valid) |
| ANDA217075 | TAZAROTENE | Cream | Not available (valid) |

## Cytotoxicity

Not applicable. Tazarotene is not an antineoplastic drug, so this section is omitted from the assessment.

## Safety Considerations

- **Disease-related contraindications (knowledge graph, not label text)**: photoparoxysmal response, photosensitivity disease, sunburn.
- **Drug Interactions**: 25 potential interactions were identified, none with a severity level assigned. Examples include doxycycline, minocycline, adapalene, tretinoin, clobetasol, tacrolimus, diclofenac, etodolac, citalopram, and duloxetine. The retinoids (adapalene, tretinoin) and the tetracyclines (doxycycline, minocycline) deserve particular attention for additive irritation or photosensitivity.
- **Other considerations**: Tazarotene is contraindicated in pregnancy, which matters for women of reproductive age. Package insert warnings and contraindications were not available, so please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9979), but the evidence level is L5: there are no clinical trials and no literature for seborrheic dermatitis. In addition, the drug is marketed with 11 valid licenses, but package insert safety data and mechanism data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA) from DrugBank
- Literature and trial searches specific to tazarotene in seborrheic dermatitis
- Review of the full text of the seborrheic keratosis publications to confirm whether tazarotene was evaluated
- Clarification of the cancelled US market status and the current availability of the product
- A tolerability assessment for topical retinoid use on facial seborrheic skin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


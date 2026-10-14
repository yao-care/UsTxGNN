---
layout: default
title: Benzoyl Peroxide
parent: Model Prediction Only (L5)
nav_order: 450
evidence_level: L5
indication_count: 4
---

# Benzoyl Peroxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Benzoyl Peroxide: From Acne to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Benzoyl peroxide is a topical agent originally used for skin conditions such as acne, atopic and contact dermatitis, and seborrheic dermatitis.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (disease). The US license records contain no approved indication text, so this comes from the knowledge-graph indication list (which also includes atopic dermatitis, contact dermatitis, seborrheic dermatitis, seborrheic keratosis, and granuloma annulare). |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, benzoyl peroxide is a topical oxidizing agent with keratolytic, comedolytic, and antibacterial activity. Its efficacy in acne is well established, and mechanistically it may be applicable to follicular skin lesions.

Inverted follicular keratosis is a benign follicular neoplasm related to seborrheic keratosis, which is among benzoyl peroxide's original indications. This shared link to follicular and keratinizing skin disease probably explains the graph-based association.

The link is speculative, however. No trials or publications support it. Applying a topical oxidizing agent to a vulvar lesion also carries a risk of mucosal irritation, so the high score should be treated as a hypothesis only.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M006 (cancelled) | Neutrogena On-the-Spot Acne Treatment | Cream | Not stated |
| M014 (cancelled) | Benzoyl Peroxide | Gel | Not stated |

## Other Predicted Indications (Lower Priority)

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | 2-Hydroxyethyl methacrylate sensitization | 99.43% | L5 | Likely a false positive or safety signal. Benzoyl peroxide is a known contact sensitizer and a radical initiator in methacrylate resins, so treating this allergy with it is implausible and could worsen it. |
| 3 | Acrodermatitis chronica atrophicans | 99.17% | L5 | Weak rationale. This is a late Lyme disease manifestation treated with systemic antibiotics, and topical benzoyl peroxide is not expected to reach Borrelia in deeper tissue. |
| 4 | Acne keloid (acne keloidalis) | 99.06% | L4 | The most plausible of the alternatives. It is a chronic scarring folliculitis adjacent to the approved acne use. Evidence is indirect only (see below). |

Acne keloid is classed as a research question rather than a Hold. One publication was retrieved (PMID [39090034](https://pubmed.ncbi.nlm.nih.gov/39090034/), 2024, *Dermatology Online Journal*). It is a retrospective chart review of 77 Black pediatric patients with acne vulgaris, covering presentation and treatment patterns, and it does not directly demonstrate efficacy in acne keloidalis. Tolerability in skin of color (irritation and post-inflammatory pigmentation) should be considered.

## Clinical Trial Evidence

Currently no related clinical trials registered for the lead prediction (vulvar inverted follicular keratosis).

## Literature Evidence

Currently no related literature available for the lead prediction (vulvar inverted follicular keratosis).

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The graph links benzoyl peroxide to contraindications or cautions in these conditions:
  - Skin and sun-related: photosensitivity disease, photoparoxysmal response, exfoliative dermatitis, dermatitis, skin atrophy
  - Viral skin and genital: anogenital human papillomavirus infection, common wart
  - Vascular: telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia, peripheral vascular disease, intermittent claudication, peripheral arterial disease
  - Gastrointestinal: Crohn disease, Crohn's colitis, inflammatory bowel disease, ulcerative colitis, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, adrenocortical insufficiency, Addison disease
  - Renal and urinary: kidney disease, pyoureter

  These come from graph edges and need confirmation against the official labelling before they are treated as true contraindications.
- **Contact sensitization:** Benzoyl peroxide is a known contact sensitizer, which is relevant to any new topical use, especially on mucosal or genital skin.

For the package insert warnings, contraindications, and drug interactions, please refer to the package insert. No interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for vulvar inverted follicular keratosis is very high (99.92%), but there are no clinical trials or publications, so the evidence level is L5. The mechanistic link is speculative, and mucosal irritation is a concern on vulvar skin. No currently valid US license exists for any benzoyl peroxide product in the data compiled for this report.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Detailed mechanism of action data
- A literature and clinical-case search specific to inverted follicular keratosis, including any topical keratolytic treatment reports
- A route and site compatibility assessment for vulvar and mucosal application
- Consideration of acne keloidalis as a better-supported alternative to take forward as a research question, with a direct efficacy search
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Halcinonide
parent: Model Prediction Only (L5)
nav_order: 766
evidence_level: L5
indication_count: 10
monitor_inn: "HALCINONIDE"
predicted_indications: ["annular atrophic lichen planus", "lichen planus pigmentosus", "hypertrophic lichen planus", "vulvar inverted follicular keratosis", "lichen planus pemphigoides", "alopecia areata", "telogen effluvium", "alopecia mucinosa", "hereditary hypotrichosis with recurrent skin vesicles", "Quinquaud's folliculitis decalvans"]
last_modified_at: 2026-10-28
description: "Halcinonide: predicted new indication Annular atrophic lichen planus (evidence level L5). Approved use: Not recorded in the local data"
---

# Halcinonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Halcinonide: Annular atrophic lichen planus
{: .text-alpha }

## One-Sentence Summary

Halcinonide is a high-potency topical corticosteroid, originally used for inflammatory and eczematous skin conditions such as atopic dermatitis, contact dermatitis, seborrheic dermatitis, neurodermatitis, lichen disease and discoid lupus erythematosus.
The TxGNN model predicts it may be effective for **annular atrophic lichen planus**, but there are currently **0 clinical trials** and **0 publications** for this specific indication, so the support is a model prediction only.
Across the 10 predicted indications, the only published item is a 1977 title-only report on **alopecia areata**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Annular atrophic lichen planus |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 4 of 4) |
| Number of NDAs | 4 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, halcinonide is a high-potency topical corticosteroid. Its efficacy in inflammatory dermatoses is established, and mechanistically it may be applicable to lichen planus.

Lichen planus and its variants are T-cell mediated inflammatory skin diseases, and topical corticosteroids are standard first-line therapy. This is why the prediction is biologically plausible, and it sits close to halcinonide's existing indications such as lichen disease and neurodermatitis.

There is an important caution for this particular variant. Annular atrophic lichen planus involves atrophic (thinned) skin, and a potent steroid carries a theoretical risk of further skin thinning. The knowledge graph also lists skin atrophy as a contraindication for halcinonide. No trials or literature specific to this variant were found.

### Other Predicted Indications

The model produced 10 predictions in total. They differ widely in plausibility:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 1 | Annular atrophic lichen planus | 0.9993 | L5 | Plausible mechanism, but atrophy concern |
| 2 | Lichen planus pigmentosus | 0.9993 | L5 | Plausible anti-inflammatory rationale, no data |
| 3 | Hypertrophic lichen planus | 0.9993 | L5 | Most clinically plausible; high-potency steroids (including under occlusion) are commonly used |
| 4 | Vulvar inverted follicular keratosis | 0.9993 | L5 | Weak rationale; may reflect similarity to seborrheic keratosis |
| 5 | Lichen planus pemphigoides | 0.9992 | L5 | Anti-inflammatory rationale, but severe disease usually needs systemic therapy |
| 6 | Alopecia areata | 0.9991 | L4 | Plausible; one 1977 title-only publication |
| 7 | Telogen effluvium | 0.9989 | L5 | Weak rationale (non-inflammatory, self-limiting) |
| 8 | Alopecia mucinosa | 0.9989 | L5 | Modest rationale; possible lymphoma association needs careful diagnosis |
| 9 | Hereditary hypotrichosis with recurrent skin vesicles | 0.9989 | L5 | No clear mechanism; likely a network artifact |
| 10 | Quinquaud's folliculitis decalvans | 0.9988 | L5 | Antibiotics are the mainstay; steroid only adjunctive |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked indication (annular atrophic lichen planus), currently no related literature is available.

The only publication found across the predicted indications relates to rank 6, alopecia areata:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [915049](https://pubmed.ncbi.nlm.nih.gov/915049/) | 1977 | Unclassified (likely clinical study or case series) | Journal of Cutaneous Pathology | "Topical halcinonide in alopecia areata and in alopecia totalis." Only the title was available, so design, size and outcomes cannot be verified |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017556 | Halcinonide (Sun Pharmaceutical Industries) | Cream | Not available; status valid |
| ANDA217671 | Halcinonide Topical Solution (INA Pharmaceutics) | Solution | Not available; status valid |
| NDA017823 | HALOG (E.R. Squibb & Sons) | Solution | Not available; status valid |
| ANDA211027 | Halcinonide (Mylan Pharmaceuticals) | Cream | Not available; status valid |

All four US licenses are valid, and halcinonide is currently marketed in the US.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, glaucoma, skin atrophy, peripheral vascular disease (including intermittent claudication and peripheral arterial disease), and cutaneous tuberculosis. These should be verified against the official label.
- **Relevance to the lead indication:** skin atrophy is directly relevant to annular atrophic lichen planus and warrants particular caution.

Please refer to the package insert for further safety information, as no label warnings or drug interaction data were available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9993), and a topical corticosteroid for lichen planus is mechanistically reasonable. However, there are no trials or literature for annular atrophic lichen planus, and skin atrophy is a listed contraindication. The drug is marketed in the US, with all four licenses valid. Of the candidates, hypertrophic lichen planus is the most clinically plausible, and alopecia areata is the only one with any published report (1977, title only).

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Drug-specific clinical evidence, prioritising hypertrophic lichen planus, and a review of the full text of the 1977 alopecia areata publication
- An assessment of the skin atrophy risk if the atrophic variant is pursued
- Confirmation of the current regulatory and commercial availability of halcinonide products, given the cancelled licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


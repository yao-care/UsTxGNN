---
layout: default
title: Amcinonide
parent: Model Prediction Only (L5)
nav_order: 323
evidence_level: L5
indication_count: 8
---

# Amcinonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Amcinonide: From Corticosteroid-Responsive Dermatoses to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Amcinonide is a mid-to-high potency topical corticosteroid, marketed in the US as creams and ointments.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but **no clinical trials and no publications** support this specific prediction, and the mechanistic rationale is weak.
The best-supported candidate in this pack is ordinary **dermatitis** (4 double-blind RCTs, 1976–1984), which is close to the drug's existing use rather than a true repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the retrieved records (all license indication texts are empty). Class use is corticosteroid-responsive dermatoses (inferred, not from the pack). |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (all listed as ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Amcinonide is a topical corticosteroid, and the general class mechanism is glucocorticoid receptor agonism, which suppresses inflammatory cytokines. This makes it a natural fit for inflammatory and eczematous skin disease.

Vulvar inverted follicular keratosis, however, is a benign keratotic follicular lesion and is not primarily inflammatory. The anti-inflammatory mechanism therefore gives little reason to expect benefit. Vulvar skin is also especially prone to steroid-related atrophy, so a potent corticosteroid carries more downside than upside here. The high TxGNN score most likely reflects network proximity to other skin diseases rather than a genuine therapeutic link. Treat this prediction as low-plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications in This Pack

| Rank | Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Hypertrophic lichen planus | 99.73% | L5 | T-cell-mediated inflammatory dermatosis. Potent topical corticosteroids are standard class practice, so a class effect is plausible. No amcinonide-specific evidence was retrieved. |
| 3 | Lichen planus pigmentosus | 99.73% | L5 | Inflammation control is plausible, but pigment outcomes are less predictable. |
| 4 | Annular atrophic lichen planus | 99.73% | L5 | Inflammatory, but the atrophic variant makes the atrophogenic potential of a potent steroid a specific concern. |
| 5 | Lichen planus pemphigoides | 99.64% | L5 | Rare overlap disease. A class-level rationale exists, but there is no evidence. Hold. |
| 6 | Primary cutaneous B-cell lymphoma | 99.42% | L5 | Topical steroids are palliative mainly in T-cell lymphoma. The link is weak, and standard care is excision, radiotherapy, or rituximab. Hold. |
| 7 | **Dermatitis** | 99.30% | **L1** | Best-supported candidate (see below). |
| 8 | 2-Hydroxyethyl methacrylate sensitization | 99.00% | L5 | Corticosteroids treat only the resulting dermatitis, not the sensitization. Amcinonide is itself a documented contact allergen. Hold. |

### Dermatitis: Supporting Literature (Rank 7)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6383735](https://pubmed.ncbi.nlm.nih.gov/6383735/) | 1984 | RCT | Cutis | 33 patients with eczematous dermatitis, amcinonide 0.1% vs halcinonide 0.1% for 2 weeks. Both improved significantly, with no significant difference between groups. |
| [7030645](https://pubmed.ncbi.nlm.nih.gov/7030645/) | 1981 | RCT | Cutis | 29 patients, amcinonide vs halcinonide cream. Both produced statistically significant and equivalent improvement by week 2. |
| [391500](https://pubmed.ncbi.nlm.nih.gov/391500/) | 1979 | RCT | Cutis | Amcinonide 0.1% vs betamethasone valerate 0.1%. Both improved significantly, and amcinonide showed significantly greater overall improvement. |
| [820519](https://pubmed.ncbi.nlm.nih.gov/820519/) | 1976 | RCT | Curr Ther Res | Double-blind comparison of amcinonide and betamethasone valerate in eczematoid conditions (no abstract available). |
| [32555122](https://pubmed.ncbi.nlm.nih.gov/32555122/) | 2020 | Review | Med Lett Drugs Ther | Overview of drugs for atopic dermatitis (no abstract available). |
| [3160532](https://pubmed.ncbi.nlm.nih.gov/3160532/) | 1985 | Case report | Contact Dermatitis | Allergic contact dermatitis from amcinonide. Should be considered in resistant or worsening eczema despite topical steroid therapy. |
| [6233341](https://pubmed.ncbi.nlm.nih.gov/6233341/) | 1984 | Case series | J Am Acad Dermatol | Five cases of contact sensitivity to topical corticosteroids. One patient was allergic only to amcinonide. |
| [8449700](https://pubmed.ncbi.nlm.nih.gov/8449700/) | 1993 | Other | Hautarzt | Three women with positive patch tests to amcinonide. Repeated open application produced massive erythematous reactions and urticaria. |

These RCTs are old, short (2 weeks), and small (about 30 patients). They support use in eczematous dermatitis, which is probably already covered by the labeled use, so this is not a repurposing signal. They also show that amcinonide is a recurrent contact allergen.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA076229 | Amcinonide (INA Pharmaceutics) | Cream | Not listed in record |
| ANDA076065 | Amcinonide (Fougera; also Solubiomix) | Cream | Not listed in record |
| ANDA076367 | Amcinonide (Sun Pharmaceutical) | Ointment | Not listed in record |
| ANDA076096 | Amcinonide (Ayurax) | Ointment | Not listed in record |

ANDA076065 appears twice, under two manufacturers. All products are topical creams or ointments.

## Safety Considerations

- **Vulvar skin:** Vulvar skin is especially prone to steroid-related atrophy, so a potent corticosteroid is a specific concern for the top predicted indication.
- **Atrophic lesions:** The atrophogenic potential of a potent steroid is a concern for annular atrophic lichen planus.
- **Contact allergy:** Amcinonide is a documented contact allergen, with multiple case reports and cross-reactivity within the corticosteroid class.

Please refer to the package insert for full warnings, contraindications, and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (vulvar inverted follicular keratosis) has no trials or literature, a weak mechanistic link, and a specific safety concern in vulvar skin. Only dermatitis has real evidence (L1), and it overlaps with existing corticosteroid use. The lichen planus variants (ranks 2–4) are reasonable class-effect research questions rather than actionable candidates.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap for safety screening)
- Original indications and mechanism of action data for amcinonide
- Amcinonide-specific evidence, or a decision to evaluate hypertrophic lichen planus as a class-effect research question instead
- Confirmation of whether dermatitis falls within the labeled indication, which would make it a non-repurposing use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


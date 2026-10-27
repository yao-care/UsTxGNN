---
layout: default
title: Fidaxomicin
parent: Model Prediction Only (L5)
nav_order: 706
evidence_level: L5
indication_count: 9
monitor_inn: "FIDAXOMICIN"
predicted_indications: ["staphylococcal scalded skin syndrome", "bullous impetigo", "inhalational botulism", "impetigo", "toxin-mediated infectious botulism", "vulvovaginal candidiasis", "hordeolum", "staphylococcus aureus pneumonia", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-14
description: "Fidaxomicin: predicted new indication Staphylococcal scalded skin syndrome (evidence level L5). Approved use: Clostridium difficile colitis"
---

# Fidaxomicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Fidaxomicin: From Clostridium difficile Colitis to Staphylococcal Scalded Skin Syndrome
{: .text-alpha }

## One-Sentence Summary

Fidaxomicin is a narrow-spectrum macrolide antibiotic, originally used to treat *Clostridium difficile* colitis and related Clostridium infections.
The TxGNN model predicts it may be effective for **staphylococcal scalded skin syndrome**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Clostridium difficile colitis (also perinatal necrotizing enterocolitis and Clostridium infectious disease, per the knowledge graph) |
| Predicted New Indication | Staphylococcal scalded skin syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 5 authorizations are listed as cancelled) |
| Number of NDAs | 5 (2 NDAs and 3 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Fidaxomicin is generally known as a narrow-spectrum macrolide that inhibits bacterial RNA polymerase. It is active mainly against Gram-positive bacteria, and in vitro it shows some activity against certain *Staphylococcus aureus* strains. That in vitro activity is the main reason the model links it to staphylococcal diseases.

The link to the new indication is weak, for the following reasons:

- Staphylococcal scalded skin syndrome is driven by exfoliative toxins and is normally treated with systemic anti-staphylococcal antibiotics.
- Fidaxomicin has minimal systemic absorption. It stays in the gut, which suits colitis but not a skin and bloodstream condition.

The other predictions follow a similar pattern, with scores of 99.0% to 99.7%. They include bullous impetigo, impetigo, inhalational botulism, toxin-mediated infectious botulism, vulvovaginal candidiasis, hordeolum, *S. aureus* pneumonia and punctate epithelial keratoconjunctivitis. Each has the same problems: poor systemic exposure, no suitable formulation, or established standard therapy. Vulvovaginal candidiasis is likely a model artifact, because fidaxomicin has no known antifungal activity. For botulism, antibiotics do not neutralize preformed toxin. None of these predictions has trial support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is linked to the top-ranked prediction. The only publication linked to any predicted indication (*S. aureus* pneumonia, rank 8) is a general review and does not show fidaxomicin efficacy for that condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31634096](https://pubmed.ncbi.nlm.nih.gov/31634096/) | 2019 | Review | Journal of Hospital Medicine | Hospital medicine literature update. It notes vancomycin or fidaxomicin as first-line treatment for *C. difficile* infection, with no evidence for staphylococcal disease. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA201699 | Dificid (Merck Sharp & Dohme LLC) | Film-coated tablet | Not available; status cancelled |
| NDA213138 | Dificid (Merck Sharp & Dohme LLC) | Granule for suspension | Not available; status cancelled |
| ANDA208443 | Fidaxomicin (Teva Pharmaceuticals, Inc.) | Film-coated tablet | Not available; status cancelled |
| ANDA219559 | Fidaxomicin (Apotex Corp.) | Film-coated tablet | Not available; status cancelled |
| ANDA220374 | Fidaxomicin (Torrent Pharmaceuticals Limited) | Film-coated tablet | Not available; status cancelled |

## Safety Considerations

- **Drug Interactions**: 79 interactions were recorded; the first 20 are summarized here.
  - **Major**: Vibrio cholerae CVD 103-HgR live vaccine. The live vaccine may be less effective when given with an antibiotic.
  - **Moderate**: alpelisib, apalutamide, binimetinib, picosulfuric acid.
  - **Minor**: nifedipine, amiodarone, brigatinib, cabozantinib, capmatinib, diltiazem, spironolactone, clarithromycin, verapamil, cyclosporine, daclatasvir, dronedarone, erythromycin, elagolix, ivacaftor.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score, but no trials or supporting publications back it. Fidaxomicin's minimal systemic absorption conflicts with the nature of staphylococcal scalded skin syndrome, a toxin-mediated systemic disease with effective standard treatments. All US authorizations are also listed as cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (the missing safety data blocks safety screening)
- Detailed mechanism-of-action data
- Preclinical evidence that fidaxomicin can reach effective concentrations at the site of infection, such as skin or blood
- A feasibility assessment of a topical or systemic formulation, since only oral forms exist
- Clarification of the cancelled US market status
- A review of whether other candidates, such as toxin-independent *S. aureus* infections or intestinal botulism colonization, have a better mechanistic fit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


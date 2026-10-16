---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 535
evidence_level: L5
indication_count: 6
monitor_inn: "CLINDAMYCIN"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis"]
---

# Clindamycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Clindamycin: From Bacterial Infections and Acne to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is an antibacterial originally used for acne, staphylococcal and streptococcal infections, anaerobic infections, bacterial vaginosis and aspiration pneumonia.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, streptococcal and staphylococcal infections, anaerobic bacterial infections, bacterial vaginosis, aspiration pneumonia (from the knowledge graph; no label text available) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 14 authorizations in total (2 NDAs, 12 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, clindamycin is a protein-synthesis-inhibiting antibacterial with activity against Gram-positive cocci (including *Staphylococcus aureus*) and anaerobes.

Punctate epithelial keratoconjunctivitis is usually inflammatory, viral (for example adenoviral), toxic or related to dry eye, so an antibacterial has no clear mechanistic rationale. A plausible link exists only when a bacterial component is present, such as staphylococcal blepharokeratoconjunctivitis. Clindamycin is also not a standard ophthalmic agent. The high score is therefore best read as a network-similarity signal rather than evidence of efficacy.

Other predictions in the list were reviewed and are also weak:

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Exposure keratitis | 99.80% | L4 | Literature covers infectious keratitis in general (*S. aureus*, contact lens-related), not exposure keratitis or clindamycin specifically. Indirect link only. |
| Non-human animal disease | 99.69% | L5 | Non-specific category. The literature is on *C. difficile* epidemiology in animals, and clindamycin is a risk factor for *C. difficile* infection, so it points the wrong way. Not actionable. |
| Neurotrophic keratopathy | 99.49% | L5 | Caused by impaired corneal innervation. Antibacterial activity might help only with secondary infection. |
| Epidemic keratoconjunctivitis | 99.49% | L5 | Adenoviral, so an antibacterial has no activity. The literature concerns bovine disease. |
| Postmenopausal atrophic vaginitis | 99.03% | L5 | Estrogen-deficiency disease. The prediction likely overlaps with the existing vaginitis and bacterial vaginosis use. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

For reference, the closest related predicted indication (exposure keratitis) has the following literature, all of low evidentiary tier and none specific to clindamycin:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24244625](https://pubmed.ncbi.nlm.nih.gov/24244625/) | 2013 | Retrospective hospital case review | PLoS One | Characterizes *S. aureus* keratitis, comparing MRSA and MSSA in demographics, clinical features, antibiotic susceptibility and outcomes |
| [22880135](https://pubmed.ncbi.nlm.nih.gov/22880135/) | 2012 | Retrospective cohort | PLoS One | Prevalence, clinical features and antibiotic susceptibility of MRSA versus MSSA ocular infections |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-related *Bacillus cereus* keratitis with genetic match between corneal and lens-case isolates |

## US Market Information

All 14 authorizations are cancelled, and no approved indication text is available. Main entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050441 | Cleocin Phosphate | Injection, solution | Not available |
| NDA050793 | Clindesse | Cream | Not available |
| ANDA065061 | Clindamycin hydrochloride | Capsule | Not available |
| ANDA065139 | Clindamycin phosphate | Cream | Not available |
| ANDA090902 | Clindamycin palmitate hydrochloride | Granule, for solution | Not available |

Dosage forms across all authorizations include oral capsules, injectable solutions, topical cream, oral granules and solutions. No ophthalmic formulation appears.

## Cytotoxicity

Not applicable: clindamycin is not an antineoplastic drug.

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Those rated Moderate are balsalazide, clarithromycin, picosulfuric acid, attapulgite and kaolin. Many others, such as amphotericin B, aspirin, amoxicillin, bupropion, morphine, metformin, vancomycin and proton pump inhibitors, have an unrated (Unknown) severity.
- **Disease associations of concern (knowledge graph, not label text)**: liver failure, inflammatory bowel disease (Crohn disease, ulcerative colitis), *Clostridium difficile* colitis, diarrheal disease, necrotizing enterocolitis, atopic and exfoliative dermatitis, sunburn and vulvovaginal candidiasis.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information. Clindamycin is widely known to carry a risk of *C. difficile*-associated diarrhea.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or literature, and no clear mechanistic rationale for a non-infectious, mostly viral or inflammatory condition. In addition, no valid US license currently exists, and no ophthalmic formulation is available.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Evidence of a bacterial component in punctate epithelial keratoconjunctivitis (for example, staphylococcal blepharokeratoconjunctivitis) and clindamycin-specific efficacy data
- An assessment of ophthalmic formulation and route feasibility
- Review of the alternative predictions: exposure keratitis is the only one with any indirect literature, but it still lacks clindamycin-specific data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


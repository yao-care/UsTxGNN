---
layout: default
title: Ivermectin
parent: Model Prediction Only (L5)
nav_order: 821
evidence_level: L5
indication_count: 9
monitor_inn: "IVERMECTIN"
predicted_indications: ["vulvovaginal candidiasis", "esophageal candidiasis", "anogenital human papillomavirus infection", "vulvovaginitis", "neonatal candidiasis", "candida glabrata", "congenital candidiasis", "postmenopausal atrophic vaginitis", "candidiasis, invasive"]
---

# Ivermectin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Ivermectin: From Strongyloidiasis and Onchocerciasis to Vulvovaginal Candidiasis

## One-Sentence Summary

Ivermectin is an antiparasitic drug originally used to treat strongyloidiasis and onchocerciasis.
The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis**,
but currently there are **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Strongyloidiasis, onchocerciasis |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 authorizations in total (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, ivermectin acts on glutamate-gated chloride channels in invertebrates, which paralyses and kills parasites. This is the basis of its use against strongyloidiasis and onchocerciasis.

This mechanism does not readily extend to the predicted indication. Fungi such as *Candida* lack these targets, so there is no established antifungal mechanism. The very high TxGNN score (99.95%) is a graph-based prediction only. It likely reflects network proximity to other infection-related indications rather than real pharmacological activity.

Other predictions for this drug are also dominated by candidiasis and vaginal conditions (esophageal, neonatal, congenital and invasive candidiasis, *Candida glabrata*, vulvovaginitis). They share the same weakness: no clinical trials, and no literature that actually supports an antifungal effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for vulvovaginal candidiasis.

For the second-ranked prediction (esophageal candidiasis) and the seventh-ranked prediction (congenital candidiasis), the linked papers do not show antifungal activity:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) | 2022 | Case report | BMJ Case Reports | Disseminated strongyloidiasis after prolonged corticosteroid treatment. This is an existing ivermectin indication, not candidiasis. |
| [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) | 1999 | Case report | Australasian Journal of Dermatology | Oral ivermectin cleared crusted scabies in two immunocompromised children, one of whom had chronic mucocutaneous candidiasis. The benefit was for scabies, not candidiasis. |

## US Market Information

All 10 authorizations are listed as cancelled. The data compiled for this report contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA050742 | Stromectol | Tablet | Merck Sharp & Dohme LLC |
| NDA206255 | Ivermectin | Cream | Mayne Pharma Inc. |
| ANDA204154 | Ivermectin | Tablet | Edenbridge Pharmaceuticals LLC |
| ANDA215922 | Ivermectin | Tablet | Advagen Pharma Ltd |
| ANDA215210 | Ivermectin | Cream | Zydus Lifesciences Limited |

## Safety Considerations

- **Knowledge-graph contraindication signals**: loiasis and filariasis are linked to ivermectin as contraindicated conditions. These come from a knowledge graph, not from label text.
- **Drug Interactions**: 100 interactions were identified. Those rated Moderate include:
  - Aprepitant
  - Clarithromycin
  - Ethanol
  - Cobicistat
  - Deferasirox
  - Warfarin
  - Dicoumarol
  - Fostamatinib
  - Radioactive iodide (I-123, I-131)
  - Abametapir (topical)

  Several others, such as omeprazole, lansoprazole, prednisone, dexamethasone and heparin, have an unclassified severity.
- **Population concern**: ivermectin is not routinely used in young infants or children under 15 kg, which matters for the neonatal and congenital candidiasis predictions.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no clinical trials or supporting literature, and no plausible antifungal mechanism. Effective antifungals (azoles, echinocandins, amphotericin B) are already standard of care. All US authorizations are cancelled.

**To proceed, the following is needed:**
- Mechanism of action data, and in vitro evidence of activity against *Candida* species
- Preclinical or early clinical studies in vulvovaginal candidiasis
- Package insert warnings and contraindications, which are required for safety screening
- Confirmation of the current US regulatory status, and of which route (oral or topical) a new indication would need
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


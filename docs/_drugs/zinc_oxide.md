---
layout: default
title: Zinc Oxide
parent: Moderate Evidence (L3-L4)
nav_order: 1308
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Zinc Oxide: predicted new indication Acne (disease) (evidence level L4). Approved use: Not stated in the US license records"
monitor_inn: "ZINC OXIDE"
predicted_indications: ["anorectal stricture", "anal polyp", "papillary conjunctivitis", "postinfectious vasculitis"]
---

# Zinc Oxide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Zinc Oxide: From Skin Conditions (Tinea, Dermatitis, Burns) to Acne

## One-Sentence Summary

Zinc oxide is a topical skin protectant and astringent, originally used for skin conditions such as tinea infections, dermatitis, burns and hemorrhoids.
The TxGNN model predicts it may be effective for **Acne (disease)**, but there are **no registered clinical trials** and only **3 publications** (one general review, one preclinical study, one small clinical study), so the evidence is weak and this remains a research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records; the knowledge graph lists tinea pedis, tinea corporis, dermatitis, cutaneous candidiasis, pityriasis versicolor, hemorrhoid, proctitis, burn and injury |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold (research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for zinc oxide. The reasoning below rests on general pharmacology, not on a defined drug mechanism.

Zinc ions have mild antibacterial activity, including against *Cutibacterium acnes*, along with anti-inflammatory effects, and they may reduce sebum-related inflammation. Zinc oxide is already used topically in dermatology as a skin protectant, so acne sits in the same therapeutic area as its existing indications (dermatitis, cutaneous infections).

The high TxGNN score (99.86%) is a computational prediction only. The supporting literature is limited: one nanoparticle review mentions nano-preparations under investigation for acne, one preclinical microneedle study involves zinc-related nanomaterials, and one small clinical study of mild catamenial acne does not clearly establish a role for zinc oxide.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21342155](https://pubmed.ncbi.nlm.nih.gov/21342155/) | 2011 | Review | International Journal of Dermatology | Overview of engineered nanoparticles such as zinc oxide and titanium dioxide in skin care. Nano-preparations are under investigation for acne vulgaris, condyloma acuminata, atopic dermatitis and other conditions. |
| [36888703](https://pubmed.ncbi.nlm.nih.gov/36888703/) | 2023 | Preclinical/Experimental | Science Advances | Ultrasound-responsive microneedle patch delivering nanoparticles for *P. acnes* infection, as an antibiotic-free acne approach. Zinc oxide's role is unclear (the nanoparticles are zinc porphyrin-based). |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical study (split-face, small, likely non-RCT) | Skin Research and Technology | Assessment of mild inflammatory catamenial acne in young women. The design and the role of zinc oxide cannot be confirmed from the available information. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M016 (cancelled) | zinc oxide 20% (Bionpharma Inc) | Ointment | Not stated |
| M020 (cancelled) | Mineral Sunscreen For Face and Body (Skin Philosophy by Kelly) | Cream | Not stated |

Both licenses are cancelled, so no valid US authorization currently exists in the data compiled for this report.

---

## Safety Considerations

The knowledge graph links zinc oxide to contraindication edges for several conditions. This comes from graph relationships, not from label text, and should be treated as a signal for review, not as confirmed contraindications:
- **Cardiovascular:** hypertensive disorder, hypertension, coronary artery disease, sudden cardiac arrest, heart conduction disease
- **Metal and iron metabolism:** hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease
- **Haematological:** sickle cell anemia, hereditary persistence of fetal hemoglobin
- **Endocrine:** hyperthyroidism, Graves disease, thyrotoxicosis
- **Other:** benign prostatic hyperplasia, primary hyperoxaluria, anxiety

No drug-interaction records were found. For package-insert warnings and contraindications, please refer to the product labeling.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score and general zinc pharmacology. There are no registered trials, the literature is indirect (a review, a preclinical study and a small study of unclear design), and no US license is currently valid. This makes it a research question, not a candidate ready for development.

**To proceed, the following is needed:**
- Mechanism of action data for zinc oxide, to support the link to acne
- Package-insert warnings and contraindications, to allow safety screening
- Controlled clinical evidence (for example, a randomized trial of topical zinc oxide in acne)
- A route and formulation compatibility assessment for acne use
- Review of the knowledge-graph contraindication signals against topical use

---

### Other Predictions (For Reference)

The other four predictions have no clinical trials or literature and are all rated L5 (model prediction only) with a Hold recommendation:

| Predicted Indication | TxGNN Score | Note |
|------|------|------|
| Anorectal stricture | 99.46% | Only a weak contextual link to existing anorectal uses; a topical protectant is unlikely to address fibrotic narrowing |
| Anal polyp | 99.31% | Only anatomical proximity; no known effect on polyp growth |
| Papillary conjunctivitis | 99.14% | Speculative; zinc oxide is not formulated for ocular use, so tolerability is a concern |
| Postinfectious vasculitis | 99.02% | No plausible pathway from a topical agent to a systemic immune-mediated disease |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


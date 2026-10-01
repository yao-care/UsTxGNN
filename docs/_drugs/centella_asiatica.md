---
layout: default
title: Centella Asiatica
parent: Moderate Evidence (L3-L4)
nav_order: 512
evidence_level: L4
indication_count: 3
---

# Centella Asiatica
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Centella asiatica: From Topical Skin-Care Products to Insomnia

## One-Sentence Summary

Centella asiatica (Gotu Kola) is a botanical ingredient that appears in the marketed products in this dataset as topical scar gels, creams and similar skin-care items. The TxGNN model predicts it may be useful for **insomnia**, but the supporting evidence is thin: **2 clinical trials** (neither testing Centella asiatica alone for sleep) and **1 preclinical publication** (a zebrafish model).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text on record; marketed products are topical skin and scar-care products |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 registered licenses |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Centella asiatica is a plant extract whose main constituents are triterpenoids (asiaticoside, madecassoside, asiatic acid, madecassic acid). It is used traditionally and in skin-care products, and it has no formally recorded original indication in this dataset.

The biology offers a plausible link to sleep. Triterpenoids from Centella asiatica modulate GABA-A receptors in vitro, and rodent studies report anxiolytic and neuroprotective effects. An ethanol extract also reduced insomnia-like behaviour in a zebrafish larvae model, apparently through inhibition of orexin, ERK, Akt and p38 signalling. The link between skin-care use and sleep is indirect, and it rests on this central nervous system activity rather than on the product's original use.

Two related predictions point the same way. Anxiety scored 99.08%, supported by rodent studies and one small open clinical study in generalized anxiety disorder (33 participants). "Sleep disorder, initiating and maintaining sleep" scored 99.03% but relies on the same zebrafish study, so it adds no independent evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07274371](https://clinicaltrials.gov/study/NCT07274371) | N/A | Active, not recruiting | 30 | Nightly foot massage with Brahmi-Gotu Kola oil vs sesame oil for sleep and mood in perimenopausal women. It is on-target for sleep but a combination herbal product with a topical route, and it has no results yet. |
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | N/A | Completed | 74 | Oral supplement plus topical regimen for skin appearance, redness and sensitivity. It targets skin, not sleep, so it gives no indication-specific evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38812527](https://pubmed.ncbi.nlm.nih.gov/38812527/) | 2024 | Preclinical (zebrafish larvae) | F1000Research | Centella asiatica ethanol extract in an insomnia model, associated with inhibition of orexin, ERK, Akt and p38 signalling. |

---

## US Market Information

The regulatory records list no approved indication text for these products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M014 | JAYSUING Silicone Scar Gel | Gel | Shantou Jaysuing Cleaning and Environmental Protection Technology Co., Ltd. |
| M020 | EELHOE Bio Sun Stick | Cream | Shantou Eelhoe Daily Chemical Technology Co., Ltd. |
| M020 | OUHOE Universal Colored Moisturizer | Cream | Shantou Ouhoe Technology Co., Ltd. |
| M020 | EELHOE Sun Cream | Cream | Shantou Eelhoe Daily Chemical Technology Co., Ltd. |
| Not listed | MADECASSOL | Gel | Lydia Co., Ltd. |

These are 5 of 20 licenses. Other forms on record include pellet, liquid and stick.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the only sleep-specific support is one zebrafish study and one small, ongoing trial of a multi-herb topical oil. No human efficacy data for sleep exist, and safety and mechanism data are missing, so the candidate cannot yet move forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A human sleep study using a defined, standardized Centella asiatica extract, ideally a randomized controlled trial with validated sleep outcomes
- Route and formulation assessment, since the marketed products are topical and an insomnia use would likely need an oral or otherwise systemic form
- Results from NCT07274371, and a review of the full literature set (only part of it was supplied)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


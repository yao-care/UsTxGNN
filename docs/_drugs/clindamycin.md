---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 535
evidence_level: L5
indication_count: 6
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

# Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic that inhibits the bacterial 50S ribosome and is used against susceptible bacterial infections. The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction. This is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (the license records provided list no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Clindamycin blocks bacterial protein synthesis by binding the 50S ribosomal subunit. It mainly covers Gram-positive organisms and anaerobes. The Evidence Pack does not include a detailed DrugBank mechanism entry beyond this class-level description.

The predicted indication is a poor mechanistic fit. Punctate epithelial keratitis is usually viral or toxic/inflammatory, and an antibacterial has no clear therapeutic link to it. The high score of 99.97% is not backed by any trial or publication, so it most likely reflects graph-level similarity rather than a real efficacy signal.

Two other predictions in the pack are worth noting. Exposure keratitis (score 99.80%) has a plausible but indirect link, since secondary bacterial infection is possible and clindamycin covers *S. aureus*. However, none of the retrieved papers tested clindamycin in that condition, and topical ocular clindamycin is not an established regimen. The other predictions (non-human animal disease, neurotrophic keratopathy, epidemic keratoconjunctivitis, postmenopausal atrophic vaginitis) show no meaningful evidence or mechanistic support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Clindamycin has 20 US authorizations in total. The main ones are below, and the records provided do not include approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA090902 | Clindamycin Palmitate Hydrochloride | Granule, for solution | Bryant Ranch Prepack |
| ANDA065061 | Clindamycin hydrochloride | Capsule | Proficient Rx LP |
| ANDA090108 | Clindamycin | Injection, solution | Medical Purchasing Solutions, LLC |
| ANDA064050 | Clindamycin Phosphate | Solution | Bryant Ranch Prepack |
| NDA050441 | CLEOCIN PHOSPHATE | Injection, solution | Henry Schein, Inc. |

Available routes across all licenses are oral, injectable, topical (cream) and other. No ophthalmic formulation appears, and route compatibility for the predicted indication has not been assessed.

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the database query.
- **Clostridioides difficile risk**: The literature retrieved for another prediction describes clindamycin as a known risk factor for *C. difficile* infection.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no supporting trials or literature. The antibacterial mechanism has no clear link to a viral or toxic/inflammatory keratitis. Of the six predictions in the pack, exposure keratitis is the only one with a plausible link, and it could be raised as a research question rather than a development candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed before safety screening
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence that clindamycin acts on the etiology of punctate epithelial keratoconjunctivitis
- An ophthalmic formulation and route-compatibility assessment
- Clarification of the original indication, since the license records list none

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


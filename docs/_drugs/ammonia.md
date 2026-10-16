---
layout: default
title: Ammonia
parent: Model Prediction Only (L5)
nav_order: 330
evidence_level: L5
indication_count: 6
monitor_inn: "AMMONIA"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "acne keloid", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "hydroa vacciniforme, familial"]
---

# Ammonia
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

# Ammonia: From Psoriasis and Other Skin Disorders to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Ammonia is listed in the knowledge graph for several dermatologic conditions, including psoriasis, acne and seborrheic dermatitis. The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis, parapsoriasis, acne, seborrheic dermatitis, pityriasis simplex, seborrheic keratosis, keratinization disease (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ammonia is a topical/counterirritant agent that has been associated with dermatologic conditions, but no mechanism has been documented that would link it to the predicted disease.

Acrodermatitis chronica atrophicans is a late-stage skin infection caused by *Borrelia* and is treated with antibiotics. Nothing in the data compiled for this report suggests that ammonia has antibacterial or other relevant activity against it. The high score (99.70%) most likely reflects graph-based proximity to the drug's original skin-related indications rather than a real pharmacologic connection.

The other top predictions show the same pattern. None has trial or literature support, and several raise safety concerns:

| Rank | Predicted Disease | Score | Main Concern |
|------|------|------|------|
| 2 | Neonatal dermatomyositis | 99.64% | Immune-mediated disease; no immunomodulatory activity documented; neonatal safety concern |
| 3 | Acne keloid | 99.63% | Closest to the original indications (acne), but no antifibrotic action is known |
| 4 | Childhood secondary interstitial lung disease associated with a connective tissue disease | 99.61% | Ammonia is a respiratory irritant; clear safety concern |
| 5 | Amyopathic dermatomyositis | 99.60% | Autoimmune disease requiring immunomodulation |
| 6 | Familial hydroa vacciniforme | 99.56% | Photosensitive disorder; no relevant activity known |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M011 | UpSniff Smelling Salts | Powder | Not stated (cancelled) |
| Not available | Ammonium Causticum | Pellet | Not stated (cancelled) |

Both authorizations are cancelled, and no valid single-ingredient or combination products remain on the market.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: The graph links ammonia to possible contraindications in anogenital human papillomavirus infection, common wart, diabetes mellitus, diabetic ketoacidosis, dermatitis, peripheral vascular disease, intermittent claudication and peripheral arterial disease.
- **Respiratory concern**: Ammonia is a respiratory irritant, and inhalation exposure can injure the lungs. This is especially relevant to the predicted pediatric lung disease.
- **Drug interactions**: No interaction records were found.

Package insert warnings and contraindications were not retrieved, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (Evidence Level L5), no documented mechanism, and no plausible pharmacologic link to a late-stage *Borrelia* skin infection that is treated with antibiotics. Both US authorizations are cancelled, and the knowledge graph flags several disease contraindications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking ammonia to the predicted disease
- Route-of-administration compatibility assessment and similarity analysis against the original indications
- A review of whether the model's top predictions are artifacts of graph proximity, given the lack of any mechanistic support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


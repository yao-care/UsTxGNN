---
layout: default
title: Lincomycin
parent: Model Prediction Only (L5)
nav_order: 862
evidence_level: L5
indication_count: 3
monitor_inn: "LINCOMYCIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia"]
last_modified_at: 2026-10-14
description: "Lincomycin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Lincomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Lincomycin: Polyclonal hyperviscosity syndrome
{: .text-alpha }

## One-Sentence Summary

Lincomycin is a lincosamide antibiotic, originally used to treat pneumococcal, staphylococcal and streptococcal infections.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9914 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 6 of 6) |
| Number of NDAs | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, lincomycin is a lincosamide antibiotic that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit. Its efficacy in gram-positive bacterial infections is established.

For the predicted indication, **no established mechanistic link was identified**. Polyclonal hyperviscosity syndrome arises from elevated serum immunoglobulins, for example in autoimmune disease or chronic infection. An antibacterial would not directly address this. Any benefit would at most be indirect, through treating an underlying infection.

The high TxGNN score (0.9914) is a TxGNN model (deep learning) prediction only. It is not supported by any trial or publication, and it should be treated as a hypothesis, not as evidence.

Two other predictions had the same pattern of no supporting evidence and no plausible mechanism:
- **Hyperamylasemia** (score 0.9914): lincomycin has no known action on amylase regulation, and antibiotics are occasionally associated with pancreatitis-related enzyme elevations, so the safety direction may be opposite to a benefit.
- **Congenital analbuminemia** (score 0.9906): this is a genetic disorder of albumin synthesis (ALB mutations) that a bacterial ribosome inhibitor would not correct.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050317 | Lincocin (Pharmacia & Upjohn) | Injection, solution | Valid |
| ANDA212770 | Lincomycin (PAI Pharma) | Injection | Valid |
| ANDA215657 | Lincomycin (Sagent) | Injection, solution | Valid |
| ANDA216662 | Lincomycin (Slate Run) | Injection, solution | Valid |
| ANDA201746 | Lincomycin (Henry Schein) | Injection, solution | Valid |

One further licence (ANDA215082, Armas Pharmaceuticals, injection solution) is also cancelled.

## Safety Considerations

- **Contraindication-related conditions (knowledge-graph data, not label text)**: liver failure, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, colitis, digestive system disease, and intestinal disease. This suggests caution in patients with gastrointestinal or hepatic disease.
- **Drug Interactions**: 21 interactions were recorded. Those rated Moderate:
  - Balsalazide
  - Picosulfuric acid
  - Attapulgite
  - Kaolin
  - Erythromycin
  - Ethinylestradiol

  Others have an unclassified severity, including warfarin, metformin, morphine, simvastatin, omeprazole, cimetidine, ranitidine, lidocaine and clotrimazole.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no plausible mechanistic link to the antibacterial action of lincomycin. In addition, the gastrointestinal contraindication signals (especially *C. difficile* colitis) add safety concerns.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for lincomycin
- A biological hypothesis connecting lincosamide pharmacology to immunoglobulin-driven hyperviscosity, followed by preclinical or observational evidence
- Clarification of the current regulatory and supply status, since the drug is marketed in the US with 6 valid licenses of 6
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


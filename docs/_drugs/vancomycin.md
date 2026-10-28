---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 1283
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vancomycin: predicted new indication Diffuse Scleroderma (evidence level L5). Approved use: Clostridium difficile colitis (other listed uses: staphylococcal infe…"
monitor_inn: "VANCOMYCIN"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
---

# Vancomycin
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

## Vancomycin: From Clostridium difficile Colitis to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic originally used for Gram-positive infections such as *Clostridium difficile* colitis, staphylococcal infections and endocarditis.
The TxGNN model predicts it may be effective for **Diffuse Scleroderma**, but there are **0 clinical trials** and only **1 publication** (an unrelated case report), so the prediction is **not supported by any direct evidence**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Clostridium difficile colitis (other listed uses: staphylococcal infection, endocarditis, bacterial arthritis, staphylococcal pneumonia) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 13) |
| Number of NDAs | 13 (all single-ingredient, 0 currently valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Vancomycin is known to be a glycopeptide antibiotic that inhibits cell wall synthesis in Gram-positive bacteria, and its efficacy in Gram-positive infections is well established.

That mechanism does not plausibly link to diffuse scleroderma, which is an autoimmune fibrotic disease and not a bacterial infection. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The single retrieved paper is a case report on erythroderma with sepsis and eosinophilia, and it does not show any benefit in scleroderma.

**Other predictions worth noting.** Most of the other top-ranked predictions also lack a mechanistic basis:
- **Paratyphoid fever, salmonellosis and typhoid fever:** these are caused by Gram-negative *Salmonella*, which vancomycin cannot penetrate because of the outer membrane, so it is intrinsically inactive.
- **Congenital analbuminemia, hyperamylasemia, polyclonal hyperviscosity syndrome, blood group incompatibility and premalignant hematological system disease:** no mechanistic rationale and little or no literature.
- **Streptococcal pneumonia (rank 9)** is the only biologically plausible prediction. Vancomycin is active against *Streptococcus pneumoniae*, including penicillin-resistant strains. It was rated L4 and flagged as a research question. However, this is closer to label or guideline positioning than to novel repurposing, and the supporting literature consists of indirect reviews and resistance surveillance.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | Diffuse exfoliative rash with sepsis and eosinophilia in a 56-year-old man, a possible erythroderma. It does not address vancomycin efficacy in scleroderma. |

## US Market Information

13 valid authorizations are on record, and none has approved indication text on record. The five below are representative.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050606 | Vancomycin hydrochloride (ANI Pharmaceuticals) | Capsule | Not available (valid) |
| NDA211962 | Vancomycin (Xellia) | Injection, solution | Not available (valid) |
| NDA210274 | Vancomycin hydrochloride (Hikma) | Injection, powder, for solution | Not available (valid) |
| NDA209481 | Vancomycin hydrochloride (Mylan Institutional) | Injection, powder, lyophilized, for solution | Not available (valid) |
| NDA050671 | Vancomycin hydrochloride (Baxter) | Injection, solution | Not available (valid) |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** kidney disease, pyoureter, neutropenia, agranulocytosis, hearing disorder and auditory system disease.
- **Drug interactions:** 100 interactions were found. The listed Major-level interactions are:
  - Human immunoglobulin G (intravenous)
  - Human botulinum neurotoxin A/B immune globulin
  - Vibrio cholerae CVD 103-HgR live vaccine

  Moderate-level interactions include:
  - NSAIDs (ketorolac, ibuprofen, celecoxib, diclofenac)
  - Nephrotoxic or ototoxic agents (amphotericin B, amikacin, capreomycin, carboplatin, bacitracin)
  - Metformin
  - Estrogens (estradiol, ethinylestradiol)
  - Mesalazine
  - Balsalazide
  - Ibandronate
  - Cholestyramine

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic link, no clinical trial and no relevant literature supporting vancomycin in diffuse scleroderma, so the prediction is probably an artifact of the TxGNN model (deep learning). The drug is marketed in the US with 13 valid licenses.

**To proceed, the following is needed:**
- Do not pursue diffuse scleroderma without new mechanistic or preclinical evidence.
- If a repurposing question is worth pursuing, evaluate streptococcal pneumonia (rank 9) as a label or guideline-positioning question rather than as a new indication.
- Obtain the FDA package insert warnings and contraindications, which are currently missing and block safety screening.
- Obtain detailed mechanism of action data from DrugBank.
- Confirm the current US availability and labeling of vancomycin products.
- Review renal, auditory and hematologic safety for any planned use, given the knowledge-graph contraindication signals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


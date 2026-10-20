---
layout: default
title: Sulfacetamide
parent: Model Prediction Only (L5)
nav_order: 1185
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sulfacetamide: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Acne, seborrheic dermatitis, conjunctivitis…"
monitor_inn: "SULFACETAMIDE"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis", "exposure keratitis", "parasitic eyelid infestation"]
---

# Sulfacetamide
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

# Sulfacetamide: From Acne and Seborrheic Dermatitis to Postinfectious Vasculitis

## One-Sentence Summary

Sulfacetamide is a sulfonamide antibacterial, originally used for skin conditions (acne, seborrheic dermatitis) and eye conditions (conjunctivitis, uveitis).
The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but **0 clinical trials** and **0 publications** currently support this prediction.
The prediction rests on graph-based modelling alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, seborrheic dermatitis, conjunctivitis, uveitis and related conditions (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 licenses in total (all cancelled; 1 NDA and 2 ANDAs, 1 without a listed number) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sulfacetamide is a sulfonamide antibacterial. Sulfonamides generally inhibit bacterial dihydropteroate synthase, blocking folate synthesis. Its use in acne, seborrheic dermatitis and bacterial conjunctivitis is consistent with this antibacterial role.

Postinfectious vasculitis, however, is an immune-mediated sequela that follows an infection rather than an active bacterial infection. A direct antibacterial mechanism is therefore unlikely to be relevant. The very high TxGNN score most likely reflects proximity to infectious-disease nodes in the knowledge graph rather than a testable biological link. This should be treated as a weak hypothesis.

Other top-ranked predictions, none of which has clinical trials, include:

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Post-bacterial disorder | 99.99% | Too broad and non-specific to define a testable hypothesis |
| **Otitis externa** | 99.99% | Most biologically plausible (topical antibacterial for an ear canal infection). However, sulfacetamide has limited activity against *Pseudomonas aeruginosa*, and established fluoroquinolone and aminoglycoside drops are available |
| Post-infectious syndrome | 99.99% | No clear target; immune-mediated |
| Infective urethral stricture | 99.99% | Fibrotic condition; no relevant urinary exposure from topical use |
| Chagas cardiomyopathy | 99.99% | No evidence of activity against *T. cruzi*; topical use would not reach the heart |
| Infection-related hemolytic uremic syndrome | 99.99% | Antibiotics may worsen toxin-mediated disease; potential safety concern |
| Punctate epithelial keratoconjunctivitis | 99.98% | Ocular delivery is established, but the condition is often viral or inflammatory |
| Exposure keratitis | 99.90% | Only literature is an adverse-event case report |
| Parasitic eyelid infestation (Demodex) | 99.83% | Indirect plausibility only; sulfacetamide is not acaricidal |

## Clinical Trial Evidence

Currently no related clinical trials registered for postinfectious vasculitis or for any of the other top-ranked predicted indications.

## Literature Evidence

Currently no related literature available for postinfectious vasculitis.

For other predicted indications, two papers were retrieved. Neither supports efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3157322](https://pubmed.ncbi.nlm.nih.gov/3157322/) | 1985 | Case report (adverse event) | American Journal of Ophthalmology | An 8-year-old boy developed erythema multiforme major after topical sulfacetamide for conjunctivitis. This is a hypersensitivity safety signal, not efficacy evidence (linked to exposure keratitis) |
| [18561612](https://pubmed.ncbi.nlm.nih.gov/18561612/) | 2007 | Observational/Review | Annales Academiae Medicae Stetinensis | Describes Demodex as a cause of chronic marginal blepharitis. Sulfacetamide is not evaluated (linked to parasitic eyelid infestation) |

## US Market Information

All four US licenses are cancelled, and none has approved indication text on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019931 | Sodium sulfacetamide (Oceanside Pharmaceuticals) | Lotion | Not available |
| ANDA089560 | Sulfacetamide Sodium (Asclemed USA, Inc.) | Solution | Not available |
| ANDA040066 | Sulfacetamide Sodium (NuCare Pharmaceuticals, Inc.) | Solution/Drops | Not available |
| Not listed | PLEXION NS (Eckson Labs, LLC) | Shampoo | Not available |

## Safety Considerations

- **Hypersensitivity signal**: A published case report describes erythema multiforme major in a child after topical sulfacetamide (PMID 3157322).
- **Knowledge-graph contraindication signals** (not label text, so they need verification against the package insert): the graph links sulfacetamide to contraindications in many conditions. Examples include kidney disease, liver disease, hematologic disease, porphyria, G6PD deficiency, diabetes mellitus, cardiovascular disease, hypertension, hyperthyroidism, open-angle and angle-closure glaucoma, herpes simplex virus keratitis, and dermatitis.
- **Potential concern for the predicted indication**: In infection-related hemolytic uremic syndrome, antibiotics are often avoided.

Please refer to the package insert for complete warnings, contraindications and drug interaction information. No drug interaction data were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for postinfectious vasculitis has no clinical trials or literature (Evidence Level L5). Its mechanism is implausible, because an antibacterial would not be expected to treat an immune-mediated sequela. The drug has no currently valid US license, and package insert safety data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A more testable hypothesis. Of the predicted indications, otitis externa is the most plausible, though it would need comparison against existing topical agents.
- Evidence that links sulfacetamide to vasculitis or other immune-mediated post-infectious conditions, or a decision to deprioritise this prediction
- Review of the cancelled license status and available formulations if development is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


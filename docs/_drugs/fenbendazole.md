---
layout: default
title: Fenbendazole
parent: Model Prediction Only (L5)
nav_order: 697
evidence_level: L5
indication_count: 10
---

# Fenbendazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Fenbendazole: From Anthelmintic (No Human Indication on Record) to Urinary Bladder Carcinoma

## One-Sentence Summary

Fenbendazole is a benzimidazole anthelmintic, mainly a veterinary drug, and no approved indication text is recorded for its one marketed capsule product.
The TxGNN model predicts it may be effective for **urinary bladder carcinoma** (score 99.99%), but the exact term has **0 clinical trials** and **0 publications**.
This is a model prediction only, with no actual studies behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (approved indication text is empty) |
| Predicted New Indication | Urinary bladder carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this drug. Based on general pharmacology, fenbendazole is a benzimidazole that inhibits tubulin polymerization. In proliferating cells this can cause G2/M cell-cycle arrest and apoptosis, so it is a plausible antiproliferative mechanism in urothelial tumor cells.

The TxGNN prediction is not tied to a known original indication, because none is recorded. The mechanistic link is class-level reasoning and has not been validated for bladder carcinoma. Fenbendazole is a veterinary anthelmintic, so human dosing, bioavailability and toxicity are uncharacterized.

The related term "urinary bladder neoplasm" (rank 2) has one 2024 paper (PMID 39128990). It studies intravesical fenbendazole combined with CRISPR-Cas13a for bladder cancer, and the title suggests a preclinical study. That evidence is indirect and does not upgrade the level for the exact predicted term.

Other high-scoring predictions are bladder subtypes, including urothelial carcinoma variants, adenocarcinoma variants and squamous papilloma. Their scores likely reflect proximity in the knowledge graph, not subtype-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the exact predicted term. See the note above for the one indirect paper found under the parent term "urinary bladder neoplasm".

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not recorded | Fenbendazole 222 MG (B & L Healthcare Products INC) | Capsule (oral) | Not recorded |

## Safety Considerations

No warnings, contraindications, or drug interaction records were retrieved (the DDI query returned no results). The package insert has not been obtained, so safety information should be taken from the label once available. Human safety of fenbendazole is uncharacterized.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is L5, which means model prediction only. There are no trials for the exact term, and the only related paper is indirect and likely preclinical. The package insert and MOA data are also missing, and the missing label blocks safety screening.

**To proceed, the following is needed:**
- The package insert (warnings and contraindications), to clear the blocking safety data gap
- Mechanism-of-action data from DrugBank
- Full-text review of PMID 39128990 to confirm study type and fenbendazole's role
- A search for preclinical and human data on benzimidazole antitubulin agents in bladder cancer
- Human dosing, bioavailability and toxicity data, and an assessment of whether intravesical or oral routes are feasible

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


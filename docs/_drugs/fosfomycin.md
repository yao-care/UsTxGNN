---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 737
evidence_level: L5
indication_count: 8
monitor_inn: "FOSFOMYCIN"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
last_modified_at: 2026-10-28
description: "Fosfomycin: predicted new indication Uterine inflammatory disease (evidence level L5). Approved use: Urinary tract infection"
---

# Fosfomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Fosfomycin: From Urinary Tract Infection to Uterine Inflammatory Disease
{: .text-alpha }

## One-Sentence Summary

Fosfomycin is an antibiotic. Urinary tract infection is recorded as its original use.
The TxGNN model predicts it may be effective for **uterine inflammatory disease**, but no study directly examines this use. The data compiled for this report include **2 clinical trials** and **1 publication**, and none of them test fosfomycin for this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (a relation recorded in the knowledge graph; no approved-indication text is available in the licence record) |
| Predicted New Indication | Uterine inflammatory disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Number of Approvals | 1 NDA |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, fosfomycin is a broad-spectrum bactericidal antibiotic. It inhibits MurA (UDP-N-acetylglucosamine enolpyruvyl transferase), which blocks an early step of bacterial cell wall (peptidoglycan) synthesis.

Uterine inflammatory disease is often caused by bacterial infection, so an antibacterial drug could plausibly be useful. This reasoning is inferred from general pharmacology. No direct evidence shows that fosfomycin reaches adequate concentrations in uterine tissue or works against the organisms involved.

The prediction therefore rests on the model's score and a general mechanistic argument, not on studies of this disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3,520 | Pediatric pharmacokinetics of understudied drugs given per standard of care. It does not test efficacy in uterine inflammatory disease. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | Pharmacokinetics, pharmacodynamics and safety of understudied drugs in children and young adults. It is a general platform study with no link to uterine inflammatory disease. |

Both trials were graded as having no disease-specific relevance.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35653789](https://pubmed.ncbi.nlm.nih.gov/35653789/) | 2022 | Cohort | J Obstet Gynaecol | Prospective study of cystitis symptoms and bacteriuria in women with endometriosis taking dienogest or combined oral contraceptives after laparoscopic surgery. It does not evaluate fosfomycin for uterine inflammatory disease. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212271 | Contepo (Meitheal Pharmaceuticals Inc.) | Injection, powder, for solution | Indication text not available in the licence record |

A 2026 publication (PMID 41711122) describes intravenous fosfomycin (Contepo) as FDA-approved for complicated urinary tract infection. Uterine inflammatory disease is not an approved use.

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph lists contraindication relations with kidney disease, pyoureter, *Clostridium difficile* colitis and perinatal necrotizing enterocolitis. These need confirmation against the official label.
- **Drug Interactions:** Three interactions were found in the DDInter database:
  - Balsalazide (moderate)
  - Picosulfuric acid (moderate)
  - Metoclopramide (minor)

For warnings and contraindications from the label, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trial or publication studies fosfomycin in uterine inflammatory disease. The two trials are generic pediatric pharmacokinetic studies, and the one publication is about cystitis in women with endometriosis. The evidence is model prediction only (L5).

By comparison, a different prediction for fosfomycin, pyelitis, is supported by a Phase 2/3 RCT of intravenous fosfomycin in complicated UTI including acute pyelonephritis (PMID 30861061). It is a closer extension of the existing urinary use and may be a better candidate to pursue first.

**To proceed, the following is needed:**
- Clinical or microbiological evidence that fosfomycin is active against the pathogens of uterine infection, such as endometritis or pelvic inflammatory disease
- Data on fosfomycin penetration into uterine and pelvic tissue
- Detailed mechanism of action data
- Package insert warnings and contraindications, to replace the knowledge-graph relations
- A safety review for the target population, including pregnant and postpartum women, who are common in this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


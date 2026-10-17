---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 1264
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Trimethoprim: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Urinary tract infection, infectious otitis media, pneumocystosis…"
---

# Trimethoprim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Trimethoprim: From Urinary Tract Infection to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is an antibacterial originally used for urinary tract infection, infectious otitis media, pneumocystosis, shigellosis and bacterial eye infections such as conjunctivitis.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, but currently there are **0 clinical trials** and **0 publications** supporting this specific indication. The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, infectious otitis media, pneumocystosis, shigellosis, conjunctivitis, blepharoconjunctivitis (from the knowledge graph; no approved-indication text is available from US licences) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 7 (all cancelled; 1 NDA and 6 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, trimethoprim inhibits bacterial dihydrofolate reductase, and it is used in ophthalmic solutions, usually combined with polymyxin B, for bacterial conjunctivitis and blepharoconjunctivitis.

The link to punctate epithelial keratoconjunctivitis is weak. This condition is frequently viral (for example adenoviral) or immune-mediated, so an antibacterial would not be expected to address the primary cause. The high score likely reflects the closeness of this disease to the already-listed conjunctivitis indications in the knowledge graph, rather than an independent therapeutic signal. Bacterial superinfection prophylaxis is a theoretical role only and is not supported by any evidence provided.

For context, a second prediction, **conjunctivitis**, scored 99.17%. It is already among trimethoprim's original indications, so it is not a true repurposing candidate. Its supporting literature is summarised below only as background for the existing use.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis. No trials were found for the conjunctivitis prediction either.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

Background literature for the existing conjunctivitis use (not evidence for the new indication):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT / comparative study (design not confirmed) | J Pediatr Ophthalmol Strabismus | Multicenter comparison of polymyxin B/trimethoprim with 0.5% moxifloxacin on speed of clinical efficacy in bacterial conjunctivitis |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Clinical evaluation | Am J Ophthalmol | Trimethoprim combined with polymyxin B (with or without sulfacetamide) evaluated for efficacy and safety in bacterial conjunctivitis or blepharitis |
| [2418736](https://pubmed.ncbi.nlm.nih.gov/2418736/) | 1985 | Clinical study | Ann Ophthalmol | Trimethoprim-polymyxin B was compared with a trimethoprim-sulfacetamide-polymyxin B combination in surface ocular bacterial infections |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Survey | Clin Ther | Survey of children with acute bacterial conjunctivitis treated with trimethoprim-polymyxin B ophthalmic solution |
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Systematic review / meta-analysis | J Pediatric Infect Dis Soc | Antibiotic treatments, including trimethoprim, for neonatal chlamydial conjunctivitis (not trimethoprim-specific) |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Review | Paediatr Child Health | Etiology, clinical features and management of acute infectious conjunctivitis in children |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Review | J Pediatr Ophthalmol Strabismus | Controlling contagious bacterial conjunctivitis and limiting transmission with antimicrobials |

## US Market Information

All licences are cancelled; no valid licence is currently listed. Approved-indication text was not available.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA018679 | Trimethoprim (Dr. Reddy's) | Tablet | Cancelled |
| ANDA091437 | Trimethoprim (Lupin) | Tablet | Cancelled |
| ANDA216393 | Trimethoprim (Novitium) | Tablet | Cancelled |
| ANDA064120 | Polymyxin B Sulfate and Trimethoprim (Proficient Rx) | Solution/drops | Cancelled |
| ANDA064211 | Polymyxin B Sulfate and Trimethoprim (NuCare) | Solution | Cancelled |

Two further cancelled licences (ANDA211572 and ANDA065006) are polymyxin B/trimethoprim ophthalmic solutions.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Knowledge-graph contraindication signals** (not label text): porphyria and other porphyrin metabolism disorders, kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, G6PD deficiency, folic acid deficiency anemia, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, glycogen storage disease, cystinuria, galactosemia and pyoureter.
- **Drug interactions** (100 recorded; examples):
  - Major: potassium citrate, potassium bicarbonate, potassium chloride, potassium gluconate (hyperkalaemia risk)
  - Moderate: metformin, pioglitazone, rosiglitazone, repaglinide, balsalazide, picosulfuric acid, sapropterin
  - Severity not classified: pantoprazole, omeprazole, doxycycline, clotrimazole, morphine, sucralfate, vancomycin, lactulose, simvastatin

These apply mainly to systemic use; their relevance to topical ophthalmic use is unclear.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.57% score is a computational prediction only, with no trials or literature for punctate epithelial keratoconjunctivitis. The condition is often viral or immune-mediated, so an antibacterial is mechanistically unlikely to address it. All US licences are also cancelled.

**To proceed, the following is needed:**
- Evidence that bacterial infection plays a role in this condition, or any clinical or preclinical data in this setting
- Mechanism of action data and package insert warnings and contraindications
- Confirmation of the route and formulation (ophthalmic) and of current market availability
- A comparison with existing standard care, to judge whether any added benefit is plausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 737
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fosfomycin: predicted new indication Ureaplasma urethritis (evidence level L5). Approved use: Urinary tract infection"
monitor_inn: "FOSFOMYCIN"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
---

# Fosfomycin
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

# Fosfomycin: From Urinary Tract Infection to Ureaplasma Urethritis

## One-Sentence Summary

Fosfomycin is an antibiotic originally used to treat urinary tract infections.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**,
but **no clinical trials and no publications** specific to this indication were found in the data compiled for this report.
The closest supported direction among the top predictions is **gonococcal urethritis**, with **6 publications** (including one randomized controlled trial).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (from the knowledge graph; no approved indication text is listed on the US license) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (for Ureaplasma urethritis: model prediction only) |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the published literature, fosfomycin is an epoxide antibiotic that inhibits an early step in bacterial cell wall synthesis. It has broad in vitro activity, including against some multidrug-resistant Gram-negative bacteria. Its efficacy in urinary tract infection is established.

Ureaplasma urethritis is an infection of the lower urogenital tract, anatomically close to the urinary tract infections for which fosfomycin is used. This explains why the model links the two. However, *Ureaplasma* species have no cell wall. A drug that blocks cell wall synthesis therefore has no obvious target in this organism, so the mechanistic basis for this specific prediction is weak and unsupported by any evidence found. Gonococcal urethritis (rank 2) is more plausible, since *Neisseria gonorrhoeae* has a cell wall and fosfomycin has been tested against it.

## Clinical Trial Evidence

Currently no related clinical trials are registered for Ureaplasma urethritis.

For reference, two trials were found for the lower-ranked prediction "uterine inflammatory disease". They are general pediatric pharmacokinetic studies of understudied drugs, not trials of fosfomycin for this condition:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Pharmacokinetics of understudied drugs given to children as standard of care |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | Pharmacokinetics, pharmacodynamics and safety of understudied drugs in children and young adults |

## Literature Evidence

Currently no related literature is available for Ureaplasma urethritis. The table below shows the most relevant literature for the closest predicted indication, **gonococcal urethritis**:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/) | 2016 | RCT (open-label) | Clin Microbiol Infect | Fosfomycin trometamol 3 g orally on days 1, 3 and 5 tested in 152 men with uncomplicated gonococcal urethritis; 126 completed the study |
| [832528](https://pubmed.ncbi.nlm.nih.gov/832528/) | 1977 | Clinical series | Chemotherapy | 70 patients treated with intramuscular fosfomycin; 92% cure with 4 g in divided doses and 86% with a single 4 g dose |
| [832523](https://pubmed.ncbi.nlm.nih.gov/832523/) | 1977 | Clinical study | Chemotherapy | Bacteriological evaluation in 959 patients across multiple infections, including gonococcal urethritis |
| [35820778](https://pubmed.ncbi.nlm.nih.gov/35820778/) | 2023 | Secondary analysis of a trial | Sex Transm Infect | Spontaneous clearance of asymptomatic gonorrhoea; not specific to fosfomycin |
| [19593988](https://pubmed.ncbi.nlm.nih.gov/19593988/) | 2009 | Clinical study | Zhonghua Nan Ke Xue | Diagnosis and treatment of non-gonococcal Neisseria genitourinary infection in men |
| [17878816](https://pubmed.ncbi.nlm.nih.gov/17878816/) | 2007 | Case report | J Fr Ophtalmol | Gonococcal conjunctivitis with corneal abscess after urethritis; limited relevance |

For the original indication, one relevant publication is the Phase 2/3 ZEUS randomized trial ([30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/), 2019, Clin Infect Dis), which compared intravenous fosfomycin (ZTI-01) with piperacillin-tazobactam in complicated urinary tract infection, including acute pyelonephritis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212271 (cancelled) | Contepo | Injection, powder, for solution | Not listed in the data compiled for this report |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis
- **Drug Interactions** (3 found):
  - Balsalazide: Moderate
  - Picosulfuric acid: Moderate
  - Metoclopramide: Minor

Please refer to the package insert for warnings and full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for Ureaplasma urethritis is very high, but no clinical trials or publications support it. In addition, *Ureaplasma* lacks a cell wall, which weakens the mechanistic rationale. The US product (Contepo) is also in cancelled status.

**To proceed, the following is needed:**
- In vitro susceptibility data for fosfomycin against *Ureaplasma* species
- Mechanism of action data (MOA) to clarify the biological link
- FDA package insert warnings and contraindications
- Consider prioritizing gonococcal urethritis, which has an RCT and older clinical series, and verify the current gonococcal resistance and treatment guidelines
- Clarification of the regulatory status of Contepo and of any other fosfomycin products in the US
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


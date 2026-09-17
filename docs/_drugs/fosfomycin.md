---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 737
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fosfomycin: From Urinary Tract Infection to Pyelitis and Gonococcal Urethritis

## One-Sentence Summary

Fosfomycin is a bactericidal antibiotic whose established use covers urinary tract infections, including complicated UTI and acute pyelonephritis. TxGNN screened it against 10 candidate indications; of these, only **Pyelitis** and **Gonococcal urethritis** are supported by real clinical evidence — including a completed Phase 3 RCT (ZEUS trial) and a 2016 RCT, respectively — while the single highest-scoring prediction (Ureaplasma urethritis) is very likely a **false positive**, since Ureaplasma lacks the cell-wall target that fosfomycin acts on.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary Tract Infection (complicated UTI / acute pyelonephritis) |
| Predicted New Indication | Pyelitis (primary); Gonococcal urethritis (secondary) |
| TxGNN Prediction Score | 99.37% (Pyelitis) / 99.99% (Gonococcal urethritis) |
| Evidence Level | L1 (Pyelitis) / L2 (Gonococcal urethritis) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails (Pyelitis, Gonococcal urethritis) / Hold (remaining 8 candidates) |

**Note:** TxGNN's single top-ranked prediction, *Ureaplasma urethritis* (score 99.99%), is **not** used as the headline finding. See "Screened Indications Overview" below for why it is held.

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action documentation for fosfomycin is currently a data gap (DG002, High severity, requires DrugBank lookup). Based on the mechanistic evidence embedded in the literature reviewed here, fosfomycin inhibits **MurA (UDP-N-acetylglucosamine enolpyruvyl transferase)**, blocking an early step of bacterial peptidoglycan cell-wall synthesis. This gives it bactericidal, broad-spectrum activity against Gram-negative organisms such as *E. coli*, and it is renally excreted, reaching high concentrations in urine.

**Pyelitis** (inflammation of the renal pelvis) shares the same anatomical site and pathogen profile (predominantly *E. coli*) as fosfomycin's already-recognized use in complicated UTI and acute pyelonephritis. This is less a novel repurposing signal and more a natural label extension, which is why it carries the strongest evidence of the ten candidates: a completed Phase 3 RCT (ZEUS trial) compared IV fosfomycin against piperacillin-tazobactam in complicated UTI/acute pyelonephritis and demonstrated non-inferiority.

**Gonococcal urethritis** is mechanistically more distant but still plausible: *N. gonorrhoeae* retains a peptidoglycan cell wall, so MurA inhibition remains a valid target. Clinical use dates back to the 1970s (intramuscular fosfomycin cohorts), and a 2016 open-label RCT confirmed efficacy of oral fosfomycin trometamol in men with uncomplicated gonococcal urethritis. Because first-line gonorrhea therapy is now ceftriaxone, fosfomycin would sit as an alternative option, particularly relevant where antimicrobial resistance limits standard regimens.

By contrast, *Ureaplasma urethritis* — TxGNN's highest-scoring prediction — is mechanistically contradicted: Ureaplasma is a cell-wall-deficient, mycoplasma-like organism, so a cell-wall synthesis inhibitor has no theoretical target. This high score most likely reflects a knowledge-graph artifact from co-infection/comorbidity associations rather than true pharmacological signal, and no clinical trials or literature support it.

---

## Screened Indications Overview

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Note |
|------|-----------|-------------|-----------------|----------|------|
| 1 | Ureaplasma urethritis | 99.99% | L5 | Hold | Mechanistically implausible — no cell wall target; likely false positive |
| 2 | Gonococcal urethritis | 99.99% | L2 | **Proceed with Guardrails** | Historical use + 2016 RCT |
| 3 | Uterine inflammatory disease (PID) | 99.98% | L4 | Hold | Weak spectrum coverage of typical PID pathogens; no efficacy trials |
| 4 | Xanthogranulomatous pyelonephritis | 99.98% | L5 | Hold | Primarily a surgical disease; no antibiotic-monotherapy evidence |
| 5 | Epiglottitis | 99.93% | L5 | Hold | Wrong pathogen spectrum; no supporting evidence |
| 6 | Urogenital tuberculosis | 99.88% | L5 | Hold | No known antimycobacterial activity |
| 7 | Laryngitis | 99.68% | L4 | Hold | Only indirect evidence (nebulizer/sinusitis studies) |
| 8 | Polyclonal hyperviscosity syndrome | 99.47% | L5 | Hold | Non-infectious; biologically implausible |
| 9 | Hyperamylasemia | 99.47% | L5 | Hold | Non-infectious; biologically implausible |
| 10 | Pyelitis | 99.37% | L1 | **Proceed with Guardrails** | Phase 3 RCT (ZEUS) supports IV formulation in the pyelonephritis spectrum |

---

## Clinical Trial Evidence

No clinical trials are directly registered under Pyelitis or Gonococcal urethritis in the evidence pack (the pivotal Pyelitis RCT, ZEUS, is indexed as a PubMed publication rather than a registry entry — see Literature Evidence below).

The only registered trials retrieved (under *Uterine inflammatory disease*, relevance grade C, low disease-specificity) are general pediatric pharmacokinetic studies and are not disease-specific efficacy evidence:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | Broad PK/safety study of understudied drugs in children; not a disease-specific efficacy trial |
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Pediatric PK characterization of understudied drugs; not disease-specific |

---

## Literature Evidence

| PMID | Year | Type | Journal | Indication | Key Findings |
|------|-----|------|------|------|---------|
| [30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/) | 2019 | RCT (Phase 2/3, ZEUS) | Clin Infect Dis | Pyelitis | IV fosfomycin (ZTI-01) non-inferior to piperacillin-tazobactam in complicated UTI/acute pyelonephritis |
| [27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/) | 2016 | RCT | Clin Microbiol Infect | Gonococcal urethritis | Open RCT: oral fosfomycin trometamol effective in uncomplicated male gonococcal urethritis |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Systematic review / NMA | J Comp Eff Res | Pyelitis | Network meta-analysis of treatment options for complicated UTI/acute pyelonephritis |
| [33819054](https://pubmed.ncbi.nlm.nih.gov/33819054/) | 2021 | Guideline | Ann Intern Med | Pyelitis | ACP best-practice advice on short-course antibiotics for common infections including UTI |
| [32303061](https://pubmed.ncbi.nlm.nih.gov/32303061/) | 2020 | Retrospective Cohort | J Antimicrob Chemother | Pyelitis | 1-year real-world review of oral fosfomycin outcomes in pyelonephritis/complicated UTI |
| [31608743](https://pubmed.ncbi.nlm.nih.gov/31608743/) | 2020 | Review | Postgrad Med | Pyelitis | Fosfomycin among recommended first-line agents amid rising UTI antimicrobial resistance |
| [832528](https://pubmed.ncbi.nlm.nih.gov/832528/) | 1977 | Cohort (open-label) | Chemotherapy | Gonococcal urethritis | 70 patients treated with IM fosfomycin; 86–92% cure rates across dosing regimens |
| [35820778](https://pubmed.ncbi.nlm.nih.gov/35820778/) | 2023 | Cohort (secondary analysis) | Sex Transm Infect | Gonococcal urethritis | Spontaneous clearance data from NABOGO trial informing antibiotic-treatment context |
| [30854892](https://pubmed.ncbi.nlm.nih.gov/30854892/) | 2019 | Review | Future Microbiol | Pyelitis | Overview of IV fosfomycin (ZTI-01) microbiology, PK, and clinical development for cUTI |
| [19593988](https://pubmed.ncbi.nlm.nih.gov/19593988/) | 2009 | Review | Zhonghua Nan Ke Xue | Gonococcal urethritis | Diagnosis/treatment considerations for non-gonococcal *Neisseria* genitourinary infection |

---

## US Market Information

No license records are currently available — the drug is **not marketed** in this jurisdiction (0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not yet available in the current dataset (DG001, blocking severity — TFDA/local label warnings must be sourced before any S1 safety assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Pyelitis and Gonococcal urethritis only) / **Hold** (remaining 8 candidates, including the top TxGNN-ranked Ureaplasma urethritis)

**Rationale:**
Pyelitis is essentially a label-adjacent extension of fosfomycin's established UTI/pyelonephritis use and is backed by a completed Phase 3 RCT. Gonococcal urethritis has weaker but real evidence — historical clinical use plus a modern RCT — but should be positioned as an alternative/resistance-driven option rather than first-line. All other candidates, including the single highest-scoring prediction, lack adequate mechanistic or clinical support and should not advance without new evidence.

**To proceed, the following is needed:**
- Local regulatory safety labeling (key warnings, contraindications, DDI) — currently blocking (DG001)
- Formal DrugBank/MOA documentation to replace the current data gap (DG002)
- Local/regional *N. gonorrhoeae* antimicrobial-resistance surveillance data to justify fosfomycin's role as a guardrail-bound alternative for gonococcal urethritis
- Since the product is not currently marketed here, a registration/import pathway assessment if either indication is pursued locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


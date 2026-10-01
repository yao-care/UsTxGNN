---
layout: default
title: Amikacin
parent: Model Prediction Only (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
---

# Amikacin
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

# Amikacin: From Gram-Negative Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Amikacin is an aminoglycoside antibacterial, marketed in the US as an injection. The TxGNN model predicts it may be effective for **Paratyphoid Fever**, but there are **0 clinical trials** and only **12 publications** (all case reports, surveys or observational studies, none testing amikacin efficacy in paratyphoid). The evidence is weak, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured: all approved-indication fields in the US records are empty (amikacin is a systemic aminoglycoside antibacterial) |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 (in vitro and mechanism-level data only; no efficacy studies) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 (all generic ANDA licenses) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Amikacin is an aminoglycoside that binds the 30S ribosomal subunit and is bactericidal against aerobic Gram-negative bacilli. Salmonella Paratyphi, a Gram-negative bacillus, is often susceptible in vitro. That susceptibility is the only mechanistic reason the prediction looks plausible.

There are strong reasons for caution:
- Salmonella lives inside cells, and aminoglycosides penetrate tissue and cells poorly, so they are generally not clinically effective for enteric fever.
- The retrieved literature is mostly case reports and antibiogram surveys, with no amikacin efficacy data for paratyphoid.
- For typhoid fever, a closely related prediction, a 1989 study (PMID 2598731) reported a clinical effective rate of 36.4% with amikacin (11 patients) versus 100% with ofloxacin (64 patients). This is a small, old, non-randomized comparison, but it points the same way.

The 99.82% score therefore reflects knowledge-graph proximity (Gram-negative pathogen, antibacterial), not demonstrated clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case report | Pediatr Hematol Oncol | Child with leukemia and S. Paratyphi B acalculous cholecystitis treated successfully with cefepime, amikacin and G-CSF. Amikacin was one part of a combination, so its contribution is unclear. |
| [17337835](https://pubmed.ncbi.nlm.nih.gov/17337835/) | 2007 | Case report | Indian J Pediatr | Neonatal sepsis due to multidrug-susceptible S. Paratyphi A. The excerpt does not mention amikacin. |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Clinical study | Mikrobiyol Bul | 48 children with paratyphi B infection, with treatment and antibiogram results for strains resistant to classical therapy. Amikacin results are not visible in the excerpt. |
| [9459410](https://pubmed.ncbi.nlm.nih.gov/9459410/) | 1997 | Case report | J Infect | Quinolone-resistant S. Paratyphi B meningitis in a newborn. Shows resistance problems but not amikacin efficacy. |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Case series | J Pediatr Surg | Four children with splenic abscess managed by needle aspiration plus antibiotics. The abstract does not name amikacin. |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Cross-sectional (microbiology) | Pak J Biol Sci | Isolation and identification of S. Paratyphi from enteric fever patients in Quetta. Microbiology only. |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Prospective cohort | J Indian Med Assoc | 145 children with culture-positive enteric fever, with antibiotic sensitivity patterns. |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Cross-sectional (antibiogram) | JNMA J Nepal Med Assoc | Blood culture isolates and antibiograms at a teaching hospital. No amikacin efficacy data. |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Observational (susceptibility) | Med J Armed Forces India | Susceptibility of S. Typhi and S. Paratyphi A isolates in northern India, noting re-emergence of chloramphenicol sensitivity. |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Surveillance | New Microbiol | Occurrence of S. Typhi and S. Paratyphi in Jordan, 1988–2000. Epidemiology only. |

None of these papers is an RCT or shows amikacin efficacy in paratyphoid fever.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA063315 | Amikacin Sulfate (Hikma Pharmaceuticals USA Inc.) | Injection | Not stated in retrieved record |
| ANDA204040 | Amikacin Sulfate (Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc.) | Injection, solution | Not stated in retrieved record |
| ANDA218146 | Amikacin Sulfate (Qilu Pharmaceutical Co., Ltd.) | Injection, solution | Not stated in retrieved record |

There are 12 licenses in total. Only 3 distinct authorizations are shown because ANDA204040 appears three times with identical details.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings or contraindications were retrieved, and no drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no literature showing amikacin efficacy in paratyphoid fever. Aminoglycosides are not considered effective for enteric fever because of Salmonella's intracellular niche. The high TxGNN score is best read as a model signal, not clinical support.

**To proceed, the following is needed:**
- The US package insert warnings and contraindications, which are missing and block safety screening.
- Detailed mechanism-of-action data from DrugBank.
- Direct clinical evidence of amikacin in enteric fever, such as comparative studies against standard agents (fluoroquinolones, cephalosporins, azithromycin), and a review of current treatment guidelines.
- Intracellular and tissue-penetration pharmacokinetic and pharmacodynamic data supporting a workable regimen.
- The approved-indication text for the existing US labels, so the original indication can be documented.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


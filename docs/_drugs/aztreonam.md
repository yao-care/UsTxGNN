---
layout: default
title: Aztreonam
parent: Model Prediction Only (L5)
nav_order: 435
evidence_level: L5
indication_count: 10
monitor_inn: "AZTREONAM"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-10-30
description: "Aztreonam: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Urinary tract infection, Pseudomonas aeruginosa infection…"
---

# Aztreonam
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

## Aztreonam: From Gram-Negative Bacterial Infections to Polyclonal Hyperviscosity Syndrome
{: .text-alpha }

## One-Sentence Summary

Aztreonam is a monobactam antibiotic, originally used for gram-negative bacterial infections such as urinary tract infection, Pseudomonas aeruginosa infection, peritonitis and Escherichia coli infection.
The TxGNN model predicts it may be effective for **gonococcal urethritis**, the only high-ranked prediction with meaningful supporting evidence, backed by **0 registered clinical trials** and **6 publications** (one 2020 single-arm trial and several 1980s clinical studies).
The top-scoring predictions (such as polyclonal hyperviscosity syndrome) have no plausible mechanistic link and look like model artifacts.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, Pseudomonas aeruginosa infection, peritonitis, Escherichia coli infection (the data compiled for this report contains no approved-indication label text) |
| Predicted New Indication | Gonococcal urethritis (best-supported of the top 10 predictions; the rank-1 prediction is polyclonal hyperviscosity syndrome, which has no supporting evidence) |
| TxGNN Prediction Score | 0.9959 (gonococcal urethritis); rank-1 prediction scored 0.9973 |
| Evidence Level | L5 (gonococcal urethritis: single-arm and uncontrolled clinical studies, no RCTs); L5 for the rank-1 prediction |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of FDA Applications | 3 (valid: 3) |
| Recommended Decision | Hold (gonococcal urethritis may be pursued as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, aztreonam is a monobactam that inhibits bacterial cell wall synthesis by binding penicillin-binding protein 3 (PBP3). It is active against aerobic gram-negative bacteria and is stable against many beta-lactamases.

*Neisseria gonorrhoeae* is a gram-negative aerobe susceptible to PBP3-targeting monobactams. Aztreonam is stable against the penicillinase produced by penicillin-resistant gonococci. Its original indications (urinary tract infection, *E. coli* infection, peritonitis) are also gram-negative infections, so extension to gonococcal urethritis is mechanistically coherent.

Important caveats apply. The evidence is mostly historical (1980s), there is no randomized evidence, and aztreonam-high-resistant gonococci have been reported. Current guidelines favor other agents, so any renewed interest would be as a niche option for resistant strains or beta-lactam-allergic patients.

Most of the other top-10 predictions are not supported:
- **Polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological system disease, monoclonal gammopathy:** non-infectious conditions with no antibacterial target. The high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Ureaplasma urethritis:** *Ureaplasma* has no cell wall, so aztreonam is intrinsically ineffective.
- **Epiglottitis:** biologically plausible (*H. influenzae* type b), but the only evidence is indirect, and first-line agents are well established.
- **Xanthogranulomatous pyelonephritis:** plausible as an extension of the UTI indication, but management is mainly surgical and no specific evidence exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Publications for gonococcal urethritis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Single-arm open-label trial | Antimicrob Agents Chemother | Single-dose intramuscular aztreonam 2 g tested in men with *N. gonorrhoeae* as a possible repurposed regimen against ceftriaxone-resistant gonorrhea |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical efficacy study (uncontrolled) | Antimicrob Agents Chemother | Aztreonam 1 g IM vs spectinomycin 2 g IM for uncomplicated gonorrhea; no failures with either drug |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Clinical study | Genitourin Med | Single 1 g IM dose cleared infection in 61 men and 26 women at all sites except one pharynx; effective against penicillin-sensitive and resistant strains |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiologic and therapeutic study | Hinyokika Kiyo | Epidemiologic study of gonorrheal infections plus single-dose aztreonam therapy |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | In vitro / clinical susceptibility study | J Infect Dis | Aztreonam was effective against penicillin-resistant gonococci |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Resistance surveillance | J Infect Chemother | Reported emergence of cephem- and aztreonam-high-resistant non-beta-lactamase-producing *N. gonorrhoeae* |

Indirect evidence for other predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/) | 1986 | Pediatric case series | Am J Dis Child | Open trial in 59 children with serious gram-negative infections, including one epiglottitis case (indirect evidence for epiglottitis) |
| [4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/) | 1985 | Clinical study | Jpn J Antibiot | Aztreonam in 109 patients with infections accompanying hematologic disorders; effective rate 51.1% (supports treating infections only, not monoclonal gammopathy itself) |
| [34956120](https://pubmed.ncbi.nlm.nih.gov/34956120/) | 2021 | Microbiology / genomic study | Front Microbiol | NDM-1 and mcr-9 co-occurrence in a carbapenem-resistant *K. pneumoniae* isolate; off-topic for blood group incompatibility |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050580 (cancelled) | AZACTAM | Injection, powder, for solution | Not available |
| ANDA206517 (cancelled) | Aztreonam (Hospira, Inc.) | Injection, powder, lyophilized, for solution | Not available |
| ANDA065439 (cancelled) | Aztreonam (Fresenius Kabi USA, LLC) | Injection, powder, lyophilized, for solution | Not available |

All three US authorizations are valid, and only injectable forms are listed.

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, bronchial disease.
- **Drug Interactions:** 27 interactions were identified. Those rated **Moderate** are picosulfuric acid, dicoumarol and warfarin (anticoagulant effect should be monitored). Others, such as vancomycin, amikacin, amphotericin B, tacrolimus, heparin, acetylsalicylic acid, metronidazole, fluconazole, acyclovir and morphine, have no severity rating.

Please refer to the package insert for key warnings and formal contraindications, which are not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-scoring predictions have no mechanistic or clinical support and appear to be model artifacts. Gonococcal urethritis is the only plausible candidate (L3, with historical studies and a 2020 single-arm trial). It lacks randomized evidence, resistance has been reported, and current guidelines favor other agents, so it is best treated as a research question rather than a development candidate.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Randomized, controlled evidence for aztreonam in gonorrhea, including pharyngeal and rectal sites
- Current resistance surveillance data for *N. gonorrhoeae*
- Positioning against current guideline regimens (resistant strains, beta-lactam allergy)
- Assessment of route compatibility and the commercial pathway, since only injectable forms exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


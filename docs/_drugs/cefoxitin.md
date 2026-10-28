---
layout: default
title: Cefoxitin
parent: Model Prediction Only (L5)
nav_order: 505
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Cefoxitin: predicted new indication Infectious otitis media (evidence level L5). Approved use: Bacterial infections (streptococcal and staphylococcal infections…"
monitor_inn: "CEFOXITIN"
predicted_indications: ["infectious otitis media", "urinary tract infection (disease)", "chronic otitis media", "suppurative otitis media", "middle ear disease", "Ureaplasma urethritis", "toxocariasis", "otosalpingitis", "non-suppurative otitis media"]
---

# Cefoxitin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Cefoxitin: From Bacterial Infections to Infectious Otitis Media
{: .text-alpha }

## One-Sentence Summary

Cefoxitin is a second-generation cephamycin antibiotic, originally used for bacterial infections such as pneumonia, peritonitis, gonorrhea and endometritis.
The TxGNN model predicts it may be effective for **urinary tract infection (UTI)**, which is its top-ranked prediction with clinical or literature support.
Currently **1 clinical trial** (terminated after 6 patients) and **20 publications** support this direction, mostly older or observational studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal and staphylococcal infections, bacterial pneumonia, peritonitis, gonorrhea, endometritis, etc.) |
| Predicted New Indication | Urinary tract infection (the rank 1 prediction, infectious otitis media, has no supporting trials and only one unsupportive review) |
| TxGNN Prediction Score | 0.9926 (UTI); rank 1 infectious otitis media scored 0.9930 |
| Evidence Level | L5 (UTI) |
| US Market Status | Marketed (valid licenses: 6 of 6) |
| Number of NDAs | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cefoxitin is a cephamycin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It is stable against many beta-lactamases, including some extended-spectrum beta-lactamases (ESBLs), and covers common uropathogens such as *E. coli* and *Klebsiella*. Formal mechanism-of-action data were not available in the data compiled for this report, so this description is based on the drug's known class properties.

UTI lies within cefoxitin's established antibacterial spectrum, so this is closer to an extended or on-label use than true repurposing. Historical clinical studies from 1978-1979 report use in complicated UTI, and a murine model suggests cefoxitin may be an alternative to carbapenems for UTI caused by ESBL-producing *E. coli*. The evidence is largely old, uncontrolled or preclinical.

Other top-ranked predictions are weaker:
- **Otitis media variants** (infectious, chronic, suppurative, non-suppurative, middle ear disease, otosalpingitis): only susceptibility surveys, with signs that AmpC-mediated resistance may limit cefoxitin use. The MRSA review linked to infectious otitis media does not support efficacy, since MRSA is generally cefoxitin-resistant.
- **Gonococcal urethritis**: the best-supported by older studies, but gonorrhea is already among the original indications, and ceftriaxone is now the standard of care.
- **Ureaplasma urethritis and toxocariasis**: biologically implausible. Ureaplasma has no cell wall, and toxocariasis is a helminth infection. These are model predictions without support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02474706](https://clinicaltrials.gov/study/NCT02474706) | Phase 4 | Terminated | 6 | Non-inferiority of cefoxitin vs imipenem/cilastatin for UTI caused by ESBL-producing *E. coli*. Terminated after only 6 patients, so it cannot support a conclusion. |

No clinical trials are registered for the other predicted indications.

---

## Literature Evidence

Selected publications for UTI:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [357399](https://pubmed.ncbi.nlm.nih.gov/357399/) | 1978 | Clinical study | J Antimicrob Chemother | Cefoxitin sodium in complicated UTI |
| [400934](https://pubmed.ncbi.nlm.nih.gov/400934/) | 1979 | Clinical study | Rev Infect Dis | Intramuscular cefoxitin in 102 patients with mild to moderate infections; high cure or improvement rates |
| [400937](https://pubmed.ncbi.nlm.nih.gov/400937/) | 1979 | Review | Rev Infect Dis | US clinical overview: 69% cured and 92% cured or improved among 657 evaluable patients |
| [22214774](https://pubmed.ncbi.nlm.nih.gov/22214774/) | 2012 | Preclinical (murine) | Antimicrob Agents Chemother | Cefoxitin as an alternative to carbapenems for UTI due to CTX-M-15 ESBL *E. coli* |
| [15009360](https://pubmed.ncbi.nlm.nih.gov/15009360/) | 2004 | Review | Int J Urol | Urinary and genitourinary suppurative infections due to anaerobic bacteria |
| [40165096](https://pubmed.ncbi.nlm.nih.gov/40165096/) | 2025 | Cohort | BMC Infect Dis | Cefepime vs carbapenem for complicated UTI caused by cefoxitin-nonsusceptible organisms (indirect) |
| [37284390](https://pubmed.ncbi.nlm.nih.gov/37284390/) | 2023 | Cohort | Cureus | Multidrug-resistant UTI in chronic kidney disease patients (resistance epidemiology) |

For other predicted indications:
- **Gonococcal urethritis**: several controlled trials from 1979-1983, including [400933](https://pubmed.ncbi.nlm.nih.gov/400933/) (cefoxitin vs penicillin, 143 men; failure 1.8% vs 3.6%) and [6303490](https://pubmed.ncbi.nlm.nih.gov/6303490/) (vs ceftriaxone), plus [6658629](https://pubmed.ncbi.nlm.nih.gov/6658629/) (406 patients; failure 5.1% vs 4.3% for penicillin, no significant difference) and [3089907](https://pubmed.ncbi.nlm.nih.gov/3089907/) (96% overall cure with 1 g). These predate current resistance patterns.
- **Middle ear disease**: [7182531](https://pubmed.ncbi.nlm.nih.gov/7182531/) (1982), 11 cholesteatoma surgery patients, 72.7% cure rate; perioperative use only.
- **Chronic and suppurative otitis media**: only microbiology and susceptibility surveys, including [38156308](https://pubmed.ncbi.nlm.nih.gov/38156308/), which describes FOX-AmpC resistance.

---

## US Market Information

All six US authorizations are valid. The data compiled for this report contain no approved indication text for them.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA065415 | Cefoxitin (WG Critical Care) | Injection, powder, for solution | Valid |
| NDA065214 | Cefoxitin and Dextrose (B. Braun) | Injection, solution | Valid |
| ANDA065238 | Cefoxitin (Hikma) | Injection, powder, for solution | Valid |
| ANDA200938 | Cefoxitin (Samson Medical Technologies) | Injection, powder, for solution | Valid |
| ANDA065414 | Cefoxitin (Sagent) | Injection, powder, for solution | Valid |

A sixth authorization (ANDA065239, Hikma) is also cancelled.

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, colitis.
- **Drug Interactions**: 35 interactions were identified. Those rated **Moderate** include aminoglycosides (kanamycin, neomycin, streptomycin), picosulfuric acid and dicoumarol. Heparin is rated **Minor**. Others (e.g., vancomycin, metronidazole, omeprazole, morphine) have an unclassified severity.

Please refer to the package insert for warnings and contraindications from the label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only registered UTI trial was terminated with 6 patients, and the remaining evidence is decades-old clinical studies or preclinical data. UTI is already within cefoxitin's antibacterial spectrum, so it adds little as true repurposing. All six US authorizations are valid, and the other predictions are weak or implausible.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Contemporary comparative data against current standard-of-care agents, particularly for ESBL-producing uropathogens
- Local susceptibility and resistance data (AmpC and ESBL) for target pathogens
- Confirmation of regulatory and supply status, given that all six US licenses are valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


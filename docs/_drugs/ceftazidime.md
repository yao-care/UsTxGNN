---
layout: default
title: Ceftazidime
parent: High Evidence (L1-L2)
nav_order: 507
evidence_level: L2
indication_count: 10
monitor_inn: "CEFTAZIDIME"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "urinary tract infection (disease)", "epiglottitis", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "infectious otitis media", "Peptostreptococcus infectious disease"]
last_modified_at: 2026-10-14
description: "Ceftazidime: predicted new indication Urinary tract infection (disease) (evidence level L2). Approved use: Bacterial infections"
---

# Ceftazidime
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

## Ceftazidime: From Bacterial Infections to Urinary Tract Infection
{: .text-alpha }

## One-Sentence Summary

Ceftazidime is a third-generation cephalosporin antibiotic, originally used for bacterial infections such as pneumonia, meningitis, peritonitis and staphylococcal or streptococcal infections.
The TxGNN model predicts it may be effective for **urinary tract infection**, supported by **4 clinical trials** and **20 publications**. Most of this evidence concerns the ceftazidime-avibactam combination rather than ceftazidime alone, and UTI is closer to an existing antibacterial use than to true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal infection, bacterial pneumonia, peritonitis, bacterial meningitis, etc.; taken from the knowledge-graph indication list because no approved indication text is available for the US licenses) |
| Predicted New Indication | Urinary tract infection (disease) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L2 |
| US Market Status | Cancelled only (all 3 licenses cancelled) |
| Number of NDAs | 3 (all are ANDAs; none currently valid) |
| Recommended Decision | Proceed with Guardrails |

Note: the top two predictions by score (polyclonal hyperviscosity syndrome and hyperamylasemia) and the third (congenital analbuminemia) have no evidence and no plausible mechanism. Urinary tract infection is the highest-ranked prediction with meaningful supporting evidence, so this report focuses on it.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, ceftazidime is a broad-spectrum cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins. It is active against Gram-negative bacteria, including *Pseudomonas aeruginosa* and Enterobacterales.

Many urinary tract infections, especially complicated ones, are caused by these Gram-negative organisms. The new indication is therefore mechanistically coherent with the drug's original use against bacterial infections. This is essentially a class-consistent use rather than a true repurposing.

One caveat is that most of the available trials test ceftazidime combined with avibactam (a β-lactamase inhibitor), so the evidence applies to the combination more than to ceftazidime alone. Resistance (ESBL and carbapenemase producers) also limits how widely it can be used.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00921024](https://clinicaltrials.gov/study/NCT00921024) | Phase 2 | Completed | 129 | Randomized, double-blind comparison of IV CXA-101 versus IV ceftazidime in complicated UTI, including pyelonephritis (ceftazidime serves as comparator) |
| [NCT04882085](https://clinicaltrials.gov/study/NCT04882085) | Phase 4 | Completed | 60 | Open-label randomized study of ceftazidime-avibactam versus best available treatment for carbapenem-resistant Gram-negative infections (HAP/VAP, cUTI, cIAI, BSI) in Chinese adults |
| [NCT01430910](https://clinicaltrials.gov/study/NCT01430910) | Phase 1 | Completed | 43 | Pharmacokinetic and drug interaction study of avibactam plus ceftazidime in healthy subjects (no efficacy data) |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | Pediatric pharmacokinetics and safety program for understudied drugs (not indication-specific) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Systematic review / network meta-analysis | J Comp Eff Res | Efficacy of treatment options for complicated UTI and acute pyelonephritis, in the context of rising resistance |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrob Agents | Clinical data on novel antibiotics for multidrug-resistant Gram-negative infections, including ceftazidime-avibactam |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Review (guidance) | Int J Antimicrob Agents | Practical approach to treating multidrug-resistant Gram-negative bacilli (Italian and French societies) |
| [33618353](https://pubmed.ncbi.nlm.nih.gov/33618353/) | 2021 | Cohort | Clin Infect Dis | Retrospective multicenter study supporting ceftazidime-avibactam for KPC-producing *K. pneumoniae* infections |
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | Retrospective cohort (labeled RCT in the data) | Antimicrob Agents Chemother | Meropenem-vaborbactam versus ceftazidime-avibactam for carbapenem-resistant Enterobacteriaceae; patients with localized UTI excluded |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Review | Clin Infect Dis | Renal dose adjustment of antibiotics, including ceftazidime-avibactam, and reduced clinical response at creatinine clearance 30-50 mL/min |
| [39934901](https://pubmed.ncbi.nlm.nih.gov/39934901/) | 2025 | Systematic review / meta-analysis | Antimicrob Resist Infect Control | Global trends of ceftazidime-avibactam resistance in Gram-negative bacteria |
| [26289307](https://pubmed.ncbi.nlm.nih.gov/26289307/) | 2015 | Review | Pharmacotherapy | Overview of ceftazidime-avibactam and its activity against multidrug-resistant Gram-negative bacteria |
| [27716499](https://pubmed.ncbi.nlm.nih.gov/27716499/) | 2016 | Commentary | Cell | Ceftazidime targets penicillin-binding proteins; avibactam blocks β-lactamases that would inactivate it |
| [30224941](https://pubmed.ncbi.nlm.nih.gov/30224941/) | 2018 | Observational | Can J Infect Dis Med Microbiol | Catheter-associated UTI and biofilm-producing uropathogens |

Most of these publications concern the ceftazidime-avibactam combination or related antibiotics, not ceftazidime alone.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA064032 | TAZICEF (Hospira) | Injection, powder, for solution | Not available (status: cancelled) |
| ANDA062640 | Ceftazidime (WG Critical Care) | Injection, powder, for solution | Not available (status: cancelled) |
| ANDA062662 | TAZICEF (Hospira) | Injection, powder, for solution | Not available (status: cancelled) |

All three licenses are cancelled, so there is currently no valid single-agent ceftazidime product in the data compiled for this report.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, pyoureter, liver disease, gallbladder disease, blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions**: 100 interactions were found. The main moderate-level ones are:
  - Amphotericin B (including cholesteryl sulfate, lipid complex and liposomal forms)
  - Aminoglycosides: kanamycin, neomycin, streptomycin
  - Picosulfuric acid

  Interactions with other drugs, such as pantoprazole, omeprazole, vancomycin and metformin, are of unknown severity.
- **Clinical guardrails from the literature**: renal dose adjustment matters, and reduced clinical response has been reported at creatinine clearance of 30-50 mL/min.

For label warnings and contraindications, please refer to the package insert. This information was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Urinary tract infection is mechanistically consistent with ceftazidime's Gram-negative activity, and a completed Phase 2 randomized trial supports L2 evidence. However, that trial uses ceftazidime as a comparator, and most other evidence concerns the avibactam combination, so the support for ceftazidime alone is indirect.

**To proceed, the following is needed:**
- Confirm the exact regimens in NCT00921024 and NCT04882085 (ceftazidime alone versus the avibactam combination)
- Obtain the package insert warnings and contraindications
- Obtain mechanism of action data
- Susceptibility confirmation before use, with renal dose adjustment and attention to ESBL and carbapenemase-producing organisms
- A review of regulatory status, since all US single-agent licenses are cancelled

**Other predictions (not recommended to advance now):** Chronic suppurative otitis media (labeled "infectious otitis media"; L3, research question) has older small pediatric studies of ceftazidime but is burdensome compared with topical therapy. Epiglottitis (L4, research question) has only case reports. The remaining predictions are on hold. Ureaplasma urethritis is mechanistically contradicted because the organism has no cell wall. The other predictions have no supporting evidence or only unrelated publications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


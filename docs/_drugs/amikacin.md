---
layout: default
title: Amikacin
parent: Model Prediction Only (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
monitor_inn: "AMIKACIN"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "meningococcemia"]
last_modified_at: 2026-10-27
description: "Amikacin: predicted new indication paratyphoid fever (evidence level L5). Approved use: Not recorded in the local data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Amikacin: aminoglycoside antibacterial → paratyphoid fever
{: .text-alpha }

## One-Sentence Summary

Amikacin is an injectable aminoglycoside antibiotic used against serious gram-negative bacterial infections.
The TxGNN model predicts it may be effective for **paratyphoid fever**, with a score of 0.9982.
No clinical trials are registered for this prediction, and the 8 publications compiled for this report are mostly epidemiology and antibiogram reports rather than studies of amikacin treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | paratyphoid fever |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 6 of 6) |
| Number of NDAs | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Amikacin belongs to the aminoglycoside class, which is active against gram-negative Enterobacterales, including Salmonella species, so activity against the organisms that cause paratyphoid fever is plausible in the laboratory.

There are important limits to this link. Aminoglycosides penetrate cells poorly, and Salmonella persists inside macrophages, so they are not considered clinically effective for enteric fever. Guideline-preferred agents are fluoroquinolones, azithromycin and third-generation cephalosporins.

The retrieved literature is largely descriptive: surveillance of Salmonella occurrence, antibiograms and case series. One case report describes a child with acalculous cholecystitis due to *Salmonella paratyphi* B who was treated with a combination including amikacin (PMID 10505326), but this is a single combination-therapy case and cannot show amikacin's own effect. None of the cited studies tests amikacin as a treatment for paratyphoid fever itself, so the prediction stays at the model-only level (L5).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case report | Pediatric Hematology and Oncology | Child with leukemia and *S. paratyphi* B acalculous cholecystitis recovered on cefepime, amikacin and granulocyte support |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Case series | Mikrobiyoloji Bülteni | 48 children with paratyphi B infection resistant to classical therapy; antibiotic choices and antibiogram results reported |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Cohort | Medical Journal, Armed Forces India | In-vitro susceptibility of typhi and paratyphi A isolates from 45 enteric fever cases; chloramphenicol sensitivity re-emerging |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Cohort | Journal of the Indian Medical Association | 145 children with culture-positive enteric fever; clinical profile and antibiotic sensitivity of typhi and paratyphi |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Cohort | JNMA | Blood culture isolates and antibiogram in a teaching hospital |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Epidemiology | Pakistan Journal of Biological Sciences | Isolation and identification of *S. paratyphi* from enteric fever patients in Quetta |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Epidemiology | The New Microbiologica | Occurrence of *S. typhi* and *S. paratyphi* in Jordan, 1988–2000 |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Case series | Journal of Pediatric Surgery | Four children with splenic abscess managed with needle drainage and antibiotics |

## US Market Information

The licence records compiled for this report list injectable and suspension products, including amikacin sulfate injections and ARIKAYCE (a suspension). The records carry no indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA063315 | Amikacin Sulfate | Injection | Not recorded |
| ANDA204040 | Amikacin Sulfate | Injection, solution | Not recorded |
| ANDA218146 | Amikacin Sulfate | Injection, solution | Not recorded |
| ANDA203323 | Amikacin Sulfate | Injection, solution | Not recorded |
| ANDA205604 | Amikacin Sulfate | Injection, solution | Not recorded |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report; please refer to the package insert.

- **Drug Interactions**: Interaction screening returned 100 records. Major-level interactions include **magnesium sulfate** and **mannitol**. Moderate-level interactions include other aminoglycosides (kanamycin, neomycin), amphotericin B products, proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, pantoprazole, rabeprazole, dexlansoprazole), acetylsalicylic acid, mesalazine and related drugs, and exenatide.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and plausible in-vitro activity only. No study directly tests amikacin for paratyphoid fever, and aminoglycosides are not effective clinically for enteric fever because Salmonella survives inside cells. Established alternatives are available.

**To proceed, the following is needed:**
- Clinical or well-designed preclinical data on amikacin for paratyphoid fever, including intracellular activity against *Salmonella*
- Mechanism of action data
- Package insert warnings and contraindications
- A comparison against guideline-recommended agents (fluoroquinolones, azithromycin, third-generation cephalosporins)
- A renal and ototoxicity monitoring plan for a systemic aminoglycoside
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


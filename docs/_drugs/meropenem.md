---
layout: default
title: Meropenem
parent: Model Prediction Only (L5)
nav_order: 903
evidence_level: L5
indication_count: 10
---

# Meropenem
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

# Meropenem: From Broad-Spectrum Carbapenem Antibiotic to Bacterial Arthritis

## One-Sentence Summary

Meropenem is a broad-spectrum carbapenem antibiotic that is already marketed in the United States as injectable generics.
The TxGNN model predicts it may be effective for **bacterial arthritis** (score 99.92%).
Support is weak: **1 registered trial** (not about meropenem or arthritis) and **about 20 publications**, mostly case reports, retrospective series and in vitro studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Bacterial arthritis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (preclinical, in vitro and case-level evidence; no controlled trials) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the sampled records are ANDAs, i.e., generics) |
| Recommended Decision | Hold |

The approved indication text was empty in the supplied US license records, so the original label indication is not shown here.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. Meropenem is a carbapenem that inhibits penicillin-binding proteins and blocks bacterial cell wall synthesis. It is active against many gram-negative and anaerobic bacteria.

Bacterial arthritis (septic arthritis and related osteoarticular infection) is a bacterial infection, so an antibiotic with this spectrum is plausible. The supporting reports concern hard-to-treat or resistant pathogens:
- *Burkholderia pseudomallei* (melioidosis)
- ESBL-producing *Klebsiella pneumoniae*

In a retrospective series of 22 musculoskeletal melioidosis cases, all isolates were susceptible to meropenem. Two immunocompromised adults with ESBL *K. pneumoniae* septic arthritis were treated successfully with meropenem plus amikacin and early arthroscopic washout.

The evidence has clear limits:
- Bone and joint penetration of meropenem is not established by the supplied data.
- The supporting reports are case-level or retrospective, so they cannot show that meropenem works better than existing options.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Phase 3 | Completed | 624 | Levofloxacin prophylaxis against bacteremia in children with acute leukemia or undergoing stem cell transplant. It does not involve meropenem or arthritis, so it provides no direct support. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | Off-label use versus formal recommendations of antibiotics for multidrug-resistant bacterial infections |
| [36678359](https://pubmed.ncbi.nlm.nih.gov/36678359/) | 2022 | Review | Pathogens | Antibiotic and phage therapy options for melioidosis, which can present with septic arthritis |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Cohort (retrospective) | Le Infezioni in Medicina | Characteristics of patients with osteoarticular melioidosis |
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Retrospective review | Indian J Med Microbiol | 22 musculoskeletal melioidosis cases (osteomyelitis, septic arthritis); all isolates susceptible to meropenem |
| [17433752](https://pubmed.ncbi.nlm.nih.gov/17433752/) | 2007 | Case report | Joint Bone Spine | Two cases of ESBL *K. pneumoniae* septic arthritis treated successfully with meropenem plus amikacin and arthroscopic washout |
| [39380073](https://pubmed.ncbi.nlm.nih.gov/39380073/) | 2024 | Case report | J Med Case Rep | Disseminated melioidosis with septic arthritis, initially misdiagnosed |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | In vitro study | J Bone Joint Surg Am | Thermal stability and elution of meropenem and other antibiotics from PMMA bone cement, relevant to orthopaedic infection |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Observational | Clin Lab | Pathogen distribution and antimicrobial resistance in bone and joint infections in children under four |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Observational | Eur J Orthop Surg Traumatol | Antibiogram for empiric antibiotic choice in orthopaedic infections, including septic arthritis |
| [38139869](https://pubmed.ncbi.nlm.nih.gov/38139869/) | 2023 | Case report | Pharmaceuticals | Septic arthritis of the hip treated with linezolid, not meropenem; shown as context only |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA091404 | Meropenem | Injection, powder, for solution | Fresenius Kabi USA, LLC; Hospira, Inc. (listed twice) |
| ANDA216424 | Meropenem | Injection, powder, for solution | Sagent Pharmaceuticals |
| ANDA206086 | Meropenem | Injection | Civica, Inc |

The source data provide 20 licenses in total, and only 5 records were supplied. All supplied products are injectables, so route compatibility with an intravenous bone and joint infection regimen is plausible but was not assessed in the data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the support is only in vitro data, case reports and retrospective series. The only registered trial is unrelated to meropenem or arthritis. Bone and joint penetration is not established, and the safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Confirmation of the US label indications for meropenem, to check whether bone and joint infection is already covered or is truly new
- Bone and joint tissue penetration and pharmacokinetic data for meropenem
- Comparative or controlled clinical data against standard septic arthritis regimens, especially for resistant pathogens such as ESBL-producing Enterobacterales and *B. pseudomallei*

**Other predictions:** Among the other nine predictions, only urinary tract infection has strong trial support (Level L1). It comes from Phase 3 trials in which meropenem was mainly the comparator, so its status as a new use needs checking against the label.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Ertapenem
parent: Moderate Evidence (L3-L4)
nav_order: 668
evidence_level: L4
indication_count: 2
---

# Ertapenem
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Ertapenem: From Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Ertapenem is a broad-spectrum carbapenem antibiotic given by injection and marketed in the United States.
The TxGNN model predicts it may be effective for **bacterial arthritis**, but **no clinical trials** are registered for this indication.
The **10 retrieved publications** are mostly case reports and small cohorts, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in the input data (ertapenem is a carbapenem antibacterial) |
| Predicted New Indication | Bacterial arthritis |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the input. Ertapenem is a carbapenem, and this class is generally active against many Enterobacterales, including ESBL producers, and against anaerobes. These are the organisms reported in the retrieved case reports of septic arthritis and bone/joint infection, such as *Klebsiella pneumoniae*, *Prevotella bivia* and *Clostridium paraputrificum*.

Bacterial arthritis is an infection, so an antibiotic that covers the causative organisms is a plausible fit. Once-daily dosing also suits outpatient parenteral antimicrobial therapy (OPAT), and one long-term OPAT safety cohort exists, in which bone and joint infections were among the indications.

The high TxGNN score is a graph-based prediction. The retrieved literature contains no controlled comparison in bacterial arthritis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Cohort | Antimicrob Agents Chemother | Retrospective study of 306 patients on outpatient ertapenem. Indications included intra-abdominal infection, pneumonia and bone/joint infection. Provides long-term safety and efficacy data. |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Case report | J Chemother | *Klebsiella pneumoniae* septic wrist arthritis treated successfully with ertapenem plus levofloxacin. |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Case report | BMJ Case Rep | *Citrobacter koseri* osteomyelitis with septic arthritis in a diabetic foot, alongside gout, treated successfully with ertapenem. |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Cohort | J Antimicrob Chemother | Ten patients received off-label subcutaneous β-lactam suppressive therapy for bone and joint infections when optimal surgery was not feasible. |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | Cohort | J Antimicrob Chemother | Temocillin was evaluated as an alternative to carbapenems for bone and joint infections caused by third-generation cephalosporin-resistant Enterobacterales. These infections are hard to treat, and treatment often relies on carbapenems. |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohort | Clin Lab | Pathogen distribution and antimicrobial resistance in bone and joint infections in children under four years old. |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Case report/Review | Anaerobe | First reported case of *Clostridium paraputrificum* septic arthritis and osteomyelitis of the shoulder, with a literature review. |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Case report/Review | J Investig Med High Impact Case Rep | *Prevotella bivia* septic arthritis in an immunocompetent adult, with a literature review. |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro study | Diagn Microbiol Infect Dis | Auranofin restored ertapenem susceptibility in carbapenem-resistant *E. coli*. This is laboratory evidence only. |
| [29183082](https://pubmed.ncbi.nlm.nih.gov/29183082/) | 2017 | Review | JAMA | Review of hidradenitis suppurativa. It has low relevance to bacterial arthritis. |

## US Market Information

The input does not include approved-indication text for these authorizations, so that column is omitted. Only 5 of the 17 authorizations are listed. ANDA218067 appears three times with different manufacturers.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021337 | INVANZ | Lyophilized powder for injection | Merck Sharp & Dohme LLC |
| ANDA218067 | Ertapenem | Lyophilized powder for injection | Qilu Antibiotics Pharmaceutical Co., Ltd. |
| ANDA218067 | Ertapenem | Lyophilized powder for injection | Hikma Pharmaceuticals USA Inc. |
| ANDA208790 | Ertapenem | Lyophilized powder for injection | Fresenius Kabi USA, LLC |
| ANDA218067 | Ertapenem | Lyophilized powder for injection | Sagent Pharmaceuticals |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no registered trials and no controlled comparison in bacterial arthritis. The supporting evidence is limited to case reports and small cohorts. Ertapenem is already marketed, so the safety profile is established, but its benefit in this indication is unproven.

For reference, the second prediction, *Staphylococcus aureus* infection, has a stronger signal (Evidence Level L3). It rests on cefazolin plus ertapenem for persistent MSSA bacteremia, and a Phase 2 RCT (NCT04886284) is recruiting. It is worth tracking separately.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications, which are currently missing and block the safety screening
- Mechanism of action data from DrugBank
- Comparative data or a prospective study of ertapenem in bacterial arthritis (septic arthritis), with a bone/joint penetration and PK/PD assessment
- Pathogen-specific analysis, since ertapenem has limited coverage of *Pseudomonas* and enterococci

*This report is for research reference only and does not constitute medical advice. Predicted candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Daptomycin
parent: Moderate Evidence (L3-L4)
nav_order: 570
evidence_level: L4
indication_count: 10
---

# Daptomycin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Daptomycin is an intravenous cyclic lipopeptide antibiotic used against Gram-positive bacterial infections such as skin infections, bacteremia and right-sided endocarditis.
The TxGNN model predicts it may be effective for **osteoarthritis**, but there are **0 clinical trials** and only **9 publications**, all on bone and joint infections rather than degenerative osteoarthritis.
The high score most likely reflects knowledge-graph proximity to "osteoarticular" terms, not a real anti-osteoarthritis effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (NDA/ANDA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Daptomycin is a cyclic lipopeptide that depolarizes the membranes of Gram-positive bacteria. Detailed mechanism-of-action data is not available in the Evidence Pack.

The relationship between the original and predicted indication is weak. Osteoarthritis is a degenerative disease driven by cartilage breakdown and low-grade joint inflammation, and daptomycin's antibacterial action has no known link to it.

All retrieved papers concern **bone and joint infections**, such as prosthetic joint infection and septic arthritis, treated with daptomycin. That is a different disease from degenerative osteoarthritis. The prediction most likely comes from term proximity in the knowledge graph rather than from a genuine therapeutic signal.

Among the other predictions, **rheumatoid arthritis** (rank 2) has the only preclinical signal. A 2025 study (PMID 39571268) reported that daptomycin reduced collagen-induced arthritis in mice via suppression of inflammatory cytokines and NF-κB signaling. There is no human data, and this is a separate research question from osteoarthritis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | Int Orthop | Safety and efficacy of high-dose daptomycin plus rifampicin in Gram-positive osteoarticular **infections** |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Clinical efficacy and safety of daptomycin in hip and knee periprosthetic joint **infections** |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) in complicated bone and joint and implant-associated **infections** (no abstract available) |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Daptomycin vs standard therapy for osteoarticular infections associated with *S. aureus* bacteremia |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Cohort (registry) | Med Clin (Barc) | Spanish data from the EU-CORE registry of routine daptomycin use in Gram-positive infections |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Survey | Int J Antimicrob Agents | Survey of current prosthetic joint infection management among infectious disease physicians |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Cohort | Surg Infect | Ten-year evolution of staphylococcal profiles in osteoarticular infections |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiot | Antibiotic susceptibility of *S. aureus* and *S. epidermidis* from prosthetic joint infections |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case report | Case Rep Orthop | Chronic *Corynebacterium striatum* septic arthritis in a patient with osteoarthritis referred for knee arthroplasty |

None of these studies tests daptomycin as a treatment for degenerative osteoarthritis. The 2020 case report only mentions osteoarthritis as the patient's background diagnosis.

---

## US Market Information

The Evidence Pack lists 20 authorizations in total. The first five are shown below. Approved indication text is not included in the records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA217215 | Daptomycin | Lyophilized powder for injection (solution) | Biocon Pharma Inc. |
| NDA217415 | Daptomycin | Lyophilized powder for injection (solution) | Xellia Pharmaceuticals USA LLC |
| ANDA207104 | Daptomycin | Lyophilized powder for injection (solution) | Sagent Pharmaceuticals |
| ANDA216445 | Daptomycin | Lyophilized powder for injection (solution) | NorthStar Rx LLC |
| ANDA208375 | Daptomycin | Lyophilized powder for injection (solution) | BluePoint Laboratories |

All available forms are injectable: lyophilized powder for solution or suspension, and ready-to-use solution.

---

## Safety Considerations

Please refer to the package insert for safety information.

- **Adverse-event signal**: One case report (PMID 36693494) describes daptomycin-induced rhabdomyolysis followed by acute gouty arthritis. Muscle injury is a known concern with this drug.
- **Practical constraint**: IV-only dosing is a poor fit for a chronic condition like osteoarthritis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, and the literature covers joint infections rather than osteoarthritis. The high TxGNN score is likely an artifact of term proximity, so the osteoarthritis prediction lacks a mechanistic basis.

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Preclinical evidence of daptomycin activity in degenerative osteoarthritis models, if the direction is pursued at all
- Consideration of redirecting the effort to the rheumatoid arthritis hypothesis (PMID 39571268), which has a preclinical signal and would need translational work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Plazomicin
parent: Model Prediction Only (L5)
nav_order: 1054
evidence_level: L5
indication_count: 7
---

# Plazomicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Plazomicin: From Complicated Urinary Tract Infection to Gonococcal Urethritis

## One-Sentence Summary

Plazomicin is an injectable aminoglycoside antibiotic marketed in the US as Zemdri, used against complicated urinary tract infections caused by resistant Gram-negative bacteria.
The TxGNN model predicts it may be effective for **gonococcal urethritis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complicated urinary tract infection, including pyelonephritis (the label text was not in the supplied data) |
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 entries (all under NDA210303, from three different manufacturers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. From general pharmacology, plazomicin is an aminoglycoside that binds the 30S ribosomal subunit and is bactericidal against Gram-negative bacteria. It is approved for resistant Enterobacterales infections of the urinary tract.

Gonococcal urethritis is a Gram-negative bacterial infection of the genitourinary tract, so a class-level link to antibacterial therapy is plausible. Another aminoglycoside, gentamicin, has been studied for gonorrhea. However, no plazomicin-specific laboratory, clinical, or literature evidence was supplied. The link is therefore plausible but unverified.

Two practical concerns remain:
- Plazomicin is IV-only and approved for a narrow indication, so its practical feasibility for a common outpatient infection is unclear.
- Route compatibility with the new indication has not been assessed.

The other six predictions from the model are weaker. Uterine inflammatory disease and xanthogranulomatous pyelonephritis have indirect links. Ureaplasma urethritis has a weak link. Hyperamylasemia, polyclonal hyperviscosity syndrome and congenital analbuminemia have no credible mechanism and are probably graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA210303 | Zemdri (plazomicin) | Injection | Achaogen, Inc. |
| NDA210303 | Zemdri (plazomicin) | Injection | Cipla Therapeutics Inc. |
| NDA210303 | Zemdri (plazomicin) | Injection | Cipla USA Inc. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.64%), but the evidence level is L5. No trials, no literature and no mechanism data support plazomicin for gonococcal urethritis, and the IV-only formulation makes practical use doubtful.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- In vitro susceptibility data for plazomicin against *Neisseria gonorrhoeae*
- A comparison with current standard gonorrhea therapy and a route-of-administration feasibility assessment
- A literature and trial search specific to plazomicin and gonorrhea
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


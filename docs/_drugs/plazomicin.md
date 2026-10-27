---
layout: default
title: Plazomicin
parent: Model Prediction Only (L5)
nav_order: 1054
evidence_level: L5
indication_count: 7
monitor_inn: "PLAZOMICIN"
predicted_indications: ["gonococcal urethritis", "Ureaplasma urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
last_modified_at: 2026-10-14
description: "Plazomicin: predicted new indication Gonococcal urethritis (evidence level L5). Approved use: Urinary tract infection"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Plazomicin: From Urinary Tract Infection to Gonococcal Urethritis
{: .text-alpha }

## One-Sentence Summary

Plazomicin is an aminoglycoside antibiotic, originally used to treat urinary tract infections.
The TxGNN model predicts it may be effective for **gonococcal urethritis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection |
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, plazomicin belongs to the aminoglycoside class, which acts against many Gram-negative bacteria, including Enterobacterales. Its efficacy in urinary tract infection is the basis of its original use.

*Neisseria gonorrhoeae* is also a Gram-negative pathogen, and other aminoglycosides (e.g., gentamicin) have been used in gonorrhea treatment. This gives the prediction a plausible antibacterial link. However, plazomicin has not been established for gonococcal infection, and current standard-of-care options are well defined. The high score (0.996) is a computational output only, and the US marketing authorization is cancelled, which further limits practical feasibility.

Other predicted indications are weaker still. The closest to the approved use is xanthogranulomatous pyelonephritis (a Gram-negative-associated condition usually managed surgically, with antibiotics as an adjunct). Ureaplasma urethritis is unlikely to respond because Ureaplasma lacks a cell wall and aminoglycosides are not reliable against it. Hyperamylasemia, polyclonal hyperviscosity syndrome and congenital analbuminemia have no plausible antibacterial mechanism and are likely graph-based artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210303 | Zemdri (plazomicin) (Achaogen, Inc.; status: cancelled) | Injection | Not specified |

## Safety Considerations

- **Drug Interactions**: 70 interactions were identified in total. Those listed below are from the first 20 records reviewed.
  - **Major**: Magnesium sulfate, Mannitol
  - **Moderate**: Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), other aminoglycosides and related antibiotics (kanamycin, neomycin, neomycin topical, vancomycin), proton pump inhibitors (rabeprazole, omeprazole, lansoprazole, dexlansoprazole, pantoprazole), aminosalicylates (mesalazine, balsalazide, olsalazine), acetylsalicylic acid, picosulfuric acid
- **Class considerations**: Aminoglycoside nephrotoxicity and ototoxicity are class concerns. The interaction list above is consistent with this (combinations with other nephrotoxic or ototoxic agents). Please refer to the package insert for full safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (evidence level L5). Although there is a plausible antibacterial link for gonococcal urethritis, standard-of-care options are well established, and the product's US authorization is cancelled. The remaining predicted indications lack a credible mechanism.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (required before any safety screening)
- Mechanism of action data
- In vitro susceptibility data for *N. gonorrhoeae* and comparison with current standard-of-care agents
- Any clinical or observational evidence in gonococcal urethritis
- Assessment of the feasibility of reintroducing or re-licensing the product, given the cancelled US status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


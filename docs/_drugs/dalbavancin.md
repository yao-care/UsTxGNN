---
layout: default
title: Dalbavancin
parent: Model Prediction Only (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
monitor_inn: "DALBAVANCIN"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "otitis externa", "ophthalmic herpes zoster", "infectious mononucleosis", "orbital cellulitis"]
last_modified_at: 2026-10-30
description: "Dalbavancin: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Dalbavancin
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

## Dalbavancin: Postinfectious vasculitis
{: .text-alpha }

## One-Sentence Summary

Dalbavancin is a lipoglycopeptide antibiotic, originally used to treat skin disease caused by infection.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**,
but currently **0 clinical trials** and **0 publications** support this direction, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 4 of 4) |
| Number of FDA Applications | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dalbavancin is a lipoglycopeptide antibiotic active against Gram-positive bacteria, and it is used for infections of the skin and skin structures.

Postinfectious vasculitis is typically an immune-mediated process that follows an infection, not an active bacterial infection. Direct antibacterial activity therefore has no clear role, and the mechanistic link is speculative. The very high score (0.9976) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other predictions reviewed (all L5, no trials or literature):**

| Rank | Predicted Indication | Score | Assessment |
|---|------|------|------|
| 2 | Post-bacterial disorder | 0.9976 | Non-specific category; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |
| 3 | Post-infectious syndrome | 0.9976 | Immune-driven after pathogen clearance; no clear rationale |
| 4 | Infective urethral stricture | 0.9974 | Fibrotic complication; an antibiotic would not reverse it |
| 5 | Chagas cardiomyopathy | 0.9972 | Caused by a protozoan; weak rationale |
| 6 | Infection-related hemolytic uremic syndrome | 0.9972 | Mostly Gram-negative E. coli; antibiotics are generally avoided in STEC-HUS |
| 7 | Otitis externa | 0.9970 | Plausible only for staphylococcal cases; usually treated topically |
| 8 | Ophthalmic herpes zoster | 0.9925 | Viral; no mechanistic basis |
| 9 | Infectious mononucleosis | 0.9916 | Viral; no mechanistic basis |
| 10 | Orbital cellulitis | 0.9902 | Most plausible: Staphylococcus aureus (including MRSA) and Streptococcus fall within its spectrum, and it is related to the approved skin infection indication. Orbital tissue penetration is unknown. Flagged as a research question |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA217591 | Dalbavancin Hydrochloride (Fresenius Kabi USA, LLC) | Injection, powder, for solution | Not available (valid) |
| NDA021883 | Dalvance (Allergan, Inc.) | Injection, powder, for solution | Not available (valid) |
| ANDA219465 | Dalbavancin (Teva Pharmaceuticals, Inc.) | Injection, powder, for solution | Not available (valid) |
| ANDA218929 | Dalbavancin (Meitheal Pharmaceuticals Inc) | Injection, powder, lyophilized, for solution | Not available (valid) |

## Safety Considerations

- **Drug Interactions**: Three moderate-level interactions were identified:
  - Picosulfuric acid
  - Ethinylestradiol
  - Mycophenolic acid

Please refer to the package insert for warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the mechanistic link is speculative because postinfectious vasculitis is immune-mediated rather than an active bacterial infection. The US license records are all cancelled, and the package insert safety data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Clarification of current US market and license status
- Preclinical or case-level evidence for any candidate indication; orbital cellulitis is the most biologically plausible one to examine first, including orbital tissue penetration data
- Route compatibility assessment (the drug is available only as an injectable)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


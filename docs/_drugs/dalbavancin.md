---
layout: default
title: Dalbavancin
parent: Model Prediction Only (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Dalbavancin: From Skin Infection to Postinfectious Vasculitis

## One-Sentence Summary

Dalbavancin is a lipoglycopeptide antibiotic, originally used to treat skin disease caused by infection.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**,
but currently **0 clinical trials** and **0 publications** support this direction, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Skin disease caused by infection (from the knowledge graph; no approved indication text is available in the license records) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 license records (1 NDA, 3 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dalbavancin is a lipoglycopeptide antibiotic active against Gram-positive bacteria, and it is used for infections of the skin and skin structures.

Postinfectious vasculitis is typically an immune-mediated process that follows an infection, not an active bacterial infection. Direct antibacterial activity therefore has no clear role, and the mechanistic link is speculative. The very high score (0.998) reflects proximity to infection-related nodes in the knowledge graph, not a demonstrated biological rationale.

**Other predictions reviewed (all L5, no trials or literature):**

| Rank | Predicted Indication | Score | Assessment |
|---|------|------|------|
| 2 | Post-bacterial disorder | 99.76% | Non-specific category; likely graph proximity only |
| 3 | Post-infectious syndrome | 99.76% | Immune-driven after pathogen clearance; no clear rationale |
| 4 | Infective urethral stricture | 99.74% | Fibrotic complication; an antibiotic would not reverse it |
| 5 | Chagas cardiomyopathy | 99.72% | Caused by a protozoan; weak rationale |
| 6 | Infection-related hemolytic uremic syndrome | 99.72% | Mostly Gram-negative E. coli; antibiotics are generally avoided in STEC-HUS |
| 7 | Otitis externa | 99.70% | Plausible only for staphylococcal cases; usually treated topically |
| 8 | Ophthalmic herpes zoster | 99.25% | Viral; no mechanistic basis |
| 9 | Infectious mononucleosis | 99.16% | Viral; no mechanistic basis |
| 10 | Orbital cellulitis | 99.02% | Most plausible: Staphylococcus aureus (including MRSA) and Streptococcus fall within its spectrum, and it is related to the approved skin infection indication. Orbital tissue penetration is unknown. Flagged as a research question |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA217591 | Dalbavancin Hydrochloride (Fresenius Kabi USA, LLC) | Injection, powder, for solution | Not available (cancelled) |
| NDA021883 | Dalvance (Allergan, Inc.) | Injection, powder, for solution | Not available (cancelled) |
| ANDA219465 | Dalbavancin (Teva Pharmaceuticals, Inc.) | Injection, powder, for solution | Not available (cancelled) |
| ANDA218929 | Dalbavancin (Meitheal Pharmaceuticals Inc) | Injection, powder, lyophilized, for solution | Not available (cancelled) |

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


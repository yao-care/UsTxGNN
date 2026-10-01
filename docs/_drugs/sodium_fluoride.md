---
layout: default
title: Sodium Fluoride
parent: Model Prediction Only (L5)
nav_order: 1170
evidence_level: L5
indication_count: 7
---

# Sodium Fluoride
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

# Sodium Fluoride: Predicted Repurposing to Epiglottitis

## One-Sentence Summary

Sodium fluoride is marketed in the US mainly as dental products such as rinses, toothpastes, gels and foams, but no approved indication text is recorded in the source data.
The TxGNN model predicts it may be effective for **epiglottitis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is recorded in the evidence pack. Fluoride is known to inhibit bacterial enolase in vitro. However, no evidence connects this to epiglottitis, which is an acute, potentially airway-threatening bacterial infection.

The high TxGNN score (99.92%) most likely reflects similarity in the knowledge graph to other infection-related nodes, not a demonstrated mechanism. The other top predictions (urinary tract infection, Ureaplasma urethritis, gonococcal urethritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis, laryngitis) are also L5 and have no supporting clinical evidence. Two of them share an identical score, which suggests a shared graph neighborhood rather than independent evidence.

The marketed forms are topical or oral dental products. Their route compatibility with treating epiglottitis has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for epiglottitis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M021 | Anticavity fluoride rinse | Mouthwash | Topco Associates LLC |
| M022 | Sensodyne Pronamel | Paste | Haleon US Holdings LLC |
| Not listed | Acclean Foam Fluoride 60 Second Application | Aerosol, foam | Henry Schein |
| M021 | Hismile | Gel | Hismile Pty Ltd |
| M021 | Burts Bees Kids | Paste, dentifrice | Procter & Gamble Manufacturing Company |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no plausible mechanistic link to epiglottitis. Safety and mechanism data are also missing, so the candidate cannot advance to safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap)
- Mechanism of action data (for example, from DrugBank)
- The original approved indication of the marketed products
- A plausible mechanistic rationale and route-compatibility assessment for epiglottitis
- Any preclinical or clinical evidence for this drug-disease pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


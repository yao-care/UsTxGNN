---
layout: default
title: Ritonavir
parent: Model Prediction Only (L5)
nav_order: 1129
evidence_level: L5
indication_count: 3
---

# Ritonavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Ritonavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Ritonavir is an HIV-1 protease inhibitor that is also widely used as a pharmacokinetic booster (a strong CYP3A4 inhibitor) in HIV regimens.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are **0 feline-specific studies** and **0 publications** behind this prediction. The only registered trial is a human HIV-1 study, so the entry looks like a species-variant echo of the existing HIV indication rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred; the license indication text in the record is empty) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only for the feline indication; the pack labels it L4) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed authorizations are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. From known pharmacology, ritonavir inhibits HIV-1 protease and strongly inhibits CYP3A4, which is why it is used to boost other protease inhibitors.

The link to feline immunodeficiency virus (FIV) rests on lentiviral similarity: FIV and HIV are both lentiviruses. The high TxGNN score most likely reflects proximity to HIV-related nodes in the knowledge graph. FIV protease differs from HIV-1 protease in substrate and inhibitor specificity, so activity against FIV cannot be assumed. Ritonavir is already a marketed HIV-1 drug, so this prediction is probably a species-variant artifact and not a new therapeutic direction.

The other predictions in the pack show the same pattern.
- **Simian immunodeficiency virus (SIV) infection** has some literature: in vitro susceptibility data (SIVmac239 inhibited by ritonavir at about 13 nM) and macaque combination-ART studies. SIV is an animal model of HIV, so this supports preclinical model use only, not a new human indication.
- **A rare neurodevelopmental disorder** has a similar score (0.999) but no trials, no literature and no plausible mechanistic link. It looks like a graph-propagation artifact.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Ritonavir-boosted darunavir + lamivudine vs boosted darunavir + tenofovir/emtricitabine or tenofovir/lamivudine in treatment-naïve HIV-1 patients. It studies human HIV-1, with ritonavir only as a booster. It gives no direct evidence for FIV or feline AIDS. |

The Phase 4 label should not be read as L1 evidence for the predicted indication.

## Literature Evidence

Currently no related literature available

## US Market Information

The approved indication text is empty in all listed records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA206614 | Ritonavir | Tablet, film coated | NuCare Pharmaceuticals, Inc. |
| ANDA202573 | Ritonavir | Tablet | Cipla USA Inc. |
| ANDA206614 | Ritonavir | Tablet, film coated | American Health Packaging |
| ANDA204587 | Ritonavir | Tablet | Camber Pharmaceuticals, Inc. |
| ANDA208890 | Ritonavir | Tablet | Amneal Pharmaceuticals LLC |

The record shows 20 authorizations in total. Dosage forms include oral tablets (film-coated and plain), powder and solution.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The feline AIDS prediction has no feline-specific trials or literature. Its high score most likely reflects the existing HIV-1 indication in the knowledge graph. FIV protease differs from HIV-1 protease, so efficacy cannot be inferred.

**To proceed, the following is needed:**
- FIV protease inhibition data for ritonavir (in vitro enzyme or cell-based susceptibility)
- Any veterinary or feline pharmacology and safety data; this is a species-specific question, and human data do not transfer directly
- The ritonavir mechanism of action from DrugBank and the package insert warnings and contraindications (both are still missing from the record)
- Confirmation of the original indication, since the license indication text is empty
- Treatment of the SIV entry as a preclinical research question, not a clinical indication, unless macaque studies confirm ritonavir was part of the tested regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


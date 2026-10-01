---
layout: default
title: Pretomanid
parent: Model Prediction Only (L5)
nav_order: 1080
evidence_level: L5
indication_count: 5
---

# Pretomanid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Pretomanid: From Drug-Resistant Tuberculosis to Candidiasis

## One-Sentence Summary

Pretomanid is an oral antibacterial used as part of the BPaL regimen (bedaquiline, pretomanid, linezolid) for extensively drug-resistant and treatment-intolerant or non-responsive multidrug-resistant pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **candidiasis** with a very high score, but there are **0 clinical trials** and **0 publications** supporting this prediction, and the known biology argues against it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Drug-resistant pulmonary tuberculosis (as part of BPaL; the license record has no indication text, so this comes from the literature) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on the pharmacology assessment, pretomanid is a nitroimidazooxazine prodrug. It is activated inside mycobacteria by the F420-dependent nitroreductase Ddn, and it acts against *Mycobacterium tuberculosis*. It is not known to have antifungal activity.

Tuberculosis is a bacterial infection and candidiasis is a fungal infection. The two diseases have different pathogens, different drug targets and different activation pathways. No plausible mechanistic link between the original indication and candidiasis was identified.

The high TxGNN score (0.997) is a graph-based prediction only. It should be treated as a hypothesis-generating signal, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212862 | Pretomanid (Viatris Specialty LLC) | Tablet (oral) | Not provided in the license record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidiasis prediction is supported only by the model score. There are no trials or publications, and no plausible antifungal mechanism, since pretomanid works through a mycobacteria-specific activation pathway. The other four predictions were also reviewed:

- **Leprosy:** it has only tangential trials (all TB-PRACTECAL sub-studies in TB populations). Direct preclinical evidence is negative, because *M. leprae* is naturally resistant to pretomanid (PMID 17005816).
- **Coronary artery disease, myocardial ischemia, and anomalous left coronary artery from the pulmonary artery:** these have no supporting evidence or mechanism.

**To proceed, the following is needed:**
- Any in vitro antifungal activity data (for example, MIC testing against *Candida* species) to establish a biological basis
- The mechanism of action record from DrugBank and the FDA package insert warnings and contraindications, which are missing from the current record
- A mechanistic rationale for why a mycobacteria-specific prodrug would act on fungi
- A safety review before any repurposing work, given the missing package insert data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


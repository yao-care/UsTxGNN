---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 1283
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Gram-Positive Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic used against serious Gram-positive bacterial infections. The Evidence Pack does not list its approved indication text, so this is based on the drug class.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but there are **0 clinical trials** and **1 unrelated case report** behind this prediction. It is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data (vancomycin is a Gram-positive antibacterial) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It probably is not. Detailed mechanism of action data is not available in the source data. Vancomycin is known to inhibit bacterial cell wall synthesis. It has no known anti-fibrotic or immunomodulatory action relevant to systemic sclerosis (diffuse scleroderma), which is a fibrotic autoimmune disease.

The source data lists no original indication, so the relationship between the original and new indication could not be cross-checked. The score of 0.999 is high, but the single retrieved paper is a case report of sepsis with erythroderma, not a scleroderma study. The score is therefore most likely a graph-topology artifact, not a biological signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | A 56-year-old man with a diffuse exfoliative rash, sepsis and eosinophilia, evaluated for erythroderma. It is not a scleroderma study and shows no vancomycin benefit for scleroderma. |

## US Market Information

The source data gives no approved-indication text for these products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA204360 | Vancomycin Hydrochloride | Injection, powder, for solution | Hikma Pharmaceuticals USA Inc. |
| ANDA204125 | Vancomycin Hydrochloride | Injection, powder, lyophilized, for solution | BluePoint Laboratories |
| ANDA206616 | Vancomycin Hydrochloride | Injection, powder, lyophilized, for solution | Hikma Pharmaceuticals USA Inc. |
| NDA050606 | Vancomycin Hydrochloride | Capsule | ANI Pharmaceuticals, Inc. |
| NDA211962 | Vancomycin | Injection, solution | Xellia Pharmaceuticals USA LLC |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no plausible mechanism, no trials and no relevant literature for diffuse scleroderma. The prediction is model-only (L5) and likely an artifact.

Among the other predictions in the pack, only streptococcal pneumonia (L4, S1) has a biologically plausible rationale. It is probably an existing use of vancomycin, not true repurposing, so it needs a label and guideline cross-check.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data and the original indication list from DrugBank
- Any preclinical or clinical signal for vancomycin in scleroderma, otherwise deprioritize this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


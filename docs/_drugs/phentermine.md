---
layout: default
title: Phentermine
parent: Model Prediction Only (L5)
nav_order: 1040
evidence_level: L5
indication_count: 4
---

# Phentermine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Phentermine: From Obesity to Hypervitaminosis

## One-Sentence Summary

Phentermine is an oral sympathomimetic appetite suppressant, generally used for weight management. The TxGNN model predicts it may be effective for **hypervitaminosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are generic ANDAs) |
| Recommended Decision | Hold |

The original indication is not stated in the US license records supplied. The "obesity" framing in the title comes from the drug's known use as an appetite suppressant.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Phentermine is known as a sympathomimetic amine that mainly releases norepinephrine, and it is used to suppress appetite. Nothing in this pharmacology relates to vitamin excess or vitamin clearance.

**No plausible mechanistic link to hypervitaminosis was identified.** Vitamin toxicity is usually managed by stopping the offending vitamin and giving supportive care, so a drug-based indication is implausible. The high score (99.57%) reflects a knowledge-graph association only, with no clinical data behind it.

The other three TxGNN predictions are also weak:

- **Proximal 16p11.2 microdeletion syndrome (99.49%):** This has a loose thematic link, because the syndrome is associated with early-onset obesity and hyperphagia. It is speculative. The syndrome also involves neurodevelopmental features (autism spectrum, seizure susceptibility, ADHD-like symptoms), where a stimulant-like agent raises safety concerns.
- **Obsolete hypertelorism (99.41%):** The ontology term is deprecated, so this is likely an artifact. It should be remapped or excluded.
- **Frontorhiny (99.04%):** This is a congenital craniofacial malformation with no plausible link to an appetite suppressant.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| ANDA205019 | Phentermine Hydrochloride | Capsule | Bryant Ranch Prepack |
| ANDA205008 | Phentermine hydrochloride | Tablet | Proficient Rx LP |
| ANDA202248 | Phentermine Hydrochloride | Capsule | Bryant Ranch Prepack |
| ANDA040887 | Phentermine Hydrochloride | Capsule | PD-Rx Pharmaceuticals, Inc. |
| ANDA203436 | Phentermine Hydrochloride | Tablet | KVK-TECH, Inc. |

These are 5 of 20 licenses. All are oral (capsule or tablet). The approved-indication text is empty in the supplied records.

---

## Safety Considerations

Please refer to the package insert for safety information. No warning, contraindication or drug interaction data were available in the source record.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no trials or literature. No plausible mechanistic link to hypervitaminosis exists, and vitamin toxicity is managed by stopping the vitamin. No further evaluation is justified at this stage.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Evidence of any biological rationale linking phentermine to vitamin excess, if one exists
- Remapping of the obsolete hypertelorism term to a current ontology term before any review of that prediction
- A dedicated pediatric and neurodevelopmental safety review before any work on the 16p11.2 microdeletion candidate

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


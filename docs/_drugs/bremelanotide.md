---
layout: default
title: Bremelanotide
parent: Model Prediction Only (L5)
nav_order: 466
evidence_level: L5
indication_count: 10
monitor_inn: "BREMELANOTIDE"
predicted_indications: ["acne (disease)", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "exocrine pancreatic insufficiency", "cauda equina syndrome", "pituitary dwarfism", "zinc, elevated plasma", "retinopathy of prematurity", "esotropia", "Beare-Stevenson cutis gyrata syndrome", "combined small cell lung carcinoma"]
last_modified_at: 2026-10-14
description: "Bremelanotide: predicted new indication Acne (evidence level L5). Approved use: Hypoactive sexual desire disorder (HSDD)"
---

# Bremelanotide
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

# Bremelanotide: From Hypoactive Sexual Desire Disorder to Acne

## One-Sentence Summary

Bremelanotide is a melanocortin receptor agonist, originally used to treat hypoactive sexual desire disorder (HSDD).
The TxGNN model predicts it may be effective for **acne**, but **no clinical trials** and **no publications** currently support this direction, so it remains a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypoactive sexual desire disorder (HSDD) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 100.00% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available for this report. From pharmacology data, bremelanotide (PT-141) is a peptide that acts on melanocortin receptors, including MC1R, MC3R, MC4R and MC5R. It is approved as a subcutaneous injection for premenopausal women with HSDD.

Melanocortin signaling, particularly through MC1R and MC5R, has been linked to skin inflammation and sebaceous gland regulation. This offers a plausible but unvalidated link to acne. The similarity between the original and predicted indications has not been assessed, since HSDD is a central nervous system-driven condition and acne is a dermatologic one.

There is also a tolerability concern: MC1R activation can cause hyperpigmentation, a known adverse effect of bremelanotide. This would matter for any dermatologic use.

Although the TxGNN score is at its maximum, no trials or literature back it up. The score should be read as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210557 (Cancelled) | Vyleesi (Cosette Pharmaceuticals, Inc.) | Injection | Not listed in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**:
  - **Naltrexone (Major)**: this is the only graded interaction identified.
  - Pharmacology data also show that bremelanotide acts on the MC1R, MC3R, MC4R and MC5R receptors. These are target activities, not interactions in the clinical sense.
- **Disease associations flagged in the knowledge graph** (not taken from label text): hypertensive disorder, hypertension, cardiovascular disease and heart disease are listed as contraindication-related conditions. This is consistent with the transient blood pressure increases known with this drug class.
- **Dermatologic tolerability**: MC1R-mediated hyperpigmentation is a known adverse effect and is relevant to any acne use.

Please refer to the package insert for complete warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction has the maximum TxGNN score but no clinical trials or literature (Evidence Level L5). The mechanistic link is only plausible, and the hyperpigmentation and cardiovascular considerations weigh against it. The only US NDA is cancelled, which further limits near-term development.

**To proceed, the following is needed:**
- Review of the FDA package insert for warnings and contraindications
- Detailed mechanism of action data for bremelanotide
- Preclinical evidence that melanocortin receptor agonism (for example MC1R or MC5R) affects sebaceous gland activity or skin inflammation in acne models
- Assessment of whether the hyperpigmentation and blood pressure effects are acceptable for an acne population
- Evaluation of route and formulation compatibility, since only an injectable form exists and a topical or other option may be needed for acne
- Clarification of the regulatory and commercial status of the cancelled NDA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


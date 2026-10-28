---
layout: default
title: Lanreotide
parent: Model Prediction Only (L5)
nav_order: 834
evidence_level: L5
indication_count: 5
monitor_inn: "LANREOTIDE"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
last_modified_at: 2026-10-28
description: "Lanreotide: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Lanreotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Lanreotide: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Lanreotide is a somatostatin analog originally used to treat acromegaly, hyperpituitarism, and pituitary gigantism.
The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of NDAs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lanreotide is a somatostatin analog that suppresses growth hormone (GH) and IGF-1 signaling. Its efficacy in GH-excess conditions such as acromegaly is the basis of its original use.

A link to hair growth regulation is conceivable, since GH/IGF-1 signaling can influence hair follicles. However, this is speculative. Hypertrichosis is usually a drug-induced or genetic phenotype, so a causal or therapeutic rationale for lanreotide has not been established. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top predictions (malformation syndrome with odontal/periodontal component, Dandy-Walker malformation syndrome, isolated genetic hair shaft abnormality, and Ambras type hypertrichosis universalis congenita) all scored between 0.9996 and 0.9997. They also have no supporting trials or literature. The two hypertrichosis-related predictions are likely correlated rather than independent evidence. The remaining ones are structural or genetic conditions that a hormone-modulating drug is unlikely to reverse.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication | Status |
|---------|------|------|-----------|------|
| ANDA217193 | Lanreotide Acetate (Exelan Pharmaceuticals) | Injection | Not available | Valid |
| NDA022074 | Somatuline Depot (Ipsen Biopharmaceuticals) | Injection | Not available | Valid |
| NDA215395 | Lanreotide Acetate (Cipla USA) | Injection | Not available | Valid |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): hypertension and hypertensive disorder, liver disease, gallbladder disease (including cholelithiasis, cholecystolithiasis, and choledocholithiasis), hyperglycemia, hypoglycemia, hypothyroidism (including myxedema and congenital hypothyroidism), and impaired renal function.
- **Drug Interactions**: The interaction query returned 100 interactions in total. The 20 listed in the data compiled for this report are all rated Moderate. They are mainly glucose-lowering agents, which fits the glycemic effects above:
  - Acarbose, metformin, pioglitazone, chlorpropamide, glimepiride
  - Albiglutide, dulaglutide, semaglutide
  - Alogliptin, linagliptin
  - Canagliflozin, dapagliflozin, empagliflozin
  - Insulins (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular)

Please refer to the package insert for label warnings and contraindications, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5), with no trials, no literature, and no plausible established mechanism.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (from FDA sources)
- Mechanism of action data (e.g., from DrugBank)
- A literature and trial search for lanreotide or somatostatin analogs in hypertrichosis and hair disorders
- Preclinical or mechanistic evidence linking GH/IGF-1 suppression to hair growth
- Clarification of the current US regulatory and commercial status; the drug is marketed, with 3 of 3 licenses valid
- A route and formulation compatibility assessment for the proposed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


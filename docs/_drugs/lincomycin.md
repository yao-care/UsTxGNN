---
layout: default
title: Lincomycin
parent: Model Prediction Only (L5)
nav_order: 862
evidence_level: L5
indication_count: 3
---

# Lincomycin
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

# Lincomycin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Lincomycin is a lincosamide antibiotic marketed in the US as an injectable.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US regulatory record (lincomycin is a lincosamide antibiotic used for bacterial infections) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Lincomycin is known to be a lincosamide antibiotic. It inhibits bacterial protein synthesis by binding the 50S ribosomal subunit. The record lists no original indications.

Polyclonal hyperviscosity syndrome arises from excess serum immunoglobulins, usually in chronic inflammatory or autoimmune states. It is not a bacterial disease, and no credible mechanistic link to lincomycin was identified. The high score cannot be checked against known pharmacology and may reflect knowledge-graph topology rather than biology.

The other two top predictions show the same pattern:

- **Hyperamylasemia** (score 99.14%, the same as the first prediction): this is a laboratory finding with many causes, not a disease a drug treats directly. Lincomycin has no known amylase-modulating or pancreatic mechanism. The identical score suggests a shared graph-neighborhood artifact.
- **Congenital analbuminemia** (score 99.06%): this is a rare genetic disorder of albumin synthesis. An antibiotic acting on bacterial ribosomes is not expected to correct it.

All three predictions have no supporting trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The record shows 14 authorizations in total. The main injectable authorizations are listed below. Approved-indication text is not included in the source record.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA050317 | Lincocin | Injection, solution | Pharmacia & Upjohn Company LLC |
| ANDA212770 | Lincomycin | Injection | PAI Holdings, LLC dba PAI Pharma |
| ANDA215657 | Lincomycin | Injection, solution | Sagent Pharmaceuticals |
| ANDA215657 | Lincomycin hydrochloride | Injection, solution | Gland Pharma Limited |

---

## Safety Considerations

No drug-interaction records were found. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN score, with no clinical trials, no literature, and no plausible mechanistic link. Polyclonal hyperviscosity syndrome, hyperamylasemia, and congenital analbuminemia are all poorly matched to an antibacterial mechanism. Safety data is also missing, so the candidate cannot move to safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action and original indication data from DrugBank
- A literature and trial search that identifies any biological basis for the predicted link
- A check of whether the high scores are a knowledge-graph artifact, for example by reviewing neighboring drugs and diseases in the graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


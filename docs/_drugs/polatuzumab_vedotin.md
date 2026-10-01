---
layout: default
title: Polatuzumab Vedotin
parent: Model Prediction Only (L5)
nav_order: 1058
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Polatuzumab Vedotin: From B-Cell Lymphoma to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Polatuzumab vedotin is an anti-CD79b antibody-drug conjugate (ADC) carrying an MMAE payload, marketed in the US as POLIVY. The TxGNN model predicts it may be effective for **HER2 positive breast carcinoma**, but **0 clinical trials** and **0 publications** currently support this direction. It is a model-only prediction. The original indication (B-cell lymphoma) comes from general drug knowledge, because the Evidence Pack contains no approved indication text.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | B-cell lymphoma (general knowledge; no approved indication text in the source data) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 records listed (both are the same license, BLA761121) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known information, polatuzumab vedotin targets CD79b, a component of the B-cell receptor. Its payload, MMAE, is a microtubule-disrupting agent. Its efficacy in B-cell malignancies rests on B-cell-specific targeting.

**No direct mechanistic link to HER2 positive breast carcinoma is supported by the data.** CD79b is B-cell specific, so the antibody is not expected to engage HER2-positive breast tumor cells. The high TxGNN score most plausibly reflects knowledge-graph proximity to the MMAE/tubulin-inhibitor class and to HER2-directed ADCs, not a CD79b-dependent mechanism. This is an inference and no drug-specific evidence was supplied to verify it.

Similarity to the original indication and route compatibility have not been assessed. Both are pending.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761121 | POLIVY (Genentech, Inc.) | Injection, powder, lyophilized, for solution | Not listed in source data |

The source lists this license twice with identical content. It is shown once here.

## Cytotoxicity

This section applies because polatuzumab vedotin is an antineoplastic agent. The entries below are class-level information, not drug-specific data from the Evidence Pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic payload (MMAE, microtubule inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (MMAE-class ADCs commonly cause neutropenia) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function; other items per package insert |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no registered trials or literature. The antibody target (CD79b) is B-cell specific, so no plausible mechanism links it to HER2-positive breast tumor cells.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Evidence that HER2-positive breast cancer cells are affected, such as CD79b expression data or preclinical models
- Clinical trial or literature searches for polatuzumab vedotin in breast cancer
- Confirmed original indication text from the US label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


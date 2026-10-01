---
layout: default
title: Nelarabine
parent: Model Prediction Only (L5)
nav_order: 960
evidence_level: L5
indication_count: 1
---

# Nelarabine
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

# Nelarabine: From T-Cell Leukemia/Lymphoma to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Nelarabine is a purine nucleoside analog cytotoxic drug. It is generally used for T-cell hematologic malignancies, but the US regulatory data provided does not list an approved indication.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, but **0 clinical trials** and **0 publications** currently support this direction. This is a model-only prediction with a serious neurotoxicity concern.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided data (all license records have empty indication text). Nelarabine is generally known as a T-cell leukemia/lymphoma agent. |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.43% (rank 13,256) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 15 (NDA and ANDA licenses combined) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general pharmacology, nelarabine is a prodrug of ara-G, a purine nucleoside analog that is preferentially cytotoxic to T-lymphocytes. This link comes from general knowledge, not from the input data.

The proposed connection to relapsing-remitting MS is T-cell depletion. Autoreactive T-cells are thought to drive MS, and cladribine, another purine analog, is already used in relapsing MS. A T-cell-selective agent could conceptually act in a similar way.

This rationale is plausible but unverified. Nelarabine is known to carry a boxed warning for severe neurotoxicity, including demyelination, peripheral neuropathy and Guillain-Barré-like ascending paralysis. Such toxicity is a serious liability in a demyelinating CNS disease. Without clinical data, the risk-benefit balance cannot be assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The record lists 15 licenses in total. The five main ones are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021877 | Arranon (Sandoz Inc) | Injection | Not provided in source data |
| ANDA216038 | Nelarabine (Meitheal Pharmaceuticals Inc) | Injection | Not provided in source data |
| ANDA215037 | Nelarabine (Zydus Lifesciences Limited) | Injection | Not provided in source data |
| ANDA216934 | Nelarabine (Dr. Reddy's Laboratories, Inc.) | Injection | Not provided in source data |
| ANDA212605 | Nelarabine (Gland Pharma Limited) | Injection | Not provided in source data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog, prodrug of ara-G) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Neurologic assessment is essential given the neurotoxicity concern. |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Key Warnings**: The source data has no warning entries. From general pharmacology, nelarabine carries a boxed warning for severe neurotoxicity (demyelination, peripheral neuropathy, Guillain-Barré-like ascending paralysis). This should be verified against the current package insert.
- **Drug Interactions**: No interaction records were found in the queried source (0 entries).

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no supporting trials or literature. The known neurotoxicity, including demyelination, directly conflicts with the target disease, so the risk-benefit balance is unfavorable without clinical data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the US licenses
- A literature and trial search on purine analogs in MS, and on nelarabine neurotoxicity mechanisms
- Preclinical evidence that a T-cell-depleting effect can be achieved without CNS demyelination risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


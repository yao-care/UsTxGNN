---
layout: default
title: Upadacitinib
parent: Model Prediction Only (L5)
nav_order: 1276
evidence_level: L5
indication_count: 2
---

# Upadacitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Upadacitinib: From Immune-Mediated Inflammatory Diseases to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Upadacitinib is marketed in the US as Rinvoq. It is generally known as a JAK1 inhibitor for immune-mediated inflammatory diseases, but the supplied data does not list its approved indications.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare congenital developmental disorder.
Currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied US label data (generally known use: immune-mediated inflammatory diseases) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license records (2 distinct NDAs: NDA211675, NDA218347) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, upadacitinib is a selective JAK1 inhibitor. It is used in diseases driven by JAK-STAT cytokine signaling, which are immune-mediated inflammatory diseases.

The predicted disease is a different kind of condition: a rare congenital disorder combining eye coloboma/microphthalmia with rhizomelic skeletal dysplasia. It arises from abnormal development rather than JAK-driven inflammation, and no biological link to the drug's original use has been documented. An adult-use immunomodulator would also have to explain how it could affect a structural malformation present since embryogenesis.

The very high score (99.61%) is a model output only. It may reflect graph artifacts for sparsely connected rare-disease nodes. The second-ranked prediction, brachydactyly-syndactyly syndrome (score 99.58%), is also a congenital limb malformation with no supporting evidence and the same weakness.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA211675 | Rinvoq | Extended-release tablet | AbbVie Inc. |
| NDA218347 | Rinvoq | Solution | AbbVie Inc. |

NDA211675 appears three times in the supplied data (three license records). It is listed once here. Approved indication text is not included in the supplied records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanistic link. The disease is a congenital developmental disorder, while the drug acts on inflammatory signaling. The high model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (required before any safety screening)
- Detailed mechanism of action data from DrugBank
- A documented biological rationale linking JAK1 inhibition to the pathology of this syndrome
- Any preclinical, case-level, or registry evidence in this disease
- Confirmation of the US approved indication text for the Rinvoq licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


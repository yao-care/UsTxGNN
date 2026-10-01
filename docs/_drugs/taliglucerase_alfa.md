---
layout: default
title: Taliglucerase Alfa
parent: Model Prediction Only (L5)
nav_order: 1196
evidence_level: L5
indication_count: 5
---

# Taliglucerase Alfa
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

# Taliglucerase Alfa: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Taliglucerase alfa (brand name ELELYSO) is a plant-cell-expressed recombinant glucocerebrosidase enzyme replacement therapy, originally used for Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome (MPS I)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (inferred from the drug's mechanism; the approved indication text is not provided in the source record) |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA022458) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, taliglucerase alfa is a recombinant glucocerebrosidase that breaks down glucosylceramide. Its efficacy in Gaucher disease is established.

Hurler syndrome is caused by a different enzyme deficiency: alpha-L-iduronidase, leading to glycosaminoglycan accumulation. The enzyme and its substrate differ from those of taliglucerase alfa. The only shared feature is that both diseases are lysosomal storage disorders. A specific enzyme replacement therapy for Hurler syndrome (laronidase) already exists.

The high score most likely reflects knowledge-graph proximity within lysosomal storage disorders, not a biological rationale. The mechanistic link is therefore weak.

Other predictions show the same pattern:
- **Scheie syndrome** (99.29%): the attenuated form of MPS I, with the same enzyme mismatch.
- **Cholesteryl ester storage disease** (99.12%): a different substrate, and sebelipase alfa is already available.
- **Benign neoplasm of adrenal gland** (99.28%): no plausible mechanistic link.
- **Autosomal ichthyosis syndrome with fatal disease course** (99.24%): only a weak, indirect connection through epidermal ceramide metabolism.

None of these has clinical trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA022458 | ELELYSO (Pfizer Laboratories Div Pfizer Inc) | Injection, powder, lyophilized, for solution | Not provided in the source record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (Evidence Level L5). There are no trials or publications, and the mechanism does not fit: glucocerebrosidase does not degrade glycosaminoglycans, and a specific approved therapy already exists.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently blocking safety screening)
- Detailed mechanism of action data (MOA)
- Preclinical evidence that glucocerebrosidase replacement affects glycosaminoglycan accumulation or MPS I pathology
- Route compatibility and similarity-to-original assessments (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


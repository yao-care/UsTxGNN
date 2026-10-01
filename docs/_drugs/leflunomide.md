---
layout: default
title: Leflunomide
parent: Model Prediction Only (L5)
nav_order: 842
evidence_level: L5
indication_count: 2
---

# Leflunomide
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

# Leflunomide: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Leflunomide is an oral immunomodulator, generally known for treating rheumatoid arthritis. The Evidence Pack does not record an approved indication.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, with a very high score.
There are **0 clinical trials** and **0 publications** supporting this prediction, and the signal is more likely a gene/phenotype association artifact than a treatment signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the input data (generally known: rheumatoid arthritis) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Leflunomide is generally known to act through its active metabolite teriflunomide, which inhibits DHODH (dihydroorotate dehydrogenase) and blocks de novo pyrimidine synthesis. This slows the proliferation of activated lymphocytes, which is the basis for its use in autoimmune disease.

The prediction is probably not a real therapeutic signal. The DHODH/pyrimidine pathway is linked to limb development: DHODH loss-of-function causes Miller syndrome, and leflunomide is teratogenic. The graph link may therefore reflect a shared gene or phenotype association rather than benefit. Brachydactyly-syndactyly syndrome is a structural congenital limb malformation, and an immunomodulator is unlikely to reverse it.

The second-ranked prediction, colobomatous microphthalmia-rhizomelic dysplasia syndrome (score 99.93%, L5), follows the same pattern. It is a rare congenital developmental syndrome, and ocular and skeletal malformations are part of the known teratogenic profile of DHODH inhibition. Neither prediction should be pursued without new evidence and verification of the underlying knowledge-graph edges.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA211863 | Leflunomide (Lupin Pharmaceuticals, Inc.) | Tablet, film coated | Not listed in the input |
| ANDA077090 | Leflunomide (AvPAK) | Tablet | Not listed in the input |
| ANDA077086 | Leflunomide (Bryant Ranch Prepack) | Tablet | Not listed in the input |
| ANDA212453 | Leflunomide (KVK-Tech, Inc.) | Tablet | Not listed in the input |
| ANDA212308 | Leflunomide (Zydus Pharmaceuticals (USA) Inc.) | Tablet, film coated | Not listed in the input |

All authorizations shown are oral products. The total number of authorizations is 20.

## Safety Considerations

- **Key Warnings**: Leflunomide is teratogenic, and DHODH inhibition is associated with limb, ocular and skeletal malformations.
- **Contraindications**: Leflunomide is contraindicated in pregnancy.

For other safety information, including drug interactions, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature. The mechanistic link points to a teratogenicity-related association rather than treatment benefit, and pregnancy contraindication adds a safety concern.

**To proceed, the following is needed:**
- Verification of the knowledge-graph edges behind the prediction (genes and pathways shared with brachydactyly-syndactyly syndrome)
- Detailed mechanism of action data (MOA) from DrugBank
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Any preclinical or clinical evidence that supports a therapeutic effect, as opposed to a phenotype association
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


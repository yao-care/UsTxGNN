---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 1273
evidence_level: L5
indication_count: 10
---

# Tyrosine
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

# Tyrosine: From No Documented Indication to Cauda Equina Syndrome

## One-Sentence Summary

Tyrosine is an amino acid supplement. The U.S. records list two liquid L-Tyrosine products, but neither has an approved indication on file.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **0 clinical trials** and only **1 publication** (an unrelated tumor case report) exist for this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text on record) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tyrosine is known as a biochemical precursor of catecholamines (dopamine, norepinephrine) and melanin. No original indication is on record, so the usual comparison between the original and the new indication cannot be made.

On the evidence provided, there is no credible mechanistic link between tyrosine and cauda equina syndrome. The high score (99.77%) comes from knowledge-graph similarity alone. The only retrieved paper is a case report of clear cell sarcoma arising from a sacral nerve root. Tyrosine appears in it only as melanin-pathway context, not as a treatment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17341045](https://pubmed.ncbi.nlm.nih.gov/17341045/) | 2006 | Case report | Neurosurgical Focus | Clear cell sarcoma originating in the S1 nerve root, previously diagnosed as psammomatous melanotic schwannoma. Tyrosine was not tested as therapy, so the paper does not support the prediction. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | L-Tyrosine | Liquid | Not listed |
| Not listed | L-Tyrosine High | Liquid | Not listed |

Both products are made by Professional Complementary Health Formulas.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). No trials exist, and the single paper is an unrelated tumor case report with no mechanistic link to tyrosine. The product records have no approved indication, and the package insert safety data is missing. The remaining top-ranked predictions are also on Hold, with no tyrosine-specific trial evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Authorization numbers and approved indication text for the two marketed products
- Any preclinical or clinical study that tests tyrosine in cauda equina syndrome or related nerve-root conditions
- Before any thyroid-related candidate is pursued, a review of whether supplying a thyroid hormone precursor could worsen the condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


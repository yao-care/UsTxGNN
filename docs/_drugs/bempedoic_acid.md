---
layout: default
title: Bempedoic Acid
parent: Model Prediction Only (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid: From Lipid Lowering to Hyperthyroidism

## One-Sentence Summary

Bempedoic acid is an oral cholesterol-lowering drug marketed in the US as Nexletol and Nexlizet.
The TxGNN model ranks **hyperthyroidism** as its top prediction, but there are **0 clinical trials** and **1 publication**, and that publication is not about bempedoic acid.
Among the model's 10 predictions, **homozygous familial hypercholesterolemia (HoFH)** has the strongest support (a 2026 real-world cohort and reviews) and is the one worth pursuing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the input data (mechanism indicates lipid lowering) |
| Predicted New Indication | Hyperthyroidism |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Bempedoic acid inhibits ATP-citrate lyase and activates AMPK. This lowers hepatic cholesterol synthesis. Because the score of hyperthyroidism is high, it looks plausible at first glance, but the review found **no credible mechanistic link**. The score most likely comes from thyroid-hormone-related lipid pathways in the knowledge graph, not from any antithyroid activity. Bempedoic acid is not known to affect thyroid hormone production or signalling.

The other predictions in the thyroid area (hyperthyroxinemia, thyroid hormone resistance due to a receptor beta mutation) show the same pattern: high scores, no evidence. Several others (infectious bovine rhinotracheitis, malignant catarrh) are veterinary diseases, which points to knowledge-graph artifacts.

One prediction is different. **Homozygous familial hypercholesterolemia** (score 99.48%) is biologically plausible. Bempedoic acid acts upstream of HMG-CoA reductase and upregulates LDL receptors. The effect should be weaker in patients with null LDLR variants. This is the prediction to move forward as a research question, with LDLR genotype stratification.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40549098](https://pubmed.ncbi.nlm.nih.gov/40549098/) | 2025 | Review | Drugs | First-approval review of tiratricol (a thyroid hormone analogue) for MCT8 deficiency and peripheral thyrotoxicosis. It does not involve bempedoic acid and gives no support for this prediction. |

For reference, the HoFH prediction has 17 listed publications, of which 10 were provided in the input. The most relevant are [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) (2026, cohort, real-world evaluation of bempedoic acid in HoFH) and [29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/) (2018, preclinical, LDL-C lowering and reduced atherosclerosis in LDLR-deficient minipigs).

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA211616 | Nexletol | Tablet, film coated | Esperion Therapeutics, Inc. |
| NDA211617 | Nexlizet | Tablet, film coated | Esperion Therapeutics, Inc. |

Both products are oral.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hyperthyroidism, is model output only (L5), with no trials, no relevant literature and no plausible mechanism. It should not be pursued. HoFH is the exception. It is biologically plausible and has L3 support, so it merits a separate research question.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed original approved indication text and mechanism of action data from an authoritative source
- For HoFH: review of the full 17-publication set and a controlled study stratified by LDLR genotype
- Manual review of the thyroid-related predictions to identify the graph pathway that drives their scores
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


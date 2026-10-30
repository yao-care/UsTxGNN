---
layout: default
title: Imiglucerase
parent: Model Prediction Only (L5)
nav_order: 791
evidence_level: L5
indication_count: 5
monitor_inn: "IMIGLUCERASE"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
last_modified_at: 2026-10-30
description: "Imiglucerase: predicted new indication Hurler syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Imiglucerase
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

## Imiglucerase: Hurler syndrome
{: .text-alpha }

## One-Sentence Summary

Imiglucerase is a recombinant enzyme replacement therapy, originally used to treat Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome**,
but there are currently **0 clinical trials** and only **1 general review article** (class-level context, no drug-specific data) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 0.9952 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, imiglucerase is a recombinant glucocerebrosidase (beta-glucosidase) that hydrolyzes glucosylceramide, and its efficacy in Gaucher disease is established.

Hurler syndrome (MPS I) is caused by alpha-L-iduronidase deficiency, which leads to accumulation of glycosaminoglycans (dermatan and heparan sulfate). Both Gaucher disease and Hurler syndrome are lysosomal storage disorders, and both are treated with the enzyme replacement therapy concept. However, the enzyme substrates are different, so imiglucerase would not be expected to correct the MPS I defect. The high TxGNN score most likely reflects network proximity within the lysosomal storage disease class rather than a direct mechanistic effect. A disease-specific approved therapy (laronidase) already exists.

The same reasoning applies to the second-ranked prediction, Scheie syndrome (an attenuated form of MPS I). Other lower-ranked predictions are discussed in the conclusion.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de medecine interne | General review of enzyme replacement therapy in lysosomal storage diseases; describes the progression from placenta-derived alglucerase to recombinant imiglucerase for Gaucher disease. Provides class-level context only, with no drug-specific evidence in Hurler syndrome. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA020367 (cancelled) | Cerezyme (Genzyme Corporation) | Injection, powder, lyophilized, for solution | Not specified in the data compiled |

## Safety Considerations

- **Drug Interactions**: Miglustat (Moderate, DDInter).

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, the only literature is a general class-level review, and the mechanism is not supported because imiglucerase targets glucosylceramide rather than the glycosaminoglycans accumulating in MPS I. An approved, disease-specific therapy (laronidase) already exists, and the US license for Cerezyme is listed as cancelled.

Other predictions show the same picture, with no trials or literature:
- **Scheie syndrome** (0.9929, L4): same reasoning as Hurler syndrome.
- **Benign neoplasm of adrenal gland** (0.9928, L5): no clear mechanistic link; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Autosomal ichthyosis syndrome with fatal disease course** (0.9924, L5): plausible but unverified link through impaired glucosylceramide metabolism in the skin barrier; hard to study given the early onset and fatal course.
- **Cholesteryl ester storage disease** (0.9912, L5): caused by lysosomal acid lipase deficiency, which imiglucerase does not address; sebelipase alfa is the approved specific therapy.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently missing, which blocks safety screening)
- Detailed mechanism of action data (MOA)
- Experimental evidence (in vitro or preclinical) that imiglucerase has any activity against MPS I substrates, which is unlikely given the differing enzyme specificity
- Clarification of the current US regulatory and supply status of Cerezyme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


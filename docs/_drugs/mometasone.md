---
layout: default
title: Mometasone
parent: Model Prediction Only (L5)
nav_order: 941
evidence_level: L5
indication_count: 1
---

# Mometasone
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

# Mometasone: From Nasal Corticosteroid Use to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Mometasone is a corticosteroid marketed in the US as metered nasal sprays. The supplied records do not state its approved indication.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**, but **no clinical trials** and only **2 case reports** are on file, and neither shows mometasone working in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the records (all listed licenses have blank indication text) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 (model prediction only; the Evidence Pack assigned L4, but the two case reports do not support mometasone in this disease) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for mometasone is not available in the supplied records. As a corticosteroid, mometasone plausibly acts through glucocorticoid receptor-mediated anti-inflammatory and pro-apoptotic effects on lymphocytes in the skin. This is general pharmacology, not something the records support directly.

Corticosteroids are widely used against inflammatory skin disease, and topical steroids are a standard treatment in early cutaneous T-cell lymphoma. The very high graph score most likely reflects this drug-class association rather than evidence specific to mometasone.

There is also a route gap. Every US product in the records is a metered nasal spray, and route compatibility with a skin-directed indication has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case Report | Proc (Bayl Univ Med Cent) | A 62-year-old woman had cutaneous pseudolymphoma, a benign condition that mimics lymphoma. Mometasone and tacrolimus failed, and she was then treated with tapinarof. It does not show mometasone benefit in true lymphoma. |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case Report | J Cutan Pathol | An 11-year-old boy had CD8+CD56+ cytotoxic-type mycosis fungoides, a form of cutaneous T-cell lymphoma, with delayed diagnosis. The available abstract excerpt does not mention mometasone. |

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA215712 | Nasonex (L. Perrigo Company) | Spray, metered |
| NDA215712 | Rugby mometasone furoate nasal (Rugby Laboratories) | Spray, metered |
| ANDA217498 | Mometasone Furoate (Aurohealth LLC) | Spray, metered |
| NDA215712 | up and up allergy (Target Corporation) | Spray, metered |
| NDA215712 | allergy nasal (Walgreen Company) | Spray, metered |

The records give no approved indication text for these licenses.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any trial, and the only literature is two case reports. One describes a mometasone failure in a benign look-alike condition, and the other does not mention mometasone. The marketed forms are nasal sprays, which do not match a skin-directed indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data for mometasone (e.g., from DrugBank)
- Published evidence of topical mometasone in mycosis fungoides or other cutaneous T-cell lymphoma, such as retrospective series or trials
- Route and formulation assessment: whether a topical mometasone product exists and how it fits this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


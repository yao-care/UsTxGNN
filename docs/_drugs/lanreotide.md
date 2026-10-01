---
layout: default
title: Lanreotide
parent: Model Prediction Only (L5)
nav_order: 834
evidence_level: L5
indication_count: 5
---

# Lanreotide
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

# Lanreotide: From Acromegaly to Hypertrichosis

## One-Sentence Summary

Lanreotide is a somatostatin analog that is marketed in the US as an injectable. The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no drug-specific publications** currently support this prediction. It is a model-only signal and should be held.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided data (approved indication text is empty for all licenses). Acromegaly is assumed from general pharmacology, not from the Evidence Pack. |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 registered entries (only 3 distinct authorizations are listed) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, lanreotide is a somatostatin analog acting on SSTR2 and SSTR5. It suppresses growth hormone (GH) and IGF-1 secretion.

The only rationale is indirect and speculative. Excess GH/IGF-1 can cause hirsutism in acromegaly, so suppressing this axis might, in theory, reduce hair overgrowth in that setting. Congenital and generalized hypertrichosis, however, is generally genetic and not driven by GH excess. No direct mechanistic link is established. The prediction rests on the knowledge-graph score alone.

The other top-ranked predictions have no plausible link either:

- **Malformation syndrome with odontal/periodontal component** (99.96%): 20 publications were retrieved, but they cover periodontitis in general. None mentions lanreotide or somatostatin analogs, so the match came from the disease term only.
- **Dandy-Walker malformation syndrome** (99.96%): this is a congenital structural defect that a hormone-suppressing peptide would not be expected to reverse.
- **Isolated genetic hair shaft abnormality** (99.96%): these are structural and genetic (keratin-related) conditions.
- **Ambras type hypertrichosis universalis congenita** (99.96%): this is a rare genetic hypertrichosis not known to be driven by the GH/IGF-1 axis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for hypertrichosis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022074 | SOMATULINE DEPOT (Ipsen Biopharmaceuticals) | Injection | Indication text not provided |
| NDA215395 | Lanreotide Acetate (Cipla USA) | Injection | Indication text not provided |
| ANDA217193 | LANREOTIDE ACETATE (Exelan Pharmaceuticals) | Injection | Indication text not provided |

The data contains duplicate entries for NDA022074 and ANDA217193. Only the injectable route is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials, no drug-specific literature and no established mechanism. The hypertrichosis phenotype is mostly genetic and is not driven by the GH/IGF-1 axis. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Approved indication text for the US licenses
- Drug-specific literature or case reports of lanreotide or somatostatin analogs in hypertrichosis, ideally in acromegaly-associated hirsutism
- Route compatibility assessment (currently pending; only injectable forms are available)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


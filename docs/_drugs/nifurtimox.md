---
layout: default
title: Nifurtimox
parent: Model Prediction Only (L5)
nav_order: 965
evidence_level: L5
indication_count: 7
---

# Nifurtimox
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Nifurtimox: From Antiparasitic Therapy to Congenital Analbuminemia

## One-Sentence Summary

Nifurtimox is a nitrofuran antiparasitic drug, marketed in the US as LAMPIT film-coated tablets.
The TxGNN model predicts it may be effective for **congenital analbuminemia**,
but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Congenital analbuminemia |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 records (both NDA213464) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Based on known information, nifurtimox is a nitrofuran antiparasitic. Its activity is thought to come from nitroreductase-mediated generation of reactive oxygen species and nitro-radical metabolites in trypanosomes.

No plausible mechanistic link to congenital analbuminemia was identified. This is a rare genetic disorder of albumin synthesis, and a drug that acts on parasite nitroreductase pathways has no evident way to correct it. The high score (0.996) is a graph-based prediction with no supporting biological rationale.

The other six predictions show the same pattern. All are L5, with scores of 0.991–0.995 and no trials or literature:
- polyclonal hyperviscosity syndrome
- hyperamylasemia
- blood group incompatibility
- monoclonal gammopathy
- premalignant hematological system disease
- hematological disease associated with an acquired peripheral neuropathy

The first two share the same score (0.9947), which suggests a shared graph-neighborhood artifact rather than disease-specific signal. Peripheral neuropathy is a known adverse effect of nifurtimox, so for the last of these the drug could worsen the condition rather than treat it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA213464 | LAMPIT (Bayer Healthcare Pharmaceuticals Inc.) | Film-coated tablet (oral) |

The source data lists NDA213464 twice with identical content, and no approved-indication text is included.

## Safety Considerations

- **Adverse effects**: Peripheral neuropathy is a known adverse effect of nifurtimox. This matters especially for the neuropathy-related prediction (rank 7).
- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for other safety information (warnings and contraindications).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5, no trials or literature), and no plausible mechanistic link to congenital analbuminemia exists. Safety data are also incomplete, with the package insert warnings still missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A biological rationale connecting nitrofuran activity to albumin synthesis, or evidence from preclinical studies
- A safety assessment of the peripheral neuropathy risk before evaluating any neuropathy-related indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


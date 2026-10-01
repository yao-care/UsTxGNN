---
layout: default
title: Darolutamide
parent: Model Prediction Only (L5)
nav_order: 571
evidence_level: L5
indication_count: 3
---

# Darolutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Darolutamide: From Prostate Cancer to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Darolutamide is a non-steroidal androgen receptor antagonist. The source record does not list an approved indication, but the drug is known clinically as a prostate cancer therapy.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data (known clinically as a prostate cancer drug) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on its known pharmacology, darolutamide blocks the androgen receptor.

The mechanistic link to HoFH is weak. HoFH is caused by loss-of-function variants in the LDL receptor (LDLR) pathway. Androgen signaling may have indirect effects on lipids, but blocking the androgen receptor would not correct LDL receptor deficiency. The high TxGNN score (0.991) reflects a pattern in the knowledge graph and is not supported by any clinical or literature evidence in this dataset.

The next two predictions are also weak:
- **Multiple endocrine neoplasia (score 99.06%)**: The only trial signal is a terminated, generic precision-oncology study (NCT03878524, Phase 1, 2 participants), so it offers no interpretable evidence.
- **HIV infectious disease (score 99.04%)**: There is no plausible antiviral mechanism and no supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered for homozygous familial hypercholesterolemia.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212099 | NUBEQA (Bayer HealthCare Pharmaceuticals Inc.) | Film-coated tablet (oral) | Not listed in the source data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support (L5). Blocking the androgen receptor has no credible way to correct the LDL receptor deficiency that causes HoFH. The high model score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism of action data from DrugBank
- Preclinical or mechanistic evidence that androgen receptor antagonism affects LDL metabolism
- Any registered studies or publications that link darolutamide to lipid disorders

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


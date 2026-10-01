---
layout: default
title: Fostamatinib
parent: Model Prediction Only (L5)
nav_order: 740
evidence_level: L5
indication_count: 2
---

# Fostamatinib
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

# Fostamatinib: From Immune Thrombocytopenia to Autosomal Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Fostamatinib is marketed in the US as TAVALISSE for immune thrombocytopenia (from general drug knowledge; the supplied data lists no indication text). The TxGNN model predicts it may be useful for **autosomal thrombocytopenia with normal platelets**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Autosomal thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 listed entries, both under NDA209299 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied input. From general drug knowledge, fostamatinib is a SYK inhibitor whose active metabolite is R406. In immune thrombocytopenia it reduces Fc-gamma-receptor-mediated platelet destruction by macrophages.

The predicted disease is an inherited thrombocytopenia, usually linked to ANKRD26 variants that dysregulate thrombopoietin-receptor signalling and impair platelet production. Its cause is not immune clearance, so the SYK-inhibition mechanism does not obviously apply. The link appears to be a weak, indirect inference from the shared low-platelet phenotype in the knowledge graph.

A high model score is not evidence of efficacy. The prediction needs independent mechanistic and clinical support before it can be considered credible.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA209299 | TAVALISSE | Tablet (oral) | Rigel Pharmaceuticals, Inc. |

The input lists this NDA twice with identical details, so it is shown once here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score, with no trials or publications. The SYK-inhibition mechanism does not fit an inherited platelet-production disorder. The second-ranked prediction, non-syndromic esophageal malformation (score 99.05%), has no plausible mechanism for a SYK inhibitor and is likely a knowledge-graph artifact.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence that SYK inhibition affects platelet production in ANKRD26-related thrombocytopenia
- Any registered trials or published case reports in this indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


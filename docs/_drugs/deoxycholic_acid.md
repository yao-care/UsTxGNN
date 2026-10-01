---
layout: default
title: Deoxycholic Acid
parent: Model Prediction Only (L5)
nav_order: 583
evidence_level: L5
indication_count: 3
---

# Deoxycholic Acid
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

# Deoxycholic Acid: From an Injectable Cytolytic Agent (KYBELLA) to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome

## One-Sentence Summary

Deoxycholic acid is a secondary bile acid marketed in the US as an injectable cytolytic agent (KYBELLA).
The TxGNN model predicts it may be effective for **autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome**, a rare monogenic vascular basement-membrane disorder.
This prediction currently has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data (marketed as KYBELLA, an injectable cytolytic product) |
| Predicted New Indication | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Deoxycholic acid is a secondary bile acid, and its marketed use is as a cytolytic agent given by injection.

The data support no mechanistic link between this drug and the predicted disease. The disease is a rare monogenic disorder of vascular basement membranes. The 99.49% score comes from graph-based prediction alone, with no trials, no literature and no known mechanism of action to back it. This prediction should be treated as a model output that needs independent validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA206333 | KYBELLA (Kythera Biopharmaceuticals Inc.) | Injection, solution | Not provided in the record |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, at evidence level L5. There is no clinical, literature or mechanistic support. The drug is a locally injected cytolytic agent, and the target disease is a monogenic vascular disorder with no plausible drug-specific link.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Package insert warnings and contraindications, which are needed before any safety screening
- A drug-specific mechanistic rationale linking deoxycholic acid to the disease, or supporting preclinical data
- A review of the other two TxGNN predictions for this drug:
  - Diabetic nephropathy (score 99.32%) has L4 preclinical support. Most of it involves FXR/TGR5 signalling or other bile acids such as UDCA rather than deoxycholic acid itself. Its systemic relevance is doubtful because the marketed product is a local injection. It is classed as a research question, not a development candidate.
  - Brain small vessel disease 1 with or without ocular anomalies (score 99.49%) has only generic disease-background literature, with no drug-specific evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


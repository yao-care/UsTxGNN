---
layout: default
title: Zanamivir
parent: Model Prediction Only (L5)
nav_order: 1301
evidence_level: L5
indication_count: 2
---

# Zanamivir
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Zanamivir is a viral neuraminidase inhibitor used against influenza A and B. The TxGNN model predicts it may be effective for **pyelonephritis**, a kidney infection that is usually bacterial. **No clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (the US label text is blank in the data provided; this comes from the drug's known class and use) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, zanamivir is a neuraminidase (sialidase) inhibitor, and its efficacy in influenza A and B is established.

A credible mechanistic link to pyelonephritis has not been identified. Pyelonephritis is usually caused by bacteria in the upper urinary tract, while zanamivir targets a viral enzyme. Some bacteria produce sialidases, but there is no data showing that zanamivir inhibits them at relevant concentrations or affects urinary pathogens.

The very high TxGNN score (0.998) is a model output only. With no trials, no literature, and no confirmed original indication or mechanism data, the prediction cannot be cross-checked.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021036 | RELENZA (GlaxoSmithKline LLC) | Powder | Not listed in the data provided |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). There is no clinical or preclinical evidence, and no plausible mechanism links a viral neuraminidase inhibitor to a bacterial kidney infection.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications, approved indication), which is required before any safety screening
- Detailed mechanism of action data from DrugBank
- Preclinical evidence that zanamivir has activity against urinary pathogens, or a mechanistic argument for why it might
- Route compatibility assessment: the marketed product is a powder formulation, and its suitability for a systemic kidney infection has not been assessed
- A search for relevant clinical trials and literature specific to pyelonephritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Benazepril
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 5
---

# Benazepril
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

# Benazepril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Benazepril is an ACE inhibitor marketed in the US, and its original indication is hypertension. The pack's license records contain no indication text, so this is inferred from the drug class and the pack's own rationale.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but the prediction rests on the model alone: **0 clinical trials** and **0 publications** support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (inferred; license records contain no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are all ANDAs, i.e., generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, benazepril is an ACE inhibitor. It blocks the renin-angiotensin-aldosterone system (RAAS), and its efficacy in hypertension is established. Mechanistically it may be applicable to renovascular hypertension, which is largely driven by renin-angiotensin activity.

The link is biologically plausible, but two caveats apply:

- **May not be true repurposing.** Renovascular hypertension may simply be a subtype of the hypertension benazepril is already marketed for. This needs confirmation against the label.
- **Renal safety risk.** ACE inhibitors carry a risk of acute kidney injury in bilateral renal artery stenosis, which is a central concern for this population.

The other four predictions are weaker:

| Predicted Indication | Score | Assessment |
|------|------|------|
| Malignant hypertensive renal disease | 99.65% | Same score as the top prediction, so likely a shared graph neighborhood rather than an independent signal. RAAS blockade is plausible, but there is no clinical evidence. |
| Pulmonary hypertension, unclear multifactorial mechanism | 99.60% | Model prediction only. The RAAS rationale is weak, and systemic vasodilation may be a concern. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.60% | The 20 literature hits (10 shown) are general hypoxia papers with no mention of benazepril or ACE inhibitors. They look like keyword matches. |
| Braddock syndrome | 99.44% | No mechanistic rationale; possibly a graph artifact. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction.

## US Market Information

The pack's license records contain no approved-indication text, so the manufacturer is shown instead.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076118 | Benazepril Hydrochloride | Tablet, coated | PD-Rx Pharmaceuticals, Inc. |
| ANDA076118 | Benazepril Hydrochloride | Tablet, coated | REMEDYREPACK INC. |
| ANDA076118 | Benazepril Hydrochloride | Tablet, coated | A-S Medication Solutions |
| ANDA076820 | Benazepril Hydrochloride | Tablet | Bryant Ranch Prepack |
| ANDA076820 | Benazepril Hydrochloride | Tablet | Cardinal Health 107, LLC |

All are oral products (tablet, coated tablet, film-coated tablet).

## Safety Considerations

Please refer to the package insert for safety information.

Caution from the prediction rationale: ACE inhibitors carry a risk of acute kidney injury in bilateral renal artery stenosis.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predictions are supported only by model scores (L5), with no trials or drug-specific literature. The package insert safety data is missing, which blocks safety screening. The top prediction may also overlap with benazepril's existing hypertension use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (downloaded from the FDA website), to unblock safety screening
- Mechanism of action data (e.g., from the DrugBank API)
- Confirmation from the current label of whether renovascular or malignant hypertension is already covered under the hypertension indication
- Targeted searches for benazepril or ACE inhibitors in renovascular hypertension, and screening of the 10 unshown hypoxia-related papers
- A renal safety assessment for patients with renal artery stenosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


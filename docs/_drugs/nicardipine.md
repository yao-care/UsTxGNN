---
layout: default
title: Nicardipine
parent: Model Prediction Only (L5)
nav_order: 964
evidence_level: L5
indication_count: 5
---

# Nicardipine
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

# Nicardipine: From Its Approved Use to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Nicardipine is a marketed dihydropyridine calcium channel blocker with 20 US authorizations, in capsule and injectable forms.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**.
Currently there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nicardipine is a dihydropyridine calcium channel blocker, so pulmonary vasodilation is biologically plausible. That is background pharmacology, not something the provided data confirms. The approved indication text is also missing from the source data, so the relationship between the original and predicted indications cannot be assessed.

The 99.26% TxGNN score is a graph-based output only. With no trials, no literature and no MOA data, the mechanistic link cannot be checked. The disease subtype ("unclear multifactorial mechanism") has no defined pathophysiology, which makes any mechanistic argument weaker.

The same model run also predicted nicardipine for pulmonary hypertension owing to lung disease and/or hypoxia, malignant renovascular hypertension, malignant hypertensive renal disease, and Braddock syndrome. The two malignant hypertension predictions are mechanistically coherent, because nicardipine lowers blood pressure by arterial vasodilation. Neither has supporting evidence in the provided data. For hypoxic or lung-disease pulmonary hypertension, non-selective vasodilators can worsen ventilation-perfusion matching and gas exchange, so that prediction could point toward harm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

For the second-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), 20 publications were retrieved. They cover general hypoxia biology (brain aging, cancer, multiple sclerosis, altitude) and do not evaluate nicardipine, so they are not counted as clinical evidence.

## US Market Information

Five of the 20 authorizations are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA218638 | Nicardipine Hydrochloride | Capsule | Zydus Pharmaceuticals USA Inc. |
| ANDA216420 | Nicardipine Hydrochloride | Injection | Armas Pharmaceuticals Inc. |
| NDA019734 | CARDENE IV | Injection, solution | Baxter Healthcare Corporation |
| ANDA218202 | Nicardipine hydrochloride | Capsule | Amneal Pharmaceuticals NY LLC |
| ANDA217548 | Nicardipine Hydrochloride | Injection | Fresenius Kabi USA, LLC |

Available routes are oral (capsule) and injectable (injection and injection, solution).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no relevant literature and no mechanism data. The disease subtype is also poorly defined. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed before any safety screening
- Mechanism of action data (e.g., from DrugBank) and the approved indication text
- A targeted search for nicardipine in pulmonary hypertension (clinical trials and literature), replacing the non-specific hypoxia results
- A clearer definition of the disease subtype, and a check of route compatibility (oral vs. injectable) against the setting
- Verification of the malignant hypertension predictions (ranks 3 and 4) against the label and guidelines, since these are the more mechanistically coherent directions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


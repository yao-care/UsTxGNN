---
layout: default
title: Insulin Lispro
parent: Model Prediction Only (L5)
nav_order: 802
evidence_level: L5
indication_count: 9
monitor_inn: "Insulin lispro"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
last_modified_at: 2026-10-28
description: "Insulin Lispro: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Not recorded in the local data"
---

# Insulin Lispro
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Insulin Lispro: Autoimmune oophoritis
{: .text-alpha }

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analog, originally used to control blood glucose in type 1 and type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but **no clinical trials and no publications** currently support this prediction.
The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as shared autoimmune comorbidity with type 1 diabetes, rather than a true therapeutic mechanism or biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 6) |
| Number of NDAs | 6 (all cancelled; listed as BLAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general knowledge, insulin lispro is a rapid-acting insulin analog that acts on the insulin receptor to promote cellular glucose uptake. Its efficacy in diabetes mellitus is well established.

Autoimmune oophoritis is an immune-mediated ovarian disorder, often seen in autoimmune polyglandular syndromes that include type 1 diabetes. The high score (0.9978) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No direct mechanistic link is established: insulin would at most treat a coexisting diabetes, not the oophoritis itself. The prediction should therefore be read as an association signal, not as evidence of therapeutic benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|-----------|
| BLA020563 | HUMALOG | Injection, solution | A-S Medication Solutions | Valid |
| BLA021018 | Humalog | Injection, suspension | Eli Lilly and Company | Valid |
| BLA021017 | Humalog | Injection, suspension | Eli Lilly and Company | Valid |
| BLA209196 | ADMELOG | Injection, solution | Sanofi-Aventis U.S. LLC | Valid |
| BLA205747 | Humalog | Injection, solution | Eli Lilly and Company | Valid |

One additional cancelled license (BLA761109, LYUMJEV, injection solution, A-S Medication Solutions) is also on record. Approved indication text was not available for these entries.

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. Most of those reviewed are of moderate severity, and a few are minor. Examples include:
  - Beta-agonists and sympathomimetics (formoterol, salbutamol, epinephrine, phenylephrine, pseudoephedrine), which may alter glycaemic control
  - Corticosteroids (hydrocortisone)
  - Other antidiabetic agents (metformin, alogliptin, albiglutide)
  - Beta-blockers (acebutolol)
  - Hydrochlorothiazide, acetazolamide, estrogens/hormonal contraceptives (estradiol, ethinylestradiol, levonorgestrel), alpelisib, doxycycline and ethanol

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (evidence level L5), with no trials or literature for autoimmune oophoritis and no plausible direct mechanism. The high score likely reflects similarities the TxGNN model (deep learning) learned between related diseases, such as comorbidity with autoimmune diabetes. The drug is marketed in the US, with 6 valid licenses on record.

**To proceed, the following is needed:**
- Mechanistic evidence showing insulin lispro could affect ovarian autoimmune pathology
- Clinical or observational data in autoimmune oophoritis
- Package insert warnings and contraindications, and mechanism of action data
- Confirmation of current US marketing status

**Other predictions reviewed (all Hold):** The remaining predictions are also unsupported or reflect existing diabetes care or adverse effects rather than new indications.
- Thiamine-responsive dysfunction syndrome (0.9937): insulin would only treat the diabetic component.
- Classic stiff person syndrome (0.9936) and focal stiff limb syndrome (0.9936): anti-GAD autoimmune comorbidity with type 1 diabetes.
- Opsismodysplasia (0.9934): only a hypothetical link through INPPL1/SHIP2 insulin signaling.
- Drug-induced localized lipodystrophy (0.9909): insulin injection is a known cause, not a treatment.
- Pancreatic agenesis (0.9909): insulin replacement is standard care but falls within the existing diabetes indication. The single review found (PMID 12150359, 2002) covers type 2 diabetes in general and is not specific to this condition.
- Centrifugal lipodystrophy (0.9904) and pressure-induced localized lipoatrophy (0.9903): no supporting evidence, and insulin injections are themselves associated with lipoatrophy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


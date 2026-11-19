---
layout: default
title: Benazepril
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 4
monitor_inn: "BENAZEPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-11-06
description: "Benazepril: predicted new indication malignant hypertensive renal disease (evidence level L5). In the US: 34 FDA applications (22 active)"
---

# Benazepril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Benazepril: ACE inhibitor → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Benazepril is an angiotensin-converting enzyme (ACE) inhibitor marketed in the United States.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**.
So far, **no clinical trials and no publications** directly studying this disease with benazepril have been compiled, so the prediction rests on the model score and class-level mechanistic reasoning.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 22 of 34) |
| Number of FDA Applications | 34 (active: 22) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for benazepril: "Benazepril and benazeprilat inhibit angiotensin-converting enzyme (ACE) in human subjects and animals. Benazeprilat has much greater ACE inhibitory activity than does benazepril. ACE is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor substance, angiotensin II." ([DailyMed: Lotensin (benazepril hydrochloride) prescribing information, Validus Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2abb091b-a53e-46b0-9b84-e5ee8f2bdd8e), label version 2025-09-30; accessed 2026-11-19.) Based on its drug class, benazepril blocks the ACE enzyme and thereby dampens the renin-angiotensin-aldosterone system (RAAS). This lowers blood pressure and reduces pressure inside the kidney's filtering units.

Malignant hypertensive kidney disease involves severe blood pressure elevation together with strong RAAS activation. Reducing intraglomerular pressure and protein leakage is therefore biologically coherent for an ACE inhibitor.

This reasoning is indirect, however. It rests on class-level knowledge and on the TxGNN score. No study specific to benazepril in this disease was supplied. Any investigation would need close monitoring of kidney function and potassium.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Benazepril is marketed in the United States. The records compiled for this report are listed below and may be partial.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076118 | Benazepril Hydrochloride | Tablet, coated | PD-Rx Pharmaceuticals, Inc. |
| ANDA076820 | Benazepril Hydrochloride | Tablet | Bryant Ranch Prepack |
| ANDA078212 | Benazepril Hydrochloride | Tablet, film coated | Preferred Pharmaceuticlas Inc. |
| ANDA076267 | Benazepril hydrochloride | Tablet | Chartwell RX, LLC |

All listed products are oral dosage forms.

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. The entries reviewed are all rated Moderate and are mainly:
  - Glucose-lowering drugs: insulins (human, aspart, degludec, detemir, glargine, glulisine, lispro and others), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), alogliptin, dapagliflozin and exenatide
  - Corticosteroids: hydrocortisone
  - Glycerin

  Blood glucose should be monitored closely when benazepril is combined with these agents.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9965) and the mechanistic reasoning is plausible for an ACE inhibitor. However, no clinical trial or publication directly studies benazepril in malignant hypertensive renal disease, so the evidence is at the model-prediction level only (L5).

**To proceed, the following is needed:**
- A systematic literature search for ACE inhibitors, or benazepril specifically, in malignant hypertensive nephrosclerosis
- Detailed mechanism-of-action data for benazepril
- The package insert warnings and contraindications, reviewed for renal impairment, hyperkalaemia and hypotension
- A kidney-function and potassium monitoring plan for any proposed study

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for benazepril are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lotensin (benazepril hydrochloride) prescribing information, Validus Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2abb091b-a53e-46b0-9b84-e5ee8f2bdd8e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


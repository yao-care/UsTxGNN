---
layout: default
title: Insulin Human
parent: Model Prediction Only (L5)
nav_order: 801
evidence_level: L5
indication_count: 10
monitor_inn: "Insulin human"
predicted_indications: ["autoimmune oophoritis", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy"]
last_modified_at: 2026-10-30
description: "Insulin Human: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Type 2 diabetes mellitus, type 1 diabetes mellitus…"
---

# Insulin Human
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Insulin Human: From Diabetes Mellitus to Autoimmune Oophoritis
{: .text-alpha }

## One-Sentence Summary

Insulin human is a replacement hormone originally used to treat type 1 and type 2 diabetes mellitus and diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on a TxGNN model (deep learning) score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus, type 1 diabetes mellitus, diabetic ketoacidosis (the US license records contain no indication text) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 8) |
| Number of FDA Applications | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Insulin is known as the replacement hormone for diabetes, but this report cannot draw a mechanistic argument for ovarian disease from the available data.

The prediction is plausible only in a loose sense. Insulin signaling influences ovarian function, and autoimmune polyendocrine syndromes can co-occur with autoimmune diabetes. These are indirect associations, not evidence that insulin treats autoimmune oophoritis. The score of 0.9984 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

### Other predictions reviewed

The other top-ranked predictions have no clinical or literature support either, and several are better explained by artifacts than by true therapeutic potential:

| Predicted Indication | TxGNN Score | Interpretation |
|------|------|------|
| Classic stiff person syndrome | 0.9981 | Likely reflects anti-GAD65 autoimmunity and comorbid type 1 diabetes; insulin would treat the diabetes, not the neurological disease |
| Focal stiff limb syndrome | 0.9981 | Score from the TxGNN model (deep learning); it may reflect similarities the model learned between related diseases, not biological evidence |
| Thiamine-responsive dysfunction syndrome | 0.9980 | Diabetes is a core feature; insulin would be symptomatic management, with thiamine as the disease-directed therapy |
| Opsismodysplasia | 0.9979 | Theoretical link via INPPL1 (SHIP2) in insulin/PI3K signaling; direction of effect unclear |
| Drug-induced localized lipodystrophy | 0.9972 | A known adverse effect of injected insulin; a safety signal, not a treatment |
| Centrifugal lipodystrophy | 0.9970 | Speculative adipose-tissue link; no support for benefit |
| Pressure-induced localized lipoatrophy | 0.9970 | Speculative; injection-site lipoatrophy is a known insulin adverse effect |
| Pancreatic agenesis | 0.9970 | Insulin replacement is already standard care for the resulting diabetes, so this is an extension of the existing indication rather than true repurposing |
| Idiopathic localized lipodystrophy | 0.9968 | Generic lipodystrophy association; insulin may itself cause localized lipodystrophy |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA018780 | HUMULIN R (A-S Medication Solutions) | Injection, solution | Not recorded; status valid |
| BLA019959 | Novolin (A-S Medication Solutions) | Injection, suspension | Not recorded; status valid |
| BLA018781 | Humulin (Eli Lilly and Company) | Injection, suspension | Not recorded; status valid |
| BLA019717 | Humulin (Eli Lilly and Company) | Injection, suspension | Not recorded; status valid |
| BLA022472 | AFREZZA (Mannkind Corporation) | Powder, metered | Not recorded; status valid |

The compiled data lists 8 authorizations in total, all with cancelled status. Only the first 5 are shown above. The other three are Novolin (BLA019938 and BLA019991, Novo Nordisk) and MYXREDLIN (BLA208157, Baxter Healthcare Corporation).

## Safety Considerations

- **Drug Interactions**: The interaction query completed with 100 interactions recorded. The 19 reviewed here are mostly Moderate, with a few Minor. Notable moderate ones include:
  - Other antidiabetic agents (metformin, pioglitazone, alogliptin, albiglutide), which may add to glucose-lowering effects
  - Sympathomimetics and bronchodilators (epinephrine, phenylephrine, pseudoephedrine, salbutamol)
  - Corticosteroids (hydrocortisone), estrogens (estradiol, ethinylestradiol) and hydrochlorothiazide, which may alter glucose control
  - Beta-blockers (acebutolol), the ACE inhibitor benazepril, acetazolamide, doxycycline, alpelisib and ethanol
  - Minor: topical hydrocortisone and topical alclometasone

- **Predicted-indication signal**: Localized lipodystrophy and lipoatrophy are known adverse effects of injected insulin at repeated injection sites, so insulin should not be considered for lipodystrophy-type conditions.

Please refer to the package insert for warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for autoimmune oophoritis is supported only by a TxGNN model (deep learning) score, with no clinical trials or literature (evidence level L5). No mechanistic data is available, and the package insert safety information is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data for insulin human
- A literature and trial search specific to autoimmune oophoritis and insulin, to test whether any real-world support exists
- Route compatibility and similarity-to-original-indication assessments, which are still pending
- Clarification of the regulatory picture, since the drug is marketed with 8 valid licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


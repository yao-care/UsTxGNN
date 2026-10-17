---
layout: default
title: Insulin Glargine
parent: Model Prediction Only (L5)
nav_order: 799
evidence_level: L5
indication_count: 10
monitor_inn: "Insulin glargine"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
last_modified_at: 2026-10-14
description: "Insulin Glargine: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Type 2 diabetes mellitus, type 1 diabetes mellitus…"
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting insulin analog, originally used to treat type 1 and type 2 diabetes mellitus and diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is a computational inference only, and it most likely reflects shared autoimmune biology, not a therapeutic effect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus, type 1 diabetes mellitus, diabetic ketoacidosis (the approved indication text for the US licenses is not available; these indications come from the knowledge graph) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin glargine is a long-acting insulin analog that acts on the insulin receptor to regulate glucose metabolism. Its efficacy in diabetes is well established.

No direct mechanistic link to autoimmune oophoritis has been established. Autoimmune oophoritis is an immune-mediated ovarian disorder that is sometimes part of autoimmune polyendocrine syndromes, which also include type 1 diabetes. The connection is shared autoimmunity, not a therapeutic effect of insulin on ovarian pathology. The high TxGNN score (0.9988) is most likely driven by network proximity to autoimmune diabetes and not by a causal therapeutic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761201 | SEMGLEE (Biocon Biologics Inc.) | Injection, solution | Not available (status: cancelled) |
| BLA021081 | Lantus Solostar (sanofi-aventis U.S. LLC) | Injection, solution | Not available (status: cancelled) |
| BLA205692 | BASAGLAR (Eli Lilly and Company) | Injection, solution | Not available (status: cancelled) |
| BLA761215 | Rezvoglar (Eli Lilly and Company) | Injection, solution | Not available (status: cancelled) |
| BLA206538 | TOUJEO (A-S Medication Solutions) | Injection, solution | Not available (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the data compiled for this report. Most of the ones listed are Moderate and a few are Minor; none are rated higher. Main examples:
  - Antidiabetic agents (additive glucose-lowering effects): metformin, pioglitazone, alogliptin, albiglutide
  - Sympathomimetics and bronchodilators: epinephrine, phenylephrine, pseudoephedrine, salbutamol, formoterol
  - Corticosteroids: hydrocortisone (Moderate), topical hydrocortisone and topical alclometasone (Minor)
  - Hormonal agents: estradiol, ethinylestradiol
  - Others: acebutolol, hydrochlorothiazide, acetazolamide, doxycycline, ethanol, alpelisib

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications for autoimmune oophoritis, and the likely driver is the shared autoimmune link with type 1 diabetes. In addition, all six US licenses are cancelled, and the package insert safety data have not been retrieved.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are blocking for safety screening
- Detailed mechanism of action data (MOA)
- Preclinical or clinical evidence that insulin glargine affects ovarian autoimmune pathology
- Clarification of the current US regulatory status, since all six licenses are cancelled

## Other Predicted Indications (Reference)

The other top predictions are also computational only and are on Hold. None has clinical trial support.

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Thiamine-responsive dysfunction syndrome | 99.61% | L5 | Insulin treats only the diabetic component, already covered by the standard indication |
| 3 | Focal stiff limb syndrome | 99.60% | L5 | Shared anti-GAD autoimmunity with type 1 diabetes, not a therapeutic mechanism |
| 4 | Classic stiff person syndrome | 99.60% | L5 | Insulin would address only coexisting diabetes |
| 5 | Opsismodysplasia | 99.59% | L5 | Plausible link through INPPL1 (SHIP2) in insulin signaling, hypothesis only |
| 6 | Pancreatic agenesis | 99.43% | L4 | Insulin replacement is standard care, so this is not true repurposing; the 4 publications found are indirect |
| 7 | Drug-induced localized lipodystrophy | 99.42% | L5 | Insulin injection can cause this condition, so the prediction is likely a false positive |
| 8 | Centrifugal lipodystrophy | 99.39% | L5 | Speculative, no evidence |
| 9 | Pressure-induced localized lipoatrophy | 99.38% | L5 | Insulin can itself cause lipoatrophy |
| 10 | Idiopathic localized lipodystrophy | 99.34% | L5 | No mechanism or evidence |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


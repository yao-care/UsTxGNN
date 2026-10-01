---
layout: default
title: Insulin Human
parent: Model Prediction Only (L5)
nav_order: 801
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Insulin Human: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin human is a marketed recombinant hormone replacement therapy, used mainly for glycemic control in diabetes.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on model output alone, and no plausible mechanism has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (the license records in the Evidence Pack contain no indication text) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (BLA licenses) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Insulin human is exogenous insulin, a replacement hormone whose efficacy in diabetes is well established. The Evidence Pack contains no MOA record for it.

Autoimmune oophoritis is an autoimmune disorder of the ovary. Exogenous insulin has no documented mechanism in this condition. The high score most likely reflects graph proximity through shared autoimmune or endocrine nodes, not a therapeutic relationship.

This prediction should therefore be treated as a weak, model-generated hypothesis. Without a mechanistic link, direct evidence or any registered study, it is not a credible repurposing candidate for now.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA018780 | HUMULIN R | Injection, solution | A-S Medication Solutions |
| BLA019959 | Novolin | Injection, suspension | A-S Medication Solutions |
| BLA018780 | Humulin | Injection, solution | Eli Lilly and Company |
| BLA018781 | Humulin | Injection, suspension | Eli Lilly and Company |
| BLA019717 | Humulin | Injection, suspension | Eli Lilly and Company |

The list shows 5 of 20 licenses. Available dosage forms are injectable solution and suspension, plus a metered powder form.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature and no documented mechanism for insulin in autoimmune oophoritis. The data gaps in the package insert warnings and MOA also block safety screening.

Across the top 10 predictions, only pancreatic agenesis reached the S1 stage. There, insulin replacement is physiologically rational, but disease-specific evidence is still needed. Two lipodystrophy-related predictions (drug-induced localized lipodystrophy and pressure-induced localized lipoatrophy) more likely reflect insulin's known injection-site adverse effects than a therapeutic use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking data gap)
- Mechanism of action data, e.g. from DrugBank
- A literature search for any link between insulin, or glycemic and metabolic dysregulation, and autoimmune oophoritis
- A rationale for why insulin would act on an autoimmune ovarian process, before any further evaluation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Insulin Glargine
parent: Model Prediction Only (L5)
nav_order: 799
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin analog, used to control blood glucose in diabetes mellitus.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (basal insulin analog; label indication text was not included in the data provided) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (all listed entries are BLAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin glargine is a basal insulin analog, its efficacy in glycemic control is well established, and it has no known immunomodulatory action.

Autoimmune oophoritis is an immune-mediated ovarian disorder. No mechanism explains how a basal insulin would treat it. The high score (0.9988) most likely reflects proximity in the knowledge graph, such as polyglandular autoimmunity that co-occurs with type 1 diabetes. It probably does not reflect a therapeutic effect.

Among the other top-10 predictions, most also look like association artifacts. Examples are stiff person spectrum disorders (anti-GAD autoimmunity with comorbid diabetes) and localized lipodystrophies (a known adverse effect of injected insulin). The most mechanistically coherent one is pancreatic agenesis, where insulin is standard replacement therapy for the resulting diabetes. That is supportive care, not a new mechanism, and no glargine-specific evidence was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| BLA761201 | SEMGLEE | Injection, solution | Biocon Biologics Inc. |
| BLA021081 | Lantus Solostar | Injection, solution | sanofi-aventis U.S. LLC |
| BLA021081 | Lantus | Injection, solution | sanofi-aventis U.S. LLC |
| BLA761201 | Insulin Glargine | Injection, solution | Biocon Biologics Inc. |
| BLA021081 | Lantus | Injection, solution | A-S Medication Solutions |

All marketed forms are injectable. Route compatibility with the predicted indication has not been assessed.

---

## Safety Considerations

Please refer to the package insert for safety information.

One signal from the predictions is worth noting. Injected insulin is a recognized cause of localized lipohypertrophy and, less commonly, lipoatrophy at injection sites.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There is no trial or literature support, and no plausible mechanism links basal insulin to an autoimmune ovarian disorder. The score more likely reflects autoimmune and endocrine co-occurrence.

**To proceed, the following is needed:**
- Mechanism of action data and the package insert warnings and contraindications
- Any clinical or preclinical evidence for insulin glargine in autoimmune oophoritis
- If pursuing this drug further, review pancreatic agenesis as a supportive-care research question rather than autoimmune oophoritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


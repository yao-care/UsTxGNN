---
layout: default
title: Pentosan Polysulfate
parent: Model Prediction Only (L5)
nav_order: 1029
evidence_level: L5
indication_count: 3
---

# Pentosan Polysulfate
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

# Pentosan Polysulfate: From a Marketed Oral Capsule (ELMIRON) to Primary Release Disorder of Platelets

## One-Sentence Summary

Pentosan polysulfate is a heparin-like sulfated polysaccharide, currently marketed in the US as an oral capsule (ELMIRON).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, with a very high score.
**No clinical trials and no publications** currently support this prediction, and the drug's known anticoagulant effects point in the opposite direction.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, pentosan polysulfate is a heparin-like sulfated polysaccharide with weak anticoagulant and fibrinolytic activity.

A platelet secretion (release) defect is a bleeding disorder. An anticoagulant-like drug with bleeding risk would be expected to worsen it, not treat it. The high TxGNN score most likely reflects shared coagulation and platelet network neighbors in the knowledge graph, not a plausible therapeutic mechanism. Without original MOA data, the link cannot be validated mechanistically.

The two next-ranked predictions show the same pattern:

| Rank | Predicted Indication | TxGNN Score | Concern |
|------|------|------|------|
| 2 | Glanzmann thrombasthenia | 99.65% | This is an integrin alpha-IIb/beta-3 (GPIIb/IIIa) deficiency that impairs platelet aggregation. The drug has no known restorative effect on this receptor, and its anticoagulant properties would be expected to worsen bleeding. |
| 3 | Pseudo-von Willebrand disease | 99.62% | This is a gain-of-function GPIbα defect. The drug has no established action on the GPIb-VWF axis, and its anticoagulant effect would add to bleeding risk. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020193 | ELMIRON | Capsule, gelatin coated (oral) | Janssen Pharmaceuticals, Inc. |

## Safety Considerations

Please refer to the package insert for safety information.

Because pentosan polysulfate has heparin-like anticoagulant activity, bleeding risk is a central concern for any bleeding-disorder indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (Evidence Level L5). The drug's known anticoagulant, bleeding-prone profile runs counter to treating platelet function disorders. The same holds for the other two top-ranked predictions.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) and a plausible mechanistic rationale for platelet function disorders
- Package insert warnings and contraindications, which are required for safety screening
- Preclinical or mechanistic studies showing a benefit, or at least no harm, in platelet function models
- Route compatibility assessment (currently pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Orlistat
parent: Model Prediction Only (L5)
nav_order: 996
evidence_level: L5
indication_count: 1
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
last_modified_at: 2026-10-14
description: "Orlistat: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder"
---

# Orlistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Orlistat: From Obesity to Hypervitaminosis

## One-Sentence Summary

Orlistat is a lipase inhibitor originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction is based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, orlistat is a gastric and pancreatic lipase inhibitor that reduces dietary fat absorption by roughly 30%.

Fat-soluble vitamins (A, D, E, K) are absorbed together with dietary fat, so reduced fat absorption could in theory lower their uptake. This gives a plausible but purely theoretical rationale for fat-soluble vitamin excess.

There are important limits to this reasoning:
- Lowering vitamin absorption is generally regarded as an **adverse effect** of orlistat (risk of vitamin deficiency), not a therapeutic benefit.
- It would not apply to excess of water-soluble vitamins.
- It would not address excess from non-dietary sources, such as injected or supplemental vitamins.
- The very high TxGNN score (99.42%) is a computational prediction only and is not backed by clinical or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020766 | ORLISTAT (H2-Pharma LLC) | Capsule | Not listed; status: cancelled |
| NDA021887 | ALLI (Aphena Pharma Solutions - Tennessee, LLC) | Capsule | Not listed; status: cancelled |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease relationships in the TxGNN knowledge graph, not from label text): liver failure, primary hyperoxaluria, anorexia nervosa, bulimia nervosa, vitamin deficiency disorder, cholestasis, benign recurrent intrahepatic cholestasis, familial intrahepatic cholestasis, drug-induced liver injury.
  - Vitamin deficiency disorder is especially relevant here, because the proposed use depends on lowering vitamin absorption.
- **Drug Interactions**: 100 interactions were found in total. The first 20 returned are mostly Moderate, with a few Minor. Examples:
  - Moderate: abacavir, lamivudine, emtricitabine, atazanavir, acarbose, albiglutide, alogliptin, canagliflozin, metformin, chlorpropamide, amiodarone, cannabidiol, asparaginase products, brentuximab vedotin, calaspargase pegol, clofarabine
  - Minor: cholecalciferol, calcifediol, calcitriol

For package-insert warnings, please refer to the official label.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or literature (Evidence Level L5). The proposed mechanism, reduced fat-soluble vitamin absorption, is a known adverse effect of orlistat rather than an established benefit. Both US authorizations are cancelled.

**To proceed, the following is needed:**
- Clinical or literature evidence for orlistat in fat-soluble vitamin excess
- Detailed mechanism of action data
- FDA package insert warnings and contraindications
- Assessment of whether lowering vitamin absorption can be done safely, given the contraindication for vitamin deficiency disorder
- Clarification of the regulatory pathway, since no US authorizations are currently valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Orlistat
parent: Model Prediction Only (L5)
nav_order: 996
evidence_level: L5
indication_count: 1
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Orlistat: From Obesity to Hypervitaminosis

## One-Sentence Summary

Orlistat is an oral lipase inhibitor sold as Xenical and alli, a drug for weight management. The indication text is not included in the supplied licence records.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity / weight management (the licence records supplied contain no indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 licence entries (2 distinct NDA numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Orlistat is a reversible inhibitor of gastric and pancreatic lipases. It reduces intestinal absorption of dietary fat by about 30%. Fat-soluble vitamins (A, D, E, K) are absorbed together with dietary fat, so orlistat also lowers their absorption. This is a known adverse effect that can cause vitamin deficiency, and labeling recommends multivitamin supplementation.

In theory, less absorption could limit further accumulation in hypervitaminosis from fat-soluble vitamins, mainly A and D. This link is speculative, for three reasons:
- Toxicity usually comes from excess supplementation, and the standard fix is to stop the source.
- Vitamin already stored in liver and adipose tissue is not affected by blocking new absorption.
- The mechanism does not apply to excess of water-soluble vitamins.

The high TxGNN score is a knowledge-graph prediction only. Detailed mechanism-of-action data and original indications are not available in the DrugBank record, so the prediction cannot be cross-checked against a known mechanism. The score may reflect a graph association with vitamin absorption (an adverse effect) rather than a real therapeutic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020766 | ORLISTAT (H2-Pharma LLC) | Capsule | Not listed in supplied records |
| NDA020766 | Xenical (H2-Pharma LLC) | Capsule | Not listed in supplied records |
| NDA021887 | ALLI (Haleon US Holdings LLC) | Capsule | Not listed in supplied records |
| NDA021887 | ALLI (Aphena Pharma Solutions - Tennessee, LLC) | Capsule | Not listed in supplied records |

All products are oral capsules.

## Safety Considerations

Please refer to the package insert for safety information.

One point does follow from the mechanism. Orlistat reduces absorption of fat-soluble vitamins (A, D, E, K), so the drug can itself cause vitamin deficiency. This runs against using it in patients who are otherwise at risk of deficiency.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no registered trials or publications. The proposed mechanism is speculative. Stopping the vitamin source already addresses the cause, and orlistat does not clear vitamin already stored in the body.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank to allow proper mechanistic cross-checking
- Preclinical or observational data showing that reduced fat-soluble vitamin absorption changes vitamin levels or outcomes in hypervitaminosis
- Comparison against standard management (stopping supplementation, supportive care) to define any realistic added benefit

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


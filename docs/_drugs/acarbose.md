---
layout: default
title: Acarbose
parent: Model Prediction Only (L5)
nav_order: 63
evidence_level: L5
indication_count: 9
---

# Acarbose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Acarbose: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Acarbose is an intestinal alpha-glucosidase inhibitor that lowers postprandial blood glucose, and it is marketed in the US as oral tablets.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied US license records; acarbose is an alpha-glucosidase inhibitor that lowers postprandial glucose (type 2 diabetes) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 17 (all listed licenses are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Acarbose is known to inhibit intestinal alpha-glucosidase, which slows carbohydrate digestion and blunts the rise in blood glucose after meals.

Stiff person syndrome is an autoimmune neurological disorder, typically involving anti-GAD antibodies and disrupted GABAergic signalling. No plausible mechanistic link to alpha-glucosidase inhibition was found in the supplied data. The high score is most likely a knowledge-graph artifact, for example the known association between stiff person syndrome and diabetes.

The same pattern applies to the other high-scoring predictions, which are also L5 with no trials or literature:
- Focal stiff limb syndrome: a stiff person spectrum variant, same reasoning.
- Thiamine-responsive dysfunction syndrome: at most indirect glycemic control, with no effect on the underlying transporter defect.
- Opsismodysplasia: a rare skeletal dysplasia with no evident connection.
- Localized lipodystrophies (drug-induced, centrifugal, pressure-induced, idiopathic): no known effect of acarbose on adipose tissue.
- Pancreatic agenesis (rank 9): the only prediction with retrieved literature (L4), but the papers concern type 2 diabetes, insulin autoimmune syndrome and animal models rather than pancreatic agenesis itself. Insulin remains the required therapy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

17 licenses are recorded. All are tablets, and the main distinct ones are listed below. Approved indication text was not included in the supplied records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA090912 | Acarbose | Tablet | Strides Pharma Science Limited |
| ANDA202271 | Acarbose | Tablet | Chartwell RX, LLC |
| ANDA202271 | Acarbose | Tablet | Bryant Ranch Prepack |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for acarbose in the supplied data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and no plausible mechanism linking alpha-glucosidase inhibition to stiff person syndrome. It is most likely a knowledge-graph artifact, so it does not justify further investment.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting acarbose to anti-GAD autoimmunity or GABAergic pathways
- Any preclinical or clinical signal specific to stiff person syndrome
- Package insert warnings, contraindications and approved indication text (the safety screening stage cannot proceed without them)
- Detailed mechanism of action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


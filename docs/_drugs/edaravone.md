---
layout: default
title: Edaravone
parent: Model Prediction Only (L5)
nav_order: 641
evidence_level: L5
indication_count: 2
monitor_inn: "EDARAVONE"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis"]
last_modified_at: 2026-10-30
description: "Edaravone: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Edaravone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Edaravone: Heparin cofactor 2 deficiency
{: .text-alpha }

## One-Sentence Summary

Edaravone is a free radical scavenger originally used to treat acute ischemic stroke and amyotrophic lateral sclerosis (ALS).
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 0.9947 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 4) |
| Number of FDA Applications | 4 (valid: 2) |
| Recommended Decision | Hold |

A second prediction, **factor 5 excess with spontaneous thrombosis** (score 0.9906), was also generated. It likewise has no supporting trials or literature and is discussed briefly below.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, edaravone is a free radical scavenger. In ischemic stroke and ALS, it is thought to reduce oxidative stress and endothelial injury.

Heparin cofactor 2 deficiency is a hereditary thrombophilia in which thrombin inhibition (dependent on dermatan sulfate) is reduced. A possible, but unproven, link is that antioxidant and endothelial-protective effects could limit vascular injury associated with thrombosis.

This link is weak. Edaravone does not act on the heparin cofactor 2 / thrombin axis, and no direct mechanistic or clinical data connect the two. The same applies to factor 5 excess with spontaneous thrombosis, a disorder driven by increased coagulation cascade activity (prothrombinase activity), which edaravone is not known to modulate. The high TxGNN scores should be read as computational predictions only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209176 | RADICAVA | Injection | Not listed (valid) |
| ANDA217565 | Edaravone (XGen Pharmaceuticals DJB) | Injection, solution | Not listed (valid) |
| ANDA216199 | Edaravone (Gland Pharma) | Injection, solution | Not listed (valid) |
| ANDA216902 | Edaravone (Sandoz) | Injection | Not listed (valid) |

All four authorizations are injectable products and all are currently cancelled.

## Safety Considerations

No drug-drug interaction records were found, and no contraindication edges were identified in the knowledge graph.

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (0.9947), with no clinical trials, no publications, and no direct mechanistic link between edaravone and the heparin cofactor 2 / thrombin axis. In addition, the drug is marketed in the US with all 4 of 4 authorizations valid, and package insert safety data could not be obtained.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (obtained from the FDA website) to allow safety screening
- Detailed mechanism of action data (e.g., from DrugBank)
- Preclinical or mechanistic studies testing whether edaravone's antioxidant effects influence thrombosis in heparin cofactor 2 deficiency
- Clarification of the reasons for the cancelled US authorizations and the current availability of injectable products
- A route-compatibility assessment for the proposed new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


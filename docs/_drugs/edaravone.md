---
layout: default
title: Edaravone
parent: Model Prediction Only (L5)
nav_order: 641
evidence_level: L5
indication_count: 2
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Edaravone: From Amyotrophic Lateral Sclerosis to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Edaravone is a free radical scavenger, marketed in the US as an injection for amyotrophic lateral sclerosis (ALS) and acute ischemic stroke.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amyotrophic lateral sclerosis (the license indication text is blank in the record; ALS comes from the model's rationale notes) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 (includes ANDA generic authorizations) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, edaravone is an antioxidant free radical scavenger with endothelial-protective effects. Its efficacy has been established in ALS and acute ischemic stroke, so it might reduce oxidative endothelial injury.

Heparin cofactor 2 deficiency is a hereditary serpin deficiency. It impairs thrombin inhibition, mainly the dermatan sulfate-dependent pathway, and increases thrombotic risk. Edaravone's antioxidant activity could plausibly limit oxidative damage during thrombotic events. However, it would not correct the underlying coagulation-inhibitor deficiency, and no direct mechanistic link is established. The high model score (0.995) is a knowledge-graph output, not clinical evidence.

The model also ranks a second prediction, factor 5 excess with spontaneous thrombosis (score 99.06%). It has the same limitation: edaravone has no known action on factor V or the coagulation cascade, and no trials or literature were found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209176 | RADICAVA (Tanabe Pharma America) | Injection | Not listed in the record |
| ANDA217565 | Edaravone (XGen Pharmaceuticals DJB) | Injection, solution | Not listed in the record |
| ANDA216199 | Edaravone (Gland Pharma) | Injection, solution | Not listed in the record |

The record shows 7 authorizations in total. Only 5 entries are listed, and they cover just these 3 unique numbers, since two are duplicated.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (L5). The proposed mechanism is indirect, because an antioxidant would not correct a serpin deficiency. Package insert safety data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search on edaravone in thrombosis, coagulation disorders, and endothelial protection
- Preclinical evidence for an effect on the heparin cofactor II or dermatan sulfate pathway
- Route compatibility check (edaravone is injection only; the required route is not yet defined)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


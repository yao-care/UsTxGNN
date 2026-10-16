---
layout: default
title: Pentosan Polysulfate
parent: Model Prediction Only (L5)
nav_order: 1029
evidence_level: L5
indication_count: 3
monitor_inn: "PENTOSAN POLYSULFATE"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease"]
last_modified_at: 2026-10-14
description: "Pentosan Polysulfate: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Interstitial cystitis"
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

# Pentosan Polysulfate: From Interstitial Cystitis to Primary Release Disorder of Platelets

## One-Sentence Summary

Pentosan polysulfate is a semi-synthetic sulfated polysaccharide, originally used to treat interstitial cystitis.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this direction.
The prediction is computational only and, on mechanistic grounds, raises a safety concern.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Interstitial cystitis |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pentosan polysulfate is a semi-synthetic sulfated polysaccharide with heparin-like, weak anticoagulant activity and effects on coagulation and fibrinolysis. Its efficacy in interstitial cystitis is the basis of its original use.

The link to the predicted indication is purely computational. A drug acting on coagulation and fibrinolysis could plausibly touch platelet or hemostatic pathways. However, its anticoagulant activity would more likely worsen bleeding tendency in a platelet function disorder than treat it. The high score may reflect network proximity to hemostasis-related genes rather than a true therapeutic rationale.

The same pattern appears in the other top predictions:
- **Glanzmann thrombasthenia** (score 99.65%): caused by deficiency or dysfunction of integrin alphaIIb-beta3, which impairs platelet aggregation. Pentosan polysulfate has no known action that restores this receptor.
- **Pseudo-von Willebrand disease** (score 99.62%): a gain-of-function defect in platelet GPIb-alpha. A theoretical interaction with glycosaminoglycan-binding or VWF-related pathways exists, but there is no evidence of benefit.

All three predictions are likely graph-proximity artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020193 | ELMIRON (Janssen Pharmaceuticals, Inc.) | Capsule, gelatin coated (oral) | Not listed in the data (status: cancelled) |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: liver disease, gallbladder disease, thrombocytopenia, blood coagulation disease, hemophilia, and heparin-induced thrombocytopenia. These overlap strongly with the predicted bleeding and platelet disorders, so the proposed use is in direct tension with them.
- **Drug Interactions**: 58 interactions were identified, and the 20 listed in the data are all rated Moderate. Most involve agents that affect bleeding or clotting, which fits the drug's anticoagulant-like properties:
  - Antiplatelet agents: acetylsalicylic acid, clopidogrel, cilostazol, dipyridamole, abciximab, cangrelor
  - Anticoagulants: warfarin, apixaban, edoxaban, betrixaban, dalteparin, bivalirudin, antithrombin III
  - Thrombolytics and related agents: alteplase, anistreplase, defibrotide, caplacizumab
  - Radiolabelled antibodies: ibritumomab tiuxetan, tositumomab (including I-131)

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or literature. The drug's anticoagulant-like activity and the knowledge-graph contraindications (coagulation disease, hemophilia, thrombocytopenia) suggest a risk of worsening bleeding rather than benefit. The only US license is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are a blocking gap for safety screening
- Detailed mechanism of action data
- Preclinical or mechanistic evidence that the drug affects platelet release or function in a beneficial direction
- A bleeding-risk assessment for patients with platelet function disorders
- Clarification of regulatory and route-of-administration feasibility, given the cancelled license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


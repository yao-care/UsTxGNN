---
layout: default
title: Andexanet Alfa
parent: Model Prediction Only (L5)
nav_order: 349
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Andexanet Alfa: From Factor Xa Inhibitor Reversal to Glanzmann Thrombasthenia

## One-Sentence Summary

Andexanet alfa is a recombinant antidote used to reverse the anticoagulant effect of factor Xa inhibitors. The TxGNN model predicts it may be effective for **Glanzmann thrombasthenia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone and has no plausible mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reversal of factor Xa inhibitor anticoagulation (inferred from the mechanism; the approved indication text was not provided in the licence record) |
| Predicted New Indication | Glanzmann thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125586) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Andexanet alfa is a recombinant, catalytically inactive factor Xa decoy. It binds direct and indirect FXa inhibitors and neutralises their anticoagulant effect. Its only established action is to reverse FXa inhibition.

Glanzmann thrombasthenia is an inherited bleeding disorder caused by absent or dysfunctional platelet integrin αIIbβ3, which impairs platelet aggregation. Andexanet alfa does not act on this receptor or on platelet aggregation. Its high TxGNN score (0.998; model rank 6,290) is a graph-based association only. **There is no plausible mechanistic link**, and the prediction should be treated as a likely model artefact.

The other three predicted indications have the same problem:

- **Primary release disorder of platelets:** a granule-release defect, unrelated to FXa-inhibitor reversal.
- **Pseudo-von Willebrand disease:** involves enhanced GPIbα–VWF binding, which andexanet does not affect.
- **Hemophilia:** the link is weak and directionally questionable. Hemophilia is a deficiency of FVIII or FIX, and neutralising FXa inhibitors would not replace the missing factors.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Glanzmann thrombasthenia.

For hemophilia (the fourth-ranked prediction), 11 publications were retrieved. All are reviews, guidelines, laboratory studies or subanalyses. They concern DOAC reversal or DOAC interference with FVIII/FIX assays, and none tests andexanet alfa as a treatment for hemophilia. They do not support the prediction.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125586 | ANDEXXA | Injection, powder, lyophilized, for solution | AstraZeneca Pharmaceuticals LP |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no registered trials and no supporting literature. Andexanet alfa acts only on FXa inhibitors and has no effect on platelet integrin αIIbβ3, so the mechanism does not fit Glanzmann thrombasthenia. The same holds for the other three predicted platelet and bleeding disorders.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications, to complete safety screening
- A documented mechanistic rationale, if any exists, for how an FXa decoy could affect platelet function
- Preclinical evidence, such as platelet aggregation studies in Glanzmann models, before any further evaluation
- The approved indication text for BLA125586, to complete the licence record

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


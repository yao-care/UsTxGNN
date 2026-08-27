---
layout: default
title: Enoxaparin
parent: 僅模型預測 (L5)
nav_order: 654
evidence_level: L5
indication_count: 1
---

# Enoxaparin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Enoxaparin: From Venous Thromboembolism Prevention to Thrombophilia (Protein C Deficiency)

## One-Sentence Summary

> Enoxaparin is a low-molecular-weight heparin (LMWH) globally used for venous thromboembolism (VTE) prophylaxis and treatment; Taiwan-specific approved-indication data is unavailable because the product is not currently marketed here.
> The TxGNN model predicts it may be effective for **Thrombophilia due to Protein C Deficiency, Autosomal Recessive**,
> but this signal is currently **model-only**, with **no supporting clinical trials or published literature** identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Venous thromboembolism prophylaxis/treatment (general drug-class knowledge; no Taiwan license record exists — product unmarketed) |
| Predicted New Indication | Thrombophilia due to Protein C Deficiency, Autosomal Recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap DG002). Based on general pharmacological knowledge, enoxaparin is a low-molecular-weight heparin that binds antithrombin III and potentiates its inhibition of Factor Xa (and, to a lesser extent, thrombin), producing an anticoagulant effect. Its established use is prevention and treatment of venous thromboembolic disease.

Protein C deficiency is a hereditary thrombophilia in which reduced natural anticoagulant activity predisposes patients to recurrent venous thrombosis. Anticoagulants such as enoxaparin are already used clinically to manage acute thrombotic events and bridging therapy in patients with known thrombophilias, including protein C deficiency — so a mechanistic link between an anticoagulant and a hypercoagulable hereditary disorder is biologically plausible.

That said, this plausibility is based on general anticoagulant pharmacology rather than on any disease-specific study captured in this evidence pack. The TxGNN score is high, but with zero clinical trials and zero literature returned for this drug-disease pair, the prediction currently stands as an unvalidated model signal rather than an evidence-backed indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are not currently available; TFDA label information is a Blocking data gap — DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high TxGNN model score, with no corroborating clinical trials or literature, and a Blocking data gap on TFDA label/warning information prevents even an initial safety screen (S1). The drug is also not currently marketed in Taiwan (0 licenses).

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications (resolve DG001 — blocking)
- Confirmed mechanism of action detail (resolve DG002)
- Targeted literature/clinical trial search specifically for enoxaparin in protein C deficiency-related thrombophilia
- Taiwan-specific approved indication and licensing status, given the product is currently unmarketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


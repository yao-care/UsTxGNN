---
layout: default
title: Potassium Nitrate
parent: 僅模型預測 (L5)
nav_order: 1071
evidence_level: L5
indication_count: 2
---

# Potassium Nitrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Potassium Nitrate: From Unspecified Indication to Meningococcal Infection

## One-Sentence Summary

Potassium Nitrate (DB11090) has no recorded original indication or market authorization in the data reviewed, and no mechanism-of-action data is currently available.
The TxGNN model predicts a possible link to **Meningococcal Infection**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No original indication on record; drug is not currently marketed in the reviewed jurisdiction |
| Predicted New Indication | Meningococcal Infection |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Potassium Nitrate. The evidence pack notes only a theoretical pathway: nitrate ions from KNO₃ can be reduced by oral/gut microbiota to nitrite and nitric oxide (NO), and NO has some documented antimicrobial and immunomodulatory activity. On this basis, TxGNN's knowledge graph has drawn a high-scoring link between potassium nitrate and meningococcal infection.

However, this mechanistic link is explicitly assessed as weak and speculative in the source data. Meningococcal infection is an acute, life-threatening bacterial disease requiring rapid, high-potency bactericidal/bacteriostatic activity and predictable pharmacokinetics. There is no known antimicrobial spectrum data showing potassium nitrate has direct activity against *Neisseria meningitidis*, and no in vitro or in vivo evidence supports this connection. This is a pure knowledge-graph association, not a mechanistically or clinically substantiated hypothesis.

A second candidate indication was also flagged by the model — sclerosing cholangitis (score 99.21%, rank 17307) — via a similarly speculative nitrate–nitrite–NO pathway affecting biliary endothelium and fibrosis signaling. Like the primary candidate, this link has no supporting mechanistic, preclinical, or clinical data and should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No approved marketing authorizations were found for Potassium Nitrate in the reviewed jurisdiction (0 licenses on record; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA labeling/warnings and contraindication data are currently a blocking data gap — see remediation below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications rest on Evidence Level L5 (model prediction only, no clinical trials, no literature, no preclinical data), and the underlying mechanistic rationale is explicitly characterized as weak/speculative in the evidence pack itself. Combined with the absence of any market authorization, mechanism-of-action data, or safety labeling, there is currently no basis to advance either candidate beyond initial screening.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (blocking gap — DG001)
- Verified mechanism of action for potassium nitrate (DG002)
- In vitro/in vivo evidence of antimicrobial activity against *N. meningitidis*, or mechanistic studies on nitrate/NO signaling in biliary fibrosis (for the sclerosing cholangitis candidate)
- Confirmation of original approved indication(s) and any historical market data, since none are currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


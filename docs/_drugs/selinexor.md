---
layout: default
title: Selinexor
parent: 僅模型預測 (L5)
nav_order: 1152
evidence_level: L5
indication_count: 1
---

# Selinexor
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

# Selinexor: From Multiple Myeloma to Drug-Induced Osteoporosis

## One-Sentence Summary

> Selinexor is a selective inhibitor of nuclear export (SINE) approved internationally for multiple myeloma and diffuse large B-cell lymphoma.
> The TxGNN model predicts a possible association with **Drug-Induced Osteoporosis**,
> but this prediction is currently **not supported by any clinical trials or published literature** — it is a model-only inference.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no licensed indications recorded; drug is not marketed in Taiwan) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed in Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known public pharmacology, selinexor is a selective inhibitor of nuclear export (SINE) that targets XPO1/CRM1, and is approved internationally for multiple myeloma and diffuse large B-cell lymphoma. By blocking XPO1-mediated nuclear export, selinexor forces retention of tumor suppressor proteins and disrupts NF-κB signaling in malignant cells.

The proposed link to drug-induced osteoporosis is purely theoretical: osteoclast differentiation (osteoclastogenesis) partly depends on NF-κB activation, so XPO1 inhibition could plausibly interfere with this pathway. However, this is an indirect mechanistic inference, not an established pharmacological relationship. Importantly, selinexor's well-documented clinical side effects — anorexia, weight loss, and fatigue — could just as plausibly *worsen* bone loss through poor nutritional status, making the direction of any real-world effect on bone density uncertain.

No direct experimental or clinical evidence currently supports selinexor for treating or preventing drug-induced osteoporosis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Selinexor is not currently marketed in Taiwan (0 licenses on record). No NDA/license information is available.

---

## Cytotoxicity (Antineoplastic Drugs Only)

Selinexor is classified as an antineoplastic agent (approved for multiple myeloma / DLBCL) and is included here for reference, though its original indication text was not available in this Evidence Pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (XPO1/CRM1 selective inhibitor — SINE compound) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic/targeted anti-cancer drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on a theoretical mechanistic hypothesis (L5, model prediction only), with zero clinical trials or literature support, and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- Confirmed drug MOA data from DrugBank (currently flagged as a data gap, DG002)
- TFDA label warnings/contraindications (currently flagged as a blocking data gap, DG001 — required before any S1 safety review)
- Preclinical or mechanistic studies directly examining XPO1 inhibition and bone metabolism/osteoclastogenesis
- Real-world or trial-derived bone density/fracture data from existing selinexor oncology trials, if available
- Reassessment of net effect on bone health given selinexor's known anorexia/weight-loss adverse effect profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


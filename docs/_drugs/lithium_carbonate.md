---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 865
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Lithium Carbonate: From No Registered Indication to Pseudoachondroplasia

## One-Sentence Summary

Lithium carbonate (DrugBank DB14509) has no approved indication or licensed product on file in the available regulatory data, and detailed mechanism-of-action data is currently a gap. The TxGNN model's top prediction for this drug is **Pseudoachondroplasia**, with a prediction score of **99.98%**, but currently **0 clinical trials** and **0 publications** specifically support this candidate, and the underlying knowledge-graph signal may reflect score clustering rather than a disease-specific association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication or marketing license on file |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lithium carbonate is not available in the current dataset (data gap DG002, severity: High), and no approved indication or license record exists in this jurisdiction (market status: Not Marketed, 0 licenses on file). This significantly limits mechanistic and regulatory context for evaluating the prediction.

The repurposing rationale attached to this candidate anchors the prediction on lithium's known pharmacology as a **GSK-3β inhibitor / Wnt pathway modulator**. Pseudoachondroplasia is caused by COMP gene mutations leading to endoplasmic reticulum (ER) stress accumulation in chondrocytes. GSK-3/Wnt signaling is known to play a role in chondrocyte differentiation, but the evidence pack explicitly notes there is **no direct literature link** between this pathway and the ER-stress/protein-homeostasis mechanism underlying pseudoachondroplasia — the connection is inferential only.

Importantly, the evidence pack flags a specific caveat: within this prediction batch, multiple unrelated ultra-rare skeletal dysplasias received near-identical TxGNN scores (0.9998–0.9996), which raises the possibility that this is a **knowledge-graph structural clustering artifact** rather than a disease-specific signal. This should be weighed heavily when interpreting the score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorizations are on file for lithium carbonate in this jurisdiction — the drug is currently classified as **Not Marketed**, with 0 registered licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are currently gaps — DG001, severity: Blocking, required before any S1 safety assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by model score (L5) with no clinical trials or literature evidence, an inferential-only mechanistic link, and an explicit flag that the score may reflect knowledge-graph clustering across similar rare skeletal dysplasias rather than a true disease-specific signal.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap, DG001)
- Confirmed mechanism-of-action data for lithium carbonate (DG002)
- Independent verification of whether the near-identical top-10 scores in this batch represent real signal or a structural artifact of the knowledge graph
- Disease-specific pharmacological or preclinical evidence linking GSK-3/Wnt modulation to COMP-related ER stress in pseudoachondroplasia
- Basic regulatory/indication data for lithium carbonate itself, since none is currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


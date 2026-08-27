---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 820
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ivabradine: From Heart Rate Reduction (Heart Failure/Stable Angina) to Hypertrichosis

## One-Sentence Summary

Ivabradine is an HCN-channel (If current) inhibitor used to slow heart rate in heart failure and stable angina — note that Taiwan/US regulatory records for this drug are currently empty, so the original indication above is drawn from the evidence pack's own mechanistic notes, not a formal label. The TxGNN model's top prediction is **Hypertrichosis (disease)**, but this signal is supported by **0 clinical trials** and **0 publications** — it comes from embedding similarity alone, with the evidence pack explicitly noting no known receptor, pathway, or metabolic link between HCN-channel inhibition and hair overgrowth.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in regulatory data; per evidence notes, used for heart rate reduction in heart failure / stable angina |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Ivabradine is not available in this evidence pack (flagged as a High-severity data gap). The evidence pack's own rationale notes describe Ivabradine as a selective HCN-channel (If current) inhibitor acting on the sinoatrial node, used to reduce heart rate in heart failure and stable angina.

There is no known receptor, signaling pathway, or metabolic connection between this cardiac rate-control mechanism and hypertrichosis (excessive hair growth). The evidence pack explicitly states this prediction relies solely on TxGNN embedding similarity, with no mechanistic rationale identified.

The same pattern holds across all six ranked candidates in this evidence pack (hypertrichosis, Ambras syndrome, a dental/periodontal malformation syndrome, Dandy-Walker malformation syndrome, a hair-shaft abnormality, and nephrogenic SIAD) — each rationale independently concludes there is no plausible mechanistic link to Ivabradine's known pharmacology. The one candidate with literature hits (rank 3, dental/periodontal malformation) returned 20 papers on general periodontitis biology that do not mention Ivabradine or HCN channels, indicating a disease-ontology text match rather than drug-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No approved licenses were found for Ivabradine in the available US market data (market status: Not Marketed, 0 total licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on an L5, score-only TxGNN signal with zero supporting clinical trials or literature, and the evidence pack's own mechanistic analysis finds no plausible biological link between Ivabradine's HCN-channel/heart-rate mechanism and hypertrichosis. Combined with the drug's absent US market presence and missing MOA/safety data, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for Ivabradine (DrugBank query, currently a data gap)
- TFDA/FDA label warnings and contraindications (currently a Blocking data gap)
- Preclinical or in vitro evidence linking HCN-channel modulation to hair follicle biology
- Any real-world or case-report signal of hypertrichosis associated with Ivabradine use
- DDI data, which currently returns "not found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


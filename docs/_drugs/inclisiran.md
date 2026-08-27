---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 794
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: From Unknown Original Indication to Potassium Deficiency Disease

## One-Sentence Summary

> Inclisiran (DB14901) is a PCSK9-pathway siRNA therapeutic; its original approved indication is not documented in this evidence pack (drug is not currently marketed in Taiwan, no license records available).
> The TxGNN model's top-ranked prediction is **Potassium Deficiency Disease**, but this candidate has **0 clinical trials** and **0 publications** supporting it, and the evidence pack itself flags the prediction as likely embedding noise rather than a biologically plausible signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (drug not marketed in Taiwan; no license records) |
| Predicted New Indication | Potassium Deficiency Disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Market Status (Taiwan) | ✗ Not Marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for inclisiran is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the rationale text accompanying the predictions, inclisiran is known to act on the PCSK9 pathway affecting LDL receptor / lipid metabolism.

For this specific top-ranked prediction, the evidence pack's own analysis concludes the link is **not** mechanistically reasonable: there is no known interaction between the PCSK9 pathway and potassium homeostasis, and the high TxGNN score is assessed as likely reflecting knowledge-graph embedding noise rather than a real biological signal. No clinical trials or literature exist to support or refute this specific candidate.

It is worth noting that other lower-ranked candidates in this same evidence pack carry somewhat more supporting data — e.g., rank 7 ("migraine with or without aura, susceptibility to," L4, 20 publications, though all concern epilepsy/migraine genetic susceptibility rather than any drug intervention) and rank 8 ("aortic malformation," L2/S1, 2 Phase 3 inclisiran trials, though the disease-mapping accuracy is itself questioned in the pack). Neither of these is the subject of this report, but they may warrant separate evaluation given the top candidate's weak support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Inclisiran is not currently marketed in Taiwan; no license (NDA/許可證) records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label/warning data is flagged as a Blocking-severity data gap (DG001) — key warnings, contraindications, and DDI data could not be retrieved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top TxGNN prediction (Potassium Deficiency Disease) has zero clinical trial or literature support, no plausible mechanistic link, and is explicitly assessed in the evidence pack as likely model noise. This does not meet the bar for further investment at this time.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism of action data (currently high-severity gap — DG002)
- If pursuing repurposing further, re-evaluate the higher-evidence candidates in this pack (rank 7 and rank 8) rather than the top-ranked but mechanistically unsupported prediction, including verification of the disease-mapping accuracy for rank 8's clinical trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


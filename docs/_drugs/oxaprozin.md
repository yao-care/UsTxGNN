---
layout: default
title: Oxaprozin
parent: 僅模型預測 (L5)
nav_order: 1000
evidence_level: L5
indication_count: 10
---

# Oxaprozin
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

# Oxaprozin: From NSAID (Anti-Inflammatory/Analgesic Use) to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

> Oxaprozin is a nonsteroidal anti-inflammatory drug (NSAID); detailed original indication and mechanism-of-action records are not available in this evidence pack, and the drug is not currently marketed in Taiwan/US per the data on file.
> The TxGNN model predicts a possible link to **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare genetic skeletal disorder,
> but this prediction is supported by **0 clinical trials** and **0 publications** — the model's own rationale flags it as likely a false-positive knowledge graph association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no Taiwan/US license record; per embedded rationale text, oxaprozin is an NSAID with COX-1/COX-2 inhibitory, analgesic/anti-inflammatory activity) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.98% (global rank 1140) |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for oxaprozin in this evidence pack (flagged as a High-severity data gap, DG002). Based on the information embedded in the model's own rationale, oxaprozin is a conventional NSAID acting through COX-1/COX-2 inhibition to relieve pain and inflammation — the pharmacological basis typically applied to osteoarthritis, rheumatoid arthritis, and related joint disorders.

The top-ranked predicted indication, however, is Acromesomelic Dysplasia, Hunter-Thompson Type — a rare inherited skeletal dysplasia caused by GDF5 gene mutations, affecting limb development rather than active inflammation. The model's own repurposing rationale explicitly states there is **no biological mechanistic link** between NSAID pharmacology and this disorder, and attributes the high score to likely noise from generic "skeletal/joint" node connections in the knowledge graph rather than a genuine pharmacological signal.

Among the 10 predicted indications reviewed, only two (rank 5: spondyloarthropathy susceptibility; rank 9: RF-positive polyarticular juvenile idiopathic arthritis) retain a plausible NSAID-relevant mechanism — but both still lack any clinical trial or literature support and were also scored L5/Hold. The remaining candidates (ranks 1–4, 6, 8, 10) are rare monogenic skeletal/developmental syndromes with no inflammatory component, and rank 7 (rheumatoid nodulosis) has only weak theoretical plausibility. None currently clear even the earliest evidentiary bar for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Oxaprozin is not currently marketed in Taiwan/US per the records available (market status: 未上市; total licenses: 0). No NDA or license entries are on file to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available; the TFDA package insert lookup is flagged as a Blocking data gap, DG001, and must be resolved before any safety evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has a high TxGNN score but no clinical trial or literature support, and the model's own rationale identifies it as a likely false-positive/noise association with no biological plausibility. Combined with the drug's non-marketed status and missing MOA/safety data, there is currently no basis to advance any of the 10 predicted indications past initial screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — Blocking gap, required before any safety-stage (S1) evaluation
- Verified mechanism-of-action data via DrugBank API
- Independent literature/preclinical search specifically for the two mechanistically plausible candidates (spondyloarthropathy susceptibility, RF-positive polyarticular JIA), since none currently exists in this evidence pack
- Re-run TxGNN candidate screening with lower priority on rare monogenic skeletal syndromes lacking inflammatory pathophysiology, to reduce noise in future candidate lists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


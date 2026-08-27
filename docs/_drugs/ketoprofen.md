---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 826
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

# Ketoprofen: From NSAID Therapy to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a non-selective NSAID (propionic acid class, COX-1/COX-2 inhibitor) generally used for inflammatory pain conditions, though its specific original indication record is not available for this evidence pack. The TxGNN model's top-ranked prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, but this candidate is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the prediction as likely graph noise with no known mechanistic basis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no TFDA license record; drug is pharmacologically classified as a propionic acid NSAID / COX-1,2 inhibitor used for inflammatory pain) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ketoprofen is not directly available in this evidence pack ([Data Gap], DG002). What is known from the accompanying rationale text is that ketoprofen is a non-selective COX-1/COX-2 inhibitor of the propionic acid NSAID class, working through suppression of prostaglandin synthesis to achieve anti-inflammatory and analgesic effects.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare congenital skeletal dysplasia driven by disruption of BMP signaling (GDF5/CDMP1), not by an inflammatory or prostaglandin-mediated process. The evidence pack's own repurposing rationale explicitly states there is **no known mechanistic relationship** between NSAID/COX inhibition and this disorder, and characterizes the prediction as a "graph-noise-type" output — i.e., the TxGNN score is very high, but no pharmacological, clinical, or literature signal supports it.

Consequently, this specific prediction should not be interpreted as a validated repurposing hypothesis. It is worth noting that other candidates lower in this same prediction set carry more biological plausibility — for example, spondyloarthropathy susceptibility (rank 8, L3, supported literature) and LACC1-defect juvenile arthritis (rank 10, L4, inflammatory mechanism overlap) — both of which align with ketoprofen's known anti-inflammatory pharmacology and may be more productive directions for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Ketoprofen currently has no approved license record in Taiwan (0 licenses; market status: 未上市/Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction carries a very high TxGNN score but zero supporting clinical trials, zero literature, and no plausible mechanistic link — the evidence pack's own rationale identifies it as likely model noise (Evidence Level L5). Combined with the drug's absence from the Taiwan market (0 licenses) and a Blocking data gap on TFDA labeling/contraindication data (DG001), there is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap (DG001), required before any safety-stage (S1) review
- Mechanism of action (MOA) data via DrugBank — currently a High-severity data gap (DG002)
- If pursuing ketoprofen repurposing further, prioritize the higher-evidence candidates in this prediction set instead — spondyloarthropathy susceptibility (rank 8, L3, literature-supported) and LACC1-defect juvenile arthritis (rank 10, L4, mechanistically plausible) — rather than the rank-1 candidate evaluated here
- Taiwan market/licensing status confirmation, given the drug is not currently marketed domestically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


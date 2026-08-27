---
layout: default
title: Metaxalone
parent: 僅模型預測 (L5)
nav_order: 903
evidence_level: L5
indication_count: 3
---

# Metaxalone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Metaxalone: From Skeletal Muscle Relaxation to Infectious Otitis Media

## One-Sentence Summary

Metaxalone (DrugBank DB00660) is a centrally-acting skeletal muscle relaxant; its detailed original indication and mechanism of action are not documented in this evidence pack, and the drug is not currently marketed in Taiwan or the US.
The TxGNN model's top prediction is **Infectious Otitis Media** (score 99.06%), but this is supported by **zero clinical trials and zero publications**, and the evidence pack's own mechanistic analysis explicitly finds no biological rationale for the link — it flags the high score as a possible knowledge-graph hub-node artifact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no approved-indication text on file; drug is characterized only as a centrally-acting skeletal muscle relaxant) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for metaxalone in this evidence pack (marked as a blocking/high-severity data gap). Based on the limited information present, metaxalone is characterized as a centrally-acting skeletal muscle relaxant, with no documented antimicrobial, anti-inflammatory, or otologic pharmacological activity.

The relationship between "skeletal muscle relaxation" and "infectious otitis media" (a bacterial/infectious middle-ear condition) has no established pharmacological or clinical connection. The evidence pack's own repurposing rationale states this explicitly: there is no known mechanistic pathway linking metaxalone's CNS-depressant activity to infection control or middle-ear pathology, and the high TxGNN score may reflect a hub-node effect in the knowledge graph rather than a real biological relationship.

The same caveat applies to the two lower-ranked candidates (endocarditis, endocardial fibroelastosis) — both are cardiac/infectious conditions with no plausible mechanistic tie to a centrally-acting muscle relaxant. None of the three predictions in this pack are mechanistically supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Metaxalone is not currently marketed in Taiwan (0 licenses on file; market status: Not Marketed). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications (infectious otitis media, endocarditis, endocardial fibroelastosis) are L5 evidence — model prediction only, with zero supporting clinical trials or literature, and the pack's own mechanistic analysis finds no biological rationale for any of them. The drug is also unmarketed, and core safety/labeling data (TFDA warnings, contraindications, MOA) are flagged as blocking/high-severity data gaps.

**To proceed, the following is needed:**
- TFDA label / prescribing information (warnings, contraindications) — currently a blocking gap (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Independent mechanistic justification for any of the three candidate indications before further evidence collection is warranted
- If pursued, dedicated literature/clinical-trial searches specifically for metaxalone + otitis media, endocarditis, or endocardial fibroelastosis to check for signal beyond the current null result
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


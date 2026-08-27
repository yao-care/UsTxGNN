---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 784
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Ibuprofen: From Pain and Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely used NSAID for pain, inflammation, and fever. The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare autosomal-recessive skeletal disorder — but this is a **model-score-only prediction (L5)**, with **0 clinical trials** and **0 publications** currently supporting this direction, and the evidence pack's own mechanistic rationale states there is no known biological link between ibuprofen's mechanism and this disease's pathology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (no `original_indications` or license records available) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only) |
| Market Status (this jurisdiction) | Not marketed (0 licenses on file) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID) that inhibits cyclooxygenase (COX-1/COX-2), reducing prostaglandin synthesis to relieve pain, inflammation, and fever.

However, the mechanistic rationale supplied with this prediction explicitly undermines the biological case: Acromesomelic Dysplasia, Hunter-Thompson Type is caused by *GDF5* gene mutations that disrupt cartilage-formation signaling — a structural/developmental disorder, not an inflammatory one. The rationale states ibuprofen has "no direct mechanistic link to the disease-causing pathway," and could at most relieve secondary joint pain rather than modify the disease itself.

In other words, the high TxGNN score (99.74%) reflects graph-embedding similarity in the knowledge graph, not a validated pharmacological mechanism. This pattern repeats across all seven top-ranked candidates in this pack (brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, brachydactyly-syndactyly syndrome, pseudoachondroplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome) — all are rare genetic/structural skeletal or developmental disorders, and each rationale independently notes the absence of an inflammatory mechanism connecting them to ibuprofen.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Market Information

No license records found. Per the evidence pack, this drug is not currently marketed in this jurisdiction (0 approved licenses), so no product/dosage-form table can be produced.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: a Blocking-severity data gap exists — TFDA-equivalent label warnings/contraindications could not be retrieved, which by itself prevents this candidate from clearing the S1 safety-review stage regardless of efficacy evidence.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but evidence level is L5 (model output only) — no clinical trials, no literature, no mechanistic support (the pack's own rationale states the target disease pathology is non-inflammatory and structurally/genetically driven). Combined with a Blocking data gap on safety labeling and zero market licenses for this drug in this jurisdiction, there is no basis to advance past S0.

**To proceed, the following is needed:**
- Regulatory label data (warnings/contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action data — currently High severity gap (DG002)
- Original indication and licensing records for this drug in this jurisdiction
- Any preclinical or case-level evidence specifically linking NSAID/COX-inhibition to *GDF5*-pathway skeletal dysplasias, before this direction is pursued further

*All other top-7 predicted indications in this pack show the same profile (L5, no trials/literature, no mechanistic support, Hold recommendation) and are not expected to change this conclusion.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


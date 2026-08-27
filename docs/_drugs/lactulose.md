---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 829
evidence_level: L5
indication_count: 8
---

# Lactulose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Lactulose: From Unrecorded Original Indication to Acute Urate Nephropathy

## One-Sentence Summary

Lactulose (DrugBank DB00581) has no recorded original indication or Taiwan market license in this evidence pack — it is currently **未上市 (not marketed)** in Taiwan with zero approved licenses.
The TxGNN model's top-ranked prediction is **Acute Urate Nephropathy**, but this candidate has **zero clinical trials** and **zero publications** supporting it — it is a pure model-score prediction with no mechanistic or clinical backing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — evidence pack lists no original indications and no Taiwan license record |
| Predicted New Indication | Acute Urate Nephropathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lactulose in this evidence pack (flagged as a High-severity data gap, DG002), and no original indication is on record.

For the top-ranked prediction specifically, the evidence pack's own mechanistic assessment concludes there is **no known link**: lactulose does not affect urate metabolism or renal tubular urate crystal deposition. There is no pharmacological rationale connecting lactulose's known activity (as a non-absorbable disaccharide acting osmotically/on colonic flora) to acute urate nephropathy.

Combined with the complete absence of clinical trials or literature for this disease pairing, this prediction should be treated as knowledge-graph noise rather than a credible repurposing hypothesis at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

No licensed products found in the Taiwan regulatory database — lactulose is currently not marketed (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (acute urate nephropathy) has no clinical trials, no literature, and no plausible mechanistic link — it is a pure model-score artifact. Combined with a Blocking-severity data gap on TFDA labeling/warnings (DG001) and missing MOA data (DG002), there is currently no basis to advance this candidate past screening.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications (blocking gap, required before any safety pre-assessment)
- Confirmed mechanism of action data from DrugBank
- Confirmed original indication and licensing history for lactulose
- Independent mechanistic or preclinical rationale connecting lactulose to acute urate nephropathy before further investment

**Note:** This evidence pack also contains a considerably stronger candidate further down the ranked list — *obstructive jaundice* (rank 3, score 99.53%, Evidence Level L3) — supported by 1 completed Phase 4 trial and 20 publications, including a multicentre RCT (PMID 2032107) on lactulose preventing postoperative renal dysfunction in obstructive jaundice. If a repurposing candidate is desired from this evidence pack, that pairing warrants a separate, dedicated evaluation report rather than the top TxGNN score alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


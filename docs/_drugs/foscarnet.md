---
layout: default
title: Foscarnet
parent: 僅模型預測 (L5)
nav_order: 736
evidence_level: L5
indication_count: 4
---

# Foscarnet
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Foscarnet: From Antiviral Therapy to Autosomal Dominant Familial Hematuria–Retinal Arteriolar Tortuosity–Contractures Syndrome

## One-Sentence Summary

Foscarnet (DrugBank DB00529) is known — per the evidence pack's own rationale text — as a pyrophosphate analog antiviral active against CMV, HSV, and VZV; no formal original-indication or Taiwan license record is on file for this candidate. The TxGNN model predicts a possible link to **Autosomal Dominant Familial Hematuria–Retinal Arteriolar Tortuosity–Contractures Syndrome** with a **99.56%** prediction score, but this is supported by **zero clinical trials** and **zero publications** — a pure model signal with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no TFDA license record and `original_indications` is empty. Known antiviral use (CMV, HSV, VZV) referenced only in the rationale text, not a licensed indication |
| Predicted New Indication | Autosomal dominant familial hematuria–retinal arteriolar tortuosity–contractures syndrome |
| TxGNN Prediction Score | 99.56% (rank 10,857) |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for foscarnet is not available in this evidence pack — it is flagged as a High-severity data gap (DG002). Based on the rationale text carried alongside the prediction, foscarnet is a pyrophosphate analog that selectively inhibits viral DNA polymerase and reverse transcriptase, giving it activity against CMV, HSV, and VZV. This is an antiviral mechanism, not one associated with any genetic connective-tissue or vascular disorder.

The predicted new indication is a rare, COL4A1-related hereditary vascular collagenopathy. The evidence pack's own repurposing rationale explicitly states there is **no known mechanistic link** between foscarnet's antiviral activity and COL4A1-related vascular pathology. The 99.56% score reflects a pure knowledge-graph prediction signal and is not corroborated by any clinical trial or literature evidence — it should be treated as a hypothesis-generation output only, not a validated pharmacological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Foscarnet currently holds no license record on file (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No marketing-authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications are a **Blocking** data gap (DG001) — this must be resolved before any S1 safety screening can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has zero clinical trial or literature support and is driven purely by the TxGNN score (L5); the evidence pack's own rationale confirms no known mechanistic link exists. Combined with the absence of a Taiwan market license and a Blocking gap in MOA/label data, the candidate does not clear the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking — required before S1 safety screening)
- Confirmed mechanism of action (DG002, High — required for mechanistic plausibility review)
- Original approved indication(s) for foscarnet, to establish a repurposing baseline
- Independent literature or clinical evidence directly linking foscarnet to this indication, since the TxGNN score alone is insufficient to support advancement

**Note:** three additional TxGNN-predicted indications for foscarnet were also reviewed in this evidence pack — rheumatoid arthritis, diabetic nephropathy, and brain small vessel disease 1 with or without ocular anomalies. All three received the same **Hold** recommendation; retrieved trials/literature for each were keyword-mismatched (e.g., an unrelated brolucizumab/AMD trial, or CMV-treatment case reports mentioning foscarnet only incidentally) rather than substantive support for the stated indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


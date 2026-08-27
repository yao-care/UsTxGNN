---
layout: default
title: Givosiran
parent: 僅模型預測 (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: From Acute Hepatic Porphyria to Hepatoportal Sclerosis

## One-Sentence Summary

Givosiran (DrugBank DB15066) is a GalNAc-conjugated siRNA originally approved to prevent attacks of acute hepatic porphyria (AHP) by silencing hepatic ALAS1.
The TxGNN model's top-ranked prediction is **Hepatoportal Sclerosis**, with a score of 99.9986%,
but currently **0 clinical trials** and **0 publications** support this specific link — the evidence pack itself flags this as a likely knowledge-graph artifact rather than a genuine signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Hepatic Porphyria (AHP) — reconstructed from literature within this evidence pack (PMID 35991568, 36028858, 40312531); no structured TFDA/license indication text is available |
| Predicted New Indication | Hepatoportal sclerosis |
| TxGNN Prediction Score | 99.9986% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Market Status (Taiwan) | 未上市 (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Structured MOA data is unavailable (DG002, [Data Gap]). Based on the literature captured elsewhere in this evidence pack, givosiran is an RNA interference therapeutic that silences hepatic 5-aminolevulinic acid synthase 1 (ALAS1), the rate-limiting enzyme of heme biosynthesis. In acute hepatic porphyria, upregulated ALAS1 activity drives accumulation of the neurotoxic intermediates ALA and porphobilinogen, which trigger acute neurovisceral attacks; by knocking down ALAS1, givosiran reduces these intermediates and attack frequency.

For the top-ranked candidate, **hepatoportal sclerosis**, the evidence pack's own mechanistic assessment finds no plausible connection: this is a portal vascular/fibrotic disorder, not a disease of heme biosynthesis, and ALAS1 knockdown has no known relevance to portal vascular pathology. The pack explicitly attributes the near-1.0 TxGNN score to "liver disease" node clustering in the knowledge graph rather than causal or mechanistic evidence, and this assessment is corroborated by the complete absence of clinical trials or literature for this pairing.

Notably, among all 10 candidates evaluated for givosiran, the only one with any literature support is rank 9, "porphyria due to ALA dehydratase deficiency" (8 PMIDs, all directly about givosiran/AHP). However, this is a subtype within givosiran's already-approved AHP indication family rather than a novel repurposing opportunity, so it does not represent new-indication evidence either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Regulatory & Market Information (Taiwan)

Givosiran is not currently marketed in Taiwan (0 licenses on record); no NDA/license entries are available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. TFDA warnings and contraindications data (DG001) is flagged as a **Blocking** gap that prevents formal S1 safety review, and DDI query results were not found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication carries an extremely high TxGNN score but zero clinical or literature evidence, and the evidence pack's own mechanistic review judges it a likely knowledge-graph artifact rather than a real signal — this does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed original indication/MOA documentation from DrugBank or TFDA, rather than reconstruction from literature abstracts (DG002)
- Any preclinical or mechanistic study directly linking the ALAS1/heme pathway to portal-hepatic vascular disease, if this repurposing hypothesis is to be pursued further
- If AHP-adjacent indications remain of interest, re-scope the candidate to reflect that rank 9 ("porphyria due to ALA dehydratase deficiency") overlaps with givosiran's existing approved indication rather than representing a new therapeutic area
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


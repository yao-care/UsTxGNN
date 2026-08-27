---
layout: default
title: Glycerin
parent: 僅模型預測 (L5)
nav_order: 756
evidence_level: L5
indication_count: 10
---

# Glycerin
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

# GLYCERIN: From No Recorded Original Indication to Cauda Equina Syndrome

## One-Sentence Summary

Glycerin (DrugBank DB09462) has no original indication or mechanism-of-action data recorded in this evidence pack, and is not currently marketed in the reference regulatory database. The TxGNN model's top-ranked prediction is **Cauda Equina Syndrome**, but this prediction is supported by **zero clinical trials** and **zero publications** — it appears to be model noise rather than a substantiated repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record (drug not marketed; 0 licenses in database) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, no mechanism of action or original indication data is available for glycerin in this evidence pack, so no baseline pharmacology exists to anchor the prediction against.

More importantly, the evidence itself argues against this prediction. Cauda equina syndrome is an acute lumbosacral nerve root compression syndrome — a surgical emergency requiring urgent decompression. Glycerin's known pharmacology (osmotic diuretic / osmotic laxative action) has no mechanistic overlap with acute nerve root compression pathology. There are no clinical trials and no publications connecting the two, so this candidate cannot currently be distinguished from prediction noise — it likely reflects a high TxGNN score arising from shared graph neighbors rather than a genuine pharmacological relationship.

This prediction should not be advanced without independent mechanistic or preclinical evidence establishing a plausible link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No marketing authorization records are available for glycerin in this database (0 licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction for glycerin (cauda equina syndrome) has no clinical trial or literature support, and the underlying mechanism is pharmacologically implausible given the condition's acute surgical nature versus glycerin's osmotic action. There is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- Original indication and mechanism-of-action (MOA) data for glycerin (currently absent — flagged as a Blocking/High data gap)
- US/TFDA label data (warnings, contraindications, drug interactions) — currently unavailable
- Independent preclinical or mechanistic evidence linking glycerin to cauda equina syndrome before any further evaluation
- If pursuing repurposing for glycerin at all, consider re-scoping to candidates in this same evidence pack with materially stronger evidence bases — notably **open-angle glaucoma** (L3, 16 PubMed records, osmotic mechanism has some plausibility for acute angle-closure but not chronic open-angle use) and **irritable bowel syndrome** (L3, 15 PubMed records, though key literature shows glycerol used to *induce* pain models rather than treat symptoms) — both currently scored "Research Question" rather than "Hold"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


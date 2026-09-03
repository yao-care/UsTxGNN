---
layout: default
title: Oliceridine
parent: 僅模型預測 (L5)
nav_order: 987
evidence_level: L5
indication_count: 4
---

# Oliceridine
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

# Oliceridine: From Acute Pain Management (Inferred) to Insomnia

## One-Sentence Summary

> Oliceridine is a G-protein biased mu-opioid receptor agonist administered intravenously; based on the retrieved clinical trial context it appears to be used for acute postoperative pain control (patient-controlled analgesia), though this is not confirmed by formal regulatory indication data.
> The TxGNN model predicts it may be effective for **Insomnia**,
> but this is currently supported only by model similarity scoring — **no clinical trials or literature directly address this indication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in regulatory filings (drug not yet marketed); the one retrieved trial context suggests use as an IV opioid analgesic for postoperative pain (PCIA) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on the information present, oliceridine is a G-protein biased mu-opioid receptor agonist — a design intended to reduce beta-arrestin-mediated side effects (e.g., respiratory depression, constipation) relative to conventional opioids, while retaining analgesic potency.

The link to insomnia proposed by TxGNN appears to rest on the sedative properties of opioid agonists rather than a validated therapeutic mechanism. Opioids are pharmacologically known to **disrupt** normal sleep architecture — reducing REM and deep sleep while increasing sleep fragmentation and nighttime arousals — which runs counter to their use as an insomnia treatment. No mechanistic or clinical rationale in the evidence pack supports repurposing oliceridine for insomnia; this is a similarity-based inference from the TxGNN model rather than an evidence-backed hypothesis.

The single retrieved clinical trial (NCT07479446) further underscores this: it compares oliceridine to sufentanil for postoperative analgesia and nausea outcomes, and was flagged as **Grade C relevance** — it was captured only because the drug name matched, not because it studies insomnia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07479446](https://clinicaltrials.gov/study/NCT07479446) | NA | Not Yet Recruiting | 174 | Compares oliceridine vs. sufentanil PCIA for postoperative nausea and analgesia in cerebellopontine angle surgery. **Not related to insomnia** — included only due to drug-name match (relevance grade C). |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorization is currently on file — oliceridine has **0 licenses** and is listed as **Not Marketed** in this market's regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Safety data (key warnings, contraindications, drug-drug interactions) are currently unavailable in the evidence pack (data gap DG001, flagged as Blocking). DDI query returned no results.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction is supported only by TxGNN model similarity (Evidence Level L5), with no directly relevant clinical trials or literature, and the underlying mechanistic rationale actually argues against this indication (opioids are known to impair rather than improve sleep quality). Combined with the absence of formal TFDA safety/label data (Blocking gap DG001) and confirmed MOA, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- TFDA-equivalent package insert data (warnings, contraindications) to clear the Blocking safety gap (DG001)
- Confirmed mechanism of action and original approved indication from DrugBank or manufacturer labeling (DG002)
- Disease-specific clinical or preclinical evidence (trials, case reports, or mechanistic studies) directly addressing oliceridine and insomnia — currently none exist
- Note: Other TxGNN-predicted candidates for this drug (migraine, IBS, neurocirculatory asthenia) are similarly L5/Hold with no supporting evidence and weak or contraindicated mechanistic rationale; none are recommended for further evaluation at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


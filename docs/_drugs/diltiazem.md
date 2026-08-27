---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 609
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using no additional skill here — this is a direct report-generation task from a fully-specified Evidence Pack template, not a TxGNN pipeline operation or research task requiring tooling.

I reviewed the Evidence Pack carefully before drafting. Key characteristics that shape this report: `original_indications` is empty, `original_moa` is a data gap, `taiwan_regulatory.licenses` is empty (0 licenses, not marketed), all `safety` fields are data gaps, and the single predicted indication has **zero** clinical trials and **zero** literature despite a high raw TxGNN score — explicitly scored L5/S0/Hold in the pack itself. Per the prohibitions, I've omitted the Market Information and Cytotoxicity sections entirely (no license data; diltiazem is a calcium channel blocker, not antineoplastic) and excluded all literal "[Data Gap]" tokens, replacing them with plain statements of what's missing.

---

# Diltiazem: From an Undocumented Original Indication to Ischemic Stroke Susceptibility

## One-Sentence Summary

Diltiazem's original approved indication and mechanism of action are not documented in this evidence pack (both flagged as data gaps). The TxGNN model predicts a possible association with **Ischemic Stroke Susceptibility** (recorded in the knowledge graph under the label "obsolete susceptibility to ischemic stroke"), with a high raw model score of **99.08%** but **zero supporting clinical trials and zero publications** — the weakest possible evidence tier.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication data in this evidence pack |
| Predicted New Indication | Obsolete Susceptibility to Ischemic Stroke |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for diltiazem is not available in this evidence pack, and no original indication is on file either, so the drug's known clinical history cannot be directly compared against the predicted indication using this dataset alone.

As general pharmacological background (not sourced from this evidence pack), diltiazem is a non-dihydropyridine calcium channel blocker, a class that in principle could influence blood pressure control, cerebral vasodilation, and vasospasm — mechanisms that are plausibly relevant to ischemic stroke risk. However, this is external background knowledge, not a mechanistic link established by the data in hand, and it should not be treated as evidence.

Two additional concerns limit confidence further: first, the predicted disease label itself — "obsolete susceptibility to ischemic stroke" — carries the word "obsolete," suggesting it may be a deprecated or residual knowledge-graph node label rather than a clean clinical diagnosis (e.g., "secondary prevention of ischemic stroke"). It is unclear whether this maps to a standard clinical concept. Second, the high TxGNN score (99.08%) reflects only model confidence, not corroborating evidence — the pack itself grades this as Evidence Level L5 (model prediction only) and Decision Stage S0, meaning no clinical trial, literature, or mechanistic confirmation currently exists.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: a drug-drug interaction query and a TFDA label/warning query were both attempted and returned no results — this is a data availability gap, not a confirmation of safety.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on an unverified model prediction (L5, Decision Stage S0) with no supporting clinical trials, no literature, and no confirmed original-indication or mechanism-of-action data to justify the mechanistic rationale. The drug is also not currently marketed (0 licenses on file), and a **Blocking**-severity data gap (missing TFDA label warnings/contraindications) means this candidate cannot even proceed to the S1 safety pre-screening stage yet.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently blocking any safety pre-assessment
- Confirmed mechanism-of-action (MOA) data for diltiazem from DrugBank
- Clarification of the predicted disease label "obsolete susceptibility to ischemic stroke" against a standard clinical terminology (e.g., ICD/MeSH) to confirm it is not a deprecated knowledge-graph artifact
- At least preliminary clinical trial or literature evidence connecting diltiazem to ischemic stroke risk reduction before advancing past model-prediction-only status
- Drug-drug interaction data, since the current query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


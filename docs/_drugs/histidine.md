---
layout: default
title: Histidine
parent: 僅模型預測 (L5)
nav_order: 770
evidence_level: L5
indication_count: 2
---

# Histidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Histidine: From Essential Amino Acid Supplementation to Gastroparesis

## One-Sentence Summary

Histidine (DrugBank DB00117) is an essential amino acid; the evidence pack contains no recorded approved indication and no market license in the reference dataset. The TxGNN model predicts a possible link to **Gastroparesis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests solely on a theoretical pharmacological argument.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (histidine is an essential amino acid; no approved-indication text or license data is available) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for histidine is not available in this dataset. Based on known pharmacology, histidine is the metabolic precursor of histamine — it is converted to histamine via the enzyme histidine decarboxylase (HDC). Histamine, acting through H2 receptors, is known to modulate gastric acid secretion and gastrointestinal smooth-muscle motility.

The repurposing hypothesis therefore proposes an indirect link: since gastroparesis is a disorder of gastric motility, and histamine signaling participates in regulating that motility, increased histidine (and downstream histamine) availability is theorized to have some relevance to gastroparesis. However, this is a purely pharmacological inference — TxGNN's score is high (0.9955), but no clinical trial or literature evidence currently exists to test, support, or refute this specific drug-disease relationship.

This should be read as a hypothesis-generating signal only, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

(Note: TFDA label warnings/contraindications and DDI data are currently missing from this evidence pack — this is flagged as a blocking data gap for safety evaluation, see "To proceed" below.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has the highest TxGNN score among candidates for this drug (99.55%) but zero supporting clinical trials or literature (Evidence Level L5) — it is a computational hypothesis only, with no human or preclinical data specific to gastroparesis.
- The drug is not currently marketed and has no active license in this dataset, and core safety data (TFDA warnings, contraindications) are marked as a blocking gap, so it cannot yet pass a basic safety screen.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — currently a blocking gap for safety review
- Confirmed mechanism-of-action data via DrugBank API
- Preclinical or observational evidence directly testing histidine/histamine pathway modulation in gastroparesis, since none currently exists
- Note for context: this evidence pack also contains a second, lower-ranked prediction (sclerosing cholangitis, TxGNN score 99.27%, Evidence Level L4) supported by 8 mechanistic publications on histamine/mast-cell signaling in biliary fibrosis. That literature suggests histamine pathway activation *drives* biliary injury in that disease — a directionally *opposite* implication (i.e., increasing histidine/histamine could worsen rather than treat a histamine-driven pathology). This raises a caution flag worth investigating before advancing any histidine-repurposing hypothesis further, including for gastroparesis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


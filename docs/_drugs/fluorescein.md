---
layout: default
title: Fluorescein
parent: 僅模型預測 (L5)
nav_order: 720
evidence_level: L5
indication_count: 10
---

# Fluorescein
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

Using no specialized skill for this task — it's a direct document-generation request against the provided Evidence Pack, not a coding/pipeline task that any available skill covers.

A note before the report: this Evidence Pack is unusual — `original_indications` is empty, `original_moa` is `[Data Gap]`, and Taiwan/US regulatory data shows zero licenses. Also, **every one of the 10 predicted indications is scored L4/L5 with a "Hold" recommendation**, and the pack's own rationale notes repeatedly explain that wherever clinical trials/literature exist, fluorescein appears only as a **diagnostic dye** (angiography/corneal staining), never as the studied treatment. I've written the report to reflect this honestly rather than overstating the case.

---

# Fluorescein: From Diagnostic Ophthalmic Dye to Prinzmetal Angina

## One-Sentence Summary

Fluorescein (DrugBank DB00693) has no recorded therapeutic indication in this dataset — clinically it is known and used as a diagnostic dye for ophthalmic angiography and ocular surface staining, not as a disease-treating agent.
The TxGNN model predicts it may be effective for **Prinzmetal Angina**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and no known vascular or coronary mechanism links fluorescein to this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved therapeutic indication on file. Fluorescein's known clinical use is as an ophthalmic diagnostic dye (angiography / corneal staining), not disease treatment |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (no license on file) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for fluorescein in this dataset. Based on known information, fluorescein is not a conventional therapeutic drug — it is a fluorescent dye administered for diagnostic imaging (e.g., intravenous fluorescein angiography of the retina/choroid, or topical staining to detect corneal epithelial defects). It has no established pharmacodynamic action on vascular smooth muscle tone or coronary artery spasm, which is the pathophysiological mechanism underlying Prinzmetal (variant) angina.

The evidence pack's own analysis of this specific prediction is explicit: "Only a TxGNN prediction score (0.998) exists, with no clinical trial or literature support, and no known vascular smooth muscle or coronary mechanism to support this association." This is not a case of promising-but-unconfirmed biology — it is a pure model output with no corroborating signal of any kind.

It is worth noting a pattern across the other 9 predicted indications in this pack (rheumatoid arthritis, hemoglobinopathy, thrombophilia, hyperthyroidism, etc.): wherever clinical trials or literature were found, fluorescein appeared solely as a **diagnostic/imaging tool** (e.g., fluorescein angiography used to evaluate retinal vasculopathy in these conditions), not as an investigational treatment. This reinforces that TxGNN's high similarity scores here likely reflect fluorescein's frequent co-occurrence with vascular/ophthalmic disease concepts in the knowledge graph, rather than a genuine therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Fluorescein currently has no market authorization on file in this dataset (0 licenses; market status: Not Marketed). No NDA-level product information is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Safety warnings, contraindications, and drug interaction data are all marked as data gaps in this pack — retrieving fluorescein's package insert from the source regulatory agency is listed as a **Blocking** data gap that must be resolved before any safety assessment can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests on a TxGNN similarity score alone (L5 — model prediction only), with zero clinical trials, zero supporting literature, and no plausible pharmacological mechanism connecting a diagnostic ophthalmic dye to coronary vasospasm. There is nothing here to evaluate for safety or efficacy, and the broader pattern across this drug's other top predictions suggests the model is picking up co-occurrence with vascular/ophthalmic imaging use rather than a treatment effect.

**To proceed, the following is needed:**
- Package insert / regulatory safety labeling for fluorescein (currently a Blocking data gap)
- Verified mechanism of action data (currently a High-severity data gap)
- Any preclinical or mechanistic evidence linking fluorescein to coronary artery smooth muscle physiology
- Confirmation of whether "Prinzmetal angina" reflects a genuine disease association or a knowledge-graph artifact (e.g., dye co-mention in cardiac imaging literature) before allocating further review resources
- If proceeding despite weak evidence is being considered, an explicit review of why a diagnostic agent with no known cardiovascular pharmacology would be advanced to the next decision stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


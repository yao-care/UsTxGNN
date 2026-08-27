---
layout: default
title: Loperamide
parent: 僅模型預測 (L5)
nav_order: 869
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Diarrhea to Acute Contagious Conjunctivitis

## One-Sentence Summary

> Loperamide is a well-known peripheral mu-opioid receptor agonist used for symptomatic control of diarrhea (this evidence pack contains no confirmed original-indication or regulatory text — the drug is currently **not marketed** in this jurisdiction).
> The TxGNN model's top prediction is **Acute Contagious Conjunctivitis**, but this candidate has **0 clinical trials** and **0 publications** supporting it, and is explicitly flagged in the source rationale as a likely knowledge-graph clustering artifact rather than a real pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no licenses on file; loperamide is generically known as an antidiarrheal agent) |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| Market Status | Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for loperamide in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, loperamide acts on peripheral mu-opioid receptors in the gut wall to reduce intestinal motility and secretion — a mechanism confined to the gastrointestinal tract with no known pathway relevant to ocular surface or conjunctival inflammation.

The top-ranked prediction, acute contagious conjunctivitis, has **no supporting clinical trials or literature** in this pack. The accompanying rationale explicitly assesses it as a false positive: there is no plausible pharmacological link between a peripheral antidiarrheal agent and an infectious eye condition, and the score is judged to result from the TxGNN disease-embedding space clustering multiple unrelated conjunctivitis subtypes together (ranks 3, 5–9 are all conjunctivitis variants with near-identical scores of ~0.996, several sharing the exact same score value — a signature of embedding collinearity rather than independent evidence).

Notably, the two candidates with the *most* literature support in this batch — amebic dysentery and gastroduodenitis — are not genuine repurposing opportunities either. The available literature describes antimotility agents like loperamide as **contraindicated** in invasive/infectious diarrhea (risk of toxic megacolon, delayed pathogen clearance) and reports a case of loperamide-induced respiratory depression in severe GI inflammation. None of the 10 ranked predictions in this pack currently clear the bar for a positive repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Acute Contagious Conjunctivitis.

---

## Literature Evidence

Currently no related literature available for Acute Contagious Conjunctivitis.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and DrugBank DDI data are both marked as data gaps in this pack — DG001 "TFDA 仿單警語/禁忌" is flagged Blocking severity and must be resolved before any S1 safety evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (acute contagious conjunctivitis) has zero supporting evidence and is assessed as a likely TxGNN embedding-cluster false positive rather than a genuine signal. No candidate across the full top-10 list reaches a positive recommendation — the two candidates with literature support (amebic dysentery, gastroduodenitis) are contraindicated or carry documented safety risk rather than efficacy support.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Blocking data gap DG001) before any safety evaluation can begin
- Confirmed mechanism of action (DG002) to properly assess mechanistic plausibility
- Independent validation of the TxGNN conjunctivitis cluster (ranks 1, 3, 5–9) to rule out a systematic embedding artifact before any of these candidates are pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


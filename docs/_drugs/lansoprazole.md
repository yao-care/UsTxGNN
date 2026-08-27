---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 835
evidence_level: L5
indication_count: 2
---

# Lansoprazole
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

# Lansoprazole: From Acid-Related GI Disease (PPI Class) to Duodenogastric Reflux

## One-Sentence Summary

> Lansoprazole is a proton pump inhibitor (PPI); this evidence pack does not document its originally approved indication or a detailed mechanism of action.
> The TxGNN model predicts a possible link to **duodenogastric reflux**, but the only supporting evidence is **0 clinical trials** and **2 publications** — one an animal carcinogenesis study, the other a general PPI review — and neither supports therapeutic benefit for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug classified only as a Proton Pump Inhibitor via the mechanistic rationale field) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a **blocking-severity** data gap, DG002). Based on the mechanistic rationale that was captured, lansoprazole is a PPI that inhibits gastric parietal cell H+/K+-ATPase to reduce gastric acid secretion.

Acid suppression can theoretically relieve acid-related symptoms, but it has no mechanism to reduce duodenogastric (bile) reflux itself — the reflux event is unaffected by acid suppression. More importantly, the one directly relevant piece of evidence in this pack is an animal study reporting that long-term lansoprazole administration **promoted gastric carcinogenesis** in a duodenogastric reflux rat model, via a proposed low-acid-environment nitrosamine/bile co-carcinogenesis mechanism. This is a potential harm signal in the opposite direction from therapeutic benefit, not supporting evidence.

Given this, the TxGNN model's high prediction score (99.69%) does not align with the direction of the actual literature evidence, and the mechanistic case for repurposing is weak to potentially concerning rather than reasonable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal/Preclinical | Gastric Cancer | Lansoprazole promoted gastric carcinogenesis in rats with induced duodenogastric reflux — a potential harm signal, not a treatment benefit |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | General review of PPI clinical use and pharmacokinetics; not specific to duodenogastric reflux treatment |

---

## US Market Information

Not marketed in the US — no NDA authorizations on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: retrieval of TFDA/FDA label warnings and contraindications is flagged as a **blocking** data gap in this evidence pack — safety cannot be formally assessed until resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials for this indication, and the only literature evidence is a preclinical study suggesting a possible carcinogenesis-promoting effect rather than benefit — the opposite of what the high TxGNN score would suggest. Combined with a blocking-severity data gap on drug label safety information, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (blocking gap, DG001)
- Detailed mechanism of action data (DG002)
- Mechanistic or clinical evidence that directly supports benefit in duodenogastric reflux, and that addresses the conflicting carcinogenesis signal from the 2004 animal study

---

**Additional note:** This evidence pack also included a second TxGNN-predicted indication, *duodenal obstruction* (score 99.68%, L5, Hold). On review, all 4 associated clinical trials and the 1 associated publication were unrelated to treating duodenal obstruction (e.g., oncology immunotherapy trials, general ulcer-prevention studies). Duodenal obstruction is typically a mechanical condition (malrotation, SMA syndrome, tumor compression, adhesions) that acid suppression cannot address. This appears to be a keyword co-occurrence false positive and is not considered a viable repurposing candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


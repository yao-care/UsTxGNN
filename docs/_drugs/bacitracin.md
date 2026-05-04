---
layout: default
title: Bacitracin
parent: 僅模型預測 (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
---

# Bacitracin
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

The txgnn-pipeline skill confirms this is a standard TxGNN report generation task. I'll now generate the evaluation report directly from the Evidence Pack following the v5 prompt specification.

---

# Bacitracin: From Topical Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a polypeptide antibiotic with a long history of topical use against gram-positive bacterial infections of the skin, wounds, and ocular surface.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, the top-ranked indication with a prediction score of **99.999%**.
However, this prediction is supported by **no clinical trials** and **no published literature**, and the mechanistic connection to this predominantly viral or toxic condition is considered weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical treatment of gram-positive bacterial infections (skin, wounds, ophthalmic surface) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory data pack. Based on established pharmacological knowledge, Bacitracin is a polypeptide antibiotic belonging to the bacitracin complex class, with proven topical antibacterial efficacy against gram-positive organisms including *Staphylococcus aureus* and *Streptococcus* species. Ophthalmic ointment formulations of Bacitracin are well-established, which at minimum confirms route-level feasibility for ocular applications.

Punctate epithelial keratoconjunctivitis (PEK) is characterized by scattered punctate epithelial lesions affecting both the cornea and conjunctiva. Its most common etiologies are viral (especially adenovirus and herpes simplex virus) or toxic/chemical injury — bacterial causes represent a distinct minority of cases. While Bacitracin's gram-positive coverage could theoretically address the bacterial subset of PEK, this specific scenario accounts for only a small fraction of the overall disease burden, limiting the practical scope of any antibacterial intervention.

The TxGNN model's extremely high prediction score (99.999%, global rank #64) most likely reflects a conceptual generalization: the model recognizes Bacitracin's ophthalmic formulation availability and broad antibacterial activity and maps these to the broader ocular infectious disease node in the knowledge graph — rather than capturing a direct, PEK-specific mechanistic relationship. The mechanistic link is considered weak, and this score should be treated as a model hypothesis requiring empirical validation rather than an evidence-based clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Punctate epithelial keratoconjunctivitis is a predominantly viral or toxic condition; Bacitracin's antibacterial mechanism provides no meaningful therapeutic rationale for the primary disease etiology, and there is a complete absence of clinical trial or literature evidence to support this specific indication.

**Broader Assessment — More Actionable Direction Among All 10 Predictions:**
Of the 10 predicted indications analyzed in this multi-indication pack, **Otitis Externa** (rank 4, score 99.969%, Evidence Level **L4**) presents the strongest evidence profile with **6 supporting publications**, including a 2007 double-blind clinical comparative study evaluating a Bacitracin-containing combination ointment (polymyxin-B + bacitracin ± hydrocortisone) in 151 patients with acute bacterial otitis externa ([PMID 17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/)). Historical records also document Nebacetin (bacitracin + neomycin) use in ear canal infections dating to the 1960s. The mechanistic rationale — gram-positive coverage for a mixed gram-positive/gram-negative infection — is more defensible than for PEK, though coverage gaps against *Pseudomonas aeruginosa* and the low quality of existing literature (largely pre-1975, no modern RCT) warrant caution. This indication is classified as a **Research Question** and represents the most promising direction for further investigation.

**To proceed with any indication, the following is needed:**
- MOA data from DrugBank API (DG002 — currently missing, classified as High severity)
- Package insert safety data including warnings, contraindications, and full DDI profile (DG001 — currently blocking)
- For **Otitis Externa**: a focused systematic review comparing Bacitracin-containing topical formulations against current first-line agents (fluoroquinolone ear drops) to establish whether there is a residual clinical niche
- For **Punctate Epithelial Keratoconjunctivitis**: prospective identification of the bacterial-etiology subset and whether ophthalmic Bacitracin preparations are already used off-label in this setting
- Market authorization pathway assessment, given the current absence of any approved indications in the US or Taiwan regulatory record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


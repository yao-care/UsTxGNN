---
layout: default
title: Trolamine Salicylate
parent: 僅模型預測 (L5)
nav_order: 1267
evidence_level: L5
indication_count: 10
---

# Trolamine Salicylate
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

# Trolamine Salicylate: From Topical Musculoskeletal Pain Relief to Exostosis

## One-Sentence Summary

> Trolamine salicylate is a topical salicylate salt traditionally used as an over-the-counter counterirritant for minor muscle and joint pain, though detailed regulatory indication text is not available in the current dataset. The TxGNN model predicts it may be effective for **Exostosis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, meaning it rests on model inference alone. Additional evidence gathering and core drug-safety data (MOA, TFDA labeling) are required before this candidate can advance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available regulatory data; historically marketed OTC as a topical analgesic/rubefacient for minor muscle and joint pain |
| Predicted New Indication | Exostosis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for trolamine salicylate. Based on known information, it belongs to the salicylate class of topical NSAID-like agents, historically applied as a counterirritant/analgesic for musculoskeletal pain — its efficacy in relieving muscle and joint discomfort is well established in general clinical use, though the specific regulatory indication text could not be extracted for this evidence pack.

Exostosis (abnormal bony outgrowth, often at joint margins) shares a musculoskeletal/periarticular tissue context with the drug's traditional use in joint and muscle pain relief. Mechanistically, topical salicylates are known to penetrate periarticular tissue (see literature identified under the rheumatoid arthritis candidate, rank 8, showing radiolabeled topical salicylate reaching intra-articular tissue in both animal and human knee joints). This suggests plausible local tissue penetration relevant to bony/joint pathology, which may be the basis for the TxGNN association — however, this remains a mechanistic hypothesis rather than a validated therapeutic rationale, since exostosis is a structural bone lesion rather than an inflammatory or pain condition that salicylates are known to directly treat.

Several other TxGNN-predicted indications for this drug (tendinitis, fibromyalgia, rheumatoid arthritis, gout) are more consistent with the drug's known pharmacology as a topical anti-inflammatory/analgesic, and may warrant separate evaluation as they align more directly with established use-patterns.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: a related candidate indication for this drug — rheumatoid arthritis, rank 8 — does have one supporting publication, PMID [6977559](https://pubmed.ncbi.nlm.nih.gov/6977559/), 1982, demonstrating intra-articular penetration of topical triethanolamine salicylate. This is not directly evidence for exostosis but supports the drug's general periarticular tissue penetration mechanism.)*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (exostosis) is supported only by the TxGNN model score, with zero clinical trials and zero literature evidence (Evidence Level L5). The drug is not currently marketed, and a blocking data gap exists for TFDA labeling (warnings/contraindications), which prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA (or equivalent regulatory) label data — warnings, contraindications (currently a blocking data gap)
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Targeted literature/trial search specific to exostosis and topical salicylate use
- Consider re-evaluating lower-ranked but better-evidenced candidates (e.g., rheumatoid arthritis, rank 8) which already have supporting mechanistic literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


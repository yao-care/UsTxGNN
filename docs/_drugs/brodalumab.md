---
layout: default
title: Brodalumab
parent: 僅模型預測 (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab: From Plaque Psoriasis to Strongyloidiasis

## One-Sentence Summary

Brodalumab is a fully human monoclonal antibody that blocks the IL-17 receptor A (IL-17RA), originally developed for moderate-to-severe plaque psoriasis in markets including the United States and Japan.
The TxGNN model ranks **strongyloidiasis** as its top repurposing prediction with a score of 99.84%; however, **mechanistic analysis strongly suggests this is a false positive** — IL-17A signaling is a critical host defense against *Strongyloides stercoralis*, and blocking IL-17RA is expected to worsen rather than treat this infection.
Currently, **0 clinical trials** and **0 publications** specifically support brodalumab in strongyloidiasis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Moderate-to-severe plaque psoriasis (US/Japan approved; not registered in Taiwan) |
| Predicted New Indication | Strongyloidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured dataset. Based on known information, brodalumab is a fully human IgG2 monoclonal antibody targeting **IL-17 receptor A (IL-17RA)**. Unlike agents that neutralize only IL-17A (e.g., secukinumab, ixekizumab), brodalumab broadly suppresses signaling by all IL-17RA ligands — including IL-17A, IL-17F, IL-17C, IL-17E (IL-25), and the IL-17A/F heterodimer. This broad receptor blockade makes it highly effective in Th17-driven inflammatory diseases such as plaque psoriasis.

⚠️ **Mechanistic Warning — Likely False Positive**: IL-17A is a cornerstone of the host immune response against *Strongyloides stercoralis*. The parasite drives a Th17-biased mucosal response that contributes to its clearance; blocking IL-17RA would be expected to **impair this defense and increase infection risk or severity**, not confer therapeutic benefit. This is a known failure mode of graph-based repurposing models: high TxGNN scores can reflect distant knowledge-graph node connectivity rather than biological plausibility.

Among all top-10 predictions in this dataset, **eye disease (rank 2, score 99.82%)** carries a more mechanistically coherent rationale — IL-17 pathway dysregulation is documented in uveitis and scleritis, and class-related agents (secukinumab, ixekizumab) have preliminary evidence in ocular inflammation. The eye disease prediction should be the primary candidate for further investigation, pending sub-disease classification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for brodalumab in strongyloidiasis.

---

## Literature Evidence

Currently no related literature available for brodalumab in strongyloidiasis.

---

## Taiwan Market Information

Brodalumab has **no registered licenses with the Taiwan FDA** as of the data cutoff (2026-06-02). It is not commercially available in Taiwan.

> **Context**: Brodalumab is approved in the **United States** (Siliq®, FDA 2017) and **Japan** (Lumicef®) for moderate-to-severe plaque psoriasis in adults who are candidates for systemic therapy or phototherapy. It has not obtained Taiwan TFDA registration. Any Taiwan repurposing pathway would require de novo regulatory filing.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinically critical note**: Brodalumab carries a **US FDA Black Box Warning for suicidal ideation and behavior**, observed during clinical trials. It is distributed exclusively through a mandatory **REMS (Risk Evaluation and Mitigation Strategy) program** in the United States. This safety profile is a major constraint for any repurposing program and must be formally characterized before advancing into any new indication. Structured safety data (TFDA warnings, contraindications, DDI) was not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (strongyloidiasis, rank 1) is mechanistically contraindicated — IL-17RA blockade impairs the host Th17 response required to control *Strongyloides* infection, making this prediction a likely false positive arising from graph topology rather than biological mechanism. No supporting clinical or literature evidence exists to counter this concern.

**To proceed with any repurposing direction, the following is needed:**

- **Resolve Blocking Data Gap**: Obtain Taiwan TFDA package insert to document contraindications and Black Box Warnings (currently blocking S1 safety evaluation per DG001)
- **Confirm MOA profile**: Query DrugBank API for full mechanistic and target data (DG002)
- **Deprioritize strongyloidiasis (rank 1)**: Treat as false positive; do not advance without a credible mechanistic rebuttal
- **Advance eye disease (rank 2) as the primary candidate**: Sub-classify the indication (uveitis, scleritis, anterior vs. posterior) and assess compatibility with existing brodalumab safety data and REMS constraints
- **Conduct immune-safety screen across all top predictions**: Ranks 5–8 involve optic nerve / demyelinating disease — IL-17 pathway blockade has been associated with paradoxical worsening in MS and MOG-IgG conditions; safety review is required before any neurological indication is advanced
- **Evaluate Taiwan regulatory pathway**: Brodalumab has no Taiwan registration; a new drug application (NDA) or orphan drug pathway assessment is prerequisite to any local repurposing trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


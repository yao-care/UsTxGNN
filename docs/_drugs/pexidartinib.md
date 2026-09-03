---
layout: default
title: Pexidartinib
parent: 僅模型預測 (L5)
nav_order: 1035
evidence_level: L5
indication_count: 10
---

# Pexidartinib
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

# Pexidartinib: From Tenosynovial Giant Cell Tumor to HER2 Positive Breast Carcinoma

## One-Sentence Summary

> Pexidartinib is an oral small-molecule kinase inhibitor targeting CSF1R, KIT, and FLT3-ITD, originally developed for **tenosynovial giant cell tumor (TGCT)** — this original indication is not captured in the structured drug record but is consistently documented across the literature evidence collected in this pack (e.g., PMID 31602563, 32617868).
> The TxGNN model's top-ranked new prediction is **HER2 positive breast carcinoma**, but this is currently supported by only **1 clinical trial of uncertain relevance** and **no confirmed literature**.
> Evidence for this specific prediction is weak (L4) and does not yet justify further investment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tenosynovial giant cell tumor (TGCT) — derived from literature evidence in this pack; not present in structured drug/license fields |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Market Status | ✗ Not Marketed |
| Number of Licenses/NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The structured `original_moa` field is marked as a data gap. However, literature evidence collected alongside this candidate (PMID 31602563, "Pexidartinib: First Approval") describes pexidartinib as an orally administered small-molecule tyrosine kinase inhibitor with selective activity against the colony-stimulating factor 1 receptor (CSF1R), KIT, and FLT3 with internal tandem duplication (FLT3-ITD). Its established use in TGCT is driven by CSF1 overexpression in that tumor, with pexidartinib blocking CSF1R signaling to reduce tumor-associated macrophage recruitment.

For the predicted new indication, HER2 positive breast carcinoma, the mechanistic rationale is indirect. The evidence pack's own rationale notes that the proposed link runs through a CSF1R–tumor-associated macrophage (TAM) axis, but HER2-positive breast cancer has no established direct molecular relationship with CSF1R signaling. It is not yet clear whether this represents a genuine biological hypothesis (e.g., targeting the tumor microenvironment as an adjunct to HER2-directed therapy) or simply a knowledge-graph embedding similarity without mechanistic grounding.

**Important caveat:** within the same evidence pack, several lower-score-ranked candidates — "synovium cancer" (rank 6), "synovium disease" (rank 7), and "malignant giant cell tumor" (rank 10) — are supported by a completed Phase 3 RCT (ENLIVEN, PMID 31229240), long-term follow-up data, and FDA approval. These almost certainly reflect pexidartinib's **already-established indication (TGCT)** re-surfacing in the knowledge graph rather than a novel repurposing signal, and should not be treated as new candidates. This is a useful data-quality flag: strong evidence density in this pack correlates with known indication overlap, not necessarily with a validated new use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01042379](https://clinicaltrials.gov/study/NCT01042379) | Phase 2 | Recruiting | 5000 | I-SPY2 — a multi-drug adaptive platform trial matching investigational agents to breast cancer subtypes via imaging/biomarker response. It is **not confirmed** whether pexidartinib is an active treatment arm or specifically linked to the HER2+ subtype (relevance graded C — reasoning: "unconfirmed whether this entry includes a pexidartinib treatment arm or is specifically linked to the HER2+ population; relevance uncertain, requires verification of trial arm design"). |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Pexidartinib is currently **not marketed** in this jurisdiction (market status: Not Marketed; 0 total licenses). No license/NDA records are available to summarize.

---

## Cytotoxicity (Antineoplastic Drugs Only)

Pexidartinib's established indication (TGCT) is a neoplasm, and the drug is a small-molecule targeted kinase inhibitor, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (small-molecule tyrosine kinase inhibitor: CSF1R / KIT / FLT3-ITD) |
| Myelosuppression Risk | Not specified in available data; please refer to the package insert |
| Emetogenicity Classification | Not specified in available data; please refer to the package insert |
| Monitoring Items | Liver function parameters (ALT, AST, total bilirubin) — flagged in exposure-response safety literature within this pack (PMID 34585528); please refer to the package insert for the complete monitoring schedule |
| Handling Protection | Not specified in available data; please refer to institutional handling guidelines for oral antineoplastic agents |

---

## Safety Considerations

Please refer to the package insert for safety information. Note that a **blocking data gap** exists for TFDA-equivalent label warnings/contraindications (DG001), which prevents a formal S1 safety pre-assessment for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between pexidartinib's CSF1R/KIT/FLT3-ITD activity and HER2-positive breast carcinoma is indirect and unconfirmed. Supporting evidence is limited to a single trial (I-SPY2) whose relevance to pexidartinib and this specific subtype has not been verified, with no literature support (Evidence Level L4).

**To proceed, the following is needed:**
- Verification of whether pexidartinib is an active treatment arm in NCT01042379 (I-SPY2) and, if so, outcome data specific to the HER2+ cohort
- Resolution of the TFDA-equivalent warnings/contraindications data gap (DG001) before any S1 safety pre-assessment
- Structured MOA data (DG002) to formally support or refute the CSF1R–TAM–HER2+ breast cancer mechanistic hypothesis
- Preclinical evidence establishing a direct or TME-mediated link between CSF1R inhibition and HER2+ breast cancer response
- Clarification that TGCT-adjacent labels in this evidence pack (ranks 6, 7, 10) represent the known indication rather than independent repurposing candidates, so they are not mistakenly carried forward as "new" predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


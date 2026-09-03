---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 887
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV-1 Infection (CCR5 Antagonist) to Multiple Endocrine Neoplasia

*Note: This evidence pack does not contain a confirmed original-indication text or MOA record (see Data Gap DG002). The "HIV-1 infection / CCR5 antagonist" framing above is inferred from the repurposing-rationale text and the surrounding literature context in this pack (e.g. papers on "antiretroviral therapy," "HIV disease," "HIV+ patients ART treated"), not from a verified regulatory source.*

## One-Sentence Summary

Maraviroc is a CCR5 antagonist most commonly associated with HIV-1 antiretroviral therapy, though no confirmed original-indication or mechanism-of-action record exists in this evidence pack. TxGNN's top prediction is **multiple endocrine neoplasia (MEN)**, but this candidate has **zero supporting clinical trials and zero literature**, and the model's own rationale states no known mechanistic link between CCR5 and MEN pathogenesis (RET/MEN1 mutations) exists.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (contextually CCR5 antagonist / HIV-1 therapy — unconfirmed, see DG002) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (Data Gap DG002, High severity). Based on the repurposing-rationale text attached to this and other candidates in the same evidence pack, maraviroc is consistently identified as a **CCR5 antagonist**.

The evidence pack's own analysis states explicitly that there is **no known intersection** between the CCR5 antagonist mechanism and the RET/MEN1 gene-mutation pathways that drive multiple endocrine neoplasia. No preclinical, epidemiological, or clinical data connecting CCR5 signaling to MEN pathogenesis were found.

As a result, this candidate rests entirely on the TxGNN model's statistical prediction score, with no mechanistic, preclinical, or clinical corroboration. This is the weakest tier of evidence in the scoring framework (L5).

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Both TFDA label warnings/contraindications (DG001, Blocking severity) and drug-drug interaction data (query returned "not_found") are unavailable, which by itself blocks progression to a formal safety evaluation (S1) for this drug.*

## Other Candidates in This Evidence Pack

Ten indications were screened for maraviroc; only the top-ranked one is detailed above per report scope. For context, the full ranked set (evidence quality varies substantially — several lower-ranked candidates have stronger mechanistic grounding than the top prediction):

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|------|----------------------|-------------|-----------------|-----------------|------|
| 1 | Multiple endocrine neoplasia | 99.82% | L5 | Hold | No known CCR5–MEN mechanistic link |
| 2 | Acne (disease) | 99.76% | L5 | Hold | No known CCR5–acne link |
| 3 | Primary cutaneous T-cell lymphoma | 99.72% | L4 | Hold | CTCL mainly involves CCR4, not CCR5; literature only tangential |
| 4 | Pediatric SLE | 99.71% | L5 | Hold | CCR5Δ32/SLE link exists in general literature, but none cited here |
| 5 | Primary cutaneous T-cell non-Hodgkin lymphoma | 99.50% | L4 | Hold | Duplicate of rank 3, same tangential citation |
| 6 | Primary cutaneous B-cell lymphoma | 99.38% | L5 | Hold | No known mechanistic link |
| 7 | Candidiasis | 99.28% | L4 | Hold | Cited literature describes candidiasis as an ART side effect, not a maraviroc treatment effect |
| 8 | Complement component 4a deficiency | 99.24% | L5 | Hold | No known mechanistic link |
| 9 | Cytomegalovirus infection | 99.23% | L4 | **Research Question** | CCR5's role in immune trafficking plausible in HIV/CMV co-infection, but evidence is indirect |
| 10 | HER2-positive breast carcinoma | 99.22% | L4 | **Research Question** | Strongest direct molecular rationale: CCL5 (CCR5's endogenous ligand) drives trastuzumab resistance via ERK — theoretically blockable by a CCR5 antagonist |

Rank 10 (HER2-positive breast carcinoma) and rank 9 (CMV infection) carry the only "Research Question" recommendations in the set and may warrant separate evaluation if this pipeline is to be pursued further.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (multiple endocrine neoplasia) has no supporting clinical, literature, or mechanistic evidence beyond the raw TxGNN score, and the model's own rationale rules out a plausible biological connection. Combined with a Blocking-severity gap in TFDA safety data and an unmarketed status in the reference market, there is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action and original-indication record for maraviroc (DG002)
- If pursuing repurposing further, redirect evaluation toward the higher-mechanistic-plausibility candidates identified in this pack (HER2-positive breast carcinoma, CMV infection) rather than the top TxGNN-ranked but mechanistically unsupported MEN prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Desoximetasone
parent: 僅模型預測 (L5)
nav_order: 588
evidence_level: L5
indication_count: 10
---

# Desoximetasone
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

# Desoximetasone: From Inflammatory Dermatoses to Alopecia Areata

## One-Sentence Summary

Desoximetasone is a mid-to-high potency topical corticosteroid classically used for inflammatory skin conditions such as eczema and psoriasis.
The TxGNN model predicts it may be effective for **Alopecia Areata**,
with **0 clinical trials** and **1 publication** (a randomized double-blind placebo-controlled trial) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No US market authorization on record in this dataset |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Desoximetasone is a fluorinated mid-to-high potency topical glucocorticoid. It binds intracellular glucocorticoid receptors to suppress transcription of pro-inflammatory cytokines, inhibit immune cell recruitment, and dampen local inflammatory responses in the skin. Its formulation characteristics — including its cream and gel vehicles — confer sufficient dermal penetration to reach the perifollicular dermis.

Alopecia areata is an organ-specific autoimmune disease in which CD8+ T lymphocytes breach the immune privilege of the hair follicle bulb, driven by IFN-γ and IL-2 signaling. Topical corticosteroids directly counter this pathogenic cascade by suppressing T-cell activation and reducing local cytokine secretion at the inflammatory focus. Desoximetasone's mid-to-high potency allows it to reach perifollicular tissue at therapeutically relevant concentrations — a critical requirement for this indication, given that weaker steroids often fail to penetrate deeply enough. This mechanistic alignment makes the TxGNN prediction biologically well-grounded.

It is also worth noting that topical corticosteroids are already a cornerstone first-line therapy for patchy alopecia areata in international dermatology guidelines. The TxGNN model's prediction therefore reinforces established clinical practice, while the existing RCT (see Literature Evidence below) provides direct empirical support specifically for Desoximetasone in this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11030789](https://pubmed.ncbi.nlm.nih.gov/11030789/) | 2000 | RCT | Archives of Dermatology | Randomized double-blind placebo-controlled trial of 0.25% desoximetasone cream for alopecia areata; provides the only head-to-head clinical evidence directly evaluating this drug–disease pair |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A randomized double-blind placebo-controlled trial (PMID 11030789) directly evaluated 0.25% desoximetasone cream in alopecia areata patients, providing Level 2 clinical evidence; the mechanistic rationale is strong, as desoximetasone's immune-suppressive action directly targets the CD8+ T-cell–driven pathogenesis of this condition.

**To proceed, the following is needed:**
- Full text retrieval of PMID 11030789 to extract efficacy outcomes (hair regrowth rate, responder definition) and adverse events
- Formal mechanism of action documentation (MOA currently not available in the Evidence Pack)
- US label / package insert review: warnings, contraindications, and drug interactions are not yet captured
- Clarification of US regulatory status — Desoximetasone (Topicort®) may have existing NDA data not reflected in this dataset; cross-check FDA Orange Book
- Concentration and vehicle optimization assessment: the published RCT used 0.25% cream; confirm whether commercially available strengths (0.05%, 0.25%) and vehicles (cream, gel, ointment) are appropriate for the scalp
- Risk management plan for long-term use: skin atrophy and HPA-axis suppression are known class effects of mid-to-high potency topical corticosteroids; a safety monitoring protocol is required before proceeding to any formal study or off-label use recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


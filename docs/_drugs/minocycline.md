---
layout: default
title: Minocycline
parent: 僅模型預測 (L5)
nav_order: 931
evidence_level: L5
indication_count: 2
---

# Minocycline
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

# Minocycline: From Antibacterial Therapy to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Minocycline is a tetracycline-class antibiotic; the evidence pack does not contain a specific approved original indication or detailed mechanism-of-action record for this jurisdiction. The TxGNN model predicts potential efficacy for **Punctate Epithelial Keratoconjunctivitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on knowledge-graph similarity and class-effect reasoning from a related drug (doxycycline).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketed license records on file |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for minocycline is not available in this evidence pack, and no approved original indication is on file (the drug is not currently marketed in the reviewed jurisdiction). Based on known pharmacological classification, minocycline is a tetracycline-class antibiotic.

Per the model's own rationale, minocycline exhibits MMP-9 inhibition, anti-inflammatory activity (via suppression of the IL-1/TNF-α pathway), and anti-apoptotic effects. The related tetracycline-class drug doxycycline already has clinical use precedent in dry eye disease and ocular-surface-inflammation-related keratoconjunctivitis, which lends some mechanistic plausibility to the prediction.

However, this is explicitly a **class-effect inference**, not direct evidence for minocycline itself in this indication. The very high TxGNN score (99.63%) reflects only knowledge-graph topological similarity between minocycline and drugs used in ocular surface disease — it is not derived from any clinical or experimental validation of minocycline in this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

No US market authorization on file for minocycline in this jurisdiction (market status: Not Marketed; 0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5-level, model-prediction-only candidate with no supporting clinical trials or literature, and the mechanistic link relies on a class-effect inference from a related drug rather than direct evidence for minocycline. No original indication, MOA, or safety data are currently on file, so the candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- Confirmed original indication and detailed mechanism-of-action data for minocycline (e.g., via DrugBank/TFDA label lookup)
- TFDA/FDA package insert warnings, contraindications, and drug-drug interaction data (currently blocking per data gap DG001)
- Direct preclinical or clinical evidence of minocycline (not just doxycycline) in punctate epithelial keratoconjunctivitis or related ocular surface disease
- Route-of-administration and formulation compatibility assessment for ophthalmic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


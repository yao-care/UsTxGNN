---
layout: default
title: Ocrelizumab
parent: 僅模型預測 (L5)
nav_order: 981
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ocrelizumab: From Multiple Sclerosis to HER2 Positive Breast Carcinoma

## One-Sentence Summary

> Ocrelizumab is an anti-CD20 monoclonal antibody used to deplete B cells in autoimmune conditions such as multiple sclerosis.
> The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph inference with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple sclerosis (inferred from the mechanistic rationale text embedded in this evidence pack; not present in the structured indication/license fields) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the structured fields of this evidence pack (`original_moa` is unpopulated). Based on the rationale text accompanying the predictions, ocrelizumab is an anti-CD20 monoclonal antibody that works by depleting B cells, and is clinically used for autoimmune diseases such as multiple sclerosis. This is an immune-modulating mechanism, not a cytotoxic or oncogene-targeted one.

No mechanistic pathway connects B-cell depletion to HER2-driven tumor growth, hormone-receptor signaling (PR-positive/negative subtypes), or the luminal A/B and normal breast-like molecular subtypes also listed among the top-5 predictions. The model's own rationale text for all five candidates explicitly states this is an indirect knowledge-graph association lacking biological plausibility — the drug and disease co-occur in the graph without a demonstrated causal or mechanistic link.

A notable data-quality issue further weakens confidence: for the rank-4 candidate ("breast tumor luminal A or B"), 19 literature records were initially surfaced, but manual review shows these are false positives caused by keyword collision — they are papers on B-cell immunology, hepatitis **B** vaccines, and HLA-**B** allele typing, none of which relate to breast cancer. This suggests the underlying evidence-matching pipeline is prone to spurious "B" string matches and should be treated with caution across this drug's candidate set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

*Note: A separate, lower-ranked candidate ("breast tumor luminal A or B") did surface 19 PubMed records, but on review these are false-positive keyword matches (B-cell biology, hepatitis B vaccine studies, HLA-B allele typing) rather than genuine drug–disease evidence, and are therefore not presented as supporting literature.*

---

## US Market Information

No marketing authorization records found. Per `taiwan_regulatory`, ocrelizumab currently has a market status of **Not Marketed** with **0 licenses** on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (HER2 positive breast carcinoma) has zero supporting clinical trials or literature, and the model's own rationale explicitly flags the absence of biological plausibility for a CD20/B-cell-depletion mechanism driving HER2+ tumor growth.
- Apparent literature support found for a related candidate turned out to be a false-positive artifact of keyword matching, further undermining confidence in the current evidence pipeline for this drug.
- Critical safety data (TFDA warnings/contraindications) is flagged as a **Blocking** data gap (DG001), which alone prevents progression past initial safety screening.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (resolve DG001)
- Confirmed, sourced mechanism-of-action data (resolve DG002)
- Genuine preclinical or translational evidence linking B-cell depletion pathways to any of the five predicted breast cancer subtypes
- Re-run literature/evidence matching with disambiguated search terms to eliminate "B" keyword false positives
- Confirmation of regulatory/marketing status in target jurisdiction(s), since the drug is currently unmarketed per this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


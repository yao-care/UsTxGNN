---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 713
evidence_level: L5
indication_count: 1
---

# Fluconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using the drug-repurposing report template supplied directly in your prompt (no matching specialized skill covers this exact task — this is the report-writing instruction itself), I've built the report strictly from the Evidence Pack fields, omitting sections with no data per the prohibitions (no cytotoxicity section — fluconazole is antifungal, not antineoplastic; no US/TW market table — zero licenses; no fabricated original-indication text).

---

# Fluconazole: From No TFDA-Approved Indication to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is a triazole antifungal agent, but no original indication list, mechanism-of-action detail, or Taiwan market license data is currently available for this candidate (the drug is recorded as **not marketed** in Taiwan with 0 licenses).
The TxGNN model predicts possible efficacy for **Punctate Epithelial Keratoconjunctivitis**, with a prediction score of **99.24%**,
but this direction is currently supported by **0 clinical trials** and **0 publications**, placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no TFDA license records and empty original indication list |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap), and no original indication list is on record for this candidate. Based on the drug class information that is available, fluconazole is a **triazole antifungal**, which mechanistically inhibits the fungal cytochrome P450-dependent enzyme lanosterol 14-α-demethylase, blocking ergosterol synthesis and disrupting fungal cell membrane integrity.

The predicted new indication, punctate epithelial keratoconjunctivitis (點狀上皮性角膜結膜炎), is in most cases caused by viral infection (e.g., adenovirus-associated epidemic keratoconjunctivitis) or by dry eye/immune-mediated pathology — only a minority of cases are fungal in origin (e.g., *Candida* or *Fusarium* keratitis presenting with punctate epithelial lesions). If a given case is confirmed fungal, fluconazole's antifungal mechanism has a plausible theoretical link to topical/systemic treatment of fungal keratitis.

However, because the disease label here does not specify a pathogen, this mechanistic link is **indirect and inferential rather than a direct pathophysiological connection**. This is further weakened by the absence of original MOA data, an empty original-indication list, and the drug's unmarketed status in Taiwan — all of which reduce the overall credibility of the prediction at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are recorded as a **Blocking** data gap — this must be resolved before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at Evidence Level L5 — a TxGNN model prediction with zero supporting clinical trials or literature — and the mechanistic rationale linking fluconazole to punctate epithelial keratoconjunctivitis is indirect, since the indication's etiology is predominantly non-fungal. The drug is also unmarketed in Taiwan (0 licenses), and a Blocking data gap on TFDA warnings/contraindications prevents any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — Blocking gap, required before S1 safety review
- Confirmed mechanism of action (MOA) data via DrugBank
- Original indication history for fluconazole to assess similarity to the predicted indication
- Pathogen-specific evidence (culture/PCR-confirmed fungal keratitis) supporting relevance of the predicted indication before pursuing clinical or literature searches further
- Any real-world or case-level evidence of antifungal use in fungal-associated punctate keratoconjunctivitis, since current searches (ClinicalTrials.gov, ICTRP, PubMed) returned zero results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


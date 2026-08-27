---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 847
evidence_level: L5
indication_count: 1
---

# Letermovir
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

# Letermovir: From Cytomegalovirus (CMV) Infection to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is an antiviral agent whose known mechanism (CMV terminase complex inhibition) targets herpesvirus DNA processing; detailed original-indication and MOA records for this evidence pack are marked as data gaps. The TxGNN model predicts potential activity against **Vulvovaginal Candidiasis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on embedding similarity, and the model's own mechanistic review flags it as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this dataset — Letermovir is not marketed in Taiwan and no approved-indication text is on file. (Its known drug class, per the mechanistic rationale supplied, is a CMV terminase-complex inhibitor / anti-herpesvirus agent.) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% (rank 3764) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations (Taiwan) | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Letermovir is marked as a data gap in this evidence pack (`original_moa: [Data Gap]`), and no original indication records are available. Based on the mechanistic notes attached to this prediction, Letermovir is known to inhibit the CMV terminase complex (pUL56/pUL89/pUL51), acting on herpesvirus DNA processing and packaging — a narrow-spectrum antiviral mechanism.

Vulvovaginal candidiasis, by contrast, is a fungal infection caused by *Candida* species, with treatment targets centered on ergosterol synthesis and fungal cell-wall glucan synthesis. There is no known mechanistic overlap between a herpesvirus terminase inhibitor and antifungal drug targets, and no indirect pathway (e.g., host immune modulation, microbiome effects) has been proposed or supported by any preclinical or clinical data currently on file.

Given this, the prediction should be treated as a pure embedding-similarity output from the TxGNN model rather than a mechanistically grounded hypothesis. The evidence pack's own repurposing rationale explicitly flags this as a **potential false positive** and recommends against committing mechanism-validation resources at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Letermovir currently has no marketing authorization on file in Taiwan (`market_status: 未上市`, `total_licenses: 0`). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack; a TFDA label review remains an open, blocking data gap — see Next Steps.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is high, but there is zero clinical trial or literature support, no plausible mechanistic link between Letermovir's known antiviral action and antifungal disease biology, and the evidence pack itself identifies this as a likely false positive (Evidence Level L5, decision stage S0).

**To proceed, the following is needed:**
- TFDA label / warnings and contraindications data (currently a Blocking data gap)
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature (currently a High-severity data gap)
- Any preclinical or in vitro evidence of antifungal or immunomodulatory activity for Letermovir, to establish biological plausibility before further investment
- Periodic re-query of ClinicalTrials.gov, ICTRP, and PubMed to check whether independent evidence emerges over time
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


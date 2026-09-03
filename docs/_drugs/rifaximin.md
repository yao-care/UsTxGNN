---
layout: default
title: Rifaximin
parent: 僅模型預測 (L5)
nav_order: 1122
evidence_level: L5
indication_count: 6
---

# Rifaximin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Rifaximin: From Unspecified Original Indication to Oral Candidiasis

## One-Sentence Summary

> Rifaximin's original indication data is not available in this evidence pack, and the drug is currently **not marketed in Taiwan**.
> The TxGNN model predicts a possible link to **Oral Candidiasis** with a very high score (99.75%),
> but the only supporting literature actually reports rifaximin as a **risk factor** for candidiasis, not a treatment — the mechanistic and clinical evidence contradict the prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license or indication data provided) |
| Predicted New Indication | Oral Candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only; available evidence points opposite direction) |
| Market Status (Taiwan) | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for rifaximin in this evidence pack. Based on the drug's known pharmacological class, rifaximin is a gut-restricted, non-absorbable rifamycin-class antibiotic that inhibits bacterial DNA-dependent RNA polymerase in enteric bacteria. It has no known antifungal activity, so there is no direct pharmacological mechanism connecting it to *Candida* (fungal) infections such as oral candidiasis.

The single relevant publication identified (PMID 34180023) actually reports the **opposite relationship**: in allogeneic HSCT recipients, rifaximin use was associated with emergence of micafungin-resistant *Candida* species, likely because suppression of competing gut bacterial flora allows fungal overgrowth. A second paper found for the related "candidiasis" prediction (PMID 32360775) similarly lists broad-spectrum antibacterial exposure as a risk factor for candidaemia in cirrhotic patients, not a protective factor.

Given this, the high TxGNN score most likely reflects an indirect knowledge-graph connection (e.g., shared microbiome/gut-flora nodes) rather than a genuine therapeutic signal. The repurposing rationale for this candidate should be treated as **not mechanistically supported**, and the same conclusion extends to the lower-ranked candidates (commissural lip fistula, osteoradionecrosis of the mandible, oral leukoedema, burning mouth syndrome), none of which have any biological plausibility or supporting literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | Rifaximin use in allogeneic HSCT recipients was associated with emergence of micafungin-resistant *Candida* spp. — a risk signal, not a treatment benefit |

---

## US Market Information

Rifaximin is not currently marketed in Taiwan under this evidence pack (0 licenses on record); no product/license data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety review (S1) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, there is no mechanistic basis and no supportive clinical or literature evidence for rifaximin in oral candidiasis — the only available publication reports rifaximin as a risk factor for candidiasis, not a treatment. All other top-ranked predictions for this drug (commissural lip fistula, osteoradionecrosis of the mandible, oral leukoedema, burning mouth syndrome, candidiasis) similarly lack any supporting evidence or plausible mechanism. This candidate should not advance past S0.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Blocking gap, DG001) — required before any safety screening
- Confirmed mechanism of action (MOA) data from DrugBank (High priority gap, DG002)
- Original indication data (currently missing entirely)
- If this candidate is to be reconsidered, an independent investigation into why TxGNN scored it highly despite contradicting evidence (possible graph-embedding artifact) is recommended before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


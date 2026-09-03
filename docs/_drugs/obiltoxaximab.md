---
layout: default
title: Obiltoxaximab
parent: 僅模型預測 (L5)
nav_order: 979
evidence_level: L5
indication_count: 8
---

# Obiltoxaximab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Obiltoxaximab: From Inhalational Anthrax to Postinfectious Vasculitis

## One-Sentence Summary

> Obiltoxaximab is a monoclonal antibody that neutralizes *Bacillus anthracis* protective antigen (PA), originally developed for the treatment and prophylaxis of inhalational anthrax.
> The TxGNN model predicts it may be effective for **Postinfectious Vasculitis**,
> but currently **no clinical trials** and **no literature** support this specific direction — the prediction rests on knowledge-graph topological similarity alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inhalational anthrax (*B. anthracis* PA-toxin neutralization; not confirmed via formal label data — see Data Gaps) |
| Predicted New Indication | Postinfectious Vasculitis |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| US/Taiwan Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity Data Gap). Based on available evidence-pack context, obiltoxaximab is a highly target-specific neutralizing monoclonal antibody directed against *B. anthracis* protective antigen — its proven efficacy is confined to anthrax toxin-mediated disease.

The model's own rationale for this candidate is explicit that no known mechanistic link exists: postinfectious vasculitis involves immune-complex-mediated vascular inflammation following a broad range of infections, a pathway unrelated to anthrax toxin neutralization. The high TxGNN score is attributed to knowledge-graph embedding similarity rather than any pharmacological or clinical signal, and no supporting trials or publications were identified.

Given this, the prediction should be treated as a hypothesis-generating signal only, not as evidence of therapeutic potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US/Taiwan Market Information

No marketing authorizations are currently on file for this market (0 licenses; market status: 未上市 / Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA label warnings/contraindications and DDI data are not yet available for this drug (flagged as a Blocking Data Gap — DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no supporting clinical trials or literature, no plausible mechanistic overlap with the drug's known anthrax-toxin-neutralizing activity, and the drug itself lacks confirmed MOA and safety label data — evidence is insufficient at every level to advance this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action (DrugBank API query) — High severity gap
- TFDA label warnings/contraindications (PDF retrieval and parsing) — Blocking gap, required before any safety pre-screening (S1)
- A mechanistic plausibility study evaluating whether anti-toxin antibodies have any role in immune-complex-mediated vasculitis
- Continued monitoring for emerging trials or literature specific to postinfectious vasculitis before reconsidering this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


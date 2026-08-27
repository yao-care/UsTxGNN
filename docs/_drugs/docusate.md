---
layout: default
title: Docusate
parent: 僅模型預測 (L5)
nav_order: 618
evidence_level: L5
indication_count: 2
---

# Docusate
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

# Docusate: From No Recorded Original Indication to Plummer-Vinson Syndrome

## One-Sentence Summary

Docusate (DrugBank ID: DB11089) currently has no recorded original indication, marketing authorization, or mechanism-of-action data in this evidence pack — it is not marketed in the reference regulatory jurisdiction (0 licenses). The TxGNN model predicts a possible association with **Plummer-Vinson syndrome**, but this signal is supported by **0 clinical trials** and **0 publications**, meaning it currently rests entirely on knowledge-graph topology rather than any actual clinical or mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no licenses or original indication text on record |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for docusate in this evidence pack (flagged as a High-severity data gap, DG002). Based on the information that is available, docusate is known to function as an intestinally-acting anionic surfactant (stool softener) that lowers stool surface tension to promote water penetration, with minimal systemic absorption.

Plummer-Vinson syndrome is characterized by iron-deficiency anemia, esophageal webs, and dysphagia — a pathology rooted in iron metabolism and mucosal atrophy. There is no known pharmacological overlap between docusate's local intestinal surfactant action and the iron-metabolism/mucosal mechanisms underlying Plummer-Vinson syndrome.

Because the original mechanism-of-action data is missing and no drug-disease mechanistic bridge can be constructed, this prediction should be interpreted as a **topological similarity inference** from the TxGNN knowledge graph rather than a mechanism-driven hypothesis. The high prediction score may reflect sparse node connectivity or node-degree bias in the graph rather than genuine pharmacological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No approved licenses are currently on record for docusate in this dataset (market status: Not Marketed; total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and drug-drug interaction data are flagged as a Blocking-severity data gap, DG001 — this must be resolved before any safety pre-assessment (S1) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is at Evidence Level L5 — supported only by the TxGNN model with zero clinical trials and zero publications for Plummer-Vinson syndrome. Combined with missing original indication, mechanism of action, and safety label data, there is currently no basis to advance this candidate beyond exploratory screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications, drug interactions) — Blocking gap (DG001)
- Confirmed mechanism of action data via DrugBank — High-priority gap (DG002)
- Confirmation of docusate's original approved indication(s) and licensing status
- Any preclinical or mechanistic rationale linking intestinal surfactant activity to Plummer-Vinson syndrome pathophysiology, before committing further review resources

**Additional note:** The evidence pack also lists a second, lower-priority TxGNN prediction — vitamin B12- and folate-independent constitutional megaloblastic anemia (score 99.15%, rank 18472) — which carries the same L5/Hold status for the same reasons (ultra-rare disease, no mechanistic or clinical evidence, likely graph topology artifact). It does not change the overall recommendation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Tafenoquine
parent: 僅模型預測 (L5)
nav_order: 1193
evidence_level: L5
indication_count: 1
---

# Tafenoquine
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

# Tafenoquine: From Antimalarial Prophylaxis to Smouldering Systemic Mastocytosis

## One-Sentence Summary

> Tafenoquine is an 8-aminoquinoline antimalarial, known pharmacologically for malaria prophylaxis and radical cure of *P. vivax* infection, though it is not currently marketed in Taiwan and formal indication data is unavailable in this evidence pack.
> The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registry data; known pharmacology suggests malaria prophylaxis / *P. vivax* radical cure (not TFDA-approved) |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.05% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacological background, tafenoquine belongs to the **8-aminoquinoline** class of antimalarial drugs. Its proposed mechanism involves mitochondrial disruption and induction of oxidative stress in the parasite, leading to parasite death. It is primarily used for malaria chemoprophylaxis and radical cure of *Plasmodium vivax* infection.

Smouldering systemic mastocytosis is driven predominantly by **KIT D816V** mutation, causing abnormal proliferation of mast cells. Standard-of-care targeted therapies act on the KIT signaling pathway (e.g., midostaurin, avapritinib). There is currently no known literature or mechanistic evidence linking 8-aminoquinoline antimalarials to KIT signaling or mast cell proliferation pathways.

The TxGNN score of 0.99 in this case reflects knowledge-graph embedding similarity rather than a validated mechanistic relationship. Given the absence of any supporting clinical or literature evidence, this prediction should be treated as a hypothesis-generating signal only, not as a mechanistically substantiated repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Tafenoquine is currently not marketed in Taiwan; no license records are available in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN's model score (L5 evidence level), with no clinical trials, literature, or mechanistic rationale connecting an 8-aminoquinoline antimalarial to KIT-driven mast cell disease. Without independent corroborating evidence, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- Confirmed original MOA and approved indications for tafenoquine (DrugBank/manufacturer labeling)
- TFDA or FDA package insert warnings, contraindications, and drug interaction data (currently blocking per DG001)
- Independent literature or preclinical evidence linking 8-aminoquinoline compounds to KIT signaling or mast cell biology
- Any case reports or pharmacovigilance signals suggesting off-target hematologic effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


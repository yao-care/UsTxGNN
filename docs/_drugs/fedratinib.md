---
layout: default
title: Fedratinib
parent: 僅模型預測 (L5)
nav_order: 694
evidence_level: L5
indication_count: 10
---

# Fedratinib
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

# Fedratinib: From [Original Indication — Data Gap] to Benign PEComa

## One-Sentence Summary

> Fedratinib (DrugBank ID DB12500) is a JAK2-selective kinase inhibitor, but its original approved indication could not be verified in this Evidence Pack due to a blocking data gap (no TFDA label data retrieved).
> The TxGNN model predicts it may be effective for **Benign PEComa**, with a prediction score of **99.84%**,
> but **no clinical trials and no literature** currently support this specific direction — the evidence pack itself flags the mechanistic link as unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — blocking data gap (TFDA label not yet retrieved, see Safety section) |
| Predicted New Indication | Benign PEComa |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only, no clinical/literature support) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for fedratinib is not available in this Evidence Pack (flagged as a High-severity data gap, DG002). Based on the repurposing rationale text accompanying multiple predictions in this pack, fedratinib is consistently described as a **JAK2-selective kinase inhibitor**, which is the pharmacological basis TxGNN uses across all ten candidate indications.

For the top-ranked candidate, **benign PEComa**, the model's own rationale explicitly states the opposite of a supporting mechanistic story: PEComa is driven by **TSC1/TSC2 mutations causing mTOR pathway hyperactivation**, a pathway with **no known direct relationship to JAK2 signaling**. The rationale text describes this prediction as lacking mechanistic plausibility and having no clinical evidence to date. The same pattern holds for the next several ranked candidates (lymphangiomyoma, uterine PEComa, dermatofibrosarcoma protuberans, rhabdoid tumor, familial rhabdoid tumor, FMF, lymphangioleiomyomatosis) — all are driven by mTOR, PDGFRB, SMARCB1-loss, or IL-1β pathways rather than JAK2.

Notably, two lower-ranked candidates in this pack — **hemophagocytic syndrome associated with infection** (rank 8) and **malignancy-associated HLH** (rank 9) — have a stronger mechanistic case: HLH's cytokine storm (IFN-γ, IL-6, IL-10) signals through JAK-STAT, and the JAK1/2 inhibitor ruxolitinib already has clinical evidence (e.g., NCT03533104) in this setting. This represents a class-effect hypothesis rather than fedratinib-specific evidence, but is mechanistically more coherent than the top-ranked PEComa prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Fedratinib is currently **not marketed** in this jurisdiction (0 licenses/NDAs on file), so no authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are all marked as unresolved data gaps in this Evidence Pack — TFDA label retrieval is required (DG001, Blocking) before any safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (benign PEComa) has an evidence level of L5 — a model score with no supporting clinical trials, literature, or plausible mechanistic pathway; the pack's own rationale text argues against biological plausibility. Combined with the absence of verified original-indication, MOA, and safety data, there is no basis to advance this candidate beyond model output at this time.

**To proceed, the following is needed:**
- TFDA/FDA prescribing information (label warnings, contraindications) — currently a **blocking** gap (DG001)
- Confirmed mechanism of action via DrugBank API query — currently a **High**-severity gap (DG002)
- Verified original approved indication(s) for fedratinib
- If pursuing further research, prioritize the HLH-related candidates (rank 8–9, evidence level L4) over benign PEComa, given their class-effect rationale (ruxolitinib precedent) versus PEComa's lack of any mechanistic or empirical support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


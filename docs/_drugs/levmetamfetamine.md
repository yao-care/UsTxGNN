---
layout: default
title: Levmetamfetamine
parent: 僅模型預測 (L5)
nav_order: 851
evidence_level: L5
indication_count: 2
---

# Levmetamfetamine
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

# Levmetamfetamine: From OTC Nasal Decongestant Use to Nasal Cavity Disease

## One-Sentence Summary

> Levmetamfetamine (DB09571) is the levo-isomer of methamphetamine, best known outside formal regulatory filings as the active ingredient in OTC topical nasal inhalers (e.g., Vicks Vapor Inhaler) for nasal decongestion via sympathomimetic vasoconstriction.
> The TxGNN model predicts it may be relevant to **Nasal Cavity Disease** (score 99.88%) and, secondarily, **Acute Laryngopharyngitis** (score 99.85%),
> but **no clinical trials and no literature** currently support either direction, and the drug holds no marketing license in this dataset.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented in this dataset (no marketed license on file); pharmacologically known as an OTC topical nasal decongestant |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available from this evidence pack. Based on general pharmacological knowledge, Levmetamfetamine is the levo-isomer of methamphetamine, and its activity is dominated by sympathomimetic (indirect/direct α-adrenergic agonist) effects. This pharmacology underlies its established real-world use as an OTC topical nasal decongestant, where it constricts nasal mucosal blood vessels to relieve congestion.

Against this background, the TxGNN prediction for **nasal cavity disease** (score 0.9988, rank 3863) is highly plausible on mechanistic grounds — it likely reflects the knowledge graph capturing an already-existing drug-symptom association (vasoconstrictive decongestant activity mapped to nasal pathology) rather than a genuinely novel therapeutic hypothesis. The secondary prediction, **acute laryngopharyngitis** (score 0.9985, rank 4617), is mechanistically weaker: this condition is primarily an inflammatory/infectious upper-airway process, and its link to Levmetamfetamine's vasoconstrictive action is less direct — the association may arise from anatomical proximity (nasal–pharyngeal) or indirect co-occurrence patterns in the graph rather than specific pharmacology.

Because `original_indications` and `original_moa` are marked as data gaps in this dataset, and no clinical trial or literature evidence was retrieved for either predicted indication, these mechanistic linkages remain **hypothesis-level only** and cannot yet be upgraded to a higher evidence tier.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: A blocking data gap exists — TFDA label warnings/contraindications (DG001) were not retrieved, which prevents this candidate from entering the S1 safety pre-screening stage. A DDI query also returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Both predicted indications are supported only by TxGNN model scores (Evidence Level L5) with zero corroborating clinical trials or literature, and the drug has no marketing license or safety labeling on file, so no S1 safety pre-screening can be completed.

**To proceed, the following is needed:**
- TFDA/FDA package insert warnings and contraindications (currently a **Blocking** data gap, DG001)
- Confirmed mechanism of action from DrugBank (currently a **High**-severity data gap, DG002)
- Drug interaction (DDI) data, currently unretrieved
- At minimum, preclinical or mechanistic literature specifically linking Levmetamfetamine to nasal cavity disease or acute laryngopharyngitis before advancing beyond model-prediction-only status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


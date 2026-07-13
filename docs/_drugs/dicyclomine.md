---
layout: default
title: Dicyclomine
parent: 僅模型預測 (L5)
nav_order: 603
evidence_level: L5
indication_count: 2
---

# Dicyclomine
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

# Dicyclomine: From Gastrointestinal Spasm to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine is a non-selective anticholinergic agent traditionally used to relieve smooth muscle spasm in the gastrointestinal tract, notably in irritable bowel syndrome (IBS).
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
however, **no clinical trials** and **no publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gastrointestinal smooth muscle spasm / Irritable bowel syndrome (IBS) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Registered Licenses | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Dicyclomine is a non-selective muscarinic receptor antagonist (anticholinergic) that reduces smooth muscle spasm by blocking M1–M3 receptors throughout the gastrointestinal tract. Its approved clinical use centers on functional bowel disorders such as IBS.

The TxGNN model appears to have constructed a prediction pathway along the lines of: **Cauda Equina Syndrome (CES) → bladder dysfunction → detrusor overactivity → muscarinic receptor dysregulation → Dicyclomine**. In principle, an antimuscarinic agent could suppress involuntary detrusor contractions by blocking M2/M3 receptors, analogous to the mechanism of oxybutynin in overactive bladder.

However, this mechanistic pathway carries a fundamental clinical concern. In the **acute phase of CES**, bladder dysfunction characteristically presents as **areflexic (atonic) bladder with urinary retention** — the pathophysiological opposite of detrusor overactivity. Administering an anticholinergic agent in this context would further suppress detrusor contractility, potentially worsening urinary retention and causing harm. Anticholinergic therapy could theoretically apply only to the small subset of CES patients in the **recovery phase** who develop secondary detrusor overactivity — a scenario that is rare and for which no direct evidence for Dicyclomine exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Dicyclomine has no registered products in Taiwan. No license records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is rated **L5** — model prediction only — with zero supporting clinical trials or publications. More critically, the proposed mechanism is likely counterproductive in the dominant CES presentation: acute urinary retention from areflexic bladder, where anticholinergic therapy would exacerbate rather than relieve symptoms.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve full pharmacological profile from DrugBank, including muscarinic receptor subtype selectivity (M1/M2/M3 binding affinity vs. oxybutynin)
- **CES subgroup definition**: Identify and characterise the specific CES patient population with documented recovery-phase detrusor overactivity, where anticholinergic therapy has theoretical merit
- **Safety data retrieval**: Download and parse the official package insert (FDA label) for key warnings, contraindications, and drug interactions
- **Preclinical evidence search**: Broaden literature search to include neurogenic bladder models and spinal cord injury data, where Dicyclomine or structural analogues may have been studied
- **Comparative positioning**: Assess whether Dicyclomine offers any advantage over established agents (e.g., oxybutynin, solifenacin) in neurogenic bladder before any further investment is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


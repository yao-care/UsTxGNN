---
layout: default
title: Amifampridine
parent: 僅模型預測 (L5)
nav_order: 324
evidence_level: L5
indication_count: 2
---

# Amifampridine
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

# Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma

## One-Sentence Summary

Amifampridine is a voltage-gated potassium channel (Kv1.1/Kv1.2) blocker originally approved for Lambert-Eaton Myasthenic Syndrome (LEMS), a rare autoimmune neuromuscular junction disorder.
The TxGNN model predicts it may be effective for **Glaucoma**, however **no clinical trials or published literature** currently support this direction.
This is a pure model-driven prediction (L5) with no empirical evidence yet available.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Lambert-Eaton Myasthenic Syndrome (LEMS) |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (no license found in dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Amifampridine (DB11640) is a voltage-gated potassium channel blocker targeting Kv1.1 and Kv1.2 subtypes. By prolonging the neuronal action potential duration, it enhances calcium influx at the presynaptic terminal, thereby increasing acetylcholine release at the neuromuscular junction — the basis for its efficacy in LEMS.

The mechanistic connection to glaucoma is indirect. Glaucoma-relevant potassium channels belong primarily to the inwardly rectifying Kir family (e.g., Kir4.1), which regulate aqueous humor secretion and retinal ganglion cell (RGC) homeostasis. These are a structurally and functionally distinct subfamily from the voltage-gated Kv channels that amifampridine blocks. There is early-stage research suggesting that certain Kv channel modulators may exert neuroprotective effects on RGCs under oxidative stress conditions, which likely forms the graph-level association that TxGNN detected. However, this remains a hypothetical pathway with no direct amifampridine-specific ocular data.

In summary, while the K⁺ channel biology provides a conceptual thread, the Kv↔Kir mechanistic bridge is unvalidated and the prediction is not currently supported by any preclinical, translational, or clinical evidence specific to amifampridine in ocular disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No US NDA licenses were found for Amifampridine in the current dataset.

> **Data note:** Amifampridine phosphate (Firdapse®) is known to have received FDA approval in November 2018 for the treatment of adults with Lambert-Eaton Myasthenic Syndrome. The absence of records here likely represents a data gap in the regulatory query rather than actual non-approval status. The package insert should be consulted for official labeling and safety information.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a purely TxGNN model-driven prediction (Evidence Level L5) with zero supporting clinical trials, published literature, or preclinical ocular studies. The mechanistic link between Kv1.1/Kv1.2 blockade and glaucoma pathophysiology is indirect, relying on a Kv→neuroprotection→RGC hypothesis that has not been tested with amifampridine itself.

**To proceed, the following is needed:**

- **Preclinical proof-of-concept**: In vitro or in vivo studies examining amifampridine's effect on intraocular pressure, aqueous humor dynamics, or RGC survival in glaucoma models
- **Mechanistic clarification**: Whether Kv1.1/Kv1.2 blockade has any measurable effect on Kir4.1-mediated aqueous secretion or RGC excitotoxicity
- **MOA data reconciliation**: Retrieve full DrugBank entry (remediation: DG002) and FDA package insert (remediation: DG001) to close the two blocking data gaps before advancing to safety evaluation (S1 gate)
- **Route feasibility**: Assess whether systemic or topical ocular administration could achieve therapeutically relevant concentrations in the anterior chamber or retina
- **Safety review**: Full DDI and contraindication profile must be established before any further scoring — both DG001 (key warnings/contraindications) and DG002 (MOA) are currently flagged as Blocking/High severity data gaps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Diethylpropion
parent: 僅模型預測 (L5)
nav_order: 604
evidence_level: L5
indication_count: 4
---

# Diethylpropion
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Diethylpropion: From Obesity to Hypervitaminosis

## One-Sentence Summary

Diethylpropion is a sympathomimetic anorectic agent, originally used for short-term management of obesity through appetite suppression via central nervous system stimulation.
The TxGNN model predicts it may be relevant to **Hypervitaminosis** (rank 1 of 4 predicted indications), however mechanistic analysis identifies this as a likely **false-positive signal**,
with **0 clinical trials** and **0 publications** supporting any of the predicted directions.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Obesity / Short-term weight management (pharmacological class; no Taiwan FDA license available) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Diethylpropion belongs to the sympathomimetic amine class — structurally related to amphetamine — and acts on the central nervous system by promoting catecholamine (norepinephrine and dopamine) release, suppressing appetite through hypothalamic regulation. It is a Schedule IV controlled substance in the United States, approved for short-term adjunctive treatment of obesity.

The top-ranked prediction, Hypervitaminosis (vitamin toxicity syndrome), has no mechanistic intersection with appetite suppression. The standard management of hypervitaminosis is cessation of supplement intake — not pharmacological appetite modulation. The suggestion that "appetite suppression reduces intake of high-vitamin foods" is a logical inversion with no clinical applicability. This signal is assessed as a TxGNN knowledge graph false positive arising from distal node associations.

The remaining three predicted indications share the same pattern: **proximal 16p11.2 microdeletion syndrome** (a neurodevelopmental genetic disorder where the obesity phenotype has a gene-dosage origin rather than simple appetite dysregulation), **obsolete hypertelorism** (a structural craniofacial anomaly corrected surgically, with an "obsolete" ontology classification that further reduces its research value), and **frontorhiny** (an extremely rare congenital midline facial malformation caused by ALX1/ALX3 gene mutations, with no pharmacological treatment pathway). None of these predictions reach beyond biological speculation, and none have any supporting clinical or preclinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the four predicted indications.

## Literature Evidence

Currently no related literature available for any of the four predicted indications.

## Taiwan Market Information

Diethylpropion holds no active product licenses with the Taiwan FDA and is currently not marketed in Taiwan. No authorization records are available.

## Safety Considerations

Please refer to the package insert for safety information. Taiwan FDA prescribing information and contraindication data were not retrieved in this evidence collection cycle.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted indications are assessed as L5 false positives — supported by model output alone with zero clinical trials, zero published literature, and no credible mechanistic link to Diethylpropion's known pharmacological action as a sympathomimetic appetite suppressant. The top prediction (Hypervitaminosis) has an explicitly inverse therapeutic logic, and two of the four predicted diseases are structural congenital anomalies that are irreversible by any pharmacological intervention.

**To proceed, the following is needed:**

- Retrieve Taiwan FDA prescribing information (仿單) to complete safety profile and contraindication assessment (currently Blocking data gap DG001)
- Obtain confirmed mechanism of action data from DrugBank API to support any future mechanistic analysis (data gap DG002)
- Re-examine TxGNN prediction quality for this drug: if all top-ranked indications are false positives, consider whether graph embedding distance thresholds or disease ontology filtering (e.g., excluding "obsolete" terms) should be applied upstream
- If further investigation is warranted, explore whether Diethylpropion's established obesity indication could support repurposing queries toward obesity-associated comorbidities (e.g., metabolic syndrome, type 2 diabetes, obstructive sleep apnea) rather than the current structurally implausible predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


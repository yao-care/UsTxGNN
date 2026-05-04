---
layout: default
title: Acetaminophen Aspirin Diphenhydramine
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 0
---

# Acetaminophen Aspirin Diphenhydramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Acetaminophen + Aspirin + Diphenhydramine: Combination Drug — Insufficient Data for Repurposing Assessment

## One-Sentence Summary

Acetaminophen, Aspirin, and Diphenhydramine is a fixed-dose combination commonly used for pain relief with sleep assistance (e.g., nighttime analgesic formulations). The TxGNN model returned **no predicted new indications** for this combination, and the drug is **not registered in the US database** as a unified combination product — making a standard repurposing evaluation infeasible at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no registered product found) |
| Predicted New Indication | None (no TxGNN predictions returned) |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not assessable |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No repurposing prediction is available for this combination. Below is background context on the three components to aid future evaluation.

**Acetaminophen (paracetamol)** is a widely used analgesic and antipyretic. Its exact mechanism is not fully established, but it is believed to inhibit prostaglandin synthesis centrally and may interact with the endocannabinoid system.

**Aspirin (acetylsalicylic acid)** irreversibly inhibits COX-1 and COX-2, reducing prostaglandin synthesis. At low doses it serves as an antiplatelet agent; at higher doses it provides analgesic and anti-inflammatory effects.

**Diphenhydramine** is a first-generation H1 antihistamine with significant anticholinergic and sedative properties, commonly used as a sleep aid in OTC nighttime products.

As a fixed triple-dose combination, this product does not have a registered DrugBank ID, and TxGNN could not perform graph-based repurposing analysis. Each component individually has well-characterized pharmacology, but the combination as a single entity returned no signal in this pipeline run.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific combination.

---

## Literature Evidence

Currently no related literature available for this specific combination under the evaluated evidence pack.

---

## US Market Information

No registered products found for the ACETAMINOPHEN + ASPIRIN + DIPHENHYDRAMINE fixed-dose combination in the queried database.

> **Note:** Individual components (acetaminophen, aspirin, diphenhydramine) are widely marketed separately and in various two-component combinations (e.g., acetaminophen + diphenhydramine as Tylenol PM; aspirin + diphenhydramine as Advil PM equivalents). The specific three-component fixed-dose product was not located in this pipeline run.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Detailed safety data (key warnings, contraindications, drug-drug interactions) were not returned by this pipeline run. For clinical use, the following are known concerns for this combination:
> - **Aspirin**: Contraindicated in children/adolescents with viral illness (Reye's syndrome risk); caution in patients on anticoagulants
> - **Diphenhydramine**: Anticholinergic effects; contraindicated in narrow-angle glaucoma, urinary retention, severe COPD
> - **Acetaminophen**: Hepatotoxicity risk at high doses; avoid in severe hepatic impairment; overlapping products common (risk of unintentional overdose)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This pipeline run returned zero predicted indications, zero registered products, and no safety or MOA data for the three-component combination — there is no actionable repurposing signal to evaluate at this stage.

**To proceed, the following is needed:**

- Confirm whether this combination exists as a registered NDA product under an alternative search strategy (e.g., search by brand name or search each component individually)
- Obtain a DrugBank ID for the combination or run TxGNN predictions for each individual component separately
- Retrieve MOA data for each component from DrugBank API (data gap DG002)
- Retrieve package insert warnings and contraindications (data gap DG001)
- If repurposing analysis is the goal, consider running TxGNN against acetaminophen, aspirin, and diphenhydramine as individual drug nodes and then assess combination potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


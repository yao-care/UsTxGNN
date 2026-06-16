---
layout: default
title: Carbinoxamine
parent: 僅模型預測 (L5)
nav_order: 496
evidence_level: L5
indication_count: 7
---

# Carbinoxamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# CARBINOXAMINE: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Carbinoxamine is a first-generation H1 antihistamine historically approved in the US market for allergic rhinitis and related allergic conditions, though no current product licenses are registered in this dataset.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **0 dedicated clinical trials** and **0 publications** indexed for this specific drug–disease combination — although class-level evidence for first-generation antihistamines in urticaria is well established at L1.
The drug is currently not marketed in Taiwan, and detailed MOA and safety data remain outstanding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis / allergic conditions (historical US approval; no current license in dataset) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Taiwan Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, carbinoxamine is a **first-generation H1 histamine receptor antagonist**. It competitively blocks histamine at H1 receptors, reducing histamine-mediated vasodilation, increased vascular permeability, smooth muscle contraction, and sensory nerve stimulation — all of which are key drivers of allergic symptoms.

Allergic urticaria is caused by mast cell and basophil degranulation releasing histamine into the dermis, producing the characteristic wheal-and-flare reaction. Carbinoxamine's H1 blockade directly interrupts this downstream pathway, preventing histamine from binding to vascular and sensory receptors in the skin. Importantly, first-generation antihistamines as a drug class have L1 RCT evidence for urticaria; the mechanistic rationale is therefore not speculative — carbinoxamine simply lacks its own dedicated trials. Its additional anticholinergic properties may provide modest supplementary benefit by reducing reflex secretory responses.

The biological plausibility is high and the prediction score (99.99%) reflects a well-characterized drug–mechanism–disease alignment. The main caveat is that current international urticaria guidelines (EAACI/GA²LEN) preferentially recommend second-generation antihistamines due to their more favorable sedation and anticholinergic side-effect profiles, meaning any clinical development pathway for carbinoxamine would need to justify its use relative to already-approved alternatives.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for carbinoxamine and allergic urticaria.

---

## Literature Evidence

Currently no related literature available for carbinoxamine and allergic urticaria.

---

## US Market Information

No product licenses found. Carbinoxamine has no registered licenses in the current dataset and is not marketed in Taiwan.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data collection (TFDA package insert warnings and contraindications) is listed as a blocking data gap (DG001) and has not yet been completed. DDI query returned no results. The safety evaluation cannot be finalized until the package insert is retrieved and parsed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model assigns a near-perfect score (99.99%), and the mechanistic link is direct — H1 receptor antagonism is the established pharmacological intervention for histamine-driven urticaria. However, carbinoxamine-specific clinical trial and literature evidence is entirely absent, safety data is incomplete, and the drug is not currently marketed in Taiwan, warranting a cautious and structured development approach before any clinical application.

**To proceed, the following is needed:**
- Retrieve package insert warnings and contraindications from the TFDA official website to complete S1 safety evaluation (Blocking — DG001)
- Obtain detailed MOA data from DrugBank API to strengthen mechanistic analysis (DG002)
- Conduct a broader literature search using carbinoxamine class-level terms (e.g., "first-generation antihistamine" + "urticaria") to assess indirect evidence
- Evaluate comparative advantage versus second-generation antihistamines (e.g., cetirizine, loratadine) already preferred in current urticaria guidelines, and define the patient population where carbinoxamine's sedating profile may be clinically justified
- Map the regulatory pathway for Taiwan market entry, given the current absence of any local product licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


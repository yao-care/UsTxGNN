---
layout: default
title: Acetaminophen Dextromethorphan Hydrobromide Saposh
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 0
---

# Acetaminophen Dextromethorphan Hydrobromide Saposh
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

# Acetaminophen / Dextromethorphan / Saposhnikovia / Tangerine Combination: Repurposing Evaluation Not Feasible

## One-Sentence Summary

This product is a 4-component combination of two conventional Western drugs (acetaminophen and dextromethorphan hydrobromide) and two Traditional Chinese Medicine (TCM) herbs (saposhnikovia divaricata root and tangerine peel), most consistent in profile with a cold and upper respiratory symptom preparation.
The TxGNN model was unable to generate repurposing predictions for this combination — the product holds no US market authorization, and the multi-ingredient TCM-plus-Western formulation could not be resolved to a single DrugBank node in the knowledge graph.
Without prediction outputs, no evidence-based repurposing evaluation can be conducted at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no US market authorization found) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not applicable |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why the Prediction Could Not Be Generated

This combination product contains four active components:

1. **Acetaminophen** — A first-line analgesic and antipyretic; inhibits prostaglandin synthesis centrally to relieve pain and reduce fever.
2. **Dextromethorphan hydrobromide** — A centrally acting antitussive; acts as an NMDA receptor antagonist and sigma-1 receptor agonist to suppress the cough reflex.
3. **Saposhnikovia divaricata root (防風, Fangfeng)** — A TCM herb traditionally indicated for wind-cold syndromes, surface pain relief, and fever; active constituents include chromones and coumarins with documented anti-inflammatory activity.
4. **Tangerine (陳皮/橘皮)** — A TCM herb used to regulate qi, resolve phlegm, and relieve cough; the primary active constituent hesperidin has mild bronchodilatory and anti-inflammatory properties.

Taken together, this is the profile of a **compound cold/flu preparation** combining antipyretic, antitussive, and TCM wind-cold-clearing actions — a formulation class common in East Asian OTC markets.

However, two structural problems block TxGNN pipeline execution:

- **No single DrugBank ID exists** for this four-ingredient combination. The TxGNN knowledge graph operates at the level of individual drug entities; multi-component mixtures cannot be scored directly.
- **No US NDA or equivalent authorization was found**, so no approved indication text is available to anchor the original-indication baseline.

The TCM herbal components (saposhnikovia, tangerine peel) present an additional challenge: they typically lack standardized molecular-target profiles in Western pharmacological databases, making knowledge-graph embedding and prediction technically infeasible without custom entity modeling.

---

## Safety Considerations

No product-level prescribing information is available for this combination as a registered entity. The individual Western medicine components carry the following established safety signals:

- **Acetaminophen**: Dose-dependent hepatotoxicity is the primary concern; FDA-mandated maximum daily dose is 4 g/day in adults (lower in hepatic impairment or chronic alcohol use). Concurrent use with other acetaminophen-containing products must be avoided.
- **Dextromethorphan HBr**: Serotonin syndrome risk with MAO inhibitors (contraindicated combination); CNS and respiratory depression at supratherapeutic doses; misuse potential at high doses (dissociative effects). Caution in patients with hepatic impairment due to CYP2D6-mediated metabolism.

For the TCM herbal components, consult the relevant pharmacopoeia (e.g., Chinese Pharmacopoeia, Taiwan Herbal Medicine Compendium) for documented herb-drug interactions and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This combination cannot be evaluated by the TxGNN pipeline in its current multi-ingredient form — no US NDA registration exists, no DrugBank ID can be assigned to the full combination, and safety data at the product level is absent. Proceeding without these foundations would produce unreliable outputs.

**To proceed, the following is needed:**

- **Disaggregate and evaluate individually**: Submit acetaminophen and dextromethorphan as separate TxGNN candidates, where DrugBank coverage is strong and extensive clinical evidence already exists.
- **Identify any registered equivalent**: Confirm whether this combination is sold under a recognized brand name (domestic or international) that holds a valid NDA or equivalent approval; retrieve the product monograph to establish a formal original indication.
- **Resolve TCM component mapping**: Obtain pharmacokinetic and target-binding profiles for saposhnikovia divaricata root and tangerine peel from validated TCM databases (e.g., TCMSP, HerbMed) to enable knowledge-graph integration.
- **Define repurposing objective**: Clarify which component (or subset) is the intended repurposing candidate — broad combination repurposing is unlikely to yield actionable signals without a focused pharmacological hypothesis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


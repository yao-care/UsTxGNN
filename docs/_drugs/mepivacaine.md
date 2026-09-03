---
layout: default
title: Mepivacaine
parent: 僅模型預測 (L5)
nav_order: 899
evidence_level: L5
indication_count: 2
---

# Mepivacaine
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

# Mepivacaine: From Local Anesthesia to Gastroduodenitis

## One-Sentence Summary

Mepivacaine is an amide-type local anesthetic that blocks voltage-gated sodium channels to produce local/regional sensory blockade. The TxGNN model predicts it may be effective for **Gastroduodenitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own repurposing rationale flags no plausible mechanistic overlap with the target disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local/regional anesthesia (amide-type local anesthetic; no TFDA-approved indication text available — drug is not marketed in Taiwan) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data (`original_moa`) is marked as a data gap in this evidence pack. However, the repurposing rationale supplied with the prediction indicates that mepivacaine is an amide-type local anesthetic whose known pharmacology is blockade of voltage-gated Na⁺ channels on neuronal membranes, suppressing action potential conduction to achieve local sensory blockade.

Gastroduodenitis is a mucosal inflammatory condition, typically driven by *H. pylori* infection, NSAID-induced mucosal injury, or bile reflux — a pathophysiology centered on mucosal damage and acid/inflammatory injury, not on neural conduction. There is no established pharmacological pathway connecting sodium-channel blockade to resolution of gastroduodenal mucosal inflammation. Topical local anesthetics (e.g., viscous lidocaine) are occasionally used for symptomatic pain relief in upper-GI conditions, but this is symptom palliation, not disease-modifying treatment, and no such application has been developed or reported for mepivacaine specifically.

Given this, the high TxGNN score (99.49%) should be interpreted as a knowledge-graph topological similarity signal rather than mechanistic evidence. This is corroborated by the complete absence of clinical trials, ICTRP registrations, or PubMed literature connecting mepivacaine to gastroduodenitis (or to the closely related candidate, peptic ulcer disease — score 99.41%, same L5/Hold status, same absence of mechanistic overlap with acid/H. pylori-driven pathology).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No approved licenses on record — mepivacaine is not marketed in this jurisdiction (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label/warning data for mepivacaine is currently an unresolved, blocking data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on TxGNN's knowledge-graph score (L5), with zero clinical trials, zero literature, and no plausible mechanistic link — the rationale itself concludes that sodium-channel blockade has no known pathway to gastroduodenal mucosal inflammation. Combined with the drug's not being marketed in Taiwan and missing TFDA safety labeling, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/FDA package insert warnings and contraindications — required before any S1 safety evaluation can begin
- Resolve DG002: obtain a verified mechanism-of-action source (e.g., DrugBank API) to formally document MOA rather than relying on inferred rationale text
- Any future preclinical or mechanistic studies linking local anesthetics to GI mucosal inflammation, should they emerge
- Re-run clinical trial/literature searches periodically, as current searches (2026-04-21) returned zero results across ClinicalTrials.gov, ICTRP, and PubMed for both candidate indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


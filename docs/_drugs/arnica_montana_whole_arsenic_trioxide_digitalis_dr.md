---
layout: default
title: Arnica Montana Whole Arsenic Trioxide Digitalis Dr
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 0
---

# Arnica Montana Whole Arsenic Trioxide Digitalis Dr
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

# Homeopathic Cardiac Combination (12-Component): Insufficient Data for Repurposing Analysis

## One-Sentence Summary

This 12-component formulation — comprising botanical and mineral ingredients including Digitalis, Nitroglycerin, Hawthorn, and Arsenic Trioxide — appears to be a homeopathic cardiovascular preparation, but no original indication, regulatory approval, or DrugBank record could be confirmed.
The TxGNN model returned **no predicted indications** for this compound as submitted,
making a standard drug repurposing evaluation impossible with currently available data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Unknown — no regulatory record found |
| Predicted New Indication | None (TxGNN returned no results) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No actual studies; model returned no output |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No predicted indication was returned by TxGNN, so a formal mechanistic rationale for repurposing cannot be established. However, examining the 12 individual components reveals a pattern strongly consistent with a **homeopathic cardiac tonic**:

| Component | Traditional / Pharmacological Role |
|---|---|
| Digitalis | Cardiac glycoside source; used in heart failure and atrial fibrillation |
| Drimia maritima (Sea Squill) | Cardiotonic glycosides; historical use in cardiac oedema |
| Nitroglycerin | Nitrate vasodilator; standard angina pectoris therapy |
| Hawthorn (Crataegus) leaf with flower | Evidence-based use in mild-to-moderate cardiac insufficiency |
| Selenicereus grandiflorus (Night-blooming Cereus) | Classical homeopathic cardiotonic for palpitations and angina |
| Spigelia marilandica | Classical homeopathic remedy for cardiac neuralgias |
| Arnica montana | Homeopathic anti-inflammatory; cardiovascular use in homeopathy |
| Gelsemium sempervirens | Homeopathic nervine; used for functional cardiac symptoms |
| Arsenic trioxide | At pharmacological doses: antineoplastic (APL); as Arsenicum album in homeopathy: cardiovascular/general tonic |
| Kalmia latifolia | Homeopathic use in pericarditis and rheumatic cardiac disease |
| Potassium carbonate (Kali carbonicum) | Homeopathic use in cardiac weakness and oedema |
| Phosphorus | Homeopathic use in circulatory and hepatic conditions |

This composition closely resembles commercial homeopathic cardiac preparations (e.g., Cor Compositum by Biologische Heilmittel Heel). Without a DrugBank ID, confirmed dilution factors, MOA data, or TxGNN output, no evidence-based mechanistic rationale for repurposing can be made at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No regulatory approvals found in the provided dataset (0 licenses, market status: Not marketed).

---

## Cytotoxicity

This section is included because the formulation contains **Arsenic Trioxide** — a confirmed antineoplastic agent approved at pharmacological doses for acute promyelocytic leukemia (APL).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Context-dependent: pharmacological Arsenic Trioxide (Trisenox®) = conventional cytotoxic / differentiation agent; homeopathic dilution — cytotoxic risk is presumed negligible but not confirmed |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | If arsenic trioxide is present at pharmacological levels: ECG (QTc), CBC, liver/renal function, serum electrolytes (K⁺, Mg²⁺) |
| Handling Protection | Dilution level not specified in Evidence Pack — cannot confirm whether cytotoxic handling regulations apply; clarification required |

> ⚠️ **Critical Data Gap:** The Evidence Pack does not specify the homeopathic dilution potency (e.g., D6, C30) for Arsenic Trioxide or other potentially toxic components (Digitalis, Nitroglycerin). Until dilution levels are confirmed, the safety classification of this preparation cannot be finalised.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on high-risk components:** Even in homeopathic dilution, the following ingredients carry known pharmacological toxicity at non-diluted doses and should be verified:
> - **Arsenic Trioxide**: QTc prolongation, differentiation syndrome, hepatotoxicity
> - **Digitalis**: Narrow therapeutic index; digitalis toxicity (bradycardia, AV block, arrhythmia)
> - **Nitroglycerin**: Hypotension, reflex tachycardia
> - **Gelsemium sempervirens**: Contains gelsemine (CNS/respiratory depressant at non-diluted doses)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no predicted indications for this multi-component combination as a single query, and foundational data — including DrugBank ID, original indication, mechanism of action, and safety records — are entirely absent. A meaningful repurposing evaluation cannot proceed without resolving these gaps.

**To proceed, the following is needed:**

- **Confirm product identity**: Identify the commercial product name and manufacturer; obtain the full package insert to confirm indication, dosage form, and dilution potencies for each ingredient
- **Document dilution factors**: Confirm homeopathic potency (e.g., D6, C200) for all 12 components to determine whether cytotoxic handling precautions apply (especially for Arsenic Trioxide)
- **Disaggregate the query**: Submit each pharmacologically active component individually to TxGNN (prioritising Arsenic Trioxide, Digitalis glycosides, and Crataegus extract) to obtain interpretable prediction scores
- **Obtain DrugBank IDs**: At minimum for Arsenic Trioxide (DB01169), Digoxin/Digitalis, Nitroglycerin (DB00727), and Hawthorn extract
- **Regulatory search expansion**: Extend search to US FDA (Homeopathic Drug Products), EU HMPC monographs, and German Commission E monographs which are the primary regulatory frameworks for this class of product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Doxercalciferol
parent: 僅模型預測 (L5)
nav_order: 625
evidence_level: L5
indication_count: 1
---

# Doxercalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Doxercalciferol: Original Indication Not on Record → Predicted Vitamin D Deficiency

## One-Sentence Summary

Doxercalciferol (DrugBank DB06410) currently has no approved indication or market license on file in this evidence pack, and detailed mechanism-of-action data has not yet been retrieved. The TxGNN model predicts a link to **"obsolete vitamin D deficiency"** with a very high raw score, but this disease term is itself flagged as *obsolete* in the underlying ontology, and **zero clinical trials, zero ICTRP trials, and zero publications** currently support this direction — this is a preliminary, unverified signal, not a validated repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record — no approved indications or licenses are documented for this drug in Taiwan |
| Predicted New Indication | Obsolete vitamin D deficiency *(disease term flagged as obsolete in source ontology)* |
| TxGNN Prediction Score | 99.48% (raw score 0.9948; internal rank 12,348) |
| Evidence Level | L5 — model prediction only, no supporting studies |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for the drug record itself is not yet available (data gap DG002, DrugBank API lookup pending). However, the model's own repurposing rationale notes that doxercalciferol is a vitamin D2 prodrug that is hepatically 25-hydroxylated to its active form, which binds and activates the Vitamin D Receptor (VDR).

Based on this mechanistic description, the predicted link to "vitamin D deficiency" overlaps almost completely with the drug's core, already-known pharmacology — it reads as a restatement of the drug's own mechanism rather than a novel repurposing hypothesis. In other words, the model may simply be recognizing that a vitamin D analog activates the vitamin D pathway, which is expected and not clinically informative on its own.

Compounding this, the predicted disease node is explicitly marked **"obsolete"**, suggesting the term may have been deprecated or merged with another concept in the source ontology (e.g., MONDO/UMLS). Combined with the complete absence of clinical trials or literature evidence, the underlying data quality for this specific prediction should be verified before any further evaluation proceeds.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Doxercalciferol is currently **not marketed** in Taiwan, with no licenses on record (0 total). No product name, dosage form, or approved-indication data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are not yet available in this evidence pack — TFDA label warnings/contraindications are flagged as a **blocking** data gap, DG001, required before any safety pre-screening can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) with zero supporting clinical trials or literature, and the predicted disease term itself is flagged as obsolete/potentially unreliable in the source ontology.
- The drug is not currently marketed in Taiwan (0 licenses), and a blocking safety data gap (TFDA label warnings/contraindications) prevents progression to the S1 safety pre-screening stage.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the TFDA package insert for warnings/contraindications.
- Resolve DG002 (High): query DrugBank for confirmed mechanism-of-action data.
- Verify whether "obsolete vitamin D deficiency" maps to a current, valid disease concept before treating this as a genuine repurposing candidate.
- If the disease mapping is confirmed valid, initiate targeted clinical trial and literature searches specific to the corrected disease term.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


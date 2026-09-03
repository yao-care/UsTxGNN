---
layout: default
title: Rufinamide
parent: 僅模型預測 (L5)
nav_order: 1138
evidence_level: L5
indication_count: 5
---

# Rufinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Rufinamide: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome (FIRES)

## One-Sentence Summary

Rufinamide is a triazole-derivative anticonvulsant, publicly known as an adjunctive therapy for seizures associated with Lennox-Gastaut Syndrome; no Taiwan-specific approved indication text is available in this evidence pack.
The TxGNN model predicts it may be effective for **Febrile Infection-Related Epilepsy Syndrome (FIRES)**, a rare and severe epileptic encephalopathy.
Currently, **0 clinical trials** and **0 publications** support this specific direction — this is a model-prediction-only candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan regulatory data (drug not marketed in Taiwan). Publicly known global indication: Lennox-Gastaut Syndrome (adjunctive therapy) |
| Predicted New Indication | Febrile Infection-Related Epilepsy Syndrome (FIRES) |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on generally known information, rufinamide is a triazole-derivative antiepileptic drug that modulates voltage-gated sodium channels, prolonging their inactive state and limiting repetitive neuronal firing. It is broadly recognized as an adjunctive treatment for seizures associated with Lennox-Gastaut Syndrome, a severe, treatment-resistant childhood epileptic encephalopathy.

FIRES, the top-ranked predicted indication, is likewise a rare and catastrophic epileptic encephalopathy characterized by refractory status epilepticus following a febrile illness. Mechanistically, both conditions involve widespread cortical hyperexcitability that is poorly controlled by conventional first-line anticonvulsants, which provides a plausible biological rationale for testing broad-spectrum sodium-channel modulators such as rufinamide in FIRES.

That said, this rationale is currently supported only by TxGNN's knowledge-graph inference (score 99.57%, rank 10564) — there are no registered clinical trials, ICTRP entries, or published literature in this evidence pack that directly evaluate rufinamide in FIRES. The prediction should be interpreted as a hypothesis-generating signal rather than clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No license records are available. The evidence pack indicates rufinamide currently has 0 approved licenses and is not marketed in Taiwan (TFDA); a formal safety review is blocked pending retrieval of the package insert (see Data Gap DG001).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (FIRES) is currently supported only by a TxGNN model score with no corroborating clinical trials or literature (Evidence Level L5), and critical safety data (TFDA warnings/contraindications, mechanism of action) are marked as blocking data gaps. Proceeding to any evaluation stage beyond S0 is not appropriate at this time.

**To proceed, the following is needed:**
- TFDA (or originator) package insert — warnings, contraindications, DDI profile (Data Gap DG001, Blocking)
- Confirmed mechanism of action detail from DrugBank or primary pharmacology literature (Data Gap DG002)
- Targeted literature/case-report search specifically on rufinamide use in FIRES or related refractory status epilepticus syndromes
- Monitoring of clinicaltrials.gov / ICTRP for any newly registered trials in this indication

*Note: TxGNN also flagged four additional rare epilepsy syndromes (perioral myoclonia with absences, photosensitive occipital lobe epilepsy, cryptogenic late-onset epileptic spasms, atypical childhood epilepsy with centrotemporal spikes) as lower-ranked candidates — all similarly at Evidence Level L5 / Stage S0 / Hold, with no supporting clinical or literature evidence.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Aluminum Sesquichlorohydrate
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 0
---

# Aluminum Sesquichlorohydrate
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

# Aluminum Sesquichlorohydrate: Drug Repurposing Assessment — Insufficient Data to Generate Prediction

## One-Sentence Summary

Aluminum Sesquichlorohydrate is an aluminum salt compound commonly used as an active ingredient in antiperspirant/deodorant formulations, acting by temporarily blocking sweat ducts. The TxGNN model returned **no repurposing predictions** for this compound, and no Taiwan FDA marketing authorizations were found. With zero clinical trial or literature evidence linked to any predicted indication, this candidate cannot advance to evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no marketing authorizations on record) |
| Predicted New Indication | None — TxGNN returned no candidates |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — no predictions generated) |
| Taiwan Market Status | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

Aluminum Sesquichlorohydrate (Al₂Cl₃(OH)₃) is a partially neutralized aluminum chloride salt. Its primary known mechanism is the formation of a physical plug within eccrine sweat gland ducts, reducing sweat secretion — a purely local, topical mechanism with no systemic pharmacological target.

The absence of TxGNN predictions is mechanistically consistent: the TxGNN knowledge graph operates on systemic drug–target–disease relationships. A compound with no identified systemic protein targets (receptor, enzyme, transporter) and no DrugBank ID will not generate meaningful graph traversal paths, resulting in an empty candidate list.

Additionally, no Taiwan FDA license data was retrieved, meaning there is no approved indication from which to anchor a repurposing trajectory.

---

## Safety Considerations

No safety data — including warnings, contraindications, or drug–drug interactions — was returned from any queried source. Please refer to the product package insert and official regulatory monographs for safety information before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no TxGNN-predicted indications, no regulatory approvals, no DrugBank identifier, and no mechanism-of-action data on file. There is no scientific basis on which to conduct a repurposing analysis at this time.

**To proceed, the following is needed:**

- **Obtain a DrugBank ID** — Query DrugBank by synonyms (e.g., Aluminium chlorohydrex, Al₂Cl₃(OH)₃) to establish a structured pharmacological profile and enable TxGNN graph linkage.
- **Define a systemic MOA** — If the compound has any systemic targets beyond topical sweat-duct occlusion (e.g., aluminum ion–mediated signaling), document them to enable knowledge graph traversal.
- **Re-run TxGNN prediction** — Once a DrugBank ID and target profile are established, re-execute the prediction pipeline to determine whether any disease nodes are reachable.
- **Review TFDA package insert** — Download and parse the official monograph PDF to fill the blocking safety data gap (DG001) before any S1 safety screening can proceed.
- **Confirm intended scope** — Clarify whether this compound is being evaluated as a standalone systemic agent or as part of a formulation; if the latter, the parent active ingredient (e.g., aluminum chloride) may be the more appropriate query target.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


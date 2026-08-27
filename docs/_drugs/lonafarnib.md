---
layout: default
title: Lonafarnib
parent: 僅模型預測 (L5)
nav_order: 868
evidence_level: L5
indication_count: 1
---

# Lonafarnib
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

# Lonafarnib: From Progeria/Hepatitis D to Leprosy

## One-Sentence Summary

Lonafarnib is a farnesyltransferase inhibitor used clinically for Hutchinson-Gilford Progeria Syndrome (HGPS) and studied for chronic hepatitis D virus (HDV) infection. The TxGNN model predicts it may be effective for **Leprosy**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph inference with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hutchinson-Gilford Progeria Syndrome (HGPS) / chronic HDV infection (per mechanism description in the evidence pack; no formal Taiwan license record exists) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lonafarnib was not retrievable from DrugBank in this evidence pack (flagged as a High-severity data gap, DG002). However, the model's own rationale notes that lonafarnib is a **farnesyltransferase inhibitor**: it blocks farnesylation of the RAS protein and prelamin A (the basis for its use in HGPS), and separately blocks farnesylation of the HDV large delta antigen (L-HDAg), which underlies its investigational use against hepatitis D.

Leprosy is caused by *Mycobacterium leprae*, a bacterium whose pathogenic mechanisms (cell-wall synthesis, invasion of macrophages and Schwann cells) have no known connection to the host farnesyltransferase pathway that lonafarnib targets. No mechanistic, preclinical, or clinical literature linking lonafarnib to leprosy was found in this evidence pack's searches.

Given this, the prediction should be treated as a **speculative model association** rather than a mechanistically grounded hypothesis — it likely arises from indirect semantic pathways in the knowledge graph (e.g., "anti-infective" or "dermatology" adjacency) rather than a genuine biological link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Lonafarnib is not currently marketed in Taiwan — no TFDA license records exist (`total_licenses = 0`). TFDA label/warning data is also unavailable and is flagged as a Blocking data gap (DG001), which prevents any Stage 1 safety pre-assessment.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is evidence level L5 — a model-only inference with zero supporting clinical trials or literature, and no plausible mechanistic overlap between lonafarnib's known farnesyltransferase-inhibition activity and leprosy pathogenesis. There is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA label / package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed DrugBank mechanism-of-action record for lonafarnib
- Any preclinical or in vitro data testing farnesyltransferase inhibition against *M. leprae* or leprosy-relevant pathways
- Continued monitoring for new clinical trial or literature evidence before reconsidering this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


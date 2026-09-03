---
layout: default
title: Oxybutynin
parent: 僅模型預測 (L5)
nav_order: 1004
evidence_level: L5
indication_count: 3
---

# Oxybutynin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Oxybutynin: From [Original Indication Not Documented] to Restless Legs Syndrome

## One-Sentence Summary

> Oxybutynin (DrugBank DB01062) is an M3 muscarinic receptor antagonist / musculotropic antispasmodic agent; however, no formal original indication record is available in this evidence pack, and the drug is currently **not marketed** in the target jurisdiction.
> The TxGNN model predicts it may be effective for **Restless Legs Syndrome**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — evidence level **L5**, model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no license or approved-indication text available; drug's formal indication history is a Blocking data gap) |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (Data Gap DG002, severity High). Based on information embedded in the TxGNN evidence pack's own rationale text, oxybutynin is described as an **M3 muscarinic receptor antagonist** and a musculotropic antispasmodic agent, historically associated with antispasmodic activity on smooth muscle (notably bladder smooth muscle). This is the only mechanistic characterization available; no confirmed original-indication text or approved label exists in this pack.

The evidence pack itself is explicit that the mechanistic link between oxybutynin and restless legs syndrome (RLS) is **weak and unsupported**: RLS pathophysiology is primarily driven by dopaminergic dysfunction and iron metabolism abnormalities, which have no known direct relationship to anticholinergic/antimuscarinic activity. The pack states this prediction arises purely from TxGNN's knowledge-graph association pattern, **without a credible mechanistic hypothesis** to justify it clinically.

Given the absence of any supporting clinical trial or literature evidence, and the internally-acknowledged mechanistic mismatch, this candidate should be treated as a hypothesis-generating signal only, not a basis for further pharmacological reasoning at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

This drug currently has no license/NDA records in the evidence pack (`total_licenses: 0`); market status is **Not Marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/FDA label warnings and contraindications are listed as a Blocking data gap — DG001 — meaning a full safety evaluation cannot yet be performed for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting oxybutynin for restless legs syndrome, and the pack's own rationale identifies no credible mechanistic link between the drug's anticholinergic action and RLS pathophysiology. Combined with missing label/safety data (Blocking gap) and missing MOA confirmation (High-severity gap), this candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/FDA label warnings and contraindications before any safety screening (S1) can occur
- Resolve DG002: confirm formal mechanism of action via DrugBank API
- Independent pharmacological or preclinical rationale connecting anticholinergic activity to dopaminergic/iron-related RLS pathophysiology
- At minimum, case reports or observational data specifically evaluating oxybutynin in RLS populations

*Note: Within the same evidence pack, the rank-3 candidate (peptic ulcer disease) has more supporting literature (3 publications, evidence level L4, decision stage S1) than this top-ranked candidate, though it also carries an internal mechanistic contradiction (oxybutynin is separately reported to induce reflux esophagitis by lowering lower esophageal sphincter tone) and should be evaluated as a separate research question if pursued.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


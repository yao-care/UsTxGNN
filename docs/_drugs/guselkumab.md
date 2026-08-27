---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 765
evidence_level: L5
indication_count: 10
---

# Guselkumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Guselkumab: From Psoriasis to Drug-Induced Osteoporosis

## One-Sentence Summary

Guselkumab is an anti-IL-23(p19) monoclonal antibody, originally developed and approved (as Tremfya) for immune-mediated inflammatory diseases such as psoriasis and ulcerative colitis. The TxGNN model's top-ranked prediction for this candidate is **Drug-Induced Osteoporosis**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it reflects knowledge-graph proximity rather than any actual evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in TFDA data for this pack (Taiwan query returned 0 results); other candidate entries in this evidence pack reference Psoriasis and Ulcerative Colitis as Tremfya's already-approved original indications |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.84% (rank 4814) |
| Evidence Level | L5 |
| US Market Status | 未上市 (not marketed / no TFDA license found) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (data gap DG002). Based on the information that is available, guselkumab is a selective IL-23(p19) inhibitor; its efficacy in immune-mediated inflammatory conditions (psoriasis, ulcerative colitis) is documented elsewhere in this same evidence pack via other candidate indications, and mechanistically it acts by suppressing the IL-23/Th17 axis.

For the top-ranked prediction, drug-induced osteoporosis, the rationale supplied is explicitly weak: there is no direct mechanistic evidence linking IL-23 inhibition to bone loss. Osteoimmunology literature suggests an indirect relationship between the IL-23/Th17 axis and osteoclast activation, but no study has specifically connected guselkumab to drug-induced osteoporosis. The high TxGNN score most likely reflects the proximity of immune- and bone-metabolism-related nodes within the knowledge graph rather than a causal or clinical signal.

Because psoriasis (rank 3) and ulcerative colitis (rank 6) in this same evidence pack are described as guselkumab's already-approved indications with strong supporting evidence (L1, Proceed with Guardrails), the drug-induced osteoporosis prediction should be interpreted as a low-confidence, exploratory signal — not a validated repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Guselkumab currently has no TFDA license on record in this evidence pack (market status: 未上市, total licenses: 0). No authorization data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications for this drug are marked as a Blocking data gap — DG001 — and could not be retrieved for this evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for drug-induced osteoporosis has no supporting clinical trials or literature (Evidence Level L5, Decision Stage S0) and only a speculative, indirect mechanistic rationale. The TxGNN score alone is insufficient to justify advancing this candidate.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap DG001) before any safety pre-screen (S1) can begin
- Confirmed mechanism of action data (DG002) to assess mechanistic plausibility
- Preclinical or mechanistic studies specifically evaluating IL-23 inhibition and bone metabolism/osteoclast activity
- If pursuing guselkumab repurposing at all, prioritize the higher-evidence candidates already surfaced in this pack (psoriasis, ulcerative colitis) rather than this L5 signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


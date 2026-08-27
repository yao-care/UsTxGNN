---
layout: default
title: Ivosidenib
parent: 僅模型預測 (L5)
nav_order: 822
evidence_level: L5
indication_count: 3
---

# Ivosidenib
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

# Ivosidenib: From IDH1-Mutant AML to Treatment-Related AML/MDS (Alkylating Agent- and Radiation-Related)

## One-Sentence Summary

> Ivosidenib (DB14568) is an oral IDH1 (R132-mutant) inhibitor with established approval for IDH1-mutant acute myeloid leukemia and cholangiocarcinoma.
> The TxGNN model predicts it may also be effective for **treatment-related AML/MDS** (subtypes linked to prior alkylating-agent or radiation exposure),
> but this prediction currently rests **on mechanistic extrapolation alone — zero clinical trials and zero publications** were found for either subtype.

*Note on the model's top-ranked output:* TxGNN's single highest-scoring prediction for this drug was "bulbar polio" (score 99.31%). The evidence pack's own rationale flags this as a likely knowledge-graph artifact with no plausible biological link to an IDH1 inhibitor, and explicitly recommends against investing further resources in it. It is therefore excluded from this report as the lead candidate; the two treatment-related AML/MDS predictions (tied at rank 2–3, both mechanistically coherent with the drug's known target) are used instead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | IDH1-mutant AML / cholangiocarcinoma *(from public prescribing background referenced in the model rationale; not present in the structured evidence fields — see Data Gap DG002 below)* |
| Predicted New Indication | Treatment-related (alkylating agent- and radiation-related) AML/MDS |
| TxGNN Prediction Score | 99.26% (both subtypes) |
| Evidence Level | L4 (mechanism-based; no clinical trials or literature identified) |
| TW Market Status | 未上市 (Not Marketed) |
| Number of Licenses (NDAs) | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ivosidenib is not available in this evidence pack (Data Gap DG002). Based on known information reflected in the model's own rationale, ivosidenib is an oral, targeted inhibitor of mutant IDH1 (R132), approved for IDH1-mutant AML and cholangiocarcinoma; its efficacy in IDH1-mutant AML has been clinically established.

Treatment-related AML/MDS (t-AML/t-MDS) — including the alkylating-agent-related and radiation-related subtypes predicted here — is a recognized clinical entity that arises after prior cytotoxic chemotherapy or radiotherapy. It falls under the broader AML/MDS disease category and can, like de novo AML, harbor IDH1 R132 mutations. Because ivosidenib's approved mechanism targets the mutant enzyme itself rather than the AML's etiology, the pharmacological rationale for activity in IDH1-mutant t-AML/t-MDS is a reasonably direct extrapolation from the approved indication.

That said, this is mechanistic extrapolation only: neither subtype has any registered trial or published study in this evidence pack confirming clinical activity, and the underlying prevalence of IDH1 mutations specifically within treatment-related AML/MDS populations is not established here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US/TW Market Information

No license or marketing authorization records are available — ivosidenib is currently **not marketed in Taiwan** (0 licenses on file).

---

## Cytotoxicity

Ivosidenib is an antineoplastic agent (approved for IDH1-mutant AML/cholangiocarcinoma; targeted enzyme-inhibitor mechanism).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mutant IDH1 R132 enzyme inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label/warning data for this drug is flagged as a Blocking data gap — DG001 — meaning no independent S1 safety assessment could be performed for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted treatment-related AML/MDS indication has plausible mechanistic support but no supporting clinical trials or literature, and the drug is not currently marketed in Taiwan. A blocking data gap on TFDA safety labeling (DG001) also prevents a proper initial safety assessment (S1), so this candidate cannot advance past the research-question stage yet.

**To proceed, the following is needed:**
- TFDA label / warnings and contraindications (DG001 — Blocking)
- Confirmed original MOA and approved-indication documentation for ivosidenib (DG002)
- Literature search on IDH1 R132 mutation prevalence specifically within alkylating-agent- and radiation-related AML/MDS populations
- Any available preclinical or case-level evidence of ivosidenib activity in treatment-related AML/MDS before considering formal clinical investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


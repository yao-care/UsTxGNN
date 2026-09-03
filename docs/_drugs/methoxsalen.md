---
layout: default
title: Methoxsalen
parent: 僅模型預測 (L5)
nav_order: 912
evidence_level: L5
indication_count: 10
---

# Methoxsalen
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

# Methoxsalen: From Cutaneous T-Cell Lymphoma Photopheresis to Localized Pagetoid Reticulosis

## One-Sentence Summary

Methoxsalen is a psoralen photosensitizer whose established clinical use (via extracorporeal photopheresis, ECP/UVADEX) targets circulating malignant T-cells in cutaneous T-cell lymphoma (CTCL). The TxGNN model's top-ranked prediction is **Localized Pagetoid Reticulosis**, a rare, localized CTCL subtype, but this specific prediction currently has **no registered clinical trials and no supporting literature** — it rests on class-effect extrapolation from methoxsalen's known CTCL biology rather than direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — methoxsalen is not currently marketed in Taiwan and no approved-indication record exists. (Contextual note: evidence embedded in the pack describes methoxsalen/8-MOP as the basis of extracorporeal photopheresis, an established CTCL treatment.) |
| Predicted New Indication | Localized Pagetoid Reticulosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Market Status (Taiwan) | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for methoxsalen is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded elsewhere in the pack, methoxsalen (8-MOP) is a furocoumarin (psoralen) photosensitizer: once activated by UVA light, it forms covalent crosslinks with DNA pyrimidine bases, halting proliferation of the exposed cells. This photoactivated DNA-crosslinking mechanism is the pharmacological basis of extracorporeal photopheresis (ECP), an established treatment for the circulating malignant T-cells of cutaneous T-cell lymphoma.

Localized Pagetoid Reticulosis is a rare, indolent, localized subtype within the mycosis fungoides/CTCL disease spectrum — the same disease family that ECP already addresses. This gives the prediction mechanistic plausibility: the anti-proliferative, DNA-damaging photochemotherapy effect that clears malignant T-cells elsewhere in CTCL could plausibly extend to this localized variant.

However, this rationale is a **class-effect extrapolation, not direct evidence** — no trials or publications specific to this subtype exist yet. For context, a related and broader prediction in the same evidence pack, "indolent primary cutaneous T-cell lymphoma" (rank 2), is supported by 2 literature citations and carries a stronger evidence rating (L2, "Proceed with Guardrails"), reinforcing that methoxsalen's CTCL-photopheresis mechanism is real and applicable — just not yet demonstrated for this particular localized subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No Taiwan market authorization records are available — methoxsalen is not currently marketed in Taiwan (0 licenses on file), so no NDA/product table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although methoxsalen's DNA-crosslinking, photoactivated mechanism gives this prediction biological plausibility, Localized Pagetoid Reticulosis has zero direct trials or literature — evidence level L4 reflects mechanistic reasoning only, not demonstrated efficacy in this specific indication.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (Blocking data gap — required before any S1 safety screening can proceed)
- Full mechanism of action documentation for methoxsalen (DrugBank API lookup)
- Dedicated case series or pilot data specific to localized pagetoid reticulosis, rather than class-effect extrapolation from broader CTCL/ECP use
- Confirmation of a Taiwan registration pathway, since the drug is not currently marketed (0 licenses)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 688
evidence_level: L5
indication_count: 6
---

# Evolocumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Evolocumab: From Hypercholesterolemia to Symptomatic Hemophilia in Female Carriers

## One-Sentence Summary

Evolocumab is a PCSK9-inhibitor monoclonal antibody generally known for lowering LDL cholesterol in hypercholesterolemia/dyslipidemia (this original-indication context is general drug knowledge, not present in the evidence pack itself).
The TxGNN model predicts it may be effective for **symptomatic form of hemophilia in female carriers**,
but this is currently a **model-only prediction (L5)** — **zero clinical trials** and **zero publications** support the association, and the model's own mechanistic review found no identifiable biological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (`original_indications` and `licenses` are both empty). Evolocumab is generally known as a PCSK9-inhibitor for hypercholesterolemia/dyslipidemia. |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Market Status (Taiwan) | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a blocking/high-severity gap in this evidence pack (DG002). Based on the evidence pack's own repurposing rationale, evolocumab inhibits PCSK9, which prevents degradation of the hepatic LDL receptor, thereby lowering LDL cholesterol — a lipid-metabolism pathway.

The predicted new indication, symptomatic hemophilia in female carriers, is a coagulation-factor disorder governed by an entirely separate pathway (clotting factor deficiency, not lipid/LDL receptor biology). The evidence pack's own mechanistic assessment is explicit that **no identifiable mechanistic link exists** between PCSK9 inhibition and clotting-factor pathology, and attributes the high TxGNN score to embedding-space statistical similarity rather than a biological relationship.

In short, this candidate does not currently have a plausible mechanistic rationale — it should be treated as a low-confidence, model-only signal rather than a biologically supported repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

No marketing authorizations found — evolocumab is currently not marketed in Taiwan (0 licenses on record).

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA label warnings/contraindications are marked as a blocking data gap (DG001) in this evidence pack — this information has not yet been retrieved.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN similarity score (L5, no clinical or literature evidence), and the evidence pack's own mechanistic review found no biologically plausible link between PCSK9 inhibition and coagulation-factor pathology. A blocking data gap (missing TFDA label/warnings) also prevents entry into safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (DG001, blocking)
- Detailed mechanism-of-action data (DG002)
- Independent biological/mechanistic plausibility review before committing further evaluation resources
- Any preclinical or case-level evidence connecting PCSK9 pathway activity to coagulation-factor disorders, should it emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Elapegademase
parent: 僅模型預測 (L5)
nav_order: 646
evidence_level: L5
indication_count: 10
---

# Elapegademase
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

# Elapegademase: From ADA-SCID to Diabetic Retinopathy

## One-Sentence Summary

Elapegademase is a PEGylated recombinant adenosine deaminase (ADA) enzyme replacement therapy used exclusively for ADA-SCID (adenosine deaminase deficiency – severe combined immunodeficiency). The TxGNN model predicts it may be effective for **Diabetic Retinopathy**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ADA-SCID (enzyme replacement therapy) — not present in Taiwan/US regulatory license data (drug is unmarketed) |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (MOA field is a data gap). Based on known pharmacology, elapegademase is an enzyme replacement therapy that metabolizes deoxyadenosine to prevent its toxic accumulation in lymphocytes — its only established use is ADA-SCID.

Diabetic retinopathy's underlying pathology is hyperglycemia-driven VEGF upregulation, oxidative stress, and microvascular damage. There is no known biological pathway connecting ADA enzyme replacement to retinal microvascular disease, and the evidence pack's own analysis flags this gap explicitly.

Notably, all 10 of this drug's top predicted indications (diabetic retinopathy, diabetic cataract, severe nonproliferative diabetic retinopathy, cortical cataract, nuclear senile cataract, T2DM-associated cataract, mature cataract, tetanic cataract, immature cataract, craniostenosis cataract) cluster in a narrow score band (0.9937–0.9945) and share no coherent mechanistic theme — spanning diabetic, senile, metabolic, and congenital cataract etiologies indiscriminately. This pattern, combined with the drug having zero other indication or DDI links in the knowledge graph, is consistent with a sparse-node embedding artifact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Elapegademase is not marketed in Taiwan and has no registered NDA/license records in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label/warning data for this drug is flagged as a Blocking data gap — it must be resolved before any safety-stage [S1] evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (L5, model score only), and the proposed mechanism has no known biological link to the original ADA-SCID indication. The uniform high-score cluster across 10 unrelated ophthalmic/metabolic indications for this same sparse-node drug further suggests the signal is a knowledge-graph artifact rather than a real repurposing lead.

**To proceed, the following is needed:**
- TFDA label/warning and contraindication data (currently Blocking — required before any S1 safety review)
- Confirmed mechanism of action (MOA) data from DrugBank
- Independent mechanistic or preclinical rationale linking ADA enzyme replacement to diabetic retinopathy before further evidence collection is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


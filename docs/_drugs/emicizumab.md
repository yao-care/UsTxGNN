---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: From Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Emicizumab (DrugBank DB13923) is a bispecific monoclonal antibody described in the literature as a factor VIIIa mimetic used for bleeding prophylaxis in hemophilia A. The TxGNN model's top-ranked prediction for this drug is **Pseudo-von Willebrand Disease**, but currently **no clinical trials** and **no published literature** support this specific candidate — the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in regulatory license data (0 licenses on file); literature evidence references use in congenital/acquired hemophilia A |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for emicizumab is not available in this evidence pack. Based on information surfaced through the literature evidence for other candidate indications, emicizumab is a bispecific antibody that bridges activated factor IX and factor X, mimicking the cofactor function of activated factor VIII (FVIIIa) to restore thrombin generation — its established use is bleeding prophylaxis in congenital hemophilia A, and it has also been studied for acquired hemophilia A.

Pseudo-von Willebrand disease, however, is caused by a gain-of-function abnormality in the platelet GPIb receptor rather than a deficiency of von Willebrand factor or a coagulation factor — it is a primary platelet–VWF interaction disorder. Per the model's own rationale, this pathology does not directly overlap with emicizumab's FVIIIa/FIXa/FX pathway, and the mechanistic link is characterized as indirect with no supporting clinical evidence. The high TxGNN score should therefore be interpreted as a network-similarity signal rather than a mechanistically validated hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No marketing authorization is currently on record for this drug in the dataset (0 licenses; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the evidence level is L5 (model prediction only) — there are zero clinical trials and zero publications for pseudo-von Willebrand disease, and the model's own mechanistic rationale states there is no direct pathway overlap and no clinical evidence. This does not meet the bar to advance to safety screening.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (currently blocking — flagged as Blocking data gap DG001)
- Confirmed mechanism of action data (flagged as High-severity data gap DG002)
- Preclinical or case-level evidence directly linking emicizumab to pseudo-von Willebrand disease
- Confirmed original approved indication(s), since no license records exist in this dataset

**Note:** Among the ten candidates evaluated for this drug, rank 5 ("acquired coagulation factor deficiency") is backed by substantially stronger evidence — 20 publications including a completed phase 2/3 RCT on emicizumab in acquired hemophilia A — despite a lower raw TxGNN score. That candidate may warrant separate, higher-priority evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


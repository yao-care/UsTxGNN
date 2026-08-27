---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 635
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: From No Taiwan/US-Approved Indication to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Durvalumab (DrugBank DB11714) is not currently on the US/Taiwan regulatory market in this dataset (0 licenses recorded), so no original approved indication is documented here. The TxGNN model's top-ranked prediction is **Prostatic Urethra Urothelial Carcinoma**, but this specific prediction currently has **0 clinical trials** and **0 publications** directly supporting it — the rationale rests solely on anatomical/histological analogy to durvalumab's known class of use in urothelial carcinoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — 0 licenses on file for durvalumab in this dataset; no approved indication text recorded |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for durvalumab is not available in this evidence pack (data gap, High severity). Based on the mechanistic notes attached to this and related predictions in the pack, durvalumab is consistently described as an **anti-PD-L1 monoclonal antibody** that blocks the PD-1/PD-L1 checkpoint to restore T-cell antitumor activity — this description recurs across multiple predicted indications in the same pack (e.g., the endocervical carcinoma entry explicitly states this MOA), even though the drug-level `original_moa` field itself is marked as a data gap.

Prostatic urethra urothelial carcinoma is an anatomical subtype of urothelial carcinoma — the tissue-of-origin family in which durvalumab already has an established immunotherapy role according to the evidence pack's own rationale text. The reasoning here is a **category-level extrapolation**: since durvalumab targets PD-L1 signaling broadly across urothelial-derived tumors, a histologically related subtype (prostatic urethra) is mechanistically plausible. However, the pack explicitly flags this as an indirect, drug-class-level inference — there is no anatomic-subtype-specific trial or literature evidence, and no data on whether the prostatic urethra tumor microenvironment behaves immunologically like bladder-primary urothelial carcinoma.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No regulatory licenses are on file for durvalumab in this dataset (0 NDAs recorded; market status: Not Marketed).

---

## Cytotoxicity

Durvalumab is an oncology drug (anti-PD-L1 immune checkpoint inhibitor), based on the mechanistic descriptions attached to its predicted indications in this pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 immune checkpoint inhibitor) — not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (prostatic urethra urothelial carcinoma) has Evidence Level L4 with zero supporting clinical trials or literature — only an indirect, category-level mechanistic argument. Additionally, TFDA/regulatory warning and contraindication data is a **Blocking** data gap, which by itself prevents any progression to the S1 safety-review stage regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA/FDA package insert (warnings, contraindications) — Blocking gap, required before any S1 safety evaluation
- Confirmed mechanism of action documentation from DrugBank
- Direct clinical trial or literature evidence specific to prostatic urethra urothelial carcinoma (currently none)

**Note:** This report covers only the rank-1 prediction as specified. Among the 10 predictions in this evidence pack, **endocervical carcinoma** (rank 6) has materially stronger support — Evidence Level L2, 2 clinical trials (including a completed Phase 1 trial directly in cervical/vaginal/vulvar cancer), and 1 publication — and may warrant a separate, higher-priority evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


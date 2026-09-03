---
layout: default
title: Octreotide
parent: 僅模型預測 (L5)
nav_order: 982
evidence_level: L5
indication_count: 2
---

# Octreotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Octreotide: From Neuroendocrine Indications to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

> Octreotide is a somatostatin analog with established use in acromegaly and carcinoid syndrome/neuroendocrine tumors (not currently licensed in Taiwan).
> The TxGNN model predicts it may be effective for **Vulvar Inverted Follicular Keratosis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, with the model's own rationale flagging a lack of biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acromegaly, carcinoid syndrome (globally recognized use; not TFDA-licensed) |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (structured MOA field) is not available for this evidence pack. Based on known pharmacology, octreotide is a somatostatin analog acting on SSTR1-5 receptors to suppress growth hormone, IGF-1, insulin, glucagon, and various gastro-entero-pancreatic hormones. It is established clinically for acromegaly and carcinoid syndrome / neuroendocrine tumors.

The top-ranked prediction, vulvar inverted follicular keratosis, is a benign keratinocyte proliferative lesion of the hair follicle infundibulum. According to the model's own repurposing rationale, there is **no known literature support** linking somatostatin receptor signaling to keratinocyte differentiation or proliferation in this condition. The rationale text explicitly notes the high TxGNN score likely reflects an indirect statistical association in the knowledge graph (e.g., shared skin-tumor comorbidity genes or drug-protein interaction nodes) rather than direct biological plausibility.

The second-ranked prediction, seborrheic keratosis, is similarly a keratinocyte proliferative disorder typically driven by FGFR3/PIK3CA somatic mutations and keratinocyte aging pathways — again with no established connection to somatostatin receptor signaling. Existing octreotide dermatology literature is limited to skin manifestations of Cushing's syndrome or rare adverse-event case reports, not therapeutic use in keratinocyte hyperplasia. Both predictions should be treated as computational hypotheses requiring independent mechanistic investigation, not as evidence-supported repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Octreotide currently holds **0 NDAs / drug licenses** in Taiwan (market status: 未上市, Not Marketed). No TFDA-approved indication text is available for reference.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug interaction data are marked as data gaps (DG001, Blocking) in this evidence pack and must be sourced from TFDA labeling before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are supported only by TxGNN model scoring (Evidence Level L5) with zero clinical trials, zero literature, and no established mechanistic plausibility per the model's own rationale — and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (DG001, blocking)
- Structured mechanism of action data from DrugBank (DG002)
- Preclinical or mechanistic studies linking somatostatin receptor signaling to keratinocyte proliferative disorders
- Any case reports or observational data on octreotide use in dermatologic keratinocyte lesions
- Taiwan regulatory pathway assessment, given the drug currently has no TFDA license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


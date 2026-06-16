---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 513
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

使用 `txgnn-pipeline` 確認作業脈絡完成，現在依據系統提示的藥師報告格式，基於 Evidence Pack JSON 輸出以下報告：

---

# Ceritinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Ceritinib is a second-generation anaplastic lymphoma kinase (ALK) inhibitor, globally approved for the treatment of ALK-rearranged non-small cell lung cancer (NSCLC), and is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**, however this prediction is backed by **0 clinical trials** and **0 publications** — it rests entirely on knowledge graph topology with no direct biological rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive non-small cell lung cancer (global approval; no Taiwan license on record) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from the data source. Based on published literature, ceritinib is a potent, orally bioavailable inhibitor of anaplastic lymphoma kinase (ALK). It was the first drug to overcome crizotinib resistance in ALK-positive NSCLC, demonstrating robust efficacy in the landmark ASCEND-4 Phase 3 trial, which established its superiority over platinum-based chemotherapy in untreated patients. Beyond ALK, ceritinib also inhibits IGF-1R (insulin-like growth factor 1 receptor) and FAK (focal adhesion kinase), pathways relevant to cell survival and invasion in solid tumours.

Gingival fibromatosis is a benign, non-malignant overgrowth of fibrous gingival tissue. Its primary molecular drivers are mutations in **SOS1** and **FGFR** (fibroblast growth factor receptor), and it is fundamentally a structural, connective tissue disorder — not a malignancy driven by oncogenic kinase fusion. There is currently no known role for ALK, ROS1, IGF-1R, or FAK signalling in the pathogenesis of this condition. The mechanistic bridge between ceritinib's pharmacology and gingival fibromatosis biology does not exist in current evidence.

The high TxGNN prediction score (99.86%) most likely reflects **graph-level proximity** in the underlying knowledge graph, where "fibrous tissue proliferation" disease nodes are statistically close to nodes associated with ceritinib. This is a known artefact of graph-based models: hub nodes with high connectivity generate confident predictions that do not always reflect biological plausibility. This prediction should be treated as a computational signal only, requiring experimental validation before any further investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ceritinib in Fibromatosis, Gingival.

---

## Literature Evidence

Currently no related literature available for Ceritinib in Fibromatosis, Gingival.

---

## Taiwan Market Authorization

No regulatory licenses for Ceritinib have been identified in the Taiwan TFDA database. Ceritinib is not approved or marketed in Taiwan.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| — | — | — | No licenses on record |

> **Note:** Ceritinib (Zykadia®) holds FDA approval (US, 2014) and EMA approval (EU, 2015) for ALK-positive NSCLC, but these authorizations fall outside the scope of this Taiwan regulatory dataset.

---

## Cytotoxicity

Ceritinib is an antineoplastic agent — a targeted therapy for ALK-driven malignancy. It meets the antineoplastic criteria: its known global indication is a malignant condition (NSCLC), and it belongs to the tyrosine kinase inhibitor class used in oncology.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — 2nd-generation ALK tyrosine kinase inhibitor |
| Myelosuppression Risk | Low (myelosuppression is not a primary toxicity of ALK-TKIs; neutropenia reported infrequently) |
| Emetogenicity Classification | Moderate (nausea, vomiting, and diarrhoea are the most common dose-limiting GI effects; substantially reduced when taken at 450 mg with food per ASCEND-8 data) |
| Monitoring Items | Liver function (ALT/AST/bilirubin), QTc interval (ECG), fasting blood glucose, lipase/amylase, CBC |
| Handling Protection | Handle as oral antineoplastic agent; follow institutional cytotoxic drug handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. (No Taiwan-specific warnings, contraindications, or drug interaction data are available in the current dataset.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ceritinib's mechanism of action — centred on ALK/IGF-1R/FAK inhibition — has no established connection to gingival fibromatosis, a benign connective tissue disorder driven by SOS1/FGFR pathways. With zero supporting clinical trials or relevant literature and a purely graph-derived prediction signal, this indication does not meet the threshold for further repurposing investigation.

**To proceed, the following is needed:**
- Evidence of ALK pathway activation in gingival fibromatosis tissue (e.g., immunohistochemistry or targeted sequencing data)
- Complete MOA data from DrugBank to check whether ceritinib's off-target kinase profile overlaps with FGFR or SOS1 signalling
- Assessment of whether ceritinib's IGF-1R inhibition has any theoretical relevance to mesenchymal fibrous proliferation
- Taiwan TFDA package insert retrieval for complete local safety, contraindication, and drug interaction data (currently blocking initial safety assessment — Data Gap DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


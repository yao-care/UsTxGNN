---
layout: default
title: Actaea Cimicifuga Whole Calcium Hexafluorosilicate
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 0
---

# Actaea Cimicifuga Whole Calcium Hexafluorosilicate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# ACTAEA CIMICIFUGA / DROSERA / INULA 複方: 資料不足，無法完成老藥新用評估

## One-Sentence Summary

本品為含 8 種成分的複方製劑（包含 Actaea cimicifuga、Drosera rotundifolia、Inula helenium 等草本與礦物成分），目前在台灣及美國均未上市。由於 DrugBank 無法識別完整複方、亦無原始適應症記錄，TxGNN 模型**未能產生任何新適應症預測**，本次評估資料不足，無法進行完整分析。

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | 無登錄資料 |
| Predicted New Indication | 無預測結果 |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5（模型未產生預測，無任何實證） |
| US Market Status | 未上市 |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## 為何無法完成預測？

本複方含 8 種異質性成分（草本全株、礦物鹽、昆蟲萃取物、真菌），性質上接近**順勢療法（homeopathic）或人智學（anthroposophic）製劑**：

- **Actaea cimicifuga**（升麻）、**Drosera rotundifolia**（毛氈苔）、**Inula helenium**（土木香）為草本植物全株
- **Formica rufa**（紅蟻）、**Fuligo septica**（黃色黏菌）為非典型生物來源
- **Calcium hexafluorosilicate**、**Potassium chloride**、**Silica** 為礦物或無機成分

TxGNN 知識圖譜以 DrugBank 收錄的單一化學實體為核心節點，**無法處理複方整體或順勢療法製劑**。因此本複方無 DrugBank ID，亦無法被映射至疾病節點，導致預測流程中斷。

---

## US Market Information

目前無任何美國 NDA 或上市記錄。

---

## Safety Considerations

請參閱各成分原廠仿單或藥典（如 Homeopathic Pharmacopoeia of the United States, HPUS）中的安全性資訊。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本複方在現行 TxGNN 架構下無法生成預測，且在台灣與美國均無上市記錄，缺乏可供評估的監管與臨床基礎。

**若需繼續推進，需補充以下資料：**

- **釐清製劑屬性**：確認是否為順勢療法/人智學製劑，或具有明確藥理機轉的草本複方
- **單成分拆分分析**：若目標為特定成分（如 Actaea cimicifuga 用於更年期症狀、Drosera rotundifolia 用於咳嗽），應將各成分獨立送入 TxGNN 流程
- **文獻基礎確認**：搜尋 PubMed 是否有此特定複方配方的臨床研究
- **監管策略評估**：確認目標市場（台灣/美國）對此類製劑的分類標準（藥品 vs. 健康食品 vs. 順勢療法）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


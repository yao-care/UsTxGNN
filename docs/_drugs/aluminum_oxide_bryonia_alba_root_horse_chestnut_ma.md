---
layout: default
title: Aluminum Oxide Bryonia Alba Root Horse Chestnut Ma
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 0
---

# Aluminum Oxide Bryonia Alba Root Horse Chestnut Ma
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

# 複方草本礦物製劑：資料不足，無法生成老藥新用預測

## One-Sentence Summary

本候選藥品為含八種成分的複方製劑，包含植物提取物（白薊、馬栗、馬錢子）及多種礦物化合物，在台灣目前無任何藥品許可登記。
TxGNN 模型因無法對應 DrugBank ID 且原始適應症缺失，**未能生成任何老藥新用預測結果**。
在取得完整成分資料並建立明確藥理分類前，本候選案無法進入標準評估流程。

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | 無紀錄 |
| Predicted New Indication | 無（TxGNN 無法生成預測） |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5（模型預測不可用） |
| Taiwan Market Status | ✗ 未上市（無任一許可證） |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Possible

本複方由八種成分組成，涵蓋植物藥（Bryonia alba 白薊根、Horse Chestnut 馬栗、Strychnos nux-vomica 馬錢子種子）及礦物輔料（Aluminum Oxide 氧化鋁、Magnesium Carbonate 碳酸鎂、Magnesium Chloride 氯化鎂、Potassium Alum 明礬、Silicon Dioxide 二氧化矽）。此類配方常見於順勢療法（homeopathic）產品，各成分濃度及活性通常遠低於一般藥理學劑量。

TxGNN 模型的預測依賴單一 DrugBank ID 作為圖譜節點，複方製劑在知識圖譜中無法以單一節點表示，導致模型無法執行圖神經網路推理。此外，台灣 TFDA 資料庫查詢結果為零筆許可紀錄，亦無原始適應症可供比對，兩項關鍵輸入皆缺失。

若需繼續推進評估，建議優先對 Horse Chestnut（Aesculus hippocastanum，活性成分 Aescin，DrugBank DB01122）及 Strychnos nux-vomica（Nux vomica）等具已知藥理機轉的主要成分，拆解為個別單成分評估，再彙整複方協同效應分析。

---

## Clinical Trial Evidence

目前無相關臨床試驗資料可供呈現。

> 本複方組合在 ClinicalTrials.gov 中未查得對應登記試驗，個別成分（如 Horse Chestnut Seed Extract 用於慢性靜脈功能不全）另有試驗資料，但不適用於本複方整體評估。

---

## Literature Evidence

目前無可直接引用的複方文獻資料。

> 個別成分文獻（如 Aescin 靜脈水腫、Magnesium 補充療法）不代表本複方整體藥效，不列入本表。

---

## Taiwan Market Information

本複方製劑在台灣 TFDA 資料庫中查無任何藥品許可登記。

| 查詢來源 | 查詢狀態 | 許可數量 | 備註 |
|---------|---------|---------|------|
| TFDA | 已查詢（2026-03-24） | 0 | 無符合紀錄 |

---

## Safety Considerations

請參閱各成分個別仿單及順勢療法產品說明書，以取得安全性資訊。

> **特別提醒**：Strychnos nux-vomica（馬錢子）含生物鹼 Strychnine，高劑量具神經毒性，需確認本品劑量符合順勢療法極度稀釋規範，不適用常規藥理毒性評估。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本複方製劑缺乏 DrugBank ID 對應、無原始適應症紀錄、台灣無許可登記，且 TxGNN 模型未能產出任何預測結果，現有資料不足以支持任何老藥新用評估。

**To proceed, the following is needed:**

- **成分拆解**：確認各成分在本製劑中的劑量與稀釋倍數，判斷是否適用常規藥理學評估或順勢療法框架
- **主成分選定**：挑選 1-2 個具已知藥理機轉的成分（建議 Horse Chestnut / Aescin），以單成分重新提交 TxGNN 預測
- **DrugBank 對應**：為各植物成分查詢對應 DrugBank ID（Horse Chestnut → DB01122 Aescin，Nux vomica → DB01392 Brucine/Strychnine）
- **毒性確認**：釐清 Strychnos nux-vomica 在本品中的稀釋程度，排除 Strychnine 毒性疑慮後才可進行後續安全性評估
- **原廠資料取得**：如本品為已知市售順勢療法產品，取得原廠仿單以確認原始適應症
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


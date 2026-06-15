---
layout: default
title: Arnica Montana Root Artemisia Cina Flower Atropa B
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 0
---

# Arnica Montana Root Artemisia Cina Flower Atropa B
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

# ARNICA MONTANA ROOT 等複方: 無法進行老藥新用評估

## 摘要

本候選品項為包含 10 種成分的複方製劑（包含 Arnica montana、Atropa belladonna、Ipecac 等植物性與礦物性成分），屬同類療法（Homeopathic）配方類型。TxGNN 模型對此複方**未產生任何預測適應症**，且在台灣無任何藥品許可證記錄。由於關鍵資料（MOA、安全警語、適應症）均付之闕如，目前**無法執行老藥新用評估**。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無資料 |
| 預測新適應症 | 無（TxGNN 未輸出預測結果） |
| TxGNN 預測分數 | 無 |
| 證據等級 | L5（模型無預測，完全無實證支持） |
| 台灣上市狀態 | ✗ 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

---

## 為何無法進行預測分析？

此複方由以下 10 種成分組成，性質特殊：

| 成分 | 類型 |
|------|------|
| Arnica montana root | 植物性（菊科） |
| Artemisia cina flower | 植物性（菊科，傳統驅蟲藥） |
| Atropa belladonna whole | 植物性（茄科，含阿托品） |
| Copper | 礦物性 |
| Corallium rubrum exoskeleton | 動物性（紅珊瑚） |
| Drosera rotundifolia flowering top | 植物性（茅膏菜，傳統止咳） |
| Ferrum phosphoricum | 礦物性（磷酸鐵） |
| Ipecac | 植物性（吐根，傳統催吐） |
| Protortonia cacti | 昆蟲性（介殼蟲） |
| Solidago virgaurea flowering top | 植物性（一枝黃花，傳統利尿） |

此類成分組合為**同類療法（Homeopathic medicine）**的典型配方。TxGNN 模型的知識圖譜以 DrugBank 為核心，同類療法複方通常無法獲得 DrugBank ID，導致模型無法建立節點關聯，因此**未能輸出任何預測適應症**。

---

## 臨床試驗證據

目前無相關臨床試驗登錄紀錄。

---

## 文獻證據

目前無相關文獻資料。

---

## 台灣市場資訊

此複方在台灣藥品許可資料庫中查無任何紀錄（許可證數量：0），目前為**未上市**狀態。

---

## 安全性注意事項

請參閱各成分仿單之警語與禁忌事項。

> **特別注意**：Atropa belladonna（顛茄）含阿托品類生物鹼，具有潛在毒性；Ipecac（吐根）含吐根鹼，過量有心臟毒性風險。即使以同類療法稀釋劑型使用，處方前仍應查閱完整安全資料。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
TxGNN 模型對此同類療法複方未輸出任何預測結果，缺乏 DrugBank ID、作用機轉、原始適應症及安全資料，目前無任何基礎可進行老藥新用評估。

**若要推進，需補充以下資料：**

- 確認此複方是否有對應的 DrugBank 或其他標準藥物資料庫 ID
- 釐清各成分的有效劑量與稀釋比例（同類療法效力標記）
- 取得台灣或其他主要市場的仿單，以補充安全警語與禁忌
- 評估是否應改為針對**單一有效成分**（如 Atropa belladonna 中的阿托品）進行個別老藥新用分析，而非以複方整體查詢
- 若堅持以複方查詢，需建立自訂的知識圖譜節點，才能使 TxGNN 模型產生有意義的預測
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


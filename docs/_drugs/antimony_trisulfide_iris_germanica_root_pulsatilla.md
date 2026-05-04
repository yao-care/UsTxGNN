---
layout: default
title: Antimony Trisulfide Iris Germanica Root Pulsatilla
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 0
---

# Antimony Trisulfide Iris Germanica Root Pulsatilla
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

# 多成分順勢療法混合物：無法產生老藥新用預測報告

## One-Sentence Summary

本藥品為多成分順勢療法/草本混合物（含 Antimony Trisulfide、Iris Germanica Root、Pulsatilla Vulgaris、Silver Nitrate、Sulfur、Thuja Occidentalis Leafy Twig、Tribasic Calcium），目前在美國無核准記錄、無 DrugBank 對應 ID。TxGNN 模型**未產生任何老藥新用預測**，原因可能是此多成分混合物無法在知識圖譜中找到對應節點。因此，本報告為**資料不足通知書**，而非完整的老藥新用評估報告。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無資料 |
| 預測新適應症 | 無（TxGNN 未產生預測） |
| TxGNN 預測分數 | 無 |
| 證據等級 | L5（模型無法評估） |
| 美國上市狀態 | 未上市 |
| NDA 數量 | 0 |
| 建議決策 | **Hold** |

---

## 為何無法產生預測？

本藥品為含七種成分的順勢療法複方，具有以下特性，導致 TxGNN 流程無法正常運作：

**1. 無 DrugBank ID**
TxGNN 知識圖譜（Knowledge Graph）以 DrugBank ID 為節點識別碼。本藥品查詢 DrugBank 雖回傳 1 筆結果，但未能取得有效的 DrugBank ID，表示對應關係不明確，知識圖譜中無法建立藥物節點。

**2. 多成分混合物的映射困難**
順勢療法複方（如本品）通常以混合成分整體登記，而非以單一活性成分登記。TxGNN 設計針對單一化學實體（single chemical entity）進行預測，複方混合物在 KG 中缺乏統一節點，導致預測流程無法啟動。

**3. 美國無核准記錄**
FDA 查詢結果為零，表示此複方可能以 OTC 順勢療法產品登記（不需 NDA），或完全未在美國上市。順勢療法產品的監管路徑與傳統藥品不同，導致相關適應症資料缺失。

---

## 美國市場資訊

目前無任何 NDA 或上市記錄。

> 此藥品在美國無核准上市記錄（total_licenses = 0）。順勢療法產品在美國通常以不同監管途徑申報，建議查詢 FDA 順勢療法產品資料庫或 OTC 專論系統（OTC Monograph）以確認市場狀態。

---

## 安全性資訊

目前無可用的安全性資料，請參考各成分的個別產品仿單及相關文獻。

> **注意**：本複方含 **Silver Nitrate（硝酸銀）** 及 **Antimony Trisulfide（三硫化銻）**，均為具有潛在毒性的無機化合物。在缺乏完整安全性資料的情況下，應謹慎評估其使用風險。

---

## 結論與後續步驟

**決策：Hold（暫停評估）**

**原因：**
本藥品為多成分順勢療法複方，TxGNN 模型未能在知識圖譜中識別對應藥物節點，因此無法產生老藥新用預測。在缺乏基礎資料的情況下，無法進行有意義的老藥新用評估。

**若需繼續評估，需補充以下資料：**

1. **釐清活性成分**：確認複方中每個成分的 DrugBank ID，考慮對各成分分別執行 TxGNN 預測，再彙整結果。
2. **確認監管路徑**：查詢 FDA 順勢療法 OTC 資料庫，釐清是否以 OTC 產品登記，並取得核准適應症資料。
3. **取得安全性資料**：下載並解析 FDA 或 EMA 相關個別成分的 Monograph，補充警語與禁忌資訊。
4. **重新執行映射流程**：以個別成分（如 Sulfur、Silver Nitrate 等）為單位，重新進行 DrugBank 映射與 TxGNN 預測。
5. **評估拆分報告的可行性**：若個別成分有足夠的 KG 覆蓋率，可考慮為每個主要成分分別產生老藥新用評估報告。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


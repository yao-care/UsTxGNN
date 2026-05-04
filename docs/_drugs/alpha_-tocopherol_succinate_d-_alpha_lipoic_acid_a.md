---
layout: default
title: Alpha -Tocopherol Succinate D- Alpha Lipoic Acid A
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 0
---

# Alpha -Tocopherol Succinate D- Alpha Lipoic Acid A
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

# 複合維生素礦物質配方: 評估報告無法完成（缺乏 TxGNN 預測結果）

## One-Sentence Summary

本品為含有 20 種活性成分的複合維生素與礦物質補充劑（包含脂溶性維生素 A、D、E，水溶性 B 群全系列、維生素 C，及硒、鋅、鎂、錳、鉻、銅等微量元素與抗氧化劑 Lutein、Alpha Lipoic Acid）。
TxGNN 模型未能對此複合配方產生任何預測適應症，原因為此配方係多成分混合物，DrugBank ID 無法匹配，**目前無法進行標準老藥新用分析流程**。
由於預測結果缺失、台灣無核准上市紀錄、安全資料亦全部缺漏，本次評估屬於 **資料不足、無法結論** 的案例。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無紀錄（台灣未核准上市） |
| 預測新適應症 | **無**（TxGNN 未產生預測） |
| TxGNN 預測分數 | N/A |
| 證據等級 | **無法評級**（無預測、無試驗、無文獻） |
| 台灣市場狀態 | ✗ 未上市 |
| 許可證總數 | 0 |
| 建議決策 | **Hold** |

---

## 為何無法進行預測分析？

此候選物並非單一分子藥物，而是由 20 種成分組成的複合配方：

> **脂溶性維生素**：Vitamin A、Cholecalciferol（D3）、D-α-Tocopherol Succinate（E）
>
> **水溶性維生素（B 群全系列 + C）**：Thiamine（B1）、Riboflavin（B2）、Niacinamide（B3）、Calcium Pantothenate（B5）、Pyridoxine HCl（B6）、Cyanocobalamin（B12）、Folic Acid、Biotin、Ascorbic Acid（C）
>
> **礦物質與微量元素**：Magnesium Oxide、Zinc Oxide、Cupric Sulfate（銅）、Selenium、Manganese、Chromium
>
> **抗氧化劑**：Lutein、Alpha Lipoic Acid

TxGNN 模型以單一 DrugBank ID 作為節點進行知識圖譜推論。複合配方無對應的 DrugBank ID，導致模型無法輸入節點表示向量，**預測結果為空**。

此類配方通常以「保健食品」或「醫療用特殊營養品」（Medical Food）定位，其適應症評估框架與單一化學藥品不同，TxGNN 架構並非為此類複方設計，本次評估結果屬預期內的系統限制，而非資料錯誤。

---

## 臨床試驗證據

目前無相關臨床試驗紀錄（評估對象為複合配方整體；各成分個別文獻不在本報告範圍內）。

---

## 文獻證據

目前無相關文獻可供評估（原因同上）。

---

## 台灣市場資訊

本品於台灣查無核准上市紀錄（`market_status: 未上市`，`total_licenses: 0`）。可能情境如下：

1. 以食品或保健食品申請，未經藥品途徑核准
2. 尚未申請台灣藥品許可證
3. 成分資料串接異常，導致查詢結果為零

建議直接至[食品藥物管理署藥品查詢系統](https://www.fda.gov.tw/)逐一確認各成分的原料藥或製劑狀態。

---

## 安全性考量

本品所有安全資料（警語、禁忌、藥物交互作用）均顯示為資料缺漏，DDI 查詢亦未找到對應結果。

> 請參閱各成分之原廠仿單或參考 DrugBank 個別成分頁面以取得安全資訊。
>
> 特別注意：脂溶性維生素（A、D、E）具有蓄積毒性風險，高劑量使用時需監測血中濃度。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
本品為多成分複合配方，TxGNN 預測引擎無法處理此類輸入，台灣亦無核准上市紀錄，安全資料全部缺漏，目前不具備進行老藥新用評估的基本條件。

**若需繼續推進，需要補充以下資料：**

- **釐清評估範疇**：確認是否需針對複合配方整體，或拆解為個別成分分別進行 TxGNN 評估（建議後者）
- **取得 DrugBank ID**：針對各成分（如 Alpha Lipoic Acid、Lutein、Cholecalciferol 等）分別對應 DrugBank 節點，再逐一執行預測
- **確認法規定位**：釐清此配方在台灣應走藥品（衛福部食藥署）或特殊營養食品（衛福部國健署）途徑
- **MOA 資料補充**：若目標為特定成分（如 Alpha Lipoic Acid 用於糖尿病神經病變），需個別查詢 DrugBank API 取得 MOA
- **安全資料補全**：下載各主要成分之仿單 PDF 並解析警語與禁忌（優先：Vitamin A、Cholecalciferol、Selenium）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


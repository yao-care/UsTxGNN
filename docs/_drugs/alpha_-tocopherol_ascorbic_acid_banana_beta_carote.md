---
layout: default
title: Alpha -Tocopherol Ascorbic Acid Banana Beta Carote
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 0
---

# Alpha -Tocopherol Ascorbic Acid Banana Beta Carote
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

# 多成分天然補充品複方：評估資料不足，無法進行老藥新用分析

---

## One-Sentence Summary

本候選品項為八種天然成分組成的複方補充品（α-生育醇、抗壞血酸、香蕉、β-胡蘿蔔素、魚腥草、菊糖、納豆激酶、芸香苷），**並非單一化學藥品**，在台灣目前尚未取得任何藥品許可。TxGNN 模型**未能產生任何預測適應症**，主要原因為多成分複方無法對應至 DrugBank 知識圖譜節點，加上缺乏 DrugBank ID 及原始適應症資料，本次評估**無法進入實質分析階段**。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 成分組成 | α-生育醇 / 抗壞血酸 / 香蕉 / β-胡蘿蔔素 / 魚腥草 / 菊糖 / 納豆激酶 / 芸香苷 |
| 原始適應症 | 無資料 |
| 預測新適應症 | **無**（TxGNN 無法映射，未產生預測） |
| TxGNN 預測分數 | 不適用 |
| 證據等級 | **L5**（模型預測失敗，無任何實際研究支持） |
| 台灣上市狀態 | ✗ 未上市（0 筆藥品許可） |
| 許可證數量 | 0 |
| 建議決策 | **Hold** |

---

## Why is This Prediction Reasonable?

本品項並非傳統意義上的單一藥物，而是由八種來源各異的天然活性物質組成的複方：

- **抗氧化維生素類**：α-生育醇（維生素 E）、抗壞血酸（維生素 C）、β-胡蘿蔔素（維生素 A 前驅物），具有清除自由基、抑制氧化壓力的作用。
- **植物化學物質**：芸香苷（黃酮類，具抗炎及血管保護作用）、魚腥草（傳統草藥，具抗菌及免疫調節潛力）。
- **功能性食品成分**：菊糖（益生元纖維，調節腸道菌相）、香蕉（鉀源及碳水化合物）、納豆激酶（絲胺酸蛋白酶，具溶栓活性）。

由於本品為多成分複方，且各成分中多數為**食品或健康食品原料**（非藥品），TxGNN 知識圖譜以 DrugBank 藥品節點為基礎進行圖網路推論，無法對此類複合配方進行系統性映射與預測。

目前 **`original_moa` 欄位為空**，無法提供機轉關聯性分析。若需進行老藥新用評估，建議**將各單一成分分拆為獨立候選品項**分別評估（例如：單獨評估 Nattokinase 或 Rutin 的重定位潛力）。

---

## Clinical Trial Evidence

目前無相關臨床試驗登錄（TxGNN 未產生預測適應症，無法進行針對性查詢）。

---

## Literature Evidence

目前無相關文獻（TxGNN 未產生預測適應症，無法進行針對性查詢）。

---

## US Market Information

本品在台灣無任何藥品許可，亦無美國 FDA 藥品許可資料可供列示。

---

## Safety Considerations

請參閱各成分個別的產品說明書或安全資料表取得安全性資訊。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本品為多成分天然複方，且台灣無藥品許可、TxGNN 映射失敗、無任何預測適應症，目前技術條件下**無法執行有效的老藥新用評估**；在獲得明確的單一活性成分指定及藥品級資料之前，不建議推進。

**To proceed, the following is needed:**

- **拆分候選品項**：將八種成分分別建立獨立的 Evidence Pack，以單一 INN 進入 TxGNN 映射流程（優先建議：Nattokinase、Rutin、Houttuynia Cordata）
- **確立藥品身份**：確認各成分是否有對應的 DrugBank ID（目前整體複方查無 DrugBank ID）
- **補充作用機轉（MOA）**：透過 DrugBank API 查詢各單一成分的 MOA 資料，解除 DG002 資料缺口
- **確認法規定位**：釐清本品在台灣的定位（藥品 vs. 健康食品 vs. 食品），方可決定適用的審查路徑
- **補充 TFDA 仿單警語**：若存在相關產品，透過 TFDA 官網下載仿單 PDF 解析安全資訊，解除 DG001 阻斷性缺口
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


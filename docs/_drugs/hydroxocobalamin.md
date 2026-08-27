---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 779
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
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

# Hydroxocobalamin：從氰化物中毒解毒劑／維生素B12缺乏症 到 Esophageal Varices with Bleeding

## One-Sentence Summary

Hydroxocobalamin（維生素B12a，DrugBank ID: DB00200）核准用途為氰化物中毒解毒劑與維生素B12缺乏症治療。
TxGNN 模型預測其可能對 **Esophageal Varices with Bleeding（食道靜脈曲張出血）** 有效，
但目前**沒有任何臨床試驗**、**沒有任何文獻佐證**，僅為模型演算法預測。

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 台灣未上市，無核准適應症資料（機轉分析引用之已知用途為氰化物中毒解毒劑、維生素B12缺乏症） |
| Predicted New Indication | Esophageal Varices with Bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5（僅模型預測，無臨床試驗或文獻） |
| Market Status | 未上市 |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

目前作用機轉（MOA）資料缺失（[Data Gap]，DG002），無法直接說明藥理關聯。Hydroxocobalamin 已知核准用途為氰化物中毒之解毒劑，以及維生素B12缺乏症治療，兩者與食道靜脈曲張出血在病理生理上並無直接重疊。

唯一可想像的間接假說是：hydroxocobalamin 具有一氧化氮（NO）與硫化氫清除能力，臨床上已用於血管麻痺性休克（vasoplegic shock）以誘發血管收縮。食道靜脈曲張出血的病理機轉涉及 NO 介導之內臟血管擴張，進而導致門脈高壓；理論上 NO 清除劑可能降低內臟血流，作用路徑類似 vasopressin、terlipressin 或 octreotide 等已核准之止血用藥。然而，此僅為機轉層面的推論，**未見任何直接研究**將 hydroxocobalamin 用於靜脈曲張出血。

TxGNN 對第二個預測適應症「Esophageal Varices without Bleeding（未出血之食道靜脈曲張）」給出相同分數（99.23%），機轉假說相同，但證據強度更弱——未出血狀態下缺乏急性血管收縮劑使用的臨床類比基礎。兩者皆屬純演算法預測，且藥物於台灣未上市，尚無法進行安全性初評（S1）。

## Clinical Trial Evidence

目前無相關已註冊臨床試驗（Currently no related clinical trials registered）。

## Literature Evidence

目前無相關文獻資料（Currently no related literature available）。

## Market Information

本藥於台灣未上市（許可證數：0），無市售產品資訊可列。

## Safety Considerations

請參考仿單安全性資訊（Please refer to the package insert for safety information）。目前仿單警語與禁忌資料缺失（DG001，Blocking），列為進入安全性初評（S1）前的關鍵缺口。

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
證據等級為 L5，無任何臨床試驗或文獻支持此適應症，且藥物於台灣未上市，MOA 與仿單安全性資料均缺失，尚不具備進入下一階段評估的基礎。

**To proceed, the following is needed:**
- TFDA 仿單警語／禁忌資料（DG001，Blocking，需下載仿單 PDF 解析後才能進入 S1 安全性初評）
- 作用機轉（MOA）詳細資料（DG002，需查詢 DrugBank API）
- 針對食道靜脈曲張出血／未出血之直接臨床試驗或文獻證據
- 若評估跨國引進，需補充台灣（或目標市場）上市許可與適應症核准資訊
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


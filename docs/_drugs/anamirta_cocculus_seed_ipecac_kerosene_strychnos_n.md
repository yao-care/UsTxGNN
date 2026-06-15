---
layout: default
title: Anamirta Cocculus Seed Ipecac Kerosene Strychnos N
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 0
---

# Anamirta Cocculus Seed Ipecac Kerosene Strychnos N
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

# ANAMIRTA COCCULUS SEED 等複方：評估資料不足，無法產生預測報告

## One-Sentence Summary

本品為含有 Anamirta Cocculus Seed、Ipecac、Kerosene、Strychnos Nux-Vomica Seed 及 Tobacco Leaf 之五成分複方，原適應症資料不明。TxGNN 模型**未能產生任何老藥新用預測**，且該複方在美國亦無上市紀錄，目前缺乏支持評估的基礎資料。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 無資料 |
| Predicted New Indication | 無預測結果 |
| TxGNN Prediction Score | 無 |
| Evidence Level | L5（模型未產生預測，無任何實際研究支持） |
| US Market Status | 未上市 |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

目前 TxGNN 模型對本複方**未產生任何老藥新用預測候選**，因此無法進行預測合理性分析。

本品由五種成分組成，成分特性如下：

- **Anamirta Cocculus Seed**：含苦毒素（picrotoxin），為 GABA 受體拮抗劑，歷史上曾用作魚毒及殺蟲劑。
- **Ipecac（吐根）**：含吐根鹼（emetine），傳統用途為催吐劑，具心臟毒性。
- **Kerosene（煤油）**：石油衍生品，為有機溶劑，無已知治療用途。
- **Strychnos Nux-Vomica Seed（馬錢子）**：含士的寧（strychnine）及布魯辛（brucine），屬劇毒生物鹼，小量曾見於傳統醫藥，現代不建議使用。
- **Tobacco Leaf（菸草葉）**：含尼古丁（nicotine），已知具多種毒理作用。

本複方成分均具有顯著毒性，且多數屬農業/傳統用途，而非現代藥物開發對象。DrugBank 無對應 ID，亦無 MOA 資料，這是模型無法預測的根本原因。

---

## Clinical Trial Evidence

目前無相關臨床試驗登記。

---

## Literature Evidence

目前無相關文獻資料。

---

## US Market Information

本複方在美國無任何 NDA 或市場授權紀錄，無法提供授權資訊表格。

---

## Safety Considerations

> 本品所有安全性資料均缺失，且成分本身具有已知的急性與慢性毒性風險，強烈建議：
>
> - **不得**在未取得完整毒理學評估前進行任何人體使用評估
> - Kerosene 為有機溶劑，口服毒性明確，**本身即為非藥用成分**
> - Strychnos Nux-Vomica 含士的寧，治療指數極窄，誤用可致死
> - Anamirta Cocculus 含苦毒素，具中樞神經毒性
> - Ipecac 長期使用已知可導致心肌病變

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本複方無 TxGNN 預測結果、無上市紀錄、無 DrugBank 登錄、無安全性資料，且成分組成含多種已知有毒物質（煤油、士的寧、苦毒素），不具備進入老藥新用評估流程的基本條件。

**本案不建議繼續推進，如仍需評估，須先完成以下工作：**

- 確認本複方是否確為待評估藥品（成分組合高度疑似農用/傳統用途，非現代人用藥物）
- 若確為藥品，取得各成分之 DrugBank 個別登錄及 MOA 資料
- 對各單一成分分別執行 TxGNN 預測，再評估複方交互作用
- 完整毒理學資料（急毒、慢毒、致癌性）為進入評估的前提條件
- 釐清 Kerosene 是否為輔料或有效成分，若為有效成分，需提供安全性依據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


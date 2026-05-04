---
layout: default
title: Abacavir Sulfate Dolutegravir Sodium Lamivudine
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 0
---

# Abacavir Sulfate Dolutegravir Sodium Lamivudine
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

# ABACAVIR SULFATE / DOLUTEGRAVIR SODIUM / LAMIVUDINE: 尚無預測適應症（資料不足）

## One-Sentence Summary

Abacavir + Dolutegravir + Lamivudine 是三合一抗反轉錄病毒固定劑量組合（商品名 Triumeq），原用於 HIV-1 感染治療。
本次 Evidence Pack 中 **TxGNN 尚未產生任何新適應症預測**，且該組合藥品在台灣目前 **無核准上市紀錄**，導致大部分評估欄位缺乏資料基礎。
在補齊關鍵資料缺口（仿單警語、MOA、預測結果）之前，**建議暫緩（Hold）** 進行後續老藥新用評估。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| Original Indication | HIV-1 感染（根據國際通用知識；本 Pack 未提供台灣仿單資料） |
| Predicted New Indication | 無（TxGNN 本次未輸出預測候選） |
| TxGNN Prediction Score | 不適用 |
| Evidence Level | 無法評定（無預測、無臨床試驗、無文獻）|
| US Market Status | 未上市（台灣藥品資料庫查無核准） |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

目前 Evidence Pack 中 `predicted_indications` 為空，TxGNN 模型未對本藥品組合輸出任何老藥新用候選，因此**無法進行機轉關聯性分析或適應症合理性評估**。

就已知背景資訊而言，此組合為三種成分固定比例複方：

- **Abacavir**（ABC）：核苷酸反轉錄酶抑制劑（NRTI），需代謝活化為 carbovir triphosphate 後競爭性抑制 HIV-1 反轉錄酶
- **Dolutegravir**（DTG）：整合酶鏈轉移抑制劑（INSTI），阻斷 HIV-1 DNA 插入宿主基因組
- **Lamivudine**（3TC）：NRTI，同時具有 HBV 活性，抑制 HBV 及 HIV-1 反轉錄酶

三種成分作用於 HIV-1 複製週期的不同靶點，協同產生抗病毒效果。若未來 TxGNN 針對個別成分（尤其是 Lamivudine 的 HBV 活性）產生預測，值得優先評估 HBV 相關適應症的延伸可能性。

---

## 資料缺口說明

本次 Evidence Pack 存在以下兩項關鍵資料缺口，須補齊後才能繼續評估：

| 缺口編號 | 缺口項目 | 嚴重程度 | 影響 | 補救方式 |
|---------|---------|---------|------|---------|
| DG001 | 台灣仿單警語／禁忌 | Blocking | 無法進入安全性初評 | 至 TFDA 官網下載仿單 PDF 並解析 |
| DG002 | 作用機轉（MOA） | High | 影響機轉關聯性分析 | 查詢 DrugBank API |

---

## US Market Information

本藥品在台灣藥品資料庫中查無任何核准許可證，無法列出授權資訊。

> 備註：此三合一組合（Abacavir + Dolutegravir + Lamivudine）在美國以商品名 **Triumeq**（NDA 206708）核准上市，用於 HIV-1 感染成人及 ≥40 kg 之兒童。台灣若有臨床需求，可參照美國 FDA 核准資訊及原廠仿單。

---

## Safety Considerations

> 本 Evidence Pack 中安全性資料（警語、禁忌、藥物交互作用）均無法取得，請參閱原廠仿單及美國 FDA 核准標示（Triumeq Prescribing Information）以獲取完整安全性資訊。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN 未輸出任何預測候選，加上台灣無核准上市紀錄、安全性資料缺口為 Blocking 等級，目前不具備進行老藥新用評估的基本條件。

**To proceed, the following is needed:**

- [ ] **重新執行 TxGNN 預測**：確認模型是否已對各別成分（Abacavir、Dolutegravir、Lamivudine）建立知識圖譜節點，並分別產出預測候選
- [ ] **補齊 MOA 資料（DG002）**：透過 DrugBank API 取得 DrugBank ID 與完整機轉描述，作為機轉關聯性分析基礎
- [ ] **補齊安全性資料（DG001）**：下載並解析 TFDA 仿單 PDF（如已申請上市）或以美國 FDA 核准標示替代，完成 S1 安全性初評
- [ ] **確認適用評估單元**：評估是以組合藥品整體，或以個別成分（尤其 Lamivudine）作為老藥新用評估對象更為合適
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


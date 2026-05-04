---
layout: default
title: Aconitum Napellus Whole Bryonia Alba Root Ferrosof
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Bryonia Alba Root Ferrosof
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

# 複方順勢療法製劑（9 成分）：無法產生老藥新用預測

## 一句話摘要

本藥品為包含 9 種成分的複方順勢療法製劑（含 Aconitum napellus、Bryonia alba、Pulsatilla vulgaris 等植物性及礦物性成分），在美國市場無核准紀錄，亦未能完成 DrugBank ID 比對。由於 TxGNN 模型無法對此複方進行標準化映射，**目前無任何預測適應症**，相關臨床試驗與文獻證據亦付之闕如。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無紀錄 |
| 預測新適應症 | 無（TxGNN 無法產生預測） |
| TxGNN 預測分數 | 無 |
| 證據等級 | 無法評估 |
| 美國市場狀態 | 未上市 |
| NDA 數量 | 0 |
| 建議決策 | **Hold** |

---

## 為何無法完成預測？

本製劑為多成分複方順勢療法產品，包含以下 9 種成分：

1. Aconitum napellus（全株）
2. Bryonia alba（根部）
3. Ferrosoferric phosphate（磷酸亞鐵鐵）
4. Lycopodium clavatum（孢子）
5. Oyster shell calcium carbonate（牡蠣殼碳酸鈣，粗製）
6. Phosphorus（磷）
7. Pulsatilla vulgaris（全株）
8. Rancid beef（酸敗牛肉）
9. Sulfur（硫磺）

TxGNN 模型以 DrugBank 收錄之單一化學實體為預測基礎。由於此製劑：

- **無 DrugBank ID**：複方順勢療法製劑通常不收錄於 DrugBank
- **成分為極低濃度稀釋物**：順勢療法製劑依其製備原則，活性成分含量遠低於藥理作用閾值
- **無標準化 INN**：9 種成分組合無對應的國際非專利藥名

上述因素導致 TxGNN 無法建立知識圖譜節點映射，因此**未能產生任何老藥新用預測候選**。

---

## 美國市場資訊

本製劑在美國無任何已核准藥品許可證（NDA/ANDA），美國市場狀態為**未上市**。

---

## 安全性注意事項

請參考各成分的個別說明書，注意以下潛在風險：

- **Aconitum napellus**：含烏頭鹼（aconitine），原植物具高度毒性，過量可致心律不整及死亡；順勢療法製劑雖高度稀釋，仍需注意製備品質
- **Phosphorus**：高劑量具肝毒性

由於本製劑無完整仿單警語及禁忌資料，詳細安全性資訊需另行查閱。

---

## 結論與下一步

**決策：Hold**

**理由：**
本製劑為複方順勢療法產品，無 DrugBank 收錄紀錄，TxGNN 模型無法產生預測；加之無美國核准紀錄、無 MOA 資料、無安全性警語資料，目前缺乏進行老藥新用評估的基本資料條件。

**若要繼續評估，需補充以下資訊：**

1. **釐清評估目標**：確認是否針對個別成分（如 Aconitum napellus、Pulsatilla vulgaris）而非整體複方進行老藥新用評估
2. **取得各成分 DrugBank ID**：分別查詢 9 種成分的 DrugBank 收錄狀態
3. **確認製劑稀釋倍數**：順勢療法製劑的稀釋比（如 6X、30C）決定是否有藥理相關性
4. **補充安全性資料**：下載並解析現有仿單（如有），或查閱各成分毒理資料
5. **重新執行 TxGNN**：以個別成分 INN 分別提交，取得各自的老藥新用預測結果

> ⚠️ 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


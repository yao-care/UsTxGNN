---
layout: default
title: Activated Charcoal Araneus Diadematus Artemisia Ci
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Araneus Diadematus Artemisia Ci
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

# 多成分順勢製劑複方：資料不足，無法完成老藥新用評估

## One-Sentence Summary

本品為含 23 種成分的順勢療法複方，成分涵蓋動植物萃取物、微生物 nosode 及代謝物。
由於 TxGNN 系統未能匹配任何 DrugBank 記錄，**目前無法產生新適應症預測**，
亦無相關臨床試驗或文獻支持本複方整體的老藥新用方向。

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | 無記錄（未收載於任何已核准資料庫） |
| Predicted New Indication | 無（TxGNN 未產生預測） |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5（模型無法評估，缺乏任何實際研究） |
| US Market Status | 未上市 |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

本品由以下 23 種成分組成，性質高度異質：

| 類別 | 成分 |
|------|------|
| 順勢炭劑 | Activated Charcoal、Carbo Animalis |
| 植物萃取 | Artemisia Cina、Berberis Vulgaris Root Bark、Frangula Purshiana Bark、Medicago Sativa、Podophyllum、Rheum Palmatum Root、Spigelia Anthelmia、Taraxacum Officinale、Veratrum Album Root |
| 微生物 Nosode | Proteus Mirabilis、Salmonella Enterica Enterica Serovar Enteritidis |
| 動物來源 | Araneus Diadematus（球蛛）、Heparin Bovine、Sus Scrofa Intestinal Mucosa |
| 代謝物 / 元素 | Bilirubin、Creatine、Creatinine、Indole、Selenium、Skatole |
| 礦物順勢劑 | Mercurius Solubilis |

從成分組成判斷，本品屬**腸道 nosode 順勢療法複方（Bowel Nosode Formula）**，傳統用於腸道功能調節。然而：

1. DrugBank 未收載此複方整體，亦未提供 DrugBank ID，導致 TxGNN 知識圖譜無法進行節點比對。
2. 複方中多數成分為順勢療法專用製劑，其有效成分稀釋度極高，超出現代藥理資料庫的收載範圍。
3. 目前作用機轉（MOA）資料完全缺失，無法進行機轉關聯性分析。

**結論**：技術上無法對本複方進行老藥新用預測，需先完成成分標準化與資料補全。

---

## Clinical Trial Evidence

目前無相關臨床試驗記錄。

---

## Literature Evidence

目前無相關文獻可供檢索。

---

## US Market Information

本品在美國未有任何核准上市許可（NDA 數量：0）。

---

## Safety Considerations

請參閱產品仿單中的警語及禁忌事項。

> **注意**：本複方含有以下需特別留意之成分：
> - **Mercurius Solubilis**（汞化合物順勢製劑）：高劑量汞具神經毒性，順勢稀釋後風險程度需個別評估
> - **Heparin, Bovine**（牛源肝素）：理論上具抗凝血作用，與抗凝血藥物併用需謹慎
> - **Veratrum Album**（白藜蘆）：植物鹼含量具潛在毒性
> - **Podophyllum**（鬼臼）：含鬼臼毒素，具細胞毒性潛力

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本複方因成分過於複雜且屬順勢療法特殊類別，TxGNN 模型無法識別其 DrugBank 對應節點，導致完全無法產生預測結果；在缺乏任何預測、臨床試驗及文獻支持的情況下，不建議推進老藥新用評估。

**To proceed, the following is needed:**

- **成分拆解評估**：將 23 種成分逐一查詢 DrugBank，篩選出有藥理記錄的單一成分（例如 Berberine 來自 Berberis Vulgaris、Emodin 來自 Rheum Palmatum），對這些單成分個別執行 TxGNN 預測
- **主成分確認**：釐清本複方的「治療主成分」為何，排除純順勢稀釋成分（如 Mercurius Solubilis、nosode 類），聚焦有實質藥理意義的成分
- **適應症定位**：補充本複方的原始核准適應症或傳統使用紀錄，作為老藥新用的起點
- **MOA 資料補全**：針對各植物成分查詢 DrugBank API 或 PubChem，補充作用機轉資料
- **安全性資料**：下載各成分的仿單或毒理資料，完成 S1 安全性初評所需的警語/禁忌評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


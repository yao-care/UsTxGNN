---
layout: default
title: Apis Mellifera Arctium Lappa Root Arctostaphylos U
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 0
---

# Apis Mellifera Arctium Lappa Root Arctostaphylos U
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

# 多成分植物/順勢療法複方製劑：藥物再利用評估無法執行

## One-Sentence Summary

本候選藥物為一個包含 20 種植物及同類療法成分的複方製劑（含 Apis Mellifera、Uva-Ursi、Saw Palmetto、Cantharis 等），傳統上多用於泌尿道相關適應症。
TxGNN 模型未能產生任何再利用預測，原因在於本製劑無對應 DrugBank ID，無法對應至知識圖譜中的單一分子實體。
目前無任何預測適應症、臨床試驗或文獻可供評估，整體評估工作遭遇根本性資料缺口。

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | 無資料（未取得任何國家藥證） |
| Predicted New Indication | 無預測（TxGNN 無法處理） |
| TxGNN Prediction Score | N/A |
| Evidence Level | 無法評級（低於 L5） |
| Market Status | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why This Formula Could Not Be Evaluated

本製劑由以下 20 種成分組成，多數屬於順勢療法（Homeopathic）或草藥（Herbal）製劑常見原料：

| # | 成分 | 傳統用途 |
|---|------|---------|
| 1 | Apis Mellifera（蜜蜂） | 水腫、泌尿道炎症（順勢） |
| 2 | Arctium Lappa Root（牛蒡根） | 利尿、淋巴、皮膚 |
| 3 | Arctostaphylos Uva-Ursi Leaf（熊果葉） | 泌尿道感染（UTI）、利尿 |
| 4 | Berberis Vulgaris Root Bark（小檗根皮） | 腎結石、泌尿道（順勢） |
| 5 | Bryonia Alba Root（白苦瓜根） | 關節、呼吸道（順勢） |
| 6 | Chondrodendron Tomentosum Root（箭毒源植物） | 含箭毒鹼前驅物，肌肉鬆弛 |
| 7 | Cinchona Officinalis Bark（金雞納樹皮） | 瘧疾、退燒（奎寧來源） |
| 8 | Echinacea（紫錐菊） | 免疫支持 |
| 9 | Equisetum Hyemale（木賊） | 利尿、泌尿道 |
| 10 | Ferrosoferric Phosphate（磷酸亞鐵） | 炎症初期（Ferrum phos.，順勢） |
| 11 | Gelsemium Sempervirens Root（黃素馨根） | 神經痛、發燒（順勢；具毒性） |
| 12 | Goldenseal（金印草） | 抗菌、消化道、黏膜 |
| 13 | Juniper Berry（杜松子） | 利尿、泌尿道防腐 |
| 14 | Lytta Vesicatoria（西班牙蒼蠅，Cantharis） | 膀胱炎、尿道炎（順勢）；原物質具毒性 |
| 15 | Phosphorus | 肝、神經系統（順勢） |
| 16 | Plantago Major（車前草） | 消炎、泌尿道 |
| 17 | Pulsatilla Vulgaris（白頭翁） | 泌尿道、婦科（順勢） |
| 18 | Saw Palmetto（鋸棕欖） | 良性攝護腺肥大（BPH） |
| 19 | Solidago Virgaurea Flowering Top（一枝黃花） | 泌尿道消炎、利尿 |
| 20 | Turpentine（松節油） | 泌尿道（歷史用途）；具刺激性 |

**評估無法執行的核心原因如下：**

1. **無 DrugBank ID**：TxGNN 知識圖譜以單一分子（small molecule）為節點，本製劑為 20 種成分的複方，無法對應至任何知識圖譜節點，導致模型完全無法執行預測。

2. **順勢療法特殊性**：部分成分（如 Phosphorus、Cantharis、Pulsatilla）在順勢療法中以極低稀釋度使用，其作用機轉與現代藥理學框架不相容，難以納入 TxGNN 的 evidence-based 評估體系。

3. **原物質毒性問題**：Lytta Vesicatoria（含 cantharidin）與 Gelsemium sempervirens（含 gelsemine）原物質均具顯著毒性，若非順勢稀釋使用，安全性評估需特別審慎。

4. **無任何現有核准資料**：查無任何國家之藥品許可證，亦無 FDA/EMA/TFDA 核准記錄，無法作為監管基準。

---

## US Market Information

本製劑在美國（FDA）及台灣（TFDA）均未取得藥品許可，亦無任何 NDA/NHI 登錄紀錄。

> 查詢日期：2026-03-24 | 查詢結果：0 筆許可紀錄

---

## Safety Considerations

請參閱各成分個別的仿單或安全資訊。以下為需特別注意之原物質毒性：

- **Lytta Vesicatoria（Cantharis）**：原物質含 Cantharidin，具腎毒性及嚴重黏膜刺激性，非順勢稀釋製劑不得內服
- **Gelsemium sempervirens**：含 Gelsemine，具神經毒性，中毒劑量可導致呼吸抑制
- **Chondrodendron tomentosum**：含 D-tubocurarine（箭毒）前驅物，原物質為神經肌肉阻斷劑

藥物交互作用查詢（DDI）：未找到標準化資料（此複方製劑超出一般 DDI 資料庫的查詢範疇）。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本製劑為順勢療法/草藥複方，TxGNN 模型無法對多成分複方產生再利用預測，且現有安全性與監管資料完全缺失，無條件進行任何再利用評估。

**To proceed, the following is needed:**

- **資料重構**：若希望評估個別成分，需逐一拆分為單一活性成分（例如單獨評估 Berberine from Berberis、Quinine from Cinchona、β-sitosterol from Saw Palmetto），並分別查詢其 DrugBank ID
- **監管定性**：釐清本複方在目標市場（美國/台灣）的法規分類——是 OTC 藥品、膳食補充劑，或順勢療法製劑——以決定適用的評估標準
- **安全性資料補充**：針對含毒性原物質的成分（Cantharis、Gelsemium）取得完整的稀釋度與安全性文件
- **原廠標示查詢**：取得完整的原廠說明書（package insert）以確認實際適應症聲稱與成分配比

> ⚠️ **注意**：本報告結果僅供研究參考，不構成醫療建議。藥物再利用候選需經臨床驗證後方可應用。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


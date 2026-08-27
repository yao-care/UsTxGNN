---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 944
evidence_level: L5
indication_count: 2
---

# Mupirocin
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

# Mupirocin：從外用抗菌治療到 Pleural Empyema（肋膜膿胸）

## 一句話摘要

Mupirocin 目前無台灣/美國正式核准適應症資料，僅能依其作用機轉推論原用於**鼻腔/皮膚外用抗菌**（如鼻腔 MRSA 除菌、膿痂疹）。TxGNN 模型預測其可能對 **Pleural Empyema（肋膜膿胸）** 有效，但**目前無任何臨床試驗或文獻證據支持**，且證據包本身即指出此連結的機轉合理性偏弱，可能為知識圖譜拓樸偏誤所致。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無正式核准資料（本藥於本區未上市）；依機轉推論為鼻腔/皮膚外用抗菌（鼻腔 MRSA 除菌、膿痂疹），**未經正式來源確認** |
| 預測新適應症 | Pleural Empyema（肋膜膿胸） |
| TxGNN 預測分數 | 99.49% |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻） |
| 市場狀態 | 未上市 |
| 核准案件數 | 0 |
| 建議決策 | Hold |

---

## 為何此預測合理性存疑？

Mupirocin 的正式作用機轉資料目前缺失（original_moa 標記為 Data Gap）。但依證據包內的機轉推論說明，Mupirocin 為外用抗生素，作用機轉是抑制細菌 isoleucyl-tRNA synthetase，其**臨床劑型僅限鼻腔/皮膚外用**，並無全身性或肋膜腔給藥劑型與藥動學資料。

Pleural empyema（肋膜膿胸）多為厭氧菌或鏈球菌混合感染，需要**全身性抗生素治療合併引流**才能達到有效控制。以 Mupirocin 目前已知的外用劑型特性，並無證據顯示其能穿透至肋膜腔並達到有效殺菌濃度，因此原始（推論）用途與此預測適應症之間**缺乏合理的機轉連結**。

證據包評估認為，TxGNN 給出的高分很可能反映知識圖譜中該藥物節點與其他抗生素/感染相關節點的拓樸相似性偏誤，而非真實的藥理學合理性。此判斷同時也適用於第二順位預測（punctate epithelial keratoconjunctivitis，點狀角膜結膜炎）——該疾病多為病毒或免疫相關病因，Mupirocin 不具抗病毒活性，且無核准眼用劑型。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

（查詢紀錄：ClinicalTrials.gov 與 ICTRP 於 2026-04-21 針對 MUPIROCIN + pleural empyema 之查詢，結果數皆為 0。）

---

## 文獻證據

目前無相關文獻資料。

（查詢紀錄：PubMed 於 2026-04-21 針對 MUPIROCIN + pleural empyema 之查詢，結果數為 0。）

---

## 市場資訊

本藥於此區域**未上市**，無任何核准案件（total_licenses = 0），故無授權/劑型/適應症資料可列。

---

## 安全性考量

安全性資料目前缺失，請參考藥品仿單以取得完整安全性資訊。

**注意**：TFDA 仿單警語與禁忌資料缺失已列為 **Blocking** 等級之資料缺口（DG001），在補齊前無法進入 S1 安全性初評階段。

---

## 結論與後續建議

**決策：Hold**

**理由：**
- 證據等級僅為 L5（純模型預測，無任何臨床試驗或文獻佐證）
- 證據包本身的機轉分析已指出，Mupirocin 外用劑型與肋膜膿胸所需之全身性治療機轉間缺乏合理連結，預測分數可能源自知識圖譜拓樸偏誤而非藥理學合理性
- 本藥未上市、無核准案件，基礎安全性與劑型資料不足

**需補齊的資料/行動：**
- 取得 TFDA 仿單警語與禁忌資料（DG001，Blocking，需下載並解析仿單 PDF）
- 確認正式核准適應症與作用機轉（DG002，透過 DrugBank API 查詢）
- 評估劑型/給藥途徑相容性：確認 Mupirocin 是否存在可達肋膜腔之全身性劑型
- 待前述資料補齊後，重新評估是否有必要進入 S1 安全性初評
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Acetaminophen Chlorpheniramine
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 0
---

# Acetaminophen Chlorpheniramine
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

# ACETAMINOPHEN + CHLORPHENIRAMINE：資料不足，暫無法產生完整老藥新用預測報告

## One-Sentence Summary

ACETAMINOPHEN（乙醯胺酚）為解熱鎮痛劑，CHLORPHENIRAMINE（氯苯那敏）為第一代抗組織胺；兩者的固定劑量複方常見於感冒與過敏症狀的症狀緩解治療。
然而，本次 TxGNN 流程**未產生任何老藥新用預測結果**，台灣藥品許可證資料庫亦查無登錄紀錄，現有資料不足以進行完整的重定位評估。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 原核准適應症 | 查無台灣核准資料 |
| 預測新適應症 | 無（TxGNN 未產生預測） |
| TxGNN 預測分數 | 無 |
| 證據等級 | 無法評定 |
| 台灣上市狀態 | ✗ 未上市 |
| 許可證數量 | 0 |
| 建議決策 | **Hold** |

---

## Why is This Prediction Reasonable?

目前 TxGNN 模型未針對此複方組合（ACETAMINOPHEN + CHLORPHENIRAMINE）產生任何預測結果，故本節無法進行機轉關聯性分析。

就已知背景而言：ACETAMINOPHEN 透過抑制中樞神經系統的前列腺素合成發揮解熱鎮痛作用；CHLORPHENIRAMINE 則為競爭性 H₁ 受體拮抗劑，可抑制組織胺媒介的過敏反應。兩者均屬對症治療藥物，非疾病修飾性藥物，TxGNN 對此類複方組合的重定位預測能力可能受限。

如需推進老藥新用評估，建議將兩個活性成分分別查詢，並補充各自的 DrugBank 資料後重新執行預測流程。

---

## 台灣市場資訊

查詢結果顯示此複方組合在台灣藥品許可證資料庫中**無登錄紀錄**（許可證數量：0）。

可能原因包括：
- 以複方字串查詢時未能比對到個別成分登錄資料
- 此固定劑量複方在台灣以非處方（OTC）方式販售，且未以此確切組合名稱登錄

建議後續以個別成分名稱（ACETAMINOPHEN、CHLORPHENIRAMINE）分別查詢台灣 TFDA 資料庫。

---

## Safety Considerations

目前本 Evidence Pack 中未取得安全性資料，包括警語、禁忌、及藥物交互作用（DDI 查詢結果為 not found）。

請參閱藥品仿單了解完整安全性資訊。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN 模型未針對此複方組合產生預測結果，且台灣藥品許可證與安全性資料均付之闕如，現有資料不足以支持老藥新用評估。

**如需繼續推進，需補充以下資料：**

- [ ] 以個別成分（ACETAMINOPHEN、CHLORPHENIRAMINE）分別重新執行 TxGNN 預測，取得各自的老藥新用候選清單
- [ ] 透過 DrugBank API 補充個別成分的 DrugBank ID 及作用機轉（MOA）
- [ ] 以個別成分查詢 TFDA 資料庫，確認台灣許可證現況
- [ ] 確認 Evidence Pack 輸入格式：複方藥物建議拆分為單一成分分別處理，而非以組合字串作為查詢鍵
- [ ] 補充安全性資料（DDI、警語、禁忌），排除潛在交互作用風險
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


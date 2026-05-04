---
layout: default
title: Arnica Montana Whole Arsenic Trioxide Bos Taurus P
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 0
---

# Arnica Montana Whole Arsenic Trioxide Bos Taurus P
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

# 多成分複方製劑 (Homeopathic Complex): 無 TxGNN 預測結果

## One-Sentence Summary

本候選品為含 11 種成分的複方製劑（包括 Arnica montana、Arsenicum trioxide、Pulsatilla montana 等順勢療法及傳統成分），在美國市場目前無核准登記。由於 TxGNN 模型無法對多成分複方建立單一知識圖譜節點，**本次評估無法生成任何新適應症預測**，所有安全性與機轉資料亦均缺失，建議暫緩進一步研究。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無登記資料 |
| 預測新適應症 | 無（TxGNN 未能生成預測） |
| TxGNN 預測分數 | N/A |
| 證據等級 | L5（僅模型層級，無任何臨床或文獻依據） |
| 美國市場狀態 | 未上市 |
| NDA 件數 | 0 |
| 建議決策 | **Hold** |

---

## Why is This Prediction Reasonable?

目前無法對此複方製劑進行合理性分析，原因如下：

**成分識別問題**：此配方包含 11 種成分，其中多種為順勢療法（homeopathic）原料，包括 *Arnica montana*（山金車全株）、*Pulsatilla montana*（白頭翁全株）、Causticum（苛性鉀複合物）。這類成分在標準藥物資料庫（DrugBank、FDA Orange Book）中不存在統一的 DrugBank ID，導致 TxGNN 知識圖譜無法建立映射節點。

**MOA 資料缺失**：由於無 DrugBank ID，詳細的作用機轉資料無從取得。目前僅知 Arsenic trioxide（砒霜）作為單方藥物（品名 Trisenox）已獲 FDA 核准用於急性前骨髓細胞性白血病（APL），但在此複方中其濃度與角色不明，不能以單方藥理推論整體複方效益。

**複方評估的根本限制**：TxGNN 模型設計針對單一活性成分（single active ingredient）進行知識圖譜推理，多成分複方無法直接輸入。若要進行有效評估，必須先釐清「主要活性成分」或「複方協同機制」，方能選擇適當成分重新進行預測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻資料。

---

## 美國市場資訊

本複方製劑在美國目前無任何核准 NDA 或上市紀錄。

---

## Safety Considerations

請參閱各成分仿單之警語與禁忌事項。需特別注意：**Arsenic trioxide（砒霜）作為單方已知具有心臟毒性（QT 延長）、肝腎毒性及致骨髓抑制風險**，即便在複方中含量可能極低，仍建議在任何臨床使用前進行完整安全性評估。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN 模型無法對此 11 成分複方生成預測結果，且該製劑在美國完全無核准登記，安全性、機轉與臨床資料均缺失，現有資訊不足以支持進入下一階段評估。

**若要繼續推進，需補充以下資料：**

1. **澄清主要活性成分**：確認複方中哪一種成分具主要藥理活性，並以該單一成分重新執行 TxGNN 預測（建議優先以 Arsenic trioxide 或 Fumaric acid 作為候選）
2. **確認製劑類型與濃度**：明確各成分在製劑中的實際濃度與劑量，以判斷是否屬於順勢療法（極低濃度稀釋）或標準化學藥品
3. **DrugBank 個別查詢**：對各成分分別取得 DrugBank ID，再逐一評估重用潛力
4. **安全性文件**：取得 Arsenic trioxide 及 Fumaric acid 的完整仿單警語，評估複方安全性風險
5. **法規路徑確認**：若屬順勢療法製劑，需確認適用法規路徑（FDA OTC Homeopathic Guidance 或 NDA/ANDA）與市場准入可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


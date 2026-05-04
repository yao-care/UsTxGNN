---
layout: default
title: Activated Charcoal Ambrosia Artemisiifolia Whole E
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Ambrosia Artemisiifolia Whole E
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

# 多成分複方（均質植物/礦物組合）：無法評估藥物再利用適應症

## One-Sentence Summary

此候選藥物為一含九種成分的複方製劑，包含活性碳、豚草、小米草、洋蔥、磷、白頭翁、一枝黃花、馬錢子及硫磺，屬典型順勢療法組合配方。
TxGNN 模型**未能對此藥物產生任何新適應症預測**，且查詢日誌顯示 DrugBank 無對應紀錄（無 DrugBank ID），
現有資料不足以支撐藥物再利用評估流程，本報告僅記錄現況並提供補救建議。

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | 無紀錄（原始適應症資料缺失） |
| Predicted New Indication | 無（TxGNN 未產生預測結果） |
| TxGNN Prediction Score | 無法計算 |
| Evidence Level | L5（模型預測不適用，無任何研究支持） |
| US Market Status | 未上市 |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

目前 TxGNN **未對此多成分複方產生任何藥物再利用預測**，因此本節無法進行標準的機轉關聯性分析。

從成分組成判斷，此製劑屬於**順勢療法（Homeopathic）複方配方**，其成分包含：
- **Ambrosia artemisiifolia**（豚草）：傳統用於過敏性鼻炎
- **Euphrasia stricta**（小米草）：傳統用於眼部過敏症狀
- **Solidago virgaurea**（一枝黃花）：傳統用於呼吸道/鼻竇炎
- **Pulsatilla vulgaris**（白頭翁）：傳統用於呼吸道症狀
- **Allium cepa（洋蔥）** / **Sulfur（硫磺）** / **Phosphorus（磷）**：順勢療法常用基礎成分
- **Strychnos nux-vomica seed**（馬錢子）：含番木鱉鹼，具神經興奮性，需特別注意安全性
- **Activated Charcoal**（活性碳）：吸附/排毒用途

順勢療法製劑在分子機轉層面缺乏現代藥理學依據，TxGNN 模型的知識圖譜無法有效映射此類製劑的活性成分至 DrugBank ID，導致預測流程無法啟動。

---

## Clinical Trial Evidence

目前無相關臨床試驗已登錄（TxGNN 未產生預測適應症，無法執行證據搜索）。

---

## Literature Evidence

目前無可引用文獻（TxGNN 未產生預測適應症，無法執行文獻搜索）。

---

## US Market Information

此複方製劑在美國**無任何核准上市紀錄**（NDA 數量：0）。

---

## Safety Considerations

> ⚠️ **特別注意**：此製劑含有 **Strychnos nux-vomica seed（馬錢子種子）**，含番木鱉鹼（Strychnine）成分，具有高度神經毒性，過量使用可能導致痙攣乃至死亡。即使以順勢療法極度稀釋劑型使用，仍建議在安全性審查完成前暫停推進。

目前無其他安全性資料（警語、禁忌、藥物交互作用均無資料），如需完整安全性資訊，請參閱製造商仿單。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
此藥物因以下三項根本性障礙，無法推進藥物再利用評估流程：
1. TxGNN 模型未對此複方產生任何預測適應症（`predicted_indications` 為空）
2. 無 DrugBank ID，無法進行機轉關聯性分析
3. 含高毒性成分（馬錢子/Strychnine），安全性尚未建立

**To proceed, the following is needed:**

- **根本問題修正**：確認此候選藥物是否為有效的再利用研究標的；順勢療法複方通常不適合 TxGNN 知識圖譜預測框架
- **成分拆解評估**：若研究目的明確，建議改以**單一活性成分**（如 Strychnine、Solidago virgaurea extract）作為獨立候選分子進行預測
- **安全性審查**：取得含馬錢子製劑的毒理學資料，確認擬使用濃度的安全閾值
- **市場定位釐清**：此製劑若屬順勢療法製劑，監管路徑（如 DSHEA 膳食補充劑、順勢療法 OTC）與藥物再利用路徑有本質差異，需先釐清開發目標
- **資料補全**（若決定繼續）：
  - 自 TFDA 官網下載仿單 PDF 並解析警語/禁忌（對應 DG001）
  - 查詢 DrugBank API 取得作用機轉（對應 DG002）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


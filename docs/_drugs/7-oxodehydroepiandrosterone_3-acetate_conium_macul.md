---
layout: default
title: 7-Oxodehydroepiandrosterone 3-Acetate Conium Macul
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 0
---

# 7-Oxodehydroepiandrosterone 3-Acetate Conium Macul
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

# 多成分混合製劑（含 Somatropin 等 12 種成分）：適應症不明，TxGNN 無法預測

## One-Sentence Summary

本製劑為 12 種異質成分的混合配方，涵蓋順勢療法原料（如 Conium maculatum、Lycopodium、Sepia officinalis）、腺體萃取物（豬腎上腺、豬腦下垂體）及生長激素（Somatropin），在美國與台灣均未有核准上市紀錄。
由於成分組合極為複雜且部分成分具已知毒性，TxGNN 模型**未能產生任何預測適應症**，現有資料不足以支持老藥新用評估。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 原核准適應症 | 未知（無任何上市許可紀錄） |
| 預測新適應症 | 無（TxGNN 未產生預測結果） |
| TxGNN 預測分數 | N/A |
| 證據等級 | L5（僅模型查詢，無預測輸出；實際上低於 L5） |
| 美國市場狀態 | 未上市 |
| NDA 數量 | 0 |
| 建議決策 | **Hold（暫緩）** |

---

## Why is This Prediction Reasonable?

本製劑由 12 種高度異質成分構成，無法以單一藥理機轉描述，TxGNN 知識圖譜模型亦因此未能比對出有效的疾病節點關聯，**未產生任何預測適應症**，故本節改為說明製劑組成的已知藥理背景。

部分成分具有相對明確的藥理作用：**Somatropin**（重組人類生長激素）為已核准的處方藥，用於生長激素缺乏症；**DHEA 衍生物**（7-oxo DHEA acetate）被研究用於代謝調節；**硒（Selenium）**及**矽（Silicon dioxide）**為微量營養素。然而，**Conium maculatum**（毒芹，含 coniine 生物鹼）與**氫氟酸（Hydrofluoric acid）**在非順勢療法劑量下均具有顯著毒性，列入製劑成分需要嚴格的劑量與安全性說明。

其餘成分——Lycopodium clavatum、Sepia officinalis、牡蠣殼碳酸鈣——均為傳統順勢療法原料，在常規藥理學文獻中缺乏高品質臨床證據。整體而言，此複合配方的作用機轉不明、適應症不明，無法支持老藥新用的合理性推導。

---

## Clinical Trial Evidence

目前無相關臨床試驗登記紀錄。

（TxGNN 未輸出預測適應症，無法關聯特定疾病進行臨床試驗檢索。）

---

## Literature Evidence

目前無相關文獻資料可供引用。

---

## US Market Information

無任何上市許可紀錄。查詢結果顯示此多成分混合製劑在美國（及台灣）均無 NDA 或相應許可證。

---

## Safety Considerations

**關鍵安全警示（基於已知成分毒理學）：**

- **Conium maculatum（毒芹）**：含有 coniine 及 γ-coniceine，為強效菸鹼型乙醯膽鹼受體拮抗劑，可導致升行性運動麻痺、呼吸肌麻痺。即使在順勢療法極低劑量下，其安全邊際仍受到毒理學家關注。
- **氫氟酸（Hydrofluoric Acid）**：具強烈腐蝕性，可穿透組織並與鈣鎂離子螯合，造成低血鈣、心律不整等全身毒性。作為製劑成分，需有明確稀釋比例與安全性資料。
- **Somatropin（生長激素）**：為管制處方藥，未經授權使用可能導致肢端肥大症、糖耐量異常、顱內高壓等嚴重不良事件；與胰島素、糖皮質激素有已知藥物交互作用。
- **SUS SCROFA 腺體萃取物（豬腎上腺、豬腦下垂體）**：屬於腺體療法（glandulotherapy）原料，存在潛在的人畜共通病原體傳播風險，需符合 TSE/BSE 監管要求。

由於安全性資料缺口（Blocking 等級），目前**無法完成 S1 安全性初評**，建議在取得完整仿單或毒理資料前，不進行任何臨床應用評估。

---

## Conclusion and Next Steps

**Decision: Hold（暫緩）**

**理由：**
此製劑同時面臨三重障礙：（1）TxGNN 模型未能產生任何預測適應症；（2）含有已知毒性成分（毒芹、氫氟酸），安全性資料缺口為 Blocking 等級；（3）在美國無任何上市紀錄，市場可行性不明。在上述問題解決前，不建議推進老藥新用評估流程。

**推進前必須補齊以下資料：**

- **安全性資料（Blocking）**：取得完整的成分稀釋比例、毒理學研究報告及仿單警語，釐清 Conium maculatum 與氫氟酸的實際劑量是否達到毒性閾值
- **製劑定性**：確認此為順勢療法製劑（homeopathic）、腺體療法製劑，或複合處方藥，以決定適用的法規路徑（NDA vs. OTC Monograph vs. HMPC）
- **Somatropin 成分合規性**：確認生長激素是否以藥理活性劑量存在，若是則須單獨申請生物製劑許可
- **TxGNN 重新查詢**：將 12 種成分拆分為個別活性藥理成分（API）分別進行 TxGNN 預測，以獲取有意義的老藥新用候選
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


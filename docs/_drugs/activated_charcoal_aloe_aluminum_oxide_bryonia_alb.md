---
layout: default
title: Activated Charcoal Aloe Aluminum Oxide Bryonia Alb
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Aloe Aluminum Oxide Bryonia Alb
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

# 複方植物/順勢療法混合物：資料不足，無法完成老藥新用評估

## 一句話摘要

本候選藥物為一含 17 種成分的複方混合物（活性炭、蘆薈、氧化鋁、布里奧尼亞根等），在美國無核准上市紀錄，亦無 DrugBank ID。**TxGNN 模型未能產生任何新適應症預測**，目前安全性、機轉、臨床證據資料均不足，建議優先補齊基礎藥物資訊後再行評估。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無核准適應症紀錄 |
| 預測新適應症 | 無（TxGNN 未產生預測） |
| TxGNN 預測分數 | — |
| 證據等級 | **L5**（模型無法預測，無任何實際研究） |
| 美國市場狀態 | ✗ 未上市 |
| NDA 數量 | 0 |
| 建議決策 | **Hold** |

---

## 為何無法進行預測推論？

本候選藥物為多成分複方，包含：

> 活性炭（Activated Charcoal）、蘆薈（Aloe）、氧化鋁（Aluminum Oxide）、布里奧尼亞根（Bryonia Alba Root）、白屈菜（Chelidonium Majus）、石根（Collinsonia）、鼠李樹皮（Frangula Alnus Bark）、石松孢子（Lycopodium Clavatum Spore）、碳酸鉀（Potassium Carbonate）、大黃（Rhubarb）、水飛薊籽（Silybum Marianum Seed）、糞臭素（Skatole）、碳酸鈉（Sodium Carbonate）、馬錢子（Strychnos Nux-Vomica Seed）、豬胰臟萃取物（Sus Scrofa Pancreas）、蒲公英（Taraxacum Officinale）、硫胺素（Thiamine）

**TxGNN 知識圖譜方法依賴單一 DrugBank ID 進行節點映射**，本品為未登錄複方，系統無法辨識任何可映射節點，因此**未能產生任何疾病預測結果**。

從成分組合來看，本品多數成分具有傳統消化系統或肝膽支持用途（大黃、鼠李樹皮為通便劑；水飛薊為護肝劑；蒲公英為消化促進劑；豬胰臟萃取物含消化酶），部分成分屬順勢療法（布里奧尼亞、馬錢子、石松孢子），整體性質偏向**消化輔助/肝臟保護類**複方，但目前缺乏機轉資料支持任何推論。

---

## 臨床試驗證據

目前無相關臨床試驗登錄。

---

## 文獻證據

目前無相關文獻資料。

---

## 美國市場資訊

本品在美國無任何 NDA 核准紀錄，市場狀態為**未上市**。

---

## 安全性考量

請參閱各成分個別仿單之警語與禁忌事項。

> 特別注意：**馬錢子（Strychnos Nux-Vomica Seed）** 含士的寧（Strychnine），具有神經毒性，高劑量可致命。使用前務必確認劑量安全範圍及順勢療法稀釋比例。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
TxGNN 模型因無法識別複方中的 DrugBank 節點而未能產生任何預測，加上美國無核准紀錄、缺乏安全性資料，現階段無足夠依據支持進入評估流程。

**若要繼續推進，需補齊以下資料：**

- **澄清產品性質**：確認此複方屬於化學藥品、植物藥、順勢療法製劑或膳食補充劑，以決定適用的法規途徑
- **選定主成分**：從 17 種成分中挑選 1–3 個具 DrugBank ID 的主要活性成分，重新送入 TxGNN 進行預測
- **查詢 DrugBank**：針對 Silybum Marianum（水飛薊素/Silymarin）、Frangula Alnus（鼠李素）、Taraxacum Officinale 等有 DrugBank 登錄的成分，取得機轉資料
- **安全性資料**：尤其需確認馬錢子（Strychnos Nux-Vomica）的劑量安全上限及毒性風險
- **適應症界定**：若定位為消化/肝臟適應症，需提供至少 Phase 2 臨床試驗資料方可進入 L2 以上證據等級
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


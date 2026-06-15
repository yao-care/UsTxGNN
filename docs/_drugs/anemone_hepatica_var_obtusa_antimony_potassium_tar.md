---
layout: default
title: Anemone Hepatica Var Obtusa Antimony Potassium Tar
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 0
---

# Anemone Hepatica Var Obtusa Antimony Potassium Tar
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

# 複方順勢製劑（含百日咳相關成分）: 資料不足，無法完成老藥新用分析

## One-Sentence Summary

本品為含九種植物/礦物/生物成分的複方順勢製劑，包含 Atropa belladonna、Lobelia inflata、Antimony potassium tartrate 等傳統呼吸道用藥成分，以及 Bordetella pertussis 感染痰液（百日咳 nosode）。
TxGNN 模型**未能產生任何預測適應症**，原因為此複方在 DrugBank 中無對應 ID，無法完成知識圖譜嵌入計算。
目前**無任何臨床試驗或文獻**支持其老藥新用方向，整體資料嚴重不足。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無資料（成分組成顯示為傳統呼吸道/百日咳用途） |
| 預測新適應症 | 無（TxGNN 未產生預測） |
| TxGNN 預測分數 | — |
| 證據等級 | L5（僅有模型輸入，無實際研究） |
| US 市場狀態 | 未上市（0 件許可證） |
| 許可證總數 | 0 |
| 建議決策 | **Hold** |

---

## 為何此預測無法評估？

本品為九成分複方，性質接近順勢療法（Homeopathic）或傳統草藥複方製劑，在現代藥物資料庫中**無 DrugBank ID**，導致 TxGNN 知識圖譜無法定位此藥物節點，預測流程在輸入端即中斷。

從成分組成可推測其傳統用途方向：

- **Bordetella pertussis 感染痰液（nosode）**：順勢療法中用於百日咳的經典 nosode 製劑
- **Atropa belladonna / Hyoscyamus niger**：含阿托品/莨菪鹼，具抗膽鹼作用，傳統用於平滑肌痙攣、呼吸道症狀
- **Lobelia inflata**：含 lobeline，傳統呼吸興奮劑，曾用於支氣管痙攣
- **Antimony potassium tartrate（吐酒石）**：傳統祛痰劑，現代已少用
- **Ipecac**：傳統催吐/祛痰劑

此組合指向**呼吸道感染、百日咳或慢性支氣管炎**等傳統適應症，但均為順勢/傳統醫學脈絡，缺乏現代循證醫學支持。在無 DrugBank ID 和無 TxGNN 預測的情況下，無法進行正式的機轉關聯性分析。

---

## 臨床試驗證據

目前無相關臨床試驗已登記。

---

## 文獻證據

目前無相關文獻可供引用。

---

## US 市場資訊

本品在美國無任何 NDA/BLA/ANDA 核准紀錄（查詢結果：0 件許可證）。

---

## 安全性考量

請參閱仿單警語與禁忌症說明。

> **特別注意**：本品含有多種已知具藥理活性的成分，即便以順勢療法極低濃度使用，仍應注意以下潛在風險：
> - **Atropa belladonna / Hyoscyamus niger**：含莨菪鹼類生物鹼，過量可引起抗膽鹼中毒
> - **Antimony potassium tartrate**：含銻，具重金屬毒性
> - **Ipecac**：長期使用可能造成心肌病變
> - **Lobelia inflata**：過量可引起噁心、嘔吐、呼吸抑制

---

## 結論與後續步驟

**決策：Hold**

**理由：**
TxGNN 無法對此複方順勢製劑產生任何老藥新用預測，主要原因為缺乏 DrugBank ID 與現代藥理資料；加上美國無上市紀錄、安全性資料完全缺失，目前不具備進行老藥新用評估的基礎條件。

**若要推進，需補齊以下資料：**

1. **藥物身份確認**：確認是否有對應的 DrugBank 條目，或識別單一主要活性成分（active moiety）以便獨立評估
2. **MOA 資料**：查閱各成分的作用機轉，尤其是 Atropa belladonna 與 Lobelia inflata 的藥理文獻
3. **安全性資料**：下載並解析 FDA/TFDA 相關仿單 PDF，或查詢 Homeopathic Pharmacopoeia
4. **適應症確認**：確認此複方是否有任何國家的正式核准適應症記錄
5. **重新設計預測輸入**：若確認主活性成分，可針對單成分（如 lobeline 或 belladonna alkaloids）重新執行 TxGNN 預測流程
6. **臨床文獻搜尋**：以各成分 INN 分別進行 PubMed 搜尋，蒐集個別成分的臨床或前臨床證據

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後方可應用於臨床實踐。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


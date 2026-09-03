---
layout: default
title: Nafarelin
parent: 僅模型預測 (L5)
nav_order: 951
evidence_level: L5
indication_count: 10
---

# Nafarelin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nafarelin: 原始適應症資料缺失 → 預測新適應症 Ambras Type Hypertrichosis（證據不足）

## 一句話摘要

Nafarelin 是一種 GnRH（促性腺激素釋放激素）促效劑，但本證據包中**原始適應症與作用機轉資料均缺失**（Blocking 等級資料缺口）。
TxGNN 模型給出的第一名預測適應症為「Ambras type hypertrichosis universalis congenita」（罕見先天性多毛症），
評分高達 **99.87%**，但**無任何臨床試驗、文獻或機轉支持**，模型本身的推理註記也明確標示為「無機轉關聯」。
在同一批 10 個候選適應症中，真正具有實質證據的只有兩個（見下方「結論」），且都不是本頁預測的第一名。

---

## 總覽表

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺口（TFDA 未上市、DrugBank 授權資料為空，對應 DG001/DG002） |
| 預測新適應症 | Ambras type hypertrichosis universalis congenita |
| TxGNN 預測分數 | 99.87%（0.9986818432807922） |
| 證據等級 | L5（純模型預測，無實際研究） |
| 台灣市場狀態 | 未上市 |
| 授權許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？（或不合理？）

Nafarelin 的原始作用機轉資料在本證據包中標示為缺失（`original_moa: [Data Gap]`）。不過候選清單中其他項目的分析文字（第 9 名）提供了可信的補充資訊：Nafarelin 是 GnRH 促效劑，長期給藥會使垂體 GnRH 受體去敏感化，抑制 LH/FSH 分泌，進而降低性腺類固醇濃度——這正是其用於中樞性性早熟與子宮內膜異位症的已知機轉。

然而，針對本頁的第一名預測「Ambras type hypertrichosis universalis congenita」（一種先天性毛髮過多症候群），證據包本身的機轉關聯分析明確指出：**「無機轉關聯。此為罕見先天性毛髮過多症候群，病因與 GnRH 訊號無關，無任何臨床證據。」** 換言之，此為知識圖譜嵌入空間中的高分雜訊配對，並非具有生物學意義的假說。

TxGNN 對同一藥物產生的 10 個候選中，前 6 名與第 8、10 名均屬於此類「高分但無機轉關聯」的配對（涵蓋牙周疾病、多毛症、骨盆器官脫垂、Dandy-Walker 症候群、生殖道結核、子宮頸化生不良等），評分雖高（>99.6%）但證據等級全數落在 L5、Hold。真正值得注意的是排名第 7（生理性性功能障礙，與子宮內膜異位症疼痛相關）與第 9（中樞性性早熟）——詳見「結論」。

---

## 臨床試驗證據

目前無相關臨床試驗註冊

---

## 文獻證據

目前無相關文獻資料

---

## 台灣市場資訊

Nafarelin 目前**未於台灣上市**，無有效藥品許可證資料（`total_licenses: 0`）。

---

## 安全性考量

請參閱藥品仿單以取得安全性資訊。

（補充：DDI 查詢狀態為「未找到」，非「查無交互作用」，兩者意義不同，不應解讀為安全。）

---

## 結論與後續步驟

**決策：Hold**

**理由：**
- 資料缺口 DG001（TFDA 仿單警語/禁忌，Blocking 等級）明確標示「無法進入 S1 安全性初評」，在此缺口補齊前，任何適應症候選都不應推進。
- 本頁預測的第一名候選（Ambras type hypertrichosis）證據等級 L5，且證據包自身機轉分析已判定為無關聯的雜訊配對，不具備推進價值。

**同批候選中值得留意、但不屬本頁預測範圍的兩項：**
- **排名第 9：Central precocious puberty**（L1 / Proceed with Guardrails）——證據等級最高，但證據包特別提醒：Nafarelin（Synarel）在多國含美國已核准用於中樞性性早熟，這**很可能不是新發現，而是既有適應症因 `original_indications` 欄位資料缺口而被誤判為「新」**。應優先補齊原始適應症資料以澄清，而非當作老藥新用候選處理。
- **排名第 7：Physiological sexual disorder**（L3 / Research Question）——有 1 篇 1994 年 RCT（Nafarelin vs Danazol）支持其緩解子宮內膜異位症相關性交疼痛，但此為既有附加效益的延伸，且 TxGNN 疾病標籤與臨床性功能障礙定義是否對應，需人工核實。

**若要繼續推進，需要補充：**
- TFDA 仿單 PDF（DG001，Blocking）
- DrugBank API 查詢作用機轉（DG002）
- 原始核准適應症清單，用以釐清第 9 名候選是否為既有適應症誤判
- 若聚焦第 7 名候選，需人工核實「physiological sexual disorder」與子宮內膜異位症疼痛症狀之間的本體對應關係
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


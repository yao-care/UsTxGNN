---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
---

# Avelumab
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

以下是根據 Evidence Pack 產生的完整藥師評估報告：

---

# Avelumab: From Urothelial Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab（商品名 Bavencio）是一種抗 PD-L1 免疫檢查點抑制劑，已獲美國 FDA 核准用於 Merkel 細胞癌與局部晚期或轉移性尿路上皮癌（鉑化療後之維持治療），但目前在台灣尚未上市。
TxGNN 模型預測其可能對 **Human Herpesvirus 8-Related Tumor**（HHV-8 相關腫瘤，包含 Kaposi 肉瘤及原發性滲出性淋巴瘤）具有療效，
然而目前有 **0 項臨床試驗** 及 **0 篇文獻** 支持此方向，證據等級為最低的 **L5（模型預測，無實際研究支持）**。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 原始適應症 | 台灣 TFDA 無核准紀錄；國際核准：Merkel 細胞癌、局部晚期／轉移性尿路上皮癌（維持療法） |
| 預測新適應症 | Human Herpesvirus 8-Related Tumor |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 台灣上市狀態 | ✗ 未上市（TFDA） |
| 核准許可證數 | 0 |
| 建議決策 | **Hold** |

---

## Why is This Prediction Reasonable?

目前本 Evidence Pack 中尚無 Avelumab 正式作用機轉（MOA）資料。根據已知資訊，Avelumab 是一款完全人源化抗 PD-L1 IgG1 單株抗體，透過阻斷 PD-L1 與其受體（PD-1 及 CD80）的結合，解除腫瘤對細胞毒性 T 淋巴球的免疫抑制。值得注意的是，Avelumab 的 IgG1 Fc 段保留抗體依賴性細胞毒殺活性（ADCC），可招募自然殺手細胞直接裂解 PD-L1 陽性腫瘤細胞，此特性使其有別於 PD-1 抑制劑（如 nivolumab、pembrolizumab）。

HHV-8（Kaposi 肉瘤相關疱疹病毒／KSHV）藉由持續性病毒感染誘導腫瘤發生，相關腫瘤包含 Kaposi 肉瘤（KS）、原發性滲出性淋巴瘤（PEL）與多中心 Castleman 病（MCD）。文獻顯示 HHV-8 感染可上調腫瘤細胞表面 PD-L1 表現，為 anti-PD-L1 治療提供了理論基礎；Avelumab 的 ADCC 機制更可能對病毒轉化腫瘤具有額外殺傷效果。

然而，此預測存在重大生物學侷限。HHV-8 相關腫瘤的主要好發族群為免疫嚴重抑制患者（HIV 感染者或器官移植受者），其免疫微環境與 Avelumab 核准適應症（尿路上皮癌、Merkel 細胞癌）截然不同；PEL 屬 B 細胞源性惡性腫瘤，T 細胞耗竭模型在此不完全適用；此外，在 HIV 陽性患者中使用免疫檢查點抑制劑可能引發難以預測的免疫再活化反應。在缺乏任何臨床或基礎研究資料的情況下，此預測目前僅屬生物學假說，尚不足以支持臨床開發推進。

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Avelumab（Bavencio®）目前在台灣 **無任何 TFDA 核准許可證**，尚未於台灣上市銷售。

**國際核准紀錄（參考用）：**

| 監管機構 | 核准適應症 |
|---------|----------|
| US FDA（2017） | 不可切除或轉移性 Merkel 細胞癌（成人及 12 歲以上兒童） |
| US FDA（2020） | 鉑化療後未進展之局部晚期或轉移性尿路上皮癌——第一線維持治療（JAVELIN Bladder 100, Phase 3, N=700） |
| EMA（Bavencio） | 同上兩項適應症 |

---

## Cytotoxicity

Avelumab 屬抗腫瘤免疫治療藥物，需列出下列細胞毒性相關資訊。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（Immunotherapy）— 抗 PD-L1 免疫檢查點抑制劑；非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 低（非傳統骨髓毒性機轉；免疫介導之血球減少症〔irAE〕為可能例外） |
| 致吐性分級 | 極低（Minimal emetogenic risk，靜脈輸注製劑） |
| 監測項目 | 肝功能（ALT／AST／bilirubin）、甲狀腺功能（TSH／Free T4）、空腹血糖、CBC with differential、腎功能（creatinine）、腎上腺功能（皮質醇）；每次輸注前監測輸注反應 |
| 操作防護 | 依標準生物製劑靜脈輸注規範操作；**無需**細胞毒性藥物特殊防護裝備。根據仿單，首 4 次輸注前建議給予抗組織胺＋乙醯胺酚預防輸注反應。 |

---

## Safety Considerations

本 Evidence Pack 中台灣 TFDA 仿單警語、禁忌症及藥物交互作用資料均缺乏（Blocking data gap）。請參閱 Avelumab 原廠美國 FDA 核准仿單（Bavencio® US Prescribing Information）或 EMA SmPC 獲取完整安全性資訊。

> **特別提示（針對 HHV-8 相關腫瘤目標族群）：** 此族群（HIV 陽性或器官移植受者）通常合併使用抗病毒藥物（antiretroviral therapy, ART）或免疫抑制劑，與 Avelumab 之藥物交互作用尚無系統性評估。免疫檢查點抑制劑在此族群的 irAE 風險、免疫重建炎症症候群（IRIS）及感染性不良反應需格外謹慎評估，遠早於任何療效探索。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN 模型給出高達 99.97% 的預測分數，然而此結果完全缺乏臨床或基礎研究支持（L5）。儘管 HHV-8 腫瘤的 PD-L1 上調假說在機轉上具合理性，但目標族群特殊的免疫抑制背景及 PEL 的 B 細胞源性特徵，使得 Avelumab 的療效推論存在根本性的生物學不確定性，不符合推進臨床開發的門檻。

**To proceed, the following is needed:**

- **基礎生物標誌驗證**：HHV-8 相關腫瘤亞型（KS、PEL、MCD）之 PD-L1 表現量化及免疫微環境（TIL 組成、TMB）描述
- **臨床前數據**：建立 HHV-8 感染腫瘤模型，驗證 anti-PD-L1 ± ADCC 的抗腫瘤活性
- **MOA 資料補足**：查詢 DrugBank API（DB11945）取得完整作用機轉，用於機轉關聯性分析
- **安全性初評解鎖**：下載並解析台灣 TFDA 仿單 PDF，補齊 DG001（Blocking data gap），方可進入 S1 安全性評估
- **特殊族群安全性框架**：制定 HIV 陽性患者及器官移植受者使用免疫檢查點抑制劑的安全性評估方案，包含 ART 藥物交互作用審查
- **模型品質回饋**：本 Evidence Pack 中排名 5–8 的預測適應症（ADA 缺乏症、Reticular dysgenesis、Immunoerythromyeloid hypoplasia、非嚴重型 CID）均屬免疫缺陷疾病，與 Avelumab 機轉明顯相悖（生物學反指示），建議回饋至 TxGNN 訓練資料以修正模型偏差
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


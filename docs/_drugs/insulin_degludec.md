---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 797
evidence_level: L5
indication_count: 6
---

# Insulin Degludec
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Insulin Degludec：從第1型糖尿病適應症到「老藥新用」預測（第1型糖尿病）

## 一句話摘要

Insulin Degludec（德固胰島素，DB09564）是一款長效基礎胰島素類似物，臨床上原本即用於糖尿病患者的血糖控制。TxGNN 模型將其重新指向**第1型糖尿病（Type 1 Diabetes Mellitus）**，預測分數高達 **99.44%**，並有 **50 筆臨床試驗**與 **20 篇文獻**支持——但需注意，這實質上是藥物「本身既有適應症」被模型重新標記，而非傳統意義上的跨領域老藥新用，原因是本筆證據包在藥品原始適應症與台灣上市資料上存在缺漏（見下方說明）。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 資料缺漏：`original_indications` 與 `taiwan_regulatory.licenses` 均為空，無法從證據包直接引用；已知 Insulin Degludec 為基礎胰島素類似物，核准用途涵蓋第1型與第2型糖尿病血糖控制 |
| Predicted New Indication | Type 1 Diabetes Mellitus（第1型糖尿病） |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| 台灣上市狀態 | 未上市 |
| 藥證數量 | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

目前查無 Insulin Degludec 完整的作用機轉（MOA）描述文字（`original_moa` 標記為缺漏），但依據已知藥理學知識與本證據包中的機轉關聯性分析，Insulin Degludec 為第二代超長效基礎胰島素類似物，經皮下注射後於組織間形成可溶性多六聚體（multihexamer），緩慢且穩定地分解釋出單體進入血流，作用時間可長達 42 小時以上，藥效波動性低於傳統基礎胰島素（如 glargine、detemir）。其藥理作用為活化胰島素受體，促進周邊組織葡萄糖攝取並抑制肝醣新生／肝糖輸出。

第1型糖尿病的病理生理核心即為胰臟 β 細胞破壞導致的胰島素絕對缺乏，因此外源性基礎胰島素替代治療本就是第1型糖尿病的標準治療手段之一，機轉上高度直接對應，不需要跨適應症的外推假設。

需特別說明：本證據包中 `predicted_indications[0]` 的機轉關聯性分析明確指出，TxGNN 開發代號 NN1250 即為 Insulin Degludec，第1型糖尿病本屬其核准適應症範疇之一；證據包中「原始適應症未填、台灣未上市」的狀態，較可能反映的是本資料集在藥品原始資料欄位與台灣藥證比對上的缺口，而非該藥物真實的核准狀態。此點在下方「後續所需資料」中列為待補項目。

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02030600](https://clinicaltrials.gov/study/NCT02030600) | Phase 3 | Completed | 721 | SWITCH 2：比較 Insulin Degludec 與 Insulin Glargine 之安全性與有效性隨機交叉試驗 |
| [NCT01046110](https://clinicaltrials.gov/study/NCT01046110) | Phase 3 | Completed | 458 | BEGIN™: EARLY，NN1250（degludec）對比 sitagliptin 於胰島素初治族群之療效安全性比較 |
| [NCT03214367](https://clinicaltrials.gov/study/NCT03214367) | Phase 3 | Completed | 1392 | PRONTO-T1D：LY900014 對比 insulin lispro，兩者均併用 insulin glargine 或 degludec，於第1型糖尿病成人族群 |
| [NCT02500706](https://clinicaltrials.gov/study/NCT02500706) | Phase 3 | Completed | 1108 | Faster-acting insulin aspart 對比 NovoRapid，均併用 insulin degludec，於第1型糖尿病成人 |
| [NCT01984372](https://clinicaltrials.gov/study/NCT01984372) | N/A（上市後監測） | Completed | 6163 | Tresiba®（degludec）長期治療糖尿病患者之上市後安全性與有效性監測 |
| [NCT02662114](https://clinicaltrials.gov/study/NCT02662114) | N/A（回溯性觀察） | Completed | 2302 | EU-TREAT：歐洲多中心回溯性研究，第1型或第2型糖尿病患者轉換為 Tresiba®（degludec）後之療效 |
| [NCT04588259](https://clinicaltrials.gov/study/NCT04588259) | Phase 3 | Completed | 331 | Fast-acting insulin aspart 對比 NovoRapid，併用 insulin degludec（±metformin）於糖尿病成人 |
| [NCT03674866](https://clinicaltrials.gov/study/NCT03674866) | N/A（回溯性觀察） | Completed | 662 | CAN-TREAT：加拿大多中心回溯性研究，第1型或第2型糖尿病患者使用 Tresiba® 之療效 |
| [NCT03557892](https://clinicaltrials.gov/study/NCT03557892) | N/A | Completed | 28 | 連續皮下胰島素輸注（CSII）+CGM 對比多次注射（以 degludec 為基礎胰島素）於第1型糖尿病之隨機交叉試驗 |
| [NCT06238778](https://clinicaltrials.gov/study/NCT06238778) | Phase 2 | Active, not recruiting | 227 | HDV-Insulin Lispro 對比一般 Insulin Lispro，受試者均併用 insulin degludec，第1型糖尿病成人 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6：每週一次 Insulin Icodec 對比每日一次 Insulin Degludec，第1型糖尿病 basal-bolus 治療 Phase 3a 試驗 |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5：每週一次 Insulin Efsitora Alfa 對比每日一次 Insulin Degludec，第1型糖尿病成人 Phase 3 非劣性試驗 |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT：Insulin Degludec 對比 Insulin Detemir（均併用 Aspart）於第1型糖尿病孕婦之開放標籤非劣性試驗 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | RCT/Review | Clinical Therapeutics | Insulin Degludec 對比其他長效基礎胰島素於第1、2型糖尿病治療之系統性回顧與統合分析 |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes Obes Metab | HypoDeg：Degludec 對比 Glargine U100 於易發生夜間嚴重低血糖之第1型糖尿病患者，隨機交叉試驗 |
| [36610544](https://pubmed.ncbi.nlm.nih.gov/36610544/) | 2023 | RCT | Diabetes Res Clin Pract | INEOX：Degludec 100 IU/mL 對比 Glargine 300 IU/mL 於第1型糖尿病之單中心隨機對照試驗 |
| [34763071](https://pubmed.ncbi.nlm.nih.gov/34763071/) | 2022 | RCT | Endocr Pract | BIGLEAP：基礎胰島素 Degludec 對比幫浦給予 Aspart 於第1型糖尿病之隨機交叉試驗 |
| [36516429](https://pubmed.ncbi.nlm.nih.gov/36516429/) | 2023 | RCT | Diabetes Technol Ther | ULTRAFLEXI-1：Glargine 300 U/mL 對比 Degludec 100 U/mL，於第1型糖尿病運動前後之隨機交叉試驗 |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes Metab | Insulin Degludec 於第1、2型糖尿病隨機與觀察性試驗之現況回顧 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Review | Value Health | 成人第1型糖尿病基礎胰島素治療方案之系統性回顧與網絡統合分析 |

---

## US Market Information

目前無台灣藥證資料（`taiwan_regulatory.total_licenses = 0`，`licenses` 為空陣列）。此為已標記之高優先級資料缺口（DG001），建議向 TFDA 官網或原廠仿單另行查證上市狀態與核准適應症全文。

---

## Safety Considerations

請參閱藥品仿單以獲取安全性資訊。（`key_warnings`、`contraindications`、藥物交互作用查詢均無可用資料，且 TFDA 仿單警語／禁忌已列為 Blocking 等級資料缺口 DG001，尚無法完成 S1 安全性初評。）

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
第1型糖尿病此一預測方向擁有多筆完成之 Phase 3 RCT（如 SWITCH 2、PRONTO-T1D、BEGIN: EARLY 等）與大型上市後監測研究支持，證據等級達 L1；機轉上 Insulin Degludec 作為外源性基礎胰島素本就直接對應第1型糖尿病之胰島素絕對缺乏病理生理，關聯性強。然而本案在藥品原始適應症、台灣上市狀態、MOA 與仿單安全性資訊上皆存在資料缺口，須待補齊後才能完成完整的用藥安全評估。

**To proceed, the following is needed:**
- TFDA 仿單警語／禁忌完整資料（DG001，Blocking，需下載仿單 PDF 解析）
- DrugBank 作用機轉（MOA）完整敘述（DG002，High，需查詢 DrugBank API）
- 釐清並補齊 `original_indications` 與台灣藥證（`licenses`）資料，確認此為既有適應症之資料缺漏、而非真實未上市狀態
- 藥物交互作用（DDI）資料庫查詢結果
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


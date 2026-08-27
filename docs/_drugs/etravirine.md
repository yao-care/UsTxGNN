---
layout: default
title: Etravirine
parent: 高證據等級 (L1-L2)
nav_order: 686
evidence_level: L1
indication_count: 10
---

# Etravirine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Etravirine：從 HIV-1 感染治療 到 先天性/垂直傳染 HIV 感染預防

## 一句話摘要

Etravirine（DrugBank DB06414）是一款 NNRTI（非核苷類反轉錄酶抑制劑），原始核准族群為經治型（treatment-experienced）HIV-1 感染成人。TxGNN 模型對此藥物產生的前 10 名預測中，多數為跨物種（貓科免疫缺陷症候群、猿猴免疫缺陷病毒感染）或與抗病毒機轉無關的良性腫瘤／罕見遺傳疾病，屬知識圖譜嵌入空間鄰近造成的雜訊訊號，不具臨床意義。真正具備可信證據支持的候選是**先天性人類免疫缺乏病毒感染（congenital human immunodeficiency virus，即孕產垂直傳染防治情境）**，有 **13 筆臨床試驗**與 **1 篇文獻**支持，證據等級達 **L1**，是本報告聚焦分析的標的。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | HIV-1 感染（經治型成人），公開已知資訊；台灣藥證資料為空（未上市） |
| 預測新適應症 | 先天性 HIV 感染／孕產垂直傳染防治情境 |
| TxGNN 預測分數 | 99.79%（score 0.9979，於全部候選中排名第 5983） |
| 證據等級 | L1 |
| 台灣市場狀態 | 未上市 |
| 藥證數量 | 0 |
| 建議決策 | Proceed with Guardrails |

> 註：TxGNN 分數最高的候選（貓科免疫缺陷症候群，score 0.9998、排名第 1088）證據等級僅 L5、建議為 Hold，屬跨物種/機轉不相關的假訊號，不適合作為報告主軸，故本報告改以證據支持度最高的候選為分析對象（詳見下節說明）。

---

## 為什麼這個預測合理？

Etravirine 屬於 NNRTI（非核苷類反轉錄酶抑制劑）class，此藥理機轉為業界共識——這點也直接寫在證據包的 repurposing_rationale 中，即便正式的 `original_moa` 欄位標記為資料缺口。NNRTI 透過與 HIV-1 反轉錄酶的變構位點結合，抑制病毒複製，目前已核准用於治療經治型 HIV-1 感染成人與兒童。

先天性 HIV 感染（congenital HIV）本質上是 HIV 感染族群光譜的延伸——差別在於「孕產婦與新生兒」這個特殊族群，而非全新的疾病機轉。TxGNN 對此候選給出的推理是同機轉、不同族群的應用，而非機轉外推假說，這與臨床試驗證據（見下）高度吻合：現有 13 筆試驗中包含直接針對「HIV-1 感染孕婦」進行 etravirine 藥物動力學評估的研究（如 NCT00855335、NCT00042289），顯示產業界確實已在探索 etravirine 於孕產族群的用藥安全性與暴露量調整，支持此預測方向具備轉譯合理性。

需特別說明：本評估案候選中 disease 標籤本身（"congenital human immunodeficiency virus"）較適合理解為「垂直傳染防治／孕產期抗病毒治療」的知識圖譜對應詞，而非新生兒先天畸形類疾病，這點在解讀證據時需保持一致。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT00855335](https://clinicaltrials.gov/study/NCT00855335) | Phase 3 | Completed | 77 | 評估 HIV-1 感染孕婦體內 darunavir/ritonavir、etravirine（單用或併用）之藥物動力學，因懷孕期生理變化影響血中濃度 |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | Phase 4 | Completed | 1578 | IMPAACT P1026s：評估孕期及產後抗反轉錄病毒與抗結核藥物之藥物動力學，直接對應垂直傳染防治情境 |
| [NCT04630002](https://clinicaltrials.gov/study/NCT04630002) | Phase 1 | Completed | 54 | 評估 darunavir/ritonavir 併用 etravirine 與新藥 GSK3640254 之藥物交互作用 |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Phase 3 | Active, not recruiting | 618 | ATLAS 研究：病毒學抑制成人自 INI/NNRTI/PI 療程轉換為長效 cabotegravir + rilpivirine 之非劣效性評估 |
| [NCT02429791](https://clinicaltrials.gov/study/NCT02429791) | Phase 3 | Completed | 510 | 評估自現行 INI/NNRTI/PI 療程轉換為 dolutegravir + rilpivirine 之非劣效性 |
| [NCT03299049](https://clinicaltrials.gov/study/NCT03299049) | Phase 3b | Active, not recruiting | 1049 | ATLAS-2M：長效 cabotegravir + rilpivirine 每 8 週 vs 每 4 週給藥之療效安全性比較 |
| [NCT02938520](https://clinicaltrials.gov/study/NCT02938520) | Phase 3 | Active, not recruiting | 631 | FLAIR 研究：自 INI 單錠療程轉換為長效肌肉注射 cabotegravir + rilpivirine 之病毒抑制維持性評估 |
| [NCT02422797](https://clinicaltrials.gov/study/NCT02422797) | Phase 3 | Completed | 518 | 評估自現行 ARV 療程轉換為 dolutegravir + rilpivirine 之非劣效性（與 NCT02429791 為相近設計） |
| [NCT01458132](https://clinicaltrials.gov/study/NCT01458132) | N/A | Completed | 19 | GSK2248761 藥物暴露長期追蹤觀察登錄，族群含 HIV 感染合併癲癇病史者 |
| [NCT01199731](https://clinicaltrials.gov/study/NCT01199731) | Phase 2b | Terminated | 30 | 評估 GSK2248761 於 NNRTI 抗藥性經治成人之劑量選擇，對照組使用 etravirine 200mg BID |

> 另有 2 筆試驗（NCT04273165 Friedreich Ataxia 試驗、NCT07412977 VIROPREG 孕婦病毒感染世代研究）經標記為與本適應症不相關或資料串接疑義，已排除於上表之外。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [20587860](https://pubmed.ncbi.nlm.nih.gov/20587860/) | 2010 | Cohort（案例報告） | Antiviral Therapy | 報告 2 例懷孕期間使用 darunavir 併用 etravirine（含/不含 raltegravir）之經治型 HIV 感染孕婦案例，說明新型 ARV 藥物於高度治療經驗孕婦中拓展了可用療程選擇，惟安全性與療效資料仍有限 |

---

## 台灣市場資訊

目前台灣藥證資料庫中無 etravirine 之核准藥證（總計 0 筆），市場狀態為「未上市」。

---

## 安全性考量

請參閱藥品仿單以獲取安全性資訊。

> 說明：本證據包中的關鍵警語（key_warnings）、禁忌症（contraindications）與藥物交互作用（DDI）查詢結果均為資料缺口或查無資料，其中「TFDA 仿單警語/禁忌」被標記為 **Blocking** 等級缺口，直接影響能否進入安全性初評（S1）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
先天性 HIV／垂直傳染防治此候選具備 L1 等級證據（多筆 Phase 3/4 試驗、含孕婦族群直接藥動學研究），機轉為同一 NNRTI 類藥理延伸至孕產族群而非全新假說，合理性高；但台灣未上市、無藥證，且安全性�General資料（仿單警語、禁忌症、DDI）全數缺失，尚不足以完成完整風險評估，故不建議直接 Go，僅可在補齊安全性資料的前提下有條件推進。

**若要繼續推進，需要以下資料：**
- TFDA 仿單警語與禁忌症資料（DG001，Blocking，需下載仿單 PDF 解析）
- 詳細作用機轉（MOA）正式資料（DG002，High，查詢 DrugBank API）
- Etravirine 於孕婦／新生兒族群之正式藥物交互作用（DDI）資料庫查詢結果
- 針對「先天性 HIV／垂直傳染」此適應症標籤的孕產期安全性與劑量調整之系統性文獻回顧
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Estradiol Cypionate
parent: 僅模型預測 (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
---

# Estradiol Cypionate
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

# Estradiol Cypionate：從雌激素缺乏症狀治療到 BPES 相關卵巢早衰的輔助治療潛力

## 摘要

Estradiol Cypionate 是一種長效酯型雌激素（肌肉注射劑型），藥理學上已知用於雌激素缺乏相關症狀（更年期血管舒縮症狀、性腺功能低下、原發性卵巢功能不全）之荷爾蒙補充治療；本藥於台灣未上市，無 TFDA 核准適應症資料可供比對。

TxGNN 對本藥共產出 10 項候選新適應症，但逐一機轉審查後，其中 8 項（symptomatic form of fragile X syndrome、4 項染色體 trisomy/tetrasomy 症候群、ovarian remnant syndrome、blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement、partial autosomal trisomy/tetrasomy、luteoma of pregnancy）**經評估判定為知識圖譜鄰近性連結假影**，缺乏合理機轉且 0 筆試驗、0 筆文獻支持；另 1 項（anovulation）雖有 41 筆試驗與 3 筆文獻，但方向與治療目標相反（雌激素抑制排卵而非誘導排卵，所附文獻甚至以 estradiol cypionate「延長」乳牛產後不排卵期為結論）。

本報告聚焦於**唯一具機轉一致性的候選：Blepharophimosis-Epicanthus Inversus-Ptosis (BPES)**（TxGNN score 99.59%，rank 10311）。BPES type I 由 *FOXL2* 基因突變引起，該基因同時表現於卵巢顆粒細胞，突變會導致卵泡發育異常而合併卵巢早衰（POI）；POI 患者需雌激素補充治療已是標準臨床處置，與本藥原始藥理用途一致。然而目前**資料集中無任何直接試驗或文獻支持此連結**，屬機轉推論層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始用途 | 雌激素缺乏相關症狀之荷爾蒙補充治療（一般藥理學已知用途；本藥未於台灣上市，無 TFDA 核准適應症文字） |
| 預測新適應症 | Blepharophimosis-Epicanthus Inversus-Ptosis（BPES）相關卵巢早衰 |
| TxGNN 預測分數 | 99.59% |
| 證據等級 | L4（機轉/理論推論，無直接臨床證據） |
| 台灣上市狀態 | 未上市 |
| 台灣藥證數量 | 0 |
| 建議決策 | Hold |

---

## 為什麼此預測值得關注？

目前無 DrugBank MOA 詳細資料（Data Gap）。根據已知藥理學資訊，Estradiol Cypionate 屬長效雌激素酯類，作用機轉為活化雌激素受體，臨床上用於補充內源性雌激素不足狀態。

BPES 分為兩型：type I 除眼瞼裂狹小、內眥贅皮、眼瞼下垂三聯徵外，合併 POI；type II 則無生殖表現。已發表文獻證實 *FOXL2* 基因除決定眼瞼發育外，也是卵巢顆粒細胞分化與卵泡維持的關鍵轉錄因子，其突變會加速卵泡耗竭，導致 POI（PMID 29378385、31366388，未收錄於本 Evidence Pack，需另行查證引用細節）。POI 患者無論病因為何，標準治療皆包含雌激素補充以控制血管舒縮症狀並保護骨質與心血管系統——這與本藥原始藥理用途（雌激素缺乏症狀治療）機轉一致。

換言之，TxGNN 找到的並非「BPES 的藥物」，而是「BPES 患者中合併 POI 亞群」與「雌激素替代療法」之間的既有臨床邏輯。這是一條間接但機轉合理的路徑，區別於其他 8 項被判定為連結假影的候選。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻資料。

---

## 安全性考量

目前無可用之仿單警語、禁忌症或藥物交互作用資料，請參閱仿單安全性資訊。

---

## 結論與下一步

**決策：Hold**

**理由：**
機轉上 BPES type I 合併 POI 為已知病理生理路徑，雌激素補充治療於此族群具臨床合理性；但本候選為 TxGNN 高分預測中唯一機轉站得住腳者，資料集內仍無任何直接臨床試驗或文獻證據支持，且分數本身（99.59%）與其他 8 項已判定為假影的候選相近，顯示分數本身無法區分真實訊號與雜訊。

**若要推進，需要補齊：**
- DrugBank MOA 完整資料（DG002，High severity）
- TFDA／原廠仿單警語與禁忌症（DG001，Blocking severity，目前無法進入 S1 安全性初評）
- 直接查證 BPES type I 患者 POI 盛行率與雌激素補充治療實證（目前僅為機轉推論，PMID 29378385、31366388 未經本次 Evidence Pack 收集流程驗證）
- 確認 estradiol cypionate（肌肉注射劑型）於長期 POI 荷爾蒙補充治療的劑型適用性，相較於常規口服/貼片雌激素製劑之臨床角色

**其餘 9 項候選適應症之處置：**
- Anovulation（rank 6）：機轉方向與治療目標相反，不建議推進，Hold。
- Fragile X 相關症狀、4 項染色體 trisomy/tetrasomy 症候群、ovarian remnant syndrome、BPES due to 3q23 rearrangement、partial autosomal trisomy/tetrasomy、luteoma of pregnancy（共 8 項）：判定為 KG 鄰近性連結假影，證據等級 L5，Hold，不建議進一步投入資源查證。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


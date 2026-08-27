---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 790
evidence_level: L5
indication_count: 9
---

# Iloprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

說明:此 Evidence Pack 含 9 個候選適應症,TxGNN 原始評分最高的 rank 1(頭皮單純性稀毛症)本身在 pack 的 mechanistic_link 中已被標註為「知識圖譜雜訊,缺乏生物學合理性」且為 L5/Hold。故本報告以證據等級最高、機轉最連貫的候選 —— **PAH associated with HIV infection**(rank 8, L1, S3, Proceed with Guardrails)—— 作為主要標的撰寫,而非機械套用陣列索引 0。

---

# Iloprost: From Established PAH Treatment to HIV-Associated Pulmonary Arterial Hypertension

## One-Sentence Summary

Iloprost is a prostacyclin (PGI2) analogue used as a class-standard treatment for WHO Group 1 pulmonary arterial hypertension (PAH), acting through pulmonary vasodilation and antiplatelet effects.
The TxGNN model — together with supporting evidence in this pack — points to **Pulmonary Arterial Hypertension Associated with HIV Infection** as the most defensible repurposing candidate among nine TxGNN-predicted indications for this drug,
supported by **1 completed Phase 3 RCT** and **4 publications**, including one systematic review.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No confirmed original indication on file — this dataset lists 0 US marketing licenses for iloprost (market status: not marketed) |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with HIV Infection |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not separately available in this dataset (top-level MOA field is empty), but the evidence pack's own rationale text is consistent across multiple candidates: iloprost is a synthetic prostacyclin (PGI2) analogue that activates PGI2 receptors on pulmonary vascular smooth muscle, producing pulmonary vasodilation, inhibition of vascular remodeling, and antiplatelet aggregation. This is the core, well-established mechanism underlying iloprost's use across the WHO Group 1 PAH disease family.

HIV-associated PAH is itself a recognized WHO Group 1 PAH subtype, sharing the same underlying pathophysiology (pulmonary endothelial dysfunction, vasoconstriction, and vascular remodeling) as idiopathic and familial PAH. The repurposing signal here is therefore not a mechanistically novel hypothesis but a **sub-population extension** of an already-established drug class effect — the same logic that applies to the other PAH-subtype candidates in this pack (congenital heart disease–PAH, connective tissue disease–PAH, hemolytic anemia–PAH, schistosomiasis-PAH).

It is worth noting that TxGNN's raw highest-scoring predictions in this pack (hypotrichosis simplex of the scalp, congenital hypotrichosis milia) are explicitly flagged in the evidence pack's own rationale as likely graph-topology noise with no plausible mechanistic link and zero supporting evidence (L5/Hold). Among the biologically coherent PAH-subtype predictions, the HIV-associated PAH candidate has the strongest evidence base (L1, one completed Phase 3 RCT), which is why it is prioritized here over the raw top-ranked candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | Completed | 64 | Multicenter, double-blind, randomized, placebo-controlled crossover study (PROWESS 15) assessing a single dose of inhaled iloprost on exercise capacity in symptomatic PAH patients — enrolled idiopathic/familial PAH and PAH associated with HIV or drugs/toxins, either treatment-naive or on stable background bosentan/ambrisentan/sildenafil |

Note: this trial's population includes HIV-associated PAH as one of several enrolled subgroups rather than an HIV-PAH-exclusive cohort; subgroup-specific efficacy data for the HIV-PAH population is not isolated in this pack.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Systematic Review | American Journal of Respiratory Medicine | Reviews prostanoid therapy across PAH etiologies, explicitly grouping HIV-associated PAH with idiopathic and collagen vascular disease–associated PAH as sharing near-identical obstructive pulmonary microvascular pathology |
| [17195895](https://pubmed.ncbi.nlm.nih.gov/17195895/) | 2006 | Review | The Mount Sinai Journal of Medicine, New York | Overview of HIV-related pulmonary arterial hypertension, incidence (~0.5% of HIV-infected individuals), and treatment considerations |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review | Kardiologiia | Reviews controlled trials of prostacyclin and synthetic analogues across PAH subtypes including HIV infection–associated PAH |
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Registry/Cohort | Terapevticheskii Arkhiv | Six-year National Registry analysis of PAH prevalence, clinical course, therapy, and mortality |

## US Market Information

Currently no NDA or marketing authorization is on file for iloprost in this dataset — `total_licenses` is 0 and market status is recorded as "not marketed." No product/dosage-form table can be produced from available data.

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields in this dataset — key warnings, contraindications, and drug interactions — are unpopulated; note that `DG001` in the source metadata flags TFDA/FDA label warnings and contraindications as a **Blocking** data gap for safety pre-screening.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
HIV-associated PAH is a mechanistically coherent, class-established extension of iloprost's core PAH indication, supported by a completed Phase 3 RCT and a systematic review — the strongest evidence tier (L1) among the nine candidates in this pack. However, the pivotal trial did not isolate HIV-PAH as a standalone efficacy cohort, and iloprost currently has zero marketing licenses on file in this dataset.

**To proceed, the following is needed:**
- Resolve `DG001` (Blocking): obtain TFDA/FDA package insert warnings and contraindications before any S1 safety pre-screening
- Resolve `DG002` (High): confirm detailed mechanism-of-action data directly from DrugBank rather than inferring from rationale text
- Subgroup-level efficacy data for the HIV-PAH population specifically (from NCT00709956 or subsequent studies)
- Drug-drug interaction review for concomitant antiretroviral therapy, given the target population
- Formal regulatory filing pathway, since no existing NDA/marketing authorization exists for this product in the source dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


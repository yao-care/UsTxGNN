---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Axitinib
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

使用 `txgnn-pipeline` 技能確認報告生成適用範圍後，現在根據 Evidence Pack JSON 產生完整評估報告。

---

# Axitinib: From Advanced Renal Cell Carcinoma to Renal Cell Carcinoma Associated with Neuroblastoma

> **Multi-Indication Report** — Candidate ID: TW-DB06626-multi | Data Cutoff: 2026-05-01

---

## One-Sentence Summary

Axitinib is a second-generation selective VEGFR-1/2/3 tyrosine kinase inhibitor, globally recognized for treating advanced renal cell carcinoma, though no regulatory approvals were captured in the available dataset.
The TxGNN model ranks **renal cell carcinoma associated with neuroblastoma** as the top predicted new indication with a score of **99.90%**,
however this ultra-rare variant currently has **0 clinical trials** and **0 publications** providing direct support — making it an early hypothesis-generating signal only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No regulatory approvals in dataset; globally recognized for advanced renal cell carcinoma |
| Predicted New Indication | Renal cell carcinoma associated with neuroblastoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | Not marketed (0 regulatory approvals in dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Axitinib in this evidence pack. Based on published literature referenced within the evidence base, Axitinib is an oral second-generation tyrosine kinase inhibitor and a potent, highly selective inhibitor of VEGF receptors 1, 2, and 3 (VEGFR-1/-2/-3), with IC₅₀ values approximately 10-fold lower than first-generation agents such as sunitinib or sorafenib. Its established mechanism targets the VHL/HIF/VEGF signaling axis that drives tumor angiogenesis, particularly in clear cell renal cell carcinoma.

Renal cell carcinoma associated with neuroblastoma is an extremely rare and poorly characterized variant. It may share biological features with translocation-associated RCC subtypes — such as Xp11.2/TFE3 fusion RCC — which activate VEGF and mTOR signaling downstream of transcription factor dysregulation. Under this theoretical framework, VEGFR inhibition could have some relevance. However, the molecular driver landscape and degree of VEGF pathway dependency in this specific entity have not been systematically studied.

The high TxGNN score (0.999) reflects topological proximity within the biomedical knowledge graph — both entities share connected nodes through RCC biology and kidney cancer pathways — rather than any direct clinical or preclinical evidence of efficacy. This prediction is best understood as a hypothesis-generating signal. Foundational disease characterization, including natural history registry data and molecular profiling, must precede any therapeutic investigation.

---

## Clinical Trial Evidence

*(Primary prediction: renal cell carcinoma associated with neuroblastoma)*

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

*(Primary prediction: renal cell carcinoma associated with neuroblastoma)*

Currently no related literature available for this specific indication.

---

## Multi-Indication Prediction Landscape

Since this is a multi-indication evaluation, the following table summarizes all 10 TxGNN-predicted indications for Axitinib.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Trials | Literature | Recommendation |
|------|---------------------|------------|--------------|--------|-----------|----------------|
| 1 | Renal cell carcinoma associated with neuroblastoma | 99.90% | L5 | 0 | 0 | Hold |
| 2 | RCC — Xp11.2 translocations / TFE3 gene fusions | 99.90% | L3 | 1 | 0 | Research Question |
| 3 | Unclassified renal cell carcinoma | 99.90% | L3 | 2 | 0 | Research Question |
| 4 | **Childhood kidney cell carcinoma** | 99.87% | **L2** | 2 | 2 | **Proceed with Guardrails** |
| 5 | Liposarcoma | 99.87% | L4 | 0 | 1 | Hold |
| 6 | **Renal carcinoma** | 99.85% | **L1** | 50+ | 20+ | **Proceed with Guardrails** |
| 7 | Ovarian myxoid liposarcoma | 99.84% | L5 | 0 | 0 | Hold |
| 8 | Angiolipoma | 99.83% | L5 | 0 | 0 | Hold |
| 9 | Collecting duct carcinoma | 99.81% | L3 | 1 | 20+ | Research Question |
| 10 | Familial spontaneous pneumothorax | 99.78% | L5 | 0 | 0 | Hold |

---

## Evidence Spotlight: Childhood Kidney Cell Carcinoma (Rank 4 — L2)

The most actionable novel indication. Pediatric use is not included in standard adult approvals and represents a genuine unmet medical need.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Active, Not Recruiting | 15 | Randomized trial of Axitinib + Nivolumab vs. single-agent Nivolumab for TFE/translocation RCC across all age groups; directly targets pediatric Xp11.2 RCC subtype; results expected November 2026 |
| [NCT04510597](https://clinicaltrials.gov/study/NCT04510597) | Phase 3 | Recruiting | 364 | PROBE Trial: Immunotherapy-based combination ± cytoreductive nephrectomy in metastatic RCC; includes a pediatric RCC age subgroup |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31012542](https://pubmed.ncbi.nlm.nih.gov/31012542/) | 2019 | Review | Pediatr Blood Cancer | Advanced pediatric RCC treatment overview; highlights the critical lack of dedicated clinical trial data and the need for prospective studies of targeted agents in children |
| [26279736](https://pubmed.ncbi.nlm.nih.gov/26279736/) | 2015 | Case Report | Can Urol Assoc J | First reported use of axitinib in a 12-year-old with malignant epithelioid angiomyolipoma; adult treatment protocols including axitinib applied with acceptable tolerability; concluded adult protocols may be transferable to rare childhood malignancies |

---

## Evidence Spotlight: Renal Carcinoma (Rank 6 — L1)

The strongest evidence base across all predictions. Multiple completed Phase 3 RCTs with up to 5-year follow-up establish definitive efficacy.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02853331](https://clinicaltrials.gov/study/NCT02853331) | Phase 3 | Completed | 861 | **KEYNOTE-426**: Pembrolizumab + Axitinib vs. Sunitinib first-line mRCC; dual primary endpoints (OS + PFS) met; benefit sustained to 5-year follow-up |
| [NCT02684006](https://clinicaltrials.gov/study/NCT02684006) | Phase 3 | Completed | 886 | **JAVELIN Renal 101**: Avelumab + Axitinib vs. Sunitinib; significantly prolonged PFS in PD-L1+ and all-comer first-line mRCC populations |
| [NCT00678392](https://clinicaltrials.gov/study/NCT00678392) | Phase 3 | Completed | 723 | **AXIS**: Axitinib vs. Sorafenib second-line mRCC; pivotal approval trial demonstrating superior PFS |
| [NCT00920816](https://clinicaltrials.gov/study/NCT00920816) | Phase 3 | Completed | 492 | Confirmatory Phase 3: Axitinib vs. Sorafenib — confirmed superior tumor progression delay in mRCC |
| [NCT04394975](https://clinicaltrials.gov/study/NCT04394975) | Phase 3 | Completed | 421 | **RENOTORCH**: Toripalimab + Axitinib vs. Sunitinib first-line; demonstrated superior efficacy in intermediate/poor-risk advanced RCC |
| [NCT01599754](https://clinicaltrials.gov/study/NCT01599754) | Phase 3 | Terminated | 724 | Adjuvant Axitinib vs. Placebo post-nephrectomy in high-risk RCC; terminated — primary endpoint (DFS) not met |
| [NCT03494816](https://clinicaltrials.gov/study/NCT03494816) | Phase 2 | Completed | 24 | **NAXIVA**: Neoadjuvant Axitinib for clear cell RCC with venous tumor thrombus; 35% VTT down-staging response rate |
| [NCT05808608](https://clinicaltrials.gov/study/NCT05808608) | Phase 1/2 | Active, Not Recruiting | 37 | Cadonilimab + Axitinib first-line for special pathological RCC subtypes (non-clear cell); safety and efficacy evaluation |
| [NCT05256472](https://clinicaltrials.gov/study/NCT05256472) | Phase 2 | Active, Not Recruiting | 70 | Cadonilimab ± Axitinib for advanced/metastatic RCC; dose optimization and efficacy in clear cell and non-clear cell disease |
| [NCT05287464](https://clinicaltrials.gov/study/NCT05287464) | N/A | Recruiting | 1,220 | **ARON-1**: International multicentric real-world study of immuno-combinations in mRCC; includes genomic and biomarker substudies |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/) | 2019 | Phase 3 RCT | N Engl J Med | KEYNOTE-426 primary analysis: Pembrolizumab + Axitinib superior to Sunitinib across all IMDC risk groups |
| [30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) | 2019 | Phase 3 RCT | N Engl J Med | JAVELIN Renal 101: Avelumab + Axitinib significantly prolonged PFS vs. Sunitinib in first-line mRCC |
| [40750932](https://pubmed.ncbi.nlm.nih.gov/40750932/) | 2025 | Phase 3 RCT (5-yr FU) | Nat Med | KEYNOTE-426 5-year analysis: Durable OS and PFS benefit confirmed; exploratory biomarker predictors identified |
| [37500340](https://pubmed.ncbi.nlm.nih.gov/37500340/) | 2023 | Phase 3 RCT (43-mo FU) | Eur Urol | KEYNOTE-426 43-month follow-up: Sustained dual-primary-endpoint superiority; OS HR maintained |
| [37872020](https://pubmed.ncbi.nlm.nih.gov/37872020/) | 2024 | Phase 3 RCT | Ann Oncol | RENOTORCH: Toripalimab + Axitinib vs. Sunitinib — superior efficacy in intermediate/poor-risk advanced RCC |
| [33284113](https://pubmed.ncbi.nlm.nih.gov/33284113/) | 2020 | Phase 3 RCT (extended FU) | Lancet Oncol | KEYNOTE-426 extended follow-up: Confirmed durable OS superiority for pembrolizumab + axitinib |
| [32895571](https://pubmed.ncbi.nlm.nih.gov/32895571/) | 2020 | Biomarker Analysis | Nat Med | JAVELIN Renal 101 biomarker analysis: PD-L1 and TMB not predictive; FcγR polymorphisms explored |
| [29033542](https://pubmed.ncbi.nlm.nih.gov/29033542/) | 2017 | Review | Drug Des Devel Ther | Axitinib in RCC: pharmacokinetics, clinical efficacy across treatment lines, and place in therapy |
| [28276433](https://pubmed.ncbi.nlm.nih.gov/28276433/) | 2017 | Review | Nat Rev Dis Primers | RCC comprehensive review: VHL/HIF pathway, epigenetic drivers, tumor heterogeneity, and treatment evolution |
| [39326645](https://pubmed.ncbi.nlm.nih.gov/39326645/) | 2024 | Review | Crit Rev Oncol Hematol | Narrative review of axitinib outcomes across pediatric, young adult, and adult RCC — highlights PK/PD extrapolation challenges |

---

## US Market Information

No regulatory approvals for Axitinib were recorded in the dataset (Taiwan FDA records: 0 approvals; market status: 未上市).

> **Context Note:** Axitinib (Inlyta®, Pfizer) holds US FDA approval for advanced renal cell carcinoma — as second-line monotherapy (approved January 2012, based on the AXIS trial) and in combination with pembrolizumab as first-line therapy (approved April 2019, based on KEYNOTE-426). It is also approved in the EU, Japan, and South Korea. The absence of Taiwan regulatory records likely reflects a data collection gap (Data Gap DG001); TFDA package insert retrieval is required for a complete Taiwan regulatory assessment.

---

## Cytotoxicity

Axitinib is an antineoplastic agent indicated for renal cell carcinoma, a malignant disease.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective VEGFR tyrosine kinase inhibitor (second-generation); not a conventional cytotoxic agent; does not directly damage DNA |
| Myelosuppression Risk | Low (VEGFR TKIs are not typically associated with clinically significant bone marrow suppression; distinct from fluoropyrimidines or platinum agents) |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood pressure (hypertension is a VEGFR class effect requiring proactive management), thyroid function, hepatic enzymes (ALT/AST), renal function, urinalysis (proteinuria), CBC |
| Handling Protection | Standard oral targeted therapy precautions apply; cytotoxic drug handling protocols not typically mandated for oral TKIs in routine clinical settings, but institutional policies should be followed |

---

## Safety Considerations

Please refer to the package insert for safety information.

> No Taiwan regulatory safety data (warnings or contraindications) was captured in this evidence pack — Data Gap DG001 is blocking for initial safety evaluation. Drug-drug interaction queries returned no records. Clinicians should consult the Inlyta® US prescribing information for full safety guidance, particularly regarding hypertension, arterial and venous thromboembolic events, hepatotoxicity, GI perforation, fistula formation, and impaired wound healing. TFDA package insert retrieval (via TFDA website PDF download) is required before any clinical decision-making in Taiwan.

---

## Conclusion and Next Steps

### Primary TxGNN Prediction (Rank 1): Renal Cell Carcinoma Associated with Neuroblastoma

**Decision: Hold**

**Rationale:**
This ultra-rare variant has no clinical or preclinical evidence base for VEGFR inhibition, and the 99.90% TxGNN score reflects knowledge graph topology rather than any therapeutic signal. Disease characterization must come before any drug repurposing investigation.

**To proceed, the following is needed:**
- Natural history registry to characterize this variant's epidemiology and molecular profile
- Molecular profiling to determine whether VEGF pathway dependency is present
- Preclinical studies (cell line / PDX models) with axitinib
- MOA data retrieval — Data Gap DG002 (DrugBank API query for DB06626)
- TFDA safety data retrieval — Data Gap DG001 (TFDA website package insert PDF)

---

### Highest-Priority Novel Indication: Childhood Kidney Cell Carcinoma (Rank 4)

**Decision: Proceed with Guardrails**

**Rationale:**
Pediatric RCC — especially Xp11.2 translocation subtypes — has a plausible mechanistic basis for VEGFR inhibition (TFE3 → VEGF/mTOR activation), one active Phase 2 RCT directly evaluating axitinib in this population, and a pediatric case report confirming tolerability. This represents a genuine unmet medical need with emerging prospective data.

**To proceed, the following is needed:**
- Await results from NCT03595124 (completion: November 2026)
- Pediatric PK/PD modeling and age-appropriate dose optimization
- Biomarker studies linking TFE3 fusion status to VEGFR inhibitor sensitivity
- Pediatric-specific safety monitoring plan including growth, endocrine, and developmental endpoints

---

### Strongest Evidence Base: Renal Carcinoma (Rank 6)

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs with up to 5-year follow-up (KEYNOTE-426, JAVELIN Renal 101, AXIS, RENOTORCH) provide L1 evidence for axitinib efficacy in advanced RCC. This is consistent with the drug's existing global approval profile. Taiwan market entry is feasible via TFDA NDA submission using existing regulatory dossiers.

**To proceed, the following is needed:**
- TFDA NDA submission leveraging existing Phase 3 evidence package
- TFDA package insert safety data retrieval (DG001 remediation)
- Taiwan-specific post-marketing surveillance plan
- Evaluation of commercialization pathway for the Taiwan market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


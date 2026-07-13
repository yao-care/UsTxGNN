---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 628
evidence_level: L5
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Temozolomide: From Malignant Glioma to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide (TMZ) is an oral imidazotetrazine DNA alkylating agent that has become the global standard of care for glioblastoma and anaplastic astrocytoma since the landmark Stupp et al. (2005) Phase 3 trial.
The TxGNN model predicts it may be effective for **Adult Astrocytic Tumour**, with **2 clinical trials** and **20 publications** currently supporting this direction.
This prediction closely aligns with the drug's well-established global clinical evidence base, making it one of the strongest validation cases in the TxGNN pipeline.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Taiwan; globally approved for Glioblastoma and Anaplastic Astrocytoma |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed (no records in current regulatory dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Temozolomide is an imidazotetrazine-class DNA alkylating agent. Under physiological pH, it spontaneously hydrolyzes to the active metabolite MTIC (5-(3-methyltriazen-1-yl)imidazole-4-carboxamide), which methylates DNA at three key positions: O6-guanine (~5%), N7-guanine (~70%), and N3-adenine (~9%). The O6 methylation lesions trigger the mismatch repair (MMR) system to generate DNA double-strand breaks, ultimately inducing G2/M cell cycle arrest and apoptosis. MGMT (O6-methylguanine-DNA methyltransferase) is the primary resistance mechanism; tumors with MGMT promoter methylation demonstrate significantly enhanced response to TMZ.

Adult astrocytic tumours—including glioblastoma (WHO Grade 4) and anaplastic astrocytoma (WHO Grade 3)—are rapidly dividing, infiltrative CNS malignancies with high susceptibility to DNA alkylating agents. TMZ's favorable pharmacokinetic profile (lipophilicity LogP ~0.9, molecular weight 194 Da) allows effective penetration of the blood-brain barrier, achieving CSF exposure approximately 30–40% of plasma levels. This CNS penetration is a critical pharmacological advantage that most conventional chemotherapy agents lack.

The biological rationale is substantiated by decades of high-quality clinical evidence. The 2005 EORTC-NCIC Phase 3 trial established TMZ concurrent with and adjuvant to radiotherapy as the global standard of care for newly diagnosed glioblastoma, improving median overall survival from 12.1 to 14.6 months and 2-year survival from 10.4% to 26.5%. Subsequent studies have confirmed its role in MGMT-methylated elderly patients (NOA-08), in combination with tumor-treating fields (EF-14), and in MGMT-methylated patients when combined with lomustine (CeTeG/NOA-09). The TxGNN prediction is therefore a textbook validation of an established indication, underscoring the model's predictive validity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Head-to-head RCT comparing TMZ monotherapy vs. PCV (procarbazine + lomustine + vincristine) in recurrent WHO Grade III–IV astrocytic tumours; large-sample, fully powered comparison establishing TMZ as the preferred chemotherapy in this setting |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of XL184 (MET/VEGFR2 inhibitor) combined with TMZ and radiotherapy in newly diagnosed glioblastoma; TMZ used at standard dose as backbone agent; supports tolerability of TMZ in combination regimens |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT (Phase 3) | N Engl J Med | Stupp trial: TMZ + radiotherapy vs. radiotherapy alone in newly diagnosed glioblastoma; mOS 14.6 vs. 12.1 months; 2-year survival 26.5% vs. 10.4%; established current standard of care |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT Long-term Follow-up | Lancet Oncol | 5-year analysis of EORTC-NCIC trial; confirmed durable survival benefit with TMZ; MGMT promoter methylation identified as the key predictive biomarker for treatment response |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT (Phase 3) | JAMA | EF-14 trial: Tumor-treating fields + TMZ vs. TMZ alone in maintenance phase; addition of TTFields improved mOS from 16.0 to 20.9 months, leading to FDA approval of TTFields device |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT (Phase 3) | Lancet | CeTeG/NOA-09 trial: lomustine + TMZ vs. TMZ alone in newly diagnosed MGMT-methylated GBM; combination therapy superior in methylated subgroup, demonstrating potential to intensify TMZ-based regimens |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT (Phase 3) | Lancet Oncol | NOA-08 trial: dose-dense TMZ vs. radiotherapy alone in elderly patients (≥65) with malignant astrocytoma; established TMZ as primary treatment option for MGMT-methylated elderly patients who cannot tolerate full RT |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT (Phase 3) | N Engl J Med | Adding bevacizumab to TMZ + radiotherapy did not improve OS in newly diagnosed GBM despite PFS improvement; confirmed TMZ + RT as the non-negotiable standard backbone |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | RCT / Phase 3 | J Neurooncol | TMZ-based concurrent chemoradiotherapy in anaplastic astrocytoma (AA) and anaplastic oligo-astrocytoma (AOA); extended evidence of TMZ efficacy beyond GBM to lower-grade astrocytic tumours |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT (Phase 3) | J Clin Oncol | NRG Oncology BN007: dual immune checkpoint blockade (ipilimumab + nivolumab) with TMZ in MGMT-unmethylated newly diagnosed GBM; TMZ remains the standard chemotherapy backbone in novel combination strategies |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Systematic Review | JAMA | Comprehensive review of primary malignant brain tumors in adults; summarizes TMZ role in standard of care, MGMT biomarker utility, incidence trends, and emerging therapeutic approaches |
| [10914698](https://pubmed.ncbi.nlm.nih.gov/10914698/) | 2000 | Review | Clin Cancer Res | Foundational overview of TMZ mechanism, pharmacokinetics, and early Phase 2 clinical data in malignant glioma; documents initial proof-of-concept for CNS activity and oral bioavailability |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Alkylating agent — Imidazotetrazine class) |
| Myelosuppression Risk | Moderate-High — Thrombocytopenia and neutropenia are the dose-limiting toxicities; nadir typically at Days 21–28 of each 28-day cycle; Grade 3/4 thrombocytopenia occurs in ~14% of patients |
| Emetogenicity Classification | Moderate to High — Prophylactic antiemetics (5-HT3 antagonist ± NK1 antagonist) are strongly recommended |
| Monitoring Items | CBC with differential (before each cycle and at Day 22), liver function (ALT, AST, bilirubin), renal function (creatinine); MGMT promoter methylation status testing recommended prior to initiation for patient stratification |
| Handling Protection | Must follow cytotoxic drug handling regulations; capsules should not be opened or crushed; healthcare workers should wear protective gloves when handling; considered hazardous per NIOSH classification |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Temozolomide carries L1-level evidence for adult astrocytic tumours, supported by multiple completed Phase 3 RCTs — including the landmark 2005 Stupp trial published in the New England Journal of Medicine — that established it as the global standard of care for glioblastoma and anaplastic astrocytoma. The TxGNN prediction is strongly validated by existing clinical evidence, representing one of the most credible repurposing signals in the dataset. The primary outstanding gap is the absence of local Taiwan regulatory registration and associated pharmacovigilance documentation.

**To proceed, the following is needed:**
- Taiwan TFDA regulatory registration (NDA submission) for the glioblastoma and anaplastic astrocytoma indications
- Local Taiwan package insert review to establish key warnings, contraindications, and DDI profile (classified as Blocking data gap DG001)
- MGMT promoter methylation testing infrastructure for patient stratification prior to treatment initiation
- Reimbursement pathway evaluation under the Taiwan National Health Insurance (NHI) system
- Drug interaction assessment, particularly with antiepileptic agents commonly co-prescribed in brain tumor patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


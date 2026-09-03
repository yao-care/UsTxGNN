---
layout: default
title: Trabectedin
parent: 僅模型預測 (L5)
nav_order: 1245
evidence_level: L5
indication_count: 1
---

# Trabectedin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Trabectedin: From [Original Indication Unavailable] to Female Breast Carcinoma

## One-Sentence Summary

Trabectedin (DrugBank DB05109) is a marine-derived cytotoxic agent that is **not currently marketed in this jurisdiction**, and its original approved indication text is not available in the current dataset. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **2 clinical trials** and **20 publications** currently identified as supporting or contextual evidence — though most of this evidence is indirect (safety studies, single-arm Phase 2 trials, and preclinical work) rather than confirmatory Phase 3 data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this dataset (drug not marketed here; internationally, trabectedin is approved for soft tissue sarcoma and platinum-sensitive ovarian cancer in combination with pegylated liposomal doxorubicin) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for trabectedin is not available in this dataset as a structured field. Based on the supporting literature, trabectedin is a DNA minor-groove alkylating agent that binds DNA and interferes with transcription-coupled nucleotide excision repair (TC-NER); it also modulates the tumour microenvironment by reducing tumour-associated macrophages and pro-inflammatory cytokine signalling. It is currently used internationally for soft tissue sarcoma and, in combination with pegylated liposomal doxorubicin, for relapsed platinum-sensitive ovarian cancer.

The mechanistic rationale for breast cancer centers on a specific molecular subgroup rather than the disease as a whole: tumours with homologous recombination deficiency (HRD), particularly BRCA1/2-mutated tumours (which represent roughly 5–10% of breast cancers), are selectively sensitive to trabectedin's DNA-repair-interfering mechanism. This is supported by preclinical and early clinical data (e.g., PMID 23792433, PMID 24692579) showing activity in BRCA-mutated and hormone receptor-positive/HER2-negative breast cancer models and patients. However, this mechanistic link applies to a molecular subtype, not to female breast carcinoma broadly, which should be considered when interpreting the TxGNN score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Evaluated olaparib as maintenance therapy after response to trabectedin + pegylated liposomal doxorubicin in recurrent ovarian carcinoma (BRCA-relevant population); trabectedin used as prior/lead-in therapy, not the primary study drug. Indirect support only, very small sample. |
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | Completed | 76 | Single-blind, placebo-controlled QT/QTc cardiac safety study of trabectedin in advanced solid tumors — a safety/pharmacology trial, not an efficacy trial for breast cancer. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Phase 2 (randomized, single-arm comparison) | Clinical Breast Cancer | Multicenter Phase 2 study of single-agent trabectedin in advanced breast cancer post-anthracycline/taxane, comparing two administration regimens; assessed efficacy and safety directly in breast cancer patients. |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Phase 2 single-arm trial | Clinical Breast Cancer | Phase 2 study of trabectedin in HR-positive/HER2-negative advanced breast cancer, stratified by XPG gene expression as a predictive biomarker. |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2, first-in-class | Annals of Oncology | International Phase 2 trial showing trabectedin activity specifically in germline BRCA1/2-mutated metastatic breast cancer. |
| [25722380](https://pubmed.ncbi.nlm.nih.gov/25722380/) | 2015 | Exploratory analysis of Phase 3 (ovarian cancer, off-target) | Annals of Oncology | Exploratory biomarker analysis from the Phase 3 OVA-301 trial showing BRCA1/XPG mutation status predicts response to trabectedin + PLD; supports the DNA-repair-deficiency mechanistic rationale, though population is ovarian cancer. |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opinion on Investigational Drugs | Reviews trabectedin's mechanism (transcription regulation, tumour-associated macrophage modulation) and its investigational role in breast cancer. |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treatment Reviews | Reviews trabectedin as a chemotherapy option specifically for BRCA-deficient tumours, including breast cancer. |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunology Research | Trabectedin depletes immunosuppressive myeloid cells and enhances IL-12-driven NK-cell antitumor activity in triple-negative breast cancer models. |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preclinical/in vitro | Toxicology Letters | Trabectedin induces apoptosis via distinct pathways in MCF-7 (HER2-/ER+) and MDA-MB-453 (HER2+/ER-) breast cancer cell lines. |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Preclinical | European Cytokine Network | Demonstrates anti-angiogenic effects of trabectedin on breast cancer cell lines and endothelial cells. |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 (mixed sarcoma/breast population) | European Journal of Cancer | Phase 1 pharmacokinetic study of trabectedin + doxorubicin in soft tissue sarcoma and advanced breast cancer, showing feasibility and antitumor activity. |

---

## US Market Information

No approved authorizations are on record for this drug in this jurisdiction (`total_licenses: 0`, `market_status: 未上市 / Not Marketed`). No product table is available.

---

## Cytotoxicity

Trabectedin is a marine-derived cytotoxic antineoplastic agent (DNA minor-groove alkylator), meeting the criteria for this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA minor-groove alkylating agent, marine-derived alkaloid) |
| Myelosuppression Risk | High — literature reports Grade 3–4 neutropenia in approximately 50% and thrombocytopenia in approximately 20% of patients (per soft tissue sarcoma experience, PMID 19496709) |
| Emetogenicity Classification | Moderate to High |
| Monitoring Items | CBC with differential, liver function tests (hepatotoxicity is common), renal function, creatine phosphokinase (rhabdomyolysis has been reported), cardiac monitoring (QT/QTc, per NCT00786838) |
| Handling Protection | Yes — cytotoxic drug handling precautions (closed-system transfer devices, PPE) apply per standard antineoplastic handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. Structured safety data (key warnings, contraindications, and drug-drug interactions) are currently marked as data gaps in this evidence pack; this is flagged as a **Blocking** data gap (DG001) that must be resolved before a formal safety (S1) evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L2, supported only by single-arm Phase 2 trials and largely preclinical/review literature rather than confirmatory randomized data specific to breast cancer; combined with a Blocking data gap in TFDA/label safety information and the fact that the drug is not currently marketed in this jurisdiction, the evidence base is not yet sufficient to proceed.

**To proceed, the following is needed:**
- Resolve DG001: obtain official label warnings/contraindications (e.g., via TFDA or reference regulator such as EMA/FDA, since the drug is not locally marketed)
- Resolve DG002: confirm mechanism of action documentation via DrugBank API
- Additional randomized or larger-scale trial data specifically in breast cancer, ideally enriched for BRCA1/2-mutated or HRD-positive subgroups, given the mechanistic rationale points to this subtype rather than breast cancer broadly
- Formal route-of-administration compatibility assessment (currently marked "pending" in the evidence pack)
- Drug-drug interaction data, given trabectedin's known hepatic metabolism and myelosuppressive profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


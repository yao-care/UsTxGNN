---
layout: default
title: Alectinib
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Alectinib
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

# Alectinib: From ALK+ Non-Small-Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Alectinib is a second-generation, highly selective ALK (anaplastic lymphoma kinase) tyrosine kinase inhibitor, globally recognized as first-line standard of care for ALK-positive non-small-cell lung cancer (NSCLC), though it does not currently hold Taiwan regulatory approval.
The TxGNN model's top-ranked prediction is **Fibromatosis, Gingival**, with **0 clinical trials** and **0 publications** directly supporting this direction.
This top prediction is assessed as a likely false positive; the most clinically meaningful signal in this analysis is **Rank 7 (ALK+ Pulmonary Neuroendocrine Tumors)**, supported by 2 clinical trials and 16 publications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally approved for ALK+ NSCLC |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, Alectinib is a second-generation ALK tyrosine kinase inhibitor developed to overcome limitations of first-generation crizotinib, including poor CNS penetration and acquired resistance mutations. Its proven efficacy is rooted in inhibiting aberrant ALK kinase signaling driven by chromosomal rearrangements — primarily EML4-ALK fusions found in 3–5% of NSCLC patients.

**Assessment of the top prediction (Fibromatosis, Gingival):** Gingival fibromatosis is a benign fibrous proliferative disorder primarily caused by SOS1 gene mutations or drug-induced effects (e.g., phenytoin, calcium channel blockers). There is no established intersection between gingival fibromatosis pathogenesis and the ALK signaling pathway. Alectinib's selective ALK inhibition has no known biological rationale for this condition. The TxGNN prediction score of 99.97% most likely reflects graph-structural neighborhood similarity artifacts rather than a genuine biological signal — a pattern repeated across multiple Rank 1–6 predictions in this report.

**Important signal identified at Rank 7:** A systematic review of all 10 ranked predictions reveals that the only clinically meaningful repurposing signal is **Rank 7, labeled as "lung germ cell tumor" but actually representing ALK-rearranged pulmonary neuroendocrine tumors** (large cell neuroendocrine carcinoma, atypical carcinoid). Multiple published case reports document objective responses to alectinib in ALK+ LCNEC, and an active Phase 2/3 basket trial (DETERMINE, NCT05770037) is currently recruiting this patient population. This signal warrants separate reclassification as a "Research Question" candidate independent of the false-positive Rank 1 prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for fibromatosis, gingival.

---

> **Supplementary: Rank 7 — ALK+ Pulmonary Neuroendocrine Tumors (2 trials identified)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05770037](https://clinicaltrials.gov/study/NCT05770037) | Phase 2/3 | Recruiting | 30 | DETERMINE trial — UK national umbrella-basket platform trial evaluating alectinib in rare adult, paediatric, and TYA patients with ALK-positive cancers beyond approved lung cancer indications; primary data source for this repurposing signal |
| [NCT04644315](https://clinicaltrials.gov/study/NCT04644315) | Phase 2 | Terminated | 1 | Open-label single-arm study of alectinib in ALK+ locally-advanced or metastatic solid tumors (non-lung); terminated after enrolling only 1 patient — no usable efficacy data generated |

---

## Literature Evidence

Currently no related literature available for fibromatosis, gingival.

---

> **Supplementary: Rank 7 — ALK+ Pulmonary Neuroendocrine Tumors (top 10 of 16 publications)**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36690569](https://pubmed.ncbi.nlm.nih.gov/36690569/) | 2023 | Case Report | Clinical Lung Cancer | ALK+ pulmonary neuroendocrine tumor — documented favorable response to alectinib |
| [34994612](https://pubmed.ncbi.nlm.nih.gov/34994612/) | 2021 | Case Report | JCO Precision Oncology | Metastatic ALK fusion-positive large cell neuroendocrine lung carcinoma — partial response to alectinib |
| [35200571](https://pubmed.ncbi.nlm.nih.gov/35200571/) | 2022 | Case Report | Current Oncology | ALK-rearranged combined LCNEC + adenocarcinoma with diffuse bone metastasis — partial response to alectinib, exclusively ALK+ LCNEC component at recurrence |
| [29151522](https://pubmed.ncbi.nlm.nih.gov/29151522/) | 2018 | Case Report | Internal Medicine (Tokyo) | LCNEC with ALK rearrangement and liver/bone metastases — response to alectinib after cytotoxic chemotherapy failure |
| [37031440](https://pubmed.ncbi.nlm.nih.gov/37031440/) | 2023 | Case Report | Orvosi Hetilap | Mixed large cell neuroendocrine carcinoma with ALK fusion gene — alectinib as targeted alternative to cytostatic therapy |
| [31559892](https://pubmed.ncbi.nlm.nih.gov/31559892/) | 2020 | Case Report | Cancer Biology & Therapy | Primary pulmonary atypical carcinoid with EML4-ALK rearrangement — targeted therapy rationale for ALK+ carcinoid subtypes |
| [30591488](https://pubmed.ncbi.nlm.nih.gov/30591488/) | 2019 | Retrospective | Anticancer Research | Systematic ALK IHC screening in LCNEC series; identification of novel KIF5B-ALK fusion — supports routine ALK testing in neuroendocrine lung tumors |
| [39667359](https://pubmed.ncbi.nlm.nih.gov/39667359/) | 2024 | Case Report | Clinical Respiratory Journal | Novel CEP44-ALK fusion in metastatic neuroendocrine tumor — dramatic response to ALK-TKI (ensartinib); confirms ALK-TKI class efficacy including alectinib in ALK-rearranged NET |
| [37561984](https://pubmed.ncbi.nlm.nih.gov/37561984/) | 2023 | Review | JCO Precision Oncology | ALK inhibitors (including alectinib) for adult-onset neuroblastoma — therapeutic strategy review for ALK-driven rare neuroendocrine tumors |
| [36965191](https://pubmed.ncbi.nlm.nih.gov/36965191/) | 2023 | Case Report | Pediatric Blood & Cancer | Significant response to alectinib in pediatric spinal high-grade glioma with ALK fusion — demonstrates cross-tumor-type ALK inhibition potential |

---

## Taiwan Market Information

Alectinib is not currently registered in Taiwan (market status: 未上市). No Taiwan drug approval licenses are on record for this compound.

For global regulatory context: Alectinib (brand name Alecensa®) holds first-line NSCLC approvals in the United States (FDA), European Union, Japan, and multiple other jurisdictions, based on the landmark ALEX (global Phase 3), J-ALEX (Japan Phase 3), and ALESIA (Asia Phase 3) trials, as well as adjuvant NSCLC approval from the ALINA Phase 3 trial published in 2024.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation ALK tyrosine kinase inhibitor (small molecule, ATP-competitive) |
| Myelosuppression Risk | Low to moderate — anemia is the most commonly reported hematologic event, including rare hemolytic anemia (PMID 36604860); severe myelosuppression is uncommon compared to conventional cytotoxics |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (anemia), liver function tests (AST/ALT elevation reported), CPK (myalgia and rhabdomyolysis risk), renal function, ECG (bradycardia), and photosensitivity assessment |
| Handling Protection | Oral targeted therapy; standard institutional cytotoxic handling precautions apply per pharmacy SOPs |

---

## Safety Considerations

Please refer to the package insert for safety information.

> One published case report (PMID 36604860, 2023, *Journal of Oncology Pharmacy Practice*) specifically documents alectinib-induced hemolytic anemia — a rare but clinically significant adverse event — highlighting the importance of CBC monitoring even in the absence of expected myelosuppressive toxicity.

---

## Conclusion and Next Steps

**Decision: Hold** *(for Rank 1 — Fibromatosis, Gingival)*

**Rationale:**
The Rank 1 TxGNN prediction has no mechanistic basis (no ALK pathway involvement in gingival fibromatosis), zero supporting clinical trials, and zero supporting literature. The high prediction score (99.97%) is assessed as a graph-structural false positive. This decision applies equally to Ranks 2–4, 6, 8–10, which share the same pattern of absent evidence and absent ALK-pathway rationale.

**Separate action required for Rank 7 (ALK+ Pulmonary Neuroendocrine Tumors):**
This prediction should be reclassified and evaluated independently as a **Research Question** candidate. The mechanistic link is coherent (ALK rearrangement drives oncogenesis in a subset of LCNEC/atypical carcinoid), and objective clinical responses to alectinib in ALK+ LCNEC have been documented across multiple independent case reports.

**To pursue Rank 7 as a standalone repurposing candidate, the following is needed:**

- Obtain full mechanism of action data (DrugBank API query — DG002 remediation)
- Obtain Taiwan package insert warnings and contraindications (TFDA PDF — DG001 remediation)
- Monitor enrollment and interim results of DETERMINE trial (NCT05770037, expected completion Oct 2029)
- Define the eligible patient population: estimated ALK rearrangement frequency in LCNEC is 0.5–3% — prospective ALK IHC/FISH screening protocol needed
- Design a prospective case series or expanded access program for ALK+ LCNEC patients in Taiwan pending global trial data maturation
- Clarify Taiwan registration pathway for alectinib (currently 未上市) as a prerequisite for any repurposing clinical program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


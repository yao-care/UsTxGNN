---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 1025
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: From Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

> Pemetrexed (DB00642) is a multitargeted antifolate chemotherapy agent originally approved (as Alimta®) for pleural mesothelioma and non-small cell lung cancer.
> The TxGNN model predicts it may also be effective for **Malignant Peritoneal Mesothelioma**,
> with **11 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pleural Mesothelioma (with cisplatin) / Non-Small Cell Lung Cancer *(per evidence-pack mechanistic rationale; not separately confirmed by regulatory license data)* |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | Not Marketed (per current dataset — flagged for verification, see Next Steps) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for pemetrexed is not available from DrugBank in this evidence pack (data gap, severity: High). Based on the evidence pack's repurposing rationale, pemetrexed is known as a multitargeted antifolate that inhibits thymidylate synthase (TS), dihydrofolate reductase (DHFR), and glycinamide ribonucleotide formyltransferase (GARFT) — enzymes essential for folate-dependent DNA synthesis in rapidly dividing cells. This mechanism underlies its established, FDA-approved use in pleural mesothelioma (in combination with cisplatin).

Peritoneal mesothelioma and pleural mesothelioma belong to the same mesothelioma disease family, sharing identical histology and molecular biology and differing only in anatomical location (pleura vs. peritoneum). Because pemetrexed's antifolate mechanism suppresses tumor cell proliferation in a manner independent of anatomical site, its efficacy is expected to translate across both sites. Clinically, this extrapolation is already widespread: cisplatin-pemetrexed is commonly used off-label for peritoneal mesothelioma, and the NCCN guideline lists it as a treatment option. This makes the TxGNN prediction mechanistically well-supported and clinically plausible rather than speculative.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | First-line pemetrexed + gemcitabine, explicitly enrolling malignant pleural **and peritoneal** mesothelioma patients |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomized trial of neoadjuvant/palliative carboplatin+pemetrexed+bevacizumab ± atezolizumab specifically in peritoneal mesothelioma |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | Randomized comparison of intraperitoneal vs. IV chemotherapy (pemetrexed-containing) after CRS+HIPEC for peritoneal mesothelioma |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin + pemetrexed + imatinib safety/MTD study in unresectable or metastatic mesothelioma |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG20 + pemetrexed + cisplatin in arginine-requiring tumors, including a peritoneal mesothelioma dose-escalation cohort |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | Methoxyamine (TRC102) + pemetrexed/cisplatin in solid tumors and mesothelioma refractory to standard chemotherapy |
| [NCT03564691](https://clinicaltrials.gov/study/NCT03564691) | Phase 1 | Completed | 470 | Broad basket study of MK-4830 ± pembrolizumab in advanced solid tumors (mesothelioma-adjacent) |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Three-cohort maintenance talazoparib following first-line platinum chemo in pleural/peritoneal mesothelioma |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Sintilimab + bevacizumab + pemetrexed + cisplatin in unresectable peritoneal mesothelioma, biomarker exploration |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | MESOTIP trial: PIPAC + systemic chemo (cisplatin+pemetrexed) vs. systemic chemo alone as 1st-line for peritoneal mesothelioma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective study | Expert Rev Anticancer Ther | Retrospective evaluation of first-line pemetrexed + cisplatin efficacy specifically in MPeM |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective study | Jpn J Clin Oncol | Efficacy and safety of pemetrexed + cisplatin as first-line chemotherapy in advanced MPeM |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Comparative study | Clin Med Insights Oncol | Head-to-head comparison of pemetrexed-platinum vs. gemcitabine-platinum as first-line regimens in MPeM |
| [33743636](https://pubmed.ncbi.nlm.nih.gov/33743636/) | 2021 | Retrospective study | BMC Cancer | Second-line treatment efficacy and prognostic factors following first-line cisplatin+pemetrexed in MPeM |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multi-center study | Ann Surg Oncol | Demographic, clinicopathologic, and treatment outcome analysis across MPeM patients |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | J Gastrointest Oncol | Diagnosis and management overview of MPeM including chemotherapy role |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | Treatment review of MPeM patients including systemic chemotherapy options |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | General review of MPeM epidemiology, pathology, and treatment |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Case series | J Immunother | Chemoimmunotherapy in platinum-nonresponsive metastatic MPeM after prior pemetrexed-based regimens |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Rep | MPeM patient responding to rechallenge with cisplatin + pemetrexed, with literature review |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (multitargeted antifolate) |
| Myelosuppression Risk | High — neutropenia, thrombocytopenia, and anemia are well-documented with pemetrexed, particularly without vitamin B12/folic acid prophylaxis |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, renal function (creatinine clearance), vitamin B12/folate status, liver function |
| Handling Protection | Must follow standard cytotoxic drug handling regulations (hazardous drug precautions) |

*Note: Specific toxicity data was not available in the evidence pack (DrugBank MOA/toxicity data gap); the above reflects the established pharmacological class of pemetrexed. Please cross-check against the package insert.*

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in the current evidence pack (data gap DG001, severity: Blocking).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction (Malignant Peritoneal Mesothelioma) has L2-level evidence, including a Phase 2 completed trial with peritoneal mesothelioma patients explicitly enrolled (NCT00061477) and multiple ongoing Phase 2 trials designed specifically for this indication. The mechanistic rationale — extrapolation from the FDA-approved pleural mesothelioma indication to the same disease family at a different anatomical site — is strong and already reflected in NCCN guideline listing and off-label clinical practice.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank (currently blocking gap DG002)
- TFDA/FDA package insert data: key warnings, contraindications, and drug-drug interactions (currently blocking gap DG001)
- Verification of "Not Marketed" market status against known FDA approval history for pemetrexed (Alimta®) — this appears inconsistent with the drug's well-established regulatory record and should be re-checked at the data source
- Route compatibility data for the intraperitoneal chemotherapy protocols referenced in several trials (e.g., NCT06057935, NCT03875144)
- Subtype-specific evidence review, since other predicted indications in this pack (e.g., pleural sarcomatoid mesothelioma, pleural biphasic mesothelioma) show materially weaker chemotherapy response and warrant separate risk-benefit assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


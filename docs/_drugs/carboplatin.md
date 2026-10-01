---
layout: default
title: Carboplatin
parent: High Evidence (L1-L2)
nav_order: 497
evidence_level: L2
indication_count: 10
---

# Carboplatin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Carboplatin: From Platinum Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based cytotoxic chemotherapy marketed in the US as generic injectable products. The source data does not list its approved indications.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **a completed randomized Phase II trial, several Phase III trials, and multiple randomized publications** supporting this direction, especially in triple-negative and HER2-positive disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data (all US license records have empty indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five records reviewed are all generic ANDAs) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Based on general platinum pharmacology, carboplatin forms DNA crosslinks and adducts that block DNA replication and trigger cell death. This link is inferred rather than taken from a retrieved mechanism record.

Tumors with impaired homologous recombination, such as BRCA-related or triple-negative breast cancers, are less able to repair this damage. They are therefore plausibly more sensitive to carboplatin. The retrieved evidence is consistent with this. Randomized trials add carboplatin to neoadjuvant regimens in triple-negative and HER2-positive early breast cancer, and a carboplatin-olaparib trial targets BRCA-mutated disease.

Carboplatin is most often studied as part of a combination (with taxanes, anthracyclines, or HER2 antibodies). Its own contribution is therefore hard to isolate in many trials. The very high model score should be read as a reasonable hypothesis that already has clinical activity behind it, not as proof of standalone efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Randomized: neoadjuvant carboplatin + docetaxel vs carboplatin + paclitaxel, then doxorubicin/cyclophosphamide, in stage I-III triple-negative breast cancer. |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | Neoadjuvant weekly paclitaxel vs paclitaxel + carboplatin in large operable or locally advanced triple-negative breast cancer. |
| [NCT00532727](https://clinicaltrials.gov/study/NCT00532727) | Phase 3 | Unknown | 400 | Carboplatin vs docetaxel in metastatic or recurrent ER-/PR-/HER2- breast cancer. |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | Neoadjuvant docetaxel/carboplatin/trastuzumab/pertuzumab with or without estrogen deprivation in HR+/HER2+ disease. Carboplatin is a backbone, not the tested variable. |
| [NCT04159142](https://clinicaltrials.gov/study/NCT04159142) | Phase 2 | Recruiting | 414 | Nab-paclitaxel + carboplatin vs nab-paclitaxel + capecitabine in advanced triple-negative breast cancer. |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | Completed | 92 | Randomized: paclitaxel, carboplatin and trastuzumab as first-line therapy for HER2-overexpressing metastatic disease. |
| [NCT00232505](https://clinicaltrials.gov/study/NCT00232505) | Phase 2 | Completed | 112 | Cetuximab alone or with carboplatin in ER-/PR-/HER2-nonoverexpressing metastatic breast cancer. |
| [NCT00589238](https://clinicaltrials.gov/study/NCT00589238) | Phase 2 | Terminated | 16 | Randomized: neoadjuvant weekly paclitaxel ± carboplatin in basal-like breast cancer. Stopped early with very few patients. |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Carboplatin-olaparib followed by olaparib vs capecitabine in BRCA1/2-mutated, HER2-negative advanced disease. |
| [NCT02993094](https://clinicaltrials.gov/study/NCT02993094) | Phase 1/2 | Terminated | 31 | Ixazomib + carboplatin in pretreated advanced triple-negative breast cancer. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT (Phase 2) | Clin Cancer Res | NeoSTOP: compared anthracycline-free and anthracycline-containing neoadjuvant carboplatin regimens in stage I-III triple-negative breast cancer. |
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT (Phase 2) | Lancet Oncol | GeparSixto: tested adding carboplatin to neoadjuvant therapy in triple-negative and HER2-positive breast cancer. |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | RCT (Phase 3) | Eur J Cancer | BROCADE3 final overall survival: veliparib added to carboplatin/paclitaxel in BRCA-mutated advanced breast cancer. Carboplatin is the backbone. |
| [35462344](https://pubmed.ncbi.nlm.nih.gov/35462344/) | 2022 | Meta-analysis | Breast | Individual-patient and trial-level meta-analysis. The title states that adding carboplatin to neoadjuvant/adjuvant chemotherapy in triple-negative disease improves overall survival. |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | RCT (Phase 2) | Breast Cancer Res Treat | Single-agent carboplatin vs carboplatin + everolimus in advanced triple-negative breast cancer. |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief: camrelizumab vs placebo added to platinum-containing neoadjuvant chemotherapy in early or locally advanced triple-negative disease. |
| [40329228](https://pubmed.ncbi.nlm.nih.gov/40329228/) | 2025 | Real-world cohort | BMC Cancer | Multicenter analysis of carboplatin's effect on pathologic complete response and survival in HER2-low vs HER2-zero triple-negative disease. |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 trial | Breast Cancer Res | Carboplatin plus bevacizumab in breast cancer brain metastases (safety and efficacy). |
| [40468999](https://pubmed.ncbi.nlm.nih.gov/40468999/) | 2025 | Phase 2 trial | Acta Oncol | TCH vs TCHL neoadjuvant study in HER2-positive disease, with 5-year follow-up. |
| [35837812](https://pubmed.ncbi.nlm.nih.gov/35837812/) | 2023 | Retrospective | Cancer Med | Grade 3/4 anaemia, mainly carboplatin-induced, and pathologic complete response by carboplatin dose in neoadjuvant TCHP (294 patients). |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA208487 | Carboplatin (Ingenus Pharmaceuticals) | Injection, solution | Not listed in source data |
| ANDA207324 | Carboplatin (Gland Pharma) | Injection, solution | Not listed in source data |
| ANDA207324 | Carboplatin (BPI Labs) | Injection, solution | Not listed in source data |
| ANDA205487 | Carboplatin (Eugia US) | Injection, solution | Not listed in source data |
| ANDA077269 | Carboplatin (Teva Parenteral Medicines) | Injection, solution | Not listed in source data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum class) |
| Myelosuppression Risk | High. Myelosuppression, including anaemia, is a known dose-related toxicity, and the literature above reports frequent grade 3/4 anaemia in carboplatin combinations. |
| Emetogenicity Classification | Moderate to high, depending on dose |
| Monitoring Items | CBC with differential, renal function, liver function, electrolytes; hearing assessment at high doses (ototoxicity reported with high-dose carboplatin) |
| Handling Protection | Yes. Follow cytotoxic drug handling regulations. |

These ratings come from general drug-class knowledge, not from the source data. Please also refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed randomized Phase II trial, several randomized Phase II/III studies, and a meta-analysis support carboplatin in breast cancer, mainly triple-negative and HER2-positive disease. In many trials carboplatin is part of a combination, so its standalone effect is not isolated. Safety and mechanism records are missing from the pack, so this should proceed only with the guardrails below.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (the blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The approved indications for carboplatin, which are empty in the US license records
- Confirmed results from the Phase III trials NCT03168880 and NCT00532727 that isolate carboplatin's contribution
- A subtype-restricted scope (triple-negative, BRCA-mutated or HER2-positive) and a myelosuppression, renal and hearing monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


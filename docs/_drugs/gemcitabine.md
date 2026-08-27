---
layout: default
title: Gemcitabine
parent: 僅模型預測 (L5)
nav_order: 748
evidence_level: L5
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine: From Pancreatic Cancer to Female Breast Carcinoma

## One-Sentence Summary

Gemcitabine (DrugBank DB00441) is a nucleoside-analog cytotoxic chemotherapy long established in solid-tumor oncology, with pancreatic cancer as its best-known original indication.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, a prediction already reinforced by **50 clinical trials** and **20 publications** in this evidence pack, including a completed Phase 3 pivotal trial.
This is the strongest-evidenced candidate among the ten indications TxGNN surfaced for this drug — most of the others (rectal/colon/cervical/gallbladder/endometrial mucinous subtypes) have thin or no supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pancreatic cancer (well-established global indication; also NSCLC, ovarian, bladder). No Taiwan market license record found in this dataset. |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| US Market Status | Not marketed (per this dataset — 0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed formal MOA data for gemcitabine is flagged as a data gap in this evidence pack. However, the repurposing rationale captured alongside the top prediction provides a working mechanistic basis: gemcitabine is a deoxycytidine nucleoside analog that inhibits ribonucleotide reductase and incorporates into DNA to terminate replication — a broad-spectrum cytotoxic mechanism that is not tumor-type specific.

Because this mechanism targets rapidly dividing cells generally, its applicability is not confined to the tumor types it was first approved for. In breast cancer specifically, this is not a purely theoretical extrapolation: gemcitabine combinations (with paclitaxel, docetaxel, trastuzumab, capecitabine, carboplatin) have been studied extensively, including a completed Phase 3 randomized trial (NCT00006459, gemcitabine + paclitaxel vs. paclitaxel alone) and a large adjuvant Phase 3 study (NCT00093795, n=4,894) that included a gemcitabine-containing arm.

The combination of a non-selective cytotoxic mechanism with an already substantial, decades-long clinical trial record in breast cancer is what elevates this from a pure knowledge-graph inference (as seen in several of the other TxGNN-predicted indications for this drug) to a Level 1 evidence-supported hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | N/A | Randomized trial of gemcitabine + paclitaxel vs. paclitaxel alone in unresectable, locally recurrent, or metastatic breast cancer |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1206 | Neoadjuvant trial adding capecitabine or gemcitabine to docetaxel before AC ± bevacizumab in operable breast cancer; largest direct Phase 3 evidence, but current trial status needs verification |
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Phase 3 | Completed | 4894 | Large adjuvant trial in node-positive breast cancer comparing three regimens, one of which (dose-dense AC→paclitaxel+gemcitabine) includes gemcitabine |
| [NCT00193063](https://clinicaltrials.gov/study/NCT00193063) | Phase 2 | Completed | 41 | Weekly gemcitabine + trastuzumab in HER2-overexpressing metastatic breast cancer |
| [NCT00440622](https://clinicaltrials.gov/study/NCT00440622) | Phase 3 | Terminated | 90 | Randomized comparison of gemcitabine+Herceptin vs. capecitabine+Herceptin in pretreated HER2+ metastatic breast cancer |
| [NCT02252887](https://clinicaltrials.gov/study/NCT02252887) | Phase 2 | Completed | 45 | Gemcitabine + trastuzumab + pertuzumab in metastatic HER2+ breast cancer after prior HER2-targeted therapy |
| [NCT02139358](https://clinicaltrials.gov/study/NCT02139358) | Phase 1/2 | Completed | 15 | Gemcitabine + trastuzumab + pertuzumab in previously treated metastatic HER2+ breast cancer |
| [NCT01050322](https://clinicaltrials.gov/study/NCT01050322) | Phase 2 | Completed | 142 | Lapatinib combined with capecitabine, vinorelbine, or gemcitabine in HER2-amplified metastatic breast cancer after taxane progression |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Phase 2 | Completed | 50 | Weekly nab-paclitaxel + gemcitabine in metastatic breast cancer |
| [NCT01881230](https://clinicaltrials.gov/study/NCT01881230) | Phase 2/3 | Completed | 191 | Nab-paclitaxel + gemcitabine or carboplatin vs. gemcitabine+carboplatin as first-line therapy in triple-negative metastatic breast cancer |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase 1 | Breast Cancer Res Treat | Carboplatin + gemcitabine + mifepristone (GR antagonist) in advanced breast and recurrent/persistent ovarian cancer |
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase 1 | Gynecologic Oncology | Mirvetuximab soravtansine + gemcitabine in FRα-positive recurrent ovarian/endometrial cancer and triple-negative breast cancer |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review | Oncology (Williston Park) | Review of gemcitabine and platinum-based chemotherapy combinations in metastatic breast cancer |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | Review of gemcitabine + paclitaxel dosing schedules and response rates in metastatic breast cancer (52% ORR in pooled Phase 2 data) |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review | Oncology (Williston Park) | Review of gemcitabine/anthracycline/taxane combinations for advanced breast cancer |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Cohort | Tumori | Dose-finding study of docetaxel + gemcitabine in metastatic breast carcinoma |
| [12057039](https://pubmed.ncbi.nlm.nih.gov/12057039/) | 2002 | Preclinical | Clinical Breast Cancer | Preclinical study of gemcitabine + trastuzumab synergy in HER2-overexpressing breast and lung cancer cell lines |
| [21980041](https://pubmed.ncbi.nlm.nih.gov/21980041/) | 2011 | Pharmacogenetic study | Cancer Genomics & Proteomics | Gemcitabine/platinum pathway pharmacogenetics predicting hematologic toxicity in Asian breast cancer patients |
| [26372358](https://pubmed.ncbi.nlm.nih.gov/26372358/) | 2016 | Genomic study | Molecular Oncology | Machine-learning-derived genomic signatures for paclitaxel and gemcitabine resistance in breast cancer |
| [25398698](https://pubmed.ncbi.nlm.nih.gov/25398698/) | 2015 | Cohort | Cancer Chemother Pharmacol | Docetaxel + gemcitabine + bevacizumab as salvage chemotherapy for HER2-negative metastatic breast cancer |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — deoxycytidine nucleoside analog / antimetabolite (inhibits ribonucleotide reductase, incorporates into DNA to terminate replication) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (TFDA label data not available in this evidence pack — flagged as a blocking data gap) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Gemcitabine's use in breast cancer is backed by a completed Phase 3 RCT and a large Phase 3 adjuvant trial, plus a substantial body of Phase 1/2 combination trials with trastuzumab, taxanes, and platinum agents — this is L1-level evidence, not a purely model-derived hypothesis. However, the drug is not currently marketed in this jurisdiction, and TFDA label safety data is an explicit blocking gap, so guardrails are required before any clinical use decision.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed drug interaction (DDI) profile — current query returned "not found"
- Formal DrugBank-sourced MOA and toxicity data to replace the mechanistic-rationale text used here
- Verification of the current status of NCT00408408 (listed as "Unknown" despite being the largest direct Phase 3 trial)
- A regulatory pathway assessment given the drug's current non-marketed status in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


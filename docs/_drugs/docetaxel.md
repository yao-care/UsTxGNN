---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Cytotoxic Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel is a taxane-class antineoplastic (cytotoxic chemotherapy) agent used broadly across solid-tumor oncology; a documented original-indication record was not available for this product in the current evidence pack (Taiwan license and mechanism-of-action data are both flagged as gaps). The TxGNN model's top-ranked prediction — **Female Breast Carcinoma** — is supported by **50 clinical trials** and **20 publications**, though the evidence itself indicates this is already a globally established, approved use of docetaxel rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no Taiwan license record found in this evidence pack (see Data Gaps DG001/DG002) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed (0 licenses on record in this evidence pack) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The formal drug-level mechanism-of-action field for docetaxel is a documented data gap (DG002, High severity) in this evidence pack. However, the candidate-level analysis attached to this prediction does supply mechanistic detail: docetaxel is a taxane that binds and stabilizes microtubules, blocking their depolymerization. This arrests rapidly dividing cells — including breast cancer cells — in the G2/M phase of the cell cycle and induces apoptosis, consistent with well-established taxane pharmacology (cf. PMID 7595719, describing docetaxel as an "antineoplastic taxoid").

Because no Taiwan-approved indication was found on file (market status: Not Marketed, 0 licenses), a direct "original → new indication" comparison cannot be constructed from local regulatory records. Importantly, the evidence pack's own rationale for this candidate is explicit that female breast carcinoma is **not actually a novel finding**: docetaxel is already a globally approved, standard-of-care chemotherapy agent for breast cancer, which is precisely why the supporting literature base is so mature (multiple completed Phase 3 RCTs). In this instance, the TxGNN signal functions more as a confirmation of known pharmacology than as a genuine repurposing discovery.

Mechanistically, microtubule-stabilizing, cell-cycle-arrest cytotoxicity is broadly applicable to any rapidly proliferating solid tumor, which explains both the very high TxGNN score (99.90%) and the depth of independent clinical evidence — including at least three completed Phase 3 RCTs among the trials below — specifically supporting docetaxel-based regimens in breast carcinoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00841828](https://clinicaltrials.gov/study/NCT00841828) | Phase 2 | Completed | 102 | RCT comparing EC+Docetaxel+Trastuzumab vs. EC+Docetaxel+Lapatinib in HER2+ resectable/locally advanced breast cancer |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Neoadjuvant carboplatin+docetaxel vs. carboplatin+paclitaxel in Stage I-III triple-negative breast cancer |
| [NCT00941330](https://clinicaltrials.gov/study/NCT00941330) | Phase 2 | Completed | 31 | Pre-operative docetaxel-cyclophosphamide vs. exemestane in hormone receptor-positive breast cancer |
| [NCT03252431](https://clinicaltrials.gov/study/NCT03252431) | Phase 3 | Completed | 393 | F-627 vs. Neulasta for neutropenia prevention in docetaxel-based chemotherapy for Stage I-III breast cancer (confirms docetaxel as standard chemo backbone) |
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Phase 3 | Completed | 2,778 | Adjuvant Adriamycin/Taxotere vs. Adriamycin/Cytoxan in node-positive or high-risk node-negative breast cancer |
| [NCT00017095](https://clinicaltrials.gov/study/NCT00017095) | Phase 3 | Completed | 1,856 | Randomized taxane vs. non-taxane regimen with p53 predictive-value translational research in locally advanced/operable breast cancer |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1,206 | Neoadjuvant docetaxel ± capecitabine/gemcitabine ± bevacizumab before AC, evaluating pathologic complete response |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | 4-arm neoadjuvant study of Herceptin/docetaxel/pertuzumab combinations in HER2+ breast cancer |
| [NCT05189067](https://clinicaltrials.gov/study/NCT05189067) | Phase 2/3 | Unknown | 190 | Adjuvant paclitaxel+trastuzumab vs. docetaxel+trastuzumab in Stage I HER2+ breast cancer |
| [NCT00629278](https://clinicaltrials.gov/study/NCT00629278) (SHORT-HER) | Phase 3 | Unknown | 2,500 | Two adjuvant chemotherapy regimens plus 3 vs. 12 months trastuzumab in HER2+ breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT (ABC Trials) | J Clin Oncol | Docetaxel/cyclophosphamide (TC) vs. anthracycline-taxane regimens in early breast cancer adjuvant therapy |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Clinical Trial | Cancer | Capecitabine + docetaxel + epirubicin (TEX) as first-line therapy in advanced breast carcinoma |
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Review | The Oncologist | Review of docetaxel and paclitaxel roles across metastatic, adjuvant, and neoadjuvant breast cancer therapy |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Association between adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Foundational review of docetaxel's preclinical and clinical profile as an antineoplastic taxoid |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Review | Oncology (Williston Park) | Combination docetaxel/vinorelbine activity in metastatic breast cancer and NSCLC |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Dose-finding study | Tumori | Docetaxel + gemcitabine dose-finding study in anthracycline-pretreated metastatic breast carcinoma |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Clinical study | Breast Cancer (Tokyo) | Docetaxel, cyclophosphamide, and trastuzumab as neoadjuvant chemotherapy for HER2+ breast cancer |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 | Oncology | Weekly docetaxel + gemcitabine as first-line treatment for metastatic breast cancer |
| [15858439](https://pubmed.ncbi.nlm.nih.gov/15858439/) | 2005 | Phase 2 (interim) | Breast Cancer (Tokyo) | CEF followed by docetaxel as preoperative chemotherapy for early-stage breast carcinoma |

---

## US Market Information

No market authorization license was found for this product in the current evidence pack. The Taiwan regulatory query (`tfda`) executed successfully but returned zero license records (`total_licenses = 0`, `market_status = "Not Marketed"`). Consequently, no authorization number, product name, dosage form, or approved-indication text can be reported at this time; this should be confirmed directly against TFDA records before any market-facing decision is made.

---

## Cytotoxicity

Docetaxel is a taxane-class cytotoxic chemotherapy agent (criteria met: literature explicitly describes it as an "antineoplastic taxoid," and it belongs to the recognized taxane chemotherapy class).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane class — microtubule-stabilizing agent) |
| Myelosuppression Risk | High — the evidence base includes multiple trials specifically evaluating G-CSF/pegfilgrastim or biosimilar filgrastim support and neutropenic sepsis rates in docetaxel-treated patients (e.g., NCT03252431, retrospective UK sepsis review) |
| Emetogenicity Classification | Low to Moderate (typical of taxane-class agents) |
| Monitoring Items | CBC with differential (neutrophil count), liver function (docetaxel is predominantly hepatobiliary-excreted per PK literature in the pack), fluid retention/edema and lymphedema surveillance (per PMID 27997437), peripheral neuropathy assessment |
| Handling Protection | Must follow institutional cytotoxic/hazardous drug handling and disposal regulations |

Formal DrugBank toxicity monographs and the TFDA package insert were not retrieved in this evidence pack (see Data Gaps below); the items above are derived from the clinical trial and literature evidence on file. Please refer to the package insert warnings and precautions for complete prescribing information.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The evidence for docetaxel in female breast carcinoma is exceptionally mature (L1: multiple completed Phase 3 RCTs, 50 total trials, 20 publications), but per the evidence pack's own rationale this largely confirms an already globally approved, standard-of-care use rather than a novel repurposing signal.
- A drug-level **Blocking** data gap exists (DG001: TFDA package insert warnings/contraindications not retrieved) — per the evidence pack metadata, this gap by itself prevents the candidate from entering the S1 safety pre-screening stage, independent of how strong the efficacy evidence is for any single indication.

**To proceed, the following is needed:**
- Retrieve the TFDA package insert (warnings/contraindications) — Blocking gap (DG001)
- Retrieve a formal DrugBank mechanism-of-action record — High-priority gap (DG002)
- Directly confirm Taiwan market/license status, since this evidence pack found zero licenses on file
- Clarify why female breast carcinoma is being scored as a "predicted new indication" when the supporting rationale states it is already an approved standard use — this may warrant a candidate-selection/mapping review
- Consider follow-up on the other candidates in this multi-indication screen with genuinely off-label signal and moderate (L2) evidence: **Ewing sarcoma** (rank 2, GEMDOX-type docetaxel+gemcitabine regimens) and **rhabdomyosarcoma** (rank 8, similar sarcoma salvage regimens)
- Manually re-verify the disease-label mapping for **small cell lung carcinoma** (rank 4) and **primary pulmonary lymphoma** (rank 5) — the cited trials/literature for both predominantly concern NSCLC/ALK-positive lung cancer rather than the labeled disease, per data-quality flags already noted in the evidence pack itself
- Treat the remaining low-evidence candidates (well-differentiated fetal adenocarcinoma of the lung, botryoid-type embryonal rhabdomyosarcoma of the vagina, pulmonary blastoma, embryonal extrahepatic bile duct rhabdomyosarcoma, parameningeal embryonal rhabdomyosarcoma — all L4/L5, decision "Hold") as research hypotheses only, not near-term candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


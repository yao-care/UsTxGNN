---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 497
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# CARBOPLATIN: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based alkylating chemotherapy agent, most widely recognized as a first-line treatment backbone for ovarian cancer and other platinum-sensitive malignancies.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**—especially triple-negative (TNBC) and BRCA-mutated subtypes—
with **50 clinical trials** and **20 publications** retrieved in support of this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current regulatory database |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| US Market Status | Not found in regulatory database (likely a data gap) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query in this evidence pack. Based on established pharmacology, carboplatin is a second-generation platinum coordination compound that forms covalent DNA adducts—primarily intrastrand (Pt-GG) and interstrand cross-links—blocking DNA replication and transcription. Cells with impaired DNA repair mechanisms accumulate lethal damage and are driven toward apoptosis.

Triple-negative breast cancer (TNBC) and BRCA1/2-mutated breast cancers harbor homologous recombination deficiency (HRD), rendering them exquisitely sensitive to DNA cross-linking agents such as carboplatin. When homologous recombination cannot repair double-strand breaks, tumor cells cannot recover from carboplatin-induced damage. This rationale is supported by GeparSixto (Lancet Oncol, 2014), a landmark randomized Phase 2 trial demonstrating that carboplatin significantly improved pathological complete response (pCR) in TNBC (53.2% vs. 36.9%). A 2022 individual participant data meta-analysis (PMID 35462344) further confirmed that adding carboplatin to neoadjuvant/adjuvant chemotherapy improves overall survival in TNBC.

For HER2-positive breast cancer, carboplatin combined with trastuzumab and pertuzumab (the TCHP regimen) demonstrates synergistic anti-tumor activity, with a completed Phase 3 trial (NCT02003209, n=315) specifically evaluating this approach. An ongoing Phase 3 TNBC trial (NCT03168880, n=720) and an additional recruiting study (NCT04159142, n=414) are expected to further consolidate the evidence base and may ultimately upgrade the evidence level to L1.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, Not Recruiting | 720 | RCT comparing weekly paclitaxel alone vs. weekly paclitaxel + carboplatin as neoadjuvant therapy in patients with large operable or locally advanced TNBC |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | RCT evaluating TCHP (docetaxel + carboplatin + trastuzumab + pertuzumab) ± estrogen deprivation in HR+/HER2+ locally advanced breast cancer; primary endpoint: pCR rate |
| [NCT00532727](https://clinicaltrials.gov/study/NCT00532727) | Phase 3 | Unknown | 400 | RCT directly comparing carboplatin vs. docetaxel as standard of care for metastatic or recurrent TNBC |
| [NCT04159142](https://clinicaltrials.gov/study/NCT04159142) | Phase 2 | Recruiting | 414 | Multicenter RCT comparing nab-paclitaxel + carboplatin vs. nab-paclitaxel + capecitabine in advanced TNBC |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Randomized Phase 2 evaluating carboplatin + docetaxel vs. carboplatin + paclitaxel as neoadjuvant therapy in Stage I–III TNBC |
| [NCT00232505](https://clinicaltrials.gov/study/NCT00232505) | Phase 2 | Completed | 112 | Randomized Phase 2 comparing cetuximab alone vs. cetuximab + carboplatin in metastatic ER−/PR−/HER2− breast cancer |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | Completed | 92 | Randomized Phase 2 of paclitaxel + carboplatin + trastuzumab as first-line therapy in HER2-overexpressing metastatic breast cancer |
| [NCT00005963](https://clinicaltrials.gov/study/NCT00005963) | Phase 2 | Completed | 53 | Phase 2 study of docetaxel + carboplatin as first-line chemotherapy for metastatic breast cancer |
| [NCT07103447](https://clinicaltrials.gov/study/NCT07103447) | Phase 2 | Not Yet Recruiting | 54 | Prospective multicenter study of AK112 (bispecific anti-PD-1/VEGF antibody) + albumin-bound paclitaxel + carboplatin as neoadjuvant therapy for TNBC |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Dose-finding study of carboplatin + olaparib (PARP inhibitor) in BRCA1/2-mutated, HER2-negative advanced breast cancer; explores platinum–PARP inhibitor synergy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT | Clin Cancer Res | NeoSTOP: Randomized Phase 2 comparing anthracycline-free (carboplatin + taxane) vs. anthracycline-containing carboplatin regimen in Stage I–III TNBC; evaluates pCR across both arms |
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT | Lancet Oncol | GeparSixto: Addition of carboplatin to neoadjuvant therapy significantly improved pCR in TNBC (53.2% vs. 36.9%; p=0.005); landmark evidence establishing carboplatin's role in TNBC |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief: Phase 3 RCT showing camrelizumab (anti-PD-1) combined with platinum-containing neoadjuvant chemotherapy improves outcomes in early/locally advanced TNBC |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT | Nat Commun | MUKDEN 06: ARX788 (anti-HER2 ADC) + pyrotinib vs. TCbHP (docetaxel + carboplatin + trastuzumab + pertuzumab) in neoadjuvant HER2+ breast cancer; establishes TCbHP as the standard comparator |
| [40468999](https://pubmed.ncbi.nlm.nih.gov/40468999/) | 2025 | RCT | Acta Oncol | TCHL 5-year follow-up: TCH (docetaxel + carboplatin + trastuzumab) vs. TCHL in HER2+ neoadjuvant breast cancer with long-term efficacy and serum biomarker analysis |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | RCT | Eur J Cancer | BROCADE3 final OS results: Adding veliparib to carboplatin + paclitaxel significantly improved PFS in germline BRCA1/2-mutated, HER2-negative advanced breast cancer |
| [35462344](https://pubmed.ncbi.nlm.nih.gov/35462344/) | 2022 | Meta-analysis | Breast | Individual participant data meta-analysis confirming carboplatin addition to neoadjuvant/adjuvant chemotherapy improves overall survival in TNBC |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | RCT | Breast Cancer Res Treat | Randomized Phase 2 comparing single-agent carboplatin vs. carboplatin + everolimus (mTOR inhibitor) in advanced TNBC; investigates mTOR pathway-mediated platinum sensitization |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 | Breast Cancer Res | Phase 2 study of bevacizumab + carboplatin in breast cancer brain metastases; assessed intracranial response rate and safety |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | Comprehensive review of preclinical and clinical evidence for paclitaxel-carboplatin synergy, efficacy, and safety in advanced breast cancer |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Platinum-based alkylating agent) |
| Myelosuppression Risk | High — thrombocytopenia is the dose-limiting toxicity; neutropenia and anemia are also common at therapeutic doses |
| Emetogenicity Classification | Moderate to High (moderately emetogenic at standard doses; highly emetogenic at high doses used in stem-cell transplant conditioning) |
| Monitoring Items | CBC with differential and platelet count before each cycle; serum creatinine and estimated creatinine clearance for Calvert formula dose calculation; audiometry if high-dose regimen; electrolytes (Ca²⁺, Mg²⁺, K⁺) |
| Handling Protection | Must follow cytotoxic drug handling regulations; prepare in a biological safety cabinet with closed-system transfer devices; appropriate PPE required throughout preparation and administration |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomized Phase 2 and Phase 3 clinical trials, alongside a meta-analysis confirming overall survival benefit, establish carboplatin as a well-supported therapy for female breast carcinoma—particularly TNBC (driven by HRD/BRCA-mediated platinum sensitivity) and HER2-positive subtypes (TCH/TCHP regimens). The mechanistic and clinical evidence base is robust, and carboplatin is already embedded in internationally recognized breast cancer protocols.

**To proceed, the following is needed:**
- Verification of US FDA regulatory approval status — the current database shows 0 registered NDAs, which almost certainly reflects a data gap rather than absence of approval
- Detailed mechanism of action (MOA) data from DrugBank API (currently missing from this evidence pack)
- Patient stratification plan by breast cancer subtype: prioritize TNBC with confirmed HRD/BRCA mutation and HER2-positive disease for the strongest benefit-risk profile
- Safety monitoring protocol addressing thrombocytopenia (dose-limiting), renal function surveillance for Calvert formula dosing, and audiometry for high-dose regimens
- Tracking of results from ongoing Phase 3 trials (NCT03168880, n=720 and NCT04159142, n=414), whose completion is expected to upgrade the evidence level from L2 to L1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


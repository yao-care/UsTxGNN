---
layout: default
title: Hydroxyurea
parent: 僅模型預測 (L5)
nav_order: 781
evidence_level: L5
indication_count: 10
---

# Hydroxyurea
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

# Hydroxyurea: From Undocumented Original Indication to Female Breast Carcinoma

## One-Sentence Summary

Hydroxyurea (DrugBank DB01005) is a ribonucleotide reductase inhibitor and broad-spectrum cytotoxic/antimetabolite agent; the evidence pack does not record its original approved indication or formal DrugBank MOA text (data gaps). The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, supported currently by **0 registered clinical trials** and **20 publications**, most of which are preclinical or early-phase combination-regimen studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, formal DrugBank-style mechanism-of-action text and the drug's original approved indication are not available in this evidence pack (flagged as data gaps DG001/DG002). Based on the literature collected for this candidate, hydroxyurea is a ribonucleotide reductase (RNR) inhibitor — a broad-spectrum cytotoxic/antimetabolite agent that has historically been used as a component of combination chemotherapy regimens across multiple solid tumors, including breast cancer (e.g., PMID 26844848 describes it as "an antineoplastic drug used for the treatment of leukemia, sickle-cell disease, HIV, psoriasis, thrombocythemia, and various neoplastic diseases").

Because the evidence pack contains no record of hydroxyurea's original indication, the relationship between "original use" and "predicted new indication" cannot be characterized directly. What can be assessed is the mechanistic plausibility: RNR inhibition blocks DNA synthesis in rapidly proliferating cells, a mechanism not tissue-specific and therefore theoretically applicable to breast tumor cells as it is to other malignancies.

The literature evidence in this pack largely supports this at a mechanistic/exploratory level — preclinical studies on HU-lipid conjugates, RNR-inhibitor DNA-repair sensitization, and early-phase (Phase I/Phase I-II) combination regimens including hydroxyurea in breast cancer — but there is no modern, breast-cancer-specific randomized controlled trial. The mechanism is reasonable, but specificity and confirmatory clinical evidence for this indication are currently insufficient.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Phase I/II trial | Bone Marrow Transplantation | High-dose cyclophosphamide + thiotepa + hydroxyurea with autologous stem cell rescue as consolidation chemotherapy in 26 women with responding metastatic breast cancer |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I trial | American Journal of Clinical Oncology | Sequential 5-FU/leucovorin followed by hydroxyurea with allopurinol protection (HALF regimen) in 20 patients with advanced GI and breast cancer |
| [33631478](https://pubmed.ncbi.nlm.nih.gov/33631478/) | 2021 | Review | Pathology, Research and Practice | Review of long non-coding RNAs in breast cancer pathogenesis, prognosis, and clinical course (contextual, not HU-specific) |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | Preclinical | Drug Research | In-silico design of novel hydroxyurea-lipid drug conjugates targeting the PI3K/AKT/mTOR pathway to improve HU lipophilicity and reduce toxicity in breast cancer therapy |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | Preclinical | Molecular Cancer | Characterizes EYA4's role in breast cancer progression and metastasis via replication stress avoidance |
| [30692636](https://pubmed.ncbi.nlm.nih.gov/30692636/) | 2019 | Preclinical | Oncogene | Nucleostemin's role in genome maintenance and mammary tumor progression; DNA damage susceptibility in tumor cells |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | 2-hexyl-4-pentynoic acid sensitizes breast tumor cells to hydroxyurea via RPA2 hyperphosphorylation-mediated DNA repair modulation |
| [26844848](https://pubmed.ncbi.nlm.nih.gov/26844848/) | 2016 | Preclinical | Cancer Biotherapy & Radiopharmaceuticals | Radiolabeling and evaluation of [99mTc(CO)3]+-hydroxyurea and FITC-hydroxyurea as imaging/tracking agents |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | Preclinical | Molecular Pharmacology | Novel RNR inhibitor COH29 inhibits DNA repair in vitro; hydroxyurea referenced as an established clinical RNR-targeting agent, tested in BRCA1-defective breast cancer cells |
| [27504932](https://pubmed.ncbi.nlm.nih.gov/27504932/) | 2017 | Preclinical | Journal of Cellular Physiology | Chemoresistance characterization of lung (H460) and breast (MCF-7) cancer cells under prolonged serum starvation |

---

## US Market Information

Hydroxyurea currently has no marketing authorization on record in this evidence pack's regulatory dataset (0 licenses; market status: **Not Marketed**).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (ribonucleotide reductase inhibitor / antimetabolite class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Evidence for the breast carcinoma indication is Level L3 — literature is dominated by preclinical mechanistic studies and small Phase I/I-II combination-regimen trials from the 1990s, with no registered clinical trials and no modern controlled study specific to breast cancer. A blocking data gap (TFDA label/warnings, DG001) also prevents safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) to unblock safety evaluation (DG001)
- Formal MOA documentation via DrugBank API (DG002)
- Confirmation of hydroxyurea's original approved indication(s), currently undocumented in this evidence pack
- A modern, breast-cancer-specific controlled trial to validate the mechanistic hypothesis before advancing beyond the research-question stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


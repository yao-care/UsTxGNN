---
layout: default
title: Dasatinib
parent: Model Prediction Only (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
---

# Dasatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Dasatinib: From Chronic Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is an oral multi-kinase inhibitor, marketed for chronic myeloid leukemia (CML) and Philadelphia chromosome-positive acute lymphoblastic leukemia (Ph+ ALL).
The TxGNN model predicts it may be effective for **Ewing sarcoma**, but only **3 clinical trials** (2 actually testing dasatinib) and **8 publications** were retrieved. Most of the publications are preclinical, and the one phase 2 trial that included Ewing patients reportedly showed no single-agent benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CML and Ph+ ALL (from literature and the mechanistic rationale; label text is not in the Evidence Pack) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 (as assigned in the Evidence Pack; the supporting phase 2 trial is non-randomized, so the real strength is weaker) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (including generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dasatinib inhibits BCR-ABL, SRC-family kinases, KIT and PDGFR. BCR-ABL inhibition explains its use in CML. Detailed mechanism-of-action data from DrugBank were not available in the Evidence Pack, so this description comes from the pack's mechanistic rationale and the literature.

The link to Ewing sarcoma runs through SRC and FAK signaling. Preclinical studies show that SRC drives invadopodia formation, migration and invasion in Ewing sarcoma cells. Dasatinib showed antiproliferative and antimigratory activity in Ewing sarcoma and neuroblastoma cell lines, and induced apoptosis in bone sarcoma cells that depend on SRC. The mechanism is plausible, but it is mostly cell-line evidence.

A 2022 review reports that single-agent dasatinib was tested in a phase 2 study of advanced sarcomas including Ewing sarcoma, and that it **failed as a single agent in these subtypes**. This is the most important caution for this candidate. Clinical benefit is unconfirmed, and any future path would probably need a combination strategy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Dasatinib in advanced sarcomas, measuring response rate and 6-month progression-free survival. Non-randomized and sarcoma-wide, so Ewing-specific results must be checked in the results record. |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Pediatric trial of dasatinib with ifosfamide, carboplatin and etoposide. Terminated with only 7 patients, so it says little about efficacy. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | B7-H3 CAR-T cells in children and young adults with relapsed solid tumors. Dasatinib is not the studied drug, so this is not evidence for dasatinib. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Review | Sarcoma | Targeting FAK-Src in DSRCT, Ewing sarcoma and rhabdomyosarcoma. Reports that single-agent dasatinib failed in the phase 2 sarcoma study. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncol Lett | Src signaling in sarcoma. Discusses Src as a potential drug target. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical | Oncol Rep | Dasatinib had antiproliferative and antimigratory activity in neuroblastoma and Ewing sarcoma cell lines. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical | Cancer Res | Dasatinib inhibited migration and invasion in sarcoma cell lines and induced apoptosis in SRC-dependent bone sarcoma cells. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical | Neoplasia | Tenascin C and Src cooperate to promote invadopodia formation in Ewing sarcoma. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical | Neoplasia | Microenvironmental stress activates Src-dependent invadopodia and migration in Ewing sarcoma. |

Three other retrieved items are not dasatinib evidence for Ewing sarcoma and are not counted:
- PMID 35190971 (chondrosarcoma review)
- PMID 29776413 (plerixafor in Ewing cell lines)
- PMID 32999666 (CML case report)

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021986 | SPRYCEL | Tablet | E.R. Squibb & Sons, L.L.C. |
| ANDA216261 | Dasatinib | Tablet, film coated | Alembic Pharmaceuticals Limited |
| ANDA213383 | Dasatinib | Tablet, film coated | Dr. Reddy's Laboratories Inc |
| ANDA217217 | Dasatinib | Tablet, film coated | BluePoint Laboratories |
| ANDA211094 | Dasatinib | Tablet, film coated | AvKARE |

Approved-indication text was not available for these authorizations. All listed products are oral tablets.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Literature-reported adverse events (in CML patients):** pleural effusion, chylothorax and interstitial pneumonitis (PMIDs 36448074, 36346055, 36763239 context aside, 35916333), and skin and soft tissue infections in adolescents (PMID 35441424).

Please refer to the package insert for warnings, contraindications and drug interactions. These were not available in the Evidence Pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ewing sarcoma has a very high model score, but the clinical evidence is thin and discouraging. The only completed dasatinib trial is a non-randomized, sarcoma-wide phase 2 study, and a review reports single-agent failure in Ewing sarcoma. The rest of the support is preclinical SRC biology. It stays a research question, not a development candidate, until combination evidence appears.

**To proceed, the following is needed:**
- Ewing-specific response and progression-free survival results from NCT00464620's results record
- Preclinical or clinical evidence for dasatinib combinations in Ewing sarcoma
- The US package insert warnings and contraindications (blocking data gap)
- DrugBank mechanism-of-action data and original indication text

**Other predictions:** Among the other nine predictions, myeloid leukemia (L1) is an on-label use of dasatinib, not a true repurposing case. Liposarcoma (L3) has only preclinical SRC rationale and the same sarcoma-wide trial. The remaining seven are at L4-L5 with no dasatinib-specific evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


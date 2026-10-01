---
layout: default
title: Pemetrexed
parent: Model Prediction Only (L5)
nav_order: 1025
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: From Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed is a multitargeted antifolate chemotherapy. It is best known for pleural mesothelioma and non-squamous lung cancer, although the US label text in the input is empty.
The TxGNN model predicts it may be effective for **malignant peritoneal mesothelioma**.
Currently **10 listed clinical trials** (all Phase 1/2, none with a Phase 3 peritoneal-specific readout) and **20 publications** (mostly reviews, retrospective series and case reports) support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the US license text (empty); pleural mesothelioma and non-squamous NSCLC inferred from trial records |
| Predicted New Indication | Malignant peritoneal mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (per Evidence Pack scoring; no peritoneal-specific Phase 3) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, pemetrexed is a multitargeted antifolate that inhibits thymidylate synthase (TS), dihydrofolate reductase (DHFR) and glycinamide ribonucleotide formyltransferase (GARFT). This blocks thymidine and purine synthesis in rapidly dividing tumour cells.

Peritoneal and pleural mesothelioma share histology and biology. Pemetrexed plus cisplatin is the established first-line standard for pleural disease, supported by a Phase 3 RCT showing a survival benefit over cisplatin alone (PMID 12860938). In peritoneal disease, pemetrexed-platinum is used by extension. Japanese retrospective series describe it as the usual first-line systemic regimen, though no standard systemic chemotherapy has been formally established for the peritoneal site.

The evidence is Phase 2 and extrapolated from pleural disease. Surgery with hyperthermic intraperitoneal chemotherapy (CRS + HIPEC) remains the preferred treatment for patients suitable for it. Pemetrexed-based systemic therapy mainly applies to advanced or unresectable disease.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | ICARuS II: randomized comparison of intraperitoneal vs intravenous chemotherapy after cytoreductive surgery and HIPEC; pemetrexed is one component |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Front-line pemetrexed plus gemcitabine in pleural or peritoneal mesothelioma; covers the peritoneal site directly |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomized: carboplatin-pemetrexed-bevacizumab with or without atezolizumab; pemetrexed's contribution cannot be isolated |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Single-arm sintilimab + bevacizumab + pemetrexed-cisplatin in unresectable disease; pemetrexed is backbone therapy |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | MESOTIP: PIPAC plus systemic cisplatin-pemetrexed vs systemic chemotherapy alone, first-line |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | TRC102 (methoxyamine) with cisplatin-pemetrexed in advanced solid tumours or mesothelioma |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 with pemetrexed-cisplatin; mixed tumour types, peritoneal mesothelioma in dose escalation only |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | Vorinostat with pemetrexed-cisplatin (pleural); no participants, no data |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin, pemetrexed and imatinib; maximum tolerated dose in metastatic malignant mesothelioma |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Talazoparib maintenance after platinum-based chemotherapy in pleural or peritoneal mesothelioma |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Clinical study | Jpn J Clin Oncol | Efficacy and safety of first-line pemetrexed plus cisplatin in advanced peritoneal mesothelioma |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective | Expert Rev Anticancer Ther | First-line pemetrexed-cisplatin efficacy in peritoneal mesothelioma |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Comparative study | Clin Med Insights Oncol | Compares first-line pemetrexed-platinum vs gemcitabine-platinum; pemetrexed-platinum is the most-used first-line option |
| [33743636](https://pubmed.ncbi.nlm.nih.gov/33743636/) | 2021 | Retrospective | BMC Cancer | Second-line treatment efficacy and prognostic factors, following first-line cisplatin-pemetrexed |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Cohort | Ann Surg Oncol | Multi-center analysis of treatment strategies and outcomes in peritoneal mesothelioma |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | Treatment overview: cytoreduction plus HIPEC is the preferred initial treatment in selected patients |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Review | Cancers | Diagnostic and therapeutic pathway; median OS 34–92 months with CRS + HIPEC |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | Review of a very rare malignancy with poor prognosis |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Rep | Patient responded to cisplatin-pemetrexed and again on rechallenge after progression |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Case series | J Immunother | Two platinum-nonresponsive patients treated with chemotherapy plus immune checkpoint inhibitors |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA210661 | Pemetrexed dipotassium; AXTLE | Lyophilized powder for injection | Avyxa Pharma, LLC |
| NDA208419 | Pemetrexed | Solution, concentrate | Teva Pharmaceuticals, Inc. |

The Evidence Pack reports 7 licenses in total. The 5 entries listed are consolidated above into these 2 NDAs. Approved indication text was not provided for any of them.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (multitargeted antifolate antimetabolite) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pemetrexed-platinum is the standard first-line regimen for pleural mesothelioma (Phase 3 evidence), and peritoneal mesothelioma is biologically close to it. Several Phase 2 trials are ongoing and retrospective series support activity. However, no Phase 3 exists for the peritoneal site, the trials cannot isolate pemetrexed's contribution, and the safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap DG001), obtained from the FDA labels; safety screening cannot proceed without them
- Mechanism of action data from DrugBank (gap DG002)
- Original approved indication text, since the license entries are empty
- Results from the peritoneal-specific randomized trials (NCT06057935, NCT05001880, NCT03875144)
- Patient selection criteria separating candidates for CRS + HIPEC from those for systemic therapy

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


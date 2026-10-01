---
layout: default
title: Pralatrexate
parent: Model Prediction Only (L5)
nav_order: 1073
evidence_level: L5
indication_count: 10
---

# Pralatrexate
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

# Pralatrexate: From Peripheral T-Cell Lymphoma to Pleural Adenomatoid Tumor

## One-Sentence Summary

Pralatrexate is an injectable antifolate chemotherapy, marketed in the US and, per its public labeling, used for relapsed or refractory peripheral T-cell lymphoma. The TxGNN model's top-ranked prediction is **pleural adenomatoid tumor**, but it has **0 clinical trials** and **0 publications** behind it, and the model's own rationale suggests the score reflects graph proximity to mesothelioma rather than a real therapeutic signal. Among the model's other predictions, only **pleural mesothelioma** has meaningful support, with **1 Phase II trial** and **2 other publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peripheral T-cell lymphoma (from public labeling; the license records in the Evidence Pack have blank indication text) |
| Predicted New Indication | Pleural adenomatoid tumor |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 license records (NDA022468 and ANDA206183) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Pralatrexate is a folate analog that inhibits dihydrofolate reductase (DHFR) and is preferentially taken up into cells through the reduced folate carrier RFC-1. It is more potent than methotrexate, and its main toxicities are mucositis and myelosuppression.

For the top prediction, the case is weak. Adenomatoid tumors are typically benign mesothelial lesions, so a cytotoxic antifolate is unlikely to offer a favorable risk-benefit balance. The high score most likely comes from the drug's proximity to mesothelioma nodes in the knowledge graph.

The mesothelioma family is a different matter. Mesothelioma is a known antifolate-responsive cancer, since pemetrexed is standard therapy. This makes the mesothelioma-related predictions biologically plausible, and pleural mesothelioma is the strongest of them (see the section on other predictions below).

## Clinical Trial Evidence

Currently no related clinical trials registered for pleural adenomatoid tumor.

## Literature Evidence

Currently no related literature available for pleural adenomatoid tumor.

## US Market Information

The Evidence Pack lists 6 license records. Repeated entries are merged below. None of them include indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206183 | Pralatrexate (Dr. Reddy's Laboratories Inc.) | Injection | Not listed in source data |
| NDA022468 | Pralatrexate (Fresenius Kabi USA, LLC) | Injection | Not listed in source data |
| NDA022468 | Folotyn (Acrotech Biopharma Inc) | Injection | Not listed in source data |

## Cytotoxicity

The Evidence Pack has no toxicity data. The entries below come from general knowledge of the drug class and should be checked against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate, DHFR inhibitor) |
| Myelosuppression Risk | Medium to high (thrombocytopenia, neutropenia and anemia are expected) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, mucositis assessment, liver and renal function |
| Handling Protection | Yes. Follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were retrieved, and the DDI query returned no results. The Evidence Pack's rationale notes significant mucositis and myelosuppression for this drug.

## Other Predicted Indications

The top 10 predictions are almost all mesothelioma-related. Only two have any supporting literature.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 1 | Pleural adenomatoid tumor | 99.91% | L5 | Benign lesion. Cytotoxic therapy is unlikely to be justified |
| 2 | Relapsing-remitting multiple sclerosis | 99.91% | L5 | Only a generic antifolate immunomodulation link. No MS data, and toxicity is significant |
| 3 | Pleural biphasic mesothelioma | 99.90% | L5 | No subtype data. Sarcomatoid component tends to respond poorly |
| 4 | Pleural epithelioid mesothelioma | 99.89% | L3 | Most plausible subtype, backed by 1 Phase II trial. Subtype-specific results not confirmed |
| 5 | Lymphohistiocytoid mesothelioma | 99.89% | L5 | Rare variant with no specific evidence |
| 6 | Pericardium cancer | 99.89% | L5 | Extrapolation from pleural data is speculative |
| 7 | Pleural sarcomatoid mesothelioma | 99.89% | L5 | Typically chemoresistant |
| 8 | Malignant peritoneal mesothelioma | 99.87% | L5 | Only weak indirect support |
| 9 | Well differentiated papillary mesothelioma | 99.85% | L5 | Usually indolent, so systemic chemotherapy is rarely warranted |
| 10 | Pleural mesothelioma | 99.85% | L2 (loosely) | Best-supported prediction. Recommendation: Research Question |

### Best-Supported Candidate: Pleural Mesothelioma

There are no registered clinical trials in the dataset. Literature:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17409804](https://pubmed.ncbi.nlm.nih.gov/17409804/) | 2007 | Phase II (single-arm) | J Thorac Oncol | Trial of pralatrexate in unresectable malignant pleural mesothelioma. The abstract describes stomatitis as the main toxicity. Efficacy outcomes were not in the provided data |
| [11595715](https://pubmed.ncbi.nlm.nih.gov/11595715/) | 2001 | Preclinical | Clin Cancer Res | Pralatrexate was about 25-30-fold more cytotoxic than methotrexate in mesothelioma cell lines. Combination with platinums was also evaluated |
| [21301589](https://pubmed.ncbi.nlm.nih.gov/21301589/) | 2010 | Review | Cancer Manag Res | Overview of antifolates that target folic acid synthesis in cancer chemotherapy |

The L2 label from the Evidence Pack fits only loosely. The Phase II study was single-arm and not randomized, so it does not meet the strict L2 definition of a randomized trial.

## Conclusion and Next Steps

**Decision: Hold** (for pleural adenomatoid tumor; pleural mesothelioma is flagged as a Research Question)

**Rationale:**
The top-ranked prediction has no clinical or literature support, and it involves a benign lesion for which a toxic cytotoxic drug is a poor fit. The mesothelioma family is biologically plausible, and pleural mesothelioma is the only prediction with a Phase II study behind it.

**To proceed, the following is needed:**
- The full package insert with warnings and contraindications. This is a blocking gap for safety screening.
- Detailed mechanism of action data from DrugBank.
- The efficacy and safety outcomes of the 2007 Phase II study (PMID 17409804), including any epithelioid-specific results.
- A search of clinical trial registries for pralatrexate in mesothelioma, since none were found in the dataset.
- A decision to shift the focus from the top-ranked prediction to pleural mesothelioma.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


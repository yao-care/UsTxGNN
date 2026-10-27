---
layout: default
title: Pazopanib
parent: Model Prediction Only (L5)
nav_order: 1018
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pazopanib: predicted new indication Top-ranked: renal cell carcinoma associated with Xp11.2 translocation… (evidence level L5). Approved use: Renal cell carcinoma and soft tissue sarcoma"
monitor_inn: "PAZOPANIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "heart fibrosarcoma", "fibroblastic neoplasm", "kidney fibrosarcoma", "dermatofibrosarcoma protuberans"]
---

# Pazopanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pazopanib: From Renal Cell Carcinoma and Soft Tissue Sarcoma to Unclassified Renal Cell Carcinoma
{: .text-alpha }

## One-Sentence Summary

Pazopanib is an oral multi-target kinase inhibitor, originally used for renal cell carcinoma and soft tissue sarcoma.
The TxGNN model's top-ranked prediction is a rare renal cell carcinoma subtype with no supporting studies. The best-supported prediction is **unclassified renal cell carcinoma**, with **6 publications** (no registered clinical trials). The strongest trial evidence is for **liposarcoma** (**6 clinical trials**, **20 publications**).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma and soft tissue sarcoma (from the knowledge graph; no approved-indication text in the US licence records) |
| Predicted New Indication | Top-ranked: renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions. Best supported: unclassified renal cell carcinoma |
| TxGNN Prediction Score | 99.63% (both predictions) |
| Evidence Level | L5 for the top-ranked prediction; L3 for unclassified renal cell carcinoma |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 7 (1 NDA, 6 ANDAs; all cancelled) |
| Recommended Decision | Hold for the top-ranked prediction; Hold (research question) for unclassified renal cell carcinoma |

**Note on the top-ranked prediction:** The rank-1 prediction (Xp11.2/TFE3 translocation renal cell carcinoma) has no clinical trials or literature in the data compiled for this report, so the high score rests on the model alone. The sections below therefore focus on the best-supported predictions in the same data: unclassified renal cell carcinoma (the closest to the rank-1 renal cell carcinoma context) and liposarcoma (the strongest trial evidence).

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the rationale notes, pazopanib inhibits VEGFR, PDGFR and c-KIT signalling. Blocking these pathways limits tumour blood-vessel growth and tumour cell proliferation.

Pazopanib is already a standard first-line option in metastatic clear-cell renal cell carcinoma. Non-clear-cell subtypes, including unclassified histology and the rare Xp11.2/TFE3 translocation subtype, share the angiogenesis-driven biology to varying degrees. That is the reason for extrapolating. The evidence for these subtypes is retrospective or single-arm and does not separately analyse unclassified histology. No Phase 3 RCT exists for this subgroup.

For soft tissue sarcoma predictions, the same targets (PDGFR/VEGFR) are relevant. Pazopanib is approved for non-adipocytic soft tissue sarcoma, but liposarcoma was excluded from the registration trial. Evidence there comes from separate Phase 2 studies with modest results.

## Clinical Trial Evidence

Unclassified renal cell carcinoma has no registered trials. The table below shows trials for **liposarcoma**, the prediction with the most trial data (up to 10 shown; 6 available).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | Completed | 42 | Single-agent pazopanib in unresectable or metastatic liposarcoma; directly relevant |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | Completed | 52 | Pazopanib activity and tolerability in relapsed advanced or metastatic liposarcoma |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | Completed | 178 | Pazopanib plus oral topotecan in metastatic soft tissue and bone sarcomas; mixed population |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Completed | 140 | Preoperative radiation (with or without chemotherapy) plus or minus pazopanib in non-rhabdomyosarcoma soft tissue sarcoma; liposarcoma share unclear |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 | Completed | 54 | Randomized, double-blind gemcitabine with or without pazopanib in refractory soft tissue sarcoma |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | Recruiting | 139 | Maintenance pazopanib in pediatric non-rhabdomyosarcoma soft tissue sarcoma; indirect for liposarcoma |

## Literature Evidence

**Unclassified renal cell carcinoma** (6 publications):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase 2 (single-arm) | Cancer Res Treat | Efficacy and safety of pazopanib in metastatic non-clear-cell RCC |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospective cohort | Clin Genitourin Cancer | Italian multicenter study (PANORAMA) of first-line pazopanib in non-clear-cell RCC |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Retrospective cohort | Clin Genitourin Cancer | Outcomes of pazopanib in metastatic non-clear-cell RCC |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Real-world study | Ecancermedicalscience | Sunitinib vs pazopanib as first-line in non-clear-cell and sarcomatoid RCC |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Retrospective cohort | Eur Urol Oncol | First-line therapies in metastatic non-clear-cell RCC, including unclassified RCC (IMDC database) |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Retrospective cohort | Clin Genitourin Cancer | Carcinoma of unknown primary with RCC features treated with targeted therapy |

**Liposarcoma** (most relevant of 20 publications):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Phase 2 summary | Expert Opin Investig Drugs | Pazopanib in advanced intermediate- or high-grade liposarcoma |
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | Commentary | Lancet Oncol | Commentary on pazopanib trial in advanced liposarcoma |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | Phase 2 | Br J Cancer | Pazopanib with oral topotecan in soft tissue and bone sarcomas |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Review | Curr Treat Options Oncol | Systemic therapy options for dedifferentiated liposarcoma |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncol Res Treat | Established and experimental treatments for advanced liposarcoma |
| [30060824](https://pubmed.ncbi.nlm.nih.gov/30060824/) | 2018 | Preclinical | Tissue Cell | Pazopanib regressed a PDGFRA-amplified pleomorphic liposarcoma in a mouse xenograft model |

## US Market Information

All seven US licences are cancelled; none is currently valid. Approved-indication text is not available in the licence records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA022465 | VOTRIENT | Film-coated tablet | Novartis Pharmaceuticals Corporation |
| ANDA219922 | Pazopanib | Film-coated tablet | Torrent Pharmaceuticals Limited |
| ANDA217713 | Pazopanib | Tablet | Apotex Corp. |
| ANDA217517 | Pazopanib | Film-coated tablet | Teva Pharmaceuticals, Inc. |
| ANDA215837 | Pazopanib | Film-coated tablet | Sun Pharmaceutical Industries, Inc. |

Two further ANDAs (ANDA219034, Aurobindo Pharma; ANDA218231, Novugen Pharma) are also cancelled.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; the knowledge graph flags liver injury, hypertension, QT prolongation and proteinuria, so liver function, blood pressure, ECG and urine protein are reasonable considerations |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text):** hypertension, long QT syndrome and torsades de pointes, liver failure and drug-induced liver injury, hypothyroidism, myocardial infarction, hyperbilirubinemia (including Gilbert syndrome), intracerebral hemorrhage, active peptic ulcer disease, pancreatitis, proteinuria, diarrheal disease, and electrolyte disorders (potassium deficiency, hypercalcemia, phosphorus metabolism disease). These come from graph relationships and must be checked against the official label.
- **Drug interactions:** 100 interactions were found. Major ones among those listed include acid-suppressing drugs (famotidine, ranitidine, cimetidine, omeprazole, esomeprazole, rabeprazole, dexlansoprazole), clarithromycin and dolasetron. Moderate ones include dexamethasone, budesonide, aprepitant, loperamide, pioglitazone, saxagliptin, bisacodyl, magnesium oxide, eliglustat and polyethylene glycol.
- **Case-level signal:** one report describes pazopanib-related secondary polycythemia in metastatic myxofibrosarcoma.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, Xp11.2/TFE3 translocation renal cell carcinoma (and the other rank 2, 5, 6, 7 and 9 predictions), has no trials or literature, so it rests on the model alone (L5).
- Unclassified renal cell carcinoma (L3) is supported only by retrospective series and one single-arm study, with no confirmation that unclassified histology was analysed separately. Liposarcoma has Phase 2 evidence (L2) with modest results. Pazopanib is already established in related renal cell carcinoma and soft tissue sarcoma, so these are research questions rather than ready-to-go candidates.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Subgroup data confirming outcomes in unclassified RCC and, separately, in liposarcoma
- Clarification of the US regulatory position, given that all licences are currently cancelled
- A literature and trial search specific to Xp11.2/TFE3 translocation RCC before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


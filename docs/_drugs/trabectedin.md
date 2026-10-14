---
layout: default
title: Trabectedin
parent: High Evidence (L1-L2)
nav_order: 1245
evidence_level: L2
indication_count: 1
---

# Trabectedin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **1** 
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

# Trabectedin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Trabectedin is a marine-derived DNA-binding cytotoxic agent, originally used for ovarian cancer (together with soft tissue sarcoma in other regions).
The TxGNN model predicts it may be effective for **female breast carcinoma**,
with **1 clinical trial** (a QT-interval safety study, not an efficacy trial) and **20 publications** (including several Phase 2 breast cancer studies) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (the US approval text is not available in the data compiled for this report; the indication comes from the knowledge graph) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| US Market Status | Cancelled only (1 NDA, cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the published literature, trabectedin binds the DNA minor groove, forms DNA adducts and interferes with transcription-coupled nucleotide excision repair. This leads to DNA double-strand breaks. It is especially active in cells with homologous recombination deficiency, such as BRCA1/2-mutated tumours.

Ovarian cancer and a subset of breast cancers share BRCA-related DNA-repair biology. This overlap is the main reason the prediction is plausible. Preclinical work also suggests trabectedin reduces tumour-associated macrophages and may enhance immunotherapy. One example is its enhancement of IL-12 effects in triple-negative breast cancer (2025).

The very high TxGNN score is a model prediction only. The mechanistic link above is inferred from the literature, not from the supplied drug record.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | Completed | 76 | Single-blind, placebo-controlled study of trabectedin's effect on QT/QTc intervals in advanced solid tumours. It is a cardiac safety study, not a breast cancer efficacy trial. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Phase 2 (randomized, comparing 2 regimens) | Clin Breast Cancer | Efficacy and safety of single-agent trabectedin in advanced breast cancer after anthracycline and taxane treatment |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 | Ann Oncol | Activity of trabectedin in germline BRCA1/2-mutated metastatic breast cancer |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Phase 2 | Clin Breast Cancer | Trabectedin in HR-positive, HER2-negative advanced breast cancer, stratified by XPG expression |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 | Eur J Cancer | Trabectedin plus doxorubicin in advanced soft tissue sarcoma and breast cancer (9 breast patients) |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opin Investig Drugs | Overview of trabectedin in breast cancer, including its effects on transcription and tumour-associated macrophages |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treat Rev | Trabectedin as a chemotherapy option in BRCA-deficient patients |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunol Res | Trabectedin enhances the antitumour effect of IL-12 in triple-negative breast cancer |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Preclinical | Eur Cytokine Netw | Anti-angiogenic effects of trabectedin on breast cancer cells |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preclinical | Toxicol Lett | Different apoptosis responses in MCF-7 and MDA-MB-453 breast cancer cells |
| [25722380](https://pubmed.ncbi.nlm.nih.gov/25722380/) | 2015 | Phase 3 exploratory analysis | Ann Oncol | Effect of BRCA1 and XPG mutations on response in ovarian cancer (OVA-301) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA207953 (cancelled) | YONDELIS (Janssen Products, LP) | Lyophilized powder for injection | Indication text not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA minor-groove binder, marine-derived alkaloid) |
| Myelosuppression Risk | High. Literature reports grade 3-4 neutropenia in about 50% and thrombocytopenia in about 20% of patients. Hepatic toxicity is also common. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function tests (and renal function); cardiac monitoring should be considered given the dedicated QT study |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records, and the first 20 are listed in the data compiled for this report. Most are Moderate. The one **Major** interaction is with **clarithromycin**, a strong CYP3A4 inhibitor. Moderate interactions include aprepitant, dexamethasone, cimetidine, metronidazole, miconazole, levofloxacin, rosuvastatin and simvastatin, among others. These should be reviewed for any combination regimen.

For warnings and contraindications, please refer to the package insert. The FDA label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, especially for BRCA-mutated breast cancer, and several Phase 2 breast cancer studies exist. However, the only registered trial in the data is a QT safety study, and the Phase 2 publications do not by themselves establish efficacy. The US NDA is cancelled, and the FDA label safety review is missing, which blocks safety screening. The data support the recommendation "Research Question" rather than advancing the drug.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Full review of the Phase 2 breast cancer results (PMIDs 25239225, 24692579, 27266804) for response rates and survival outcomes
- Identification of a target subgroup (for example BRCA1/2-mutated or triple-negative breast cancer) and any registered efficacy trials
- Clarification of why the US NDA was cancelled, and of route and regulatory feasibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


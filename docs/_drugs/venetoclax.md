---
layout: default
title: Venetoclax
parent: Model Prediction Only (L5)
nav_order: 1286
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Venetoclax: predicted new indication CLL/SLL with somatic hypermutation of the immunoglobulin heavy chain… (evidence level L5). Approved use: Acute lymphoblastic/lymphocytic leukemia"
monitor_inn: "VENETOCLAX"
predicted_indications: ["Hodgkins lymphoma", "myeloid leukemia", "chronic myelogenous leukemia, BCR-ABL1 positive", "Ewing sarcoma", "follicular lymphoma", "metastatic neoplasm", "malignant spiradenoma"]
---

# Venetoclax
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

# Venetoclax: From Acute Lymphoblastic Leukemia / Richter Syndrome to Chronic Lymphocytic Leukemia Subtypes (Predicted Indication)

## One-Sentence Summary

Venetoclax is an oral BCL-2 inhibitor whose original indications in the knowledge graph are acute lymphoblastic/lymphocytic leukemia and Richter syndrome.
The TxGNN model predicts it may be effective for **chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation** (score 99.55%), but **no clinical trials and no literature** specific to this entry are available, so support is prediction only.
Among the other top-10 predictions, **acute myeloid leukemia (AML)** has the strongest supporting data (**about 35 trials and 18 publications**).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic/lymphocytic leukemia; Richter syndrome (knowledge graph indication edges; the US license record contains no indication text) |
| Predicted New Indication | CLL/SLL with somatic hypermutation of the immunoglobulin heavy chain variable-region gene (top-ranked prediction) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 (top-ranked prediction); best among top-10 predictions: L1 for AML, with caveats |
| US Market Status | Cancelled only (the single NDA record is marked cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold (top-ranked prediction); Proceed with Guardrails for AML |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From the evidence reviewed, venetoclax is a selective BCL-2 inhibitor (BH3 mimetic) that restores apoptosis in cells that depend on BCL-2 for survival.

CLL/SLL cells depend on BCL-2 overexpression, so BCL-2 inhibition is mechanistically plausible. The predicted entry is a molecular subtype (mutated IGHV) of a disease in which venetoclax is already well established. Literature in the compiled data (for example the MURANO final analysis, PMID 40009494) reports durable benefit from venetoclax-rituximab in relapsed/refractory CLL. The same BCL-2 dependence extends to other predicted indications such as follicular lymphoma (t(14;18) drives BCL-2 overexpression) and AML.

Note that the top two predictions (the mutated-IGHV and pregerminal-center CLL/SLL entries) share the same score and are essentially subtypes of the same disease. The remaining sections focus on predictions with actual supporting data.

---

## Clinical Trial Evidence

**Top-ranked prediction (CLL/SLL, mutated IGHV):** Currently no related clinical trials registered.

**Selected supporting trials for other top-10 predictions** (up to 10 shown; enrollment as registered):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06852222](https://clinicaltrials.gov/study/NCT06852222) | Phase 3 | Recruiting | 600 | AML: bleximenib + venetoclax + azacitidine vs placebo + VEN/AZA (NPM1/KMT2A); no results yet |
| [NCT05177731](https://clinicaltrials.gov/study/NCT05177731) | Phase 3 | Active, not recruiting | 188 | AML: venetoclax + decitabine vs conventional "7+3" induction in young adults |
| [NCT07132684](https://clinicaltrials.gov/study/NCT07132684) | Phase 3 | Recruiting | 240 | AML: venetoclax + azacitidine vs daunorubicin/idarubicin + cytarabine in fit older patients |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | Recruiting | 324 | AML/MDS: venetoclax with fractionated busulfan-based transplant conditioning |
| [NCT03112174](https://clinicaltrials.gov/study/NCT03112174) | Phase 3 | Completed | 366 | Mantle cell lymphoma: ibrutinib + venetoclax vs ibrutinib + placebo (results not summarized in the data) |
| [NCT02689440](https://clinicaltrials.gov/study/NCT02689440) | Phase 2 | Active, not recruiting | 155 | CML: dasatinib + venetoclax in early chronic phase |
| [NCT04188405](https://clinicaltrials.gov/study/NCT04188405) | Phase 2 | Completed | 20 | Ph+ AML / advanced-phase CML: decitabine + venetoclax + ponatinib |
| [NCT03276468](https://clinicaltrials.gov/study/NCT03276468) | Phase 2 | Completed | 136 | Relapsed/refractory follicular and other lymphomas: atezolizumab + obinutuzumab + venetoclax |
| [NCT02187861](https://clinicaltrials.gov/study/NCT02187861) | Phase 2 | Completed | 163 | Relapsed/refractory follicular lymphoma: venetoclax + bendamustine/rituximab or rituximab |
| [NCT03223610](https://clinicaltrials.gov/study/NCT03223610) | Phase 1b/2 | Recruiting | 155 | Relapsed/refractory B-cell lymphoma: ViPOR combination (Hodgkin-specific efficacy unclear) |

Other predictions with trials in the data: Hodgkin lymphoma (about 43 trials, mostly B-cell lymphoma baskets, indirect relevance) and metastatic neoplasm (mostly small or terminated breast, prostate and AML studies). No trials were supplied for Ewing sarcoma, malignant spiradenoma, or AML with t(8;21).

---

## Literature Evidence

**Top-ranked prediction (CLL/SLL, mutated IGHV):** Currently no related literature available. The second CLL/SLL entry has one review of B-cell receptor biology (PMID 35158929), which gives context but no venetoclax clinical data.

**Selected literature supporting other predictions:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40009494](https://pubmed.ncbi.nlm.nih.gov/40009494/) | 2025 | RCT follow-up | Blood | MURANO final analysis (7-year follow-up): fixed-duration venetoclax-rituximab superior to bendamustine-rituximab in relapsed/refractory CLL |
| [29339097](https://pubmed.ncbi.nlm.nih.gov/29339097/) | 2018 | Phase 1b | Lancet Oncol | Venetoclax with decitabine or azacitidine in elderly untreated AML |
| [40913104](https://pubmed.ncbi.nlm.nih.gov/40913104/) | 2025 | Post hoc analysis | Leukemia | VIALE-A: venetoclax + azacitidine vs azacitidine alone in AML ineligible for intensive chemotherapy, stratified by age |
| [35046058](https://pubmed.ncbi.nlm.nih.gov/35046058/) | 2022 | Cohort | Clin Cancer Res | Venetoclax + azacitidine in treatment-naïve IDH1/2-mutant AML |
| [39303729](https://pubmed.ncbi.nlm.nih.gov/39303729/) | 2024 | Phase 2 | Lancet Haematol | Decitabine + venetoclax + ponatinib in advanced-phase CML and Ph+ AML |
| [38591430](https://pubmed.ncbi.nlm.nih.gov/38591430/) | 2024 | Clinical study | Cancer | Dasatinib + venetoclax in newly diagnosed chronic-phase CML |
| [32785666](https://pubmed.ncbi.nlm.nih.gov/32785666/) | 2020 | Phase 2 | Blood | CONTRALTO: venetoclax-rituximab ± bendamustine vs bendamustine-rituximab in relapsed/refractory follicular lymphoma |
| [40285420](https://pubmed.ncbi.nlm.nih.gov/40285420/) | 2025 | Phase 2 | Br J Haematol | Atezolizumab + obinutuzumab + venetoclax in relapsed/refractory B-NHL (LYSA) |
| [30518523](https://pubmed.ncbi.nlm.nih.gov/30518523/) | 2019 | Phase 1b | Cancer Discov | Venetoclax + tamoxifen in ER+/BCL-2+ metastatic breast cancer |
| [28724540](https://pubmed.ncbi.nlm.nih.gov/28724540/) | 2017 | Review | Blood | Targeting BCL-2 in B-cell lymphomas |

For Ewing sarcoma, only preclinical work exists (for example PMID 30348635, BCL-2/BCL-XL dependence under PARP inhibition), and half of the items returned are unrelated AML reports.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208573 (status: cancelled) | Venclexta (AbbVie Inc.) | Tablet, film coated (oral) | Indication text not available in the data |

The only US license record on file is marked as cancelled, so the data compiled for this report show no currently valid US authorization. This should be verified against current FDA records before any decision, since venetoclax is described in the literature as FDA-approved for CLL and AML.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective BCL-2 inhibitor / BH3 mimetic) |
| Myelosuppression Risk | Medium to high (myelosuppression and tumour lysis syndrome are the most common toxicities reported in the literature, particularly in combination regimens) |
| Emetogenicity Classification | Low to moderate (not confirmed in the data; refer to the package insert) |
| Monitoring Items | CBC with differential, tumour lysis syndrome labs (electrolytes, uric acid, creatinine), liver and renal function, infection surveillance |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions:** A screen returned 100 interacting drugs (20 shown in the data). Major-level interactions include:
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Eliglustat
  - Rolapitant
  - Fidaxomicin
  - Cobicistat
  - Deferiprone
  - Samarium (153Sm) lexidronam

  Moderate-level examples include cimetidine, miconazole, clotrimazole, rifaximin and deferasirox. Literature in the data also highlights the CYP3A interaction with strong inhibitors such as posaconazole (PMID 28161120), which requires venetoclax dose adjustment.

Label warnings and contraindications were not available. Please refer to the package insert for the remaining safety information.

---

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction (CLL/SLL, mutated IGHV).
**Proceed with Guardrails** is supported only for AML (a separate prediction, rank 4).

**Rationale:**
- The top-ranked prediction has a very high TxGNN score but no trials or literature of its own, so it is prediction-only (L5), even though BCL-2 dependence makes it mechanistically plausible and venetoclax is established in CLL generally.
- AML has the broadest data (a Phase 3 randomized trial, several Phase 2/3 studies, and many publications), but the Phase 3 trial is still recruiting without results, so the L1 grade rests largely on venetoclax's established clinical standing in AML.
- Follicular lymphoma and CML (L2) have Phase 2 evidence only; Hodgkin lymphoma and metastatic neoplasm (L3) have indirect or heterogeneous evidence; Ewing sarcoma is preclinical (L4); malignant spiradenoma and AML with t(8;21) have no data (L5, Hold).

**To proceed, the following is needed:**
- Subtype-specific data (trials or analyses) for mutated-IGHV CLL/SLL, or confirmation that the established CLL evidence can be applied
- Current FDA label information (warnings, contraindications, approved indications) and verification of the "cancelled" licence status
- Detailed mechanism-of-action data
- For AML: results from the ongoing Phase 3 trials
- A monitoring plan covering tumour lysis syndrome, myelosuppression, infections, and CYP3A/azole interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


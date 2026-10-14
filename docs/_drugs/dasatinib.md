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

# Dasatinib: From Chronic Myelogenous Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is an oral tyrosine kinase inhibitor, originally used to treat BCR-ABL1-positive chronic myelogenous leukemia (including blast phase).
The TxGNN model predicts it may be effective for **Ewing sarcoma**,
but the supporting evidence is thin: **2 clinical trials** (one terminated with 7 patients, one mixed-sarcoma Phase 2) and **10 publications**, mostly preclinical or review articles.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukemia, BCR-ABL1 positive (including blast phase) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 (one completed Phase 2 trial, but in mixed sarcomas and without a positive Ewing-specific result) |
| US Market Status | Cancelled only (all licenses listed as cancelled) |
| Number of NDAs | 8 authorizations in total (2 NDAs and 6 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the published literature, dasatinib inhibits BCR-ABL and SRC-family kinases, and it also acts on c-KIT and PDGFR. Its efficacy in BCR-ABL1-positive leukemia is established.

The link to Ewing sarcoma runs through SRC. Preclinical studies show that Src signaling drives invasion, migration and invadopodia formation in Ewing sarcoma cells. Dasatinib reduced proliferation and migration in Ewing sarcoma and other sarcoma cell lines, and induced apoptosis in bone sarcoma cells that depend on SRC. The rationale is therefore plausible.

Clinical support is weak, however. A review notes that in the Phase 2 study in advanced sarcomas, single-agent dasatinib failed in the Ewing sarcoma and rhabdomyosarcoma subtypes. Only a small descriptive case series exists for a multi-drug regimen containing dasatinib (RIST) in relapsed Ewing sarcoma.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Dasatinib with ifosfamide, carboplatin and etoposide in pediatric solid tumors; terminated early, so little safety or efficacy information |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Dasatinib in advanced sarcomas, assessing response rate and 6-month progression-free survival; mixed subtypes, so Ewing-specific results are limited |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Review | Sarcoma | Targeting the FAK-Src complex in DSRCT, Ewing sarcoma and rhabdomyosarcoma; single-agent dasatinib failed in Ewing sarcoma and rhabdomyosarcoma in a Phase 2 study |
| [42804591](https://pubmed.ncbi.nlm.nih.gov/42804591/) | 2026 | Case series | J Pediatr Hematol Oncol | Descriptive single-center experience with RIST (rapamycin, irinotecan, dasatinib, temozolomide) in relapsed Ewing sarcoma |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncol Lett | Role of Src signaling in sarcoma and its feasibility as a drug target |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical | Cancer Res | Dasatinib inhibits migration and invasion in sarcoma cell lines and induces apoptosis in SRC-dependent bone sarcoma cells |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical | Oncol Rep | Antiproliferative and antimigratory activity of dasatinib in neuroblastoma and Ewing sarcoma cell lines |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical | Neoplasia | Microenvironmental stress induces Src-dependent invadopodia and cell migration in Ewing sarcoma |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical | Neoplasia | Tenascin C and Src cooperate to promote invadopodia formation in Ewing sarcoma |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review | Curr Treat Options Oncol | Systemic therapy for chondrosarcoma; only indirectly related to Ewing sarcoma |

## US Market Information

All eight authorizations are listed as cancelled in the data compiled for this report. Approved indication text was not available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021986 | SPRYCEL (E.R. Squibb & Sons) | Tablet | Not available |
| NDA216099 | PHYRAGO (Cycle Pharmaceuticals) | Tablet | Not available |
| ANDA216261 | Dasatinib (Alembic) | Film-coated tablet | Not available |
| ANDA213383 | Dasatinib (Dr. Reddy's) | Film-coated tablet | Not available |
| ANDA217217 | Dasatinib (BluePoint) | Film-coated tablet | Not available |

Three more ANDAs (AvKARE, Aurobindo, Zydus) are also listed as cancelled.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: BCR-ABL, SRC family, c-KIT, PDGFR) |
| Myelosuppression Risk | Medium to high (neutropenia, thrombocytopenia and anemia appear among the contraindication-related conditions in the knowledge graph) |
| Emetogenicity Classification | Low to medium |
| Monitoring Items | CBC with differential, liver function, cardiac monitoring including QT interval, signs of pleural effusion |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** long QT syndrome (including familial), torsades de pointes, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, congestive heart failure, heart failure, myocardial infarction, coronary thrombosis, anemia, macrocytic anemia, hemoglobinopathy, active peptic ulcer disease, intracerebral hemorrhage, pericardial effusion and hemopericardium.
- **Drug Interactions (100 interactions found; main ones shown):**
  - Major: famotidine, ranitidine, cimetidine, omeprazole, rabeprazole (acid-suppressing drugs), dexamethasone, acetylsalicylic acid, clarithromycin
  - Moderate: hydrocortisone, budesonide, loperamide, aprepitant, bisacodyl, magnesium oxide, aluminum hydroxide, calcium carbonate, saxagliptin, polyethylene glycol, castor oil
- **Reported adverse events in the literature:** pleural effusion is frequent, and chylothorax has been reported as a rare event.

Label warnings and contraindications were not available. Please refer to the package insert for the official safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The preclinical rationale (SRC dependence of Ewing sarcoma) is plausible, but the only substantial clinical trial in sarcomas reportedly showed no single-agent benefit in Ewing sarcoma. The remaining clinical data are a terminated 7-patient trial and a small case series. The L2 label comes from a mixed-sarcoma trial and overstates the Ewing-specific evidence. The high TxGNN score alone does not justify advancing.

**To proceed, the following is needed:**
- Ewing-specific subgroup results from NCT00464620
- Prospective data on dasatinib-containing combinations (such as RIST) in relapsed Ewing sarcoma
- Official package insert warnings and contraindications, together with the mechanism of action data
- A cardiac, pleural and hematologic safety monitoring plan, plus a review of acid-suppressant interactions
- Clarification of the cancelled US market status, to confirm product availability

*Other predictions (for context):* Myeloid leukemia (rank 2) has the strongest evidence (L1), but dasatinib is already approved for BCR-ABL1-positive CML, so this is largely an existing indication rather than repurposing. A Phase 3 trial in core-binding factor AML (PMID 41490515) suggests a possible subset-specific signal. Liposarcoma and dermatofibrosarcoma protuberans have only preclinical or review support, and the remaining predictions have no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Everolimus
parent: Model Prediction Only (L5)
nav_order: 687
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "EVEROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "prostate embryonal rhabdomyosarcoma"]
description: "Everolimus: predicted new indication Liposarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Everolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Everolimus: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Everolimus is an mTOR inhibitor originally used for renal cell carcinoma, breast cancer, and tuberous sclerosis-related conditions.
The TxGNN model predicts it may be effective for **liposarcoma**,
with **1 clinical trial** and **4 publications** currently supporting this direction. Only one of these publications is a clinical trial report, and it tests everolimus in combination with ribociclib.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 by the strict rules (no completed Phase 3/2-3 RCT). The data compiled for this report assigns L2, but the only trial is an uncompleted, single-arm Phase 2 combination study. |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of NDAs | 11 authorizations in total (3 NDAs, 8 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, everolimus is an mTORC1 inhibitor. Its efficacy has been established in renal cell carcinoma and other tumors, and mechanistically it may be applicable to liposarcoma.

Dedifferentiated liposarcoma is characterized by CDK4/MDM2 amplification. Blocking both the CDK4/6 pathway (with ribociclib) and the PI3K/AKT/mTOR pathway (with everolimus) is a plausible strategy. Preclinical models have shown synergistic growth inhibition for this combination in multiple tumor types. Patient-derived xenograft literature gives indirect support.

An important caveat: the evidence concerns the combination, so everolimus's own contribution cannot be separated from ribociclib's. The high TxGNN score is also partly a model similarity signal and does not by itself show clinical benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma and leiomyosarcoma after at least 1 prior systemic therapy. Single-arm, two-center, and primary aim is anti-tumor activity. Everolimus cannot be separated from ribociclib. Estimated completion is December 2026. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase II trial report | Clin Cancer Res | Report of the ribociclib + everolimus trial in advanced dedifferentiated liposarcoma and leiomyosarcoma. The rationale is CDK4/6 targeting in DDL and mTOR targeting in LMS. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (preclinical) | Front Oncol | Patient-derived orthotopic xenograft models in sarcoma used to identify combination therapies with the CDK inhibitor palbociclib. Indirect support. |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Preclinical | Oncogene | The XPO1 inhibitor selinexor disrupts the transcriptional circuitry of dedifferentiated liposarcoma. Not everolimus-specific. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Res | Eribulin combinations with other anticancer agents in xenograft models. Not everolimus-specific. |

## US Market Information

The drug is marketed in the US with 11 valid authorizations, and approved indication text is not available for any of them. The five main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022334 | Afinitor (Novartis) | Tablet | Not available (valid) |
| NDA203985 | Afinitor (Novartis) | Tablet for suspension | Not available (valid) |
| NDA021560 | Zortress (Novartis) | Tablet | Not available (valid) |
| ANDA207486 | Everolimus (Hikma) | Tablet | Not available (valid) |
| ANDA210050 | Everolimus (Teva) | Tablet | Not available (valid) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor), not a conventional cytotoxic |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function, fasting glucose and lipids, signs of stomatitis and pulmonary symptoms |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Label-based warnings and contraindications are not available in the data compiled for this report, so the package insert should be consulted.

- **Disease-level cautions (knowledge graph, not label text)**: Everolimus is linked to cautions in liver failure and liver disease, kidney disease, hyperglycemia and diabetes mellitus, diabetic ketoacidosis, hyperlipidemia and hypertriglyceridemia, cytopenias (thrombocytopenia, neutropenia, leukopenia, anemia, agranulocytosis), interstitial lung disease, congestive heart failure, pericardial effusion, hemolytic-uremic syndrome, stomatitis, and lymphoma. The graph also lists cancer itself, which likely reflects immunosuppression concerns.
- **Drug Interactions**: 100 interactions were identified. Examples of **Major** interactions include amphotericin B (including the lipid complex), aprepitant, dexamethasone, and clarithromycin. Many **Moderate** interactions involve antidiabetic agents (metformin, acarbose, glimepiride, chlorpropamide, and the DPP-4 inhibitors, SGLT2 inhibitors, and GLP-1 agonists listed), plus cimetidine, eliglustat, and eluxadoline. Strong CYP3A4/P-gp modulators warrant particular attention.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is a single-arm, uncompleted Phase 2 combination trial in dedifferentiated liposarcoma, so everolimus's own contribution is unproven. The drug is marketed in the US with 11 valid authorizations, but label safety data is missing, which blocks safety screening. This is best treated as a research question rather than a development candidate for now.

**To proceed, the following is needed:**
- Final results of NCT03114527, ideally with some way to isolate the everolimus contribution
- FDA package insert warnings and contraindications
- Detailed mechanism-of-action data (MOA)
- Clarification of the current US regulatory status, since the drug is marketed with 11 valid authorizations
- Safety monitoring plan for the cytopenia, metabolic, and pulmonary risks flagged above

**Other predictions (all Hold):** Rhabdomyosarcoma has the next-strongest support, at L3 (Phase 1 and Phase 1/2 pediatric solid-tumor trials, NCT00187174 and NCT03245151, with mixed populations). The other predictions are prediction-only with no retrieved clinical evidence, namely ovarian myxoid liposarcoma, dermatofibrosarcoma protuberans, the rhabdomyosarcoma subtypes, and the rare renal cell carcinoma variants.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


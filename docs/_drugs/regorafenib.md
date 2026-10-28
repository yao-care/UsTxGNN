---
layout: default
title: Regorafenib
parent: High Evidence (L1-L2)
nav_order: 1115
evidence_level: L2
indication_count: 8
monitor_inn: "REGORAFENIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "clear cell renal carcinoma", "unclassified renal cell carcinoma", "renal cell carcinoma associated with neuroblastoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "childhood kidney cell carcinoma", "vulva sarcoma"]
last_modified_at: 2026-10-28
description: "Regorafenib: predicted new indication Liposarcoma (evidence level L2). Approved use: Not recorded in the local data"
---

# Regorafenib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **8** 
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

## Regorafenib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Regorafenib is an oral multi-kinase inhibitor originally used for metastatic colorectal cancer, hepatocellular carcinoma and gastrointestinal stromal tumor (GIST).
The TxGNN model predicts it may be effective for **Liposarcoma**, with **1 clinical trial** and **9 publications** compiled for this direction.
However, the randomized trial data in liposarcoma (REGOSARC and the SARC024 liposarcoma cohort) did **not** show benefit, so the prediction is not supported by the clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L2 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold (the compiled system output was "Proceed with Guardrails", but see rationale below) |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not captured in the drug record. From the literature compiled for this report, regorafenib is an oral diphenylurea multi-kinase inhibitor that targets angiogenic (VEGFR1-3, TIE2), stromal (PDGFR-β, FGFR) and oncogenic (KIT, RET, RAF) kinases. It is established in metastatic colorectal cancer and GIST.

Soft tissue sarcomas, including liposarcoma, depend partly on angiogenic and growth-factor signaling. Related kinase inhibitors (sorafenib, sunitinib, pazopanib) have shown activity in some soft tissue sarcomas. This is the basis for the model's prediction.

The clinical data, however, show that benefit depends on histology. The placebo-controlled REGOSARC Phase 2 trial showed efficacy in leiomyosarcoma, synovial sarcoma and other non-adipocytic sarcomas, but **not in liposarcoma**. The SARC024 liposarcoma cohort reached the same conclusion: the authors state that the results "do not support the routine use of regorafenib in this patient population."

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 blanket protocol of oral regorafenib in selected sarcoma subtypes, including liposarcoma. Directly tests the drug in the target disease, though it is a multi-subtype protocol with limited liposarcoma-specific power. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | Randomized, double-blind, placebo-controlled Phase 2 liposarcoma cohort of SARC024. Results do not support routine use of regorafenib in treatment-refractory liposarcoma. |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | Lancet Oncology | REGOSARC: randomized Phase 2 trial in anthracycline-pretreated advanced soft tissue sarcoma. |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT | European Journal of Cancer | Updated REGOSARC analysis including cross-over; efficacy in non-adipocytic sarcoma but not in liposarcoma. |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Cohort | Cancer | Quality-adjusted time without symptoms or toxicity (Q-TWiST) analysis of REGOSARC; regorafenib improved PFS in non-adipocytic sarcoma. |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Review of the growing role of regorafenib in sarcoma treatment. |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Critical Reviews in Oncology/Hematology | Review of maintenance therapy after first-line treatment for advanced soft tissue sarcoma. |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective study | Anti-Cancer Drugs | Anlotinib in well-differentiated/dedifferentiated liposarcoma (a different drug; context only). |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Study protocol | BMC Cancer | REGOSARC trial protocol. |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Case report | Rare Tumors | Pazopanib response in Ewing sarcoma; provided rationale for adding arms to SARC024. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203085 (cancelled) | Stivarga (Bayer HealthCare Pharmaceuticals Inc.) | Film-coated tablet (oral) | Not recorded in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (hepatic toxicity is a recognized class concern for anti-angiogenic TKIs), blood pressure, urine protein (proteinuria), skin (hand-foot skin reaction), CBC |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records (20 shown in the compiled data). Major-level interactions include:
  - Acetylsalicylic acid
  - Deferasirox
  - Ibritumomab tiuxetan
  - Tositumomab (including I-131)
  - Abciximab
  - Alteplase
  - Antithrombin III human
  - Apixaban

  Many of these involve bleeding risk (antiplatelet, anticoagulant and thrombolytic agents). Moderate interactions include dexamethasone, clarithromycin, naltrexone, rosuvastatin and cobicistat.
- **Class-related toxicities from the literature**: Meta-analyses on anti-angiogenic TKIs and regorafenib describe hepatic toxicity, hand-foot skin reaction and proteinuria.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct randomized evidence in liposarcoma (REGOSARC and the SARC024 liposarcoma cohort) is negative, and the authors do not support routine use. The high TxGNN score (0.9976) and the Phase 2 evidence level (L2) reflect that the drug has been tested in this disease, not that it works. The US NDA is also recorded as cancelled, and label warnings are unavailable. The other predicted indications are either prediction-only (L5, Hold) or lack disease-specific trials (clear cell renal carcinoma, L3, research question).

**To proceed, the following is needed:**
- Retrieve the FDA package insert (warnings and contraindications), a blocking gap for safety screening
- Obtain mechanism-of-action data from DrugBank
- A biological rationale for why liposarcoma would respond when earlier randomized data did not (for example, a specific subtype or biomarker, or a combination approach)
- If the program is redirected, evaluate clear cell renal carcinoma, where a Phase 2 study in untreated metastatic disease (PMID 22959186) and preclinical DDR2-sensitivity data (PMID 41324163) exist, but no Phase 3 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Fibrinogen Human
parent: 僅模型預測 (L5)
nav_order: 705
evidence_level: L5
indication_count: 1
---

# Fibrinogen Human
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# FIBRINOGEN HUMAN: From Fibrinogen Replacement Therapy to Hemoglobinopathy

## One-Sentence Summary

Fibrinogen Human (DrugBank DB09222) is a plasma-derived coagulation factor concentrate; its specific approved indication text is not available in this Evidence Pack, and the drug is currently **not marketed** under the reviewed regulatory dataset. The TxGNN model predicts potential relevance to **Hemoglobinopathy** with a **99.12%** score, but on closer review the supporting evidence is weak: the single matched clinical trial is a data-linkage mismatch (different drug), and the 20 literature hits describe disease-related coagulation abnormalities in hemoglobinopathy patients rather than therapeutic use of exogenous fibrinogen — with some evidence pointing to a plausible **safety concern instead of a benefit signal**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (no Taiwan license records; `original_indications` empty) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`), and no approved-indication text exists in the regulatory dataset for this drug. Based on general pharmacology, Fibrinogen Human is a plasma-derived coagulation factor concentrate used to correct fibrinogen deficiency and control bleeding; mechanistically, it acts by increasing circulating fibrinogen available for clot formation.

However, the actual evidence gathered for the **hemoglobinopathy** prediction does not support a straightforward "efficacy" narrative. The literature base is dominated by observational and mechanistic studies describing an **endogenous hypercoagulable state** already present in sickle cell disease and β-thalassemia (elevated fibrinogen, thrombin generation, platelet activation, fibrinogen-mediated RBC-endothelium adhesion). This is disease pathophysiology, not evidence that *administering* exogenous fibrinogen treats hemoglobinopathy. One review (PMID 33026614) further raises the possibility that exogenous fibrinogen may increase cardiovascular/thrombotic risk. Since hemoglobinopathy patients are already prone to hypercoagulability, supplementing a pro-coagulant factor in this population is mechanistically more plausible as a **risk signal** than a therapeutic opportunity. This should be treated as a caution flag rather than a confirmation of the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03673085](https://clinicaltrials.gov/study/NCT03673085) | Phase 1 | Completed | 32 | First-in-human dose-escalation PK/safety study of **CN128** in thalassemia patients. ⚠ Data quality note: the investigational drug is CN128, not Fibrinogen Human — this appears to be a keyword-based false-positive match (disease-term overlap only) and does not constitute direct clinical evidence for this drug. |

No genuine Fibrinogen Human clinical trial in hemoglobinopathy is currently registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33026614](https://pubmed.ncbi.nlm.nih.gov/33026614/) | 2020 | Review | Molecular Biology Reports | Discusses exogenous fibrinogen's role in reducing surgical bleeding but also its potential to contribute to cardiovascular disease — a direct safety-relevant reference for this drug class. |
| [32777069](https://pubmed.ncbi.nlm.nih.gov/32777069/) | 2020 | Cohort | Blood Advances | Fibrinogen mediates sickle RBC adhesion to ICAM-1, linked to right-to-left shunts in sickle cell disease — implicates fibrinogen in disease vascular pathology, not treatment. |
| [24609765](https://pubmed.ncbi.nlm.nih.gov/24609765/) | 2014 | Cohort | Int J Hematology | Thromboelastometry shows a hypercoagulable profile in children with β-thalassemia. |
| [39441287](https://pubmed.ncbi.nlm.nih.gov/39441287/) | 2024 | Observational | Georgian Medical News | Protein C/S evaluation in β-thalassemia major, correlated with hemoglobin, ferritin, D-dimer. |
| [35417875](https://pubmed.ncbi.nlm.nih.gov/35417875/) | 2022 | Review/Cohort | Georgian Medical News | Documents thrombotic complications and latent hypercoagulation across β-thalassemia subtypes. |
| [14693325](https://pubmed.ncbi.nlm.nih.gov/14693325/) | 2003 | Review | American Journal of Medicine | Reviews hypercoagulability in sickle cell disease, including elevated fibrinogen/thrombin activity. |
| [31648337](https://pubmed.ncbi.nlm.nih.gov/31648337/) | 2019 | Review | Blood Advances | Describes coagulation system activation, including thrombin, as a driver of SCD pathophysiology and organ damage. |
| [27723451](https://pubmed.ncbi.nlm.nih.gov/27723451/) | 2017 | Observational | Blood Transfusion | Platelet procoagulant properties and effect of transfusion in β-thalassaemia patients. |
| [1203541](https://pubmed.ncbi.nlm.nih.gov/1203541/) | 1975 | Observational | Blut | Early study documenting hypercoagulability and hypofibrinolysis, with elevated fibrinogen levels, in sickle-cell disease. |
| [7272221](https://pubmed.ncbi.nlm.nih.gov/7272221/) | 1981 | Observational | British Journal of Haematology | Erythrocyte deformability and blood viscosity changes during sickle-cell vaso-occlusive crisis. |

All 10 listed publications are disease-mechanism or observational studies describing coagulation abnormalities intrinsic to hemoglobinopathies. **None report therapeutic administration of exogenous Fibrinogen Human to treat hemoglobinopathy.**

---

## US Market Information

No Taiwan marketing authorization is on record for this drug (`market_status: 未上市`, `total_licenses: 0`). No license/product data is available to tabulate.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, DDI) is available for this drug in the current dataset — all fields are marked as data gaps. Please refer to the package insert for safety information.

**Additional signal surfaced during evidence review (not from structured safety fields):** the literature base suggests hemoglobinopathy patients already exist in a hypercoagulable state; supplementing exogenous fibrinogen in this population carries a theoretical thrombotic/cardiovascular risk (per PMID 33026614) that should be explicitly evaluated before any further development is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not corroborated by real evidence — the only matched clinical trial is a data-linkage false positive (wrong drug), and all 20 literature hits describe hemoglobinopathy-associated coagulation pathophysiology rather than therapeutic benefit from exogenous fibrinogen. There is also a plausible mechanistic safety concern (added thrombotic risk in an already hypercoagulable population) rather than a benefit signal. This corresponds to Evidence Level L5 (model prediction only) and Decision Stage S0.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism of action data (High-severity data gap, DG002)
- A genuine, drug-matched clinical trial or case series evaluating Fibrinogen Human in hemoglobinopathy patients
- A dedicated thrombotic-risk assessment for administering a pro-coagulant factor to an already hypercoagulable population
- Basic Taiwan/US regulatory and DDI data, none of which currently exist for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Vorinostat
parent: Model Prediction Only (L5)
nav_order: 1296
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-03
monitor_inn: "VORINOSTAT"
predicted_indications: ["primary cutaneous B-cell lymphoma"]
description: "Vorinostat: predicted new indication Primary cutaneous B-cell lymphoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Vorinostat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Vorinostat: Primary cutaneous B-cell lymphoma
{: .text-alpha }

## One-Sentence Summary

Vorinostat is an oral histone deacetylase (HDAC) inhibitor that is currently marketed in the United States.
The TxGNN model predicts it may be effective for **primary cutaneous B-cell lymphoma**, with a score of 0.9921.
Four early-phase clinical trials and one preclinical publication are linked to this prediction, but **none studies this disease directly**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary cutaneous B-cell lymphoma |
| TxGNN Prediction Score | 0.9921 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Vorinostat belongs to the HDAC inhibitor class. HDAC inhibition raises acetylation of histones and other proteins, which can trigger cell-cycle arrest and apoptosis in malignant lymphocytes.

Preclinical work in mantle cell lymphoma, an aggressive B-cell neoplasm, shows that vorinostat induces apoptosis by acetylating the promoters of proapoptotic BH3-only genes. This suggests that HDAC inhibition may act on B-cell lymphoid malignancies as well. The very high model score probably reflects similarity to the lymphoid cancer for which the drug is already used.

This is computational inference only. No study in the compiled data tests vorinostat in primary cutaneous B-cell lymphoma, so the prediction remains a research hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01567709](https://clinicaltrials.gov/study/NCT01567709) | Phase 1 | Completed | 34 | Alisertib plus vorinostat in relapsed lymphomas, including B-cell non-Hodgkin lymphoma. It gives combination dose and safety data, with no conclusion specific to cutaneous B-cell lymphoma. |
| [NCT00045006](https://clinicaltrials.gov/study/NCT00045006) | Phase 1 | Completed | N/A | Oral vorinostat dose-finding in advanced solid tumors and hematologic malignancies. It provides safety and pharmacokinetic data only. |
| [NCT00499811](https://clinicaltrials.gov/study/NCT00499811) | Phase 1 | Completed | 15 | Vorinostat in solid tumors and lymphomas with varying degrees of liver dysfunction. It informs dosing and safety only. |
| [NCT01789255](https://clinicaltrials.gov/study/NCT01789255) | Phase 2 | Completed | 12 | Vorinostat with tacrolimus and methotrexate to prevent graft-versus-host disease after stem cell transplant. This is a different clinical setting and is not relevant to lymphoma efficacy. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21652541](https://pubmed.ncbi.nlm.nih.gov/21652541/) | 2011 | Preclinical (in vitro) | Clin Cancer Res | Vorinostat induces apoptosis in mantle cell lymphoma through acetylation of proapoptotic BH3-only gene promoters. This supports biological plausibility for B-cell lymphoid cancers but is not a study of the predicted disease. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021991 | ZOLINZA (Merck Sharp & Dohme LLC) | Capsule | Not listed in the data compiled (status: valid) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HDAC inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. Thrombocytopenia and anemia appear among the conditions flagged for caution below. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count (including platelets), serum electrolytes (potassium, calcium, phosphorus), blood glucose, liver and renal function, and ECG/QT monitoring, to be confirmed against the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Conditions flagged for caution** (drug–disease relations in the compiled data, not package-insert text): long QT syndrome (including the familial form), liver disease, gallbladder disease, thrombocytopenia, anemia (including macrocytic), hyperglycemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disorders, pulmonary embolism, and diarrheal disease.
- **Drug Interactions**: 61 interactions are recorded, and all those listed are rated Moderate. The listed ones are mainly glucose-lowering agents, for example:
  - metformin, pioglitazone, glimepiride, glipizide and glyburide
  - the SGLT2 inhibitors canagliflozin, dapagliflozin and empagliflozin
  - the GLP-1 agonists semaglutide, dulaglutide and exenatide
  - the DPP-4 inhibitors linagliptin and alogliptin
  - acarbose and human insulin

  Blood glucose should be monitored closely if vorinostat is combined with these drugs.
- Package-insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for the authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial or publication in the compiled data studies vorinostat in primary cutaneous B-cell lymphoma, so the evidence level is L5. The high model score and the preclinical B-cell lymphoma data support further investigation but do not justify clinical development yet.

**To proceed, the following is needed:**
- Disease-specific preclinical data in primary cutaneous B-cell lymphoma models, or case series and early-phase clinical data in this population
- Confirmed mechanism-of-action data for vorinostat
- Package-insert warnings and contraindications, with particular attention to QT prolongation, thrombocytopenia, thromboembolism and glucose effects
- A dosing and monitoring plan for this population, including management of glucose-lowering drug interactions

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


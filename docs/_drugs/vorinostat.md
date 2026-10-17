---
layout: default
title: Vorinostat
parent: Moderate Evidence (L3-L4)
nav_order: 1296
evidence_level: L3
indication_count: 2
last_modified_at: 2026-10-14
description: "Vorinostat: predicted new indication Primary cutaneous B-cell lymphoma (evidence level L3). Approved use: Primary cutaneous T-cell lymphoma (including primary cutaneous T-cell…"
monitor_inn: "VORINOSTAT"
predicted_indications: ["primary cutaneous B-cell lymphoma"]
---

# Vorinostat
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **2** 
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

# Vorinostat: From Cutaneous T-Cell Lymphoma to Primary Cutaneous B-Cell Lymphoma

## One-Sentence Summary

Vorinostat is an oral HDAC inhibitor, originally used to treat cutaneous T-cell lymphoma (CTCL).
The TxGNN model predicts it may be effective for **primary cutaneous B-cell lymphoma (PCBCL)**, but evidence is thin: the **4 clinical trials** compiled are general lymphoma or supportive studies, and the only **1 publication** is a preclinical mantle cell lymphoma study.
A second prediction, **Sezary syndrome**, is much better supported, but it is essentially within the original CTCL disease family rather than a true new indication (see the end of this report).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary cutaneous T-cell lymphoma (including primary cutaneous T-cell non-Hodgkin lymphoma) |
| Predicted New Indication | Primary cutaneous B-cell lymphoma |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L3 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 1 |
| Recommended Decision | Hold (research question only) |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for vorinostat is not available in the data compiled for this report. Based on known class information, vorinostat is a histone deacetylase (HDAC) inhibitor. HDAC inhibition causes hyperacetylation of histone and non-histone proteins, leading to cell-cycle arrest and apoptosis in malignant lymphocytes.

Both CTCL and PCBCL are lymphomas that primarily involve the skin, which gives a plausible biological connection. Preclinical work shows vorinostat induces apoptosis in mantle cell lymphoma (an aggressive B-cell neoplasm) by acetylating proapoptotic BH3-only gene promoters, supporting activity in B-cell malignancies in general.

However, there is no direct evidence in PCBCL. The very high TxGNN score is a computational prediction and is likely driven by similarity to the approved CTCL indication. It should not be read as proof of efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01567709](https://clinicaltrials.gov/study/NCT01567709) | Phase 1 | Completed | 34 | Alisertib plus vorinostat in relapsed Hodgkin, B-cell non-Hodgkin and peripheral T-cell lymphoma; combination safety and dose-finding, no PCBCL-specific efficacy conclusion |
| [NCT00045006](https://clinicaltrials.gov/study/NCT00045006) | Phase 1 | Completed | Not reported | Oral vorinostat dose-finding in advanced solid tumors and hematologic malignancies; general safety/PK only |
| [NCT00499811](https://clinicaltrials.gov/study/NCT00499811) | Phase 1 | Completed | 15 | Vorinostat in solid tumors and lymphomas with hepatic dysfunction; informs dosing and safety only |
| [NCT01789255](https://clinicaltrials.gov/study/NCT01789255) | Phase 2 | Completed | 12 | Vorinostat with tacrolimus/methotrexate for graft-versus-host disease prophylaxis after transplant; different clinical setting, not relevant to PCBCL efficacy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21652541](https://pubmed.ncbi.nlm.nih.gov/21652541/) | 2011 | Preclinical/in vitro study | Clin Cancer Res | Vorinostat induces apoptosis in mantle cell lymphoma through acetylation of proapoptotic BH3-only gene promoters |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021991 | ZOLINZA (Merck Sharp & Dohme LLC) | Capsule | Not listed in the data compiled (status: cancelled) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/epigenetic therapy (HDAC inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (thrombocytopenia and anemia appear among the knowledge-graph contraindication signals) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with platelets, blood glucose, electrolytes (potassium, calcium, phosphorus), liver and renal function, ECG/QT |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindication/caution signals (from the knowledge graph, not label text)**: long QT syndrome (including familial), liver disease, gallbladder disease, thrombocytopenia, anemia (including macrocytic), hyperglycemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disorders, pulmonary embolism, diarrheal disease.
- **Drug Interactions**: 61 known interactions, all of those shown rated Moderate. The listed ones are largely antidiabetic agents, including metformin, pioglitazone, glimepiride, glipizide, glyburide, insulin, semaglutide, exenatide, and SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin). Blood glucose should be monitored if co-administered.

Package insert warnings and contraindications were not available in the data compiled; please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study directly tests vorinostat in PCBCL. The trials are general lymphoma or supportive-care studies, and the only publication is preclinical work in mantle cell lymphoma. The high TxGNN score alone is not sufficient evidence. The US license is also cancelled, which limits availability.

**To proceed, the following is needed:**
- Disease-specific preclinical data in PCBCL models or patient-derived cells
- Detailed mechanism-of-action data
- FDA package insert warnings and contraindications
- Clinical data or a pilot study in PCBCL patients
- Confirmation of drug availability given the cancelled US license

---

## Additional Note: Sezary Syndrome (Second Prediction)

Sezary syndrome (TxGNN score 99.07%, Evidence Level **L1**, suggested decision **Proceed with Guardrails**) is a leukemic variant of CTCL, so this is essentially an on-label or near-label population rather than true repurposing.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01728805](https://clinicaltrials.gov/study/NCT01728805) | Phase 3 | Completed | 372 | MAVORIC: mogamulizumab vs vorinostat in previously treated MF/SS; vorinostat was the less effective arm |
| [NCT00091559](https://clinicaltrials.gov/study/NCT00091559) | Phase 2 | Completed | 74 | Pivotal single-arm study of oral vorinostat in advanced refractory CTCL |
| [NCT00601718](https://clinicaltrials.gov/study/NCT00601718) | Phase 1/2 | Completed | 29 | Vorinostat plus R-ICE in relapsed lymphoid malignancies or untreated T-cell/mantle cell lymphoma |

Key literature includes the MAVORIC randomized phase 3 trial ([30100375](https://pubmed.ncbi.nlm.nih.gov/30100375/), Lancet Oncol, 2018) and reviews of vorinostat in CTCL ([17594194](https://pubmed.ncbi.nlm.nih.gov/17594194/), [17940636](https://pubmed.ncbi.nlm.nih.gov/17940636/), 2007).

**Guardrails:** vorinostat was inferior to mogamulizumab for progression-free survival in MAVORIC; the US license is cancelled; and the 61 known interactions and class toxicities (GI effects, thrombocytopenia, thromboembolism, QT effects) require monitoring.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


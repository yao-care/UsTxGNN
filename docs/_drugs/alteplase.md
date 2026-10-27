---
layout: default
title: Alteplase
parent: Moderate Evidence (L3-L4)
nav_order: 270
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
description: "Alteplase: predicted new indication Posterolateral myocardial infarction (evidence level L4). Approved use: Myocardial infarction, pulmonary embolism, stroke"
monitor_inn: "ALTEPLASE"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
---

# Alteplase
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

## Alteplase: From Myocardial Infarction to Posterolateral Myocardial Infarction
{: .text-alpha }

## One-Sentence Summary

Alteplase is a recombinant tissue plasminogen activator, originally used to dissolve blood clots in conditions such as myocardial infarction, pulmonary embolism and stroke.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but this is a subtype of an existing indication and not a true new use, and **no clinical trials or publications** specific to it were found.
Among the other predictions, **thrombophilia** has the most support (**1 clinical trial** and **20 publications**, mostly case reports).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myocardial infarction, pulmonary embolism, stroke (from the knowledge graph; the US license record has no indication text) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (the single license is cancelled) |
| Number of NDAs | 1 (BLA103172) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Alteplase is a recombinant tissue plasminogen activator. It converts plasminogen to plasmin, which breaks down fibrin clots. Detailed mechanism of action data is not available in the compiled data, so this description rests on the drug's known class behavior.

Posterolateral myocardial infarction is an anatomical subtype of myocardial infarction, which is already an original indication. The mechanism is the same: dissolving the clot that blocks a coronary artery. The high score (0.998) most likely reflects how closely the disease sits to myocardial infarction in the knowledge graph, not new evidence. This is therefore not a true repurposing candidate.

The same applies to the posteroinferior and septal myocardial infarction predictions (scores 99.79% and 99.77%). Predictions such as heparin cofactor 2 deficiency, antithrombin deficiency type 2, factor 5 excess, and congenital coronary artery anomaly have weak mechanistic rationale and no clinical evidence (L5). Alteplase could dissolve an acute clot in these patients, but it does not correct the underlying defect.

## Clinical Trial Evidence

Currently no related clinical trials are registered for posterolateral myocardial infarction. The only registered trial in the compiled data is for a lower-ranked prediction, thrombophilia:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05540834](https://clinicaltrials.gov/study/NCT05540834) | Phase 2 | Recruiting | 70 | Viscoelastic-test-guided tPA dosing in critically ill patients with pro-thrombotic acute respiratory failure (COVID and non-COVID). Link to thrombophilia is indirect, and no results are available. |

## Literature Evidence

No publications were found for posterolateral myocardial infarction. The closest related publications are for septal myocardial infarction and coronary stenosis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8299637](https://pubmed.ncbi.nlm.nih.gov/8299637/) | 1993 | RCT | European Heart Journal | Alteplase vs placebo in 80 patients with chest pain at rest (coronary stenosis prediction) |
| [1782951](https://pubmed.ncbi.nlm.nih.gov/1782951/) | 1991 | RCT | European Heart Journal | Alteplase vs placebo in 36 patients with refractory unstable angina before angioplasty |
| [8721695](https://pubmed.ncbi.nlm.nih.gov/8721695/) | 1996 | Cohort | Catheterization and Cardiovascular Diagnosis | Lesion-directed alteplase plus intracoronary heparin in 45 patients with unstable angina and coronary thrombus |
| [8763515](https://pubmed.ncbi.nlm.nih.gov/8763515/) | 1996 | Cohort | Revista Portuguesa de Cardiologia | Effect of late alteplase thrombolysis on left ventricular function in myocardial infarction |
| [22094974](https://pubmed.ncbi.nlm.nih.gov/22094974/) | 2012 | Cohort | Journal of Thrombosis and Thrombolysis | Pilot study of early PCI after half-dose alteplase in Chinese STEMI patients |
| [2118432](https://pubmed.ncbi.nlm.nih.gov/2118432/) | 1990 | Review | Circulation | Review of thrombolytic treatment in acute myocardial infarction |
| [41876387](https://pubmed.ncbi.nlm.nih.gov/41876387/) | 2026 | Case report | Catheterization and Cardiovascular Interventions | Systemic thrombolytic resistance in antithrombin III deficiency, rescued by catheter-directed thrombolysis (thrombophilia prediction) |
| [37754803](https://pubmed.ncbi.nlm.nih.gov/37754803/) | 2023 | Case report | Journal of Cardiovascular Development and Disease | Pulmonary embolism mimicking anteroseptal STEMI, treated with thrombectomy and catheter-directed thrombolysis |

Most of the literature concerns acute myocardial infarction or case reports in thrombotic conditions. None directly tests alteplase for the predicted indications. The 1990s trials also predate modern PCI and antiplatelet practice, and unstable angina trials have generally not shown clear benefit from thrombolysis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103172 (cancelled) | Cathflo Activase (Genentech, Inc.) | Injection, powder, lyophilized, for solution | Not available in the compiled data |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified, of which 20 are shown in the compiled data (Moderate and Major levels). Major interactions with bleeding relevance include:
  - Anticoagulants and antithrombotics: fondaparinux, apixaban, anisindione, abciximab
  - Kinase inhibitor: acalabrutinib
  - Radiopharmaceuticals and chelator: ibritumomab tiuxetan, tositumomab (including I-131), deferasirox
  - Moderate interactions include acetylsalicylic acid, ibuprofen, ketorolac, aminocaproic acid, aprotinin, fluvoxamine, fosinopril, and the anorectics fenfluramine, dexfenfluramine and sibutramine.
- Bleeding risk and the altered coagulation seen in inherited thrombophilias, including heparin resistance and thrombolytic resistance in antithrombin deficiency, complicate any safety assessment.

Please refer to the package insert for warnings and contraindications, which are not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions (posterolateral, posteroinferior and septal myocardial infarction) are subtypes of an indication alteplase already covers. They offer no genuine repurposing opportunity and have no subtype-specific evidence. The more distinct predictions are supported only by case reports or have no evidence at all, so the highest evidence level reached is L3 for thrombophilia and coronary stenosis, with L4 or L5 for the rest.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of whether the myocardial infarction subtypes should be treated as new indications or as already covered by the existing myocardial infarction indication
- For thrombophilia, controlled clinical data and clarification of whether NCT05540834 is relevant
- Review of the cancelled license status (Cathflo Activase is a catheter-clearance product, not a thrombolytic for myocardial infarction), and of other alteplase products on the US market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


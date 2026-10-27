---
layout: default
title: Defibrotide
parent: Model Prediction Only (L5)
nav_order: 579
evidence_level: L5
indication_count: 10
monitor_inn: "DEFIBROTIDE"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "thrombotic thrombocytopenic purpura", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "congenital factor V deficiency", "fetal and neonatal alloimmune thrombocytopenia", "thrombocytopenic purpura"]
last_modified_at: 2026-10-14
description: "Defibrotide: predicted new indication Pseudo-von Willebrand disease (evidence level L5). Approved use: Hepatic veno-occlusive disease"
---

# Defibrotide
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

## Defibrotide: From Hepatic Veno-Occlusive Disease to Pseudo-von Willebrand Disease
{: .text-alpha }

## One-Sentence Summary

Defibrotide was originally used to treat hepatic veno-occlusive disease (VOD), including the form associated with immunodeficiency.
The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction.
The most evidence-supported related direction in the data compiled for this report is **thrombotic thrombocytopenic purpura (TTP) / transplant-associated thrombotic microangiopathy (TA-TMA)**, supported by **8 publications**, mostly small and older reports.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic veno-occlusive disease; hepatic veno-occlusive disease-immunodeficiency syndrome (from the knowledge graph; the US license record has no indication text) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Defibrotide is an oligonucleotide with endothelial-protective, profibrinolytic and antithrombotic activity. These properties explain its use in hepatic VOD, a disease of endothelial injury and microvascular thrombosis.

For pseudo-von Willebrand disease, the rationale is weak. It is a platelet-type bleeding disorder caused by a gain-of-function defect in the platelet receptor GP1BA. No plausible mechanism is established by which defibrotide would correct this defect. Using an antithrombotic agent in a bleeding disorder also raises a safety concern. The high score (0.999) most likely reflects network proximity in the knowledge graph rather than a real therapeutic link.

The same applies to the other top-ranked predictions: primary platelet release disorder, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defect, constitutional thrombocytopenia, congenital factor V deficiency and fetal/neonatal alloimmune thrombocytopenia. All are prediction-only with no supporting studies, and several raise bleeding-risk concerns.

The only predictions with a plausible biological link and some published evidence are **thrombotic thrombocytopenic purpura** (rank 4, score 99.71%) and the broader **thrombocytopenic purpura** category (rank 10, score 99.22%). Defibrotide's endothelial protection is plausible in microangiopathic disease, particularly TA-TMA, where endothelial injury plays a central role. Evidence is stronger for TA-TMA than for classical autoimmune TTP (ADAMTS13 deficiency), where plasma exchange, caplacizumab and rituximab are standard.

## Clinical Trial Evidence

Currently no related clinical trials registered for pseudo-von Willebrand disease, nor for any of the other top-ranked predictions, including TTP.

## Literature Evidence

No literature is available for pseudo-von Willebrand disease. The table below lists the publications for the TTP prediction (rank 4); the same set applies to the broader thrombocytopenic purpura category (rank 10), minus the 1986 renal failure study.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10775024](https://pubmed.ncbi.nlm.nih.gov/10775024/) | 2000 | Case report/small series | Clin Appl Thromb Hemost | Defibrotide used in recurrent TTP, a condition where relapses remain a treatment challenge |
| [11960280](https://pubmed.ncbi.nlm.nih.gov/11960280/) | 2002 | Case series/cohort | Bone Marrow Transplant | Defibrotide described as a promising treatment for TTP in bone marrow transplant patients |
| [3754836](https://pubmed.ncbi.nlm.nih.gov/3754836/) | 1986 | Small clinical study | Haemostasis | Effects of defibrotide in acute renal failure due to thrombotic microangiopathy |
| [37001283](https://pubmed.ncbi.nlm.nih.gov/37001283/) | 2023 | In vitro/preclinical | Thromb Res | Defibrotide mitigated endothelial cell injury induced by plasma from COVID-19 patients and related vasculopathies, including TTP and HSCT-associated VOD |
| [7896218](https://pubmed.ncbi.nlm.nih.gov/7896218/) | 1994 | Case report (adverse event) | Haematologica | TTP occurring after defibrotide therapy, a conflicting safety signal |
| [30305540](https://pubmed.ncbi.nlm.nih.gov/30305540/) | 2018 | Review | Rinsho Ketsueki | Management of transplant-associated thrombotic microangiopathy |
| [17603513](https://pubmed.ncbi.nlm.nih.gov/17603513/) | 2007 | Review | Bone Marrow Transplant | Diagnosis and treatment of TA-TMA; progress hampered by lack of consensus definition |
| [19228075](https://pubmed.ncbi.nlm.nih.gov/19228075/) | 2009 | Review | Drugs | TMA in HSCT: incidence 0.5–76%, mortality 60–90% despite treatment |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208114 | DEFITELIO (Jazz Pharmaceuticals, Inc.) | Injection, solution | Not listed in the data compiled for this report (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. The sample reviewed includes these main ones:
  - **Major**: acetylsalicylic acid, deferasirox, ibritumomab tiuxetan, tositumomab (including I-131), abciximab, acalabrutinib, fondaparinux, alteplase, anagrelide. Most involve additive bleeding risk with antiplatelet, anticoagulant or thrombolytic agents.
  - **Moderate**: dexfenfluramine, fenfluramine, sibutramine, ketorolac (including ophthalmic), ibuprofen, fluvoxamine, topical diclofenac, celecoxib, omega-3 fatty acids.
- **Class-level concern**: Defibrotide's antithrombotic and profibrinolytic activity could aggravate bleeding in the bleeding disorders it is predicted for. A 1994 report also describes TTP occurring after defibrotide therapy.

Please refer to the package insert for warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (pseudo-von Willebrand disease) rests on a model score alone, with no trials or literature. It has no plausible mechanism and a bleeding-risk concern. Of the predictions reviewed, only TTP/TA-TMA has a biologically plausible link, and its evidence is limited to small, older, uncontrolled reports. It could be framed as a research question, not a go decision.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- For any follow-up, a narrowed research question focused on TA-TMA, not classical autoimmune TTP or the bleeding disorders
- A review of the 1994 report of TTP after defibrotide, and a bleeding-risk assessment
- Clarification of why the US license was cancelled and whether a route and formulation are still available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


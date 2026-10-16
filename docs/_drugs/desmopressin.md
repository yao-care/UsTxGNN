---
layout: default
title: Desmopressin
parent: Model Prediction Only (L5)
nav_order: 586
evidence_level: L5
indication_count: 7
monitor_inn: "DESMOPRESSIN"
predicted_indications: ["congenital prothrombin deficiency", "inherited thrombophilia", "Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Scott syndrome", "flood factor deficiency"]
last_modified_at: 2026-10-14
description: "Desmopressin: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Hereditary von Willebrand disease"
---

# Desmopressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Desmopressin: From Von Willebrand Disease to Congenital Prothrombin Deficiency

## One-Sentence Summary

Desmopressin was originally used to treat von Willebrand disease, hemophilia A (mild forms), and nocturnal enuresis.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but **0 clinical trials** and only **1 publication (a 1993 review)** are available, and the mechanism does not support the prediction.
This top-ranked prediction is most likely a network-proximity artefact, and the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary von Willebrand disease; nocturnal enuresis; hemophilia (from the knowledge graph; no approved indication text was available in the US license records) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 11 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, desmopressin is a synthetic vasopressin analogue. It acts through V2 receptor signalling to release von Willebrand factor (VWF) and factor VIII (FVIII) from endothelial stores. This explains its use in von Willebrand disease and mild hemophilia A.

Congenital prothrombin (factor II) deficiency is a different problem. Desmopressin has no known way to raise prothrombin levels. The high TxGNN score most likely reflects the disease's proximity to other bleeding disorders in the knowledge graph rather than a true biological effect. Prothrombin deficiency is normally managed with prothrombin complex concentrate. The prediction is therefore **not mechanistically supported**.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | Overview of rational treatment options for common inherited bleeding disorders (haemophilia A, von Willebrand disease), with comparison of product safety, efficacy and cost. It does not show desmopressin benefit in prothrombin deficiency. |

## US Market Information

All 11 US authorizations are cancelled. The records contain no approved indication text. Up to 5 are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018938 | Desmopressin Acetate (Nordic Pharma) | Solution | Not available |
| NDA019955 | DDAVP (Ferring) | Tablet | Not available |
| ANDA074830 | Desmopressin Acetate (Oceanside) | Solution | Not available |
| ANDA201831 | Desmopressin Acetate (Glenmark) | Tablet | Not available |
| ANDA210223 | Desmopressin Acetate (XGen) | Injection, solution | Not available |

Dosage forms across all authorizations include oral tablets, solutions and injectables.

## Safety Considerations

- **Contraindications / disease associations (knowledge graph, not label text)**: hypertension, coronary artery disease, impaired renal function, cystic fibrosis, allergic and vasomotor rhinitis, pharyngitis, common cold, respiratory tract infection, von Willebrand disease (certain subtypes), dipsogenic diabetes insipidus, polydipsia, and water intoxication.
- **Drug Interactions** (100 interactions recorded; examples):
  - **Major**: corticosteroids including hydrocortisone, dexamethasone, prednisone, prednisolone, triamcinolone, betamethasone, budesonide and beclomethasone.
  - **Moderate**: epinephrine, loperamide, morphine, opium, chlorpropamide.
  - **Minor**: acetylsalicylic acid.
- **Class-related concerns from the literature**: hyponatremia and, rarely, arterial thrombotic events.

Please also refer to the package insert, as the label warnings could not be retrieved for this report.

## Other Predicted Indications (Context)

Six further predictions were reviewed. None has a clinical trial, and none changes the overall decision.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Inherited thrombophilia | 99.44% | L5 | Likely false positive. A pro-hemostatic agent in a prothrombotic state is counter-indicated, and the literature links desmopressin to a thrombotic signal. |
| 3 | Glanzmann thrombasthenia | 99.30% | L4 | Desmopressin cannot restore the missing αIIbβ3 receptor. It is an adjunct with limited, variable efficacy, and case reports show failures. A research question only. |
| 4 | Primary release disorder of platelets | 99.26% | L3 | The most plausible of the group. It can shorten bleeding time, supported by small observational studies and a 2023 review, but there are no randomized trials. |
| 5 | Pseudo-von Willebrand disease | 99.16% | L4 | Likely harmful, because releasing more VWF may worsen platelet clumping and thrombocytopenia. |
| 6 | Scott syndrome | 99.16% | L5 | There is no known effect on scramblase function and no direct evidence. |
| 7 | "Flood factor deficiency" | 99.15% | L4 | The disease name appears to be garbled or mis-mapped. The evidence reflects the existing von Willebrand disease indication. The ontology entry should be checked. |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, congenital prothrombin deficiency, has no clinical trials, one old general review, and no plausible mechanism. There are no currently valid US licenses, and key safety data are missing, which is a blocking data gap.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Ontology check of the mis-mapped "flood factor deficiency" entry
- If any indication is pursued, "primary release disorder of platelets" is the most credible candidate and would need a prospective study. The other candidates should be deprioritized.
- Review of why the model ranks mechanistically implausible or harmful indications so highly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Ferumoxytol
parent: Model Prediction Only (L5)
nav_order: 703
evidence_level: L5
indication_count: 6
monitor_inn: "FERUMOXYTOL"
predicted_indications: ["Plummer-Vinson syndrome", "non-syndromic esophageal malformation", "vitamin B12- and folate-independent constitutional megaloblastic anemia", "severe nonproliferative diabetic retinopathy", "esophageal ulcer", "esophageal disease"]
---

# Ferumoxytol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ferumoxytol: From Iron Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Ferumoxytol is an intravenous iron replacement product, originally used to treat iron deficiency anemia.
The TxGNN model predicts it may be useful for **Plummer-Vinson syndrome**, but **no clinical trials and no publications** directly support this prediction.
The link rests on indirect reasoning, because the anemia component of the syndrome overlaps with the drug's existing indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia (also hypochromic, deficiency and microcytic anemia, based on the knowledge graph indication edges) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 (no trials or literature for this indication; mechanistic reasoning only) |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferumoxytol is an intravenous iron oxide nanoparticle product. Its efficacy in iron deficiency anemia is established, and mechanistically it could address the iron deficiency component of Plummer-Vinson syndrome.

Plummer-Vinson syndrome combines iron deficiency anemia, esophageal webs and difficulty swallowing. Replacing iron may correct the anemia, but it is not expected to treat the esophageal webs, which usually need endoscopic dilation.

The high TxGNN score most likely reflects the overlap with iron deficiency anemia, which is already an approved target. It is therefore not a true repurposing signal and does not point to new biology.

**Other predictions reviewed (none supported by evidence):**

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Non-syndromic esophageal malformation | 99.86% | No plausible mechanism. These are structural defects needing surgery. |
| Vitamin B12- and folate-independent constitutional megaloblastic anemia | 99.85% | Not caused by iron deficiency. Iron could risk overload if stores are normal. |
| Severe nonproliferative diabetic retinopathy | 99.65% | No mechanistic rationale. Iron-related oxidative stress may even harm the retina. |
| Esophageal ulcer | 99.58% | Iron could only treat anemia from blood loss, not the ulcer itself. |
| Esophageal disease | 99.51% | Existing evidence concerns ferumoxytol as an imaging agent, not a therapy (see below). |

## Clinical Trial Evidence

There are no registered clinical trials for Plummer-Vinson syndrome. The only trials found relate to the broader "esophageal disease" prediction, and all of them use ferumoxytol as an MRI imaging agent rather than as a treatment:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Phase 1 | Completed | 45 | Ferumoxytol MRI to assess tumor drug deposition and tumor-associated macrophages in patients given nanoliposomal irinotecan (MM-398). Not specific to esophageal disease. |
| [NCT02857218](https://clinicaltrials.gov/study/NCT02857218) | Early Phase 1 | Withdrawn | 0 | Pilot of ferumoxytol-enhanced MRI for lymph node imaging in locally advanced esophageal cancer. Diagnostic use, no data. |
| [NCT02689401](https://clinicaltrials.gov/study/NCT02689401) | Phase 1 | Withdrawn | 0 | Iron oxide MRI for lymph node staging in esophageal cancer. Diagnostic use, no data. |
| [NCT02253602](https://clinicaltrials.gov/study/NCT02253602) | Not applicable | Completed | 41 | Innovative MRI techniques to improve treatment stratification in esophageal cancer. The role of ferumoxytol is unclear. |

## Literature Evidence

No literature directly supports Plummer-Vinson syndrome. One publication was found for the broader esophageal prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24824854](https://pubmed.ncbi.nlm.nih.gov/24824854/) | 2014 | Preclinical imaging study | Molecular Imaging | Fluorescent nanoparticle imaging to evaluate immune cell modulation in esophageal dysplasia. A diagnostic imaging approach, not a therapy. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022180 | Feraheme (AMAG Pharmaceuticals) | Injection | Not available; status cancelled |
| ANDA206604 | Ferumoxytol (Sandoz) | Injection | Not available; status cancelled |
| NDA219868 | FeraBright (Azurity Pharmaceuticals) | Injection | Not available; status cancelled |

## Safety Considerations

- **Drug Interactions** (5 found, from DDInter):
  - **Major:** Dimercaprol
  - **Moderate:** Iron, ferrous fumarate, ferrous gluconate, chloramphenicol

The data compiled for this report do not include package insert warnings or contraindications. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no direct clinical or literature support. The score likely reflects the overlap with the already approved iron deficiency anemia indication, so it is not a true repurposing signal. All three US authorizations are cancelled, and the label safety data is missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Clarification of the US marketing status, since all authorizations are cancelled
- Any clinical data on iron replacement in Plummer-Vinson syndrome, and a clear case that it adds value beyond the existing anemia indication
- Confirmation of route compatibility, which is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


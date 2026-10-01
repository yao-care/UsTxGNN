---
layout: default
title: Eptifibatide
parent: Model Prediction Only (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
---

# Eptifibatide
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

# Eptifibatide: From Acute Coronary Syndrome to Rheumatoid Arthritis

## One-Sentence Summary

Eptifibatide is an injectable GP IIb/IIIa (platelet aggregation) antagonist, and the literature in the pack describes it as an established treatment for acute coronary syndrome.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but this top-ranked prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.
The pack's best-supported candidate is a different one, **hemoglobinopathy (sickle cell disease)**, with 1 terminated Phase 1/2 trial and 4 publications, described below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license data (acute coronary syndrome, per the literature in the pack) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed licenses shown are generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eptifibatide blocks the GP IIb/IIIa receptor on platelets and so prevents platelet aggregation. Currently, detailed mechanism of action data is not available in the DrugBank record. The description above comes from the pack's rationale text and literature.

Platelets are known to contribute to synovial inflammation, which is the only loose link between an antiplatelet drug and rheumatoid arthritis. No data connect this mechanism to the disease, and there are no trials or publications. A high model score alone is not clinical evidence. Bleeding risk is also a concern for a chronic inflammatory disease that requires long-term treatment.

**A note on the other predictions.** The sickle cell-related predictions have a clearer mechanistic story. Platelet activation and adhesion contribute to microvascular occlusion and pain crises in sickle cell disease. Eptifibatide has been tested in small studies in this setting (see the evidence sections below). Several other predictions, such as the 16p partial deletion, look like knowledge graph artifacts with no plausible mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

For reference, the pack lists one trial for the related prediction **hemoglobinopathy**:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00834899](https://clinicaltrials.gov/study/NCT00834899) | Phase 1/2 | Terminated | 13 | Randomized, double-blind, placebo-controlled safety study of eptifibatide for acute pain episodes in sickle cell disease. Stopped early, so it is underpowered and cannot support efficacy conclusions. |

---

## Literature Evidence

Currently no related literature available for rheumatoid arthritis.

For reference, the pack lists these publications for **hemoglobinopathy** (sickle cell disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/) | 2013 | Pilot randomized study | Thromb Res | Evaluated safety and efficacy of eptifibatide in SCD patients during acute painful episodes |
| [17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/) | 2007 | Phase 1 | Br J Haematol | Safety and pharmacodynamics in 4 steady-state sickle cell anaemia patients, based on the rationale that platelet reactivity and CD40L contribute to the disease |
| [29322543](https://pubmed.ncbi.nlm.nih.gov/29322543/) | 2018 | Secondary analysis of trial | Am J Hematol | Effect of eptifibatide on inflammation biomarkers during acute pain episodes (no abstract available) |
| [22156199](https://pubmed.ncbi.nlm.nih.gov/22156199/) | 2012 | In vitro model | J Clin Invest | Microfluidic model of microvascular occlusion and thrombosis in hematologic diseases such as SCD |

The pack also links PMID 24678072 (eptifibatide tolerability in acute coronary syndrome) to sickle cell-hemoglobin C disease. It appears to be unrelated to that disease, and its listed year (2005) and truncated title do not match the PMID, so the citation should be verified before any use.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206127 | Eptifibatide (Eugia US LLC) | Injection | Not listed in the data |
| ANDA208554 | Eptifibatide (Baxter Healthcare Company) | Injection | Not listed in the data |
| ANDA203258 | Eptifibatide (Mylan Institutional LLC) | Injection, solution | Not listed in the data |
| ANDA213081 | Eptifibatide (Avenacy Inc.) | Injection, solution | Not listed in the data |

The pack reports 20 licenses in total. Only these four distinct products are shown, since ANDA206127 appears twice in the list.

---

## Safety Considerations

- **Bleeding risk**: A bleeding risk is flagged in the pack's rationale for a chronic inflammatory disease, and it needs a dedicated safety assessment before any further progression.

Please refer to the package insert for other safety information. The FDA package insert warnings and contraindications are not yet available in the pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rheumatoid arthritis prediction has a very high model score (99.99%) but no trials, no literature, and only a speculative mechanism, so it is Level L5. Bleeding risk in a chronic condition adds to the concern.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA) from DrugBank
- Any preclinical or clinical evidence linking GP IIb/IIIa inhibition to rheumatoid arthritis, or a decision to prioritize the sickle cell / hemoglobinopathy candidate (L2, still a research question because trial NCT00834899 was terminated at 13 patients)
- A bleeding-risk assessment for the intended patient population and dosing setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


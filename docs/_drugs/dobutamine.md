---
layout: default
title: Dobutamine
parent: Model Prediction Only (L5)
nav_order: 616
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine: From Cardiac Inotropic Support to Alopecia

## One-Sentence Summary

Dobutamine is an intravenous beta-1 adrenergic inotrope, used in hospitals to support heart function in cardiac decompensation.
The TxGNN model predicts it may be effective for **alopecia**, but this rests on the model score alone, with **0 clinical trials** and only **2 unrelated case reports** in the retrieved literature.
The prediction most likely reflects graph proximity to minoxidil-related cardiovascular nodes, not a real therapeutic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inotropic support in cardiac decompensation (general labeling knowledge; the US license records provided do not state an indication) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 13 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Dobutamine is a beta-1 selective adrenergic agonist given by intravenous infusion. Its efficacy in cardiac inotropic support is established, but it has no known effect on hair follicle cycling.

Mechanistically, the link to alopecia is weak. Alopecia is a hair-cycle disorder, and in its autoimmune forms (such as alopecia areata) it is driven by immune pathways like JAK/IFN-gamma. Dobutamine has no known action on these pathways.

The very high TxGNN score (99.85%) most likely comes from the knowledge graph placing dobutamine near minoxidil-related cardiovascular nodes. Minoxidil is a known hair-growth drug, but that proximity does not show dobutamine would work. The other nine predicted indications (for example hypotrichosis, glaucoma, Raynaud disease, migraine) are also unsupported by mechanism or evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case report (veterinary) | Journal of Veterinary Cardiology | A cat with heart failure from minoxidil intoxication. Dobutamine was used for hypotension as supportive cardiac care, not to treat hair loss. |
| [17505274](https://pubmed.ncbi.nlm.nih.gov/17505274/) | 2007 | Case report | Pediatric Emergency Care | Acute colchicine poisoning in a child. Hair loss appears only as a recovery-phase symptom of the poisoning, and the report does not support dobutamine for alopecia. |

Neither paper shows dobutamine treating alopecia.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074086 (HF Acquisition Co LLC, DBA HealthFirst) | Dobutamine | Injection, solution, concentrate | Not stated in the record |
| NDA020255 (HF Acquisition Co LLC, DBA HealthFirst) | Dobutamine Hydrochloride | Injection | Not stated in the record |
| ANDA074086 (Hospira, Inc.) | Dobutamine | Injection, solution, concentrate | Not stated in the record |
| NDA020201 (Hospira, Inc.) | Dobutamine in Dextrose | Injection, solution | Not stated in the record |

All marketed forms are injectable. No topical or oral form appears in the records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5), with no trials and no supporting literature. Dobutamine has no plausible mechanism for hair growth, and it is only available as an intravenous hospital drug, which is a poor fit for a chronic cosmetic or dermatological condition.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and package insert warnings and contraindications, to complete the safety screen
- Any mechanistic or preclinical evidence linking beta-1 adrenergic signaling to hair follicle biology
- A route-compatibility assessment, since only injectable forms exist
- Without such evidence, deprioritize this candidate. The other predicted indications (rank 2–10) are also L5 and on Hold.

*This report is for research reference only and does not constitute medical advice. Predicted repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


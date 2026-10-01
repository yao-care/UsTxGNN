---
layout: default
title: Ruxolitinib
parent: Model Prediction Only (L5)
nav_order: 1140
evidence_level: L5
indication_count: 10
---

# Ruxolitinib
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

# Ruxolitinib: From Myeloproliferative Neoplasms to Uterine Corpus Perivascular Epithelioid Cell Tumor (PEComa)

## One-Sentence Summary

Ruxolitinib is an oral JAK1/2 inhibitor marketed in the US as Jakafi (tablet) and Opzelura (topical cream).
The TxGNN model predicts it may be effective for **uterine corpus perivascular epithelioid cell tumor**, with a very high score (99.73%).
However, this prediction has **0 clinical trials** and **0 publications** behind it, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (all approved-indication fields are empty) |
| Predicted New Indication | Uterine corpus perivascular epithelioid cell tumor |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Based on general knowledge, ruxolitinib inhibits JAK1 and JAK2 and thereby blocks JAK-STAT signaling downstream of cytokines such as IFN-γ and IL-6. It is marketed as both an oral tablet and a topical cream.

The link to the predicted indication is weak. PEComa is driven mainly by loss of TSC1/TSC2 and hyperactivation of mTOR, not by JAK-STAT signaling. No direct JAK1/2 rationale is documented in the provided data. The high TxGNN score probably reflects proximity in the knowledge graph to related diseases rather than a validated mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA215309 | OPZELURA (Incyte Corporation) | Cream (topical) |
| NDA202192 | JAKAFI (Incyte Corporation) | Tablet (oral) |

NDA202192 appears in 4 of the 5 records provided. Approved-indication text is empty for all of them.

---

## Cytotoxicity

Ruxolitinib is a targeted kinase inhibitor, not a conventional cytotoxic chemotherapy. The Evidence Pack has no toxicity data, so only general points are given here.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (JAK1/2 inhibitor) |
| Myelosuppression Risk | Cytopenias (thrombocytopenia, anemia, neutropenia) are a recognized class of effect; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential; other items per package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it (L5). The disease is mTOR/TSC-driven and no JAK-STAT rationale is documented, so the high model score should not be read as clinical support.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Any preclinical evidence that JAK-STAT inhibition matters in PEComa

**Other predictions in the pack:** two candidates are much better supported than this one.
- **Hemophagocytic syndrome associated with an infection** (rank 10, L3). It has multiple ruxolitinib clinical reports, mainly in EBV-associated HLH. There is also a Phase 1 trial (NCT07424222, not yet recruiting) of ruxolitinib for immune effector cell-associated HLH-like syndrome, and a Phase 3 trial that includes a ruxolitinib arm (NCT04424056, COVID-19-associated hyperinflammation). Most of the evidence is retrospective or case-level, and no completed randomized trial was found.
- **Liposarcoma** (rank 5, L4). It has preclinical evidence that JAK-STAT signaling controls cancer stem cell properties and chemotherapy resistance in myxoid liposarcoma. It is still a research question only.

If the goal is to advance a candidate, the infection-associated hemophagocytic syndrome prediction is the more promising one to pursue.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


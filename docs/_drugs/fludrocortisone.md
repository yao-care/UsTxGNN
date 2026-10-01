---
layout: default
title: Fludrocortisone
parent: Model Prediction Only (L5)
nav_order: 716
evidence_level: L5
indication_count: 8
---

# Fludrocortisone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Fludrocortisone: From Adrenal Insufficiency to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Fludrocortisone is a mineralocorticoid with modest glucocorticoid activity. It is marketed as an oral tablet in the US, and its usual use is replacement therapy in adrenal insufficiency, though no approved indication text was supplied in the Evidence Pack.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma** with a very high score, but there are **0 clinical trials** and **1 publication**, a 1967 historical report that does not test this use.
The prediction rests on knowledge-graph proximity rather than documented evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (approved indication text is empty in all licenses) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (the pack assigned L4, but the only citation is not relevant to this indication) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 16 (ANDA generic approvals) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Fludrocortisone is a mineralocorticoid with modest glucocorticoid activity. Systemic corticosteroids have only a nonspecific lymphocyte-suppressive effect, and that is the most that can be said mechanistically for cutaneous T-cell lymphoma.

There is no documented rationale linking fludrocortisone to this lymphoma. The score of 0.996 reflects graph proximity in the TxGNN knowledge graph, not a demonstrated pharmacological link. The single citation is a 1967 paper on pathergic granulomatosis. It appears to be a historical, case-level report and does not appear to test fludrocortisone in cutaneous T-cell lymphoma.

The other top-ranked predictions (cystic teratoma, dermoid cysts, exostosis) have no plausible mineralocorticoid mechanism either, which suggests the high scores are graph artifacts. The one partially supported prediction is **eye disease** (rank 6). It has preclinical evidence of anti-inflammatory and neuroprotective effects in retinal degeneration (PMID 34509498) and a Phase 1B safety study in geographic atrophy (PMID 36161841). It is a separate indication and is not evaluated further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6028675](https://pubmed.ncbi.nlm.nih.gov/6028675/) | 1967 | Case report / historical report | Archives of Dermatology | "Pathergic granulomatosis." No abstract is available. It does not appear to evaluate fludrocortisone in cutaneous T-cell lymphoma. |

---

## US Market Information

The Evidence Pack lists 16 licenses in total. Five are shown below. All are oral tablets, and the approved indication text is empty in every record.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| ANDA040431 | Fludrocortisone Acetate | Tablet | NCS HealthCare of KY, LLC dba Vangard Labs |
| ANDA215279 | Fludrocortisone Acetate | Tablet | Novitium Pharma LLC |
| ANDA219251 | Fludrocortisone Acetate | Tablet | Viona Pharmaceuticals Inc |
| ANDA215279 | Fludrocortisone Acetate | Tablet | Major Pharmaceuticals |
| ANDA040431 | Fludrocortisone Acetate | Tablet | Amneal Pharmaceuticals of New York LLC |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no supporting literature, and no plausible mechanism. The score reflects knowledge-graph structure rather than biology. Nothing here justifies advancing fludrocortisone for primary cutaneous T-cell lymphoma.

**To proceed, the following is needed:**
- The package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence that fludrocortisone acts on cutaneous T-cell lymphoma. If none exists, the prediction should be deprioritized.
- Consideration of the better-supported **eye disease** prediction as a separate research question. It would need a specific ocular condition, such as retinal degeneration or geographic atrophy, defined endpoints, and confirmation of the patient population in PMID 36161841.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


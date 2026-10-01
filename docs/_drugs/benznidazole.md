---
layout: default
title: Benznidazole
parent: Model Prediction Only (L5)
nav_order: 446
evidence_level: L5
indication_count: 3
---

# Benznidazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Benznidazole: From Chagas Disease to Congenital Analbuminemia

## One-Sentence Summary

Benznidazole is an oral nitroimidazole antiprotozoal, originally used to treat Chagas disease.
The TxGNN model predicts it may be effective for **congenital analbuminemia**, but there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chagas disease (the license record has no indication text; taken from the drug's known use) |
| Predicted New Indication | Congenital analbuminemia |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license records (both under NDA209570) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Benznidazole is a nitroimidazole antiprotozoal. Its activity is generally understood to depend on activation by parasite nitroreductases, which generate reactive metabolites that damage the parasite.

Congenital analbuminemia is a rare genetic disorder caused by mutations in the albumin gene (*ALB*). No known pathway connects benznidazole to it. The drug does not act on albumin synthesis, and it has no known effect on the underlying genetic defect. The high score (99.51%) is not backed by any trial or publication, so it should be treated as a possible knowledge-graph artifact rather than a real signal.

The other two top predictions show the same pattern. Polyclonal hyperviscosity syndrome and hyperamylasemia both score 99.32% and both have no supporting evidence. Their identical scores suggest a shared graph-neighborhood effect rather than independent signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209570 | Benznidazole (Exeltis USA, Inc.) | Tablet (oral) | Not provided in the record |

The Evidence Pack contains two license records with the same NDA number and identical details. They are shown here as one entry.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There is no mechanistic link, no clinical trial and no publication, so the evidence level is L5. The drug's mechanism and safety data are also missing from the input.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A biologically plausible mechanism linking benznidazole to *ALB* deficiency, or to any predicted indication, backed by at least preclinical evidence
- A literature and trial search in disease-specific sources to confirm that no supporting evidence exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


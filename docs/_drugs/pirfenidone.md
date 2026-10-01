---
layout: default
title: Pirfenidone
parent: Model Prediction Only (L5)
nav_order: 1049
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

Pirfenidone is an oral anti-fibrotic drug. Published literature in the evidence pack notes it was approved in 2014 for idiopathic pulmonary fibrosis, and the label indication text itself was not available.
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic pulmonary fibrosis (per literature; not from label text) |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all five listed below are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source database. Published literature describes pirfenidone as inhibiting TGF-β and PDGF, which reduces fibroblast proliferation and collagen synthesis. Its efficacy in pulmonary fibrosis has been established.

Extracutaneous mastocytoma is a mast cell neoplasm. No documented mechanistic bridge links pirfenidone's anti-fibrotic activity to mast cell tumors or KIT-driven mast cell proliferation. The high score most likely reflects patterns in the knowledge graph rather than a verified biological link, and the missing MOA data prevents a closer check. Treat this prediction as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA212722 | Pirfenidone | Tablet, film coated | Laurus Labs Limited |
| ANDA212709 | Pirfenidone | Tablet | Apotex Corp. |
| ANDA212708 | Pirfenidone | Tablet, coated | Alembic Pharmaceuticals Inc. |
| ANDA212570 | Pirfenidone | Tablet, film coated | Amneal Pharmaceuticals NY LLC |
| ANDA212078 | Pirfenidone | Tablet, coated | Cipla USA Inc. |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. No trials, no literature, and no plausible mechanism link pirfenidone to extracutaneous mastocytoma.

Among the other top-10 predictions, only fibroblastic neoplasm (rank 9) has any supporting material. That material is mostly in vitro work in Dupuytren's disease fibroblasts and one 2003 pilot study in desmoid tumors (PMID 12907346, only the title was available). Two case reports point the other way: a sarcoma after pirfenidone use (PMID 29702057) and dermatofibromas aggravated on pirfenidone (PMID 32572469). Causality is unproven in both, but they are safety signals to weigh if fibroblast-lineage tumors are pursued.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search on pirfenidone in mast cell disease, including preclinical mast cell or KIT-pathway studies
- Full-text review of the 2003 desmoid tumor pilot study if the fibroblastic neoplasm direction is prioritized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Lifitegrast
parent: Model Prediction Only (L5)
nav_order: 860
evidence_level: L5
indication_count: 6
monitor_inn: "LIFITEGRAST"
predicted_indications: ["penile fibromatosis", "palmar fibromatosis", "Ledderhose disease", "infantile digital fibromatosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
last_modified_at: 2026-10-30
description: "Lifitegrast: predicted new indication Penile fibromatosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Lifitegrast
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Lifitegrast: Penile fibromatosis
{: .text-alpha }

## One-Sentence Summary

Lifitegrast is a topical eye-drop drug originally used to treat dry eye disease (keratoconjunctivitis sicca).
The TxGNN model predicts it may be effective for **penile fibromatosis** (Peyronie's disease-type fibrosis), but **0 clinical trials** and **0 publications** currently support this specific prediction. It is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Penile fibromatosis |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 2) |
| Number of FDA Applications | 2 (valid: 1) |
| Recommended Decision | Hold |

Other predicted indications from the same analysis, all at evidence level L5 and Hold: palmar fibromatosis (0.9959), Ledderhose disease (0.9957), infantile digital fibromatosis (0.9953), severe nonproliferative diabetic retinopathy (0.9924), and diabetic retinopathy (0.9903).

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for the original indication was not available in the data compiled for this report. Pharmacology data do show that lifitegrast is a topical integrin antagonist that targets LFA-1 (integrin alpha L, ITGAL). In laboratory assays it blocks T-cell adhesion to ICAM-1 (IC50 about 2.98 nM in Jurkat cells and 9 nM in HuT 78 cells) and reduces inflammatory mediator release. It was designed to have minimal systemic exposure.

Fibromatoses such as Peyronie's disease involve chronic inflammation and fibroblast activation. Blocking LFA-1/ICAM-1 interaction could in theory modulate the immune cells involved, so a link to dry eye (a T-cell-mediated inflammatory disease) is plausible but **speculative**. The same reasoning applies to palmar fibromatosis (Dupuytren's disease) and Ledderhose disease. For infantile digital fibromatosis, no data-supported mechanism exists, and the high score likely reflects network proximity to other fibromatoses rather than a biological signal.

A major translational barrier is delivery: lifitegrast is formulated for the ocular surface with minimal systemic absorption, and no obvious route exists to reach penile, palmar, or plantar tissue.

For diabetic retinopathy, leukocyte adhesion through LFA-1/ICAM-1 is implicated in retinal inflammation, which is biologically plausible. However, an ocular-surface formulation does not reach the retina in meaningful concentrations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction (penile fibromatosis), no related literature is available.

For the related prediction of diabetic retinopathy, one publication was retrieved:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41158172](https://pubmed.ncbi.nlm.nih.gov/41158172/) | 2025 | Genetic/proteomic association study | International Journal of Ophthalmology | Mendelian randomization using plasma proteomics and GWAS data to identify protein and drug targets for retinal neurodegenerative diseases. Indirect and hypothesis-generating; its relevance to lifitegrast cannot be confirmed. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208073 (cancelled) | Xiidra (Bausch & Lomb Incorporated) | Solution/drops | Not listed in the data compiled; originally approved by the FDA in July 2016 for dry eye disease |
| ANDA215063 (cancelled) | Lifitegrast (Aurobindo Pharma Limited) | For solution | Not listed in the data compiled |

---

## Safety Considerations

Please refer to the package insert for safety information.

One pharmacology record is available: lifitegrast acts on its target LFA-1 (ITGAL). No drug-drug interactions with other named drugs were identified, and no disease contraindications were found in the knowledge graph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications rest on model scores alone, with no clinical trials and no supporting literature for the leading candidates. The topical ocular formulation has no clear delivery route to fibrotic tissue, and both US licenses are currently cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking data gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Preclinical evidence that LFA-1 antagonism affects fibroblast or myofibroblast activity in fibromatosis models
- A feasibility assessment for a delivery route suitable for penile, palmar, or plantar tissue
- Clarification of the reason for the license cancellations and the current US availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


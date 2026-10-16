---
layout: default
title: Leuprolide
parent: Model Prediction Only (L5)
nav_order: 849
evidence_level: L5
indication_count: 2
monitor_inn: "LEUPROLIDE"
predicted_indications: ["osteoarthritis", "pseudoachondroplasia"]
---

# Leuprolide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Leuprolide: From Endometriosis to Osteoarthritis

## One-Sentence Summary

Leuprolide is a GnRH (gonadotropin-releasing hormone) agonist, originally used for hormone-related conditions such as endometriosis and precocious puberty.
The TxGNN model predicts it may be effective for **osteoarthritis**,
but currently **0 clinical trials** and **1 publication** (an unrelated case report) support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis, precocious puberty (from the knowledge graph; no approved-indication text is available in the US licence records) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licences cancelled) |
| Number of NDAs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known pharmacology, leuprolide is a GnRH agonist that suppresses the pituitary-gonadal axis and lowers sex steroid levels. This is the basis of its use in endometriosis and precocious puberty.

A credible mechanistic link to osteoarthritis cannot be established from the data compiled for this report. Estrogen deficiency is generally associated with worse joint health (for example, higher osteoarthritis risk after menopause). GnRH-agonist-induced hypoestrogenism would therefore be expected to be neutral or harmful rather than beneficial.

The very high TxGNN score (99.70%) is a model-based prediction only. No clinical evidence supports it, so it should be treated with caution.

A second prediction, **pseudoachondroplasia** (score 99.69%), has no clinical trials or literature either. The disease is caused by COMP gene mutations that stress cartilage cells, and GnRH suppression has no known effect on that pathology. One speculative indirect idea is that GnRH agonists delay growth-plate closure, but this does not address the underlying defect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Case report | Clinical Breast Cancer | Metastatic prostate adenocarcinoma mimicking inflammatory breast carcinoma in a 78-year-old man. It is not related to osteoarthritis and offers no support for this prediction. |

## US Market Information

All six US licences are currently cancelled. Approved-indication text is not available in the records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021488 | Eligard (Tolmar) | Extended-release injectable suspension | Not available |
| NDA021343 | Eligard (Tolmar) | Extended-release injectable suspension | Not available |
| NDA021379 | Vabrinty (Uronova) | Extended-release injectable suspension | Not available |
| NDA021731 | Vabrinty (Uronova) | Extended-release injectable suspension | Not available |
| NDA211488 | CAMCEVI (Accord BioPharma) | Injectable emulsion | Not available |

A sixth licence, NDA213150 (Fensolvi, Tolmar, extended-release injectable suspension), is also cancelled.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: hypertension, hyperglycemia, diabetes mellitus and diabetic ketoacidosis, obesity (including monogenic obesity), stroke and other cerebrovascular disorders, cerebral infarction, myocardial infarction and coronary thrombosis, hemoglobinopathy, and urinary tract obstruction.
- **Drug Interactions**: 100 interactions were recorded. Most of those listed are Moderate, including antidiabetic agents (acarbose, metformin, alogliptin, linagliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide), laxatives (bisacodyl, picosulfuric acid, castor oil, polyethylene glycol), famotidine, loperamide, and clarithromycin. **Major** interactions were found with **dolasetron** and **cisapride**.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). There are no relevant trials or literature, and the biology (sex-steroid suppression) suggests no benefit, and possibly harm, for osteoarthritis. All US licences are also cancelled.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- FDA package insert warnings and contraindications
- A plausible mechanistic rationale, plus preclinical or observational data, linking GnRH agonism to joint or cartilage outcomes
- Review of the cancelled licence status and approved-indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


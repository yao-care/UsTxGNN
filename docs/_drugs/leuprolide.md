---
layout: default
title: Leuprolide
parent: Model Prediction Only (L5)
nav_order: 849
evidence_level: L5
indication_count: 2
monitor_inn: "LEUPROLIDE"
predicted_indications: ["osteoarthritis", "pseudoachondroplasia"]
last_modified_at: 2026-11-24
description: "Leuprolide: predicted new indication Osteoarthritis (evidence level L5). In the US: 28 FDA applications (21 active)"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Leuprolide: Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Leuprolide is a GnRH (gonadotropin-releasing hormone) agonist, originally used for hormone-related conditions such as endometriosis and precocious puberty.
The TxGNN model predicts it may be effective for **osteoarthritis**,
but currently **0 clinical trials** and **1 publication** (an unrelated case report) support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 21 of 28) |
| Number of FDA Applications | 28 (active: 21) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for leuprolide: "Leuprolide acetate, a gonadotropin releasing hormone (GnRH) agonist, acts as an inhibitor of gonadotropin secretion when given continuously in therapeutic doses. Animal and human studies indicate that after an initial stimulation, chronic administration of leuprolide acetate results in suppression of testicular and ovarian steroidogenesis." ([DailyMed: Vabrinty (leuprolide acetate) prescribing information, URONOVA PHARMACEUTICALS, INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=008776cc-83f1-4f8c-819b-6471425da15f), label version 2026-04-30; accessed 2026-11-19.) Based on known pharmacology, leuprolide is a GnRH agonist that suppresses the pituitary-gonadal axis and lowers sex steroid levels. This is the basis of its use in endometriosis and precocious puberty.

A credible mechanistic link to osteoarthritis cannot be established from the data compiled for this report. Estrogen deficiency is generally associated with worse joint health (for example, higher osteoarthritis risk after menopause). GnRH-agonist-induced hypoestrogenism would therefore be expected to be neutral or harmful rather than beneficial.

The very high TxGNN score (0.9970) is a model-based prediction only. No clinical evidence supports it, so it should be treated with caution.

A second prediction, **pseudoachondroplasia** (score 0.9969), has no clinical trials or literature either. The disease is caused by COMP gene mutations that stress cartilage cells, and GnRH suppression has no known effect on that pathology. One speculative indirect idea is that GnRH agonists delay growth-plate closure, but this does not address the underlying defect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Case report | Clinical Breast Cancer | Metastatic prostate adenocarcinoma mimicking inflammatory breast carcinoma in a 78-year-old man. It is not related to osteoarthritis and offers no support for this prediction. |

## US Market Information

Approved-indication text is not available in the records.

<!-- review:begin us-lic-20261105-leuprolide-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All six US licenses are currently valid. Approved-indication text is not available in the records." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-leuprolide-1 -->

<!-- review:begin us-lic-20261106-leuprolide-3 -->

> **Review correction (2026-11-06)**: Originally stated: "A sixth licence, NDA213150 (Fensolvi, Tolmar, extended-release injectable suspension), is also cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-leuprolide-3 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA074728 | LEUPROLIDE ACETATE | SANDOZ | Solution; subcutaneous | Valid |
| ANDA075471 | LEUPROLIDE ACETATE | MEITHEAL | Solution; subcutaneous | Valid |
| ANDA078885 | LEUPROLIDE ACETATE | SUN PHARM | Solution; subcutaneous | Valid |
| ANDA212963 | LEUPROLIDE ACETATE | EUGIA PHARMA | Solution; subcutaneous | Valid |
| ANDA213829 | LEUPROLIDE ACETATE | SOMERSET THERAPS LLC | Solution; subcutaneous | Valid |

Showing 5 of 28 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: hypertension, hyperglycemia, diabetes mellitus and diabetic ketoacidosis, obesity (including monogenic obesity), stroke and other cerebrovascular disorders, cerebral infarction, myocardial infarction and coronary thrombosis, hemoglobinopathy, and urinary tract obstruction.
- **Drug Interactions**: 100 interactions were recorded. Most of those listed are Moderate, including antidiabetic agents (acarbose, metformin, alogliptin, linagliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide), laxatives (bisacodyl, picosulfuric acid, castor oil, polyethylene glycol), famotidine, loperamide, and clarithromycin. **Major** interactions were found with **dolasetron** and **cisapride**.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). There are no relevant trials or literature, and the biology (sex-steroid suppression) suggests no benefit, and possibly harm, for osteoarthritis.

<!-- review:begin us-lic-20261105-leuprolide-2 -->

> **Review correction (2026-11-05)**: Originally stated: "There are no relevant trials or literature, and the biology (sex-steroid suppression) suggests no benefit, and possibly harm, for osteoarthritis. All six US licenses are currently valid." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-leuprolide-2 -->

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- FDA package insert warnings and contraindications
- A plausible mechanistic rationale, plus preclinical or observational data, linking GnRH agonism to joint or cartilage outcomes
- Review of approved-indication text

<!-- review:begin us-lic-20261106-leuprolide-4 -->

> **Review correction (2026-11-06)**: Originally stated: "Review of the cancelled licence status and approved-indication text" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-leuprolide-4 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All six US licenses are currently valid" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-05 | Removed: "All six US licenses are currently valid" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "A sixth licence, NDA213150 (Fensolvi, Tolmar, extended-release injectable suspension), is also cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "the cancelled licence status and" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vabrinty (leuprolide acetate) prescribing information, URONOVA PHARMACEUTICALS, INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=008776cc-83f1-4f8c-819b-6471425da15f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


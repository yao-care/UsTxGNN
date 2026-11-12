---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 1215
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
description: "Teriparatide: predicted new indication Duodenal ulcer (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Teriparatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Teriparatide: Duodenal ulcer (disease)
{: .text-alpha }

## One-Sentence Summary

Teriparatide is a parathyroid hormone fragment (PTH 1-34) originally used to treat osteoporosis in patients at high risk of fracture.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal ulcer (disease) |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 7 of 8) |
| Number of FDA Applications | 8 (active: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Teriparatide is a synthetic peptide that mimics the first 34 amino acids of human parathyroid hormone. Pharmacology data show it binds the PTH1 receptor (and also the PTH2 receptor). Its established role is anabolic: it stimulates bone formation in osteoporosis. A detailed mechanism-of-action record is not available for this report, so the description above rests on the receptor data and its known clinical use.

The data compiled for this report do not show a plausible mechanistic link between PTH receptor signaling in bone and duodenal ulcer healing. The very high TxGNN score (0.9986, model rank 32) reflects network-based computational similarity, not biological or clinical validation. Neither trials nor literature were found to support it, and the similarity between the original and predicted indications has not been assessed. This prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin us-lic-20261105-teriparatide-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All six US authorizations are currently valid, and the drug is marketed." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 8 FDA applications or NDC listings for this drug, 7 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-teriparatide-1 -->

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA208569 | TERIPARATIDE | TEVA PHARMS USA | Solution; subcutaneous | Valid |
| ANDA211097 | TERIPARATIDE | APOTEX | Solution; subcutaneous | Valid |
| ANDA213641 | TERIPARATIDE | AMPHASTAR PHARMS INC | Solution; subcutaneous | Valid |
| ANDA214412 | TERIPARATIDE | DR REDDYS | Solution; subcutaneous | Valid |
| NDA021318 | FORTEO | LILLY | Solution; subcutaneous | Valid |
| NDA211939 | BONSITY | ALVOGEN | Solution; subcutaneous | Valid |

Showing 6 of 8 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

Label-based warnings and contraindications were not available for this report; please refer to the package insert.

- **Knowledge-graph contraindication signals** (from drug-disease contraindication links, not label text): hypotensive disorder, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, bone osteosarcoma, bone Paget disease, juvenile Paget disease, osteomalacia, rickets, urolithiasis, renal osteodystrophy, osteitis fibrosa, and hyperparathyroidism.
- **Drug interactions** (8 records in total, 6 drug-drug and 2 receptor-target records):
  - Moderate: topical calcitriol, topical calcipotriol, digoxin, digitoxin
  - Minor: hydrochlorothiazide, furosemide

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The duodenal ulcer prediction rests only on a model score from the TxGNN model (deep learning), with no clinical trials, no literature, and no plausible mechanistic link.

<!-- review:begin us-lic-20261105-teriparatide-2 -->

> **Review correction (2026-11-05)**: Originally stated: "The duodenal ulcer prediction rests only on a model score from the TxGNN model (deep learning), with no clinical trials, no literature, and no plausible mechanistic link. The drug is marketed in the US, with all six authorizations valid." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 8 FDA applications or NDC listings for this drug, 7 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-teriparatide-2 -->

**To proceed, the following is needed:**
- A mechanistic rationale connecting PTH1R signaling to duodenal ulcer biology, and preclinical evidence to test it
- A targeted literature and trial search specific to teriparatide and duodenal ulcer
- Label-based warnings and contraindications from the FDA package insert, and detailed mechanism-of-action data
- A review of whether other predictions for this drug deserve priority. Bone density in functional hypothalamic amenorrhea has indirect support only.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All six US authorizations are currently valid, and the drug is marketed" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-05 | Removed: "The drug is marketed in the US, with all six authorizations valid" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


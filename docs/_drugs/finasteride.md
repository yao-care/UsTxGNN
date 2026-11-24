---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 708
evidence_level: L5
indication_count: 6
monitor_inn: "FINASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
last_modified_at: 2026-11-24
description: "Finasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
---

# Finasteride
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

## Finasteride: From Benign Prostatic Hyperplasia to Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Finasteride was originally used to treat benign prostatic hyperplasia.
The TxGNN model (deep learning) predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but this is a model prediction with **0 clinical trials** and only **4 indirect publications** (narrative reviews and a methods paper) behind it. The evidence is weak and does not directly show that finasteride works for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Hypertrichosis (rank 2 of 6 predictions; the top-ranked prediction, Ambras type hypertrichosis universalis congenita, has no evidence at all) |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 17 of 27; OTC monograph / unapproved listings: 3) |
| Number of FDA Applications | 27 (active: 17) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for finasteride: "The development and enlargement of the prostate gland is dependent on the potent androgen, 5α-dihydrotestosterone (DHT). Type II 5α-reductase metabolizes testosterone to DHT in the prostate gland, liver and skin. […] Finasteride is a competitive and specific inhibitor of Type II 5α-reductase with which it slowly forms a stable enzyme complex." ([DailyMed: Proscar (finasteride) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6f988153-fc74-4ca4-b29a-111f750c4a4b), label version 2026-03-18; accessed 2026-11-19.) Based on general pharmacology, finasteride inhibits type II 5-alpha-reductase and lowers dihydrotestosterone (DHT). That is how it shrinks the prostate in benign prostatic hyperplasia, and it is also why it is used for male pattern hair loss.

The link to hypertrichosis is weak. Hypertrichosis is increased hair growth in non-androgen-dependent areas, so lowering DHT would not be expected to treat it. The retrieved publications discuss hair disorders broadly, including androgenetic alopecia, hirsutism and hypertrichosis. They mention finasteride for male pattern hair loss and laser-assisted hair removal for hypertrichosis and hirsutism, but none shows finasteride working for hypertrichosis. The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other predictions fare no better:
- **Ambras type hypertrichosis universalis congenita** (score 0.9999): a genetic developmental disorder not driven by androgens, with no trials or literature.
- **Malformation syndrome with odontal/periodontal component, Dandy-Walker malformation syndrome, isolated genetic hair shaft abnormality, familial isolated trichomegaly**: no plausible mechanism and no evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

<!-- review:begin us-lic-20261105-finasteride-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All 10 licenses compiled for this report are valid; the table shows the first 5." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-finasteride-1 -->

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Overview of new hair disease therapies: finasteride for male pattern hair loss and laser-assisted hair removal for hypertrichosis and hirsutism |
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Ann Dermatol Venereol | Investigation and treatment of adult hirsutism and hypertrichosis; hypertrichosis is non-androgen-dependent and often iatrogenic or metabolic |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Ther Umsch | Treatment options for androgenetic alopecia and hirsutism; emotional impact of cosmetic hair problems |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Methods paper | Der Hautarzt | TrichoScan digital hair analysis tool; not a drug study |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA076436 | FINASTERIDE | DR REDDYS LABS INC | Tablet; oral | Valid |
| ANDA076437 | FINASTERIDE | DR REDDYS LABS LTD | Tablet; oral | Valid |
| ANDA076511 | FINASTERIDE | TEVA | Tablet; oral | Valid |
| ANDA078341 | FINASTERIDE | AUROBINDO PHARMA | Tablet; oral | Valid |
| ANDA078900 | FINASTERIDE | ZYDUS PHARMS USA INC | Tablet; oral | Valid |

Showing 5 of 30 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: liver disease and gallbladder disease are listed as contraindication-related conditions.
- **Drug Interactions**: 100 potential interactions were found in the DDInter database, but none has a severity level assigned. Examples include calcitriol, doxycycline, clotrimazole, famotidine, acetylsalicylic acid, bupropion, omeprazole, metformin, and morphine.

Please refer to the package insert for full warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials, and the four publications are indirect reviews and a methods paper. Hypertrichosis is not androgen-driven, so finasteride's DHT-lowering action has no clear mechanistic link to it. The drug is marketed in the US.

<!-- review:begin us-lic-20261106-finasteride-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with 10 valid licenses." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-finasteride-2 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Direct clinical or preclinical evidence of finasteride in hypertrichosis
- A reassessment of whether hirsutism, an androgen-dependent condition, would be a more plausible target than hypertrichosis
- Clarification of the US regulatory pathway for this new indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All 10 licenses compiled for this report are valid; the table shows the first 5" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 10 valid licenses" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Proscar (finasteride) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6f988153-fc74-4ca4-b29a-111f750c4a4b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


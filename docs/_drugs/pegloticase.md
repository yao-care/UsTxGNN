---
layout: default
title: Pegloticase
parent: Model Prediction Only (L5)
nav_order: 1022
evidence_level: L5
indication_count: 1
monitor_inn: "PEGLOTICASE"
predicted_indications: ["severe nonproliferative diabetic retinopathy"]
last_modified_at: 2026-11-12
description: "Pegloticase: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Gout"
---

# Pegloticase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Pegloticase: From Gout to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Pegloticase is a PEGylated uricase enzyme originally used to treat gout.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9918 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, pegloticase is a PEGylated recombinant uricase that converts uric acid to allantoin, lowering serum urate. Its efficacy in gout is the basis of its original use.

A possible indirect link is that hyperuricemia and xanthine oxidase-related oxidative stress have been proposed as contributors to diabetic microvascular injury, including retinopathy. This link is speculative and has not been validated here.

There are also practical concerns for this new use:
- The drug is given systemically by intravenous infusion, while the target disease is ocular.
- Immunogenicity (anti-drug antibodies, infusion reactions, anaphylaxis) is a known issue with this class of drug.
- Route compatibility and similarity to the original indication have not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| BLA125293 | KRYSTEXXA | HORIZON PHARMA | Injectable; injection | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: Seven moderate-level interactions were identified, all with other PEGylated products:
  - Pegvaliase
  - Pegvisomant
  - Pegademase
  - Pegaspargase
  - Pegfilgrastim
  - Peginterferon alfa-2a
  - Peginterferon alfa-2b

Please refer to the package insert for other safety information, including warnings and contraindications. Package insert details were not available in the compiled data. Known class concerns noted in the evaluation include anaphylaxis and infusion reactions, and hemolysis and methemoglobinemia risk in G6PD deficiency.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this prediction is a high TxGNN score. There are no clinical trials or publications, the mechanistic link is speculative, and the drug is delivered systemically for an eye disease.

<!-- review:begin us-lic-20261031-pegloticase-1 -->

> **Review correction (2026-10-31)**: Originally stated: "There are no clinical trials or publications, the mechanistic link is speculative, and the drug is delivered systemically for an eye disease. The only US license is cancelled, which further limits availability." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-pegloticase-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Preclinical or mechanistic evidence linking urate lowering or uricase activity to diabetic retinopathy
- Assessment of route compatibility (systemic IV versus ocular delivery) and immunogenicity risk
- Clarification of current availability

<!-- review:begin us-lic-20261106-pegloticase-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of current availability, given the cancelled US license status" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-pegloticase-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only US license is cancelled, which further limits availability" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "given the cancelled US license status" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


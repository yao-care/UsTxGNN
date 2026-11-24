---
layout: default
title: Fluoroestradiol F-18
parent: Model Prediction Only (L5)
nav_order: 721
evidence_level: L5
indication_count: 1
monitor_inn: "FLUOROESTRADIOL F-18"
predicted_indications: ["amenorrhea (disease)"]
last_modified_at: 2026-11-20
description: "Fluoroestradiol F-18: predicted new indication Amenorrhea (evidence level L5). Approved use: Not available"
---

# Fluoroestradiol F-18
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

## Fluoroestradiol F-18: From a Diagnostic Imaging Agent to Amenorrhea
{: .text-alpha }

## One-Sentence Summary

Fluoroestradiol F-18 is an estrogen-analog PET radiotracer that binds estrogen receptors and is used as a diagnostic imaging agent, not a treatment.
The TxGNN model predicts it may be relevant to **Amenorrhea**, but **no clinical trials** and **no publications** currently support this direction.
The prediction most likely reflects the drug's similarity to estradiol rather than any real therapeutic potential.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the data compiled for this report) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 0.9940 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for fluoroestradiol f-18: "Fluoroestradiol F 18 binds ER. The following binding affinity: Kd = 0.13 ± 0.02 nM, Bmax = 1901 ± 89 fmol/mg, and IC 50 = 0.085 nM, was determined in an ER-positive human breast cancer cell line (MCF-7)." ([DailyMed: Cerianna (fluoroestradiol f 18) prescribing information, GE Healthcare Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b2c2a2df-cf3e-4a29-a033-231ed5a94b58), label version 2026-01-12; accessed 2026-11-19.) Based on known information, fluoroestradiol F-18 is an estrogen analog that binds estrogen receptors and is used as a PET radiotracer to visualise receptor expression.

Amenorrhea involves disrupted estrogen and hypothalamic-pituitary-ovarian axis signalling. In principle, an estrogen-receptor-binding tracer could be used to image receptor expression in uterine or other target tissue. However, at tracer doses the compound has no pharmacologic effect and would not treat amenorrhea.

The high TxGNN score (0.994) most likely reflects structural and target similarity to estradiol, which is used in estrogen-deficiency states. It should not be read as evidence that this compound has therapeutic potential for amenorrhea. If any link exists, it is a diagnostic or imaging one, not a therapeutic one.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212155 | CERIANNA (GE Healthcare Inc.) | Injection | Not available (status: valid) |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found, and no disease contraindication links were identified in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no registered clinical trials and no literature. Basic safety and mechanism data are also missing.

<!-- review:begin us-lic-20261031-fluoroestradiol_f-18-1 -->

> **Review correction (2026-10-31)**: Originally stated: "There are no registered clinical trials and no literature. The compound is a diagnostic tracer with no pharmacologic effect at tracer doses, and its only US authorization is cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-fluoroestradiol_f-18-1 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Confirmation of the original approved indication
- A clear rationale for whether any use in amenorrhea would be diagnostic (imaging) or therapeutic
- Supporting preclinical or clinical literature, if the direction is pursued

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The compound is a diagnostic tracer with no pharmacologic effect at tracer doses, and its only US authorization is cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cerianna (fluoroestradiol f 18) prescribing information, GE Healthcare Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b2c2a2df-cf3e-4a29-a033-231ed5a94b58) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


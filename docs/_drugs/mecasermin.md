---
layout: default
title: Mecasermin
parent: Model Prediction Only (L5)
nav_order: 891
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Mecasermin: predicted new indication Monosomy X (evidence level L5). Approved use: Growth hormone insensitivity syndrome"
monitor_inn: "MECASERMIN"
predicted_indications: ["monosomy X", "Wolman disease with hypolipoproteinemia and acanthocytosis", "esophageal varices without bleeding", "esophageal varices with bleeding"]
---

# Mecasermin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Mecasermin: From Growth Hormone Insensitivity Syndrome to Monosomy X
{: .text-alpha }

## One-Sentence Summary

Mecasermin (recombinant IGF-1) was originally used to treat growth hormone insensitivity syndrome and Laron syndrome.
The TxGNN model predicts it may be effective for **monosomy X (Turner syndrome)**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Growth hormone insensitivity syndrome; Laron syndrome |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1; OTC monograph / unapproved listings: 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mecasermin is recombinant human IGF-1. It acts on the GH/IGF-1 axis and bypasses defective growth hormone signaling, which is why it was used in growth hormone insensitivity.

Monosomy X (Turner syndrome) is characterized by short stature, so a biological link to growth failure is plausible: IGF-1 supplementation could theoretically address growth deficits. However, the rationale is indirect. Patients with Turner syndrome typically have normal or elevated growth hormone levels and are treated with growth hormone itself, not IGF-1. The high TxGNN score is a computational prediction only and is not backed by trials or literature.

Other predicted indications were also reviewed, and none has supporting studies:

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Wolman disease with hypolipoproteinemia and acanthocytosis | 0.9909 | No clear mechanistic connection (lysosomal acid lipase deficiency, unrelated to IGF-1 signaling) |
| Esophageal varices without bleeding | 0.9903 | No established rationale for IGF-1 therapy |
| Esophageal varices with bleeding | 0.9903 | No known role; hypoglycemia risk is a concern in acutely ill patients |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| BLA021839 | INCRELEX | IPSEN INC | Injectable; subcutaneous | Valid |
| NDC 17089-376 | GUNA-IGF | Guna spa | Solution/ drops | NDC listing, no FDA application (unapproved homeopathic) |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 24 interactions were recorded in total, and the 20 detailed entries are all rated Moderate. They involve glucose-lowering agents, which is consistent with mecasermin's hypoglycemia-related risk:
  - Sulfonylureas: chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide
  - Meglitinide: nateglinide
  - Insulins: human (regular, isophane, zinc, zinc extended, inhaled rapid-acting), aspart (including aspart protamine), lispro (including lispro protamine), glulisine, detemir, degludec, glargine

Please refer to the package insert for other safety information, such as warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model (L5). There are no clinical trials or publications, the mechanistic link to Turner syndrome is indirect (GH is the standard therapy).

<!-- review:begin us-lic-20261106-mecasermin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "There are no clinical trials or publications, the mechanistic link to Turner syndrome is indirect (GH is the standard therapy), and the US authorizations are cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-mecasermin-1 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA (a blocking gap for safety screening)
- Detailed mechanism of action data
- Literature and trial searches specific to IGF-1 in Turner syndrome, including comparison with standard GH therapy
- Review of route/formulation feasibility
- A hypoglycemia monitoring plan, given the interactions with glucose-lowering agents

<!-- review:begin us-lic-20261106-mecasermin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Review of the cancelled market status and route/formulation feasibility" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-mecasermin-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "and the US authorizations are cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "the cancelled market status and" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


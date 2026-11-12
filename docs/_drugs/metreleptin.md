---
layout: default
title: Metreleptin
parent: Model Prediction Only (L5)
nav_order: 920
evidence_level: L5
indication_count: 10
monitor_inn: "METRELEPTIN"
predicted_indications: ["familial generalized lentiginosis", "gastrocutaneous syndrome", "Moynahan syndrome", "rhabdoid tumor", "osteopathia striata-pigmentary dermopathy-white forelock syndrome", "congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome", "acromelanosis", "leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome", "benign neoplasm of adrenal gland", "peripheral nerve schwannoma"]
last_modified_at: 2026-11-12
description: "Metreleptin: predicted new indication Familial generalized lentiginosis (evidence level L5). Approved use: Lipodystrophy (including Berardinelli-Seip congenital lipodystrophy a…"
---

# Metreleptin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Metreleptin: From Lipodystrophy to Familial Generalized Lentiginosis
{: .text-alpha }

## One-Sentence Summary

Metreleptin is a leptin analog originally used to treat lipodystrophy, including congenital generalized lipodystrophy.
The TxGNN model predicts it may be effective for **familial generalized lentiginosis**, but **0 clinical trials** and **0 publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lipodystrophy (including Berardinelli-Seip congenital lipodystrophy and congenital generalized lipodystrophy) |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metreleptin is a recombinant leptin analog used to replace leptin in patients with lipodystrophy, where leptin deficiency drives metabolic disease such as insulin resistance and abnormal lipid levels.

The data compiled for this report show no plausible mechanistic link between leptin replacement and familial generalized lentiginosis, which is a pigmentation disorder. The high score (0.9971) comes from the TxGNN model (deep learning) only. It may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a hypothesis, not as evidence of efficacy.

Other top-ranked predictions are similarly unsupported. They include gastrocutaneous syndrome, Moynahan syndrome, rhabdoid tumor, and several pigmentary or rare congenital syndromes, each with scores near 99.5–0.9970 and no trials or literature. For rhabdoid tumor, leptin signaling has been discussed in cancer biology and may promote rather than suppress tumor growth, which raises a potential safety concern for any oncology use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| BLA125390 | MYALEPT | CHIESI FARMACEUTICI SPA | Injectable; injection | Valid |

<!-- licenses:end -->

Manufacturer: Amryt Pharmaceuticals Designated Activity Company. The product is injectable only.

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs; the 20 reviewed here were mostly of Moderate severity, with one Minor (bortezomib). Examples include:
  - Opioids: fentanyl, alfentanil, butorphanol, benzhydrocodone
  - Hormonal agents: ethinylestradiol, norethisterone, desogestrel
  - Oncology agents: abemaciclib, acalabrutinib, alpelisib, avapritinib, brigatinib, cabozantinib, capmatinib, ceritinib
  - Others: bictegravir, buspirone, cariprazine, chlorpropamide

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5) and no identifiable mechanistic link between leptin replacement and a pigmentation disorder. Package-insert safety data are missing.

<!-- review:begin us-lic-20261106-metreleptin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The US license is also cancelled, and package-insert safety data are missing." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-metreleptin-1 -->

**To proceed, the following is needed:**
- Mechanism of action data for metreleptin, to assess any biological link to the predicted indication
- A mechanistic or preclinical rationale connecting leptin signaling to familial generalized lentiginosis
- FDA package insert warnings and contraindications for a safety review
- Evaluation of other candidates with more plausible links, such as insulin-resistance-related conditions, if the goal is a viable repurposing path

<!-- review:begin us-lic-20261106-metreleptin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the cancelled US license status and its implications for access and development / Evaluation of other candidates with more plausible links, such as insulin-resistance-related conditions, if the goal is a viable repurposing path" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-metreleptin-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The US license is also cancelled, and p" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "Clarification of the cancelled US license status and its implications for access and development" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


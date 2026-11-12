---
layout: default
title: Terconazole
parent: Model Prediction Only (L5)
nav_order: 1213
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-12
monitor_inn: "TERCONAZOLE"
predicted_indications: ["trichomonal vulvovaginitis", "vulvitis", "postmenopausal atrophic vaginitis", "herpetic vulvovaginitis", "ulceration of vulva", "vulvar neoplasm", "vaginal discharge", "bacterial vaginosis"]
description: "Terconazole: predicted new indication Trichomonal vulvovaginitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Terconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Terconazole: Trichomonal vulvovaginitis
{: .text-alpha }

## One-Sentence Summary

Terconazole is a topical triazole antifungal, marketed in the United States as a vaginal cream and suppository.
The TxGNN model predicts it may be useful for **trichomonal vulvovaginitis**, but the data compiled for this report contain **no clinical trials** and **no publications that report trichomonal outcomes**. Evidence is therefore model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trichomonal vulvovaginitis |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 6 of 10) |
| Number of FDA Applications | 10 (active: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the compiled data. Terconazole belongs to the triazole antifungals, which inhibit fungal lanosterol 14-alpha-demethylase (CYP51) and block ergosterol synthesis.

This mechanism does not transfer plausibly to trichomonal infection. *Trichomonas vaginalis* is a protozoan, and it lacks ergosterol-dependent membrane biology comparable to that of fungi. The high TxGNN score most likely reflects shared genital-infection neighbours in the model's training data rather than a true pharmacological link.

The compiled literature does not close this gap. The only relevant paper is a general antifungal review that does not report any trichomonas outcomes. The prediction is best treated as a model artefact until there is direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials are registered for this predicted indication.

<!-- review:begin us-lic-20261105-terconazole-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All six authorizations in the local data are currently valid. This table lists the first five; the sixth is ANDA077149 (suppository)." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 10 FDA applications or NDC listings for this drug, 6 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-terconazole-1 -->

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6617296](https://pubmed.ncbi.nlm.nih.gov/6617296/) | 1983 | Review | Chemotherapy | Describes terconazole as a broad-spectrum triazole antifungal with strong in vitro activity against yeasts and mycelium-forming fungi. It reports in vivo activity in topical models of dermatophytosis and candidosis. It does not address trichomonal infection. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075953 | Terconazole (A-S Medication Solutions) | Cream | Valid |
| ANDA077553 | Terconazole (Sun Pharmaceutical Industries) | Suppository | Valid |
| ANDA076043 | Terconazole (A-S Medication Solutions) | Cream | Valid |
| ANDA076712 | Terconazole (A-S Medication Solutions) | Cream | Valid |
| NDA021735 | Terconazole (A-S Medication Solutions) | Cream | Valid |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no trials or targeted literature for trichomonal vulvovaginitis. The antifungal mechanism of terconazole gives no plausible basis for activity against a protozoan, so the high model score is not supported by pharmacology or clinical data.

**To proceed, the following is needed:**
- A mechanistic hypothesis explaining how a CYP51-targeting azole could act on *Trichomonas vaginalis*
- In vitro susceptibility data against *T. vaginalis*
- Any clinical or observational data reporting trichomonal outcomes with terconazole
- Detailed mechanism-of-action data and package-insert safety information (warnings and contraindications)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All six authorizations in the local data are currently valid. This table lists the first five; the sixth is ANDA077149 (suppository)" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


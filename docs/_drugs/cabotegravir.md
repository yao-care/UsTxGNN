---
layout: default
title: Cabotegravir
parent: Model Prediction Only (L5)
nav_order: 483
evidence_level: L5
indication_count: 5
monitor_inn: "CABOTEGRAVIR"
predicted_indications: ["rheumatoid arthritis", "sclerosing cholangitis", "bronchitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "severe nonproliferative diabetic retinopathy"]
last_modified_at: 2026-11-12
description: "Cabotegravir: predicted new indication Rheumatoid arthritis (evidence level L5). In the US: 3 FDA applications (3 active)"
---

# Cabotegravir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Cabotegravir: Rheumatoid arthritis
{: .text-alpha }

## One-Sentence Summary

Cabotegravir is an HIV-1 integrase strand transfer inhibitor (INSTI). The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but **0 clinical trials** and **0 publications** currently support this direction. The prediction is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 3 of 3) |
| Number of FDA Applications | 3 (active: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the FDA-approved prescribing information for cabotegravir: "Cabotegravir is an HIV-1 antiretroviral drug. […] Cabotegravir inhibits HIV integrase by binding to the integrase active site and blocking the strand transfer step of retroviral deoxyribonucleic acid (DNA) integration that is essential for the HIV replication cycle. The mean 50% inhibitory concentration (IC 50 ) value of cabotegravir in a strand transfer assay using purified recombinant HIV-1 integrase was 3.0 nM." ([DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3), label version 2025-04-11; accessed 2026-11-19.) Based on general pharmacology, cabotegravir is an HIV-1 integrase strand transfer inhibitor, a class that blocks viral DNA integration into the host genome.

Rheumatoid arthritis is an autoimmune and inflammatory disease driven by pathways such as TNF, IL-6 and JAK/STAT. Integrase inhibition does not target these pathways, so no established mechanistic link exists between the original use and the predicted indication. The high TxGNN score (0.9945) is a TxGNN model (deep learning) prediction and is not backed by any clinical or published evidence in the data compiled.

Other predictions in the list share the same weakness. These are sclerosing cholangitis (0.9922), bronchitis (0.9919), colobomatous microphthalmia-rhizomelic dysplasia syndrome (0.9916) and severe nonproliferative diabetic retinopathy (0.9903). Each has no trials, no literature and no plausible mechanistic link. They are likely TxGNN model (deep learning) artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA212887 | VOCABRIA | VIIV HLTHCARE | Tablet; oral | Valid |
| NDA215499 | APRETUDE | VIIV HLTHCARE | Suspension, extended release; intramuscular | Valid |
| NDA212888 | CABENUVA KIT | VIIV HLTHCARE | Suspension, extended release; intramuscular | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: Seven interactions of Moderate severity were identified. All involve polyvalent cation-containing antacids or buffering agents:
  - Calcium carbonate
  - Aluminum hydroxide
  - Magnesium carbonate
  - Magnesium hydroxide
  - Magnesium oxide
  - Sodium bicarbonate
  - Sodium citrate

Warning and contraindication data from the package insert are not available. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score. There are no trials or publications, and no plausible mechanistic link between integrase inhibition and rheumatoid arthritis.

<!-- review:begin us-lic-20261031-cabotegravir-1 -->

> **Review correction (2026-10-31)**: Originally stated: "There are no trials or publications, and no plausible mechanistic link between integrase inhibition and rheumatoid arthritis. In addition, the only US license is cancelled, and package insert safety data are missing." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 3 FDA applications or NDC listings for this drug, 3 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-cabotegravir-1 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, to allow a proper mechanistic-link analysis
- Confirmation of the original approved indication and current US regulatory status
- Preclinical or mechanistic evidence that links cabotegravir to inflammatory or autoimmune pathways
- Route and formulation compatibility assessment for the proposed indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "In addition, the only US license is cancelled, and package insert safety data are missing" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


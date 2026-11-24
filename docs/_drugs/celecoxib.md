---
layout: default
title: Celecoxib
parent: Model Prediction Only (L5)
nav_order: 510
evidence_level: L5
indication_count: 7
monitor_inn: "CELECOXIB"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "WHIM syndrome"]
last_modified_at: 2026-11-24
description: "Celecoxib: predicted new indication acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In the US: 32 FDA applications (22 active)"
---

# Celecoxib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Celecoxib: COX-2 selective NSAID → acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Celecoxib is an oral COX-2 inhibitor of the NSAID class, with locally recorded licences in the United States. The TxGNN model predicts it may be relevant to **acromesomelic dysplasia, Hunter-Thompson type**, but **no clinical trials and no publications** were found to support this direction, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 22 of 32) |
| Number of FDA Applications | 32 (active: 22) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for celecoxib: "Celecoxib has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of celecoxib is believed to be due to inhibition of prostaglandin synthesis, primarily via inhibition of COX-2. Celecoxib is a potent inhibitor of prostaglandin synthesis in vitro." ([DailyMed: Vyscoxa (celecoxib) prescribing information, Carwin Pharmaceutical Associates, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5094d47e-f791-4190-9397-b7500143a74d), label version 2025-07-31; accessed 2026-11-19.) Celecoxib is known as a selective COX-2 inhibitor, which reduces prostaglandin-mediated inflammation and pain.

Acromesomelic dysplasia, Hunter-Thompson type is a rare skeletal dysplasia caused by loss-of-function mutations in CDMP1/GDF5. COX-2 inhibition does not address this underlying genetic defect, so no credible mechanistic link can be drawn. The high score appears to reflect proximity to musculoskeletal disease nodes in the model rather than a biological rationale. At most, celecoxib might offer symptomatic pain relief, which would not be disease-modifying and is unsupported by any evidence here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- review:begin us-lic-20261124b-celecoxib-2 -->

> **Review correction (2026-11-24)**: Originally stated: "Twelve US licence records were compiled, and the list may be partial." Removed: the number or type of FDA applications stated here did not match the FDA data (Drugs@FDA and the NDC Directory). The current figures are shown in the Quick Overview and in the program-generated table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261124b-celecoxib-2 -->

 Most licences are for oral capsules. The local records carry no approved-indication text. Examples include:

<!-- review:begin us-lic-20261124-celecoxib-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The local records carry no approved-indication text, and every record is listed as "single-ingredient" type." Corrected: it said every record is a single-ingredient product, but the FDA data for this drug also include combination products (CONSENSI, NDA210045: amlodipine besylate and celecoxib; SEGLENTIS, NDA213426: celecoxib and tramadol hydrochloride). Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/).

<!-- review:end us-lic-20261124-celecoxib-1 -->

<!-- review:begin us-lic-20261124b-celecoxib-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The licences are for oral capsules." Corrected: the dosage-form statement did not match the dosage forms of all FDA applications on record (Drugs@FDA and the NDC Directory); see the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261124b-celecoxib-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA076898 | CELECOXIB | TEVA | Capsule; oral | Valid |
| ANDA200562 | CELECOXIB | WATSON LABS INC | Capsule; oral | Valid |
| ANDA202240 | CELECOXIB | LUPIN | Capsule; oral | Valid |
| ANDA204197 | CELECOXIB | APOTEX | Capsule; oral | Valid |
| ANDA204519 | CELECOXIB | ALEMBIC | Capsule; oral | Valid |

Showing 5 of 32 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions**: The interaction query returned 100 records. Examples include:
- **Major**: Eliglustat
- **Moderate**: hydrocortisone, metformin, several sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), nateglinide, exenatide, cimetidine, levofloxacin, metronidazole, naltrexone, and the aminosalicylates balsalazide, mesalazine and olsalazine

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No trials or publications address this disease, and there is no plausible link between COX-2 inhibition and the GDF5-related genetic defect.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that links celecoxib to this condition
- Mechanism-of-action data for celecoxib in the context of skeletal development
- Package insert warnings and contraindications for a safety review
- Confirmation of the original approved indication from the licence labels

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vyscoxa (celecoxib) prescribing information, Carwin Pharmaceutical Associates, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5094d47e-f791-4190-9397-b7500143a74d) |
| 2026-11-24 | Corrected: "every record is listed as 'single-ingredient' type" (two combination products are on record) | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/) |
| 2026-11-24 | Corrected: "The licences are for oral capsules." | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-24 | Removed: "Twelve US licence records were compiled, and the list may be partial." | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


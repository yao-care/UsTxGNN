---
layout: default
title: Lansoprazole
parent: Model Prediction Only (L5)
nav_order: 835
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "LANSOPRAZOLE"
predicted_indications: ["duodenal obstruction"]
description: "Lansoprazole: predicted new indication Duodenal obstruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Lansoprazole
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

## Lansoprazole: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor originally used for acid-related upper gastrointestinal conditions such as gastric ulcer, duodenal ulcer, gastroesophageal reflux disease and Zollinger-Ellison syndrome.
but currently there are **0 clinical trials** and only **1 general review article** supporting this direction, so this is a computational prediction and a research question rather than a validated use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9968 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 26 of 41) |
| Number of FDA Applications | 41 (active: 26) |
| Recommended Decision | Hold |

A second prediction, **duodenal obstruction** (score 0.9968), was also generated. It has no trials or literature (Evidence Level L5) and no clear mechanistic link, so it is not pursued further here.

## Why is This Prediction Reasonable?

Detailed mechanism of action data for lansoprazole is not available in the compiled data. Based on general knowledge, lansoprazole is a proton pump inhibitor that suppresses gastric acid secretion. Its established uses (GERD, esophagitis, peptic and duodenal ulcer) overlap with the clinical consequences of reflux.

Duodenogastric (bile) reflux is driven mainly by pyloric incompetence and altered motility, not by acid hypersecretion. Acid suppression would therefore be expected to ease symptoms and mucosal injury from mixed acid and bile exposure, but it would not correct the underlying reflux. The very high TxGNN score likely reflects network proximity to the approved gastric and esophageal indications and is a computational prediction only. The mechanistic link here is inferred from general PPI pharmacology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | Update on PPI clinical use and pharmacokinetics; PPIs are first-choice drugs for peptic ulcer, H. pylori infection, GERD, NSAID-induced GI lesions and Zollinger-Ellison syndrome. It does not address duodenogastric reflux directly. |

## US Market Information

<!-- review:begin us-lic-20261106-lansoprazole-1 -->

> **Review correction (2026-11-12)**: Originally stated: "Five more authorizations (all cancelled, 10 in total) are on record and not listed here." Removed: the number or status of FDA applications stated here did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 41 FDA applications for this drug, 26 active and 15 discontinued; the Quick Overview shows the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-lansoprazole-1 -->

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021428 | Prevacid SoluTab (Takeda) | Orally disintegrating delayed-release tablet | Not available (status: valid) |
| ANDA202366 | Lansoprazole (Bryant Ranch Prepack) | Delayed-release pellet capsule | Not available (status: valid) |
| ANDA200816 | Lansoprazole (Zydus) | Orally disintegrating tablet | Not available (status: valid) |
| ANDA205868 | Lansoprazole (Preferred Pharmaceuticals) | Delayed-release capsule | Not available (status: valid) |
| ANDA207394 | Lansoprazole (Medcore) | Delayed-release capsule | Not available (status: valid) |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** The graph links lansoprazole to conditions including long QT syndrome, torsades de pointes, liver failure and liver disease, kidney disease, porphyria, congestive heart failure, osteoporosis, myocardial infarction, stroke and cerebrovascular disorders, blood coagulation disease, anemia, *Clostridium difficile* colitis, and myasthenia gravis. These come from a computational graph and need to be verified against the official label.
- **Drug Interactions:** 100 interactions were found. Examples of **Major** interactions include acalabrutinib and atazanavir. **Moderate** examples include hydrochlorothiazide, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, aprepitant, atorvastatin, bosutinib, brigatinib and bromocriptine. **Minor** examples include acetylsalicylic acid, axitinib, brivaracetam and cyanocobalamin.

Please refer to the package insert for full warnings, as label warnings were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Mechanistically, acid suppression would at best relieve symptoms rather than treat the reflux itself.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- A targeted literature search on PPIs in bile or duodenogastric reflux, and a check of trial registries
- Confirmation of the current US marketing status of lansoprazole products
- Assessment of route and formulation compatibility, which is still pending

<!-- review:begin us-lic-20261106-lansoprazole-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Confirmation of the current US marketing status of lansoprazole products, since all 10 records are marked cancelled" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 41 FDA applications or NDC listings for this drug, 26 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-lansoprazole-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-12 | Removed: "Five more authorizations (all cancelled, 10 in total) are on record and not listed here" | Corrected (revised 2026-11-12; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "since all 10 records are marked cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


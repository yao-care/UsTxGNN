---
layout: default
title: Epinastine
parent: Model Prediction Only (L5)
nav_order: 659
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Epinastine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis"
monitor_inn: "EPINASTINE"
predicted_indications: ["rosacea conjunctivitis", "allergic urticaria"]
---

# Epinastine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Epinastine: From Allergic Conjunctivitis to Rosacea Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Epinastine is an antihistamine eye drop, originally used to treat allergic forms of conjunctivitis (atopic, papillary and vernal).
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but **0 clinical trials** and **0 publications** currently support this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 7) |
| Number of FDA Applications | 7 (active: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Epinastine is a histamine H1 receptor antagonist with mast-cell stabilizing activity. This description reflects its known drug class. According to the Mechanism of Action section of the FDA-approved prescribing information for epinastine: "Epinastine is a topically active, direct H 1 -receptor antagonist and an inhibitor of the release of histamine from the mast cell. Epinastine is selective for the histamine H 1 -receptor and has affinity for the histamine H 2 -receptor." ([DailyMed: epinastine hydrochloride prescribing information, Somerset Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4ee45c-e58f-4b7c-b389-898f5c27f54d), label version 2025-03-22; accessed 2026-11-19.)

Its efficacy is established in allergic conjunctival conditions, where histamine and mast-cell mediators drive itching and surface inflammation. Ocular rosacea involves meibomian gland dysfunction, inflammation and ocular surface irritation. It may also have an allergic or histamine-mediated component. That gives a plausible but only indirect link.

The very high TxGNN score (0.9957) is a computational prediction. It most likely reflects network proximity to the existing conjunctivitis indications rather than direct evidence in rosacea. No trials or publications were found to confirm it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

<!-- review:begin us-lic-20261031-epinastine-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The only US license on record is cancelled, so the drug's practical availability would need verification." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-epinastine-1 -->

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA090951 | Epinastine Hydrochloride (Somerset Therapeutics, LLC) | Solution / drops | Valid |

---

## Safety Considerations

Please refer to the package insert for safety information. No warning, contraindication or drug-interaction data were available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for rosacea conjunctivitis rests only on a model score, with no registered trials or literature (evidence level L5).

<!-- review:begin us-lic-20261031-epinastine-2 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction for rosacea conjunctivitis rests only on a model score, with no registered trials or literature (evidence level L5). The drug's only US license is cancelled, and label-level safety and mechanism data are missing." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-epinastine-2 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Targeted literature and trial searches on antihistamines or mast-cell stabilizers in ocular rosacea
- Consideration of the second-ranked prediction, **allergic urticaria** (score 0.9928, evidence level L3). It is supported by reviews and histamine wheal-and-flare studies in healthy volunteers, including a double-blind crossover RCT (PMID 10442525). These are surrogate pharmacodynamic data, not trials in urticaria patients, so it is best treated as a research question rather than a development candidate.

<!-- review:begin us-lic-20261031-epinastine-3 -->

> **Review correction (2026-10-31)**: Originally stated: "Targeted literature and trial searches on antihistamines or mast-cell stabilizers in ocular rosacea / Confirmation of current US availability, since the only license is cancelled" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-epinastine-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only US license on record is cancelled, so the drug's practical availability would need verification" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-10-31 | Removed: "The drug's only US license is cancelled, and label-level safety and mechanism data are missing" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-10-31 | Removed: "Confirmation of current US availability, since the only license is cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-20 | "Detailed mechanism of action data are not available in the data compiled for this report, so this description reflects its known drug class" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: epinastine hydrochloride prescribing information, Somerset Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4ee45c-e58f-4b7c-b389-898f5c27f54d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


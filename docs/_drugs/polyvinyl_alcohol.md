---
layout: default
title: Polyvinyl Alcohol
parent: Model Prediction Only (L5)
nav_order: 1063
evidence_level: L5
indication_count: 4
monitor_inn: "POLYVINYL ALCOHOL"
predicted_indications: ["congenital ichthyosiform erythroderma", "self-healing collodion baby", "lamellar ichthyosis", "bathing suit ichthyosis"]
last_modified_at: 2026-11-24
description: "Polyvinyl Alcohol: predicted new indication Congenital ichthyosiform erythroderma (evidence level L5). In the US: no FDA-approved application; 10 OTC monograph/unapproved NDC listings"
---

# Polyvinyl Alcohol
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

## Polyvinyl Alcohol: Congenital ichthyosiform erythroderma
{: .text-alpha }

## One-Sentence Summary

Polyvinyl alcohol is a polymer used in lubricating eye drops, originally for dry eye syndrome (xerophthalmia).
The TxGNN model predicts it may be effective for **Congenital Ichthyosiform Erythroderma** (and three related ichthyosis conditions), but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| US Market Status | Marketed (no FDA-approved application; OTC monograph / unapproved listings: 10) |
| Number of FDA Applications | 0 |
| Recommended Decision | Hold |

Other predicted indications, all L5 and Hold:

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 2 | Self-healing collodion baby | 0.9983 |
| 3 | Lamellar ichthyosis | 0.9972 |
| 4 | Bathing suit ichthyosis | 0.9954 |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, polyvinyl alcohol is a film-forming, hydrating polymer used as a lubricant in eye drops. Its benefit in dry eye comes from its moisture-retaining, protective properties, and mechanistically it might be applicable to dry, scaling skin conditions.

The predicted conditions are inherited disorders of skin keratinization (for example, mutations in TGM1, ALOXE3 or ALOX12B). A topical film-forming polymer could plausibly act as an occlusive or emollient layer and provide temporary relief of dryness and scaling. This would be symptomatic only and would not address the underlying genetic defect. There is also no data showing any advantage over established emollients and keratolytics.

Specific caveats for the other predictions:
- **Self-healing collodion baby:** the condition resolves on its own, so any benefit would be hard to separate from natural recovery. Use on neonates with impaired skin barrier also raises percutaneous absorption and safety questions that have not been evaluated.
- **Lamellar ichthyosis and bathing suit ichthyosis:** both are TGM1-related. Hydration and occlusion are standard supportive care, so the idea is conceptually consistent, but unsupported by data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDC 50090-5996 | Rugby Lubricating Drops | A-S Medication Solutions | Solution/ drops | NDC listing, no FDA application (OTC monograph drug) |
| NDC 50090-7119 | Polyvinyl Alcohol | A-S Medication Solutions | Solution/ drops | NDC listing, no FDA application (OTC monograph drug) |
| NDC 50090-7606 | Rugby Polyvinyl Alcohol 1.4% Lubricating Eye Drops | A-S Medication Solutions | Solution/ drops | NDC listing, no FDA application (OTC monograph drug) |
| NDC 50268-678 | Polyvinyl Alcohol | AvPAK | Solution/ drops | NDC listing, no FDA application (OTC monograph drug) |
| NDC 0363-0796 | Walgreens Soothing Eye Relief Lubricant Eye Drops | Walgreens Co. | Solution/ drops | NDC listing, no FDA application (OTC monograph drug) |

Showing 5 of 10 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

The drug is currently marketed in the US.

<!-- review:begin us-lic-20261106-polyvinyl_alcohol-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is currently marketed in the US, with 1 valid license." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-polyvinyl_alcohol-2 -->

## Safety Considerations

The data compiled for this report includes no label-based warnings or contraindications, and no drug interactions were found. Please refer to the package insert for safety information.

The knowledge graph links the drug to the following conditions as contraindication relationships. These come from a computational resource, not from label text, and should be verified:
- **Cardiovascular:** hypertension, heart disease, cardiovascular disease, coronary artery disease, sudden cardiac arrest, heart conduction disease, arteriosclerosis, atherosclerosis
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
- **Other:** benign prostatic hyperplasia, angle-closure glaucoma

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications.

<!-- review:begin us-lic-20261031-polyvinyl_alcohol-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction rests only on a model score, with no clinical trials or publications. The mechanistic link is speculative and symptomatic at best, and the only US authorization is cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-polyvinyl_alcohol-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence of benefit in ichthyosis, compared with standard emollients
- Safety and percutaneous absorption assessment for topical use, especially in neonates with impaired skin barrier
- Assessment of route and formulation compatibility (the current product is an ophthalmic solution, while the predicted use is dermatological)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The mechanistic link is speculative and symptomatic at best, and the only US authorization is cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 1 valid license" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


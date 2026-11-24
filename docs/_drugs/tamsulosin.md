---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 1199
evidence_level: L5
indication_count: 10
monitor_inn: "TAMSULOSIN"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine with brainstem aura"]
last_modified_at: 2026-11-24
description: "Tamsulosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
---

# Tamsulosin
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

## Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita
{: .text-alpha }

## One-Sentence Summary

Tamsulosin is an alpha-1 adrenoceptor antagonist originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 14 of 21) |
| Number of FDA Applications | 21 (active: 14) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for tamsulosin: "The symptoms associated with benign prostatic hyperplasia (BPH) are related to bladder outlet obstruction, which is comprised of two underlying components: static and dynamic. The static component is related to an increase in prostate size caused, in part, by a proliferation of smooth muscle cells in the prostatic stroma. […] Tamsulosin, an alpha 1 adrenoceptor blocking agent, exhibits selectivity for alpha 1 receptors in the human prostate." ([DailyMed: tamsulosin hydrochloride prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6b6aeab-bedd-4254-8811-4f65cf8a351f), label version 2026-11-12; accessed 2026-11-19.) Based on general pharmacology, tamsulosin is an alpha-1A/1D adrenoceptor antagonist that relaxes smooth muscle in the prostate and bladder neck. Its efficacy in BPH is established.

No established mechanism links this action to Ambras syndrome. Ambras syndrome is a rare congenital disorder associated with genomic rearrangements at 8q22 that affect regulation of the *TRPS1* gene. An alpha-1 blocker would not be expected to act on this pathway.

The very high score (1.0000, model rank 246) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Without trials or literature, this prediction should be treated as a computational hypothesis only.

**Other predictions in the top 10** are similarly unsupported. They include hypertrichosis, dental and periodontal malformation syndromes, Dandy-Walker malformation syndromes, hair shaft abnormalities, hypotrichosis, alopecia areata, alopecia, and migraine with brainstem aura. All are at evidence level L5 with a Hold recommendation. Hypertrichosis in particular would normally be an adverse effect rather than a therapeutic goal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

(For the rank 9 prediction, alopecia, two papers were retrieved. Neither supports tamsulosin: one is a finasteride pharmacovigilance study on suicidality and psychological adverse events, and the other is an observational study of meibomian gland changes in men with BPH. Both are only tangentially related.)

## US Market Information

No approved indication text is available for them.

<!-- review:begin us-lic-20261105-tamsulosin-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All six US authorizations are valid generic applications for oral capsules. No approved indication text is available for them." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-tamsulosin-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA077630 | TAMSULOSIN HYDROCHLORIDE | TEVA PHARMS | Capsule; oral | Valid |
| ANDA078225 | TAMSULOSIN HYDROCHLORIDE | ZYDUS PHARMS USA INC | Capsule; oral | Valid |
| ANDA078801 | TAMSULOSIN HYDROCHLORIDE | SYNTHON BV | Capsule; oral | Valid |
| ANDA078938 | TAMSULOSIN HYDROCHLORIDE | SCIEGEN PHARMS | Capsule; oral | Valid |
| ANDA090377 | TAMSULOSIN HYDROCHLORIDE | IMPAX LABS | Capsule; oral | Valid |

Showing 5 of 21 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph** (not label text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism, and intraoperative floppy iris syndrome.
- **Drug Interactions**: 100 interactions were identified. Of the 20 listed in the compiled data, one is rated Major and the rest Moderate.
  - **Major**: Clarithromycin.
  - **Moderate (examples)**: cimetidine, bupropion, aprepitant, morphine, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, clotrimazole, miconazole, and eliglustat.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no supporting literature, and no plausible mechanistic link to the predicted condition. Evidence is at level L5 (model prediction only). In addition, tamsulosin is marketed in the US.

<!-- review:begin us-lic-20261106-tamsulosin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "In addition, tamsulosin is marketed in the US with 6 valid licenses." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-tamsulosin-2 -->

**To proceed, the following is needed:**
- Mechanistic evidence connecting alpha-1A/1D blockade to the *TRPS1* or 8q22-related pathology of Ambras syndrome, or a rationale for choosing another prediction.
- Detailed mechanism of action data (MOA).
- Package insert warnings and contraindications, to allow safety screening.
- Preclinical studies (for example in cell or animal models) before any clinical consideration.
- Clarification of current US marketing status.

<!-- review:begin us-lic-20261106-tamsulosin-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of current US marketing status, since 6 valid licenses are listed." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-tamsulosin-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All six US authorizations are valid generic applications for oral capsules" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 6 valid licenses" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "since 6 valid licenses are listed" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: tamsulosin hydrochloride prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6b6aeab-bedd-4254-8811-4f65cf8a351f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


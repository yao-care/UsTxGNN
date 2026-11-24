---
layout: default
title: Guanfacine
parent: Model Prediction Only (L5)
nav_order: 764
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Guanfacine: predicted new indication Faciodigitogenital syndrome (evidence level L5). Approved use: Hypertension"
monitor_inn: "GUANFACINE"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "trichotillomania", "manic bipolar affective disorder", "restless legs syndrome", "Tourette syndrome"]
---

# Guanfacine
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

## Guanfacine: From Hypertension and ADHD to Faciodigitogenital Syndrome
{: .text-alpha }

## One-Sentence Summary

Guanfacine is an alpha-2A adrenergic agonist, originally used to treat hypertension and attention deficit hyperactivity disorder (ADHD).
The TxGNN model predicts it may be effective for **Faciodigitogenital Syndrome**, a rare genetic developmental disorder.
Currently **0 clinical trials** and **0 publications** support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension; attention deficit hyperactivity disorder (ADHD) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Marketed (active FDA-approved applications: 21 of 27) |
| Number of FDA Applications | 27 (active: 21) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for guanfacine: "Guanfacine is a central alpha 2A -adrenergic receptor agonist. Guanfacine is not a central nervous system (CNS) stimulant. The mechanism of action of guanfacine in ADHD is not known." ([DailyMed: Guanfacine Extended-Release (guanfacine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3ec4fed6-cafc-49a0-9540-8d70ac435769), label version 2026-10-15; accessed 2026-11-19.) Guanfacine is known to be a selective alpha-2A adrenergic agonist. It strengthens prefrontal cortical regulation and reduces noradrenergic tone, which underlies its effects in hypertension and ADHD.

The predicted disease is a rare genetic developmental disorder. No plausible mechanistic connection between alpha-2A agonism and this condition was identified. The high model score is not backed by any clinical trial or published study, so the prediction should be treated as a computational signal that has not been validated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The five main ones are listed below, and the approved indication text is not specified in the authorization records.

<!-- review:begin us-lic-20261106-guanfacine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "There are 11 valid authorizations. The five main ones are listed below, and the approved indication text is not specified in the authorization records." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-guanfacine-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA074145 | GUANFACINE HYDROCHLORIDE | WATSON LABS | Tablet; oral | Valid |
| ANDA074673 | GUANFACINE HYDROCHLORIDE | EPIC PHARMA LLC | Tablet; oral | Valid |
| ANDA074796 | GUANFACINE HYDROCHLORIDE | AUROBINDO PHARMA USA | Tablet; oral | Valid |
| ANDA075109 | GUANFACINE HYDROCHLORIDE | AMNEAL PHARM | Tablet; oral | Valid |
| ANDA200881 | GUANFACINE HYDROCHLORIDE | ACTAVIS ELIZABETH | Tablet, extended release; oral | Valid |

Showing 5 of 27 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. Major-level interactions include **aprepitant**, **dexamethasone** and **clarithromycin**. Many other interactions are moderate, including corticosteroids (hydrocortisone, prednisone, prednisolone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), metformin, cimetidine, miconazole, and cannabinoids (dronabinol, nabilone).
- **Knowledge-graph-derived cautions** (these are drug-disease associations, not label text): orthostatic hypotension and other hypotensive disorders, myocardial infarction and coronary artery disease, atrioventricular block, cerebrovascular disorder, chronic kidney disease and end-stage renal failure, liver and gallbladder disease, anxiety and dysthymic disorders, constipation, multiple system atrophy, and postural orthostatic tachycardia syndrome.

Please refer to the package insert for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and no plausible biological link to alpha-2A agonism was found. The drug is marketed in the US. The score alone is not enough to justify further investment.

<!-- review:begin us-lic-20261106-guanfacine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with 11 valid authorizations." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-guanfacine-2 -->

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking guanfacine to this disorder
- Any preclinical or clinical evidence in the predicted indication
- The full package insert warnings and contraindications

**Note on other predictions:** Among the other predictions for guanfacine, **Tourette syndrome** has by far the strongest support. It has a completed Phase 3 placebo-controlled trial (NCT00004376, n=35), a completed Phase 4 study (NCT01547000, n=34), and European guideline support for alpha-2 agonists in tics, particularly with comorbid ADHD. It would be a better candidate to evaluate in a separate report, with guardrails.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "There are 11 valid authorizations" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 11 valid authorizations" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Guanfacine Extended-Release (guanfacine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3ec4fed6-cafc-49a0-9540-8d70ac435769) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


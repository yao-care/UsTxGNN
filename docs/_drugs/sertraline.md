---
layout: default
title: Sertraline
parent: Model Prediction Only (L5)
nav_order: 1157
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "SERTRALINE"
predicted_indications: ["paranoid personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "schizotypal personality disorder", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder"]
description: "Sertraline: predicted new indication Paranoid personality disorder (evidence level L5). In the US: 39 FDA applications (24 active)"
---

# Sertraline
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

## Sertraline: Paranoid personality disorder
{: .text-alpha }

## One-Sentence Summary

Sertraline is an SSRI antidepressant that is marketed in the United States in several oral and concentrate forms. The TxGNN model predicts it may be useful for **paranoid personality disorder**, with a score of 0.9993. **No clinical trials** and **no publications that directly study this disease** were found, so the prediction is currently model-based only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Paranoid personality disorder |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 24 of 39) |
| Number of FDA Applications | 39 (active: 24) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for sertraline: "Sertraline potentiates serotonergic activity in the central nervous system through inhibition of neuronal reuptake of serotonin (5-HT)." ([DailyMed: Zoloft (sertraline hydrochloride) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda754f6-d0f3-4dce-a17a-927d64f912f7), label version 2023-08-08; accessed 2026-11-19.) Sertraline is an SSRI, and serotonergic modulation may reduce affective instability, anxiety and impulsivity. These symptoms often accompany personality disorders, so a mechanistic link to this group of conditions is plausible.

The literature retrieved concerns other conditions: borderline personality disorder, personality-disorder comorbidity in depression, and sertraline augmentation. None of it studies paranoid personality disorder. The same very high score (0.9993) is shared by several unrelated personality disorders. It most likely reflects a class-level model prediction rather than disease-specific evidence. Any benefit would probably be on comorbid mood or anxiety symptoms, not on the core paranoid traits.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below directly studies paranoid personality disorder, so they are indirect evidence at best.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9817625](https://pubmed.ncbi.nlm.nih.gov/9817625/) | 1998 | Secondary analysis of an RCT | International Clinical Psychopharmacology | In 308 primary-care patients with major depression, personality-disorder diagnoses were assessed before and after 24 weeks of double-blind sertraline or a comparator antidepressant. It addresses comorbidity and treatment response, not paranoid personality disorder. |
| [18848360](https://pubmed.ncbi.nlm.nih.gov/18848360/) | 2008 | Open-label trial | Psychiatry Research | Aripiprazole was added for 12 weeks in 21 patients with borderline personality disorder who had not responded to sertraline. It concerns a different personality disorder and tests the add-on drug. |
| [36853245](https://pubmed.ncbi.nlm.nih.gov/36853245/) | 2023 | Review | JAMA | General review of borderline personality disorder, covering prevalence and its social and vocational impact. It is not specific to sertraline or paranoid personality disorder. |
| [11686052](https://pubmed.ncbi.nlm.nih.gov/11686052/) | 2001 | Review | L'Encéphale | Review of psychiatric side effects of alpha-interferon. It is off-target. |

---

## US Market Information

The list may be partial. Indication text is not recorded in the local data.

<!-- review:begin us-lic-20261106-sertraline-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Eight valid US licences for single-ingredient sertraline are recorded. The list may be partial." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-sertraline-1 -->

<!-- review:begin us-lic-20261106-sertraline-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Indication text is not recorded in the local data for these licences." Removed: it conflicted with the FDA application data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-sertraline-2 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA076442 | SERTRALINE HYDROCHLORIDE | SCIEGEN PHARMS | Tablet; oral | Valid |
| ANDA076465 | SERTRALINE HYDROCHLORIDE | HERITAGE | Tablet; oral | Valid |
| ANDA076881 | SERTRALINE HYDROCHLORIDE | STRIDES PHARMA | Tablet; oral | Valid |
| ANDA076882 | SERTRALINE HYDROCHLORIDE | MACLEODS PHARMS | Tablet; oral | Valid |
| ANDA076934 | SERTRALINE HYDROCHLORIDE | STRIDES PHARMA | Concentrate; oral | Valid |

Showing 5 of 39 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

---

## Safety Considerations

- **Conditions recorded as cautions for sertraline** (from the compiled data, not from label text): epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, and serotonin syndrome.
- **Drug Interactions**: 100 interactions are recorded. Those rated **Major** include bupropion, lorcaserin, diethylpropion, dolasetron, eliglustat, palonosetron and phentermine. Moderate examples include famotidine, loperamide, morphine, acetylsalicylic acid, clarithromycin and glimepiride.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9993), but it is shared across several unrelated personality disorders. No clinical trial or publication directly studies sertraline in paranoid personality disorder, so the evidence level is L5.

**To proceed, the following is needed:**
- Disease-specific clinical or observational data on sertraline in paranoid personality disorder
- Detailed mechanism-of-action data and a mechanistic rationale specific to paranoid traits
- Review of the full package insert warnings and contraindications, particularly for psychiatric comorbidity
- A defined interaction-management plan covering the major interactions listed above

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Eight valid US licences for single-ingredient sertraline are recorded" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "for these licences" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zoloft (sertraline hydrochloride) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda754f6-d0f3-4dce-a17a-927d64f912f7) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


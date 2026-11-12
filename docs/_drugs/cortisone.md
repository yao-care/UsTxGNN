---
layout: default
title: Cortisone
parent: Moderate Evidence (L3-L4)
nav_order: 550
evidence_level: L4
indication_count: 7
monitor_inn: "CORTISONE"
predicted_indications: ["primary cutaneous T-cell lymphoma", "myelodysplastic syndrome", "lymphosarcoma", "candidiasis", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5"]
last_modified_at: 2026-11-12
description: "Cortisone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L4). Approved use: Not recorded in the local data"
---

# Cortisone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

## Cortisone: Primary cutaneous T-cell lymphoma
{: .text-alpha }

## One-Sentence Summary

Cortisone is a corticosteroid that the body converts into its active form, cortisol. The TxGNN model predicts it may be useful for **primary cutaneous T-cell lymphoma**. The supporting evidence is thin: **no registered clinical trial tests cortisone in this disease**, and the only disease-specific literature is a handful of **1950s–1960s case reports in mycosis fungoides**, the most common form of this lymphoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L4 |
| US Market Status | Marketed (active FDA-approved applications: 0 of 20; OTC monograph / unapproved listings: 65) |
| Number of FDA Applications | 20 (active: 0) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for cortisone is not available in the data compiled for this report. Pharmacologically, glucocorticoids can induce apoptosis in lymphoid cells through the glucocorticoid receptor. This gives a plausible basis for activity in T-cell lymphomas, and glucocorticoids are still used as components of lymphoma regimens.

Cortisone itself is a prodrug. It must be converted to cortisol by the enzyme 11-beta-hydroxysteroid dehydrogenase type 1 (11β-HSD1) before it becomes active, which adds a layer of uncertainty compared with directly active steroids.

The disease-specific support is anecdotal. Only a few early case reports describe cortisone in mycosis fungoides, and their abstracts are not available. Current practice relies on topical corticosteroids for early-stage disease and other systemic agents for advanced disease. Cortisone has no established role in modern treatment, so the high model score reflects a pattern-based prediction rather than demonstrated clinical benefit.

---

## Clinical Trial Evidence

No registered trial studies cortisone in primary cutaneous T-cell lymphoma. The only trial returned for this prediction is listed below. It concerns a different disease, does not test cortisone, and is shown only for completeness.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04799275](https://clinicaltrials.gov/study/NCT04799275) | Phase 2/3 | Active, not recruiting | 422 | R-miniCHOP with or without oral azacitidine in patients aged 75+ with diffuse large B-cell lymphoma. Prednisone is only part of the chemotherapy backbone, so it gives no evidence for cortisone in cutaneous T-cell lymphoma. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14896727](https://pubmed.ncbi.nlm.nih.gov/14896727/) | 1951 | Case report | Dermatologica | Effects of cortisone in two cases of mycosis fungoides (abstract not available) |
| [13612293](https://pubmed.ncbi.nlm.nih.gov/13612293/) | 1958 | Case report | Lyon medical | Two cases of mycosis treated with delta-cortisone; a terminal ulceronecrotic process was thought to be linked to the medication |
| [14884116](https://pubmed.ncbi.nlm.nih.gov/14884116/) | 1951 | Case report | Svenska lakartidningen | Combined ACTH and cortisone therapy in a patient with impetigo herpetiformis, mycosis fungoides and erythroderma psoriatica |
| [13536705](https://pubmed.ncbi.nlm.nih.gov/13536705/) | 1957 | Case report | Bulletin de la Société française de dermatologie et de syphiligraphie | Two cases of bronchial epithelioma in patients with mycosis fungoides treated with cortisone |
| [14169182](https://pubmed.ncbi.nlm.nih.gov/14169182/) | 1964 | Review | Journal de médecine et de chirurgie pratiques | General review of mycosis fungoides (abstract not available) |

All of these are old, small, descriptive reports with no controlled comparison. They are not reliable evidence of efficacy.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not recorded | Cortisone aceticum (Boiron) | Pellet | Not recorded in the local data |
| ANDA080694 | Cortisone Acetate (Chartwell RX, LLC) | Tablet | Not recorded in the local data |

Cortisone is marketed in the US.

<!-- review:begin us-lic-20261105-cortisone-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Cortisone is marketed in the US. One record is currently valid (the pellet product) and one is cancelled (the tablet product)." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 20 FDA applications or NDC listings for this drug, 0 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-cortisone-1 -->

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is high (0.9967), and glucocorticoids have a plausible lympholytic mechanism. However, the evidence level is L4: the only disease-specific data are 1950s–1960s case reports in mycosis fungoides, and no trial tests cortisone in this disease. Cortisone is also a prodrug with no established role in current cutaneous T-cell lymphoma care.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications, since safety data is currently missing
- Mechanism-of-action data, including cortisone-to-cortisol conversion in skin and lymphoma tissue
- A comparison against current standard options (topical corticosteroids, other systemic agents) to see whether cortisone adds anything
- Preclinical or early clinical data in cutaneous T-cell lymphoma showing a benefit that justifies a prospective study

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "One record is currently valid (the pellet product) and one is cancelled (the tablet product)" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


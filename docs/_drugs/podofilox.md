---
layout: default
title: Podofilox
parent: Model Prediction Only (L5)
nav_order: 1057
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Podofilox: predicted new indication Vulvovaginal candidiasis (evidence level L5). Approved use: Anogenital human papillomavirus infection"
monitor_inn: "PODOFILOX"
predicted_indications: ["vulvovaginal candidiasis", "photosensitivity disease", "herpes zoster", "benign neoplasm of tongue", "benign neoplasm of hypopharynx", "cystic neoplasm", "mesenchymoma", "nasal cavity inverting papilloma", "tumor of testis and paratestis"]
---

# Podofilox
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Podofilox: From Anogenital HPV Infection and Common Warts to Vulvovaginal Candidiasis
{: .text-alpha }

## One-Sentence Summary

Podofilox is a topical antimitotic agent, originally used for anogenital human papillomavirus (HPV) infection (genital warts) and common warts.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but there are **0 clinical trials** and only **1 publication** (a 1999 general review that does not address this use), so the prediction is **not supported by direct evidence**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anogenital human papillomavirus infection; common wart |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 0.9947 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 5) |
| Number of FDA Applications | 5 (active: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Podofilox (podophyllotoxin) is generally known as an antimitotic agent that inhibits tubulin polymerization. It kills rapidly dividing HPV-infected skin cells and causes local necrosis of wart tissue. This is why it works for genital warts and common warts.

Vulvovaginal candidiasis is a fungal infection, not a viral or proliferative skin lesion. An antimitotic wart treatment has no known antifungal activity, so **no credible mechanistic link was found**. The only related literature is a 1999 review of treatments for common sexually transmitted diseases. It discusses vaginal infections and genital warts side by side, but it does not suggest podofilox for candidiasis.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related anogenital conditions that tend to occur together (genital warts and vaginal infections), not biological evidence or a pharmacological relationship. The score should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10537386](https://pubmed.ncbi.nlm.nih.gov/10537386/) | 1999 | Review | American Family Physician | General review of CDC 1998 STD treatment guidelines covering vaginal infections, pelvic inflammatory disease, and genital warts. It does not support podofilox use for candidiasis. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA075600 | Podofilox | Solution | Valid |
| ANDA211871 | Podofilox | Gel | Valid |

Both authorizations are held by Padagis US LLC. No approved indication text was available for either one.

<!-- review:begin us-lic-20261106-podofilox-1 -->

> **Review correction (2026-11-06)**: Originally stated: "No approved indication text was available for either one. Neither product is currently active, so availability would need to be verified." Removed: it conflicted with the FDA application data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 5 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-podofilox-1 -->

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no clinical trials and no supporting literature. There is also no plausible mechanism linking an antimitotic wart treatment to a fungal infection, and established antifungal therapies already exist.

<!-- review:begin us-lic-20261106-podofilox-2 -->

> **Review correction (2026-11-06)**: Originally stated: "There is also no plausible mechanism linking an antimitotic wart treatment to a fungal infection, and established antifungal therapies already exist. Both US licenses are cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 5 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-podofilox-2 -->

**To proceed, the following is needed:**
- Any preclinical or clinical evidence of antifungal activity against *Candida* species (none identified so far)
- Detailed mechanism of action data
- Review of the FDA package insert for warnings and contraindications, especially for application to vaginal mucosa
- Confirmation of current product availability

<!-- review:begin us-lic-20261106-podofilox-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Confirmation of current product availability, since both US licenses are cancelled" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 5 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-podofilox-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Neither product is currently active, so availability would need to be verified" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "Both US licenses are cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "since both US licenses are cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


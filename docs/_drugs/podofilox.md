---
layout: default
title: Podofilox
parent: Model Prediction Only (L5)
nav_order: 1057
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
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
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of FDA Applications | 2 (valid: 2) |
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

Both authorizations are held by Padagis US LLC. No approved indication text was available for either one. Neither product is currently active, so availability would need to be verified.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no clinical trials and no supporting literature. There is also no plausible mechanism linking an antimitotic wart treatment to a fungal infection, and established antifungal therapies already exist. Both US licenses are cancelled.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence of antifungal activity against *Candida* species (none identified so far)
- Detailed mechanism of action data
- Review of the FDA package insert for warnings and contraindications, especially for application to vaginal mucosa
- Confirmation of current product availability, since both US licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


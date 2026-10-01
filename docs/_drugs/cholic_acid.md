---
layout: default
title: Cholic Acid
parent: Model Prediction Only (L5)
nav_order: 527
evidence_level: L5
indication_count: 10
---

# Cholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Cholic Acid: From Bile Acid Synthesis Disorders to HIV Infectious Disease

## One-Sentence Summary

Cholic acid is a primary bile acid, marketed in the US as CHOLBAM capsules. The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are **0 clinical trials** and **9 publications**, none showing therapeutic benefit. One in vitro study points toward harm, so this high-scoring prediction is not supported by the evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data (approved indication text is empty). Registry and literature in the pack indicate bile acid synthesis disorders. |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 (preclinical and in vitro only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license records (both NDA205750) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for cholic acid in this Evidence Pack. It is a primary bile acid. Replacing it in bile acid synthesis disorders reduces toxic bile acid intermediates and restores fat and vitamin absorption. This physiology has no established link to HIV.

The only mechanistic signals in the literature are indirect. In a 1993 study, sodium cholate showed detergent-like spermicidal and antiviral activity, including in vitro inhibition of HIV-1 reverse transcriptase. This was in a topical vaginal sponge combined with nonoxynol-9 and benzalkonium chloride. That is membrane-disrupting, non-systemic activity and does not support oral use for HIV treatment.

A 2006 study found the opposite direction. Synthetic cholic acid derivatives **increased** HIV-1 replication and syncytia formation in T cells. The other retrieved papers are reviews on barrier contraception, HIV-related liver disease, viral sterilisation of blood products, and an assay methodology paper. The very high TxGNN score is not backed by any therapeutic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16610808](https://pubmed.ncbi.nlm.nih.gov/16610808/) | 2006 | In vitro | J Med Chem | Cholic acid derivatives induced syncytia and enhanced HIV-1 replication in T cells (a signal of harm) |
| [7688380](https://pubmed.ncbi.nlm.nih.gov/7688380/) | 1993 | Preclinical / contraceptive study | Hum Reprod | Sodium cholate showed spermicidal and in vitro anti-HIV-1 activity, including reverse transcriptase inhibition, in a vaginal sponge with nonoxynol-9 |
| [2870224](https://pubmed.ncbi.nlm.nih.gov/2870224/) | 1986 | In vitro | Lancet | Tri(n-butyl)phosphate plus sodium cholate sterilised hepatitis and HTLV-III viruses in blood products (a virus-inactivation use, not a treatment) |
| [20030469](https://pubmed.ncbi.nlm.nih.gov/20030469/) | 2010 | Cohort | Pharmacotherapy | Plasma bile acids in HIV patients on protease inhibitors, examined as possible hepatotoxicity predictors |
| [32052857](https://pubmed.ncbi.nlm.nih.gov/32052857/) | 2020 | Review | Hepatology | NASH drugs in people living with HIV and drug interaction concerns |
| [9238301](https://pubmed.ncbi.nlm.nih.gov/9238301/) | 1997 | Review | Ann N Y Acad Sci | Anti-STD vaginal contraceptive sponges |
| [7848210](https://pubmed.ncbi.nlm.nih.gov/7848210/) | 1994 | Review | Aust N Z J Obstet Gynaecol | Future contraceptives and STD/HIV protection |
| [8849197](https://pubmed.ncbi.nlm.nih.gov/8849197/) | 1995 | Review | Ann Acad Med Singapore | Barrier methods and protection against STDs including HIV |
| [28745428](https://pubmed.ncbi.nlm.nih.gov/28745428/) | 2017 | In vitro (assay methodology) | ChemMedChem | Triton X-100 detergent affects HIV-1 protease inhibitor assay results; not related to cholic acid therapy |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205750 | CHOLBAM (Mirum Pharmaceuticals Inc.) | Capsule (oral) | Not stated in the license data |

The pack lists two identical records for this NDA, shown once here.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

One signal from the literature is relevant here: cholic acid derivatives enhanced HIV-1 replication in vitro (PMID 16610808). This has not been tested in patients, but it must be resolved before any HIV use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no therapeutic literature, and one in vitro study suggests possible harm. The model score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- Package insert warnings, contraindications, and approved indication text (not yet retrieved)
- Mechanism of action data from DrugBank
- Direct in vitro evidence that cholic acid itself, not derivatives or detergent formulations, has antiviral activity without enhancing HIV replication
- Any support for a plausible systemic HIV mechanism; otherwise, deprioritise this prediction

**Other predictions:** "Vitamin deficiency disorder" (rank 5, L3) is the best supported of the ten, but it is a downstream consequence of the labeled bile acid synthesis disorder use, not an independent repurposing target. The other predictions are prediction-only, negative, or unrelated.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


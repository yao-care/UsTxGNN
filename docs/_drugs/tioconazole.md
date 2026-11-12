---
layout: default
title: Tioconazole
parent: Model Prediction Only (L5)
nav_order: 1230
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-06
monitor_inn: "TIOCONAZOLE"
predicted_indications: ["vulvitis", "postmenopausal atrophic vaginitis"]
description: "Tioconazole: predicted new indication Vulvitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Tioconazole
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

## Tioconazole: Vulvitis
{: .text-alpha }

## One-Sentence Summary

Tioconazole is a topical imidazole antifungal that blocks ergosterol synthesis in fungi and yeasts. The TxGNN model predicts it may be useful for **vulvitis**, with a score of 0.9920. No clinical trials are registered for vulvitis itself. The available literature covers vaginal Candida infection and does not study vulvitis as a separate endpoint.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvitis |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 3) |
| Number of FDA Applications | 3 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Tioconazole's molecular target in fungi and yeasts is lanosterol 14-α demethylase (CYP51/ERG11). This enzyme converts lanosterol to ergosterol, an essential cell membrane component. Without ergosterol the organism cannot survive. Tioconazole also inhibits the human enzyme CYP8B1, which takes part in bile acid synthesis. Detailed mechanism-of-action data were not available in the data compiled for this report, so the mechanism above comes from pharmacology data and the general azole class.

Vulvitis often occurs together with yeast infection of the lower genital tract. Where the vulvar inflammation is caused by Candida, an azole antifungal could plausibly help. This reasoning holds only for the fungal subset. Vulvitis from non-infectious or non-fungal causes (irritant, allergic, or other causes) would not be expected to respond to an antifungal. The literature retrieved does not separate vulvitis from general vaginal Candida infection, so the link remains an inference.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these publications studies vulvitis as a stand-alone condition. They describe tioconazole in vaginal and vulvar Candida infection and related genital infections.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | Broad in vitro activity against dermatophytes and yeasts. Controlled and open trials show efficacy and safety of topical tioconazole in superficial yeast and dermatophyte infections. |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | Double-blind placebo-controlled trial | Gynakologische Rundschau | Tioconazole compared with placebo in vaginal Candida infection, with assessment of systemic absorption. |
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | Randomized comparative study | Antimicrob Agents Chemother | 80 patients. Single-dose 6.5% tioconazole ointment gave 84% asymptomatic at 4 weeks, versus 85% for 3-day clotrimazole. |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Clinical study | Acta Obstet Gynecol Scand | Tioconazole 2% vaginal cream gave an 88.5% mycological cure rate in symptomatic women. |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Open randomized study | J Int Med Res | 40 patients. Single-dose topical tioconazole 6% was compared with 5 days of oral ketoconazole. Both were effective, and symptoms resolved faster with topical therapy. |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Open-label comparative trial | Gynakologische Rundschau | 3-day treatment with tioconazole compared with econazole. |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Open-label comparative trial | Gynakologische Rundschau | Tioconazole cream compared with econazole ovules over 3 days. |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Open non-comparative study | J Int Med Res | 20 patients with Trichomonas or mixed vaginal infections. Tioconazole 2% cream cured 95% (19/20) at first follow-up. |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | Overview of non-invasive azole antifungal options and future directions for vaginal Candida infection. |
| [10990271](https://pubmed.ncbi.nlm.nih.gov/10990271/) | 2000 | Laboratory study | Microb Drug Resist | Cross-resistance of Candida isolates to over-the-counter azoles, a concern for repeated azole use. |

## US Market Information

<!-- review:begin us-lic-20261112-tioconazole-1 -->

> **Review correction (2026-11-12)**: Originally stated: "The local records show one licence, and it is valid." Removed: the number or status of FDA applications stated here did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 3 FDA applications for this drug, 2 active and 1 discontinued; the Quick Overview shows the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261112-tioconazole-1 -->

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075915 | Tioconazole (CVS Pharmacy) | Ointment | Not specified |

## Safety Considerations

- **Drug Interactions**:
  - Omeprazole: an interaction is listed, but its severity level is not specified.
  - CYP8B1 (human enzyme): tioconazole inhibits this enzyme, which participates in bile acid biosynthesis.
- Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9920), but no clinical trial or publication studies vulvitis itself, so the evidence level is L5. The antifungal mechanism could apply only to the Candida-related subset of vulvitis, and the supporting literature does not separate vulvitis from general vaginal Candida infection.

**To proceed, the following is needed:**
- Studies or case series that define vulvitis as a distinct endpoint, separating Candida-related from non-fungal causes
- Package insert warnings and contraindications for the marketed ointment
- Confirmation that the marketed ointment's dosage form and route suit vulvar application
- A clinical plan limited to culture-confirmed or clinically suspected fungal vulvitis

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-12 | Removed: "The local records show one licence, and it is valid" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


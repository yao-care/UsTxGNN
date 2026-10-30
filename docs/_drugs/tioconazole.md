---
layout: default
title: Tioconazole
parent: Model Prediction Only (L5)
nav_order: 1230
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "TIOCONAZOLE"
predicted_indications: ["vulvovaginitis", "vulvitis", "postmenopausal atrophic vaginitis"]
description: "Tioconazole: predicted new indication Vulvovaginitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Tioconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Tioconazole: Vulvovaginitis
{: .text-alpha }

## One-Sentence Summary

Tioconazole is a topical imidazole antifungal originally used to treat vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **vulvovaginitis**, but this is largely an extension of the original indication (the Candida-driven subtype).
Currently there are **0 registered clinical trials** and **19 publications** (mostly older clinical studies and reviews on vaginal candidiasis) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Tioconazole is an imidazole antifungal. In fungi and yeast, it inhibits the cytochrome P450 enzyme lanosterol 14-alpha-demethylase (CYP51/ERG11), which blocks ergosterol synthesis and disrupts the fungal cell membrane. It also inhibits the human enzyme CYP8B1, which is involved in bile acid biosynthesis.

Vulvovaginal candidiasis is one of the most common causes of vulvovaginitis, so the prediction is mainly an extension of the original indication rather than true repurposing. It applies only where the inflammation is caused by Candida. Bacterial vaginosis, trichomoniasis, and atrophic or irritant forms are not expected to respond to an antifungal.

Note that detailed mechanism-of-action data was not available in the data compiled for this report, so the mechanism above relies on the known azole class and pharmacology data.

Two other predictions were also generated:
- **Vulvitis** (score 0.9920, L3): overlaps with candidiasis, but the literature does not isolate vulvitis as its own endpoint.
- **Postmenopausal atrophic vaginitis** (score 0.9919, L5): no mechanistic rationale, since the condition is driven by estrogen deficiency rather than infection. No trials or literature exist, and the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. This prediction should be set aside.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Most relevant publications (all concern vaginal candidiasis, not vulvovaginitis as a separate endpoint):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | Double-blind placebo-controlled trial | Gynakologische Rundschau | Tioconazole vs placebo in vaginal candidiasis, including systemic absorption assessment |
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | Randomized comparative study | Antimicrob Agents Chemother | Single-dose 6.5% tioconazole ointment vs 3-day clotrimazole: 84% vs 85% asymptomatic at 4 weeks |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Randomized open study | J Int Med Res | Topical tioconazole 6% vs oral ketoconazole (40 patients): both eradicated disease; topical symptoms resolved faster |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | Broad antimicrobial activity; trials show efficacy and safety of topical tioconazole in superficial yeast infections and vaginal candidiasis |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Clinical study | Acta Obstet Gynecol Scand | Tioconazole 2% vaginal cream: 88.5% mycological cure in symptomatic women |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Open non-comparative study | J Int Med Res | 2% cream for Trichomonas or mixed vaginal infections (20 patients): 95% cured at first follow-up |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Open-label comparative trial | Gynakologische Rundschau | Tioconazole vs econazole, 3-day treatment of vaginal candidiasis |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Open-label comparative trial | Gynakologische Rundschau | Tioconazole cream vs econazole ovules, 3-day treatment |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | Future non-invasive azole options for vulvovaginal candidiasis |
| [30553009](https://pubmed.ncbi.nlm.nih.gov/30553009/) | 2019 | Formulation study (preclinical) | Int J Pharm | Chitosan-HPMC tioconazole films as an alternative vaginal dosage form |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075915 (cancelled) | Tioconazole (CVS Pharmacy) | Ointment | Not specified |

## Safety Considerations

- **Drug Interactions**: Two entries were found. Omeprazole (severity level unknown). CYP8B1, a human enzyme in bile acid synthesis that tioconazole inhibits; this is a pharmacological target interaction rather than a drug-drug interaction.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is almost entirely historical (1983–1988) clinical work on vaginal candidiasis, which is the original indication. The prediction is therefore not new repurposing evidence, and it does not extend to non-fungal vulvovaginitis.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Evidence that separates Candida-driven vulvovaginitis or vulvitis from candidiasis in general, with confirmed etiology
- Clarification of the current US commercial and regulatory status, given the cancelled license
- Dropping the postmenopausal atrophic vaginitis prediction unless a plausible mechanism emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


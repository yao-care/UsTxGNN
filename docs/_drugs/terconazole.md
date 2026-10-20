---
layout: default
title: Terconazole
parent: Model Prediction Only (L5)
nav_order: 1213
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Terconazole: predicted new indication Trichomonal vulvovaginitis (evidence level L5). Approved use: Vulvovaginal candidiasis"
monitor_inn: "TERCONAZOLE"
predicted_indications: ["trichomonal vulvovaginitis", "vulvitis", "vulvovaginitis", "postmenopausal atrophic vaginitis", "vaginitis (disease)", "herpetic vulvovaginitis", "ulceration of vulva", "vulvar neoplasm", "vaginal discharge", "bacterial vaginosis"]
---

# Terconazole
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

# Terconazole: From Vulvovaginal Candidiasis to Trichomonal Vulvovaginitis

## One-Sentence Summary

Terconazole is a topical triazole antifungal originally used to treat vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **trichomonal vulvovaginitis**, but **no clinical trials** and only **2 general review papers** support this direction, and neither reports trichomonas outcomes.
The top-ranked prediction therefore looks like a knowledge-graph artefact rather than a real repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vulvovaginal candidiasis |
| Predicted New Indication | Trichomonal vulvovaginitis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 6 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From general knowledge, terconazole is a triazole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis. This explains its efficacy in candidal vulvovaginitis.

*Trichomonas vaginalis* is a protozoan, not a fungus, and it does not rely on ergosterol-dependent membrane biology in the way fungi do. The antifungal mechanism therefore does not plausibly transfer. The high TxGNN score most likely reflects shared vaginitis-related neighbours in the knowledge graph rather than a true pharmacological link.

Other predictions in the list are mostly either the same as the approved indication (vulvitis, vulvovaginitis, vaginitis) or lack a mechanistic rationale (atrophic vaginitis, herpetic vulvovaginitis, vulvar ulceration, vulvar neoplasm, bacterial vaginosis).

## Clinical Trial Evidence

No clinical trials are registered for trichomonal vulvovaginitis. Currently no related clinical trials registered.

For context, the following completed trials test terconazole in vaginitis broadly (mainly the approved candidal indication), not in trichomoniasis:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00803738](https://clinicaltrials.gov/study/NCT00803738) | NA | Completed | 572 | Bioequivalence of two terconazole 80 mg suppositories in vulvovaginal candidiasis |
| [NCT02180100](https://clinicaltrials.gov/study/NCT02180100) | Phase 4 | Completed | 140 | Terconazole suppository vs fluconazole in severe vulvovaginal candidiasis |
| [NCT02308007](https://clinicaltrials.gov/study/NCT02308007) | Phase 3 | Completed | 475 | Intravaginal metronidazole and/or terconazole gels in vaginal infections (combination design) |
| [NCT02308046](https://clinicaltrials.gov/study/NCT02308046) | Phase 3 | Completed | 212 | Terconazole gel in vaginal infections (companion study) |
| [NCT03473418](https://clinicaltrials.gov/study/NCT03473418) | Phase 3 | Unknown | 69 | Ketoconazole in situ gel vs terconazole cream in vaginal candidiasis |
| [NCT04208555](https://clinicaltrials.gov/study/NCT04208555) | NA | Unknown | 76 | Boric acid vs terconazole in recurrent vulvovaginal candidiasis |

## Literature Evidence

Only two papers were linked to the predicted indication, and neither reports trichomonas outcomes.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10546257](https://pubmed.ncbi.nlm.nih.gov/10546257/) | 1999 | Review | The Nurse Practitioner | General review of bacterial, fungal and protozoal vaginitis, covering symptoms and management |
| [6617296](https://pubmed.ncbi.nlm.nih.gov/6617296/) | 1983 | Review | Chemotherapy | Terconazole is a triazole antifungal highly active in vitro against yeasts and filamentous fungi, and active in topical models of dermatophytosis and candidosis |

Strong supporting literature exists only for the approved candidal indication. Examples are randomized trials such as [25877666](https://pubmed.ncbi.nlm.nih.gov/25877666/) (2015, terconazole suppository vs oral fluconazole, n=140) and [2381618](https://pubmed.ncbi.nlm.nih.gov/2381618/) (1990, 0.8% vs 1.6% cream).

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075953 | Terconazole (A-S Medication Solutions) | Cream | Cancelled |
| ANDA077553 | Terconazole (Sun Pharmaceutical Industries) | Suppository | Cancelled |
| ANDA076043 | Terconazole (A-S Medication Solutions) | Cream | Cancelled |
| ANDA076712 | Terconazole (A-S Medication Solutions) | Cream | Cancelled |
| NDA021735 | Terconazole (A-S Medication Solutions) | Cream | Cancelled |

A sixth authorization (ANDA077149, Padagis Israel Pharmaceuticals, suppository) is also cancelled. None of the six has valid status.

## Cytotoxicity

Not applicable. Terconazole is an antifungal, not an antineoplastic drug.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug-interaction data were available in the data compiled for this report.

One literature item is worth noting: a case report ([33860751](https://pubmed.ncbi.nlm.nih.gov/33860751/), 2021) described chills, fatigue, chest distress and raised inflammatory markers after a single 80 mg vaginal suppository, which resolved after the residue was removed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no trials and no supporting literature, and the antifungal mechanism does not plausibly act on a protozoan. The score appears to come from graph proximity to vaginitis. Standard trichomoniasis treatment (nitroimidazoles) is already established.

**To proceed, the following is needed:**
- A new mechanistic hypothesis for activity against *Trichomonas vaginalis*, ideally with in vitro susceptibility data
- Retrieval of the FDA package insert warnings and contraindications (a blocking safety data gap)
- Confirmation of the mechanism-of-action data from DrugBank
- Clarification of why all US authorizations are cancelled, if commercial availability matters
- If a related direction is of interest, the better-supported options are within candidal disease (non-albicans Candida, recurrent vulvovaginal candidiasis), but these are extensions of the approved use rather than new indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


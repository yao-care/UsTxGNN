---
layout: default
title: Tioconazole
parent: 僅模型預測 (L5)
nav_order: 1230
evidence_level: L5
indication_count: 3
---

# Tioconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Tioconazole: From Vaginal Candidiasis to Vulvovaginitis

## One-Sentence Summary

> Tioconazole is a topical imidazole antifungal whose established clinical use, based on decades of published literature, is the treatment of vaginal (vulvovaginal) candidiasis and other superficial mycoses.
> The TxGNN model predicts it may also be effective for **Vulvovaginitis** (a broader diagnostic category encompassing candidal, trichomonal, and mixed vaginal infections),
> with **2 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in structured regulatory data (drug is not currently marketed in this jurisdiction); per literature, established use is topical treatment of vaginal candidiasis / superficial mycoses |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on the literature evidence provided, tioconazole is a substituted imidazole antifungal agent that inhibits fungal ergosterol biosynthesis, giving it broad-spectrum activity against dermatophytes, yeasts (notably *Candida albicans*), and even some trichomonads and Gram-positive bacteria.

Vulvovaginitis is a broad clinical diagnosis that frequently overlaps with vaginal candidiasis, trichomonal vaginitis, bacterial vaginosis, and mixed infections — the exact indications for which tioconazole already has decades of published clinical support. The TxGNN prediction is therefore less a discovery of a novel mechanism and more a confirmation that tioconazole's known antifungal/antimicrobial activity extends to the broader "vulvovaginitis" diagnostic umbrella, as demonstrated by multiple RCTs comparing tioconazole to placebo, econazole, clotrimazole, and oral ketoconazole across mixed vaginal infection populations.

Because the drug's core pharmacology (topical, local antifungal action with some antitrichomonal/antibacterial activity) is well matched to the polymicrobial nature of vulvovaginitis, the mechanistic plausibility is high even without formal MOA documentation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03839875](https://clinicaltrials.gov/study/NCT03839875) | Phase 4 | Completed | 116 | Open-label, single-arm study of Gynomax® XL Ovule (tioconazole-based) evaluating efficacy/safety in trichomonal vaginitis, bacterial vaginosis, candidal vulvovaginitis, and mixed vaginal infections |
| [NCT06056947](https://clinicaltrials.gov/study/NCT06056947) | Phase 3 | Completed | 577 | Randomized 3-arm study comparing new fenticonazole+tinidazole+lidocaine formulations against Gynomax® XL Ovule (tioconazole) across bacterial vaginosis, candidal vulvovaginitis, trichomonal vaginitis, and mixed infections |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | RCT | Gynäkologische Rundschau | Double-blind comparison of tioconazole vs placebo confirming efficacy, tolerance, and low systemic absorption in vaginal candidiasis |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | RCT | Gynäkologische Rundschau | 3-day tioconazole vs econazole showed comparable efficacy and tolerability in vaginal candidiasis |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | RCT | Gynäkologische Rundschau | 3-day tioconazole cream vs econazole ovules showed comparable efficacy and safety |
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | RCT | Antimicrob Agents Chemother | Single-dose 6.5% tioconazole ointment vs 3-day clotrimazole: 84% vs 85% asymptomatic at 4-week follow-up |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | RCT | J Int Med Res | Single-dose topical tioconazole 6% vs 5-day oral ketoconazole: comparable eradication rate, faster symptom relief with topical route |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | Broad review confirming antimicrobial spectrum and established efficacy/safety of tioconazole in vaginal candidiasis and superficial mycoses |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | Recent review of non-invasive azole treatment options for vulvovaginal candidiasis, situating tioconazole among current azole therapies |
| [10470518](https://pubmed.ncbi.nlm.nih.gov/10470518/) | 1999 | Review | Compr Ther | Review of epidemiology, diagnosis, and therapy of vulvovaginitis in otherwise healthy women |
| [4025721](https://pubmed.ncbi.nlm.nih.gov/4025721/) | 1985 | Cohort | Ala J Med Sci | Clinical and cytological assessment supporting efficacy of tioconazole in vulvovaginal candidiasis |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Cohort | Acta Obstet Gynecol Scand | Tioconazole 2% vaginal cream (3-day regimen) achieved an 88.5% mycological cure rate in symptomatic vaginal candidiasis |

---

## US Market Information

Tioconazole currently has no approved product licenses on record in this jurisdiction (`total_licenses = 0`), consistent with its "Not Marketed" status.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: label-derived warnings, contraindications, and drug-interaction data were not retrievable at this time — this is a blocking gap for formal safety assessment; see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for the vulvovaginitis indication is reasonably strong for a repurposing candidate (Evidence Level L2 — one completed Phase 3 RCT plus multiple supporting older RCTs and reviews), and the drug's known antifungal/antimicrobial activity is mechanistically well matched to this diagnostic category. However, a **blocking data gap** — absence of TFDA-equivalent label warnings and contraindications — prevents the candidate from entering the initial safety screening stage (S1), and the drug is currently not marketed in this jurisdiction (0 licenses).

**To proceed, the following is needed:**
- Official product label / warnings & contraindications (to unblock S1 safety screening)
- Confirmed mechanism of action from DrugBank (currently unavailable)
- Confirmation of available/required dosage forms and routes for the vulvovaginitis indication
- Drug-drug interaction data, if the product is intended for markets where it will be co-prescribed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


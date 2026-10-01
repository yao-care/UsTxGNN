---
layout: default
title: Tioconazole
parent: Model Prediction Only (L5)
nav_order: 1230
evidence_level: L5
indication_count: 3
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tioconazole: From Vaginal Candidiasis (Literature-Based) to Vulvovaginitis

## One-Sentence Summary

Tioconazole is an imidazole antifungal, marketed in the US as a topical ointment. The regulatory records provided do not state its approved indication, but the literature describes its use in vaginal candidiasis and superficial fungal infections.
The TxGNN model predicts it may be effective for **vulvovaginitis**, with **2 registered clinical trials** (both of other azole products) and **20 publications** in the evidence pack.
Because most of the evidence is for candidal vulvovaginitis, this prediction is probably close to existing on-label use rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records; the literature describes vaginal candidiasis and superficial mycoses |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L2 (rests on older tioconazole-specific studies; the two registered trials involve other drugs) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 17 licenses (the five listed below are all under ANDA075915) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this record. Tioconazole is a substituted imidazole antifungal, and azoles as a class inhibit fungal lanosterol 14-alpha-demethylase (CYP51). This blocks ergosterol synthesis and disrupts the fungal cell membrane. That is a direct fit for candidal vulvovaginitis, the most common infectious cause of the condition.

The 1986 *Drugs* review reports broad in-vitro activity against dermatophytes and yeasts, and some activity against trichomonads, chlamydia and Gram-positive bacteria. It also reports that open and controlled trials showed efficacy and safety of topical tioconazole in skin yeast infections and vaginal candidiasis. The high TxGNN score is therefore consistent with the biology.

The prediction applies only to the **candidal** part of vulvovaginitis. Bacterial vaginosis, trichomoniasis, and atrophic or irritant causes are not expected to respond to an antifungal alone. Whether vaginal candidiasis is already an on-label use of the US products should be checked against the label.

Two other predicted indications were also reviewed:
- **Vulvitis** (score 99.20%, evidence L3): it is anatomically contiguous with vulvovaginal candidiasis, but no study was designed for isolated vulvitis. The antifungal link holds only for candidal vulvitis. Status: research question.
- **Postmenopausal atrophic vaginitis** (score 99.19%, evidence L5): this condition is driven by estrogen deficiency, not infection, so tioconazole's mechanism does not address it. The score likely reflects graph proximity to other vaginitis terms. Status: Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03839875](https://clinicaltrials.gov/study/NCT03839875) | Phase 4 | Completed | 116 | Single-arm, open-label study of Gynomax® XL ovule in trichomonal vaginitis, bacterial vaginosis, candidal vulvovaginitis and mixed infections. Tioconazole is not confirmed as the tested product, and there is no comparator. |
| [NCT06056947](https://clinicaltrials.gov/study/NCT06056947) | Phase 3 | Completed | 577 | Randomized three-arm study of two fenticonazole + tinidazole + lidocaine formulations against Gynomax® XL ovule in the same vaginal infections. It is a different azole, so it gives class-level support only. |

Neither registered trial tests tioconazole directly.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | RCT (double-blind) | Gynakol Rundsch | Tioconazole vs placebo in vaginal candidiasis, including assessment of systemic absorption. |
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | Randomized comparative trial | Antimicrob Agents Chemother | 80 patients: single-dose 6.5% tioconazole ointment vs 3-day clotrimazole. 84% vs 85% remained asymptomatic at 4 weeks. |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Randomized open-label | J Int Med Res | 40 patients: topical 6% tioconazole (single dose) vs 5 days of oral ketoconazole. Both eradicated disease; topical symptom relief was faster. |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | Broad antimicrobial activity. Trials show efficacy and safety of topical tioconazole in skin yeast infections and vaginal candidiasis. |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | Non-invasive azole options for vulvovaginal candidiasis, including complicated and recurrent disease. |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Open-label comparative | Gynakol Rundsch | Tioconazole cream vs econazole ovules, 3-day treatment of vaginal candidiasis. |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Open-label comparative | Gynakol Rundsch | Tioconazole vs econazole, 3-day treatment of vaginal candidiasis. |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Clinical study | Acta Obstet Gynecol Scand | 2% vaginal cream for 3 days in 29 symptomatic women: 88.5% mycological cure. |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Open, non-comparative | J Int Med Res | 2% cream for 3 days in 20 patients with *T. vaginalis* or mixed infections: 95% cured at first follow-up. |
| [10990271](https://pubmed.ncbi.nlm.nih.gov/10990271/) | 2000 | Laboratory study | Microb Drug Resist | Cross-resistance of *Candida albicans* and *C. glabrata* isolates to over-the-counter azoles used for vaginitis. |

Most of these studies are from the 1980s and evaluate vaginal candidiasis, not vulvovaginitis of all causes.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075915 | tioconazole 1 (CVS Pharmacy) | Ointment | Not listed in the records |
| ANDA075915 | good sense tioconazole 1 (L. Perrigo) | Ointment | Not listed in the records |
| ANDA075915 | MONISTAT TIOCONAZOLE 1 (Insight Pharmaceuticals) | Ointment | Not listed in the records |
| ANDA075915 | Topcare Tioconazole 1 (Topco Associates) | Ointment | Not listed in the records |
| ANDA075915 | signature care tioconazole 1 (Safeway) | Ointment | Not listed in the records |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tioconazole-specific randomized and comparative studies support efficacy in vaginal candidiasis, and the azole mechanism fits candidal vulvovaginitis. The registered trials involve other azole products, and the evidence does not extend to non-candidal vulvovaginitis, vulvitis or atrophic vaginitis. The recommendation therefore applies only to the candidal subset.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block the safety screening
- The approved indication text from the US label, to confirm whether vaginal candidiasis is already on-label
- Mechanism of action data from DrugBank
- Confirmation of whether the products in NCT03839875 contain tioconazole
- Diagnostic confirmation of candidal infection before use, and exclusion of bacterial, trichomonal and atrophic causes
- Review of azole cross-resistance in *Candida* (PMID 10990271)

*These results are for research reference only, are not medical advice, and require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


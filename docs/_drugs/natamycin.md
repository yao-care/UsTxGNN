---
layout: default
title: Natamycin
parent: Model Prediction Only (L5)
nav_order: 957
evidence_level: L5
indication_count: 10
---

# Natamycin
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

# Natamycin: From Fungal Eye Infections to Vulvovaginal Candidiasis

## One-Sentence Summary

Natamycin is a polyene antifungal. Its US product, NATACYN, is an ophthalmic suspension, and the license record does not list an approved indication. TxGNN predicts it may be effective for **vulvovaginal candidiasis**. Support comes from **1 completed Phase 3 trial (a natamycin + lactulose combination)** and about **20 publications**, most of them old uncontrolled reports. Natamycin vaginal products are already used outside the US, so this is closer to an established topical use than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license record (NATACYN is an ophthalmic drop; fungal eye infection is inferred from the dosage form and literature) |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license entries (both NDA050514, held by two manufacturers) |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note: the Evidence Pack labels this L1. Under the L1–L5 rules, L1 needs at least 2 completed Phase 3 RCTs, and only one is found here. It also tested a combination product, so L2 is the more defensible grade.*

## Why is This Prediction Reasonable?

Natamycin is a polyene macrolide. It binds ergosterol in the fungal cell membrane and disrupts membrane function. Candida species are ergosterol-containing fungi, so the mechanism fits vulvovaginal candidiasis directly. The mechanism-of-action field in DrugBank was empty, so this explanation comes from the Evidence Pack's mechanistic rationale.

The original ophthalmic use (fungal infection at a mucosal or surface site) and the predicted use are both topical fungal infections. Natamycin is poorly absorbed, which suits local treatment. Vaginal natamycin (Pimafucin) has been studied since the 1960s. The Phase 3 trial tested a natamycin + lactulose suppository against Pimafucin and lactulose alone.

**Guardrails:**
- The US-marketed NATACYN is an eye drop, not a vaginal product.
- The Phase 3 evidence is for a combination, so the effect cannot be attributed to natamycin alone.
- Support is limited to candidal (topical or vaginal) disease. It does not extend to bacterial, trichomonal or atrophic vaginitis, or to systemic candidiasis.

## Clinical Trial Evidence

Currently no clinical trials are linked to this indication in the Evidence Pack. However, the Phase 3 trial behind PMID 39979898 is registered and appears under the parent term "candidiasis":

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06411314](https://clinicaltrials.gov/study/NCT06411314) | Phase 3 | Completed | 218 | Natamycin 100 mg + lactulose 300 mg vaginal suppositories vs Pimafucin (natamycin 100 mg) or lactulose 300 mg alone in non-pregnant adult women with vulvovaginal candidiasis. Superiority design; results are not included in the pack. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [39979898](https://pubmed.ncbi.nlm.nih.gov/39979898/) | 2025 | RCT (Phase 3 publication) | BMC Women's Health | Efficacy and safety of natamycin + lactulose vaginal suppositories in vulvovaginal candidiasis. Design details were not verified. |
| [4561566](https://pubmed.ncbi.nlm.nih.gov/4561566/) | 1972 | Comparative trial | Med J Aust | Amphotericin B pessaries vs natamycin (Pimafucin) pessaries in vaginal candidiasis. |
| [6760652](https://pubmed.ncbi.nlm.nih.gov/6760652/) | 1982 | Clinical study | Acta Obstet Gynecol Scand | 33 women given 10-day vaginal natamycin. Cure rate was 94% with partner treatment vs 88% with placebo cream, not significantly different. |
| [159686](https://pubmed.ncbi.nlm.nih.gov/159686/) | 1979 | Controlled clinical trial | Aust N Z J Obstet Gynaecol | 120 patients with monilial vulvovaginitis. Adding the enzyme Elase to natamycin improved symptom relief and organism eradication. |
| [6966774](https://pubmed.ncbi.nlm.nih.gov/6966774/) | 1980 | Clinical study | N Z Med J | 50 women on a 10-day vaginal natamycin course. 76% cure at 2 weeks, maintained at 4 weeks. |
| [5296471](https://pubmed.ncbi.nlm.nih.gov/5296471/) | 1966 | Clinical study | Can Med Assoc J | 91 pregnant women with vaginal moniliasis. 63% cured by culture; 94.3% benefited. |
| [1082689](https://pubmed.ncbi.nlm.nih.gov/1082689/) | 1975 | Clinical study | Zentralbl Gynakol | Oral metronidazole + vaginal natamycin. Candida cured clinically in 89% after the first course. |
| [11048415](https://pubmed.ncbi.nlm.nih.gov/11048415/) | 1999 | Review | Ceska Gynekol | Diagnosis of chronic vaginal candidiasis; natamycin compared with clotrimazole. |
| [41412769](https://pubmed.ncbi.nlm.nih.gov/41412769/) | 2025 | Survey | Ceska Slov Farm | 408 women in Lviv, Ukraine. Lifetime prevalence of vulvovaginal candidiasis was 72.6%. Describes management practice, not natamycin efficacy. |
| [18288724](https://pubmed.ncbi.nlm.nih.gov/18288724/) | 2008 | In vitro / formulation | J Pharm Sci | Natamycin–γ-cyclodextrin vaginal mucoadhesive tablets. MIC90 was below 0.0313 µg/mL. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050514 | NATACYN (Eyevance Pharmaceuticals, LLC) | Suspension/Drops | Not stated in the record |
| NDA050514 | NATACYN (Harrow Eye, LLC) | Suspension/Drops | Not stated in the record |

## Safety Considerations

- **Drug Interactions**: No interaction records were found for this drug.
- **Pregnancy**: A population-based case-control teratology study of vaginal natamycin in pregnancy exists ([PMID 12849848](https://pubmed.ncbi.nlm.nih.gov/12849848/), 2003). Its results are not included in the pack.
- **Systemic use**: Natamycin is poorly absorbed, so systemic or invasive candidiasis is not supported.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism fits, and one completed Phase 3 trial plus decades of clinical reports support natamycin in candidal vulvovaginitis. But the Phase 3 tested a combination product, and the US-approved product is an eye drop. Claims should be limited to topical or vaginal candidiasis. The related predictions "candidiasis", "vaginitis" and "vulvovaginitis" rest on the same evidence and only apply to the candidal form. Predictions for trichomonal vulvovaginitis, atrophic vaginitis, vulvar ulceration, vulvar neoplasm and tinea nigra have weak or no support and should be held.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking safety gap)
- Published results of NCT06411314, especially the natamycin-alone (Pimafucin) arm
- Comparison of natamycin against standard azole therapy for vulvovaginal candidiasis
- A regulatory pathway for a vaginal formulation, since the US product is ophthalmic
- Review of the pregnancy teratology data (PMID 12849848) for use in pregnant women
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


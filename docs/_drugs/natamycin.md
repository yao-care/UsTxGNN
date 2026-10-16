---
layout: default
title: Natamycin
parent: Model Prediction Only (L5)
nav_order: 957
evidence_level: L5
indication_count: 10
monitor_inn: "NATAMYCIN"
predicted_indications: ["vulvovaginal candidiasis", "candidiasis", "vulvitis", "vulvovaginitis", "trichomonal vulvovaginitis", "postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "vaginitis (disease)", "tinea nigra"]
last_modified_at: 2026-10-14
description: "Natamycin: predicted new indication Vulvovaginal candidiasis (evidence level L5). Approved use: Mycotic corneal ulcer"
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

# Natamycin: From Mycotic Corneal Ulcer to Vulvovaginal Candidiasis

## One-Sentence Summary

Natamycin is a polyene antifungal originally used to treat mycotic (fungal) corneal ulcer.
The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis**,
with **1 completed Phase 3 clinical trial** and **14 publications** currently supporting this direction.
Note that the Phase 3 trial tested a natamycin plus lactulose combination, so natamycin's own contribution is not isolated.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mycotic corneal ulcer |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 (as assigned in the compiled data; see the note in the Clinical Trial Evidence section) |
| US Market Status | Cancelled only (no active US authorization) |
| Number of NDAs | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, natamycin is a polyene antifungal that binds ergosterol in fungal cell membranes and impairs membrane integrity.

Its established use is in fungal infection of the eye (mycotic corneal ulcer). *Candida* species also contain ergosterol and are susceptible to polyenes, so activity against vulvovaginal candidiasis is mechanistically consistent. Natamycin vaginal products (e.g., Pimafucin) have a long history of use in vaginal yeast infections, supported by historical comparative studies, including one against amphotericin B pessaries.

Other predicted indications appear less well supported. Broader candidiasis, vulvitis, vulvovaginitis and general vaginitis are partly covered by the same vulvovaginal candidiasis evidence. Trichomonal vulvovaginitis, postmenopausal atrophic vaginitis, vulvar ulceration and vulvar neoplasm lack a plausible antifungal mechanism or any direct evidence and should be held. Tinea nigra is mechanistically plausible but has no supporting studies.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06411314](https://clinicaltrials.gov/study/NCT06411314) | Phase 3 | Completed | 218 | Randomized, controlled superiority trial of natamycin 100 mg + lactulose 300 mg vaginal suppositories vs. Pimafucin (natamycin 100 mg) or lactulose 300 mg alone in non-pregnant adult women with vulvovaginal candidiasis (2022–2023). Efficacy and safety were assessed. |

**Caveat:** This is the only registered trial. Because it tests a fixed combination, it does not isolate natamycin's own effect. By the strict definition (two or more completed Phase 3 RCTs), the evidence would be closer to L2. The L1 label comes from the compiled data.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39979898](https://pubmed.ncbi.nlm.nih.gov/39979898/) | 2025 | RCT | BMC Women's Health | Publication of the Phase 3 trial of natamycin + lactulose vaginal suppositories in vulvovaginal candidiasis |
| [4561566](https://pubmed.ncbi.nlm.nih.gov/4561566/) | 1972 | RCT | Med J Aust | Comparative trial of amphotericin B (Fungilin) vs. natamycin (Pimafucin) pessaries in vaginal candidiasis |
| [12849848](https://pubmed.ncbi.nlm.nih.gov/12849848/) | 2003 | Case-control | Reprod Toxicol | Teratology study of vaginal natamycin during pregnancy, providing supportive safety information |
| [6760652](https://pubmed.ncbi.nlm.nih.gov/6760652/) | 1982 | Clinical study | Acta Obstet Gynecol Scand | 33 women with vaginal candidosis treated with natamycin tablets; cure rate 94% with partner treatment vs. 88% with placebo cream, not significantly different |
| [6966774](https://pubmed.ncbi.nlm.nih.gov/6966774/) | 1980 | Clinical study | N Z Med J | 50 women given Pimafucin vaginal tablets for 10 days; 76% cure rate at 2 weeks, maintained at 4 weeks |
| [159686](https://pubmed.ncbi.nlm.nih.gov/159686/) | 1979 | Controlled clinical trial | Aust N Z J Obstet Gynaecol | 120 patients with monilial vulvovaginitis; adding Elase to natamycin improved symptom relief and organism eradication |
| [4584444](https://pubmed.ncbi.nlm.nih.gov/4584444/) | 1973 | Cohort | Practitioner | Natamycin for vaginal candidiasis in pregnancy |
| [11048415](https://pubmed.ncbi.nlm.nih.gov/11048415/) | 1999 | Review | Ceska Gynekol | Diagnosis and treatment of chronic vaginal candidiasis, comparing natamycin with clotrimazole |
| [1082689](https://pubmed.ncbi.nlm.nih.gov/1082689/) | 1975 | Clinical study | Zentralbl Gynakol | Oral metronidazole plus vaginal natamycin; Candida infections cured clinically in 89% after the first course |
| [18288724](https://pubmed.ncbi.nlm.nih.gov/18288724/) | 2008 | Formulation/preclinical | J Pharm Sci | Natamycin–γ-cyclodextrin vaginal mucoadhesive tablets; MIC90 below 0.0313 µg/mL |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050514 (cancelled) | NATACYN (Eyevance Pharmaceuticals, LLC) | Ophthalmic suspension/drops | Not listed in the compiled data |

No active US authorization exists for natamycin in the data compiled for this report. The only license is cancelled, and it covers an ophthalmic product, not a vaginal one.

## Safety Considerations

Please refer to the package insert for safety information.

Supportive information: a case-control teratology study of vaginal natamycin in pregnancy (PMID 12849848) provides some reassurance for use in pregnancy, though the formal label data are unavailable. No drug interaction records were found, and no disease-level contraindications were identified in the knowledge graph.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (n=218) and decades of historical clinical use support natamycin in vulvovaginal candidiasis, and the mechanism is consistent with its antifungal action. However, the Phase 3 trial used a combination product, and there is currently no active US authorization for a vaginal formulation. The recommendation should be limited to the vulvovaginal candidal site. Candidal vulvitis, vulvovaginitis and general vaginitis fall under it only where a fungal cause is confirmed.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Evidence isolating natamycin's own effect, such as a trial of natamycin monotherapy vs. an established azole
- Results data from NCT06411314 and a review of the full publication
- Route and formulation planning, since the US-listed product is ophthalmic and the supporting evidence is for vaginal use
- Hold the non-fungal predictions (trichomonal vulvovaginitis, atrophic vaginitis, vulvar ulceration, vulvar neoplasm). Tinea nigra is a research question only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


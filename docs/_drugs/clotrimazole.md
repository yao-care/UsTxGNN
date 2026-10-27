---
layout: default
title: Clotrimazole
parent: Model Prediction Only (L5)
nav_order: 543
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Clotrimazole: predicted new indication Acne (evidence level L5). Approved use: Fungal skin and mucosal infections (e.g., tinea pedis, tinea corporis…"
monitor_inn: "CLOTRIMAZOLE"
predicted_indications: ["acne (disease)", "vulvovaginitis", "postmenopausal atrophic vaginitis"]
---

# Clotrimazole
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

## Clotrimazole: From Fungal Skin and Mucosal Infections to Acne
{: .text-alpha }

## One-Sentence Summary

Clotrimazole is an azole antifungal, originally used for fungal and yeast infections such as tinea pedis, cutaneous candidiasis and vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **acne**, but the support is weak: **1 clinical trial** (suspended, testing a triple-combination product) and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal skin and mucosal infections (e.g., tinea pedis, tinea corporis, cutaneous candidiasis, vulvovaginal candidiasis) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 (weak; no clotrimazole-specific efficacy data) |
| US Market Status | Cancelled only (all 4 listed authorizations are cancelled) |
| Number of NDAs | 4 (generic applications and related authorizations, all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Clotrimazole is a synthetic azole antifungal. The published literature describes it as inhibiting ergosterol biosynthesis, which slows fungal growth. Its efficacy in superficial fungal infections is well established, and it has also attracted interest for activities beyond its antifungal effect.

The link to acne is indirect. Some *Malassezia*/*Candida* colonization has been proposed as a contributor to acne-like folliculitis, so an antifungal could plausibly help in a subset of cases. Acne itself, however, is mainly driven by sebum production, follicular blockage, *Cutibacterium acnes* and inflammation, and clotrimazole has no established role in these processes. The very high TxGNN score looks like a knowledge-graph proximity effect rather than a mechanistic or clinical signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Compared a fixed-dose combination cream (beclomethasone 0.025% + gentamicin 0.1% + clotrimazole 1%) in contaminated dermatosis with bilateral symmetrical lesions. No results are available, and the effect of clotrimazole alone cannot be isolated. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| ANDA072641 | Clotrimazole | Cream | Sun Pharmaceutical Industries, Inc. | Cancelled |
| M005 | Clotrimazole | Cream | Proficient Rx LP | Cancelled |
| ANDA072640 | Clotrimazole | Cream | Sun Pharmaceutical Industries, Inc. | Cancelled |
| ANDA078338 | Clotrimazole | Cream | E. Fougera & Co. (Fougera Pharmaceuticals Inc.) | Cancelled |

Other dosage forms are also recorded for clotrimazole, including ointment, soap and solution.

---

## Safety Considerations

- **Contraindication-related conditions (from the TxGNN knowledge graph, not label text):** adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia, peripheral vascular disease, intermittent vascular claudication, peripheral arterial disease. These associations likely come from the corticosteroid component of combination products and should be verified against current labelling.
- **Drug Interactions:** The interaction screen recorded 100 interacting drugs (the first 20 were reviewed).
  - **Major:** fentanyl, alfentanil, hydrocodone, amiodarone.
  - **Moderate:** abemaciclib, paclitaxel, acalabrutinib, nifedipine, amlodipine, levonorgestrel, norethisterone, estradiol, alprazolam, apixaban, aprepitant, alfuzosin, aliskiren.
  - **Minor:** dolutegravir, amphotericin B (including the lipid complex).
  - These mainly reflect CYP3A4-related interactions. They matter most for systemic exposure and are likely less relevant to topical use on intact skin.

Package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial is a suspended study of a three-drug combination, with no results, so no clotrimazole-specific benefit in acne can be shown. There is no supporting literature, and the mechanistic link is speculative. The high TxGNN score is not backed by clinical evidence, and all US authorizations are currently cancelled.

**To proceed, the following is needed:**
- Mechanism-of-action data, and preclinical evidence on antifungal or anti-inflammatory effects relevant to acne
- A controlled trial of clotrimazole monotherapy in acne, ideally in *Malassezia*-associated or folliculitis-type disease
- FDA package insert warnings and contraindications
- Confirmation of current product availability

**Note on the other predicted indications in the same evidence set:**
- **Vulvovaginitis (TxGNN 99.59%):** This has far stronger support, with Level L1 evidence, multiple completed Phase 3 trials and RCTs, and a suggested decision of Proceed with Guardrails. It is essentially an existing indication (vulvovaginal candidiasis) rather than true repurposing. Guardrails: confirm Candida as the cause, and take care in pregnancy, where safety data are mixed.
- **Postmenopausal atrophic vaginitis (TxGNN 99.46%):** There is no clinical or literature evidence (L5), and no clear mechanistic rationale, since the condition is driven by estrogen deficiency. The recommendation is Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


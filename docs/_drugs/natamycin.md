---
layout: default
title: Natamycin
parent: 僅模型預測 (L5)
nav_order: 957
evidence_level: L5
indication_count: 10
---

# Natamycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Natamycin: From Antifungal Use (No Taiwan License on File) to Vulvovaginal Candidiasis

## One-Sentence Summary

Natamycin (DrugBank DB00826) is a polyene macrolide antifungal with **no current market authorization in Taiwan** (0 licenses) and no structured mechanism-of-action record on file. The TxGNN model predicts efficacy for **Vulvovaginal Candidiasis** with a **99.97% score**, and this is not a speculative new use — the evidence pack's own literature (spanning 1959–2025) and **1 completed Phase 3 RCT** show this is natamycin's long-established, historically proven antifungal indication (marketed elsewhere as *Pimafucin*) that Taiwan simply has not registered.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — Natamycin has zero approved licenses in Taiwan; internationally it is a classic topical/vaginal antifungal (brand *Pimafucin*) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, no structured mechanism-of-action (DrugBank MOA field) data is available for Natamycin. Based on the pharmacological annotation attached to this candidate's evidence pack, Natamycin is a **polyene macrolide antifungal** that binds ergosterol in the fungal cell membrane, disrupting membrane integrity and ion permeability — a well-established, decades-old mechanism against *Candida* spp., not a novel mechanistic inference.

Because Taiwan has no approved license for Natamycin, there is no local "original indication" to compare against. What the evidence pack actually shows is that vulvovaginal candidiasis **is** natamycin's classic clinical use worldwide — the literature contains reports of vaginal natamycin/pimaricin tablets treating candidiasis as far back as 1965, continuing through a 2025 international Phase 3 RCT. In this sense, the TxGNN prediction is best read as **confirming and re-surfacing an already-proven indication that Taiwan's regulatory record simply lacks**, rather than identifying genuinely new pharmacology. This lowers scientific risk but does not remove the regulatory and safety-documentation gap described below.

## Clinical Trial Evidence

No trial is indexed directly under the "vulvovaginal candidiasis" entry in the evidence pack (`predicted_indications[0].evidence.clinical_trials` is empty).

Currently no related clinical trials registered under this specific ranked entry.

*Note: A directly relevant completed Phase 3 RCT — [NCT06411314](https://clinicaltrials.gov/study/NCT06411314) (n=218, Natamycin + Lactulose vs. Pimafucin vs. Lactulose vaginal suppositories for vulvovaginal candidiasis) — is indexed in the evidence pack under the closely related "candidiasis" and "vulvovaginitis" entries rather than this exact term, and should be treated as directly supporting evidence.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39979898](https://pubmed.ncbi.nlm.nih.gov/39979898/) | 2025 | RCT | BMC Women's Health | International RCT of Natamycin 100mg + Lactulose 300mg vaginal suppositories vs. Pimafucin vs. Lactulose alone in adult women with vulvovaginal candidiasis; assessed superiority efficacy and safety |
| [4561566](https://pubmed.ncbi.nlm.nih.gov/4561566/) | 1972 | RCT (comparative) | The Medical Journal of Australia | Comparative trial of amphotericin B vs. natamycin (Pimafucin) pessaries for vaginal candidiasis (abstract unavailable; title indicates head-to-head design) |
| [6760652](https://pubmed.ncbi.nlm.nih.gov/6760652/) | 1982 | Cohort | Acta Obstetricia et Gynecologica Scandinavica | 33 patients treated with natamycin vaginal tablets (10 days); partner cream vs. placebo cream compared — 94% vs. 88% cure rate, not significantly different |
| [41412769](https://pubmed.ncbi.nlm.nih.gov/41412769/) | 2025 | Survey | Ceska a Slovenska farmacie | Survey of 408 women in Lviv, Ukraine; lifetime VVC prevalence 72.6%, most common symptoms were vaginal itching (89.7%) and discharge (71.7%) |
| [18288724](https://pubmed.ncbi.nlm.nih.gov/18288724/) | 2008 | Not yet classified | Journal of Pharmaceutical Sciences | Natamycin–γ-cyclodextrin inclusion complex for vaginal mucoadhesive tablets; improved solubility/stability, MIC₉₀ <0.0313 µg/mL against Candida |
| [11048415](https://pubmed.ncbi.nlm.nih.gov/11048415/) | 1999 | Not yet classified | Ceska Gynekologie | Compared diagnosis/treatment outcomes of chronic vaginal candidiasis: natamycin vs. clotrimazole |
| [6966774](https://pubmed.ncbi.nlm.nih.gov/6966774/) | 1980 | Not yet classified | The New Zealand Medical Journal | 50 women given Pimafucin vaginal tablets for 10 days; 76% cure rate at 2 weeks, maintained at 4 weeks |
| [1082689](https://pubmed.ncbi.nlm.nih.gov/1082689/) | 1975 | Not yet classified | Zentralblatt fur Gynakologie | Oral metronidazole + vaginal natamycin combination for mixed urogenital infections; 96.1% cure for trichomoniasis, 89% for candida |
| [5296471](https://pubmed.ncbi.nlm.nih.gov/5296471/) | 1966 | Not yet classified | Canadian Medical Association Journal | 91 pregnant women with vaginal moniliasis treated with pimaricin; 63% culture-negative cure, 94.3% overall symptomatic benefit |
| [159686](https://pubmed.ncbi.nlm.nih.gov/159686/) | 1979 | Not yet classified | Aust & NZ J Obstet Gynaecol | Controlled trial (n=120): adding a lytic enzyme (Elase) to natamycin increased effectiveness vs. natamycin alone for monilial vulvovaginitis |

## US Market Information

Natamycin currently has **no approved license or authorization on file in Taiwan** (`taiwan_regulatory.total_licenses = 0`, `licenses = []`). There is no registered product, dosage form, or approved indication text available for local review.

## Safety Considerations

Please refer to the package insert for safety information.

*No structured key warnings, contraindications, or drug interaction data are available in this evidence pack (DDI query returned `not_found`). Since Natamycin is not currently marketed in Taiwan, no local package insert exists — international manufacturer labeling (e.g., Pimafucin SmPC) should be consulted before any clinical use.*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is supported by a 2025 international completed Phase 3 RCT plus decades of consistent historical clinical literature on natamycin's antifungal efficacy in vulvovaginal candidiasis, giving reasonable scientific confidence (L2). However, TFDA-equivalent safety labeling is a **Blocking** data gap (DG001) and Natamycin has zero existing Taiwan market authorization, so it cannot yet clear a formal safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA package insert / warnings & contraindications (DG001, Blocking — required before any S1 safety pre-screen)
- Structured mechanism-of-action data via DrugBank API (DG002)
- Formal drug-drug interaction screening (current query: not found)
- Confirmation of regulatory pathway for Taiwan registration, given the drug has no existing local license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


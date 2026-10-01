---
layout: default
title: Nystatin
parent: Moderate Evidence (L3-L4)
nav_order: 978
evidence_level: L3
indication_count: 10
---

# Nystatin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Nystatin: From Topical Antifungal Therapy to Vulvovaginitis

## One-Sentence Summary

Nystatin is a polyene antifungal that is marketed in the US in several forms (suspension, ointment, powder, tablet, cream). The TxGNN model predicts it may be effective for **vulvovaginitis**, with a very high score of 99.92%. No clinical trials are registered for this indication, but **20 publications** support it, mostly reviews and small clinical or in vitro studies on vulvovaginal candidiasis. This looks more like an established use than true repurposing, and the missing original-indication data probably reflects a DrugBank gap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied US label data (nystatin is a polyene antifungal) |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nystatin binds ergosterol in the Candida cell membrane and forms pores, which kills the fungal cell. Detailed mechanism-of-action data is not available in the supplied record, so this description is based on the known pharmacology of the polyene class.

*Candida albicans* causes 85–90% of vulvovaginal candidiasis, the main infectious cause of vulvovaginitis. The mechanism therefore fits the predicted indication directly. The literature also says nystatin was introduced in the 1950s for vulvovaginal candidiasis. Later it was surpassed by imidazoles and triazoles as first-line treatment.

The prediction should be read with these limits:
- Nystatin is not expected to help non-fungal vaginitis, such as bacterial vaginosis, trichomoniasis or atrophic vaginitis.
- The study designs behind the literature cannot be confirmed from titles alone, so the evidence is not graded L1 or L2.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Management of fluconazole-resistant vulvovaginal candidiasis. Alternatives include boric acid, nystatin, oteseconazole and ibrexafungerp. |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clin Evid | Vulvovaginal candidiasis is the second most common cause of vaginitis. *C. albicans* accounts for 85–90% of cases. |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Womens Health | Boric acid for recurrent vulvovaginal candidiasis. Non-albicans species are more resistant to azoles. |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Review | BMJ Clin Evid | Evidence review on vulvovaginal candidiasis (earlier edition). |
| [19454049](https://pubmed.ncbi.nlm.nih.gov/19454049/) | 2007 | Review | BMJ Clin Evid | Evidence review on vulvovaginal candidiasis (earlier edition). |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Review | Obstet Gynecol Clin North Am | Nystatin was introduced in the 1950s for vulvovaginal candidiasis. Imidazoles and triazoles have since become first choice. |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Clinical/in vitro study | Mycoses | 287 Candida isolates from 283 patients with complicated vulvovaginal candidiasis. Fluconazole and nystatin susceptibility was correlated with clinical outcome. |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Animal study | BMC Microbiol | In a rat vulvovaginal candidiasis model, nystatin enhanced the immune response against *C. albicans* and protected vaginal epithelial ultrastructure. |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | In vitro study | Infect Drug Resist | ZnO nanoparticles and nystatin against fluconazole-resistant *C. albicans*. SAP1-3 gene expression was downregulated. |
| [37023426](https://pubmed.ncbi.nlm.nih.gov/37023426/) | 2023 | In vitro study | J Infect Dev Ctries | Tea tree oil 5% and 10% were compared with nystatin by inhibition zone against vaginal Candida isolates in pregnancy. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA203621 | Nystatin | Suspension | Atlantic Biologicals Corp. |
| ANDA214346 | Nystatin | Suspension | NuCare Pharmaceuticals, Inc. |
| ANDA207767 | Nystatin | Ointment | Bryant Ranch Prepack (two identical entries) |
| ANDA208581 | Nystatin | Powder | Zydus Pharmaceuticals USA Inc. |

The record lists 20 authorizations in total, and the table shows the first five entries. Other forms on record include film-coated oral tablets and topical cream. Approved-indication text is not included in the supplied data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nystatin has a direct antifungal mechanism against vulvovaginal candidiasis, and the literature supports its use, so the prediction is credible. However, the evidence consists of reviews and small clinical or in vitro studies. There are no registered trials, and safety and label data are missing.

**To proceed, the following is needed:**
- Download and review the current US package insert, including warnings, contraindications and approved indications. This is a blocking gap for safety screening.
- Confirm whether vulvovaginitis is already a labeled use, in which case this is not repurposing.
- Check current treatment guidelines and the fluconazole-resistant and non-albicans Candida literature.
- Confirm the study design of the key publications, since the evidence level is L3 and not L1 or L2.
- Retrieve detailed mechanism-of-action data from DrugBank.
- Limit any use to candidal vulvovaginitis, because non-fungal causes are not expected to respond.

**Other predictions:**
- Vulvitis has indirect evidence extrapolated from vulvovaginal candidiasis and is a research question only.
- The remaining predictions, including postmenopausal atrophic vaginitis and disease of orbital region, have no plausible mechanistic link and should be held.

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


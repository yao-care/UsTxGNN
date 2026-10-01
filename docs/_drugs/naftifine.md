---
layout: default
title: Naftifine
parent: Moderate Evidence (L3-L4)
nav_order: 952
evidence_level: L3
indication_count: 8
---

# Naftifine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **8** 
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

# Naftifine: From Superficial Fungal Skin Infections (Dermatophytosis) to Cutaneous Candidiasis

## One-Sentence Summary

Naftifine is a topical allylamine antifungal, used mainly for dermatophyte skin infections such as tinea pedis, cruris and corporis. The TxGNN model predicts it may be effective for **cutaneous candidiasis**. No clinical trials are registered for this indication, but **2 randomized or controlled clinical studies (1984, 1988)** and several reviews in the literature support it.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Cutaneous candidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 licenses (1 NDA + 3 ANDAs) |
| Recommended Decision | Proceed with Guardrails |

The license records contain no approved-indication text. The original indication above is taken from the literature, not from the label.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the drug record. The literature describes naftifine as an allylamine that inhibits squalene epoxidase. This depletes ergosterol, an essential fungal membrane component, and causes toxic squalene to build up. Naftifine is fungicidal against dermatophytes and is also reported to have anti-inflammatory and some antibacterial activity.

Cutaneous candidiasis is a superficial skin infection caused by yeast rather than dermatophytes. Both organisms depend on ergosterol synthesis, so a topical drug that works on dermatophyte skin infections may also act on Candida. There is a caveat: allylamines are generally less potent against Candida than against dermatophytes, and terbinafine, a related allylamine, is described as fungistatic against *Candida albicans*. The prediction is therefore plausible but less certain than for dermatophytosis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3048914](https://pubmed.ncbi.nlm.nih.gov/3048914/) | 1988 | RCT | Cutis | Double-blind, parallel-group trial of 60 patients with cutaneous candidiasis. Naftifine 1% cream vs vehicle, twice daily for 3 weeks. 77% of naftifine patients were mycologically cured two weeks after therapy (the abstract is truncated). |
| [6388169](https://pubmed.ncbi.nlm.nih.gov/6388169/) | 1984 | RCT | Z Hautkr | Multicenter, double-blind, contralateral comparison of naftifine and clotrimazole cream in 126 patients with dermatophytosis or candidosis. After 7 days, 63.5% were mycologically cured with naftifine vs 56% with clotrimazole. |
| [2620916](https://pubmed.ncbi.nlm.nih.gov/2620916/) | 1989 | Open clinical study | G Ital Dermatol Venereol | Open study of 29 patients with dermatomycoses, including only 2 with cutaneous candidiasis, so it says little about candidiasis specifically. |
| [1723367](https://pubmed.ncbi.nlm.nih.gov/1723367/) | 1991 | Review | Drugs | Review of naftifine's antimicrobial activity and use in superficial dermatomycoses. Potent against dermatophytes, with good clinical and mycological correlation. |
| [18346400](https://pubmed.ncbi.nlm.nih.gov/18346400/) | 2008 | Review | J Cutan Med Surg | Naftifine is effective and safe in superficial dermatomycoses. It has good in vitro activity against Candida and Aspergillus species. |
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Review | J Drugs Dermatol | Review of topical antifungal therapy for superficial cutaneous fungal infections, focused on naftifine for dermatophytosis. |
| [20677526](https://pubmed.ncbi.nlm.nih.gov/20677526/) | 2010 | Review | J Drugs Dermatol | Overview of naftifine as a topical allylamine (no abstract available). |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA204286 | Naftin | Gel | Legacy Pharma USA Inc. |
| ANDA206901 | Naftifine Hydrochloride | Cream | Sun Pharmaceutical Industries, Inc. |
| ANDA208201 | Naftifine Hydrochloride | Gel | Sun Pharmaceutical Industries, Inc. |
| ANDA205975 | Naftifine Hydrochloride | Cream | Sun Pharmaceutical Industries, Inc. |

All four products are topical (cream or gel). Approved-indication text was not provided for any of them.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two controlled clinical studies in candidiasis, including a vehicle-controlled trial of 60 patients, and a marketed topical product point in the same direction. The evidence is old, small and partly truncated, and allylamines are less potent against Candida. The product is already marketed in the same topical form, which lowers the route and formulation barrier.

**To proceed, the following is needed:**
- Package insert warnings and contraindications. This is a blocking gap that must be closed before safety screening.
- Full text of PMID 3048914 and 6388169 to confirm the candidiasis-specific results, since the abstracts are truncated.
- Head-to-head comparison against azole antifungals, which are standard for cutaneous candidiasis.
- Detailed mechanism of action data from DrugBank.
- Consider prioritizing pityriasis versicolor (a yeast infection) as a parallel indication. It has two naftifine-specific clinical studies, from 1986 and 2011.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


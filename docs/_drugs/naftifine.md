---
layout: default
title: Naftifine
parent: 僅模型預測 (L5)
nav_order: 952
evidence_level: L5
indication_count: 8
---

# Naftifine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Naftifine: From Dermatophytosis (Tinea) to Cutaneous Candidiasis

## One-Sentence Summary

> Naftifine is a topical allylamine antifungal, established for treating superficial dermatophyte (tinea) infections of the skin.
> The TxGNN model predicts it may also be effective for **Cutaneous Candidiasis**,
> with **no registered clinical trials** but **9 supporting publications**, including one direct double-blind RCT and one dedicated candidiasis trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Superficial dermatophytosis / tinea infections (per literature evidence; no formal TFDA license record available — see Data Gaps) |
| Predicted New Indication | Cutaneous Candidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, official mechanism-of-action data (DrugBank MOA field) is marked as a data gap. However, the literature evidence collected in this pack consistently describes naftifine as an **allylamine-class antifungal** that inhibits **squalene epoxidase**, blocking ergosterol biosynthesis in the fungal cell membrane — the same target class as terbinafine. Several sources also note naftifine may carry additional anti-inflammatory and antibacterial properties, though the precise mechanism is not fully characterized (PMID 1723367).

Naftifine's established use is against dermatophytes (tinea corporis, tinea pedis, tinea versicolor), which are keratinophilic filamentous fungi. Candida albicans is a yeast rather than a dermatophyte, but multiple reviews in this evidence set explicitly note that naftifine "provides good activity against Candida and Aspergillus species" in addition to dermatophytes (PMID 18346400). This dual antifungal spectrum is the mechanistic basis for the TxGNN prediction.

Importantly, this repurposing signal is not purely theoretical — a dedicated double-blind, vehicle-controlled clinical trial of naftifine cream specifically in cutaneous candidiasis exists (PMID 3048914), along with a multicenter contralateral-comparison RCT that included candidosis patients (PMID 6388169). This places the candidiasis indication on stronger empirical footing than most of the other TxGNN-ranked candidates for this drug, several of which (e.g., "ectothrix infectious disease," "dermatophytosis of scalp or beard") had zero or only irrelevant literature hits.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6388169](https://pubmed.ncbi.nlm.nih.gov/6388169/) | 1984 | RCT (double-blind, contralateral comparison vs clotrimazole) | Zeitschrift für Hautkrankheiten | In 126 patients with dermatophytosis or candidosis, naftifine achieved 63.5% mycological cure at 7 days vs. 56% for clotrimazole, with comparable local tolerance |
| [3048914](https://pubmed.ncbi.nlm.nih.gov/3048914/) | 1988 | Cohort/open-label (described as double-blind, parallel-group in abstract) | Cutis | 60 patients with cutaneous candidiasis randomized to naftifine 1% cream vs. vehicle twice daily for 3 weeks; 77% mycological cure in the naftifine group two weeks post-therapy |
| [18346400](https://pubmed.ncbi.nlm.nih.gov/18346400/) | 2008 | Review | Journal of Cutaneous Medicine and Surgery | Naftifine is fungicidal in vitro against dermatophytes and provides good activity against Candida and Aspergillus species; also active against gram-positive/negative bacteria |
| [2620916](https://pubmed.ncbi.nlm.nih.gov/2620916/) | 1989 | Cohort | Giornale Italiano di Dermatologia e Venereologia | Open, mycologically-controlled study of 29 patients with dermatomycosis from dermatophytes and yeasts, including 2 cutaneous candidiasis cases; naftifine (cream/gel/solution) was effective and well tolerated |
| [1723367](https://pubmed.ncbi.nlm.nih.gov/1723367/) | 1991 | Review | Drugs | Comprehensive review of naftifine's antimicrobial activity, squalene epoxidase inhibition mechanism, and clinical/mycological efficacy in dermatomycoses |
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Review | Journal of Drugs in Dermatology | Overview of topical antifungal therapy optimization for superficial cutaneous fungal infections, including naftifine for cutaneous dermatophytosis |
| [18840006](https://pubmed.ncbi.nlm.nih.gov/18840006/) | 2008 | Review (comparator drug — fenticonazole) | Drugs | Reviews fenticonazole's antimycotic mechanisms against dermatophytes and yeasts; included as comparator-class evidence, not naftifine-specific |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Review (comparator drug — terbinafine) | Drugs | Reviews terbinafine (same allylamine class as naftifine), noting fungistatic activity against Candida albicans |
| [20677526](https://pubmed.ncbi.nlm.nih.gov/20677526/) | 2010 | Review | Journal of Drugs in Dermatology | General review of naftifine as a topical allylamine (no abstract available) |

---

## US Market Information

No license or NDA records are available — the drug is currently **not marketed** in this jurisdiction (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence Level L2 is supported by a direct, purpose-built RCT of naftifine cream in cutaneous candidiasis (PMID 3048914, 77% mycological cure) plus a corroborating multicenter contralateral-comparison trial (PMID 6388169) and multiple reviews confirming in vitro anti-Candida activity. However, both key trials are decades old (1984/1988), small, and predate modern GCP standards, so confirmatory contemporary data is still needed before broader adoption.

**To proceed, the following is needed:**
- TFDA-equivalent package insert / label data (currently Blocking data gap — required for safety review, S1)
- Confirmed mechanism-of-action documentation from DrugBank (currently High-severity data gap)
- A modern, adequately powered RCT of naftifine specifically for cutaneous candidiasis to update the 1980s-era evidence base
- Drug-drug interaction and contraindication data (currently not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


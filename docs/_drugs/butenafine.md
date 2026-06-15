---
layout: default
title: Butenafine
parent: 僅模型預測 (L5)
nav_order: 481
evidence_level: L5
indication_count: 5
---

# Butenafine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Butenafine: From Superficial Dermatophytosis to Cutaneous Candidiasis

## One-Sentence Summary

Butenafine is a synthetic benzylamine antifungal agent, clinically established for treating superficial dermatophytoses including tinea pedis, tinea cruris, and tinea corporis; it is not currently marketed in the US regulatory dataset on file.
The TxGNN model's top prediction suggests potential efficacy for **Cutaneous Candidiasis** (score 99.33%), though mechanistic evidence for this specific extension is indirect and weak.
This indication is supported by **0 clinical trials** and **3 publications** — notably, the model's Rank 2 prediction of **Superficial Mycosis** carries substantially stronger evidence (**2 RCTs**, **9 additional publications**, L1 level), representing the drug's established therapeutic territory.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no regulatory records on file for US market) |
| Predicted New Indication | Cutaneous Candidiasis |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L4 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is not available in the structured dataset for this candidate. From the published literature included in this Evidence Pack, butenafine hydrochloride is a benzylamine derivative that inhibits **squalene epoxidase** — a fungal enzyme critical for ergosterol biosynthesis. This inhibition causes two compounding effects: depletion of ergosterol (which destabilizes the fungal cell membrane) and toxic accumulation of squalene. Because this action is fungicidal rather than fungistatic, butenafine provides durable post-treatment activity lasting at least four weeks after discontinuation. The drug reaches therapeutic concentrations in the stratum corneum after topical application, where dermatophytes predominantly reside.

The connection to cutaneous candidiasis is where the prediction becomes mechanistically strained. Candida albicans and related species depend on squalene epoxidase to a far lesser degree than dermatophytes (Trichophyton, Microsporum, Epidermophyton), and they possess alternative ergosterol synthesis routes that partially bypass the blocked step. In vitro MIC data consistently show butenafine activity against Candida is weak (MIC > 8 µg/mL), compared to low MICs against dermatophytes. The three literature citations retrieved for this indication treat butenafine as a comparator or background reference — not as a primary Candida agent.

The TxGNN model likely captured the phenotypic overlap: both cutaneous candidiasis and tinea present as superficial skin infections responsive to topical antifungals, sharing disease-level graph proximity. This makes the graph-based prediction structurally coherent, even though the drug-target biology does not support a strong mechanistic case for Candida specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for butenafine in cutaneous candidiasis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Review | J Drugs Dermatol | Butenafine listed among available topical antifungals for superficial cutaneous fungal infections; article notes dermatophytes (Trichophyton spp.) as the predominant pathogens — Candida coverage not a primary focus |
| [11302816](https://pubmed.ncbi.nlm.nih.gov/11302816/) | 2001 | In vitro comparative | Antimicrob Agents Chemother | Guinea pig cutaneous candidiasis model used to benchmark novel triazole KP-103; butenafine serves as a reference comparator, confirming its weaker anti-Candida activity relative to azoles |
| [11893219](https://pubmed.ncbi.nlm.nih.gov/11893219/) | 2002 | Review | Am J Clin Dermatol | Narrative review of six novel antimycotics including butenafine; documents potential for cutaneous and mucosal disease applications but acknowledges spectrum limitations against Candida |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Butenafine's squalene epoxidase inhibition is a poor fit for Candida infections — where the enzyme target is less critical and in vitro activity is consistently weak — and no clinical trial evidence supports this indication. The high TxGNN score reflects graph-level phenotypic proximity rather than a drug-target mechanistic match.

**Note on Rank 2 (Superficial Mycosis — L1 evidence, Proceed with Guardrails):** The model's second prediction describes what is effectively butenafine's established clinical role. Two RCTs (including a head-to-head trial vs. bifonazole, PMID [23283047](https://pubmed.ncbi.nlm.nih.gov/23283047/)) and nine supporting publications confirm efficacy in tinea pedis, tinea corporis, tinea cruris, and pityriasis versicolor. If the objective is establishing a regulatory pathway, Superficial Mycosis is the higher-priority and more actionable candidate.

**To proceed with Cutaneous Candidiasis, the following is needed:**
- In vitro MIC90 data for Candida albicans and non-albicans Candida to formally assess susceptibility
- Formal MOA documentation (DrugBank API query recommended per data gap DG002)
- At least one proof-of-concept clinical study comparing butenafine to azole standard of care in skin candidiasis
- Taiwan/US regulatory package insert retrieval to address safety data gaps (DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


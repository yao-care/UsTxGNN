---
layout: default
title: Butenafine
parent: Moderate Evidence (L3-L4)
nav_order: 481
evidence_level: L4
indication_count: 5
---

# Butenafine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Butenafine: From Topical Antifungal Use to Cutaneous Candidiasis

## One-Sentence Summary

Butenafine is a topical benzylamine antifungal marketed in the US as creams for skin fungal infections. The TxGNN model predicts it may be effective for **cutaneous candidiasis**, but there are **0 registered clinical trials** and **3 publications** for this indication, none with butenafine-specific Candida data. The evidence is model prediction plus general antifungal literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied US license records. The literature describes use in tinea pedis, tinea cruris, tinea corporis and pityriasis versicolor. |
| Predicted New Indication | Cutaneous candidiasis |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (NDA and ANDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on general pharmacology (not the supplied data), butenafine is a benzylamine that inhibits squalene epoxidase. This depletes ergosterol and causes toxic squalene to accumulate in the fungal cell. It is strongly fungicidal against dermatophytes.

Cutaneous candidiasis is a superficial skin infection by yeast, so it is close to butenafine's established use in superficial fungal disease, and the topical route suits it. The TxGNN score reflects network similarity between butenafine and other antifungals.

The main weakness is that butenafine's activity against *Candida* is generally weaker than against dermatophytes. The only Candida-related papers in the pack are a general review of six antimycotics (including butenafine), an animal study of a different drug (KP-103), and a naftifine review. None provides butenafine-specific Candida clinical data, so this prediction is a research question rather than a supported use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11893219](https://pubmed.ncbi.nlm.nih.gov/11893219/) | 2002 | Review | Am J Clin Dermatol | Reviews six newer antimycotics, including butenafine, for skin and mucosal fungal disease. No butenafine-specific Candida results are visible in the supplied excerpt. |
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Review | J Drugs Dermatol | Overview of topical therapy for superficial cutaneous fungal infections (dermatophytes and yeasts), focused on naftifine, not butenafine. |
| [11302816](https://pubmed.ncbi.nlm.nih.gov/11302816/) | 2001 | Preclinical (different drug) | Antimicrob Agents Chemother | In vitro and guinea pig study of KP-103, a triazole, in tinea pedis and cutaneous candidiasis. It says nothing directly about butenafine. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021307 | Lotrimin Ultra | Cream | Bayer Healthcare LLC. |
| ANDA205181 | Butenafine Hydrochloride | Cream | Meijer Distribution Inc |
| ANDA205181 | Butenafine Hydrochloride | Cream | Wal-Mart Stores Inc |
| ANDA205181 | Butenafine Hydrochloride | Cream | YYBA Corp |
| ANDA205181 | Athletes Foot | Cream | Sun Pharmaceutical Industries, Inc. |

Marketed forms are topical only (cream, gel). The records supplied contain no approved-indication text.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for butenafine.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The cutaneous candidiasis prediction rests on a high model score alone, with no registered trials and no butenafine-specific Candida clinical data. Butenafine's activity against Candida is also generally weaker than against dermatophytes.

**Other predicted indications from the same run:**

| Indication | TxGNN Score | Evidence Level | Suggested Decision |
|------|------|------|------|
| Superficial mycosis | 99.02% | L1 | Proceed with Guardrails |
| Endothrix infectious disease | 99.02% | L5 | Hold |
| Ectothrix infectious disease | 99.02% | L5 | Hold |
| Majocchi granuloma | 99.02% | L5 | Hold |

Superficial mycosis is the only well-supported direction. It has vehicle-controlled and comparator trials in tinea infections (for example PMID 9039200, 11676116 and 23283047) plus several reviews. However, this is essentially butenafine's established use rather than a new repurposing signal. The L1 grade was inferred from titles and abstracts only and needs confirmation against full texts. The hair-shaft and deep follicular infections (endothrix, ectothrix, Majocchi granuloma) have no supporting data. Topical agents generally penetrate these sites poorly.

**To proceed, the following is needed:**
- Butenafine-specific in vitro susceptibility data (MIC) against *Candida* species
- A controlled clinical study, or a registered trial, of butenafine in cutaneous candidiasis
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the original approved indications from the license records
- Confirmation of the evidence grade for superficial mycosis from full-text review of the cited trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


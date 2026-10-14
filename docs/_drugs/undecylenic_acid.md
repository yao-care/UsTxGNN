---
layout: default
title: Undecylenic Acid
parent: Model Prediction Only (L5)
nav_order: 1275
evidence_level: L5
indication_count: 7
---

# Undecylenic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Undecylenic Acid: From Tinea Pedis and Tinea Corporis to Dermatophytosis of the Groin and Perianal Area

## One-Sentence Summary

Undecylenic acid is a topical fatty acid used as an antifungal, originally for tinea pedis, tinea corporis and other tinea infections.
The TxGNN model predicts it may be effective for **dermatophytosis of the groin and perianal area (tinea cruris)**, but **no clinical trials** and **no publications** directly support this prediction. The prediction rests on model output alone, and it is largely an extension of the existing tinea uses rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea infection |
| Predicted New Indication | Dermatophytosis of the groin and perianal area |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorization) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, undecylenic acid is generally described as a topical fungistatic fatty acid. Its use in tinea pedis and tinea corporis is established, and mechanistically it may be applicable to other dermatophyte skin infections.

Tinea cruris is a dermatophyte infection of the groin. It is caused by the same group of organisms as tinea pedis and tinea corporis, and it affects similar skin sites. This makes the prediction biologically plausible. The prediction is largely a label extension, and no studies in the data compiled for this report test it directly.

**Other predicted indications (all lower priority):**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Majocchi granuloma | 99.08% | L5 | Deep follicular infection. A topical fatty acid is unlikely to reach the site, and systemic therapy is usually needed. |
| 3 | Ectothrix infectious disease | 99.08% | L5 | Hair infection with spores outside the shaft. No evidence, and follicle penetration is uncertain. |
| 4 | Endothrix infectious disease | 99.03% | L5 | Spores inside the hair shaft. Topical penetration is poor and systemic therapy is the standard. |
| 5 | Dermatophytosis of scalp or beard | 99.02% | L4 | Only one 1956 historical report on a combination product. Scalp infection generally requires systemic therapy. |
| 6 | Pityriasis versicolor | 99.01% | L5 | Caused by Malassezia yeast, not dermatophytes. No supporting data, and established azole and selenium sulfide options exist. |
| 7 | Superficial mycosis | 99.01% | L4 | Closest to the original uses, with two indirect publications. Rated a research question. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications were found for the top-ranked prediction (tinea cruris). Indirect literature exists for two lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42334914](https://pubmed.ncbi.nlm.nih.gov/42334914/) | 2026 | Review / clinical recommendations | Ceska a Slovenska farmacie | Covers over-the-counter treatment of tinea pedis (athlete's foot). Full text is needed to confirm whether undecylenic acid is discussed. |
| [28906086](https://pubmed.ncbi.nlm.nih.gov/28906086/) | 2017 | Formulation / review | Giornale italiano di dermatologia e venereologia | New topical formulation for onychomycosis. Titles and the abstract excerpt do not show whether undecylenic acid is included. |
| [13371368](https://pubmed.ncbi.nlm.nih.gov/13371368/) | 1956 | Historical clinical report (uncontrolled) | Southern Medical Journal | Treatment of tinea capitis due to *Microsporum audouini* with Salundek ointment and lotion. This is a combination product, so effects cannot be attributed to undecylenic acid alone. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M005 | ViLLsure Antifungal Pen | Liquid | Not specified (cancelled) |
| part333C | CVS Pharmacy | Liquid | Not specified (cancelled) |
| M002 | SFEIXE Antifungal Pen | Paste | Not specified (cancelled) |

All three authorizations are cancelled. Other dosage forms recorded for the drug include cream and spray.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.94%) and tinea cruris is biologically close to the existing tinea uses. However, the evidence level is L5, with no trials and no literature. There are also no currently valid US authorizations, and the safety and mechanism data are incomplete.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Full-text review of PMID 42334914 and PMID 28906086 to check for undecylenic acid efficacy data
- A literature search targeted at tinea cruris and undecylenic acid
- Clarification of the regulatory status of current marketed products, since all three records are cancelled
- Route and formulation compatibility assessment (currently pending)
- Among the lower-ranked candidates, the deep and hair-follicle infections (Majocchi granuloma, ectothrix, endothrix, scalp) are unlikely to suit a topical agent and should not be prioritized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


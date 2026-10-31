---
layout: default
title: Miconazole
parent: Moderate Evidence (L3-L4)
nav_order: 925
evidence_level: L3
indication_count: 1
monitor_inn: "MICONAZOLE"
predicted_indications: ["acne (disease)"]
last_modified_at: 2026-10-31
description: "Miconazole: predicted new indication Acne (disease) (evidence level L3). Approved use: Not recorded in the local data"
---

# Miconazole
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
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

## Miconazole: Acne (disease)
{: .text-alpha }

## One-Sentence Summary

Miconazole is an imidazole antifungal, originally used for fungal and yeast infections of the skin and vagina, such as tinea pedis, tinea corporis, cutaneous candidiasis and vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **acne**, with **0 registered clinical trials** and **4 publications** (1 small split-face clinical study, 1 review, 1 therapeutic trial in a look-alike condition and 1 in vitro study) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L3 (observational or small clinical studies and a review only; no completed Phase 2/3 RCTs) |
| US Market Status | Marketed (valid licenses on record: at least 6) |
| Number of FDA Applications | at least 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general knowledge, miconazole is an azole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks ergosterol synthesis and damages the fungal cell membrane. This reasoning rests on general knowledge of azoles, not on the provided record.

The link to acne is plausible through three routes:
1. **Activity against acne bacteria:** An in vitro study of azole antifungals tested their activity against *Propionibacterium acnes* isolated from patients with acne vulgaris. This matters because antibiotic-resistant strains are increasingly common.
2. **Activity against Malassezia (Pityrosporum):** Malassezia causes folliculitis that looks very much like acne and is often misdiagnosed as acne. Part of the apparent benefit may come from treating this look-alike condition rather than true acne vulgaris.
3. **Anti-inflammatory effects on skin:** A review describes multiple effects of miconazole on skin disorders.

Direct evidence in true acne is thin: a small split-face study in mild inflammatory catamenial acne. The high TxGNN score is a computational prediction, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical study (split-face, small sample) | Skin Res Technol | Clinical and bioinstrumental assessment in mild inflammatory catamenial acne in young women; the only study directly in acne |
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opin Pharmacother | Overview of the multifaceted effects of miconazole on skin disorders; miconazole nitrate is a long-established imidazole antifungal |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Clinical study / therapeutic trial | Clin Exp Dermatol | 62 patients with Pityrosporum (Malassezia) folliculitis, a condition often misdiagnosed as acne vulgaris; this is not acne vulgaris itself |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | Biol Pharm Bull | In vitro activity of azole antifungals against *P. acnes* isolated from acne vulgaris patients |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M005 | MICONAZOLE Nitrate 2% | Cream | Not stated (valid) |
| ANDA076773 | Miconazole 3 | Cream | Not stated (valid) |
| ANDA074760 | good sense miconazole 7 | Cream | Not stated (valid) |
| ANDA073508 | Miconazole Nitrate | Suppository | Not stated (valid) |
| ANDA091366 | basic care miconazole 3 | Cream | Not stated (valid) |

All six licenses on record are valid; a sixth, ANDA074444 (Miconazole 7, cream), is not listed above.

## Safety Considerations

- **Disease-related cautions (knowledge graph):** Contraindication links to liver disease and gallbladder disease. These come from the drug-disease knowledge graph, not from label text.
- **Drug Interactions:** 100 interactions were found. Examples of those rated Moderate include paclitaxel, fentanyl, alfentanil, hydrocodone, acalabrutinib, nifedipine, amlodipine, amiodarone, amitriptyline, alprazolam, alfuzosin, aliskiren, alosetron, ethinylestradiol and estradiol. Minor examples include dolutegravir, loratadine, amphotericin B and ambrisentan. Many involve drugs metabolized by CYP enzymes, so systemic exposure matters.

Please refer to the package insert for warnings and contraindications from the label.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence for acne is weak: no registered trials, one small split-face study, and supporting data that are in vitro or in a look-alike condition (Malassezia folliculitis). The drug is marketed in the US with six valid licenses, and the label safety information has not been reviewed. The high TxGNN score alone does not justify advancing.

**To proceed, the following is needed:**
- Review of the FDA package insert for warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- A controlled trial in acne vulgaris, ideally distinguishing it from Malassezia folliculitis
- Assessment of topical formulation suitability and dosing for acne
- Evaluation of the interaction and liver-related safety signals if any systemic exposure is expected
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


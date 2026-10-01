---
layout: default
title: Hyaluronic Acid
parent: Model Prediction Only (L5)
nav_order: 774
evidence_level: L5
indication_count: 10
---

# Hyaluronic Acid
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

# Hyaluronic Acid: From Marketed Topical and Cosmetic Products to Dry Eye Syndrome

## One-Sentence Summary

Hyaluronic acid is a water-retaining, lubricating molecule. In the US records supplied it appears mainly in skin-care, topical and other non-ophthalmic products, and no approved indication text is listed.
The TxGNN model predicts it may be effective for **dry eye syndrome**, with **50 clinical trials** and **20 publications** retrieved for this indication.
Evidence is strong: two completed Phase 3 trials, several Phase 4 trials, and meta-analyses of randomized trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records (all approved-indication fields are empty) |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 (see caveat below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 18 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank for this record. Hyaluronic acid is a well-characterized, hygroscopic, viscoelastic glycosaminoglycan. It holds water on the ocular surface, lubricates, stabilizes the tear film, and may support corneal epithelial healing, partly through the CD44 receptor.

The US license records give no original indication, so the link rests on the mechanism. Dry eye is mainly a problem of tear-film instability and surface dryness, which is what a humectant and lubricant addresses. Sodium hyaluronate eye drops are also widely used as the standard comparator in dry eye trials, as seen in many of the studies below.

**Evidence-level caveat:** L1 is assigned because two completed Phase 3 trials exist (NCT01382225 and NCT01240382). In NCT01240382, sodium hyaluronate is the comparator arm, not the test drug. Further support comes from completed Phase 4 trials and meta-analyses of randomized trials. Label status for an ophthalmic product should still be verified against the actual product label, because none of the listed US licenses is an eye drop.

## Clinical Trial Evidence

No trial results were included in the data, so the findings column reflects study design and stated objectives only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01382225](https://clinicaltrials.gov/study/NCT01382225) | Phase 3 | Completed | 1936 | Randomized, double-masked trial of 0.18% sodium hyaluronate for signs and symptoms of dry eye |
| [NCT01240382](https://clinicaltrials.gov/study/NCT01240382) | Phase 3 | Completed | 332 | Double-masked non-inferiority comparison of 3% DE-089 vs 0.1% sodium hyaluronate (HA is the comparator) |
| [NCT02777723](https://clinicaltrials.gov/study/NCT02777723) | Phase 3 | Unknown | 138 | Active-controlled, double-blind trial of CKD-350 eye drops in dry eye syndrome |
| [NCT00938704](https://clinicaltrials.gov/study/NCT00938704) | Phase 4 | Completed | 71 | Randomized comparison of carboxymethylcellulose + glycerin vs 0.18% sodium hyaluronate, non-preserved artificial tears |
| [NCT03888183](https://clinicaltrials.gov/study/NCT03888183) | Phase 4 | Unknown | 334 | Randomized, double-blind, controlled trial of preservative-free low-dose HA salt solution |
| [NCT06517667](https://clinicaltrials.gov/study/NCT06517667) | Phase 2/3 | Completed | 30 | Randomized, single-blind comparison of different HA tear-substitute formulations in evaporative dry eye |
| [NCT00788229](https://clinicaltrials.gov/study/NCT00788229) | Phase 2 | Completed | 72 | Randomized, double-blind study of artificial tears (DHP-101/300/500) in dry eye syndrome |
| [NCT02510235](https://clinicaltrials.gov/study/NCT02510235) | Not labeled | Completed | 56 | Double-masked non-inferiority study of Lubricin vs 0.13% sodium hyaluronate in moderate dry eye |
| [NCT05356728](https://clinicaltrials.gov/study/NCT05356728) | Not labeled | Unknown | 96 | Two artificial tears compared, including a trehalose + hyaluronate product |
| [NCT06731725](https://clinicaltrials.gov/study/NCT06731725) | Not labeled | Completed | 20 | Single-arm post-marketing study of an HA-based product in mild/moderate dry eye |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [39260878](https://pubmed.ncbi.nlm.nih.gov/39260878/) | 2024 | RCT | BMJ | Non-inferiority trial of laughter exercise vs 0.1% sodium hyaluronate for dry eye discomfort (HA as comparator) |
| [37117131](https://pubmed.ncbi.nlm.nih.gov/37117131/) | 2023 | RCT | Contact Lens & Anterior Eye | Trehalose + HA artificial tears over 3 months in women with moderate to severe dry eye |
| [33804439](https://pubmed.ncbi.nlm.nih.gov/33804439/) | 2021 | Meta-analysis | Int J Environ Res Public Health | Compares HA-based vs non-HA eye drops (saline and conventional artificial tears) for dry eye |
| [38895674](https://pubmed.ncbi.nlm.nih.gov/38895674/) | 2024 | Systematic review / meta-analysis | Int J Ophthalmol | Compares high vs low concentrations of HA eye drops for dry eye |
| [35514082](https://pubmed.ncbi.nlm.nih.gov/35514082/) | 2022 | Review | Acta Ophthalmol | Critical review of the safety and efficacy of HA-containing artificial tears in dry eye disease |
| [37042308](https://pubmed.ncbi.nlm.nih.gov/37042308/) | 2024 | Review | Acta Ophthalmol | Summarizes ingredients directly compared with HA in dry eye; describes HA as a long-standing safe and effective treatment |
| [34843023](https://pubmed.ncbi.nlm.nih.gov/34843023/) | 2022 | Randomized multicenter study | Jpn J Ophthalmol | Sequential use of 0.3% and 0.15% unpreserved HA for dry eye |
| [34562113](https://pubmed.ncbi.nlm.nih.gov/34562113/) | 2022 | Clinical study | Graefes Arch Clin Exp Ophthalmol | 0.3% HA with cyanocobalamin and electrolytes in menopausal patients with moderate dry eye |
| [30510396](https://pubmed.ncbi.nlm.nih.gov/30510396/) | 2018 | Clinical study | Clin Ophthalmol | Safety and efficacy of a cross-linked HA gel occlusive device for dry eye |
| [38838456](https://pubmed.ncbi.nlm.nih.gov/38838456/) | 2024 | Clinical study | J Fr Ophtalmol | New preservative-free drop combining HA, trehalose and NAAGA in dry eye patients |

## US Market Information

None of the licenses states an approved indication, and none is an ophthalmic eye drop.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M016 | Roushun kojic Skin Lightening Nutural Skin Care treament serum 30ml | Liquid | Not stated |
| Not listed | JASBELLO VAGINAL | Suppository | Not stated |
| Not listed | EyeOne eyelid cleansing tools | Cloth | Not stated |
| M016 | ClearSoothingCream | Cream | Not stated |
| M016 | Body essential oil | Liquid | Not stated |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 trials, multiple Phase 4 trials, and meta-analyses of randomized trials directly address HA in dry eye. Its lubricating and tear-film mechanism is plausible, and HA is a common comparator in dry eye trials. The guardrails are that the US license records list no ophthalmic product, no indication text or safety data are available, and one of the two Phase 3 trials uses HA only as the comparator.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Confirmation of a licensed ophthalmic HA product and its approved indication
- Verification of the HA-specific arms in the Phase 4 and Phase 2/3 trials, and of the results of the two Phase 3 trials
- Detailed mechanism-of-action data from DrugBank
- Consolidation of the overlapping predicted indication "xerophthalmia" (in the sources it means dry eye, not vitamin A deficiency) with dry eye syndrome
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


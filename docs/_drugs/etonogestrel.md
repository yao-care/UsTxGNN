---
layout: default
title: Etonogestrel
parent: Model Prediction Only (L5)
nav_order: 684
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a progestin used in contraceptive products such as the Nexplanon implant and the NuvaRing vaginal ring. The original indication is inferred from the product forms and trial data, because no indication text was provided.
The TxGNN model predicts it may be effective for **amenorrhea**, but only **1 indirectly related clinical trial** and **1 loosely related publication** exist, and amenorrhea is more likely an expected effect of the drug than a treatment target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided data (contraception inferred from implant and ring products) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (indirect evidence only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Etonogestrel is a progestin, and progestins generally suppress ovulation and thin the endometrium. Its contraceptive efficacy is established through the marketed implant and ring products.

Amenorrhea is a well-known bleeding-pattern effect of the etonogestrel implant and ring. It is therefore an expected pharmacological effect or adverse event of a contraceptive, not a therapeutic indication. The high TxGNN score likely reflects this drug-disease association in the knowledge graph.

Whether the drug induces or treats amenorrhea is unresolved. This direction-of-effect question needs review before any repurposing claim is made.

The model also ranked four breast conditions:
- fibrocystic disease
- apocrine adenosis
- blunt duct adenosis
- benign mammary dysplasia

These have scores of 99.2%–99.6% but no trials or literature. The last three are histologic variants or synonyms of the first, so their scores are not independent evidence. The hormonal rationale for them is speculative.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Single-arm, open-label study of the etonogestrel implant (MK-8415) as the only contraceptive method in years 4–5 of use, in females ≤35 years. It was not designed to test amenorrhea and has no comparator, so amenorrhea could appear only as a secondary bleeding-pattern outcome. Indirect evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Randomized multicenter study in China (n=200) comparing the single-rod Implanon with the six-capsule Norplant implant for contraceptive efficacy, tolerability and bleeding patterns. There were no pregnancies. It is relevant to bleeding patterns, not to treating amenorrhea. |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT protocol | Trials | Protocol for BIO101 in preventing respiratory deterioration in COVID-19 pneumonia. It appears unrelated to etonogestrel or amenorrhea. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021529 | Nexplanon | Implant | Organon LLC |
| ANDA211157 | EnilloRing | Ring | Xiromed, LLC |
| NDA021187 | Etonogestrel/Ethinyl Estradiol | Insert, extended release | Prasco Laboratories |
| NDA021187 | NuvaRing | Insert, extended release | A-S Medication Solutions |

Approved indication text was not provided for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only related trial is a single-arm contraceptive study that does not test amenorrhea as a treatment target, and the literature does not support treating amenorrhea. The high model score most likely reflects amenorrhea as an expected effect of contraceptive use, not a repurposing opportunity.

**To proceed, the following is needed:**
- Clarify whether the prediction means treating amenorrhea or inducing it as an effect. If it is only an expected effect, close the candidate.
- Obtain FDA package insert warnings, contraindications and approved indication text (blocking for safety screening).
- Obtain mechanism of action data from DrugBank.
- If pursued, find controlled studies with amenorrhea as a primary outcome.
- For the breast conditions, collect clinical evidence first, since the predictions are model-derived only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Sulfacetamide
parent: Model Prediction Only (L5)
nav_order: 1185
evidence_level: L5
indication_count: 10
---

# Sulfacetamide
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

# Sulfacetamide: From Topical Antibacterial Use to Postinfectious Vasculitis

## One-Sentence Summary

Sulfacetamide is a sulfonamide antibacterial sold in the US as topical, ophthalmic and dermatologic products such as shampoos, gels, lotions, creams and solutions.
The TxGNN model ranks **postinfectious vasculitis** as its top predicted new indication, but **0 clinical trials** and **0 publications** support it. This is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records (the products are topical, ophthalmic and dermatologic antibacterials) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.99% (scores are saturated across all candidates and do not discriminate between them) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank for this record. Sulfacetamide is a bacteriostatic sulfonamide that inhibits dihydropteroate synthase, blocking bacterial folate synthesis.

The link to the predicted indication is weak. Postinfectious vasculitis is mainly an immune-complex-mediated inflammatory condition that develops after an infection. An antibacterial has no clear target in it, and the topical products would not reach affected vessels in any case.

The TxGNN score of 0.99994 should not be read as strong support. Scores across all ten candidates fall between about 0.998 and 0.9999. A model-only prediction like this needs independent evidence before it can be considered credible.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications Worth Noting

Only one other candidate has evidence that resembles the antibacterial mechanism. Because the top-ranked prediction has no support, the one candidate with literature is shown here for context.

| Rank | Predicted Indication | Evidence Level | Evidence Summary | Decision Stage |
|------|------|------|------|------|
| 3 | Otitis externa | L3 | Four publications, two of them double-blind RCTs. Both tested a fixed combination (trimethoprim-sulphacetamide-polymyxin B), so sulfacetamide's own contribution cannot be isolated. | S1 (Research Question) |
| 2 | Post-bacterial disorder | L4 | One early Phase 1 osteomyelitis trial, terminated with 11 patients. It gives no efficacy signal. | S0 (Hold) |
| 10 | Parasitic eyelid infestation | L4 | One Demodex blepharitis paper, which does not test sulfacetamide. | S0 (Hold) |
| 9 | Exposure keratitis | L5 | Only a 1985 case report of erythema multiforme after topical sulfacetamide. This is a safety signal, not evidence of benefit. | S0 (Hold) |

Ranks 4-8 (post-infectious syndrome, infective urethral stricture, Chagas cardiomyopathy, infection-related hemolytic uremic syndrome, punctate epithelial keratoconjunctivitis) have no trials or literature.

### Otitis externa (rank 3) evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6269476](https://pubmed.ncbi.nlm.nih.gov/6269476/) | 1981 | RCT (double-blind, combination product) | Ann Otolaryngol Chir Cervicofac | 68 patients with otitis externa or otorrhoea. Satisfactory results in 88.6% with trimethoprim-sulphacetamide-polymyxin B, versus 60.6% with trimethoprim-polymyxin B. |
| [207210](https://pubmed.ncbi.nlm.nih.gov/207210/) | 1978 | RCT (double-blind, combination product vs gentamicin) | Ann Otolaryngol Chir Cervicofac | 100 otorrhoea cases. The combination gave positive results in 42 of 50 patients, and both treatments were effective. |
| [13095457](https://pubmed.ncbi.nlm.nih.gov/13095457/) | 1953 | Case series | Eye Ear Nose Throat Mon | Uncontrolled report of 30% sodium sulamyd solution in otitis externa and chronic otitis media. |
| [14867160](https://pubmed.ncbi.nlm.nih.gov/14867160/) | 1951 | Case series | Vestn Otorinolaringol | Uncontrolled report of sulfacyl-sodium in chronic suppurative otitis media and external ear canal inflammation. |

All of this evidence is 45-75 years old and has no phase designation.

---

## US Market Information

The record lists 20 authorizations. Five are shown below. The records do not include approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | PLEXION NS (Eckson Labs, LLC) | Shampoo | Not stated in record |
| Not listed | SULFACETAMIDE SODIUM (KMM Pharmaceuticals, LLC) | Shampoo | Not stated in record |
| Not listed | SULFACETAMIDE SODIUM (Cintex Services, LLC) | Gel | Not stated in record |
| Not listed | OVACE (Mission Pharmacal Company) | Liquid | Not stated in record |
| ANDA089560 | Sulfacetamide Sodium (Asclemed USA, Inc.) | Solution | Not stated in record |

Other marketed forms in the record include solution/drops, lotion and cream.

---

## Safety Considerations

Please refer to the package insert for safety information.

One safety signal appears in the retrieved literature. A 1985 case report ([PMID 3157322](https://pubmed.ncbi.nlm.nih.gov/3157322/)) describes erythema multiforme major in an 8-year-old boy after topical sodium sulfacetamide for conjunctivitis. Sulfonamide hypersensitivity should be considered in any further work.

Two candidates carry additional cautions. In infection-related hemolytic uremic syndrome, antibiotic exposure is generally cautioned against, and sulfonamides carry renal and hematologic concerns. In otitis externa, irritation and ototoxicity risk with a perforated tympanic membrane needs review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, postinfectious vasculitis, has no trials or literature and no plausible mechanistic route for an antibacterial. Its TxGNN score is saturated and does not separate it from the other candidates. The package-insert safety review is also still outstanding, a blocking data gap.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking data gap DG001)
- Mechanism of action data from DrugBank (DG002)
- If any candidate is pursued, start with otitis externa, the only one with controlled-trial literature. This requires evidence that isolates sulfacetamide from the fixed combinations, plus a safety review for ear use.
- Route compatibility and similarity-to-original analysis, both still pending for every candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


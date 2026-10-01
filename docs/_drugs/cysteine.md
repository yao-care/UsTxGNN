---
layout: default
title: Cysteine
parent: Model Prediction Only (L5)
nav_order: 561
evidence_level: L5
indication_count: 7
---

# Cysteine
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

# Cysteine: From an Unspecified Original Indication to Dry Eye Syndrome

## One-Sentence Summary

Cysteine is a marketed amino acid product in the US (injectable and liquid forms), but the available regulatory data does not state its approved indication.
The TxGNN model predicts it may be effective for **dry eye syndrome**, with **6 registered trials** (only 2 of them related to dry symptoms or ocular disease) and **20 publications** retrieved.
Most of the clinical evidence concerns **N-acetylcysteine (NAC)** or NAC-modified polymers, not free cysteine, so the support is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available data (all approved-indication fields are empty) |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 (the source pack labelled L2, but no completed Phase 2/3 RCT in dry eye exists, so the L2 criterion is not met; see the note in Clinical Trial Evidence) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 listed licenses (2 distinct NDA numbers; ELCYS appears twice, and one entry has no NDA number) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for the original use. Based on known information, cysteine is a thiol-containing amino acid and a precursor of glutathione, a major cellular antioxidant. Mechanistically it may be applicable to conditions driven by oxidative stress.

Oxidative stress and inflammation on the ocular surface are recognised contributors to dry eye. Reactive oxygen species can activate NLRP3 inflammasomes in corneal epithelial cells (PMID 25701684). NAC, the acetylated form of cysteine, scavenges reactive oxygen species and is a mucolytic. This gives a plausible link to dry eye, where tear-film and mucus abnormalities are common.

There are three important caveats:
- Nearly all of the ocular evidence is for NAC, chitosan-NAC conjugates or thiolated polymers, not free cysteine.
- The marketed cysteine products are injectable or liquid, whereas the evidence relates to topical eye drops. Route compatibility has not been assessed.
- One 2018 study (PMID 30025127) used topical NAC as a mucolytic to create a mucin-deficient dry eye animal model. Its effect on the ocular surface therefore needs careful evaluation and is not clearly beneficial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04793646](https://clinicaltrials.gov/study/NCT04793646) | N/A | Completed | 60 | Randomised, double-blind, controlled trial of NAC for dryness symptoms in primary Sjögren's syndrome. Results are not in the pack. |
| [NCT04440280](https://clinicaltrials.gov/study/NCT04440280) | Phase 2 | Recruiting | 45 | Topical NAC eye drops to reduce oxidative stress in Fuchs endothelial corneal dystrophy. A different corneal disease. |
| [NCT01424033](https://clinicaltrials.gov/study/NCT01424033) | Phase 2/3 | Terminated | 5 | Oral NAC for connective tissue disease-related interstitial lung disease. Not an ocular indication. |
| [NCT01064830](https://clinicaltrials.gov/study/NCT01064830) | Phase 2 | Completed | 21 | Topical cyclosporine 0.05% under occlusion for brittle nail syndrome. Does not test cysteine. |

Three further retrieved trials (NCT04162210, NCT03525678, NCT03544281) are belantamab mafodotin studies in multiple myeloma, unrelated to cysteine or dry eye, and are omitted.

**Note on evidence level:** no completed Phase 2/3 RCT in dry eye is registered, so L2 is not supported. The only completed randomised trial is Phase "N/A" and tests NAC in Sjögren's-related dryness.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28441068](https://pubmed.ncbi.nlm.nih.gov/28441068/) | 2017 | RCT | J Ocul Pharmacol Ther | Controlled, randomised, double-blind study of chitosan-NAC eye drops on tear film thickness in dry eye syndrome. The abstract excerpt does not report results. |
| [39360368](https://pubmed.ncbi.nlm.nih.gov/39360368/) | 2024 | RCT | Clin Exp Rheumatol | Randomised, placebo-controlled, double-blind study of NAC for dryness symptoms in Sjögren's disease. The abstract excerpt does not report results. |
| [16334742](https://pubmed.ncbi.nlm.nih.gov/16334742/) | 2005 | Clinical comparison | Acta Med Croat | Topical acetylcysteine compared with artificial tears in dry eye. It was proposed as a mucolytic that reduces mucus accumulation. |
| [34339721](https://pubmed.ncbi.nlm.nih.gov/34339721/) | 2022 | Review | Surv Ophthalmol | Systematic search (106 references) on topical NAC in ocular disease, covering mechanisms (mucolysis, radical scavenging), applications and adverse effects. |
| [30025127](https://pubmed.ncbi.nlm.nih.gov/30025127/) | 2018 | Animal study | Invest Ophthalmol Vis Sci | Topical NAC was used to build a mucin-deficient dry eye model, and its effects on tears and the ocular surface were studied. |
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclinical | Adv Mater | Eye-drop nanoformulation of catalase with cysteine-modified chitosan, designed to reduce excess ROS in dry eye. |
| [36581034](https://pubmed.ncbi.nlm.nih.gov/36581034/) | 2023 | Preclinical | Int J Biol Macromol | Chondroitin sulfate-L-cysteine conjugate on dexamethasone lipid carriers, aimed at better corneal retention and permeability. |
| [39842600](https://pubmed.ncbi.nlm.nih.gov/39842600/) | 2025 | Preclinical | Int J Biol Macromol | NAC-chitosan conjugate on dexamethasone lipid carriers, aimed at better permeability and lower inflammation. |
| [24993428](https://pubmed.ncbi.nlm.nih.gov/24993428/) | 2014 | Review | J Control Release | Thiolated polymers (thiomers) have improved mucoadhesion through disulfide bonds with mucus glycoproteins. |
| [25701684](https://pubmed.ncbi.nlm.nih.gov/25701684/) | 2015 | Mechanistic | Exp Eye Res | ROS-activated NLRP3 inflammasomes drive inflammation in hyperosmolarity-stressed corneal epithelial cells and in dry eye patients. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212535 | Cysteine Hydrochloride (Baxter Healthcare) | Injection | Not stated in the available data |
| NDA210660 | ELCYS (Exela Pharma Sciences), listed twice | Injection, solution | Not stated in the available data |
| Not listed | L-Cysteine (Professional Complementary Health Formulas) | Liquid | Not stated in the available data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.98%), but the supporting clinical evidence is for NAC and NAC-conjugates rather than free cysteine. There is no completed Phase 2/3 trial in dry eye. The marketed products are injectable or liquid, not ocular. The package insert warnings and contraindications are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed cysteine products
- Original mechanism of action and approved indication data, to assess the link between the original use and dry eye
- Extraction of results from the NAC RCTs (PMID 28441068, PMID 39360368) and NCT04793646
- A decision on whether the dry eye candidate should really be "NAC" (an ophthalmic formulation) rather than cysteine
- A route and formulation feasibility assessment for topical ocular delivery

**Other predicted indications (all Hold):**

| Indication | TxGNN Score | Evidence Level | Note |
|------|------|------|------|
| Closed-angle glaucoma | 99.95% | L5 | Only SPARC protein literature, likely a keyword match |
| Nasal cavity disease | 99.88% | L4 | Only indirect NAC data (an old combination-product study) |
| Acute laryngopharyngitis | 99.79% | L5 | No trials or publications |
| Pharyngitis | 99.78% | L4 | Only ex vivo NAC antibiofilm data |
| Exercise-induced malignant hyperthermia | 99.26% | L5 | No established link |
| Angle-closure glaucoma | 99.06% | L5 | Near-duplicate of closed-angle glaucoma; should be merged |

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


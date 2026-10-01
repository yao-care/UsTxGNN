---
layout: default
title: Nepafenac
parent: Model Prediction Only (L5)
nav_order: 961
evidence_level: L5
indication_count: 10
---

# Nepafenac
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

# Nepafenac: From Postoperative Ocular Pain and Inflammation to Eye Disease

## One-Sentence Summary

Nepafenac is a topical NSAID eye drop, marketed in the US as ILEVRO and NEVANAC. The literature describes its approved use as treating pain and inflammation after cataract surgery. The TxGNN model predicts it may be effective for **eye disease**, a very broad label, with **41 clinical trials** and **20 publications** linked to this prediction. Most of that evidence covers uses that overlap with the marketed indication, so this is largely not repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain and inflammation after cataract surgery (from published literature; the US license records contain no indication text) |
| Predicted New Indication | Eye disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 (≥2 completed Phase 3 trials; the Evidence Pack's own scoring lists L2, and the trials below meet the L1 rule) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available in the Evidence Pack. The Pack's rationale and the literature describe nepafenac as a prodrug of **amfenac**, a COX-1/COX-2 inhibitor. After topical dosing it penetrates the cornea and reaches the retina and choroid. There it reduces prostaglandin-mediated inflammation, pain and macular edema.

"Eye disease" is a very broad term. The uses actually supported by the evidence are:
- Postoperative inflammation and pain after cataract surgery
- Prevention of cystoid macular edema, including in diabetic patients
- Exploratory uses, such as macular thickening after laser treatment, diabetic macular edema, and inflammation after laser iridotomy

The first two overlap heavily with the marketed use. The exploratory uses are the genuinely new directions, and they are mostly small studies.

The other predicted indications are much weaker. Most have no trials or literature and look like knowledge-graph artifacts. Examples include hair and skin disorders such as hypotrichosis and seborrheic keratosis.

---

## Clinical Trial Evidence

The Pack lists 41 related trials, of which the 10 most relevant are shown below. The selection favors larger, completed, controlled studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Nepafenac 0.3% for prevention and treatment of inflammation and pain after cataract surgery |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% vs vehicle for clinical outcomes in diabetic patients after cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Companion study of nepafenac 0.3% once daily vs vehicle in diabetic patients after cataract surgery |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Nepafenac 0.3% vs 0.1% vs vehicle for ocular inflammation and pain after cataract surgery |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Clinical equivalence of a generic nepafenac 0.3% vs Ilevro, placebo-controlled |
| [NCT00333255](https://clinicaltrials.gov/study/NCT00333255) | Phase 3 | Completed | 267 | Nevanac 0.1% vs Acular LS for inflammation after cataract surgery |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Phase 3 | Completed | 227 | Nepafenac 0.1% vs ketorolac vs placebo for inflammation and pain after cataract surgery (European study) |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | Completed | 260 | Nepafenac 0.1% vs vehicle after cataract surgery in Chinese subjects |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | Completed | 263 | Nevanac 0.1% vs vehicle for reducing macular edema after cataract surgery in diabetic retinopathy |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | N/A | Completed | 662 | Once-daily nepafenac 0.3% vs placebo added to steroid for prevention of pseudophakic cystoid macular edema |

Other listed trials cover uses beyond routine cataract surgery. Examples include macular thickening after pan-retinal photocoagulation (NCT00801905, terminated) and diabetic macular edema after laser (NCT00900887). Another is macular edema in diabetic patients after cataract surgery (NCT00939276, Phase 3, terminated). Two more are vitreous biomarkers in retinal detachment (NCT07162818) and epiphora with punctal stenosis (NCT07372014, ongoing).

---

## Literature Evidence

The Pack lists 20 publications, of which 10 are shown. Comparative and randomized studies come first, then reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24345529](https://pubmed.ncbi.nlm.nih.gov/24345529/) | 2014 | Phase 3 study | J Cataract Refract Surg | Evaluated once-daily nepafenac 0.3% to prevent and treat pain and inflammation after cataract surgery |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | Randomized trial | Ophthalmol Glaucoma | Compared 0.1% nepafenac with 1% prednisolone acetate for inflammation after laser peripheral iridotomy |
| [22795976](https://pubmed.ncbi.nlm.nih.gov/22795976/) | 2012 | Comparative trial vs placebo | J Cataract Refract Surg | Compared prophylactic ketorolac vs nepafenac vs placebo on macular volume after uneventful phacoemulsification |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | Comparative study | Korean J Ophthalmol | Compared 0.1% nepafenac with 1% prednisolone for postoperative inflammation control after micro-incisional cataract surgery |
| [30284393](https://pubmed.ncbi.nlm.nih.gov/30284393/) | 2018 | Comparative study | Acta Ophthalmol | Compared efficacy and tolerability of nepafenac vs preservative-free diclofenac after cataract surgery |
| [30046541](https://pubmed.ncbi.nlm.nih.gov/30046541/) | 2018 | Comparative study | Int J Ophthalmol | Compared bromfenac, nepafenac and diclofenac for prevention of cystoid macular edema after phacoemulsification |
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Systematic review and meta-analysis | Eur J Ophthalmol | Pooled randomized trials on nepafenac's effect on foveal thickness, macular volume and visual acuity after cataract surgery when added to topical steroids |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Reviews nepafenac in cataract surgery, noting high ocular penetration and a low side-effect profile for topical NSAIDs |
| [19040348](https://pubmed.ncbi.nlm.nih.gov/19040348/) | 2008 | Dosing study | J Ocul Pharmacol Ther | Compared once-, twice- and three-times-daily 0.1% nepafenac for pain and inflammation after cataract surgery |
| [24345317](https://pubmed.ncbi.nlm.nih.gov/24345317/) | 2014 | Randomized prospective study | Am J Ophthalmol | Reported the effect of nepafenac 0.1% eye drops on intraocular pressure in eyes with cataract |

The Pack also includes preclinical work in rat models on diabetic retinopathy, retinal angiogenesis and ocular inflammation (PMIDs 17259381, 19897019, 24697218). These support a possible role in retinal disease but are not clinical evidence.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203491 | ILEVRO (Harrow Eye, LLC) | Suspension/drops | Pain and inflammation associated with cataract surgery (per literature; no text in license record) |
| NDA021862 | NEVANAC (Harrow Eye, LLC) | Suspension/drops | Pain and inflammation associated with cataract surgery (per literature; no text in license record) |

---

## Safety Considerations

Please refer to the package insert for safety information. Warnings and contraindications are not available in the Evidence Pack, and no drug-drug interaction records were found.

The linked literature includes some ocular safety signals worth checking against the label:
- **Intraocular pressure:** studies on IOP effects (PMIDs 24345317 and 25493620) and a case report of extreme IOP (PMID 36573765).
- **Corneal surface:** topical NSAIDs, including nepafenac, have been associated with corneal epithelial toxicity. This matters for eyes with a compromised ocular surface.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several large completed Phase 3 trials, and a 2025 meta-analysis, support nepafenac for postoperative inflammation, pain and macular edema prevention. This use is already marketed in the US, so the "eye disease" prediction is largely confirmatory. Genuinely new uses, such as diabetic macular edema, retinal detachment and iridotomy inflammation, rest on small, terminated or biomarker-only studies. The remaining predictions (ranks 2–9) are unsupported and should stay on Hold. Rank 10, vitreous detachment, is only a research question.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- A narrower target than "eye disease", such as diabetic macular edema, with randomized trials that use clinical endpoints
- Review of corneal and intraocular-pressure safety in patients with a compromised ocular surface or glaucoma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Nepafenac
parent: High Evidence (L1-L2)
nav_order: 961
evidence_level: L1
indication_count: 10
monitor_inn: "NEPAFENAC"
predicted_indications: ["eye disease", "optic papillitis", "hypotrichosis simplex of the scalp", "seborrheic keratosis", "von Hippel anomaly", "congenital hypotrichosis milia", "mcpherson robertson cammarano syndrome", "lagophthalmos", "vulvar inverted follicular keratosis", "vitreous detachment"]
last_modified_at: 2026-10-14
description: "Nepafenac: predicted new indication Eye disease (evidence level L1). Approved use: Not recorded in the local data"
---

# Nepafenac
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

## Nepafenac: Eye disease
{: .text-alpha }

## One-Sentence Summary

Nepafenac is a topical ophthalmic NSAID (eye-drop suspension) marketed in the US as Nevanac and Ilevro.
The TxGNN model predicts it may be effective for **eye disease** (a broad category), with **40 clinical trials** and **20 publications** currently supporting this direction.
Most of this evidence concerns uses that nepafenac is already established for, such as inflammation and macular edema after cataract surgery, so this is largely confirmation of an existing use rather than a novel repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Eye disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L1 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From the literature, nepafenac is a prodrug. Ocular tissue enzymes convert it to amfenac, a COX-1 and COX-2 inhibitor. Blocking COX reduces prostaglandin synthesis, which lowers ocular inflammation, pain, and breakdown of the blood-retinal barrier.

The original use, controlling inflammation and pain after cataract surgery, is directly tied to this mechanism. The same pathway plausibly applies to related eye conditions such as pseudophakic cystoid macular edema, diabetic macular edema, and post-surgical retinal inflammation. Preclinical work also shows that topical nepafenac reaches the retina and inhibits retinal edema and ocular neovascularization in animal models.

"Eye disease" is a very broad label. The prediction should be read as support for inflammation-driven ocular conditions, not for every eye disorder. The other lower-ranked predictions were also reviewed:

- **Optic papillitis** (score 0.9984): the evidence is indirect, with one rabbit study and one post-cataract trial. Evidence level L4, Hold.
- **Vitreous detachment** (score 0.9981): one biomarker trial in retinal detachment. Evidence level L4, treated as a research question.
- **Hair, skin and rare syndrome predictions** (for example hypotrichosis, seborrheic keratosis): no plausible mechanism and no trials or literature. These look like TxGNN model (deep learning) artifacts, and the evidence level is L5 (model prediction only).

## Clinical Trial Evidence

The predicted indication has 40 registered trials. The 10 most relevant are listed below, prioritizing larger or higher-phase studies with direct nepafenac data.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Nepafenac 0.3% for prevention and treatment of inflammation and pain after cataract surgery |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% once daily vs vehicle in diabetic patients after cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Same design as above, a companion study in diabetic patients after cataract surgery |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Nepafenac 0.3% vs 0.1% vs vehicle for inflammation and pain after cataract surgery |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Clinical equivalence of a nepafenac 0.3% generic vs Ilevro, with a placebo arm |
| [NCT00333255](https://clinicaltrials.gov/study/NCT00333255) | Phase 3 | Completed | 267 | Nevanac 0.1% vs Acular LS (ketorolac) before and after cataract surgery |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | Completed | 263 | Nevanac 0.1% vs vehicle to reduce macular edema after cataract surgery in diabetic retinopathy |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | Completed | 260 | Nepafenac 0.1% vs vehicle for inflammation and pain after cataract surgery in Chinese adults |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | N/A | Completed | 662 | Once-daily nepafenac 0.3% vs placebo added to steroid for preventing pseudophakic cystoid macular edema |
| [NCT01021761](https://clinicaltrials.gov/study/NCT01021761) | Phase 4 | Completed | 126 | PGE2 inhibition of Acuvail, Xibrom and Nevanac in cataract surgery, direct pharmacodynamic evidence of COX inhibition |

Other registered trials cover diabetic macular edema, epiretinal membrane surgery, retinal detachment, and head-to-head comparisons with ketorolac, bromfenac and diclofenac. One trial (NCT00939276) was terminated early.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | Systematic review / network meta-analysis | Eye (London) | Compared topical NSAIDs, with or without steroids, for macular thickening and visual outcome after phacoemulsification |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | Cochrane systematic review | Cochrane Database Syst Rev | Topical NSAIDs for diabetic cystoid macular edema |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Nepafenac has high ocular penetration and a low side-effect profile; reduces inflammation, pain and macular edema risk in cataract surgery |
| [26502088](https://pubmed.ncbi.nlm.nih.gov/26502088/) | 2016 | Review | Dev Ophthalmol | NSAIDs in retinal diseases through COX inhibition |
| [17720068](https://pubmed.ncbi.nlm.nih.gov/17720068/) | 2007 | Cohort | J Cataract Refract Surg | Incidence of visually significant pseudophakic macular edema in patients treated with prednisolone plus nepafenac |
| [26703278](https://pubmed.ncbi.nlm.nih.gov/26703278/) | 2015 | Comparative clinical study | J Cataract Refract Surg | Ketorolac, nepafenac and bromfenac compared on post-operative inflammation using laser flare photometry |
| [40243047](https://pubmed.ncbi.nlm.nih.gov/40243047/) | 2025 | Clinical study | Indian J Ophthalmol | Nepafenac 0.1% vs 0.3% on aqueous flare and macular thickness in pseudoexfoliation after cataract surgery |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | Randomized trial | Ophthalmol Glaucoma | Nepafenac 0.1% vs prednisolone acetate 1% after laser peripheral iridotomy |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | Preclinical PK study | Exp Eye Res | Topical nepafenac and amfenac reach the posterior segment of the eye |
| [17964407](https://pubmed.ncbi.nlm.nih.gov/17964407/) | 2007 | Case report | J Cataract Refract Surg | Corneal melt with nepafenac in a patient with systemic graft-versus-host disease (a safety signal) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203491 | ILEVRO (Harrow Eye, LLC) | Suspension/drops | Not listed; status: valid |
| NDA021862 | NEVANAC (Harrow Eye, LLC) | Suspension/drops | Not listed; status: valid |


## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not from label text): rheumatoid arthritis, diabetes mellitus, diabetic ketoacidosis, blood coagulation disease, keratitis, keratoconjunctivitis, dry eye syndrome, xerophthalmia, and corneal ulcer.
- **Published case report**: corneal melt and perforation after cataract surgery in a patient with systemic graft-versus-host disease (PMID 17964407). This is consistent with the known corneal risk of topical NSAIDs in predisposed patients, particularly those with ocular surface disease.

Please refer to the package insert for the full warnings, contraindications and drug interaction information, because label data was not available when this report was compiled.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several large Phase 3 trials (for example NCT01109173, NCT01853072 and NCT01872611) and a systematic review support nepafenac for inflammation and macular edema after cataract surgery, giving Evidence Level L1. However, "eye disease" is a broad prediction, and the evidence mostly confirms an existing use rather than a new one. The US licenses are currently cancelled, and label safety data was not available.

**To proceed, the following is needed:**
- Retrieve and review the FDA package insert for warnings, contraindications and approved indications (a blocking gap for safety screening)
- Confirm detailed mechanism of action data from DrugBank
- Narrow the target to specific conditions, such as pseudophakic or diabetic macular edema, rather than the broad "eye disease" label
- Clarify the commercial and regulatory status given that both US NDAs are cancelled
- Define corneal safety guardrails for patients with ocular surface disease, diabetes, or autoimmune conditions
- Treat the optic papillitis and vitreous detachment predictions as research questions only. Do not pursue the dermatologic and rare-syndrome predictions without a new mechanistic rationale.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


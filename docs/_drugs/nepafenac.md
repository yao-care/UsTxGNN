---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 960
evidence_level: L5
indication_count: 10
---

# Nepafenac
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nepafenac: From Postoperative Ocular Inflammation to Eye Disease

## One-Sentence Summary

> Nepafenac is a topical ophthalmic NSAID prodrug whose established use is controlling inflammation and pain after cataract surgery (and preventing cystoid macular edema). The TxGNN model's top prediction is the broad category **"Eye Disease,"** supported by **41 clinical trials** and **20 publications** — but as detailed below, this evidence largely reflects the drug's *already-approved* use rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postoperative ocular inflammation and pain (cataract surgery), including CME prevention — inferred from trial evidence; official license text unavailable (data gap) |
| Predicted New Indication | Eye Disease (broad grouping) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| US Market Status | Not Marketed (per this evidence pack) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nepafenac is a prodrug that, following topical ocular administration, is hydrolyzed intraocularly to its active metabolite **amfenac**, a non-selective COX-1/COX-2 inhibitor. This mechanism underlies its established anti-inflammatory and analgesic effect in the eye, particularly for controlling inflammation and pain after cataract surgery and reducing the risk of postoperative cystoid macular edema (CME).

The TxGNN model's top-ranked prediction, "eye disease," is mechanistically coherent — but the evidence pack itself flags an important caveat: this is a very broad disease grouping, and essentially all of the supporting clinical trials and literature relate to nepafenac's **existing, already-approved indication** (postoperative ophthalmic inflammation/pain and CME prophylaxis), not a novel disease target. In other words, the model has high confidence largely because it is re-confirming known pharmacology rather than surfacing a new repurposing opportunity.

That said, within this broad "eye disease" evidence set are pockets of more exploratory signal — e.g., use in vitreoretinal inflammation following retinal detachment repair, uveitis-associated macular edema, and diabetic macular edema — that could warrant closer, disease-specific evaluation separate from the general "eye disease" label. Two related, disease-specific candidates from this run (optic papillitis, vitreous detachment) each returned only sparse or preclinical evidence and are scored as Hold/Research Question, underscoring that the strength here sits with the known indication, not adjacent ones.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Large dose-comparison trial: nepafenac 0.3% vs 0.1% vs vehicle for prevention/treatment of ocular inflammation and pain after cataract surgery |
| [NCT02084576](https://clinicaltrials.gov/study/NCT02084576) | Phase 4 | Completed | 40 | Prospective randomized double-masked comparison of ketorolac 0.4% vs nepafenac 0.1% for prevention of cystoid macular edema after phacoemulsification |
| [NCT00818844](https://clinicaltrials.gov/study/NCT00818844) | Phase 4 | Completed | 40 | Topical nepafenac 0.1% vs placebo for reducing macular volume after epiretinal membrane surgery |
| [NCT07162818](https://clinicaltrials.gov/study/NCT07162818) | Phase 4 | Completed | 61 | Effects of nepafenac 0.1% on vitreous inflammatory biomarkers in rhegmatogenous retinal detachment and proliferative vitreoretinopathy |
| [NCT00347204](https://clinicaltrials.gov/study/NCT00347204) | Phase 4 | Completed | 40 | Double-masked comparison of Acular LS vs Nevanac (nepafenac) for postoperative pain control after PRK |
| [NCT00348582](https://clinicaltrials.gov/study/NCT00348582) | Phase 4 | Completed | N/A | Acular LS vs Nevanac for postoperative inflammation following cataract surgery |
| [NCT01475877](https://clinicaltrials.gov/study/NCT01475877) | N/A | Completed | 20 | Bromfenac 0.09% QD vs Nevanac (nepafenac) 0.1% TID for pain control and epithelial healing after PRK |
| [NCT00865540](https://clinicaltrials.gov/study/NCT00865540) | Phase 4 | Unknown | 30 | Comparison of prednisolone acetate 1%, nepafenac 0.1%, and ketorolac 0.4% for maintaining intraoperative mydriasis during phacoemulsification |
| [NCT01939691](https://clinicaltrials.gov/study/NCT01939691) | Phase 4 | Terminated | 9 | Nepafenac vs difluprednate regimens for uveitis-associated macular edema |
| [NCT05847049](https://clinicaltrials.gov/study/NCT05847049) | N/A | Completed | 16 | Combined eplerenone, intravitreal aflibercept, and topical nepafenac for serous foveal detachment in central serous chorioretinopathy |

*41 clinical trials were identified in total against the "eye disease" query; the trials above are the 10 rated most relevant.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology. Glaucoma | Nepafenac 0.1% vs prednisolone acetate 1% for controlling inflammation after laser peripheral iridotomy |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Review | Drugs | Review of diagnostic agents and therapeutic medications for non-infectious corneal injury |
| [16466612](https://pubmed.ncbi.nlm.nih.gov/16466612/) | 2006 | Review | Curr Med Res Opin | Ocular permeation and inhibition of retinal inflammation — clinical utility of nepafenac |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | Cohort | Korean J Ophthalmol | Nepafenac 0.1% vs prednisolone acetate 1% in postoperative management after micro-incisional cataract surgery |
| [29199864](https://pubmed.ncbi.nlm.nih.gov/29199864/) | 2018 | Cohort | Curr Eye Res | Intracameral nepafenac safety and efficacy in inhibiting prostaglandin synthesis during phacoemulsification |
| [30284393](https://pubmed.ncbi.nlm.nih.gov/30284393/) | 2018 | Cohort | Acta Ophthalmol | Nepafenac vs preservative-free diclofenac in postoperative management after cataract surgery |
| [25493620](https://pubmed.ncbi.nlm.nih.gov/25493620/) | 2016 | Cohort | J Glaucoma | Interaction of nepafenac and prostaglandin analogs in primary open-angle glaucoma patients |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | PK/Preclinical | Exp Eye Res | Distribution of topical nepafenac and active metabolite amfenac to the posterior segment of the eye |
| [19897019](https://pubmed.ncbi.nlm.nih.gov/19897019/) | 2010 | Preclinical | Brain Res Bull | Effects of nepafenac and amfenac on retinal angiogenesis |
| [24697218](https://pubmed.ncbi.nlm.nih.gov/24697218/) | 2014 | Preclinical | J Pharm Pharmacol | Effects of topical indomethacin, bromfenac and nepafenac on LPS-induced ocular inflammation |

*20 publications were identified in total against the "eye disease" query; the 10 above are prioritized by evidence tier (RCT > Review > Cohort > Preclinical).*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1) with numerous completed Phase 2/3 RCTs, but this evidence chiefly validates nepafenac's known approved use rather than a distinct new indication — "eye disease" is too broad a category to treat as a novel repurposing signal. Before any regulatory or clinical action, the blocking safety data gap must be resolved.

**To proceed, the following is needed:**
- TFDA/FDA package insert data — warnings, precautions, and contraindications (currently missing; flagged as a **Blocking** data gap that prevents entry into the S1 safety review stage)
- Confirmed mechanism-of-action documentation at the drug record level (currently a data gap; this report's MOA discussion was reconstructed from trial/literature evidence, not a verified source record)
- Re-scoping of the "eye disease" prediction into disease-specific sub-indications (e.g., uveitic macular edema, post-vitrectomy inflammation) to distinguish genuinely novel signal from confirmation of existing use
- Verified US/Taiwan market authorization records, since this evidence pack shows zero licenses on file despite nepafenac's known marketed ophthalmic products (Nevanac, Ilevro) — this is likely a data completeness gap that should be corrected before final decisioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


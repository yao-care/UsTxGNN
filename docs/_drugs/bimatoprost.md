---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma to Alopecia

## One-Sentence Summary

Bimatoprost (Lumigan®/Latisse®) is a synthetic prostamide F2α analog whose FDA-approved indications—glaucoma and eyelash hypotrichosis—led to active investigation in hair-loss disorders after clinicians observed hypertrichosis as a side effect in glaucoma patients. The TxGNN model predicts efficacy across multiple alopecia-related conditions; the strongest evidence cluster centers on **alopecia**, supported by **10 registered clinical trials** (including 4 completed Phase 2 RCTs enrolling over 850 participants) and **20 publications**. Of 10 total predicted indications, 2 reach actionable evidence levels (L2–L4), while the remainder are hypothesis-only (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma / Eyelash hypotrichosis (FDA-approved; no licenses found in database search) |
| Predicted New Indication | Alopecia (androgenetic alopecia, alopecia areata) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | Not found in database (known FDA approvals: Lumigan® 2001, Latisse® 2008) |
| Number of NDAs | 0 (database search returned no results — likely a data gap) |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query in this evidence pack (flagged as data gap DG002). However, based on clinical trial descriptions and published literature, bimatoprost is a synthetic prostamide F2α analog that acts as an FP prostanoid receptor agonist. Its primary approved use — lowering intraocular pressure in glaucoma — operates by increasing aqueous humor outflow via FP receptor activation. The hair-growth application arose serendipitously: ophthalmologists noticed that patients using prostaglandin analog eyedrops for glaucoma developed longer, darker, and thicker eyelashes (hypertrichosis) as a local side effect, prompting formal investigation into hair follicle biology.

The mechanistic bridge from glaucoma to alopecia is anchored in FP prostanoid receptor expression in hair follicles. Bimatoprost promotes hair growth through at least three pathways: ① prolonging the anagen (active growth) phase of the hair cycle; ② facilitating follicle transition from telogen (resting) back to anagen; and ③ potentially increasing follicular density and hair shaft diameter. A landmark 2013 translational study (PMID 23104985) directly confirmed that scalp hair follicles express FP receptors and respond to prostamide signaling — mechanistically connecting the glaucoma drug to scalp alopecia. The FDA's subsequent approval of Latisse® for eyelash hypotrichosis provides regulatory validation of this exact pathway, and creates a strong precedent for the broader scalp application.

Androgenetic alopecia (AGA) differs biologically from glaucoma, yet the prostamide/FP pathway operates independently of the androgen-driven miniaturization process in AGA — meaning bimatoprost could serve as an adjunct or alternative rather than a substitute for androgen-targeting therapies. This mechanistic independence is a key advantage worth exploring in combination regimens.

---

## Clinical Trial Evidence

The following trials relate to the **alopecia** predicted indication (rank 8 by TxGNN score; highest evidence level among all 10 predictions):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | Double-blind RCT evaluating bimatoprost (3 doses) vs. vehicle and minoxidil 5% in men with androgenetic alopecia — the largest and most directly relevant trial |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | Double-blind RCT evaluating bimatoprost (3 doses) vs. vehicle and minoxidil 2% in women with female pattern hair loss — paired with NCT01325337 for gender-complete evidence |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Safety and efficacy study of bimatoprost in male subjects with androgenetic alopecia |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Mechanistic validation study: effect of bimatoprost on scalp hair growth in androgen-dependent follicles; confirmed FP receptor activity in scalp |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | Combined CO2 fractional laser + bimatoprost 0.03% for alopecia areata (2019–2021); published results in 2025 (PMID 40252129) showing superior regrowth vs. laser alone |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Bimatoprost 0.03% for eyelash loss or hypotrichosis in children — extends safety/efficacy evidence to pediatric populations and the eyelash indication |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Completed | 42 | Safety, tolerability, and pharmacokinetics of a new bimatoprost formulation in patients with alopecia; supports novel formulation development |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Completed | 11 | Local scalp pharmacokinetics and tolerability following 14 days of once-daily topical application in men with AGA; confirms feasibility of scalp delivery |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | Terminated | 53 | Dose escalation study of safety, tolerability, and PK in male AGA patients; terminated March 2017 — reason not publicly reported, warrants clarification |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | N/A | Completed | 14 | Latanoprost vs. bimatoprost for eyelash growth in alopecia areata; small pilot study providing indirect efficacy comparison |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | Systematic Review | J Dermatol Treatment | Network meta-analysis of non-surgical AGA monotherapies in men and women; bimatoprost included as an investigational comparator with evidence quality assessment |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | Clinical Guideline | J Dermatology | Japanese 2017 guidelines for male- and female-pattern hair loss; provides evidence-based context for prostaglandin analogs relative to established therapies |
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | RCT/Prospective | Arch Dermatol Res | CO2 fractional laser combined with bimatoprost 0.03% demonstrated superior hair regrowth vs. laser alone in alopecia areata; supports combination strategy |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Prospective Study | Dermatol Therapy | Open-label prospective study of topical bimatoprost for eyelash loss in alopecia totalis and universalis; 16 of 18 subjects showed measurable eyelash regrowth over mean 30.6-week treatment |
| [23104985](https://pubmed.ncbi.nlm.nih.gov/23104985/) | 2013 | Mechanistic/Translational | FASEB J | Landmark study confirming FP receptor expression in human scalp hair follicles; prostamide pathway proposed as a novel therapeutic route for scalp alopecias — the mechanistic foundation for this repurposing |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Review | Expert Opin Investig Drugs | Comprehensive review of bimatoprost for eyelash, eyebrow, and scalp alopecia; summarizes the full investigational trial landscape and mechanism of action |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | Clinical Trial (non-RCT) | Indian Dermatol Online J | Prospective non-randomized comparison of bimatoprost vs. clobetasol propionate in scalp alopecia areata; bimatoprost shown as an emerging treatment modality |
| [33631058](https://pubmed.ncbi.nlm.nih.gov/33631058/) | 2021 | Systematic Review/NMA | Dermatol Therapy | Systematic review and network meta-analysis of alopecia areata treatments; contextualizes bimatoprost within the broader AA treatment landscape |
| [29854658](https://pubmed.ncbi.nlm.nih.gov/29854658/) | 2018 | Review | Indian Dermatol Online J | Overview of bimatoprost in dermatology: traces the discovery pathway from glaucoma side effect to applications in alopecia, vitiligo, and hyperpigmentation |
| [35040730](https://pubmed.ncbi.nlm.nih.gov/35040730/) | 2022 | Formulation/Preclinical | Drug Delivery | Novel topical bimatoprost formulation with 4.6× higher human skin flux and demonstrated in vivo hair regrowth efficacy in androgenic alopecia; supports formulation development pathway |

---

## US Market Information

No NDA records were returned in the database search for bimatoprost. This likely represents a data gap in the search rather than true non-approval status. Based on information referenced across the retrieved clinical trials, the following US approvals are publicly documented:

| Authorization | Product Name | Dosage Form | Approved Indication |
|--------------|-------------|-------------|-------------------|
| NDA (not retrieved) | Lumigan® | Ophthalmic solution 0.01%/0.03% | Reduction of elevated intraocular pressure in patients with open-angle glaucoma or ocular hypertension |
| NDA (not retrieved) | Latisse® | Ophthalmic solution 0.03% | Hypotrichosis of the eyelashes (inadequate or not enough eyelashes) |

> These approvals should be verified directly via the FDA's Drugs@FDA database before any regulatory filing.

---

## Safety Considerations

Please refer to the package insert for safety information. No DDI records, key warnings, or contraindication data were retrieved in this evidence pack (data gaps DG001 and DG002).

Based on the known drug class (prostaglandin analog / prostamide), clinically relevant class effects to be aware of include periorbital skin and iris pigmentation changes, conjunctival hyperemia, and paradoxical hypertrichosis at application sites. For scalp formulations, systemic absorption data from NCT02848300 and NCT01189279 should be reviewed during safety evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 RCTs (>850 participants across both sexes) and FDA approval of Latisse® for eyelash hypotrichosis collectively validate the prostamide/FP receptor pathway for hair promotion; however, the AGA Phase 2 trials did not advance to Phase 3, suggesting scalp efficacy may not be superior to established treatments such as minoxidil and finasteride — a key constraint that guardrails should address before committing further resources.

**To proceed, the following is needed:**

- Full efficacy results from NCT01325337 and NCT01325350 (Phase 2 RCTs vs. minoxidil comparator): were the bimatoprost arms statistically superior to vehicle, and how did they compare to minoxidil?
- Clarification of the termination reason for NCT02676310 (Phase 1 dose escalation) — safety signal vs. commercial decision
- MOA documentation from DrugBank API (data gap DG002) to complete mechanistic analysis
- Package insert safety review for warnings and contraindications (data gap DG001, currently blocking S1 safety evaluation)
- Head-to-head comparison positioning vs. JAK inhibitors (baricitinib, ritlecitinib — newly approved for AA), particularly for the alopecia areata subpopulation
- Dedicated pilot trials for hypotrichosis simplex of the scalp (rank 5) and diffuse alopecia areata (rank 7), where the eyelash approval precedent provides strong biological rationale but no scalp-specific data exists
- Formulation strategy decision: existing 0.03% ophthalmic solution vs. novel penetration-enhanced scalp formulation (see PMID 35040730, PMID 38577618)

---

### Reference: All 10 TxGNN-Predicted Indications

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Note |
|------|-----------|-------------|---------------|---------|------|
| 1 | Malformation syndrome with odontal/periodontal component | 99.99% | L5 | Hold | 20 periodontitis background papers retrieved; none involve bimatoprost — prostanoid mechanism link is speculative and indirect |
| 2 | Dandy-Walker malformation syndrome | 99.99% | L5 | Hold | Structural CNS malformation; FP agonism mechanistically irrelevant |
| 3 | Isolated genetic hair shaft abnormality | 99.99% | L5 | Hold | Structural keratin gene defect; no known FP receptor repair mechanism |
| 4 | Ambras hypertrichosis universalis congenita | 99.99% | L5 | Hold | ⚠️ **Direction reversal**: bimatoprost promotes hair growth; this condition features pathological excessive hair — likely model false positive |
| 5 | Hypotrichosis simplex of the scalp | 99.99% | L5 | Research Question | Biologically plausible (direct extension of eyelash approval); no dedicated trials yet; warrants pilot study |
| 6 | Congenital hypotrichosis milia | 99.95% | L5 | Hold | Mixed phenotype; milia (epidermal cysts) component unrelated to prostamide pathway |
| 7 | Diffuse alopecia areata | 99.99% | L4 | Research Question | Indirect support from NCT05600673 and PMID 35278027 (AT/AU); needs dedicated prospective trial |
| **8** | **Alopecia** | **99.99%** | **L2** | **Proceed with Guardrails** | Strongest evidence cluster; multiple Phase 2 RCTs completed; primary actionable target |
| 9 | Genetic alopecia | 99.97% | L4 | Research Question | Mechanistic paper (PMID 23104985) and pediatric case report (PMID 27377163); no dedicated scalp trial |
| 10 | Pulmonary arteriovenous malformation | 99.95% | L5 | Hold | Structural vascular malformation; FP pathway mechanistically irrelevant; likely knowledge-graph artifact |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


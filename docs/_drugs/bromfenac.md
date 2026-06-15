---
layout: default
title: Bromfenac
parent: 僅模型預測 (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
---

# Bromfenac
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

# Bromfenac: From Systemic NSAID to Eye Disease

## One-Sentence Summary

Bromfenac is a dual COX-1/COX-2 inhibitor originally developed as a systemic non-steroidal anti-inflammatory drug (NSAID) for pain and inflammation management, before being reformulated as a topical ophthalmic solution.
The TxGNN model predicts it may be effective for **Eye Disease** — spanning post-cataract surgery inflammation, cystoid macular edema, dry eye, and VEGF-driven maculopathies —
with **multiple completed Phase 3 RCTs** and **20 publications** providing robust support for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic pain and inflammation (oral NSAID class; reformulated as topical ophthalmic solution for ocular use) |
| Predicted New Indication | Eye Disease (post-surgical ocular inflammation, macular edema, dry eye, VEGF-driven retinal conditions) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| US Market Status | Not found in regulatory query (data gap; clinical trial evidence documents FDA-approved ophthalmic formulations Xibrom / Bromday / Prolensa) |
| Number of NDAs | 0 (per regulatory query) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bromfenac is a potent dual COX-1/COX-2 inhibitor that blocks prostaglandin synthesis, particularly prostaglandin E2 (PGE2) — the primary mediator of ocular inflammation, surgical-induced miosis, and macular edema. Its topical ophthalmic formulation is designed to achieve high local concentrations in both the anterior and posterior segments of the eye while minimizing systemic absorption. This is clinically critical: oral bromfenac (Duract) was voluntarily withdrawn from the US market in 1998 due to severe hepatotoxicity, but the ophthalmic formulation bypasses this risk entirely through its negligible systemic exposure.

The mechanistic link between bromfenac and eye disease is direct. Post-cataract surgery trauma triggers a prostaglandin cascade that, if unchecked, leads to cystoid macular edema (CME) — a leading cause of suboptimal visual outcomes after otherwise successful surgery. By locally inhibiting COX enzymes at the ocular surface, topical bromfenac interrupts this cascade at its source. Multiple Phase 3 RCTs have confirmed this mechanism in clinical practice, with bromfenac consistently outperforming placebo and demonstrating non-inferiority or superiority to comparator NSAIDs in controlling post-operative inflammation and preventing macular thickening.

Beyond its core post-surgical indication, the evidence base has broadened considerably. A 2024 meta-analysis (PMID 39180057) demonstrates that topical bromfenac can reduce intravitreal anti-VEGF injection burden in neovascular AMD, diabetic macular edema, and retinal vein occlusions — suggesting anti-inflammatory COX inhibition complements VEGF-targeted therapy. In vitro work (PMID 30908581) further shows bromfenac inhibits TGF-β1-driven fibrosis in pterygium and conjunctival fibroblasts, supporting application in degenerative conjunctival conditions. The convergence of multiple mechanistic pathways and a deep clinical evidence base explains the TxGNN model's high confidence score of 99.80%.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01774474](https://clinicaltrials.gov/study/NCT01774474) | Phase 3 | Completed | 1,127 | Large RCT evaluating bromfenac for prevention of cystoid macular edema after cataract surgery in both diabetic and non-diabetic patients; highest-powered direct evidence for this indication |
| [NCT00198445](https://clinicaltrials.gov/study/NCT00198445) | Phase 3 | Completed | 527 | Pivotal placebo-controlled RCT of bromfenac sodium 0.09% for post-cataract ocular inflammation; served as a key FDA approval-supporting study |
| [NCT01367249](https://clinicaltrials.gov/study/NCT01367249) | Phase 3 | Completed | 440 | Efficacy and safety of bromfenac ophthalmic solution vs. placebo for ocular inflammation and pain associated with cataract surgery |
| [NCT01212471](https://clinicaltrials.gov/study/NCT01212471) | Phase 3 | Completed | 840 | Dose-ranging study evaluating bromfenac ophthalmic solution for dry eye disease; largest trial exploring this non-surgical indication |
| [NCT00704418](https://clinicaltrials.gov/study/NCT00704418) | Phase 3 | Completed | 156 | Phase 3 RCT assessing efficacy and safety of bromfenac ophthalmic solution in routine cataract surgery |
| [NCT00469781](https://clinicaltrials.gov/study/NCT00469781) | Phase 4 | Completed | 95 | Compared twice-daily vs. four-times-daily prednisolone combined with bromfenac BID for prevention of retinal thickening and CME; provides regimen optimization data |
| [NCT00698724](https://clinicaltrials.gov/study/NCT00698724) | Phase 4 | Completed | 200 | Bromfenac monotherapy vs. bromfenac plus prednisolone acetate; used OCT and visual acuity as primary endpoints after cataract surgery |
| [NCT02137161](https://clinicaltrials.gov/study/NCT02137161) | Phase 4 | Completed | 62 | REPEX Study: randomized trial of bromfenac 0.09% in patients with pseudoexfoliation syndrome undergoing cataract surgery, extending evidence to a high-risk subgroup |
| [NCT01475877](https://clinicaltrials.gov/study/NCT01475877) | N/A | Completed | 20 | Head-to-head comparison of Bromday (bromfenac 0.09% QD) vs. Nevanac (nepafenac 0.1% TID) for pain control and epithelial healing after photorefractive keratectomy (PRK) |
| [NCT03578276](https://clinicaltrials.gov/study/NCT03578276) | Phase 4 | Completed | 35 | Evaluated a compounded Lessdrops™ formulation (antibiotic + bromfenac + steroid) vs. standard three-drop regimen following phacoemulsification; proof-of-concept for simplified dosing |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39180057](https://pubmed.ncbi.nlm.nih.gov/39180057/) | 2024 | Meta-analysis | BMC Ophthalmology | Systematic review and meta-analysis showing topical bromfenac reduces treatment burden and improves outcomes as adjunct to anti-VEGF therapy in neovascular AMD, diabetic macular edema, and retinal vein occlusions |
| [39025658](https://pubmed.ncbi.nlm.nih.gov/39025658/) | 2024 | Systematic Review / Network Meta-analysis | J Cataract Refract Surg | Network meta-analysis of topical NSAIDs for pain management after PRK; provides comparative effectiveness data positioning bromfenac against other agents in refractive surgery |
| [31343372](https://pubmed.ncbi.nlm.nih.gov/31343372/) | 2019 | RCT | Expert Opin Pharmacother | Efficacy and safety of bromfenac 0.075% in DuraSite® vehicle for cataract surgery; notes slightly superior posterior segment bioavailability vs. comparable topical NSAIDs |
| [30046541](https://pubmed.ncbi.nlm.nih.gov/30046541/) | 2018 | RCT | Int J Ophthalmology | Three-arm head-to-head RCT comparing bromfenac 0.09%, nepafenac 0.1%, and diclofenac 0.1% for CME prophylaxis after phacoemulsification |
| [30009640](https://pubmed.ncbi.nlm.nih.gov/30009640/) | 2018 | RCT | Current Eye Research | Direct comparison of bromfenac 0.09% and diclofenac 0.1% as adjunctive therapy after cataract surgery; assessed efficacy and tolerability with laser flare photometry |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Review | Drugs | Comprehensive review of pharmacological treatment for non-infectious corneal injury, including the role of topical NSAIDs such as bromfenac in the therapeutic landscape |
| [19735215](https://pubmed.ncbi.nlm.nih.gov/19735215/) | 2009 | Review | Expert Opin Pharmacother | Overview of the ophthalmic utility of twice-daily topical bromfenac; describes COX inhibition mechanism and clinical applications for post-cataract inflammation and pain |
| [26068607](https://pubmed.ncbi.nlm.nih.gov/26068607/) | 2015 | Prospective Study | Asia-Pac J Ophthalmol | Prospective evaluation of bromfenac sodium ophthalmic solution in dry eye patients with inadequate response to artificial tear monotherapy; supports use beyond surgical contexts |
| [30908581](https://pubmed.ncbi.nlm.nih.gov/30908581/) | 2019 | In vitro Study | Invest Ophthalmol Vis Sci | Bromfenac inhibits TGF-β1-induced fibrotic signaling in human pterygium and conjunctival fibroblasts; provides mechanistic rationale for anti-fibrotic applications in conjunctival degeneration |
| [17445902](https://pubmed.ncbi.nlm.nih.gov/17445902/) | 2007 | Clinical Study | Ophthalmology | Multi-center evaluation of bromfenac ophthalmic solution 0.09% (Xibrom) for post-cataract inflammation and pain; foundational clinical publication supporting FDA approval of the ophthalmic formulation |

---

## US Market Information

No FDA license records were returned by the regulatory database query for bromfenac (market status: not found; 0 registered NDAs). This appears to represent a data gap in the regulatory query pipeline rather than true absence of approval.

Based on clinical trial documentation and peer-reviewed literature, the following ophthalmic formulations have been FDA-approved:

| Formulation | Brand Name | Dosing | Approved Indication |
|-------------|-----------|--------|-------------------|
| Bromfenac 0.09% ophthalmic solution | Xibrom | BID | Ocular inflammation and pain following cataract surgery |
| Bromfenac 0.09% ophthalmic solution | Bromday | QD | Ocular inflammation and pain following cataract surgery |
| Bromfenac 0.07% ophthalmic solution | Prolensa | QD | Ocular inflammation and pain following cataract surgery |

**Note:** Oral bromfenac sodium (Duract, 25 mg capsules) was FDA-approved in 1997 for short-term pain management but voluntarily withdrawn in 1998 following reports of severe and fatal hepatotoxicity. The topical ophthalmic formulation is a distinct product with a fundamentally different safety profile.

---

## Safety Considerations

Please refer to the package insert for safety information.

The following safety signals are documented in the published literature and warrant proactive monitoring:

- **Hepatotoxicity (historical, oral formulation only):** Oral bromfenac was withdrawn from the global market due to fatal hepatic necrosis. Topical ophthalmic use carries negligible systemic absorption and is not associated with this risk.
- **Corneal safety:** Topical NSAIDs as a class — including bromfenac — have been associated with corneal melting and perforation in patients with compromised epithelial integrity. High-risk populations include those with dry eye syndrome, rheumatoid arthritis, collagen vascular disease, and Stevens-Johnson syndrome. A documented case of corneal perforation in undiagnosed Sjögren's syndrome following bromfenac post-cataract (PMID 30042108) and a case of corneal melting in Stevens-Johnson syndrome (PMID 17720085) underscore the importance of patient selection.
- **Severe cutaneous reactions:** At least one case of toxic epidermal necrolysis (TEN) associated with topical bromfenac ophthalmic solution has been reported (PMID 38734855). Prescribers should be alert to early signs of hypersensitivity.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs — including a landmark N=1,127 study on CME prevention — combined with a 2024 meta-analysis and extensive Phase 4 real-world data confirm that bromfenac ophthalmic solution has well-established efficacy across a broad spectrum of eye disease indications; the TxGNN score of 99.80% reflects validation of an already clinically mature ophthalmic use case.

**To proceed, the following is needed:**
- Resolve the regulatory data gap: confirm current US FDA NDA numbers and approval status for ophthalmic bromfenac formulations (Xibrom / Bromday / Prolensa) via direct FDA database query
- Obtain mechanism of action (MOA) data from DrugBank API (DrugBank ID: DB00963)
- Retrieve and parse the full package insert for key warnings, contraindications, and precautions from FDA label database
- Define a specific sub-indication focus for portfolio prioritization (post-cataract CME prevention vs. dry eye vs. anti-VEGF adjunct for maculopathy) to enable more targeted evidence gap analysis
- Establish a corneal safety monitoring plan for high-risk populations, particularly patients with pre-existing corneal surface disease or autoimmune conditions
- Conduct a drug–drug interaction analysis with commonly co-administered ophthalmic agents (steroids, antibiotics, anti-VEGF agents) once DDI database query is resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


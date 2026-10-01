---
layout: default
title: Simvastatin
parent: High Evidence (L1-L2)
nav_order: 1163
evidence_level: L1
indication_count: 8
---

# Simvastatin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **8** 
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

# Simvastatin: From Lipid Lowering to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is a statin (HMG-CoA reductase inhibitor) already marketed in the US as an oral film-coated tablet.
The TxGNN model predicts it may be effective for **familial hypercholesterolemia (FH)**, with **19 clinical trials** and **18 publications** currently supporting this direction.
This is closer to a guideline-supported use than true repurposing, because simvastatin is already a standard lipid-lowering option.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Familial hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed records are ANDA generic authorizations) |
| Recommended Decision | Proceed with Guardrails |

The license records contain no approved-indication text, so the original labeled indication cannot be quoted here.

## Why is This Prediction Reasonable?

Simvastatin inhibits HMG-CoA reductase, which lowers hepatic cholesterol synthesis and upregulates LDL receptors. This is the same pathway that drives LDL-cholesterol elevation in FH. Detailed mechanism-of-action data was not returned from the DrugBank query, so this description comes from the pack's mechanistic rationale.

FH is an inherited disorder of LDL clearance that leads to premature coronary disease. In heterozygous FH, residual LDL receptor function remains, so statins can still work through receptor upregulation. In homozygous FH, response is expected to be weaker, and add-on therapy is typically needed. The trials below reflect this: several study ezetimibe added on top of simvastatin or atorvastatin.

The pack also lists FH-adjacent predictions. "Hypercholesterolemia, autosomal dominant" (rank 4) overlaps heavily with this entry and carries the same L1 evidence. The other predictions are weaker and are covered in the conclusion.

## Clinical Trial Evidence

Most trials below use simvastatin as a comparator arm or background therapy, not as the sole test agent. They are ordered roughly by relevance.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe + high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in heterozygous FH. Simvastatin is a defined arm (highest relevance). |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Randomized, double-blind study of ezetimibe with simvastatin vs simvastatin alone in adolescents (10-17 years) with heterozygous FH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous FH (simvastatin is background therapy) |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Up to 24 months of open-label safety extension of ezetimibe plus atorvastatin or simvastatin in homozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Open-label 6-week comparison of renal effects of rosuvastatin and simvastatin in type IIa/IIb dyslipidaemia, including heterozygous FH |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A | Completed | 2089 | Post-marketing re-examination survey of ezetimibe/simvastatin (VYTORIN) in usual practice; non-randomized, real-world safety and efficacy data |
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Phase 3 | Completed | 199 | Niacin ER + simvastatin vs atorvastatin on HDL-C in hyperlipidemia or mixed dyslipidemia (not FH-specific) |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Completed | 194 | Colesevelam in children with heterozygous FH on a stable statin (including simvastatin) or treatment-naive; simvastatin is background therapy |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab added to stable statin therapy in heterozygous FH or high-risk hypercholesterolemia; simvastatin role is indirect |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Placebo-controlled alirocumab study in heterozygous FH on lipid-modifying therapy; simvastatin role is indirect |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | Trial publication (ENHANCE) | N Engl J Med | Simvastatin with or without ezetimibe in FH, assessing progression of atherosclerosis |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Statins for children with FH (earlier versions: 2017, 2014) |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Guideline | J Am Coll Cardiol | 2026 ACC/AHA multisociety dyslipidemia guideline; replaces the 2018 cholesterol guideline (also published in Circulation, PMID 41824552) |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for management of dyslipidemia and prevention of cardiovascular disease |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort analysis | J Am Coll Cardiol | Quantifies statin-related reduction in coronary artery disease events and all-cause mortality in heterozygous FH |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | Benefit and risk assessment of simvastatin in FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Saf | Long-term benefits and risks of simvastatin in FH |
| [21173733](https://pubmed.ncbi.nlm.nih.gov/21173733/) | 2010 | Long-term clinical study | Int Angiol | Long-term efficacy and safety of ezetimibe/simvastatin in FH |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative study | Nutr Metab Cardiovasc Dis | Atorvastatin vs simvastatin in attaining the LDL-C goal in heterozygous FH |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cross-sectional cohort | J Clin Med | Cellular immunity in 26 children with FH, 13 treated with simvastatin 10 mg for at least 26 weeks |

## US Market Information

The records list 20 authorizations in total; the main distinct ones are shown below. All carry an ANDA number, and none includes approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA077691 | Simvastatin | Tablet, film coated (oral) | A-S Medication Solutions |
| ANDA077691 | Simvastatin | Tablet, film coated (oral) | NorthStar Rx LLC |
| ANDA078103 | Simvastatin | Tablet, film coated (oral) | St. Mary's Medical Park Pharmacy |
| ANDA078103 | Simvastatin | Tablet, film coated (oral) | Proficient Rx LP |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug-interaction records were returned in the safety data.

The retrieved rationale and literature do flag the following:
- **Dose:** Avoid maximum-dose simvastatin (80 mg) because of myopathy risk.
- **CYP3A4 interactions:** Simvastatin exposure rises markedly with CYP3A4 inhibitors such as ritonavir and cobicistat. Rhabdomyolysis and myopathy have been reported in people with HIV on such regimens (PMID 12240878, 36409337).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials in FH include simvastatin as a defined arm or background therapy, and guidelines and reviews support statin use in FH. The direct evidence is limited, though. Many trials test add-on agents, and simvastatin is often only background therapy.

Other predicted indications do not meet this bar:
- **HIV infectious disease:** Hold. Evidence covers statin-HIV drug interactions only, with no efficacy data, and the safety signal argues against use.
- **Brain stem infarction, CETP deficiency, CYP7A1 deficiency, ABri amyloidosis, and an ultra-rare neurodevelopmental disorder:** Hold. Prediction-only evidence (L5), with no supporting trials or literature.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking data gap for safety screening)
- Approved-indication text for the US labels, to confirm whether FH is already labeled
- Manual review of the trials graded C, to confirm the role of simvastatin
- A dosing cap (avoid 80 mg) and a CYP3A4 interaction check in any development plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


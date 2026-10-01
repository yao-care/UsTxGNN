---
layout: default
title: Potassium
parent: Model Prediction Only (L5)
nav_order: 1066
evidence_level: L5
indication_count: 5
---

# Potassium
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

# Potassium: From Marketed Potassium Products to Hypertensive Disorder

## One-Sentence Summary

Potassium is an essential electrolyte sold in the US as prescription potassium citrate extended-release tablets and as homeopathic pellets. The label data provided do not state an approved indication. The TxGNN model predicts it may help with **hypertensive disorder**. The literature is strong (a dose-response meta-analysis of RCTs, a systematic review and a large salt-substitute RCT), but it concerns dietary potassium, not a standalone potassium drug. Most of the **48 listed clinical trials** are only loosely related to potassium.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license data provided |
| Predicted New Indication | Hypertensive disorder |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L3 by the rule table (the pack's automated label is L1, see the note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Proceed with Guardrails |

**Note on the evidence level:** L1 requires at least 2 completed Phase 3 RCTs of the drug itself. Only one completed Phase 3 trial of potassium is listed (NCT03809884, 7 participants). The level rests on the systematic review and meta-analysis literature, so I rate it L3.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for potassium is not available in DrugBank. The literature supplies a physiological rationale. Higher potassium intake promotes sodium excretion in urine and vasodilation, and it reduces sympathetic nervous system and renin-angiotensin activity. Together these lower blood pressure. Reviews also describe the interaction of excess sodium and potassium deficiency as a key environmental driver of primary hypertension.

No original indication is recorded, so the link to the original use is weaker than in a typical repurposing case. The direct evidence is about dietary potassium and potassium-enriched salt substitutes, not potassium drug products. In the large salt-substitute RCT (SSaSS), the intervention also lowered sodium, so the benefit cannot be attributed to potassium alone. Most listed trials concern hypertension or primary aldosteronism in general. Few test potassium itself.

---

## Clinical Trial Evidence

The 10 trials below are the most relevant of the 48 listed. The closest are the potassium-magnesium citrate trials. Many others are hypertension trials that do not test potassium.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02653560](https://clinicaltrials.gov/study/NCT02653560) | Phase 4 | Completed | 30 | Liquid potassium-magnesium citrate compared with the DASH diet for controlling hypertension |
| [NCT05145309](https://clinicaltrials.gov/study/NCT05145309) | Phase 2 | Not yet recruiting | 45 | Potassium-magnesium citrate to prevent and treat hypertension in African Americans |
| [NCT03809884](https://clinicaltrials.gov/study/NCT03809884) | Phase 3 | Completed | 7 | Dietary potassium versus a potassium supplement to raise potassium intake for high blood pressure |
| [NCT05155436](https://clinicaltrials.gov/study/NCT05155436) | Phase 4 | Completed | 1090 | Prevalence of hypo- and hyperkalemia in patients starting a telmisartan/amlodipine combination |
| [NCT01224314](https://clinicaltrials.gov/study/NCT01224314) | N/A | Completed | 24 | Effect of dialysate potassium concentration on blood pressure in haemodialysis |
| [NCT07172425](https://clinicaltrials.gov/study/NCT07172425) | N/A | Recruiting | 30 | Nitrate-fortified foods for nitric oxide metabolism; prior work used potassium nitrate capsules |
| [NCT05593055](https://clinicaltrials.gov/study/NCT05593055) | Phase 4 | Recruiting | 75 | Mineralocorticoid receptor antagonist versus a thiazide-like diuretic in hypertension with left ventricular hypertrophy; indirectly relevant through potassium handling |
| [NCT05222191](https://clinicaltrials.gov/study/NCT05222191) | Phase 2 | Unknown | 24 | Spironolactone enabled by chlorthalidone in CKD; serum potassium rise is the key side effect |
| [NCT03569020](https://clinicaltrials.gov/study/NCT03569020) | N/A | Completed | 43 | DASH diet (potassium-rich) effect on serum uric acid; potassium is not isolated |
| [NCT02452749](https://clinicaltrials.gov/study/NCT02452749) | N/A | Completed | 30 | Safety of a cardiovascular health dietary supplement in borderline to mild hypertension |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32500831](https://pubmed.ncbi.nlm.nih.gov/32500831/) | 2020 | Meta-analysis of RCTs | J Am Heart Assoc | Dose-response relationship between potassium supplementation and blood pressure in trials of at least 4 weeks |
| [23558164](https://pubmed.ncbi.nlm.nih.gov/23558164/) | 2013 | Systematic review and meta-analysis | BMJ | Effect of increased potassium intake on cardiovascular risk factors and disease |
| [34459569](https://pubmed.ncbi.nlm.nih.gov/34459569/) | 2021 | RCT | N Engl J Med | Potassium-enriched, sodium-reduced salt substitute and cardiovascular events and death |
| [37772757](https://pubmed.ncbi.nlm.nih.gov/37772757/) | 2024 | Review | Am J Hypertens | State-of-the-art review of potassium and hypertension |
| [39472546](https://pubmed.ncbi.nlm.nih.gov/39472546/) | 2025 | Review | Hypertens Res | Dietary potassium and salt substitution in preventing and managing hypertension |
| [25016398](https://pubmed.ncbi.nlm.nih.gov/25016398/) | 2014 | Review | Semin Nephrol | Interaction of sodium surfeit and potassium deficiency in the pathogenesis of hypertension |
| [27455317](https://pubmed.ncbi.nlm.nih.gov/27455317/) | 2016 | Review | Nutrients | Potassium intake, bioavailability, hypertension and glucose control |
| [23674806](https://pubmed.ncbi.nlm.nih.gov/23674806/) | 2013 | Review | Adv Nutr | Potassium and health; moderate evidence linking intake to lower blood pressure |
| [40507134](https://pubmed.ncbi.nlm.nih.gov/40507134/) | 2025 | Preclinical (rat) | Nutrients | Potassium supplementation had differing effects on blood pressure and renal function in two hypertensive rat models |
| [40232853](https://pubmed.ncbi.nlm.nih.gov/40232853/) | 2025 | Preclinical (rat) | JCI Insight | Potassium supplementation attenuated blood pressure in salt-sensitive rats of both sexes |

---

## US Market Information

The data list 20 authorizations. The 5 below are the main ones shown. None includes an approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212779 | Potassium Citrate (Bryant Ranch Prepack) | Extended-release tablet | Not provided |
| ANDA203546 | Potassium Citrate (Zydus Pharmaceuticals) | Extended-release tablet | Not provided |
| No number listed | Kali bichromicum (Boiron) | Pellet | Not provided |
| No number listed | Kali bromatum (Boiron) | Pellet | Not provided |
| No number listed | Kali Aceticum (Hahnemann Laboratories) | Pellet | Not provided |

---

## Safety Considerations

Please refer to the package insert for safety information. The drug interaction query returned no results, which likely reflects a data gap, not an absence of interactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Direct human evidence, including a dose-response meta-analysis and a large salt-substitute RCT, supports potassium for lowering blood pressure. That evidence covers dietary potassium and KCl salt substitutes, not a standalone potassium drug. The salt-substitute effect is confounded by sodium reduction. The other four predicted indications (pulmonary hypertension of two types, malignant renovascular hypertension and malignant hypertensive renal disease) have no supporting evidence or only indirect evidence, and the recommendation for each is Hold.

**To proceed, the following is needed:**
- The US package insert warnings and contraindications, which are currently missing and block safety screening.
- Mechanism-of-action data from DrugBank.
- A trial of a potassium drug product itself (for example potassium-magnesium citrate) against placebo, with blood pressure as the primary outcome.
- A patient-selection and monitoring plan:
  - Exclude or closely monitor patients with CKD, hyperkalemia risk, ACE inhibitor/ARB/MRA/potassium-sparing diuretic use, or diabetic hyporeninemic states.
  - Check serum potassium and eGFR before and during use.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


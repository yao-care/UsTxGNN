---
layout: default
title: Potassium Cation
parent: 僅模型預測 (L5)
nav_order: 1068
evidence_level: L5
indication_count: 6
---

# Potassium Cation
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Potassium Cation: From Electrolyte Supplementation to Hypertensive Disorder

## One-Sentence Summary

> Potassium Cation (DrugBank DB01345) is a fundamental electrolyte used for potassium replacement/supplementation; no original indication or product license data is currently on file for this entity.
> The TxGNN model predicts it may be effective for **Hypertensive Disorder**,
> with **3 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the available regulatory dataset (potassium cation is generally used as an electrolyte/potassium replacement agent) |
| Predicted New Indication | Hypertensive Disorder |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, potassium is the principal intracellular cation and, via the Na⁺/K⁺-ATPase pump, regulates vascular smooth muscle tone, suppresses renin secretion, and promotes natriuresis — effects that counteract the pressor response to high sodium intake.

This mechanism is not a novel model hypothesis but is already supported by decades of human dietary and epidemiological evidence: the DASH diet and WHO potassium intake guidelines both rely on this exact pathway to lower blood pressure. The predicted link between potassium supplementation and hypertension is therefore mechanistically well-grounded rather than speculative.

The main caveat is that most supporting evidence concerns **dietary potassium** rather than the pharmaceutical potassium cation product itself, and the benefit is counterbalanced by a hyperkalemia risk in patients with impaired renal function — a population where potassium is more often contraindicated than therapeutic. This is the central guardrail for this candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06683430](https://clinicaltrials.gov/study/NCT06683430) | NA | Completed | 62 | High-potassium, low-sodium diet (3500 mg K⁺/1500 mg Na⁺) in a 14-day RCT for blood pressure reduction in older adults |
| [NCT02910427](https://clinicaltrials.gov/study/NCT02910427) | NA | Completed | 291 | Potassium/magnesium-enriched salt intervention in stroke patients; blood pressure evaluated as a secondary outcome |
| [NCT06256991](https://clinicaltrials.gov/study/NCT06256991) | Phase 4 | Recruiting | 44 | Placebo-controlled crossover RCT testing whether potassium correction (patiromer) allows RAAS-blocker up-titration and reduces blood pressure/albuminuria in CKD stage 3b/4 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27455317](https://pubmed.ncbi.nlm.nih.gov/27455317/) | 2016 | Review (Tier 1) | Nutrients | Reviews potassium intake, bioavailability, and effects on hypertension and glucose control |
| [1986994](https://pubmed.ncbi.nlm.nih.gov/1986994/) | 1991 | Review/Cohort (Tier 1) | Hypertension | Low potassium intake linked to hypertension and stroke risk; potassium increases natriuresis and may blunt sodium's pressor effect |
| [29492706](https://pubmed.ncbi.nlm.nih.gov/29492706/) | 2018 | Review | Curr Cardiol Rep | Discusses hyperkalemia risk in hypertensive patients, especially with CKD, diabetes, heart failure, or RAAS inhibitor use |
| [24459498](https://pubmed.ncbi.nlm.nih.gov/24459498/) | 2007 | Review | Electrolyte Blood Press | Reviews hypertensive hypokalemic disorders and the aldosterone-mediated renal handling of potassium |
| [34063969](https://pubmed.ncbi.nlm.nih.gov/34063969/) | 2021 | Review (Tier 2) | Nutrients | Potassium promotes sodium excretion with an antihypertensive effect, particularly relevant in CKD management |
| [32498812](https://pubmed.ncbi.nlm.nih.gov/32498812/) | 2020 | Review (Tier 2) | J Am Coll Cardiol | State-of-the-art review on dyskalemia (hypo/hyperkalemia) in heart failure and its prognostic implications |
| [24721891](https://pubmed.ncbi.nlm.nih.gov/24721891/) | 2015 | Review (Tier 2) | Clin J Am Soc Nephrol | Foundational review of renal regulation of potassium homeostasis |
| [39604607](https://pubmed.ncbi.nlm.nih.gov/39604607/) | 2025 | Review (Tier 3) | Heart Fail Rev | Multidisciplinary expert perspective on hyperkalemia management and new potassium binders |
| [15692166](https://pubmed.ncbi.nlm.nih.gov/15692166/) | 2005 | Review | Clin Calcium | Discusses cellular Na:K ratio and its direct/indirect role in blood pressure regulation |
| [27194424](https://pubmed.ncbi.nlm.nih.gov/27194424/) | 2017 | Review (Tier 3) | Pediatr Nephrol | Reviews physiological consequences of deviations in serum potassium, "friend or foe" framing |

---

## US Market Information

No marketing authorizations are on file for this entity (`total_licenses = 0`, market status: **Not Marketed**). This may reflect a data gap in the regulatory dataset rather than true absence of potassium products in the US market, since potassium salts are widely marketed generically under various formulations.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or DDI data are currently available for this entity (flagged as a Blocking data gap, DG001).

**Guardrail note from evidence review:** Multiple retrieved publications emphasize that hyperkalemia risk rises sharply in patients with chronic kidney disease, diabetes, heart failure, or those on RAAS-inhibitor therapy — the same populations where hypertension is most prevalent. Any repurposing pathway must screen for renal function and concurrent RAAS-inhibitor use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between potassium and blood pressure reduction is well-established (DASH diet, WHO guidance) and supported by one completed dietary RCT (n=62) and an ongoing Phase 4 RCT in CKD patients. However, evidence targets **dietary potassium intake** rather than the pharmaceutical potassium cation product specifically, and the population most likely to benefit overlaps substantially with the population most at risk of hyperkalemia.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (Blocking data gap, DG001) — required before any S1 safety review
- Confirmed mechanism of action data via DrugBank (High-severity data gap, DG002)
- A trial or evidence source testing the **pharmaceutical potassium cation product** (not dietary intervention) specifically for blood pressure outcomes
- Renal function-based screening protocol to exclude hyperkalemia-risk patients (CKD, RAAS-inhibitor users, diabetics)
- US/Taiwan regulatory licensing status confirmation, given the current "Not Marketed" record

**Other predicted indications** (pulmonary hypertension variants, malignant hypertensive/renovascular renal disease, Braddock syndrome) are rated **Hold** — they carry TxGNN scores in a similar range but lack supporting clinical trials or mechanistically relevant literature, and in some cases (malignant hypertensive renal disease) potassium supplementation is more plausibly contraindicated than therapeutic.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


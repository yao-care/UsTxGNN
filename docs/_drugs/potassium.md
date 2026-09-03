---
layout: default
title: Potassium
parent: 僅模型預測 (L5)
nav_order: 1066
evidence_level: L5
indication_count: 5
---

# Potassium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Potassium: From Electrolyte Replacement (Hypokalemia) to Hypertensive Disorder

## One-Sentence Summary

Potassium is an essential electrolyte, conventionally used for potassium replacement/supplementation in hypokalemia and as part of routine electrolyte management.
The TxGNN model predicts it may be effective for **Hypertensive Disorder**, with **~44 registered clinical trials** (many of low direct relevance) and **21 publications** currently reviewed for this direction, including several high-quality meta-analyses and a large NEJM RCT on potassium-enriched salt substitutes.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this Evidence Pack (no TFDA/US license records); potassium is generically used for hypokalemia correction / electrolyte replacement |
| Predicted New Indication | Hypertensive Disorder |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action (MOA) data for this candidate is currently unavailable in the Evidence Pack (DG002, High severity). Based on established physiology, however, potassium promotes natriuresis, suppresses renin-angiotensin-aldosterone system (RAAS) activity, and reduces vascular smooth muscle tone — this is the core mechanistic basis underlying the DASH diet and WHO dietary recommendations for blood pressure control.

Unlike a typical drug-repurposing candidate moving between two disease areas, potassium's link to hypertension is an **already well-established nutrient-disease relationship** rather than a novel mechanistic hypothesis generated purely from knowledge-graph similarity. This is reflected in the evidence base: large-scale meta-analyses, systematic reviews, and a landmark cluster-randomized NEJM trial (potassium-enriched salt substitution) all support an inverse dose-response relationship between potassium intake and blood pressure.

The main caveat is that this evidence largely concerns **dietary potassium intake or salt substitution**, not a discrete pharmaceutical potassium product dosed for hypertension indication. Clinical translation into a formal antihypertensive indication would still require dose-ranging and safety validation, particularly given the narrow therapeutic window of potassium and hyperkalemia risk in renal impairment.

---

## Clinical Trial Evidence

Note: Many KG-matched trials in the raw evidence set were graded "C" (low relevance/noise — e.g., unrelated interventions co-occurring with a "hypertension" label). The table below lists the trials with a direct, interpretable link to potassium and blood pressure/electrolyte physiology.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03809884](https://clinicaltrials.gov/study/NCT03809884) | Phase 3 | Completed | 7 | Adaptive trial comparing dietary counseling vs. additional potassium supplement to increase potassium intake in patients with high blood pressure |
| [NCT02653560](https://clinicaltrials.gov/study/NCT02653560) | Phase 4 | Completed | 30 | Liquid potassium-magnesium citrate tested for blood pressure control, building on DASH diet rationale (K/Mg/alkali components) |
| [NCT05145309](https://clinicaltrials.gov/study/NCT05145309) | Phase 2 | Not yet recruiting | 45 | Potassium-magnesium citrate for prevention/treatment of hypertension specifically in African American patients |
| [NCT03569020](https://clinicaltrials.gov/study/NCT03569020) | N/A | Completed | 43 | DASH diet (high-potassium) effects on blood pressure/uric acid in adults with hyperuricemia and gout |
| [NCT05155436](https://clinicaltrials.gov/study/NCT05155436) | Phase 4 | Completed | 1090 | Prevalence/incidence of dyskalemia (hypo/hyperkalemia) in hypertensive patients starting fixed-dose telmisartan/amlodipine — relevant to potassium monitoring during antihypertensive therapy |
| [NCT01224314](https://clinicaltrials.gov/study/NCT01224314) | N/A | Completed | 24 | Direct hemodynamic study: rapid changes in dialysate potassium concentration produce measurable blood pressure effects ("rebound hypertension") |
| [NCT05222191](https://clinicaltrials.gov/study/NCT05222191) | Phase 2 | Unknown | 24 | Spironolactone (potassium-retaining) vs. chlorthalidone in CKD-associated hypertension; hyperkalemia risk directly relevant to potassium safety |
| [NCT02452749](https://clinicaltrials.gov/study/NCT02452749) | N/A | Completed | 30 | Safety/tolerability of a cardiovascular dietary supplement (includes potassium) in adults with borderline/mild hypertension |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34459569](https://pubmed.ncbi.nlm.nih.gov/34459569/) | 2021 | RCT (cluster) | New England Journal of Medicine | Large cluster-RCT: sodium-reduced, potassium-enriched salt substitute lowered cardiovascular events and death |
| [32500831](https://pubmed.ncbi.nlm.nih.gov/32500831/) | 2020 | Meta-analysis of RCTs | Journal of the American Heart Association | Dose-response meta-analysis showing potassium supplementation lowers blood pressure across trials ≥4 weeks |
| [23558164](https://pubmed.ncbi.nlm.nih.gov/23558164/) | 2013 | Systematic Review | BMJ | Increased potassium intake associated with reduced cardiovascular risk factors and stroke risk |
| [39472546](https://pubmed.ncbi.nlm.nih.gov/39472546/) | 2025 | Review | Hypertension Research | Role of dietary potassium and salt substitution in prevention/management of hypertension |
| [37772757](https://pubmed.ncbi.nlm.nih.gov/37772757/) | 2024 | Review | American Journal of Hypertension | State-of-the-art review on potassium's role in blood pressure regulation |
| [10979053](https://pubmed.ncbi.nlm.nih.gov/10979053/) | 2000 | Clinical Practice Guideline | Archives of Internal Medicine | National Council on Potassium in Clinical Practice guidelines for potassium replacement |
| [27455317](https://pubmed.ncbi.nlm.nih.gov/27455317/) | 2016 | Review | Nutrients | Potassium bioavailability and its relationship to hypertension and glucose control |
| [29771736](https://pubmed.ncbi.nlm.nih.gov/29771736/) | 2018 | Review | Current Opinion in Cardiology | Dietary approaches (including potassium intake) for hypertension prevention/management |
| [30190007](https://pubmed.ncbi.nlm.nih.gov/30190007/) | 2018 | Review | Journal of the American College of Cardiology | Inadequate dietary potassium identified as a modifiable environmental risk factor for hypertension |
| [25016398](https://pubmed.ncbi.nlm.nih.gov/25016398/) | 2014 | Review | Seminars in Nephrology | Interaction of sodium surfeit and potassium deficiency as the chief driver of primary hypertension risk |

---

## US Market Information

This drug currently has no marketing authorizations on file in the Evidence Pack (market status: **Not Marketed**, 0 licenses). No dosage form or approved-indication data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this Evidence Pack (flagged as Blocking data gap, DG001 — TFDA label/warnings not yet retrieved).

Given potassium's known narrow therapeutic index, any forward evaluation should explicitly prioritize hyperkalemia risk assessment (especially in renal impairment, concurrent RAAS-inhibitor/potassium-sparing diuretic use) once label data is obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The potassium–blood pressure relationship is supported by strong epidemiological and interventional evidence, including a landmark NEJM cluster-RCT and multiple meta-analyses/systematic reviews, giving this candidate an L2 evidence level. However, this reflects a nutrient-disease relationship rather than a validated pharmaceutical indication, and safety data for a formal potassium drug product in hypertension is still absent.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (DG001, Blocking — required before any S1 safety screening)
- Formal mechanism-of-action documentation from DrugBank (DG002)
- Clarification of target population and dosing (dietary supplementation vs. pharmaceutical-grade potassium product) given hyperkalemia risk, particularly in renal impairment
- A dedicated safety monitoring plan (serum potassium, renal function) before any clinical development step

*Note: Ranks 2–5 (pulmonary hypertension variants, malignant renovascular/hypertensive renal disease) are assessed as L4–L5 with no supporting mechanistic or clinical evidence and are recommended for **Hold** — several carry an increased hyperkalemia risk signal that runs counter to the proposed intervention.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


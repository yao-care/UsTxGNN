---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 1206
evidence_level: L5
indication_count: 10
monitor_inn: "TELMISARTAN"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant renovascular hypertension", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin receptor blocker, originally used to treat hypertension and to reduce stroke and cerebrovascular risk.
The TxGNN model ranks **Prinzmetal angina** as its top predicted new indication, but **no clinical trials and no publications** currently support this specific prediction.
The data compiled for this report show stronger support for two other candidates, **cerebral artery occlusion** (3 trials, 20 publications) and **intracerebral hemorrhage** (3 trials, 12 publications), which are discussed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (also stroke and cerebrovascular disorders, per the knowledge graph) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, telmisartan blocks the angiotensin II type 1 (AT1) receptor and has partial PPARgamma agonist activity. Its original use is blood pressure control, so a link to a disease of vascular tone such as Prinzmetal angina is plausible, but it is speculative and unsupported by any trial or publication provided.

Prinzmetal angina is a coronary vasospasm disorder. Vascular tone modulation through AT1 blockade is a conceivable connection to hypertension treatment, but the prediction currently rests on the model score alone.

Other predictions have more supporting data:
- **Cerebral artery occlusion** (score 99.95%): animal studies show telmisartan reduces infarct volume, oxidative stress and inflammation after middle cerebral artery occlusion. It sits close to the original stroke and cerebral infarction indications.
- **Intracerebral hemorrhage** (score 99.93%): blood pressure control is the main modifiable factor for preventing recurrence. The Phase 3 TRIDENT trial tested a single-pill combination of three low-dose antihypertensives, which cannot be attributed to telmisartan alone.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked indication, Prinzmetal angina. The tables below cover the two best-supported alternatives.

**Cerebral artery occlusion (Evidence Level L3)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) | Phase 4 | Completed | 1228 | Open-label PROBE study of telmisartan vs. ordinary therapy in high-risk hypertensive patients, looking at biomarkers and cardiovascular events; no direct outcome in cerebral artery occlusion |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study; too small to be informative |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; no usable evidence |

**Intracerebral hemorrhage (Evidence Level L2)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1671 | TRIDENT: fixed low-dose triple-pill BP lowering to prevent recurrent stroke after intracerebral hemorrhage; combination therapy, not telmisartan alone |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study; negligible evidential value |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; negligible evidential value |

---

## Literature Evidence

No publications are available for Prinzmetal angina. The tables below show the main publications for the two best-supported alternatives.

**Cerebral artery occlusion** (all preclinical; no clinical RCT evidence for this indication)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19604102](https://pubmed.ncbi.nlm.nih.gov/19604102/) | 2009 | Preclinical (animal) | J Neurotrauma | Telmisartan reduced cerebral infarct volume and peri-infarct cPLA2 level in experimental stroke |
| [25245484](https://pubmed.ncbi.nlm.nih.gov/25245484/) | 2014 | Preclinical (animal) | J Stroke Cerebrovasc Dis | Telmisartan ameliorated inflammatory responses in rats after transient MCAO |
| [32992165](https://pubmed.ncbi.nlm.nih.gov/32992165/) | 2020 | Preclinical (mechanistic) | J Stroke Cerebrovasc Dis | PPARγ activation by telmisartan inhibited Egr-1 and benefited ischaemic brain injury |
| [24650592](https://pubmed.ncbi.nlm.nih.gov/24650592/) | 2014 | Preclinical (animal) | Pharmacol Biochem Behav | Non-hypotensive telmisartan plus nimodipine gave synergistic neuroprotection by lowering brain cytokines |
| [28699721](https://pubmed.ncbi.nlm.nih.gov/28699721/) | 2016 | Preclinical (animal) | Indian J Exp Biol | Pre- vs. post-ischemic telmisartan and nimodipine combination in cerebral ischemia |
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | Preclinical (animal) | PLoS One | Telmisartan, ramipril and their combination compared in rat stroke prevention and neuroprotection models |
| [41341617](https://pubmed.ncbi.nlm.nih.gov/41341617/) | 2025 | Preclinical (animal) | Toxicol Rep | Telmisartan reduced cerebral ischemia-reperfusion neurotoxicity via the Nrf2/HO-1 pathway |

**Intracerebral hemorrhage**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT (TRIDENT results) | N Engl J Med | Three low-dose antihypertensives in a single pill after intracerebral hemorrhage; the effect direction is not shown in the data provided |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial design/protocol | Int J Stroke | TRIDENT rationale, design and progress |
| [27078703](https://pubmed.ncbi.nlm.nih.gov/27078703/) | 2016 | Preclinical (animal) | Neurol Res | Telmisartan ameliorated oxidative stress and subarachnoid haemorrhage-induced cerebral vasospasm |
| [17538008](https://pubmed.ncbi.nlm.nih.gov/17538008/) | 2007 | Preclinical (animal) | J Pharmacol Exp Ther | AT1 blockade with telmisartan reduced apoptosis, inflammation and oxidative stress in rats with ICH |

---

## US Market Information

Telmisartan has no currently valid US licenses. All 10 records are cancelled generic (ANDA) tablet products, and the approved indication text is not available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202397 | Telmisartan (A-S Medication Solutions) | Tablet | Not available (cancelled) |
| ANDA205150 | Telmisartan (Bryant Ranch Prepack) | Tablet | Not available (cancelled) |
| ANDA203986 | Telmisartan (NorthStar Rx LLC) | Tablet | Not available (cancelled) |
| ANDA208605 | Telmisartan (Bryant Ranch Prepack) | Tablet | Not available (cancelled) |
| ANDA090032 | Telmisartan (Glenmark Pharmaceuticals Inc., USA) | Tablet | Not available (cancelled) |

---

## Safety Considerations

- **Contraindications in the knowledge graph** (not label text): liver failure, kidney disease, pancreatitis, liver disease, gallbladder disease, systemic lupus erythematosus, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, gout, anuria, hyperparathyroidism, hypercalcemia, hepatic encephalopathy, cholestasis, renal artery obstruction, and several others.
- **Drug Interactions** (100 interactions were found; examples):
  - **Major:** potassium citrate and potassium bicarbonate (risk of raised potassium).
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, morphine, bupropion, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulin, exenatide, and bowel-preparation agents.
- **Specific caution:** ARBs carry known risks in renovascular disease such as bilateral renal artery stenosis. This matters for the malignant renovascular hypertension prediction.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, Prinzmetal angina, has only a model score (99.98%) with no trials or publications, so it is Level L5. Other candidates are better supported. Intracerebral hemorrhage has a Phase 3 trial, but it tested a triple combination. Cerebral artery occlusion is supported mainly by animal data. Neither can be attributed to telmisartan alone.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Any clinical or mechanistic evidence for Prinzmetal angina
- TRIDENT result details and any component-level analysis for intracerebral hemorrhage
- A clinical (not animal) study of telmisartan alone in cerebral artery occlusion
- A review of the regulatory position, since all US licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


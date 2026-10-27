---
layout: default
title: Isosorbide Dinitrate
parent: Model Prediction Only (L5)
nav_order: 815
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Isosorbide Dinitrate: predicted new indication Vascular disease (evidence level L5). Approved use: Not recorded in the compiled license data (approved indication text i…"
monitor_inn: "ISOSORBIDE DINITRATE"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "pulmonary hypertension", "diffuse alopecia areata", "vascular disease", "hypertrichosis (disease)", "visceral calciphylaxis", "venous thoracic outlet syndrome"]
---

# Isosorbide Dinitrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Isosorbide Dinitrate: From Angina/Ischemic Heart Disease to Vascular Disease
{: .text-alpha }

## One-Sentence Summary

Isosorbide dinitrate is a nitrate vasodilator, and its original approved indication is not recorded in the data compiled for this report (it is well known for angina and, combined with hydralazine, heart failure).
The TxGNN model's top-ranked predictions are mostly hair-related disorders with no supporting evidence. The best-supported candidate is **Vascular Disease**, with **6 clinical trials** (only 1 directly relevant) and **20 publications**; **Pulmonary Hypertension** is a second candidate with **20 publications** but no registered trials.
Evidence is limited, and the drug currently has no valid US licenses (all 8 are cancelled).

## Quick Overview

The report focuses on the best-supported prediction (Vascular Disease, rank 6 in the TxGNN output), not the top-scored one (alopecia), which has no evidence at all.

| Item | Content |
|------|------|
| Original Indication | Not recorded in the compiled license data (approved indication text is empty) |
| Predicted New Indication | Vascular disease (best-supported of the top 10 predictions) |
| TxGNN Prediction Score | 99.97% (Vascular disease); the top-ranked prediction, alopecia, scored 99.99% but has no evidence |
| Evidence Level | L2 (capped, because outcome data from the Phase 3 trial are not confirmed) |
| US Market Status | Cancelled only |
| Number of NDAs | 8 (all cancelled; 7 ANDAs and 1 NDA) |
| Recommended Decision | Hold (treated as a research question) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, isosorbide dinitrate is a nitric oxide (NO) donor. NO activates soluble guanylate cyclase, raises cGMP, and relaxes vascular smooth muscle. It is established in angina and, combined with hydralazine, in heart failure.

Because this mechanism acts directly on blood vessels, a link to "vascular disease" is plausible. Supporting signals include a Phase 3 trial of topical ISDN spray plus chitosan in diabetic foot ulcers, hemodynamic studies in coronary artery disease, and peripheral vascular disease work combining prostaglandin E1 with ISDN. "Vascular disease" is a very broad category, so any conclusion would require a narrower indication to be defined.

The other predictions are weaker:
- **Pulmonary hypertension** is mechanistically sound (pulmonary vasodilation). Small hemodynamic studies in COPD-related, cardiomyopathy-related, and interstitial lung fibrosis-related pulmonary hypertension show reduced pulmonary pressures. Concerns include ventilation/perfusion mismatch, nitrate tolerance, and hypotension, and PAH-specific therapies remain the standard of care.
- **Hair-related conditions** (alopecia, hypotrichosis, alopecia areata, hypertrichosis) appear to reflect graph proximity rather than a real mechanism. A vasodilator effect on scalp perfusion is speculative. Alopecia areata is autoimmune, and the hereditary hair disorders have a genetic cause. Hypertrichosis is the opposite phenotype of hair loss.
- **Kyphoscoliotic heart disease, visceral calciphylaxis, and venous thoracic outlet syndrome** have no direct evidence and only weak or unclear rationale.

## Clinical Trial Evidence

Trials for Vascular Disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02789033](https://clinicaltrials.gov/study/NCT02789033) | Phase 3 | Completed | 68 | ISDN spray plus chitosan in diabetic foot ulcers; the most directly relevant trial, but results are not available |
| [NCT00000478](https://clinicaltrials.gov/study/NCT00000478) | Phase 3 | Completed | Not reported | Asymptomatic Cardiac Ischemia Pilot study comparing anti-ischemic strategies; ISDN-specific role unclear |
| [NCT00803634](https://clinicaltrials.gov/study/NCT00803634) | Phase 3 | Completed | 117 | PRONTO pilot of IV clevidipine vs standard antihypertensives in acute heart failure; ISDN's role unconfirmed |
| [NCT01513070](https://clinicaltrials.gov/study/NCT01513070) | Phase 4 | Completed | 120 | Chinese herbal formula vs isosorbide dinitrate in moderate coronary stenosis; ISDN likely a comparator |
| [NCT02135315](https://clinicaltrials.gov/study/NCT02135315) | N/A | Completed | 1500 | Intensive vs standard blood pressure treatment in non-ST elevation acute coronary syndrome; tests a strategy, not ISDN itself |
| [NCT03011775](https://clinicaltrials.gov/study/NCT03011775) | Phase 4 | Completed | 43 | Pioglitazone and atherosclerosis in coronary disease; only indirectly relevant |

No clinical trials are registered for pulmonary hypertension or the other predicted indications.

## Literature Evidence

Selected publications for Vascular Disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1969017](https://pubmed.ncbi.nlm.nih.gov/1969017/) | 1990 | Clinical study | Lancet | PGE1 and ISDN synergistically reduced platelet deposition and increased platelet survival in peripheral vascular disease |
| [1094819](https://pubmed.ncbi.nlm.nih.gov/1094819/) | 1975 | Placebo-controlled hemodynamic study | Am Heart J | Hemodynamic effects of oral ISDN vs placebo in significant coronary artery disease |
| [822703](https://pubmed.ncbi.nlm.nih.gov/822703/) | 1976 | Hemodynamic study | Am Heart J | Sublingual and oral ISDN vs nitroglycerin on central circulatory dynamics in coronary artery disease |
| [33721195](https://pubmed.ncbi.nlm.nih.gov/33721195/) | 2021 | Physiological study | J Cardiovasc Transl Res | Afterload reduction by ISDN and its effects on cardiac mechanics and coronary hemodynamics |
| [3539616](https://pubmed.ncbi.nlm.nih.gov/3539616/) | 1986 | Hemodynamic study | Eur Heart J | Sustained-release ISDN effects on carotid and forearm circulation in 16 hypertensive patients |
| [3925742](https://pubmed.ncbi.nlm.nih.gov/3925742/) | 1985 | Review | Am Heart J | Nitrate tolerance, a key limitation of long-term therapy |
| [6430767](https://pubmed.ncbi.nlm.nih.gov/6430767/) | 1984 | Review | Herz | Tolerance to ISDN develops within 24 hours and reverses after about 21 hours of withdrawal |
| [3893082](https://pubmed.ncbi.nlm.nih.gov/3893082/) | 1985 | Review | Am Heart J | ISDN alone and in combination with other antianginal agents |
| [813510](https://pubmed.ncbi.nlm.nih.gov/813510/) | 1976 | Animal/hemodynamic | Am J Cardiol | Nitroglycerin vs ISDN on coronary collaterals and ischemic myocardium in dogs |
| [30118486](https://pubmed.ncbi.nlm.nih.gov/30118486/) | 2018 | Experimental | PLoS One | Nitroglycerin and coronary arteriogenesis, with NO playing an essential role |

Selected publications for Pulmonary Hypertension:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [373940](https://pubmed.ncbi.nlm.nih.gov/373940/) | 1979 | Randomized, double-blind hemodynamic study | Clin Pharmacol Ther | Oral ISDN vs placebo in 18 COPD patients with pulmonary hypertension |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Hemodynamic study | Bull Eur Physiopathol Respir | ISDN and nitroglycerin lowered pulmonary arterial pressure in 27 COPD patients; only nitroglycerin reduced pulmonary vascular resistance |
| [3409916](https://pubmed.ncbi.nlm.nih.gov/3409916/) | 1988 | Clinical study | Eur Heart J | Two-year ISDN therapy gave sustained hemodynamic improvement in interstitial lung fibrosis |
| [39164577](https://pubmed.ncbi.nlm.nih.gov/39164577/) | 2025 | Clinical study | Heart Vessels | Bolus ISDN in pulmonary hypertension with cardiopulmonary comorbidities; risk of reduced cardiac output and blood pressure, especially in pre-capillary disease |
| [8908227](https://pubmed.ncbi.nlm.nih.gov/8908227/) | 1996 | Hemodynamic study | Acta Anaesthesiol Scand | Pulmonary vascular effects of nitroglycerin vs ISDN in end-stage cardiomyopathy |
| [7125407](https://pubmed.ncbi.nlm.nih.gov/7125407/) | 1982 | Hemodynamic study | Ann Intern Med | In primary pulmonary hypertension, ISDN was the only drug that reduced pulmonary pressure |
| [2868878](https://pubmed.ncbi.nlm.nih.gov/2868878/) | 1986 | Review | Drugs | Drug treatment of primary pulmonary hypertension; adequate trials have not been performed |
| [28810603](https://pubmed.ncbi.nlm.nih.gov/28810603/) | 2017 | Preclinical | Exp Ther Med | Intratracheal ISDN improved pulmonary pressure and ventricular remodeling in a rat heart failure model |
| [2498122](https://pubmed.ncbi.nlm.nih.gov/2498122/) | 1989 | Animal | Exp Mol Pathol | ISDN in monocrotaline-induced pulmonary hypertension in rats |
| [6530750](https://pubmed.ncbi.nlm.nih.gov/6530750/) | 1984 | Case report | Jpn Heart J | Sustained improvement with prazosin plus ISDN in primary pulmonary hypertension |

## US Market Information

All 8 US authorizations are cancelled. No approved indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|-----------|
| NDA012093 | Isosorbide Dinitrate | Tablet | Oceanside Pharmaceuticals | Cancelled |
| ANDA088088 | Isosorbide Dinitrate | Tablet | Golden State Medical Supply | Cancelled |
| ANDA086923 | Isosorbide Dinitrate | Tablet | Endo USA | Cancelled |
| ANDA213057 | Isosorbide dinitrate | Tablet | Zydus Pharmaceuticals (USA) | Cancelled |
| ANDA215723 | Isosorbide Dinitrate | Tablet | Advagen Pharma | Cancelled |

Three more cancelled licenses (ANDA086067, ANDA086066, ANDA087537) are not shown. All products are oral tablets.

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these are drug-disease links from the TxGNN knowledge graph, not package insert text):
- Cardiovascular: hypotensive disorder, hypertrophic cardiomyopathy, coronary artery disease, coronary thrombosis, myocardial infarction
- Cerebrovascular: stroke disorder, cerebrovascular disorder, cerebral infarction, intracerebral hemorrhage, pseudotumor cerebri, intracranial hypertension
- Hematologic: hemoglobinopathy, anemia, macrocytic anemia
- Endocrine: hyperthyroidism, Graves disease, thyrotoxicosis
- Other: slow acetylation, Rowell syndrome

Because coronary artery disease and myocardial infarction appear in this list, it should be interpreted cautiously and checked against the actual label.

**Drug Interactions**: 100 interactions were found. Examples of those listed:
- Moderate: bupropion, morphine, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, dronabinol, nabilone, opium, rosiglitazone, sapropterin
- Minor: omeprazole
- Unknown severity: calcitriol, glimepiride, doxycycline, clotrimazole, cimetidine, atropine, epinephrine, amphotericin B

**Class concerns noted in the literature**: nitrate tolerance (develops within 24 hours), hypotension, and possible worsening of ventilation/perfusion matching in lung disease.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-scoring predictions (hair disorders) have no evidence or plausible mechanism and appear to be graph artifacts. Vascular disease has the most evidence, but it is a broad category. The only directly relevant Phase 3 trial (topical ISDN in diabetic foot ulcers) has no confirmed results, and the literature is mostly older hemodynamic studies and reviews. Pulmonary hypertension is a reasonable research question, but outcome benefit is not established. In the US, all licenses are currently cancelled and the package insert safety data are missing.

**To proceed, the following is needed:**
- Results of NCT02789033 (topical ISDN spray in diabetic foot ulcers)
- A narrower, clinically defined indication in place of "vascular disease" (for example, diabetic foot ulcer or peripheral artery disease)
- Randomized outcome data for pulmonary hypertension, including ventilation/perfusion and oxygenation safety
- FDA package insert warnings and contraindications, plus mechanism of action data
- Clarification of the cancelled US license status and the approved original indication
- A strategy to manage nitrate tolerance and hypotension risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


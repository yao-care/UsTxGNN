---
layout: default
title: Diltiazem
parent: Model Prediction Only (L5)
nav_order: 609
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Diltiazem: From Hypertension and Arrhythmia to Obsolete Susceptibility to Ischemic Stroke

## One-Sentence Summary

Diltiazem is a calcium channel blocker originally used for hypertension, atrial fibrillation, Prinzmetal angina and ventricular tachycardia.
The TxGNN model predicts it may be effective for **obsolete susceptibility to ischemic stroke**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, Prinzmetal angina, ventricular tachycardia (from the knowledge graph; no approved-indication text is available) |
| Predicted New Indication | Obsolete susceptibility to ischemic stroke |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all listed authorizations are cancelled) |
| Number of NDAs | 19 authorizations in total (3 NDAs and 16 ANDAs by number prefix, none currently valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, diltiazem is a non-dihydropyridine calcium channel blocker. It lowers blood pressure and reduces vascular smooth muscle tone, and it may also cause cerebral vasodilation. These effects could plausibly relate to stroke susceptibility, since hypertension is a major stroke risk factor. This reasoning was not verified against any study in the data provided.

There is an important caveat: the predicted disease term is flagged as "obsolete" in the ontology. It may be a deprecated or merged concept and may not map cleanly onto a current clinical indication such as secondary stroke prevention or a defined ischemic stroke risk phenotype. The high score of 99.08% is a model output, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 19 authorizations are cancelled. The main ones are listed below (approved-indication text is not available in the data).

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA020401 | TIAZAC | Capsule, extended release | Cancelled |
| NDA020062 | Cardizem CD | Capsule, coated, extended release | Cancelled |
| NDA021392 | Diltiazem Hydrochloride | Tablet, extended release | Cancelled |
| ANDA077686 | Matzim LA | Tablet, extended release | Cancelled |
| ANDA074752 | Cartia | Capsule, extended release | Cancelled |

The other authorizations cover oral capsules and tablets, as well as injectable solution and lyophilized powder.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert for them.

- **Knowledge-graph contraindication signals** (not label text): The knowledge graph links diltiazem to the following conditions, which need verification against the label:
  - Cardiac conduction and rhythm: atrioventricular block, sick sinus syndrome, Wolff-Parkinson-White syndrome, Lown-Ganong-Levine syndrome, ventricular tachycardia
  - Structural heart and blood pressure: aortic stenosis, hypertrophic cardiomyopathy, hypotensive disorder
  - Hepatic and renal: liver disease, kidney disease, renal artery obstruction
  - Haematological: neutropenia, agranulocytosis
  - Angioedema (several types)
  - Other: gallbladder disease, connective tissue, bone and cartilage disease
- **Drug Interactions**: 100 interactions were recorded, and 20 are shown in the data. One is rated **Major**: loperamide. The rest are rated Moderate, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), pioglitazone, canagliflozin, bupropion, aprepitant, morphine, acetylsalicylic acid, and calcium salts (carbonate, chloride, citrate, acetate and others).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or publications (evidence level L5). The predicted disease term is obsolete, and the US market status is "cancelled only". Package insert safety data and mechanism of action data are also missing.

**To proceed, the following is needed:**
- Clarify the current disease concept that replaces the obsolete term, such as secondary stroke prevention or a specific risk phenotype
- A literature and trial search on diltiazem and ischemic stroke
- Detailed mechanism of action data
- Package insert warnings and contraindications, to complete the safety screening
- Confirmation of whether any diltiazem product is currently marketed in the US, and review of the route and dosage form for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


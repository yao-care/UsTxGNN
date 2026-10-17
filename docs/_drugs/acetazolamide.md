---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
monitor_inn: "ACETAZOLAMIDE"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "myopathic intestinal pseudoobstruction"]
last_modified_at: 2026-10-14
description: "Acetazolamide: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Absence epilepsy, congestive heart failure, open-angle glaucoma…"
---

# Acetazolamide
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

# Acetazolamide: From Absence Epilepsy and Glaucoma to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor, originally used for conditions such as absence epilepsy, congestive heart failure, open-angle and angle-closure glaucoma, and altitude sickness.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but **0 clinical trials** and **0 publications** currently support this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence epilepsy, congestive heart failure, open-angle glaucoma, angle-closure glaucoma, altitude sickness (the US license records contain no indication text) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 12 (all ANDA generic applications, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, acetazolamide inhibits carbonic anhydrase, which changes acid-base balance and fluid handling. It has an established record in several conditions, including glaucoma, epilepsy, heart failure and altitude sickness. It has also been used in some channelopathies, such as periodic paralysis.

A link to exercise-induced malignant hyperthermia would have to run through skeletal muscle calcium handling or acid-base effects during exertion. This connection is speculative. The data compiled for this report contain no clinical or mechanistic evidence supporting it. The very high model score (0.9995) should therefore be read as a hypothesis-generating signal only.

Other top-ranked predictions are also weak:
- **Hypertrophic cardiomyopathy and cardiomyopathy:** The retrieved papers concern acetazolamide in heart failure, which is an existing use. They do not address cardiomyopathy itself.
- **Intestinal obstruction:** The literature points toward harm, with case reports of acetazolamide-induced ileus.
- **Cirrhotic cardiomyopathy:** Acetazolamide may precipitate hyperammonemia in cirrhosis, a safety concern.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for exercise-induced malignant hyperthermia.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA210588 | Acetazolamide (ANI Pharmaceuticals) | Tablet | Not stated; status cancelled |
| ANDA211372 | Acetazolamide (TruPharma) | Tablet | Not stated; status cancelled |
| ANDA205530 | Acetazolamide (AvKARE) | Tablet | Not stated; status cancelled |
| ANDA040904 | Acetazolamide (Heritage/Avet) | Extended-release capsule | Not stated; status cancelled |
| ANDA040089 | Acetazolamide (Hikma) | Lyophilized powder for injection | Not stated; status cancelled |

All 12 records in the compiled data are cancelled, with no currently valid single-ingredient or combination licenses. The five above are a selection; the remainder are generic tablet and capsule applications.

## Safety Considerations

- **Disease-level cautions from the knowledge graph (not label text):** The knowledge graph flags contraindication relationships with liver failure and liver disease, kidney disease, renal tubular acidosis, respiratory failure, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), gout, gallbladder disease, hematologic disease, diabetes mellitus (type 1 and type 2), and diabetic ketoacidosis.
- **Drug Interactions:** The interaction query returned 100 records. The main ones shown include:
  - **Major:** acetylsalicylic acid and cisapride.
  - **Moderate:** antidiabetic agents (acarbose, acetohexamide, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide), amphotericin B formulations, corticosteroids (beclomethasone, betamethasone, dexamethasone), and laxatives (bisacodyl, castor oil).
  - **Minor:** doxycycline.
- **Signals from the retrieved literature:** Case reports describe acetazolamide-induced adynamic ileus and non-cardiogenic pulmonary edema after intravenous use. Acetazolamide may also worsen hyperammonemia in cirrhosis.

Please refer to the package insert for full warnings and contraindications, which were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials or publications for exercise-induced malignant hyperthermia, and no plausible mechanism was identified. The drug has no currently valid US licenses in the compiled data, and the safety data are incomplete. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanistic data (MOA) and a testable rationale linking carbonic anhydrase inhibition to the muscle pathophysiology of the predicted condition
- Preclinical or case-based evidence in exercise-induced malignant hyperthermia
- FDA package insert warnings and contraindications, to complete safety screening
- Confirmation of current US regulatory and marketing status, since all 12 records are cancelled
- Review of the disease-level cautions and the interaction profile for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


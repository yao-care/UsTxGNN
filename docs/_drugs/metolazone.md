---
layout: default
title: Metolazone
parent: Model Prediction Only (L5)
nav_order: 919
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Metolazone: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertensive disorder / hypertension"
monitor_inn: "METOLAZONE"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Metolazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metolazone: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Metolazone is a thiazide-like diuretic originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **0 clinical trials** and **0 publications** currently support this prediction. The result is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metolazone is a thiazide-like diuretic. Its efficacy in hypertension is established, and it may mechanistically be applicable to malignant renovascular hypertension.

Malignant renovascular hypertension is driven largely by activation of the renin-angiotensin system and by volume and pressure dynamics. A thiazide-like diuretic could plausibly play an adjunctive role by reducing volume load. This indication is biologically adjacent to the original use, which likely contributes to the very high score.

The score is a computational prediction only. No trials or publications support it, and overlap with the original indication (hypertension) may inflate it.

Other predicted indications from the model are weaker still:
- **Malignant hypertensive renal disease** (score 99.84%): a renal complication of severe hypertension. Metolazone is known to retain efficacy in reduced renal function, which offers a plausible rationale, but there is no clinical validation.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.83%) and **pulmonary hypertension with unclear multifactorial mechanism** (99.83%): diuretics may relieve right-heart volume overload, but this is symptom management, not disease modification. Systemic and pulmonary hypertension are distinct conditions, so the shared name likely drives the prediction.
- **Braddock syndrome** (99.78%): a rare genetic condition with no evident mechanistic link to thiazide-like action. The prediction is likely a knowledge-graph artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top predicted indication. For the third-ranked indication (pulmonary hypertension owing to lung disease and/or hypoxia), one paper was retrieved:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2916665](https://pubmed.ncbi.nlm.nih.gov/2916665/) | 1989 | Preclinical/Basic research | The American Journal of Physiology | In rats, thiazide diuretic receptors (labelled with [3H]metolazone) fell by about 90% after 10 minutes of acute renal ischemia, and the change was reversible. It does not address pulmonary hypertension and offers no clinical support. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA076466 | Metolazone (Sandoz Inc) | Tablet | Not available (cancelled) |
| ANDA217563 | Metolazone (Micro Labs Limited) | Tablet | Not available (cancelled) |
| ANDA213827 | Metolazone (American Health Packaging) | Tablet | Not available (cancelled) |
| ANDA214799 | Metolazone (Unichem Pharmaceuticals (USA), Inc.) | Tablet | Not available (cancelled) |
| ANDA076698 | Metolazone (Mylan Pharmaceuticals Inc.) | Tablet | Not available (cancelled) |

All 10 authorizations on record are cancelled; the table shows the first 5. There are no valid single-ingredient or combination licenses.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: The model's knowledge graph links metolazone to contraindications in the following conditions:
  - Circulatory: orthostatic hypotension, multiple system atrophy, postural orthostatic tachycardia syndrome
  - Hepatic: liver failure, hepatic coma, hepatic encephalopathy
  - Renal: anuria, nephrocalcinosis
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, gout, potassium deficiency disease, hypercalcemia, phosphorus metabolism disease
  - Autoimmune: systemic lupus erythematosus (including the pediatric form)
  - Other: pancreatitis, HELLP syndrome
- **Drug Interactions**: 100 interactions were identified. Most of those listed are Moderate, including:
  - Antidiabetics: acarbose, alogliptin, albiglutide
  - Corticosteroids: hydrocortisone, dexamethasone, triamcinolone, betamethasone, beclomethasone
  - Proton pump inhibitors: omeprazole, rabeprazole
  - Amphotericin B (including the lipid complex), bupropion, morphine, cholecalciferol, bisacodyl, calcium phosphate
  - Minor: doxycycline, hyoscyamine, atropine

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.84%) is a model prediction only. No clinical trials or publications support it (Evidence Level L5). Metolazone has no currently valid US licenses, and the shared hypertension terminology likely inflates the score.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications (the current safety data comes only from the knowledge graph)
- Mechanism of action data
- A literature and trial search specific to renovascular and malignant hypertension
- Review of the regulatory and market status, since all US licenses are cancelled
- Route compatibility and similarity-to-original-indication assessments (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


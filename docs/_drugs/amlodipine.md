---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 329
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Amlodipine: predicted new indication Brain stem infarction (evidence level L5). Approved use: Hypertension (also stroke, cerebral infarction, Prinzmetal angina)"
monitor_inn: "AMLODIPINE"
predicted_indications: ["brain stem infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
---

# Amlodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Amlodipine: From Hypertension to Brain Stem Infarction
{: .text-alpha }

## One-Sentence Summary

Amlodipine is a calcium channel blocker originally used to treat hypertension and related cerebrovascular conditions, including stroke and cerebral infarction. The TxGNN model predicts it may be effective for **brain stem infarction**, but **no clinical trials and no publications** specific to this indication were found, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (also stroke, cerebral infarction, Prinzmetal angina) |
| Predicted New Indication | Brain stem infarction |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of NDAs | 11 authorizations (2 NDAs, 9 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amlodipine is a dihydropyridine L-type calcium channel blocker. Its efficacy in hypertension is established, and it is already linked to stroke and cerebral infarction through blood pressure control and a possible neuroprotective effect.

Brain stem infarction is an anatomical subtype of the cerebral infarction family. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence for this subtype. Mechanistically, lowering blood pressure and blocking calcium channels could help in ischemic stroke generally, but nothing in the data compiled for this report addresses brain stem infarction specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications Worth Noting

The data compiled for this report contain stronger evidence for other predictions than for the top-ranked one. These are shown for context only.

| Predicted Indication | TxGNN Score | Evidence Level | Key Evidence | Recommendation |
|------|------|------|------|------|
| Intracerebral hemorrhage | 0.9979 | L1 | TRIDENT (NCT02699645): completed Phase 3 RCT, n=1671, testing a triple low-dose antihypertensive pill that includes amlodipine; results published in 2026 ([PMID 42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/)) | Proceed with Guardrails |
| Cerebral artery occlusion | 0.9989 | L3 | Rodent stroke models show reduced infarct size with amlodipine; the related clinical sub-studies were terminated with 1 to 4 participants | Research question |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9991 | L5 | Mostly indirect preclinical work and case reports. Vasodilation may worsen ventilation-perfusion matching, so there is a safety concern | Hold |

The intracerebral hemorrhage result concerns amlodipine as one component of a combination pill. Its independent contribution cannot be separated from the other two drugs.

---

## US Market Information

All 11 listed authorizations are valid. The five main ones are shown below. Approved indication text was not available for these entries.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019787 | Amlodipine besylate (Mylan Pharmaceuticals) | Tablet | Not listed |
| NDA219531 | Sdamlo (Pangea Pharmaceuticals) | Solution | Not listed |
| ANDA206367 | Amlodipine besylate (Exelan Pharmaceuticals) | Tablet | Not listed |
| ANDA078021 | Amlodipine besylate (Aurobindo Pharma) | Tablet | Not listed |
| ANDA078226 | Amlodipine besylate (Cardinal Health 107) | Tablet | Not listed |

---

## Safety Considerations

Label-based warnings and contraindications were not available. Please refer to the package insert for safety information.

- **Conditions flagged in the knowledge graph (not label text)**: the TxGNN knowledge graph links amlodipine to the following contraindicated or caution-needed conditions, and these should be verified against the label:
  - Liver failure and liver disease
  - Kidney disease
  - Angioedema (including hereditary and RAAS-blocker-induced forms)
  - Hypotensive disorders
  - Pancreatitis
  - Diabetes mellitus and diabetic ketoacidosis
  - Hypothyroidism
  - Systemic lupus erythematosus
  - Myopathy
  - Neutropenia and agranulocytosis
- **Drug interactions**: 100 interactions were found, and the 20 reviewed are all rated Moderate. Examples include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide), aspirin, aprepitant, bupropion, clarithromycin, clotrimazole, calcium salts, and the SGLT2 inhibitors canagliflozin and dapagliflozin.
- **Literature signals**: case reports describe amlodipine overdose with non-cardiogenic pulmonary edema, amlodipine-associated angioedema, and hypoxia during one-lung ventilation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for brain stem infarction rests only on the TxGNN model (deep learning) score, which may reflect similarities the model learned between related diseases, not biological evidence. There are no trials or publications for this subtype. The drug is marketed in the US, with 11 valid authorizations.

**To proceed, the following is needed:**
- Clinical or observational evidence specific to brain stem infarction
- Mechanism of action data and a clearer link between amlodipine and posterior circulation stroke
- The FDA package insert warnings and contraindications, which are currently missing
- Consideration of intracerebral hemorrhage as a more evidence-supported repurposing direction, noting that the TRIDENT evidence applies to a combination regimen and requires hypotension monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Lisinopril
parent: Moderate Evidence (L3-L4)
nav_order: 864
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Lisinopril: predicted new indication Posterolateral myocardial infarction (evidence level L4). Approved use: Hypertension, myocardial infarction"
monitor_inn: "LISINOPRIL"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
---

# Lisinopril
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Lisinopril: From Hypertension and Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor originally used to treat hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**,
but **no clinical trials** and **no publications** specific to this indication were found, so the prediction mainly reflects its closeness to the already-approved myocardial infarction indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (the US license records contain no indication text; these are taken from the knowledge-graph indication list) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 7 (1 NDA and 6 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known information, lisinopril is an angiotensin-converting enzyme (ACE) inhibitor. It lowers angiotensin II-mediated vasoconstriction, and its efficacy in hypertension and myocardial infarction is established.

Posterolateral myocardial infarction is an anatomical subtype of myocardial infarction, for which lisinopril is already indicated. The high TxGNN score most likely reflects this closeness in the disease ontology rather than a genuinely new repurposing signal. The same is true of the other infarction subtypes ranked by the model (posteroinferior and septal), and of malignant renovascular hypertension and malignant hypertensive renal disease, which sit close to the approved hypertension indication.

Other predictions have a weaker basis. Pulmonary hypertension and chronic pulmonary heart disease have a plausible mechanistic rationale, but ACE inhibitors are not an established therapy for them. Braddock syndrome and the COL4A1-related familial hematuria syndrome have no established mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction.

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

For context, the table below lists the most relevant publications retrieved for the other predicted indications.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | Clinical study (design unconfirmed) | Kardiologiia | Lisinopril 10 mg/day reduced pulmonary hypertension and improved right ventricular systolic function in heart failure patients with ischemic heart disease and COPD (chronic pulmonary heart disease) |
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | Clinical study (design unconfirmed) | Problemy tuberkuleza i boleznei legkikh | Lisinopril in patients with chronic cor pulmonale (no abstract available) |
| [39018146](https://pubmed.ncbi.nlm.nih.gov/39018146/) | 2024 | Case report | JPMA | ACE inhibitor plus coenzyme Q10 as adjunctive treatment in ventricular septal rupture after late-onset myocardial infarction (septal MI) |
| [10456287](https://pubmed.ncbi.nlm.nih.gov/10456287/) | 1999 | Preclinical (isolated vessels) | Fundamental & Clinical Pharmacology | In rat pulmonary arteries, endothelin rather than angiotensin II drives the hypoxic contractile response, which argues against an ACE-inhibitor mechanism in hypoxic pulmonary hypertension |
| [26895877](https://pubmed.ncbi.nlm.nih.gov/26895877/) | 2016 | Review/Commentary | Eur J Pediatr | Discusses ACE inhibitor use in pediatric chronic heart failure despite limited data |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019777 | Zestril (Upsher-Smith) | Tablet | Not recorded; cancelled |
| ANDA076180 | Lisinopril (Proficient Rx) | Tablet | Not recorded; cancelled |
| ANDA075903 | Lisinopril (XLCare) | Tablet | Not recorded; cancelled |
| ANDA076164 | Lisinopril (A-S Medication Solutions) | Tablet | Not recorded; cancelled |
| ANDA077321 | Lisinopril (RemedyRepack) | Tablet | Not recorded; cancelled |

Two further ANDAs (ANDA076102, Bryant Ranch Prepack; ANDA203508, Exelan) are also cancelled. All seven licenses are oral tablets.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report; please refer to the package insert for label information.

- **Knowledge-graph contraindication signals (not label text)**: angioedema (including hereditary, acquired and RAS-blocker-induced forms), kidney disease, liver disease, pancreatitis, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, systemic lupus erythematosus and connective tissue disease, neutropenia and agranulocytosis, aortic stenosis, hypotensive disorders, potassium deficiency, hyperparathyroidism and bone disease, and hepatic encephalopathy.
- **Drug Interactions**: 100 interactions were found. Two are rated Major: **potassium citrate** and **potassium bicarbonate** (risk of hyperkalaemia). Moderate ones include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic drugs (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), acetylsalicylic acid, morphine, bupropion and dronabinol.
- **Indication-specific cautions**: ACE inhibitors carry a known risk of acute kidney injury in bilateral renal artery stenosis (relevant to renovascular hypertension), and renal function and hyperkalaemia need evaluation in malignant hypertensive renal disease.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Lisinopril is already used for myocardial infarction, and posterolateral MI is a subtype of it. The high score therefore reflects ontology proximity rather than new evidence, and no subtype-specific trials or literature were found. The evidence level is L4, and all seven US licenses are cancelled. Of the other predicted indications, only chronic pulmonary heart disease has any lisinopril-specific clinical publications (older, small, and unconfirmed in design).

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data
- Clarification of whether the myocardial infarction subtypes need separate evaluation at all, given that the parent indication is already covered
- Controlled clinical evidence in chronic pulmonary heart disease, if that indication is pursued, because the existing studies are old and their design is unconfirmed
- Clarification of the reason for the cancelled US licenses and the current market availability of lisinopril products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


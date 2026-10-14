---
layout: default
title: Dulaglutide
parent: Model Prediction Only (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
---

# Dulaglutide
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

# Dulaglutide: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Dulaglutide is a once-weekly injectable GLP-1 receptor agonist, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Opsismodysplasia**, a rare skeletal dysplasia, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single registered license is cancelled) |
| Number of NDAs | 1 (BLA125469) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dulaglutide belongs to the GLP-1 receptor agonist class. Its efficacy in type 2 diabetes is established, and it acts by stimulating glucose-dependent insulin secretion.

The link to opsismodysplasia is weak. Opsismodysplasia is a rare skeletal dysplasia caused by mutations in INPPL1 (SHIP2). SHIP2 is a negative regulator of insulin/PI3K signaling, so there is a speculative connection to insulin-pathway biology. However, GLP-1 receptor agonism has no established role in skeletal dysplasia. The high TxGNN score reflects graph-based proximity only and is not backed by clinical or literature evidence.

**Other predictions in the list** (all L5, all Hold, none with trials or literature):

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Classic stiff person syndrome | 97.05% | Indirect link via GAD autoimmunity; no evidence of benefit |
| 3 | Focal stiff limb syndrome | 97.05% | Same weak rationale and identical score, suggesting an ontology-driven prediction |
| 4 | Thiamine-responsive dysfunction syndrome | 96.81% | Overlap with diabetes is plausible but untested; standard care is thiamine and insulin |
| 5 | Drug-induced localized lipodystrophy | 95.62% | No known benefit; dulaglutide is itself injectable |
| 6 | Pancreatic agenesis | 95.55% | Biologically implausible, as beta cells are absent |
| 7 | Centrifugal lipodystrophy | 95.37% | No known mechanistic link |
| 8 | Pressure-induced localized lipoatrophy | 95.29% | Mechanical injury; no plausible GLP-1 role |
| 9 | Idiopathic localized lipodystrophy | 94.99% | Undefined etiology; no mechanism-based link |
| 10 | Autoimmune oophoritis | 69.57% | Possible immunomodulatory effects, but no evidence |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125469 (cancelled) | TRULICITY (A-S Medication Solutions) | Injection, solution | Not listed in the compiled data |

## Safety Considerations

**Drug Interactions**: The interaction screening completed and returned 100 interacting drugs. Most of the entries reviewed are Moderate, and a few are Minor. Examples:

- **Moderate**: phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol, hydrocortisone, ethinylestradiol, estradiol, norethisterone, furosemide, hydrochlorothiazide, acetazolamide, ethanol, fosamprenavir, fosphenytoin, gemifloxacin, alpelisib, aripiprazole
- **Minor**: topical hydrocortisone, topical alclometasone

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications. The mechanistic link between GLP-1 receptor agonism and opsismodysplasia is speculative. The only US license in the data is cancelled, and warnings and contraindications are missing from the data compiled.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank)
- The FDA package insert, to complete warnings and contraindications (a blocking gap for safety screening)
- Preclinical or mechanistic studies testing whether GLP-1 receptor agonism affects INPPL1/SHIP2-related skeletal pathology
- Confirmation of current US marketing status, since the only listed license is cancelled
- A review of whether another candidate (for example, thiamine-responsive dysfunction syndrome) has a more testable rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


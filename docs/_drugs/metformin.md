---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 905
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metformin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Metformin was originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations in the data compiled for this report) |
| Number of NDAs | 14 (all cancelled; all listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for metformin in the data compiled for this report. Based on known information, metformin is an established oral antidiabetic agent for type 2 diabetes, but no mechanism has been identified that addresses the neurological pathology of the predicted indication.

Stiff person syndrome is an autoimmune neurological disorder involving anti-GAD65 antibodies and impaired GABAergic signaling. One possible indirect link is that GAD-antibody autoimmunity co-occurs with type 1 and type 2 diabetes. This is speculative and does not suggest that metformin treats the neurological condition.

The same score (99.45%) was given to a closely related condition, focal stiff limb syndrome, which suggests the model treats these as neighboring nodes in its knowledge graph rather than providing independent support. The score should therefore be read as a computational signal only.

**Other predicted indications (all L5, all Hold, no trials or literature):**

| Rank | Predicted Indication | TxGNN Score | Note |
|---|---|---|---|
| 2 | Focal stiff limb syndrome | 99.45% | Variant of the stiff person spectrum; no plausible metformin mechanism identified |
| 3 | Opsismodysplasia | 99.40% | INPPL1/SHIP2 and PI3K/AKT signaling; loose link to metformin's AMPK/mTOR effects, hypothetical only |
| 4 | Thiamine-responsive dysfunction syndrome | 99.40% | Possible transporter overlap, unvalidated; standard treatment is thiamine, and the relationship could even be adverse |
| 5 | Drug-induced localized lipodystrophy | 99.06% | Metformin has been studied in other lipodystrophy settings, but no evidence for the localized drug-induced form in the data |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 14 authorizations are cancelled, and the data compiled for this report contains no approved-indication text. The five below are shown as examples.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA201991 | Metformin Hydrochloride (Northwind Health Company) | Tablet, extended release | Not available (cancelled) |
| ANDA077078 | Metformin Hydrochloride (Zydus Lifesciences) | Tablet, extended release | Not available (cancelled) |
| ANDA211052 | Metformin Hydrochloride (Epic Pharma) | Tablet, extended release | Not available (cancelled) |
| ANDA202917 | Metformin Hydrochloride (Sun Pharmaceutical) | Tablet, film coated, extended release | Not available (cancelled) |
| ANDA075972 | Metformin Hydrochloride (Chartwell RX) | Tablet | Not available (cancelled) |

All dosage forms are oral (tablet, film-coated tablet, and extended-release versions).

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text):**
  - Liver failure and liver disease
  - Kidney disease
  - Congestive heart failure
  - Pancreatitis
  - Gallbladder disease
  - Pyoureter
  - Adrenocortical insufficiency
  - Thymus gland disease
  - Pituitary hormone deficiency conditions (hypopituitarism, Sheehan syndrome, growth hormone deficiencies, and related forms)
  - Hypogonadotropic hypogonadism conditions (including Kallmann syndrome)
- **Drug Interactions:** 100 interactions were found in total. Examples of those listed:
  - **Major:** Acetazolamide, Ethanol
  - **Moderate:** Dolutegravir, Abemaciclib, Phenylephrine, Ranitidine, Formoterol, Pseudoephedrine, Ketorolac, Nifedipine, Epinephrine, Ibuprofen, Ethinylestradiol, Hydrocortisone, Salbutamol, Hydrochlorothiazide, Acetohexamide
  - **Minor:** Acarbose, topical hydrocortisone, topical alclometasone

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or literature, and no plausible mechanistic link between metformin and stiff person syndrome has been established. The drug also has no currently valid US authorizations in the compiled data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for metformin
- A targeted literature and trial search for stiff person syndrome and metformin, including the neuroimmunological rationale
- Confirmation of current US marketing status, since all listed authorizations are cancelled
- Route and formulation compatibility assessment for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


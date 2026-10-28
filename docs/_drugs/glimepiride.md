---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 753
evidence_level: L5
indication_count: 9
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-10-28
description: "Glimepiride: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Glimepiride
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

## Glimepiride: Classic stiff person syndrome
{: .text-alpha }

## One-Sentence Summary

Glimepiride is a sulfonylurea originally used to lower blood glucose in type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 6) |
| Number of NDAs | 6 (all ANDA, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, glimepiride is a sulfonylurea that closes KATP channels in pancreatic beta cells to stimulate insulin secretion. Its efficacy in type 2 diabetes is established.

Stiff person syndrome is an autoimmune neurological disorder, typically with anti-GAD65 antibodies that impair GABAergic signaling. No mechanistic link to glimepiride is established, and the drug has no known benefit for the neurological symptoms. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence: stiff person syndrome is commonly comorbid with type 1 diabetes, and the model may be picking up that association rather than a therapeutic rationale.

The same caution applies to the other predictions. Focal stiff limb syndrome received an identical score (0.9975), which suggests similarities the TxGNN model (deep learning) learned between related diseases rather than independent evidence. The remaining candidates are:

- **Opsismodysplasia**: possible link to insulin signaling, but speculative.
- **Thiamine-responsive dysfunction syndrome**: sulfonylureas may treat its diabetic component only, not the underlying disorder.
- **Localized lipodystrophies** (drug-induced, centrifugal, pressure-induced, idiopathic): no supporting evidence.
- **Pancreatic agenesis**: biologically implausible, since glimepiride needs residual beta cells to work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no relevant literature is available for the top prediction. The only publication retrieved across the candidate list was for pancreatic agenesis, and it is not relevant evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12720536](https://pubmed.ncbi.nlm.nih.gov/12720536/) | 2003 | Review / diagnostic imaging | European Journal of Endocrinology | Pitfalls in endosonographic imaging of suspected insulinomas; does not address glimepiride or pancreatic agenesis therapy |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202112 | Glimepiride (A-S Medication Solutions) | Tablet | Not available; status valid |
| ANDA077091 | Glimepiride (Dr. Reddy's Laboratories) | Tablet | Not available; status valid |
| ANDA202759 | Glimepiride (Aurobindo Pharma) | Tablet | Not available; status valid |
| ANDA077911 | Glimepiride (Carlsbad Technology) | Tablet | Not available; status valid |
| ANDA078181 | Glimepiride (Proficient Rx) | Tablet | Not available; status valid |

A sixth license (ANDA091220, Micro Labs Limited) is also cancelled.

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Most listed ones are Moderate, including:
  - Beta-agonists and sympathomimetics: phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol
  - Beta-blocker: acebutolol
  - Acid reducers: famotidine, ranitidine
  - NSAIDs: ibuprofen, ketorolac
  - Corticosteroid: hydrocortisone
  - Others: acetazolamide, acitretin, ethinylestradiol, albiglutide, hydrochlorothiazide, nitazoxanide, ethanol

  Topical hydrocortisone and topical alclometasone are Minor.
- **Disease associations flagged in the knowledge graph (not label text)**: kidney disease, liver disease, gallbladder disease, congestive heart failure, pituitary hormone deficiencies, hypogonadotropic hypogonadism, osteoporosis, and infectious disease, among others. These come from graph edges and should be verified against the package insert.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5), with no clinical trials or relevant literature. No plausible mechanism links glimepiride to stiff person syndrome, and the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. In addition, glimepiride is marketed in the US, with 6 valid licenses.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Evidence from preclinical or clinical studies on glimepiride in stiff person syndrome, or a clear mechanistic hypothesis connecting KATP channel inhibition or insulin signaling to GABAergic dysfunction
- Confirmation of current US market and licensing status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


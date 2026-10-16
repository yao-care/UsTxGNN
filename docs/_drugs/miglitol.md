---
layout: default
title: Miglitol
parent: Model Prediction Only (L5)
nav_order: 928
evidence_level: L5
indication_count: 10
monitor_inn: "MIGLITOL"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pancreatic agenesis", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "type 1 diabetes mellitus"]
---

# Miglitol
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

# Miglitol: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Miglitol is an oral alpha-glucosidase inhibitor, originally used to control blood sugar in type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but **0 clinical trials** and **0 publications** support this prediction, and no plausible mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active marketing authorization) |
| Number of NDAs | 1 (one ANDA, cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Miglitol is known to inhibit intestinal alpha-glucosidases, which delays carbohydrate digestion and lowers the rise in blood glucose after meals. It acts mainly in the gut.

**The prediction is not mechanistically convincing.** Focal stiff limb syndrome is a variant of stiff person syndrome spectrum disorders. These are autoimmune or neurological disorders of the central nervous system, often linked to anti-GAD antibodies. Miglitol's local action on carbohydrate digestion has no known effect on this pathology.

The high score most likely reflects network proximity in the knowledge graph. Diabetes and GAD-related autoimmunity are closely connected there, and this is not a true therapeutic signal. The same pattern appears for the neighbouring prediction, classic stiff person syndrome, which has an identical score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for focal stiff limb syndrome.

---

## Literature Evidence

Currently no related literature available for focal stiff limb syndrome.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA203965 (Westminster Pharmaceuticals, LLC; cancelled) | Miglitol | Tablet, coated (oral) | Not listed in the record |

---

## Safety Considerations

- **Contraindication associations (knowledge graph, not label text):** kidney disease, pyoureter, inflammatory bowel disease, infectious disease, ulcerative colitis, hypoglycemia, injury.
- **Drug Interactions:** 100 interactions were found. The main moderate-level ones include:
  - Sympathomimetics and bronchodilators: phenylephrine, pseudoephedrine, epinephrine, formoterol, salbutamol.
  - Corticosteroids: hydrocortisone, triamcinolone.
  - Hormones: ethinylestradiol, estradiol.
  - Other drugs: acetazolamide, hydrochlorothiazide, ethanol, alpelisib, aripiprazole, asenapine, asparaginase (E. coli and Erwinia).
- Minor-level interactions include ranitidine and topical corticosteroids (hydrocortisone, alclometasone).

Please refer to the package insert for full warnings and contraindications.

---

## Additional Note: Other Predictions for Miglitol

Of the 10 predicted indications, only **type 1 diabetes mellitus** (TxGNN score 99.60%) has any supporting evidence. The other eight, including lipodystrophy variants, pancreatic agenesis, opsismodysplasia and thiamine-responsive dysfunction syndrome, have no trials or literature and no credible mechanism.

For type 1 diabetes, miglitol acts as an adjunct to insulin to blunt after-meal glucose peaks.

| Source | Type | Key Findings |
|---------|------|---------|
| [NCT00213109](https://clinicaltrials.gov/study/NCT00213109) | Phase 3, Completed, open-label, enrollment not reported | Efficacy and safety of miglitol in type 1 diabetes patients treated with insulin |
| [24843410](https://pubmed.ncbi.nlm.nih.gov/24843410/) (2010) | Clinical study | Miglitol plus insulin combination in type 1 diabetes |
| [21869539](https://pubmed.ncbi.nlm.nih.gov/21869539/) (2011) | Clinical study, 11 patients | Miglitol with intensive insulin therapy; assessed glycemic control, hypoglycemia and incretin responses |
| [2060451](https://pubmed.ncbi.nlm.nih.gov/2060451/) (1991) | Clinical study | Effects on meal glucose tolerance and insulin timing |
| [2663321](https://pubmed.ncbi.nlm.nih.gov/2663321/) (1989) | Single-blind crossover, 13 patients | Reduced post-meal glucose area under the curve versus placebo |

The evidence is small and mostly dated. With only one open-label Phase 3 trial, it does not strictly meet the L1 criterion of at least two completed Phase 3 RCTs. If this drug is pursued, type 1 diabetes is the only realistic direction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication, focal stiff limb syndrome, has no clinical trials or publications, and no plausible mechanistic link to an intestinal alpha-glucosidase inhibitor. The prediction appears to be a knowledge-graph artifact. The only US authorization is cancelled, so the drug has no active US marketing authorization.

**To proceed, the following is needed:**
- Any clinical or preclinical evidence linking miglitol to stiff person spectrum disorders (none currently exists)
- Detailed mechanism of action data
- Full package insert warnings and contraindications
- If pursuing the better-supported type 1 diabetes direction, a re-evaluation with a controlled trial design and a plan for hypoglycemia and gastrointestinal monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


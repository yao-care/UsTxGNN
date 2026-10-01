---
layout: default
title: Empagliflozin
parent: Model Prediction Only (L5)
nav_order: 650
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Empagliflozin: From Type 2 Diabetes, Heart Failure and CKD to Classic Stiff Person Syndrome

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor marketed in the US as Jardiance, and the evidence pack describes it as used for adult type 2 diabetes, heart failure and chronic kidney disease.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but the prediction is supported by **0 clinical trials** and **0 publications**, so it currently rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | The US license records contain no indication text. The pack's rationale text describes use in type 2 diabetes, heart failure and CKD. |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.06% (model rank 20304) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 18 |
| Recommended Decision | Hold |

Two other predictions were generated for this drug, both also L5 and Hold:
- **Focal stiff limb syndrome**: score 99.06%.
- **Opsismodysplasia**: score 99.03%.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Empagliflozin is an SGLT2 inhibitor that blocks renal glucose reuptake. This is described in the pack's rationale text, not in the MOA field.

No direct mechanistic link to stiff person syndrome has been established. Classic stiff person syndrome is an autoimmune disorder of GABAergic neurotransmission, typically with anti-GAD65 antibodies. Any link would be indirect, for example through metabolic or anti-inflammatory effects, or through comorbid autoimmune diabetes. None of these is documented in the pack.

The same caution applies to the other two predictions:
- Focal stiff limb syndrome is a localized variant of the same disease spectrum. Its score is identical to classic stiff person syndrome, which suggests a shared knowledge-graph neighborhood rather than independent evidence.
- Opsismodysplasia is a rare pediatric skeletal dysplasia caused by loss of INPPL1 (SHIP2), which affects PI3K/AKT and insulin signaling. This offers a tenuous, unvalidated rationale for a glucose-lowering drug.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The 18 US licenses all fall under NDA204629. The table lists 5 of them. The record contains no approved-indication text, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA204629 | JARDIANCE | Film-coated tablet | A-S Medication Solutions |
| NDA204629 | Jardiance | Film-coated tablet | Boehringer Ingelheim Pharmaceuticals, Inc. |
| NDA204629 | Jardiance | Film-coated tablet | Aphena Pharma Solutions - Tennessee, LLC |
| NDA204629 | Jardiance | Film-coated tablet | Aphena Pharma Solutions - Tennessee, LLC |
| NDA204629 | Jardiance | Film-coated tablet | A-S Medication Solutions |

All forms are oral: film-coated tablet, extended-release tablet and tablet.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score (99.06%), with no clinical trials, no literature and no established mechanistic link. The disease pathophysiology (autoimmune, GABAergic) is far from the drug's SGLT2-inhibitor pharmacology. Package insert safety data is missing, so this cannot proceed to safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap).
- Mechanism of action data from DrugBank.
- Preclinical or mechanistic evidence linking SGLT2 inhibition to stiff person syndrome, for example through immune or metabolic pathways.
- A literature and trial re-check, including case reports in patients with stiff person syndrome who also have diabetes.
- Clarification of the original indication, since the license records have no indication text.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


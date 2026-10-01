---
layout: default
title: Nimodipine
parent: Model Prediction Only (L5)
nav_order: 967
evidence_level: L5
indication_count: 2
---

# Nimodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Nimodipine: From Subarachnoid Hemorrhage to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Nimodipine is an L-type calcium channel blocker. The Evidence Pack lists no approved indication text, but the drug is generally known for use after subarachnoid hemorrhage. The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**, but **0 clinical trials** and **0 publications** support this, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source data. Generally known use: subarachnoid hemorrhage. |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 license records (1 NDA listed twice, plus 3 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Nimodipine is a dihydropyridine L-type calcium channel blocker, and this class acts mainly on vascular smooth muscle.

The link to the new indication is weak. Homozygous familial hypercholesterolemia is caused by loss of LDL receptor function, which leaves LDL cholesterol very high. Calcium channel blockade has no established effect on this defect. A vascular or anti-atherosclerotic effect seen in preclinical models is possible, but it is speculative and would not correct the LDL problem. Effective treatments (statins, PCSK9 inhibitors, lomitapide, evinacumab, LDL apheresis) act through different pathways.

The high score (0.993) most likely reflects graph-based associations in the knowledge network rather than a demonstrated biological mechanism. The model's second prediction, nephrogenic syndrome of inappropriate antidiuresis (score 99.05%), is similarly unsupported. It is driven by AVPR2 gain-of-function mutations, and nimodipine has no established action on that receptor.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203340 | Nymalize (Azurity Pharmaceuticals) | Solution | Not listed in source data (two records) |
| ANDA216937 | Nimodipine (Camber Pharmaceuticals) | Solution | Not listed in source data |
| ANDA076740 | Nimodipine (Bionpharma) | Capsule, liquid filled | Not listed in source data |
| ANDA077811 | Nimodipine (Heritage / Avet Pharmaceuticals) | Capsule, liquid filled | Not listed in source data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score. There are no trials or publications, and there is no plausible mechanistic link between L-type calcium channel blockade and the LDL receptor defect. Established therapies already target the disease pathway directly.

**To proceed, the following is needed:**
- The approved indications and mechanism of action from the package insert and DrugBank
- The FDA package insert warnings and contraindications, needed for safety screening
- Preclinical or mechanistic evidence linking nimodipine to lipid metabolism or LDL receptor pathways
- Literature and trial searches on nimodipine in familial hypercholesterolemia
- Route compatibility and comparison against current standard therapies

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


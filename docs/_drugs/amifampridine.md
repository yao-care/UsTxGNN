---
layout: default
title: Amifampridine
parent: Model Prediction Only (L5)
nav_order: 324
evidence_level: L5
indication_count: 2
---

# Amifampridine
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

# Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma

## One-Sentence Summary

Amifampridine is marketed in the US as Firdapse tablets. The Evidence Pack contains no approved indication text, but the drug is generally known for Lambert-Eaton myasthenic syndrome. The TxGNN model predicts it may be effective for **glaucoma**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it remains a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (approved indication text is empty; Lambert-Eaton myasthenic syndrome is from general knowledge, not verified against the pack) |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Amifampridine is generally described as a voltage-gated potassium channel blocker. It prolongs presynaptic depolarization and increases acetylcholine release, which improves neuromuscular transmission.

That mechanism has no established link to intraocular pressure control or to protecting retinal ganglion cells, the main therapeutic goals in glaucoma. Any connection would be speculative. The high TxGNN score is a knowledge-graph output, not evidence, and the supplied data cannot verify the reasoning behind it.

A second prediction, acute intermittent porphyria (score 99.32%), is also prediction-only. Potassium channel blockade might at most act symptomatically on neuropathic weakness and would not address the underlying heme biosynthesis defect. Potassium channel blockers can also lower the seizure threshold, and seizures are a recognized complication of acute porphyric attacks. That would need specific safety review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208078 | Firdapse (Catalyst Pharmaceuticals, Inc.) | Tablet (oral) | Not listed in source data |

## Safety Considerations

Please refer to the package insert for safety information.

Amifampridine may lower the seizure threshold. This comes from the mechanism-based caution in the Evidence Pack's rationale for the porphyria prediction, not from label data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The glaucoma prediction is supported only by the model score, with no trials, no literature, and no plausible established mechanistic link. Evidence is at L5, and the package insert safety data has not been obtained.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, and the approved indication text
- A literature and preclinical search for potassium channel blockers in glaucoma or retinal ganglion cell neuroprotection
- Route compatibility assessment (oral tablet versus the routes glaucoma treatment would require)
- Specific seizure-risk review before any consideration of the porphyria prediction

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


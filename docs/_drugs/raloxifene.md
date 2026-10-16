---
layout: default
title: Raloxifene
parent: Model Prediction Only (L5)
nav_order: 1105
evidence_level: L5
indication_count: 4
monitor_inn: "Raloxifene"
predicted_indications: ["duodenal ulcer (disease)", "hypoalphalipoproteinemia", "duodenal obstruction", "duodenogastric reflux"]
last_modified_at: 2026-10-14
description: "Raloxifene: predicted new indication Duodenal ulcer (evidence level L5). Approved use: Postmenopausal osteoporosis / osteoporosis"
---

# Raloxifene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Raloxifene: From Postmenopausal Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Raloxifene is a selective estrogen receptor modulator (SERM), originally used to treat postmenopausal osteoporosis.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but **0 clinical trials** and **0 publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis / osteoporosis |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 7 (1 NDA and 6 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, raloxifene is a selective estrogen receptor modulator, and its efficacy in postmenopausal osteoporosis has been established. Whether it could apply to duodenal ulcer is unclear.

No mechanistic link is supported by the data compiled for this report. One speculative idea is that estrogen receptor effects might influence gastric or duodenal mucosal protection, but no retrieved evidence backs this. The high TxGNN score (0.997) is a knowledge-graph prediction only and should not be read as evidence of efficacy.

Other predicted indications show the same pattern:

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Hypoalphalipoproteinemia | 99.65% | Raloxifene modestly lowers LDL-C and total cholesterol, but has little documented HDL-raising effect. The link is speculative. |
| 3 | Duodenal obstruction | 99.64% | The condition is mostly structural or mechanical and unlikely to respond to a SERM. Probably a graph-proximity artifact. |
| 4 | Duodenogastric reflux | 99.59% | A motility and pyloric-function disorder with no documented role for estrogen receptor modulation. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020815 | Evista (Eli Lilly and Company) | Tablet | Not listed (cancelled) |
| ANDA078193 | Raloxifene Hydrochloride (Teva) | Tablet, film coated | Not listed (cancelled) |
| ANDA090842 | Raloxifene Hydrochloride (Cipla USA) | Tablet | Not listed (cancelled) |
| ANDA204310 | Raloxifene Hydrochloride (Aurobindo) | Tablet, film coated | Not listed (cancelled) |
| ANDA208206 | Raloxifene Hydrochloride (AvPAK) | Tablet, film coated | Not listed (cancelled) |

Two further cancelled ANDAs (ANDA211324 and ANDA206384) are not shown. All 7 records are oral dosage forms and all are cancelled.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these come from model graph edges, not package insert text): hypertension and hypertensive disorder, liver disease, gallbladder disease, atrial fibrillation, hypertriglyceridemia, thrombophlebitis, coronary artery disease, stroke and cerebrovascular disorders, cerebral infarction, transient ischemic attack, vertebrobasilar insufficiency, pulmonary embolism, retinal artery occlusion, thrombophilia, antiphospholipid syndrome, and impaired renal function. The theme is mainly thromboembolic and cardiovascular risk.
- **Drug Interactions**: The interaction search returned 100 records. None carry a severity level. The first 20 listed include calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, clotrimazole, morphine, metformin, omeprazole, lansoprazole, sucralfate, rosiglitazone, vancomycin, lactulose, triamcinolone, simvastatin, nystatin, nateglinide, scopolamine, and tetracycline. Clinical significance cannot be judged without severity grading.

Please refer to the package insert for full warnings and contraindications, as label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials, literature, or mechanistic rationale (Evidence Level L5). The drug has no currently valid US licenses, and the knowledge graph flags substantial thromboembolic and cardiovascular risk. The signals do not justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological link between estrogen receptor modulation and duodenal ulcer pathophysiology
- Preclinical or observational evidence in duodenal ulcer or related gastric mucosal models
- Package insert warnings and contraindications to complete the safety screening
- Severity grading for drug interactions, especially with agents commonly used in peptic ulcer disease (PPIs, sucralfate)
- Clarification of regulatory status, since all US licenses are cancelled, and a review of the route and dosing needed for the new indication
- A benefit-risk assessment in a population different from postmenopausal women, given the thromboembolic risk signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


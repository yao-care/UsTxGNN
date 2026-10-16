---
layout: default
title: Trolamine Salicylate
parent: Model Prediction Only (L5)
nav_order: 1267
evidence_level: L5
indication_count: 10
monitor_inn: "TROLAMINE SALICYLATE"
predicted_indications: ["exostosis", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "fibromyalgia", "inclusion body myositis", "exostoses, multiple,", "rheumatoid arthritis", "headache disorder", "gout"]
last_modified_at: 2026-10-14
description: "Trolamine Salicylate: predicted new indication Exostosis (evidence level L5). Approved use: Not stated in the data compiled for this report . The product names s…"
---

# Trolamine Salicylate
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

# Trolamine Salicylate: From Topical Pain Relief to Exostosis

## One-Sentence Summary

Trolamine salicylate is a topical salicylate used in over-the-counter pain relief creams. The TxGNN model predicts it may be effective for **exostosis**, with a very high computational score. However, there are currently **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the approved indication text of all three licenses is empty). The product names suggest topical pain and arthritis relief. |
| Predicted New Indication | Exostosis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, trolamine salicylate is a topical salicylate with cyclooxygenase (COX) inhibiting analgesic and anti-inflammatory activity, and it has been marketed in creams for local muscle and joint pain.

Exostosis is a structural bony outgrowth. There is no plausible mechanism by which a topical NSAID-like agent would alter it. At most, the drug could relieve associated local pain. The high TxGNN score is a computational, graph-based prediction with no supporting clinical or literature evidence, so the prediction is not considered mechanistically convincing.

Other predicted indications are more plausible on class-level reasoning, though they also lack any supporting evidence in the compiled data:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Tendinitis | 99.70% | L5 | Symptomatic relief is plausible through prostaglandin inhibition. Worth investigating as a research question. |
| 8 | Rheumatoid arthritis | 99.25% | L5 | Symptomatic pain relief in superficial joints is conceivable, not disease-modifying. Research question. |
| 5 | Fibromyalgia | 99.59% | L5 | Centrally mediated pain, so limited benefit expected. |
| 9 | Headache disorder | 99.23% | L5 | Limited systemic absorption from topical use. |
| 10 | Gout | 99.18% | L5 | No urate-lowering effect. |
| 3, 4, 6 | Idiopathic granulomatous myositis, myositis fibrosa, inclusion body myositis | 99.65%, 99.65%, 99.46% | L5 | No plausible disease-modifying role for a topical salicylate. |
| 7 | Multiple exostoses | 99.43% | L5 | Genetic skeletal disorder (EXT1/EXT2) unrelated to salicylate pharmacology. |

The identical scores for idiopathic granulomatous myositis and myositis fibrosa suggest a shared graph-based inference rather than disease-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication | Status |
|---------|------|------|-----------|------|
| 505G(a)(3) | MOBISYL | Cream | Not stated | Cancelled |
| M017 | Arthritis Relief | Cream | Not stated | Cancelled |
| part348 | Pain Relief Cream | Cream | Not stated | Cancelled |

All three licenses are single-ingredient products and all are cancelled. The drug is also recorded in spray form.

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found, and no contraindications were identified from the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (exostosis) rests only on a model score, with no clinical trials or literature and no plausible mechanistic link. In addition, all US licenses are cancelled and the safety label data are missing. Tendinitis and rheumatoid arthritis are more plausible symptomatic-relief directions but are also prediction-only at this stage.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- A literature and trial search for topical salicylates and NSAIDs in tendinopathy and inflammatory arthritis, as the more plausible alternatives
- Confirmation of the original approved indications and a review of why the licenses were cancelled
- Route compatibility assessment between the available topical forms and the intended use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


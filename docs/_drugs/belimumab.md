---
layout: default
title: Belimumab
parent: Model Prediction Only (L5)
nav_order: 440
evidence_level: L5
indication_count: 6
---

# Belimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Belimumab: From an Unspecified Original Indication to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab is a marketed biologic (a BLyS/BAFF inhibitor), but the Evidence Pack does not list its approved indication.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, with a very high graph score (99.96%).
Evidence is thin: **1 clinical trial** was retrieved, and it studied a different disease. There are **0 publications**, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 license entries (BLA125370 appears twice; BLA761043 once) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Belimumab inhibits BLyS (BAFF), which reduces B-cell survival and autoantibody production. Detailed mechanism-of-action data from DrugBank is not in the Evidence Pack, so this description comes from the mechanistic assessment in the pack.

The prediction is hard to justify mechanistically. Primary platelet release disorders are typically inherited or intrinsic platelet function defects, not B-cell-mediated diseases, so B-cell suppression has no clear therapeutic rationale. The very high TxGNN score is a graph-based signal with no supporting biology and is probably a knowledge-graph artifact.

The other five predicted indications are also weak. Only **fetal and neonatal alloimmune thrombocytopenia (FNAIT)** has a plausible link, because maternal IgG alloantibodies against fetal platelet antigens could in principle be reduced by BLyS inhibition. That link rests on mechanistic reasoning alone, and pregnancy safety data are limited. Belimumab is an IgG1 antibody that can cross the placenta.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Open-label mechanistic study of belimumab in anti-PLA2R-positive idiopathic membranous glomerulonephropathy. It does not test any platelet disorder and was likely matched by drug name only (relevance grade C). |

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125370 | BENLYSTA (GlaxoSmithKline LLC) | Injection, powder, lyophilized, for solution | Not provided |
| BLA761043 | BENLYSTA (GlaxoSmithKline LLC) | Solution | Not provided |

BLA125370 appears twice in the source data with the same dosage form.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trial or publication, and the only retrieved trial studied a different disease. The mechanism (B-cell/BLyS inhibition) does not fit a non-immune platelet function disorder, so the high score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening) and the approved indication text
- Detailed mechanism-of-action data from DrugBank
- Any evidence linking BLyS/B-cell pathways to primary platelet release disorders, such as case reports or immune-mediated subtypes
- If the team wants to pursue a platelet-related direction, FNAIT is the more plausible research question. It would need a dedicated literature review and a careful pregnancy safety assessment first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


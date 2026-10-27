---
layout: default
title: Brolucizumab
parent: Model Prediction Only (L5)
nav_order: 472
evidence_level: L5
indication_count: 4
monitor_inn: "BROLUCIZUMAB"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "esophageal varices with bleeding", "esophageal varices without bleeding", "exocrine pancreatic insufficiency"]
last_modified_at: 2026-10-14
description: "Brolucizumab: predicted new indication Mitochondrial oxidative phosphorylation disorder due to nuclear DNA a… (evidence level L5). Approved use: Macular degeneration"
---

# Brolucizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Brolucizumab: From Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies
{: .text-alpha }

## One-Sentence Summary

Brolucizumab is an anti-VEGF-A antibody fragment, originally used to treat macular degeneration.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Macular degeneration (the US license record contains no indication text) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA761125) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, brolucizumab is a single-chain antibody fragment (scFv) that targets VEGF-A. It is approved for neovascular age-related macular degeneration, where it is given by intravitreal injection.

No documented mechanistic link between VEGF-A inhibition and oxidative phosphorylation disorders caused by nuclear DNA anomalies was identified. The only conceivable connection is speculative, for example through VEGF-related retinal or vascular complications of mitochondrial disease. The very high TxGNN score is a model-derived output and is not supported by any trial or publication.

Three other predictions were also reviewed. All are L5 and Hold, with no trials or literature:

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Esophageal varices with bleeding | 99.12% | VEGF-driven angiogenesis in portal hypertension is biologically conceivable. However, intravitreal dosing gives low systemic exposure, and anti-VEGF agents carry hemorrhagic and thromboembolic concerns. Standard care is well established. |
| 3 | Esophageal varices without bleeding | 99.12% | The same speculative rationale applies. Prophylaxis already exists (non-selective beta-blockers, band ligation). |
| 4 | Exocrine pancreatic insufficiency | 99.07% | No plausible link to VEGF-A inhibition was found. The score may reflect graph-based artifacts. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761125 (cancelled) | BEOVU (Novartis Pharmaceuticals Corporation) | Injection, solution | Not listed in the compiled data |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from a computational knowledge graph, not label text): uveitis, iris disease, ciliary body disease, panuveitis, eye infectious disease, and conjunctivitis.

No drug interaction records were found. For other warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no clinical trials, no publications, and no identified mechanistic link. The US license is cancelled, and the product is an intravitreal agent with limited systemic exposure, which makes the predicted systemic indications doubtful.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- A biological rationale linking VEGF-A inhibition to nuclear-DNA-driven oxidative phosphorylation disorders
- Preclinical or clinical evidence in the predicted indication
- An assessment of route and formulation compatibility, since the current product is intravitreal only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Atracurium Besylate
parent: Model Prediction Only (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
monitor_inn: "ATRACURIUM BESYLATE"
predicted_indications: ["preeclampsia", "cauda equina syndrome", "blepharospasm", "migraine disorder", "obsolete neurogenic bladder (disease)", "thrombotic disease", "migraine with brainstem aura", "severe pre-eclampsia", "mild pre-eclampsia", "irritable bowel syndrome"]
last_modified_at: 2026-11-24
description: "Atracurium Besylate: predicted new indication preeclampsia (evidence level L5). In the US: 23 FDA applications (6 active)"
---

# Atracurium Besylate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Atracurium Besylate: neuromuscular blocker (nicotinic receptor antagonist) → preeclampsia
{: .text-alpha }

## One-Sentence Summary

Atracurium besylate is a non-depolarizing neuromuscular blocking agent given by injection.
The TxGNN model predicts it may be relevant to **preeclampsia**, but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | preeclampsia |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 6 of 23) |
| Number of FDA Applications | 23 (active: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the FDA-approved prescribing information for atracurium besylate: "Atracurium besylate is a nondepolarizing skeletal muscle relaxant. Nondepolarizing agents antagonize the neurotransmitter action of acetylcholine by binding competitively with cholinergic receptor sites on the motor end-plate." ([DailyMed: atracurium besylate prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=efe90ee2-fe9e-421f-9e54-2961085d3b12), label version 2024-12-04; accessed 2026-11-19.) From general pharmacology, atracurium is a non-depolarizing neuromuscular blocker that acts on nicotinic acetylcholine receptors at the motor end plate and is eliminated rapidly by Hofmann degradation.

There is no established mechanistic link between this action and the pathophysiology of preeclampsia, which involves placental dysfunction, endothelial injury and angiogenic imbalance. Muscle relaxants are used during general anesthesia for cesarean delivery in women with preeclampsia, but that is a procedural use, not treatment of the disease. The high score (0.9997) is a model output only. It may partly reflect the proximity of magnesium sulfate, the standard preeclampsia therapy, which potentiates neuromuscular blockade. The prediction should therefore be regarded as hypothesis-generating and not mechanistically supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The compiled licence records list six single-ingredient ANDA injection (solution) products from AuroMedics Pharma LLC, Meitheal Pharmaceuticals Inc. and Hospira, Inc. No approved-indication text is recorded for them in the local data. Market status is recorded as marketed.

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA074900 | ATRACURIUM BESYLATE PRESERVATIVE FREE | HIKMA | Injectable; injection | Valid |
| ANDA074901 | ATRACURIUM BESYLATE | HIKMA | Injectable; injection | Valid |
| ANDA090761 | ATRACURIUM BESYLATE | HOSPIRA INC | Injectable; injection | Valid |
| ANDA090782 | ATRACURIUM BESYLATE PRESERVATIVE FREE | HOSPIRA INC | Injectable; injection | Valid |
| ANDA091488 | ATRACURIUM BESYLATE PRESERVATIVE FREE | MEITHEAL | Injectable; injection | Valid |

Showing 5 of 23 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug-interaction records were available in the data compiled for this report. As general pharmacological context, concurrent magnesium sulfate can prolong neuromuscular blockade, which is relevant in the preeclampsia setting.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and no plausible disease-modifying mechanism is identified for preeclampsia. Use of the drug in this setting is limited to anesthesia during delivery.

**To proceed, the following is needed:**
- Any clinical or preclinical study that directly examines atracurium in preeclampsia
- Mechanism-of-action data and a defined biological rationale for the disease
- FDA package insert warnings and contraindications, particularly regarding magnesium sulfate and use in pregnancy
- Evaluation of route and dosing suitability, given the drug's short duration of action and injectable-only forms

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for atracurium is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: atracurium besylate prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=efe90ee2-fe9e-421f-9e54-2961085d3b12) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


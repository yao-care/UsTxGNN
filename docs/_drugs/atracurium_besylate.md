---
layout: default
title: Atracurium Besylate
parent: Model Prediction Only (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
monitor_inn: "ATRACURIUM BESYLATE"
predicted_indications: ["preeclampsia", "cauda equina syndrome", "blepharospasm", "migraine disorder", "obsolete neurogenic bladder (disease)", "thrombotic disease", "migraine with brainstem aura", "severe pre-eclampsia", "mild pre-eclampsia", "irritable bowel syndrome"]
last_modified_at: 2026-10-14
description: "Atracurium Besylate: predicted new indication Preeclampsia (evidence level L5). Approved use: Not available in the compiled US license records (the indication text…"
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Atracurium Besylate: From Neuromuscular Blockade to Preeclampsia

## One-Sentence Summary

Atracurium besylate is a non-depolarizing neuromuscular blocking agent given by injection, used as a skeletal muscle relaxant in anesthesia.
The TxGNN model predicts it may be effective for **preeclampsia**,
but **no clinical trials and no publications** currently support this prediction. It is a knowledge-graph signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled US license records (the indication text is empty). Known pharmacology points to use as a skeletal muscle relaxant during anesthesia. |
| Predicted New Indication | Preeclampsia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active licenses) |
| Number of NDAs | 6 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, atracurium is a non-depolarizing neuromuscular blocker that acts on nicotinic acetylcholine receptors at the motor end plate. It is short-acting and cleared by Hofmann elimination.

There is no established mechanistic link between this action and preeclampsia, which involves placental dysfunction, endothelial injury, and angiogenic imbalance. Muscle relaxants are used in general anesthesia for cesarean delivery in women with preeclampsia, but that is a procedural use, not treatment of the disease.

The high score (0.9997) most likely reflects graph proximity. Magnesium sulfate, the standard preeclampsia therapy, potentiates neuromuscular blockade and may explain why the two sit close together in the knowledge graph. The same reasoning applies to the related nodes "severe pre-eclampsia" and "mild pre-eclampsia", which are largely redundant with this prediction.

Other top predictions fare no better. Blepharospasm is biologically plausible in principle, but atracurium's short duration makes it unsuitable for chronic focal injection, and botulinum toxin is the established therapy. Cauda equina syndrome, migraine (including migraine with brainstem aura), obsolete neurogenic bladder, thrombotic disease, and irritable bowel syndrome have no plausible mechanistic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206010 (AuroMedics Pharma LLC) | Atracurium Besylate | Injection, solution | Not available (cancelled) |
| ANDA206011 (AuroMedics Pharma LLC) | Atracurium Besylate | Injection, solution | Not available (cancelled) |
| ANDA091489 (Meitheal Pharmaceuticals Inc.) | Atracurium Besylate | Injection, solution | Not available (cancelled) |
| ANDA090782 (Hospira, Inc.) | Atracurium Besylate | Injection, solution | Not available (cancelled) |
| ANDA091488 (Meitheal Pharmaceuticals Inc.) | Atracurium Besylate | Injection, solution | Not available (cancelled) |

One additional cancelled ANDA is on record (ANDA090761, Hospira, Inc.). All six licenses are for single-ingredient injectable products, and none is currently valid.

## Safety Considerations

Please refer to the package insert for safety information.

Based on the rationale compiled for this report, atracurium's interaction with magnesium sulfate (prolonged neuromuscular blockade) is relevant in the preeclampsia setting. Its histamine-releasing properties are also a concern. No formal drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no trials, no literature, and no plausible disease-modifying mechanism for preeclampsia or any other top-ranked indication. All US licenses are cancelled, and the package-insert safety information is missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence showing a disease-modifying effect in the predicted indication
- Route and formulation compatibility assessment (the current injectable, short-acting form is unsuited to chronic use)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


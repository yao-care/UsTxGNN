---
layout: default
title: Dexmedetomidine
parent: Model Prediction Only (L5)
nav_order: 594
evidence_level: L5
indication_count: 5
---

# Dexmedetomidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Dexmedetomidine: From Procedural and ICU Sedation to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Dexmedetomidine is a central alpha-2 adrenergic agonist, used for sedation in ICU and procedural settings.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license records (sedation in ICU and procedural settings, per trial descriptions in the evidence pack) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (total licenses, including ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on the analysis, dexmedetomidine is a central alpha-2 adrenergic agonist with reported effects on vasopressin release and diuresis. This is the only rationale for linking it to an antidiuresis disorder.

That link is weak. NSIAD is caused by gain-of-function variants in the *AVPR2* gene. These variants activate the vasopressin V2 receptor independently of circulating vasopressin. A drug acting upstream in the central nervous system is therefore unlikely to help.

The high score (0.996) reflects graph proximity in the knowledge graph. No clinical or literature evidence supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212791 | Dexmedetomidine Hydrochloride (Slayback Pharma LLC) | Injection | Not listed in source data |
| NDA021038 | Precedex (Hospira, Inc.) | Injection, solution | Not listed in source data |
| NDA021038 | Precedex (Henry Schein, Inc.) | Injection, solution, concentrate | Not listed in source data |
| NDA021038 | Precedex (Hospira, Inc.) | Injection, solution | Not listed in source data |
| ANDA204843 | Dexmedetomidine (ProPharma Distribution) | Injection, solution | Not listed in source data |

All listed products are injectables.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (L5). The proposed mechanism is also implausible: NSIAD is driven by V2 receptor gain-of-function, so central alpha-2 agonism is unlikely to help.

**To proceed, the following is needed:**
- Mechanism-of-action data (DrugBank) and a mechanistic analysis specific to the AVPR2 pathway
- FDA package insert warnings and contraindications, which are currently missing and block safety screening
- Any preclinical or clinical signal for NSIAD, since none currently exists

**Note on other predictions for this drug:** the pack's evidence is concentrated in **headache disorder** (rank 4, score 99.30%, L1, "Research Question"). It includes a Phase 3 RCT of nebulized dexmedetomidine versus neostigmine/atropine, plus one systematic review and meta-analysis. That evidence covers post-dural puncture headache only, using an off-label nebulized route, and does not generalize to other headache types. It would be a better candidate to pursue than NSIAD.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Benzonatate
parent: Model Prediction Only (L5)
nav_order: 449
evidence_level: L5
indication_count: 2
monitor_inn: "BENZONATATE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)"]
last_modified_at: 2026-10-14
description: "Benzonatate: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not listed in the US license data (benzonatate is generally known as…"
---

# Benzonatate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Benzonatate: From Cough Suppression to Cauda Equina Syndrome

## One-Sentence Summary

Benzonatate is an oral antitussive (cough suppressant) with a local anesthetic-like action, but the data compiled for this report do not include an approved indication text.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, with a very high score, but **0 clinical trials** and **0 publications** currently support this direction.
This is a model-only prediction (evidence level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US license data (benzonatate is generally known as a cough suppressant) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 8 (all generic ANDA applications, none currently valid) |
| Recommended Decision | Hold |

A second prediction was also generated: **obsolete neurogenic bladder (disease)**, with a score of 99.39% and the same evidence level (L5) and decision (Hold). It is discussed below.

## Why is This Prediction Reasonable?

Detailed mechanism of action data for benzonatate is not available in the data compiled for this report. Based on general pharmacological knowledge, benzonatate is a peripherally acting antitussive that numbs stretch receptors in the respiratory tract through local anesthetic-like sodium channel blockade. It is structurally related to tetracaine and procaine.

A plausible but unverified link to cauda equina syndrome is sodium channel modulation of neuropathic pain or of bladder and sensory dysfunction. However, cauda equina syndrome is primarily a surgical emergency caused by mechanical compression of the nerve roots, and treatment centers on decompression. A symptomatic local-anesthetic-type drug is unlikely to address the underlying pathology. The very high TxGNN score is a computational prediction only and has not been validated clinically.

For the second prediction, neurogenic bladder, the theoretical rationale is that suppressing sensory afferent signaling might reduce bladder afferent hyperexcitability, similar to intravesical local anesthetics. This is speculative. The disease term is flagged as obsolete in the ontology and should be mapped to a current term (e.g., neurogenic lower urinary tract dysfunction) before any further evaluation. Established therapies (antimuscarinics, beta-3 agonists, intermittent catheterization, onabotulinumtoxinA) set a high bar for any new candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040682 | Benzonatate (Redpharm Drug) | Capsule, liquid filled | Not specified (cancelled) |
| ANDA202765 | Benzonatate (RemedyRepack Inc.) | Capsule | Not specified (cancelled) |
| ANDA081297 | Benzonatate (Golden State Medical Supply) | Capsule | Not specified (cancelled) |
| ANDA040597 | Benzonatate (A-S Medication Solutions) | Capsule | Not specified (cancelled) |
| ANDA040749 | Benzonatate (Proficient Rx LP) | Capsule | Not specified (cancelled) |

Eight licenses in total are on record, all cancelled and all for single-ingredient oral products. The table shows the first five.

## Safety Considerations

- **Drug Interactions**: One interaction was identified, with **tizanidine** (Moderate severity).
- **General caution**: Systemic benzonatate is associated with CNS effects and overdose toxicity, especially in children.

Please refer to the package insert for full warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on a model score alone, with no clinical trials, no literature, and no mechanism data. The proposed targets (a mechanical compression syndrome and an obsolete disease term) have weak mechanistic fit. All US licenses are cancelled, which further limits practical feasibility.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently blocking for safety screening)
- Mechanism of action data from DrugBank
- Mapping of "obsolete neurogenic bladder" to a current disease term
- Preclinical or mechanistic evidence supporting sodium channel modulation in the proposed conditions
- Route compatibility assessment (oral capsule versus the needs of the target conditions)
- Assessment of whether any valid marketed product exists, given that all licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Tetracaine
parent: Model Prediction Only (L5)
nav_order: 1218
evidence_level: L5
indication_count: 9
---

# Tetracaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Tetracaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Tetracaine is a sodium-channel-blocking local anesthetic, marketed in the US as eye drops, topical gel or cream, and injection.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans** (a late-stage, Borrelia-driven skin atrophy), but there are **0 clinical trials** and **0 publications** supporting this. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (the approved indication text is blank in the US label data) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tetracaine is a local anesthetic that blocks sodium channels, and its efficacy for numbing the eye, skin and spinal region is well established.

Acrodermatitis chronica atrophicans is a chronic skin atrophy caused by Borrelia infection. No plausible link between sodium-channel blockade and this disease was identified. The very high score (99.93%) most likely reflects patterns in the knowledge graph rather than a real therapeutic relationship.

Route compatibility and similarity to the original indication have not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The approved indication text is blank for all listed authorizations. Five of the 14 are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA208135 | Tetracaine Hydrochloride | Solution | Alcon Laboratories, Inc. |
| ANDA217227 | Tetracaine Hydrochloride | Solution | Somerset Therapeutics, LLC |
| M017 | BLT 3 | Ointment | Centura Pharmaceuticals Inc |
| M017 | Tetracaine | Gel | Bellus Medical, LLC |
| NDA210821 | Tetracaine Hydrochloride | Solution/Drops | Bausch & Lomb Americas Inc. |

## Safety Considerations

- **Neurotoxicity with intrathecal use**: The literature retrieved for other predicted indications includes several case reports of cauda equina syndrome after spinal tetracaine. The proposed mechanisms are high local concentration and maldistribution in the subarachnoid space.

Please refer to the package insert for all other safety information (warnings, contraindications, interactions).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no plausible mechanism. Standard treatment of this Borrelia-driven condition is not related to local anesthesia.

Other predicted indications were also reviewed. None supports advancing:
- **Acne keloid**: The one completed Phase 4 RCT (NCT02372786, n=30) tested lidocaine/tetracaine cream for pain control during laser treatment. That is procedural analgesia, not disease treatment.
- **Cauda equina syndrome**: All 9 publications describe it as an adverse outcome of local anesthetics, so it is a harm signal, not a therapeutic one.

**To proceed, the following is needed:**
- The US package insert (warnings and contraindications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- Any experimental or clinical evidence connecting tetracaine to Borrelia-related skin atrophy, without which the candidate should not advance
- Route compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


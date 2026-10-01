---
layout: default
title: Prilocaine
parent: Model Prediction Only (L5)
nav_order: 1081
evidence_level: L5
indication_count: 10
---

# Prilocaine
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

# Prilocaine: From Local Anesthesia to Papillary Conjunctivitis

## One-Sentence Summary

Prilocaine is an amide local anesthetic, marketed in the US as a dental injection (Citanest Plain).
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.
Among the top 10 predictions, **neuralgia** has the most supporting evidence (see Conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (inferred from drug class and product; no indication text in the label data) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (listed as ANDA079235) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Prilocaine is an amide local anesthetic that blocks voltage-gated sodium channels. Detailed mechanism-of-action data is not available in the source record beyond this class-level description.

No mechanism linking sodium channel blockade to the pathology of papillary conjunctivitis (allergic or mechanical) is evident. The original indication, nerve conduction block for anesthesia, is unrelated to the inflammatory and allergic nature of this eye condition.

The high TxGNN score reflects knowledge-graph proximity only. No trials or literature were retrieved, so the prediction is currently unsupported by any independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA079235 | Citanest Plain (Dentsply Pharmaceutical Inc.) | Injection, solution | Not stated in the available data |

---

## Safety Considerations

Package insert warnings and contraindications were not retrieved, and no drug interactions were found in the queried data. Please refer to the package insert for safety information.

Literature retrieved for other predicted indications, mostly on the lidocaine/prilocaine combination (EMLA), notes methemoglobinemia, contact allergy, and higher systemic absorption through compromised skin. These are relevant to any repurposing plan.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanism, so it rests on the model score alone (L5). The other top 10 predictions are also weak, except neuralgia (rank 5, L3): small clinical reports and a Phase 2 study of topical lidocaine/prilocaine cream in postherpetic neuralgia exist. That evidence cannot separate prilocaine's own contribution from lidocaine's.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Any direct evidence for ocular use, or a decision to redirect evaluation to neuralgia, where a formal review of the EMLA/PHN evidence would be the logical next step
- A methemoglobinemia risk assessment for any repeated or large-area topical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


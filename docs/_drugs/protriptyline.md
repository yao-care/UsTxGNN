---
layout: default
title: Protriptyline
parent: 僅模型預測 (L5)
nav_order: 1096
evidence_level: L5
indication_count: 5
---

# Protriptyline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Protriptyline: From Tricyclic Antidepressant to Attention-Deficit Hyperactivity Disorder, Inattentive Type

## One-Sentence Summary

> Protriptyline is a tricyclic antidepressant (TCA); its original indication text and detailed mechanism of action are not available in this evidence pack.
> The TxGNN model predicts it may be effective for **Attention-Deficit Hyperactivity Disorder, Inattentive Type**,
> with **0 clinical trials** and **0 publications** directly supporting this specific subtype — evidence is currently mechanistic/extrapolated only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in source data (drug class noted as Tricyclic Antidepressant, TCA) |
| Predicted New Indication | Attention-Deficit Hyperactivity Disorder, Inattentive Type |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap). Based on the mechanistic rationale provided, Protriptyline is a tricyclic antidepressant (TCA) that primarily inhibits norepinephrine (NE) reuptake with minimal serotonergic activity, giving it a pharmacological profile similar to desipramine and nortriptyline.

NE signaling is known to regulate prefrontal executive function and attention. TCAs with this profile have historically been used as second-line options for ADHD, particularly in patients with poor stimulant response or comorbid tics, and have also shown mild alerting/activating effects (historically used in narcolepsy). This gives biological plausibility to the TxGNN prediction for the inattentive ADHD subtype.

However, this specific mechanistic link has not yet been tested directly: no clinical trials or literature target the inattentive subtype specifically. A related, lower-ranked prediction in this evidence pack — general ADHD (not the inattentive subtype) — is supported by one retrospective naturalistic cohort study (PMID 8936915, tier 2 evidence), which lends indirect support to the drug class's plausibility for attention-related symptoms, but does not directly validate the inattentive-subtype prediction shown here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this specific prediction (inattentive-type ADHD).

*Note: A related but distinct prediction in this evidence pack — general ADHD — is supported by one retrospective naturalistic study (PMID 8936915, Wilens et al., 1996, J Am Acad Child Adolesc Psychiatry), evaluating protriptyline in children/adolescents with ADHD. This does not directly confirm efficacy for the inattentive subtype specifically.*

## US Market Information

No marketing authorization records are available. Per regulatory data, this drug is currently **not marketed** (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN prediction score is very high (99.95%), there is no direct clinical trial or literature evidence for this specific ADHD subtype, and the mechanistic rationale is extrapolated rather than confirmed. Critical safety data (TFDA warnings/contraindications) is also flagged as a **blocking** gap, preventing any S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (blocking gap — required before any safety assessment)
- Confirmed mechanism of action data via DrugBank
- Subtype-specific clinical evidence (trials or literature) for inattentive-type ADHD, rather than relying on general ADHD extrapolation
- Expert/ontology review to confirm the "inattentive type" disease mapping is clinically meaningful and distinct from general ADHD in this context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


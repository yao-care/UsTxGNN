---
layout: default
title: Propylhexedrine
parent: Model Prediction Only (L5)
nav_order: 1094
evidence_level: L5
indication_count: 10
---

# Propylhexedrine
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

# Propylhexedrine: From an Inhaled Sympathomimetic to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Propylhexedrine is a volatile alkylamine sympathomimetic marketed in the US as an inhalant (BENZEDREX). The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but **no clinical trials and no publications** currently support this direction. The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license record (product is an inhalant) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, propylhexedrine is a volatile alkylamine sympathomimetic that is structurally related to amphetamine-type agents. A noradrenergic or dopaminergic rationale for ADHD is therefore conceivable, since drugs acting on those systems are established ADHD treatments.

This link is speculative. The record has no MOA data, no approved indication text, and no similarity analysis to the original use. Route compatibility is also unassessed: the only marketed form is an inhalant, and the record does not say whether an inhaled product could deliver a systemic CNS effect.

Abuse and misuse potential is a safety concern for any CNS indication.

The other top-ranked predictions are weaker or implausible:
- **Migraine disorder and its subtypes:** The vasoconstrictor rationale is unverified. Sympathomimetics can provoke headache or raise blood pressure, so the direction of effect is uncertain.
- **Erectile dysfunction and Tourette syndrome:** Sympathomimetic activity is likely unfavorable for both. Sympathetic tone promotes detumescence, and stimulant-like agents can exacerbate tics.
- **Faciodigitogenital syndrome, atrophoderma vermiculata and ulerythema ophryogenesis:** These rare genetic or skin conditions have no plausible pharmacological link and are likely knowledge-graph artifacts.
- **Trichotillomania:** This is a possible neuropsychiatric neighbor of the ADHD prediction, with no direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the ADHD prediction.

The only literature retrieved in the record (20 records, 10 shown) belongs to the lower-ranked migraine-susceptibility prediction. It covers epilepsy-migraine shared genetics and mechanisms and never mentions propylhexedrine, so it provides no drug-specific support for any indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M012 | BENZEDREX (BF Ascher and Co Inc) | Inhalant | Not listed in the record |

## Safety Considerations

- **Drug Interactions:** The interaction query returned no results.
- **Misuse potential:** Abuse and misuse of this drug are a safety concern for any CNS indication.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD prediction has a high model score (99.97%) but is at evidence level L5, with no trials, no literature, no MOA data, and a stated abuse and misuse concern. The other top predictions are unsupported or implausible.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications. Their absence blocks safety screening.
- Mechanism of action data (for example, from DrugBank) to test the noradrenergic or dopaminergic hypothesis.
- A route-compatibility assessment, since only an inhalant form is marketed.
- A targeted literature and trial search on propylhexedrine in ADHD, including preclinical data.
- An abuse and misuse risk assessment before any CNS indication is considered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


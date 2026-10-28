---
layout: default
title: Methohexital
parent: Model Prediction Only (L5)
nav_order: 910
evidence_level: L5
indication_count: 5
monitor_inn: "METHOHEXITAL"
predicted_indications: ["insomnia (disease)", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "migraine with brainstem aura", "headache disorder"]
last_modified_at: 2026-10-28
description: "Methohexital: predicted new indication Insomnia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Methohexital
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Methohexital: Insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Methohexital is an ultra-short-acting barbiturate anesthetic, but the data compiled for this report contain no approved indication text for it.
The TxGNN model predicts it may be effective for **insomnia**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction with no direct clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, methohexital is an ultra-short-acting barbiturate that enhances GABA-A receptor activity, producing sedation and hypnosis. This gives a plausible rationale for sleep induction.

There are strong practical reasons to doubt the prediction. Barbiturates are not used for chronic insomnia because of tolerance, dependence, a narrow therapeutic index, and respiratory depression. Methohexital also redistributes rapidly, so its duration of action is very short. The high score (0.9988) is a model output only, with no supporting trials or literature.

The other top predictions fare no better:
- **Nephrogenic syndrome of inappropriate antidiuresis (0.9980)**: no plausible mechanistic link. The condition stems from gain-of-function variants in AVPR2 or GNAS, which are unrelated to GABA-A modulation. This is likely a TxGNN model (deep learning) artifact.
- **Migraine disorder (0.9954)**, **migraine with brainstem aura (0.9946)** and **headache disorder (0.9912)**: only indirect literature, in which methohexital appears as an ECT anesthetic and headache appears as a peri-procedural or adverse outcome.

## Clinical Trial Evidence

Currently no related clinical trials registered for insomnia.

## Literature Evidence

No literature is available for insomnia. The literature below relates to the lower-ranked migraine and headache predictions and is indirect only. None of it shows a therapeutic effect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31425262](https://pubmed.ncbi.nlm.nih.gov/31425262/) | 2020 | Systematic review | Anesthesia and Analgesia | Anesthetic considerations for ECT in children; methohexital appears as an anesthetic agent |
| [8528666](https://pubmed.ncbi.nlm.nih.gov/8528666/) | 1995 | Case report | Convulsive Therapy | Recurrent migraine after ECT; attacks stopped after switching from methohexital to propofol because of methohexital intolerance |
| [8442962](https://pubmed.ncbi.nlm.nih.gov/8442962/) | 1993 | Clinical study | Journal of Clinical Anesthesia | Effect of two atracurium doses on convulsion modification in monitored ECT |
| [14309941](https://pubmed.ncbi.nlm.nih.gov/14309941/) | 1965 | Historical clinical article | Wiener Klinische Wochenschrift | Article on vascular headache treatment (no abstract; relevance to methohexital unconfirmed) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA215488 (cancelled) | Methohexital Sodium | Injection | Not stated |
| NDA011559 (cancelled) | Brevital Sodium | Injection, powder, lyophilized, for solution | Not stated |

## Safety Considerations

- **Drug Interactions**: 22 interactions were recorded. The major ones are:
  - **Major**: ethanol, warfarin
  - **Moderate** (examples): morphine, hydrocodone, codeine, theophylline, aminophylline, chloramphenicol, doxepin, doxycycline, cyclosporine, methylene blue, griseofulvin, aldesleukin, ozanimod
  - **Minor**: pyridoxine, cimetidine, promethazine, mitotane
- **Knowledge-graph contraindication signals** (from the model's knowledge graph, not label text): liver failure, epilepsy, chronic obstructive pulmonary disease, porphyria and other porphyrin metabolism disorders, kidney disease, asthma, hypotensive disorder, anemia, and morbid obesity.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction rests on model score alone, with no trials or literature. Barbiturates are poorly suited to chronic insomnia because of dependence, respiratory depression, and a very short duration of action. In addition, no US license for methohexital is currently valid, and label safety information is missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (required for safety screening)
- Mechanism of action data
- A mechanistic and clinical rationale for insomnia, including comparison with established hypnotics
- Any clinical or preclinical studies of methohexital for sleep disorders
- Clarification of the original approved indication and the cancelled license status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Camphor
parent: Model Prediction Only (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
monitor_inn: "CAMPHOR"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "erectile dysfunction (disease)", "pulmonary hypertension", "migraine with or without aura, susceptibility to", "kyphoscoliotic heart disease", "ulerythema ophryogenesis", "Raynaud disease", "atrophoderma vermiculata", "Tourette syndrome"]
last_modified_at: 2026-10-14
description: "Camphor: predicted new indication Migraine disorder (evidence level L5). Approved use: Not specified in the available regulatory data"
---

# Camphor
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

# Camphor: From an Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

Camphor is a topical counter-irritant found in over-the-counter salves, vapor rubs, lip balms and ointments, and the data compiled for this report do not list a specific approved indication for it.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only **3 indirect publications** (case reports and a case series), so this remains a computational hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available regulatory data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 (preclinical or mechanistic signals only; no clinical trials) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on general pharmacology, camphor is a modulator of TRPM8 and TRPV1 channels with topical counter-irritant and cooling effects. These channels are involved in sensory and pain signaling, so a link to trigeminovascular pain pathways is plausible.

The relationship between the original use and migraine is therefore indirect. Camphor has been used topically for minor pain and irritation, and migraine is a pain disorder. However, topical counter-irritation and migraine pathophysiology are quite different, and the literature retrieved here does not establish a direct connection.

The very high TxGNN score is a computational prediction only. Other predictions on the list (such as pulmonary hypertension) appear to be driven by name-matching artifacts: "CAMPHOR" is also the acronym of a pulmonary hypertension questionnaire. This calls for caution in interpreting the scores.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case series | Headache | Five cases of cluster headache linked to toothpastes containing pro-convulsant essential oils; this suggests a possible trigger, not a treatment |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case report | BMJ Case Reports | Two cases of cluster headache temporally related to toothpastes containing camphor and eucalyptus oils |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Review | Z Kinder Jugendpsychiatr Psychother | Historical review of neuropsychopharmacotherapy in children in the 1940s and 50s; not specific to migraine |

A related lead was found under the predicted indication "migraine with or without aura, susceptibility to": a 2026 preclinical animal study ([PMID 42849823](https://pubmed.ncbi.nlm.nih.gov/42849823/)) reports that natural (+)-camphor alleviated reserpine-induced migraine with cerebral vasospasm via the p38β MAPK/ATF2 pathway. This is the most direct mechanistic signal but has not been replicated, and no human data exist.

The retrieved literature does not support efficacy in migraine. The human reports describe essential oils as possible headache triggers.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA nan (cancelled) | Owell Naturals Draw Salve with Camphor 2.0 oz. | Salve | Not specified |
| M012 (cancelled) | Quality Choice Vapor Steam | Liquid | Not specified |
| M017 (cancelled) | 365 Medicated Lip Balm | Stick | Not specified |
| part341 (cancelled) | Discount Drug Mart Value Vapor Steam | Liquid | Not specified |
| part348 (cancelled) | Cirlutone | Ointment | Not specified |

All five listed authorizations are cancelled, and none is currently valid.

## Safety Considerations

- **Drug Interactions**: No interaction records were found.
- **Toxicity signals from the literature**: Systemic camphor is associated with neurotoxicity and seizure risk, and pro-convulsant essential oils may worsen migraine. An oral acute toxicity study in rats (edible camphor) also reported oxidative stress and tissue histopathological changes.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests on a high model score, one unreplicated animal study and indirect case reports that point toward camphor as a possible headache trigger rather than a treatment. There are no clinical trials, no confirmed mechanism, and no currently valid US licenses.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- Replication of the preclinical migraine findings, and a clear TRPM8/TRPV1 mechanistic rationale specific to migraine
- Assessment of route and formulation compatibility (topical vs. systemic exposure) with a defined safety margin
- Human clinical evidence, starting with an exploratory study, after the safety review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


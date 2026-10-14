---
layout: default
title: Chlorzoxazone
parent: Model Prediction Only (L5)
nav_order: 525
evidence_level: L5
indication_count: 9
---

# Chlorzoxazone
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

# Chlorzoxazone: From Muscle Relaxation (Original Indication Not Recorded) to Migraine Disorder

## One-Sentence Summary

Chlorzoxazone is a centrally acting skeletal muscle relaxant, but the data compiled for this report contain no recorded approved indication text.
The TxGNN model predicts it may be effective for **migraine disorder**, with a very high score (99.73%).
However, there are **0 clinical trials** and only **3 indirect publications** (none migraine-specific), so the prediction currently rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no indication text in the compiled license records) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 (all ANDA generic applications, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Chlorzoxazone is known as a skeletal muscle relaxant, and it is also known to activate Ca²⁺-dependent K⁺ channels (SK/IK/BK).

The only mechanistic thread is indirect. A 2012 mouse study of a CaV2.1 (CACNA1A) mutation showed that Ca²⁺-dependent K⁺-channel activators alleviated cerebellar ataxia. CACNA1A mutations are also linked to familial hemiplegic migraine, so channelopathy biology could connect chlorzoxazone to migraine. This is preclinical-level reasoning only. The retrieved papers address cerebellar and vestibular pharmacotherapy, vertigo, and an ataxia animal model. None tests chlorzoxazone in migraine, and no migraine-specific clinical data exist.

Other high-scoring predictions have equally weak support:

| Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|------|------|------|
| Migraine with brainstem aura | 99.66% | L5 | No trials or literature; same speculative channel link |
| Migraine with or without aura, susceptibility to | 99.38% | L5 | A genetic susceptibility phenotype, not a treatable indication |
| Pulmonary hypertension | 99.31% | L5 | No trials or literature; speculative vascular K⁺ channel link |
| Rheumatoid arthritis | 99.05% | L4 | Possible adjunctive symptom relief for spasm and pain only; historical and indirect literature |
| Nephrogenic syndrome of inappropriate antidiuresis, atrophoderma vermiculata, ulerythema ophryogenesis, kyphoscoliotic heart disease | 99.07%–99.68% | L5 | Prediction only; no plausible mechanistic rationale |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the papers below tests chlorzoxazone in migraine.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Review | Journal of Neurology | Pharmacotherapy of cerebellar and central vestibular disorders (e.g., 4-aminopyridine for downbeat nystagmus); no migraine data on chlorzoxazone |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Review | Deutsches Ärzteblatt International | Treatment and natural course of vertigo; vestibular migraine accounts for 11.4% of cases |
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | Preclinical (mouse) | Journal of Neuroscience | Ca²⁺-dependent K⁺-channel activators alleviated ataxia in CaV2.1 mutant mice, an indirect link to migraine channelopathy |

For the lower-ranked rheumatoid arthritis prediction, the compiled literature includes a 2012 Cochrane review of muscle relaxants for pain in RA ([22258993](https://pubmed.ncbi.nlm.nih.gov/22258993/)), which noted a paucity of supporting evidence. It also includes historical clinical reports from 1962 and 1970, and in vitro studies from 1976. There are no registered trials and no modern RCTs.

## US Market Information

No approved indication text is recorded for any license. All 10 licenses are generic oral tablets with cancelled status.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA089859 | Chlorzoxazone (Bryant Ranch Prepack) | Tablet | Not recorded |
| ANDA212743 | Chlorzoxazone (Endo USA, Inc.) | Tablet | Not recorded |
| ANDA214702 | Chlorzoxazone (Lifsa Drugs LLC) | Tablet | Not recorded |
| ANDA089853 | Chlorzoxazone (REMEDYREPACK INC.) | Tablet | Not recorded |
| ANDA215158 | Chlorzoxazone (Happy Robin, LLC) | Tablet | Not recorded |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: liver failure, liver disease, gallbladder disease, substance abuse/dependence, drug-induced liver injury, and paracetamol poisoning.
- **Drug Interactions**: 72 interactions were identified. The main ones are:
  - **Major**: morphine, liposomal morphine
  - **Moderate**: dronabinol, metoclopramide, nabilone, naltrexone, opium, sibutramine, ethanol, promethazine
  - **Unknown severity**: doxycycline, metformin, omeprazole, lansoprazole, prednisone, simvastatin, ranitidine, bupropion, folic acid, warfarin

  The major and moderate items are mostly additive central nervous system depressant combinations; this should be confirmed against the full interaction records.

Please refer to the package insert for warnings and contraindications, as label-level data were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials and no migraine-specific literature, and the mechanistic link through K⁺ channel activation is indirect and preclinical. All US licenses are cancelled, no original indication is recorded, and label-level safety data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data, for example from DrugBank
- Preclinical or early clinical evidence of chlorzoxazone in migraine models, or K⁺ channel modulator data relevant to migraine
- Review of the hepatic safety signals, given the liver-related contraindications, and of the central nervous system depressant interactions
- Clarification of the current regulatory and market situation, since all licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


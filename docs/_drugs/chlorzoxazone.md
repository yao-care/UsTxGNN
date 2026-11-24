---
layout: default
title: Chlorzoxazone
parent: Model Prediction Only (L5)
nav_order: 525
evidence_level: L5
indication_count: 8
monitor_inn: "CHLORZOXAZONE"
predicted_indications: ["migraine disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine with brainstem aura", "pulmonary hypertension", "atrophoderma vermiculata", "ulerythema ophryogenesis", "kyphoscoliotic heart disease", "rheumatoid arthritis"]
last_modified_at: 2026-11-24
description: "Chlorzoxazone: predicted new indication migraine disorder (evidence level L5). In the US: 38 FDA applications (16 active)"
---

# Chlorzoxazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Chlorzoxazone: centrally acting skeletal muscle relaxant → migraine disorder
{: .text-alpha }

## One-Sentence Summary

Chlorzoxazone is a centrally acting skeletal muscle relaxant.
The TxGNN model predicts it may be effective for **migraine disorder**, with a score of 0.9973.
However, **no clinical trials** are registered and the **3 publications** retrieved do not directly study chlorzoxazone in migraine, so evidence is limited to model prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | migraine disorder |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 16 of 38) |
| Number of FDA Applications | 38 (active: 16) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the FDA-approved prescribing information for chlorzoxazone: "Data available from animal experiments as well as human study indicate that chlorzoxazone acts primarily at the level of the spinal cord and subcortical areas of the brain where it inhibits multisynaptic reflex arcs involved in producing and maintaining skeletal muscle spasm of varied etiology. The clinical result is a reduction of the skeletal muscle spasm with relief of pain and increased mobility of the involved muscles." ([DailyMed: chlorzoxazone prescribing information, Solubiomix](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c3d40a90-6df8-4b44-bc61-d7655c52bacb), label version 2026-10-05; accessed 2026-11-19.) Chlorzoxazone is generally described as a centrally acting muscle relaxant, and it is known to activate calcium-dependent potassium channels (SK/IK/BK).

The link to migraine is indirect. One retrieved preclinical paper studies CaV2.1 (CACNA1A) channel mutations in a mouse model of cerebellar ataxia, and these mutations are also associated with familial hemiplegic migraine. Calcium-dependent potassium channel activators eased ataxia in that model. This suggests a plausible channel-biology rationale, but it is preclinical and indirect. No migraine-specific clinical data were found.

The TxGNN score is very high, but a score is a model output and not evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Review | Journal of Neurology | Overview of drug treatment for cerebellar and central vestibular disorders; does not address chlorzoxazone in migraine |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Review | Deutsches Ärzteblatt International | Treatment and natural course of peripheral and central vertigo; vestibular migraine is listed as one form, with no chlorzoxazone data |
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | Preclinical (mouse) | Journal of Neuroscience | Enhanced CaV2.1 currents caused ataxia in mutant mice, alleviated by Ca²⁺-dependent K⁺-channel activators; CACNA1A mutations are linked to hemiplegic migraine |

None of these studies directly evaluates chlorzoxazone for migraine disorder.

---

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA040861 | CHLORZOXAZONE | PHARMOBEDIENT | Tablet; oral | Valid |
| ANDA089853 | CHLORZOXAZONE | AUROBINDO PHARMA LTD | Tablet; oral | Valid |
| ANDA089859 | CHLORZOXAZONE | WATSON LABS | Tablet; oral | Valid |
| ANDA207483 | CHLORZOXAZONE | PHARMOBEDIENT | Tablet; oral | Valid |
| ANDA210961 | CHLORZOXAZONE | PHARMAZONE | Tablet; oral | Valid |

Showing 5 of 38 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

The list shows the first 5 of the licences in the local records and may be partial.

---

## Safety Considerations

- **Drug Interactions**: 72 interactions are recorded. Major interactions include morphine and liposomal morphine. Moderate interactions include dronabinol, metoclopramide, nabilone, naltrexone, opium, sibutramine, ethanol and promethazine. Several others (e.g., warfarin, metformin, omeprazole, bupropion) have an unclassified severity level.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone. No clinical trials exist, and no retrieved study directly addresses chlorzoxazone in migraine. The only mechanistic support is indirect and preclinical.

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank
- FDA package insert warnings and contraindications
- Preclinical or exploratory clinical data on chlorzoxazone in migraine models or patients
- A review of the 72 recorded interactions, particularly with opioids and other central nervous system depressants

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: chlorzoxazone prescribing information, Solubiomix](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c3d40a90-6df8-4b44-bc61-d7655c52bacb) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


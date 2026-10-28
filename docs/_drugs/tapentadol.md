---
layout: default
title: Tapentadol
parent: Model Prediction Only (L5)
nav_order: 1200
evidence_level: L5
indication_count: 2
monitor_inn: "TAPENTADOL"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
last_modified_at: 2026-10-28
description: "Tapentadol: predicted new indication Migraine disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Tapentadol
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

## Tapentadol: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Tapentadol is an opioid analgesic. The data compiled for this report do not list a specific approved indication for it.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **no directly supporting publications**.
The prediction is model-based only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of NDAs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, tapentadol is a mu-opioid receptor agonist that also inhibits norepinephrine reuptake. Both actions modulate central pain pathways, which gives a plausible but unverified link to migraine pain.

The prediction should be interpreted cautiously. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Opioids are generally not recommended for routine migraine treatment because of the risks of medication-overuse headache, chronification, and dependence. This link rests on general pharmacology, not on data supplied for this report.

The two other predictions are weaker still:
- **Migraine with brainstem aura** (score 0.9957): no trials or literature. It likely reflects the same network proximity as the parent migraine term, and no subtype-specific rationale is supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is currently available for the top prediction (migraine disorder). Neither provides evidence of tapentadol efficacy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33689517](https://pubmed.ncbi.nlm.nih.gov/33689517/) | 2021 | Review | Expert Opinion on Pharmacotherapy | Reviews whether NSAIDs and acetaminophen can replace opioids for acute pain, amid the opioid overdose crisis. Not specific to migraine or tapentadol. |
| [29760569](https://pubmed.ncbi.nlm.nih.gov/29760569/) | 2018 | Cohort | Drug, Healthcare and Patient Safety | Opioids are not recommended for routine migraine treatment because of medication-overuse headache and dependence risks. Describes the FDA's 2016 warning on serotonin syndrome when opioids are combined with triptans or serotonergic antidepressants (SSRIs/SNRIs). |

## US Market Information

All three US authorizations are valid, and no indication text is recorded for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA214378 | Tapentadol Hydrochloride (Epic Pharma) | Film-coated tablet | Not recorded (valid) |
| NDA022304 | Nucynta (Collegium) | Film-coated tablet | Not recorded (valid) |
| NDA200533 | Nucynta (Collegium) | Film-coated extended-release tablet | Not recorded (valid) |

## Safety Considerations

**Drug Interactions**: The interaction query returned 100 interacting drugs in total. Major-level interactions among those listed include:
- Bupropion
- Morphine
- Lorcaserin
- Diethylpropion
- Dolasetron
- Palonosetron
- Phentermine

Moderate-level interactions include epinephrine, hyoscyamine, atropine, glycopyrronium, dicyclomine, naloxone, eluxadoline, dronabinol, and nabilone.

For migraine specifically, the literature highlights a serotonergic interaction risk when opioids are used with triptans or SSRIs/SNRIs. Tapentadol's norepinephrine reuptake inhibition adds to this consideration.

Please refer to the package insert for warnings and contraindications, which were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-based only (L5), with no clinical trials and no literature showing tapentadol efficacy in migraine. Opioids are not recommended for routine migraine care, and the drug is marketed in the US (3 of 3 licenses valid). The serotonergic interaction signal adds further concern.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication, which is missing from the authorization records
- Preclinical or clinical evidence of tapentadol efficacy in migraine
- Assessment of medication-overuse headache and dependence risk against existing migraine therapies
- Route and formulation compatibility assessment, since all current oral products are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


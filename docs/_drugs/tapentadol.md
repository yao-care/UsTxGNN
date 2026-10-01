---
layout: default
title: Tapentadol
parent: Model Prediction Only (L5)
nav_order: 1200
evidence_level: L5
indication_count: 3
---

# Tapentadol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tapentadol: From Pain Management to Migraine Disorder

## One-Sentence Summary

Tapentadol is an oral opioid analgesic marketed in the United States as immediate-release and extended-release tablets.
The TxGNN model predicts it may be effective for **migraine disorder**, but this is a model prediction only, with **0 clinical trials** and **2 loosely related publications**, neither of which studies tapentadol.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain management (opioid analgesic; the license records provide no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank for this drug. Based on known pharmacology, tapentadol is a mu-opioid receptor agonist and norepinephrine reuptake inhibitor. Any link to migraine would rest on central pain modulation, and that link is speculative.

The high TxGNN score (0.997) reflects proximity in the knowledge graph, not drug-specific evidence. The mechanism does not support a favorable hypothesis either. Opioids are generally discouraged for migraine because of medication-overuse headache, chronification and poor efficacy.

The model also ranked two related entities. "Migraine with brainstem aura" (99.57%) is a rare subtype with no trials or literature. "Migraine with or without aura, susceptibility to" (99.08%) is a genetic susceptibility entity rather than a treatable indication. Its retrieved literature concerns epilepsy and migraine genetics and does not mention tapentadol. Neither strengthens the case.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27096438](https://pubmed.ncbi.nlm.nih.gov/27096438/) | 2016 | Review | Cochrane Database Syst Rev | Updated review of sumatriptan plus naproxen for acute migraine in adults. Does not involve tapentadol. |
| [27096578](https://pubmed.ncbi.nlm.nih.gov/27096578/) | 2016 | Review | Cochrane Database Syst Rev | Review of single-dose dipyrone (metamizole) for acute postoperative pain. Migraine is only mentioned as one use of dipyrone, and tapentadol is not studied. |

Both papers are general background on migraine or analgesic treatment, so they offer no direct support for tapentadol in migraine.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022304 | Nucynta (Collegium) | Film-coated tablet | Not provided in the license records |
| NDA200533 | Nucynta (Collegium) | Film-coated extended-release tablet | Not provided in the license records |
| ANDA214378 | Tapentadol Hydrochloride (Epic Pharma) | Film-coated tablet | Not provided in the license records |

All routes are oral. The Evidence Pack lists 11 licenses in total, but only 5 records were returned, and duplicate entries are merged above.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials and no tapentadol-specific literature. The opioid mechanism and known migraine-treatment concerns (medication-overuse headache, chronification) argue against a favorable repurposing hypothesis.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism of action data from DrugBank
- Preclinical or clinical evidence that tapentadol has a role in migraine, and a rationale that addresses medication-overuse headache
- Confirmation that the prediction is a real treatment hypothesis and not a graph-proximity artifact

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


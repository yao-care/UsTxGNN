---
layout: default
title: Fluvoxamine
parent: Model Prediction Only (L5)
nav_order: 732
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluvoxamine: predicted new indication Paranoid personality disorder (evidence level L5). Approved use: Social phobia, phobic disorder, obsessive-compulsive disorder"
monitor_inn: "FLUVOXAMINE"
predicted_indications: ["paranoid personality disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "anxiety disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder", "endogenous depression"]
---

# Fluvoxamine
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

## Fluvoxamine: From Social Phobia and Obsessive-Compulsive Disorder to Paranoid Personality Disorder
{: .text-alpha }

## One-Sentence Summary

Fluvoxamine is a selective serotonin reuptake inhibitor (SSRI) originally used for social phobia and obsessive-compulsive disorder (OCD).
The TxGNN model predicts it may be effective for **Paranoid Personality Disorder**, but there are **0 clinical trials** and only **2 loosely related publications**, neither of which tests fluvoxamine for this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Social phobia, phobic disorder, obsessive-compulsive disorder (from knowledge-graph indication links; no US label text was available) |
| Predicted New Indication | Paranoid personality disorder |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid US authorizations) |
| Number of NDAs | 8 authorizations in total (1 NDA and 7 ANDAs), all cancelled |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Fluvoxamine is known to be a potent SSRI and a sigma-1 receptor agonist. Its efficacy in OCD and social anxiety is established.

A mechanistic link to paranoid personality disorder is speculative. The very high TxGNN score most likely reflects a shared "personality disorder" node in the knowledge graph rather than drug-specific biology. The same score (99.997%) was assigned to several other personality disorders, which supports this reading. Treat this prediction as a hypothesis only.

The data compiled for this report also contain other predicted indications for fluvoxamine with much stronger support. These are anxiety disorder (L1) and agoraphobia/panic disorder (L1), both close to the original label, and endogenous depression (L2). If the goal is a repurposing candidate with real evidence, those are better starting points than this one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cohort | Comprehensive Psychiatry | Assessed personality disorders and traits in 148 people with body dysmorphic disorder, 26 of whom were in a fluvoxamine treatment study. It does not test fluvoxamine for paranoid personality disorder. |
| [11686052](https://pubmed.ncbi.nlm.nih.gov/11686052/) | 2001 | Review | L'Encephale | Review of psychiatric side effects of alpha-interferon, including personality disorders. Not specific to fluvoxamine or to this indication. |

---

## US Market Information

All eight US authorizations are cancelled. No approved-indication text was available for any of them.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA091482 | Fluvoxamine Maleate (AvKARE) | Capsule, extended release | Cancelled |
| NDA021519 | Fluvoxamine Maleate (ANI Pharmaceuticals) | Tablet, coated | Cancelled |
| ANDA219055 | Fluvoxamine Maleate (Ajanta Pharma USA) | Capsule, extended release | Cancelled |
| ANDA212182 | Fluvoxamine Maleate (Bionpharma) | Capsule, extended release | Cancelled |
| ANDA075902 | Fluvoxamine Maleate (Apotex) | Tablet | Cancelled |

Three more cancelled ANDAs are not listed here (Chartwell RX, Endo USA, Preferred Pharmaceuticals).

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** The knowledge graph links fluvoxamine to caution or contraindication in epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, and serotonin syndrome.
- **Drug Interactions:** 100 interactions were recorded. Major-level ones include alosetron, diethylpropion, dolasetron, and bupropion. Moderate-level ones include rabeprazole, aspirin, clarithromycin, morphine, pioglitazone, aprepitant, and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone). Fluvoxamine is a strong CYP1A2 and CYP2C19 inhibitor, which drives much of this interaction burden.

Please refer to the package insert for label warnings and contraindications, which were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no registered trials, no literature testing fluvoxamine in paranoid personality disorder, and no credible mechanistic rationale. The drug also has no currently valid US authorization.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale linking fluvoxamine to paranoid personality disorder
- Any clinical or preclinical studies that directly test fluvoxamine in this condition
- FDA package insert warnings and contraindications for a proper safety screen
- A decision on whether to pursue the better-supported predictions (anxiety disorder, agoraphobia/panic disorder, endogenous depression) instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


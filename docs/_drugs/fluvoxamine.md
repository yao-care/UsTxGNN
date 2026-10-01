---
layout: default
title: Fluvoxamine
parent: Model Prediction Only (L5)
nav_order: 732
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fluvoxamine: From Obsessive-Compulsive Disorder to Paranoid Personality Disorder

## One-Sentence Summary

Fluvoxamine is an SSRI marketed in the US, and the evidence pack's literature and trial records point to obsessive-compulsive disorder (OCD) and social anxiety as its established uses.
The TxGNN model predicts it may be effective for **paranoid personality disorder**, but this is a graph-based prediction only, with **0 clinical trials** and **2 publications**, neither of which tests fluvoxamine for this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license records. The literature in the pack indicates OCD and social anxiety disorder (US controlled-release formulation) |
| Predicted New Indication | Paranoid personality disorder |
| TxGNN Prediction Score | 99.997% (model rank 187) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fluvoxamine is a selective serotonin reuptake inhibitor (SSRI) and a sigma-1 receptor agonist. The structured mechanism field in the pack is empty, so this comes from the pack's rationale notes. Serotonergic modulation is an established mechanism in OCD and anxiety disorders.

The link to paranoid personality disorder is weak. Paranoid personality disorder is a pervasive pattern of distrust and suspicion, and no plausible direct serotonergic pathway to it is supported by the supplied data. The high score (0.99997) appears to be a graph-based association. The same score is shared by schizotypal, histrionic and schizoid personality disorders, which suggests a cluster effect rather than drug-specific signal.

The two cited papers do not test fluvoxamine for this condition:
- One is a comorbidity study in body dysmorphic disorder, where 26 of 148 subjects took part in a fluvoxamine treatment study.
- The other is a general review of psychiatric side effects of alpha-interferon.

Any benefit in paranoid personality traits is speculative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cohort (comorbidity/prevalence) | Comprehensive Psychiatry | Personality disorders and traits in 148 patients with body dysmorphic disorder. It is not a test of fluvoxamine for personality disorders |
| [11686052](https://pubmed.ncbi.nlm.nih.gov/11686052/) | 2001 | Review (not fluvoxamine-specific) | L'Encephale | Psychiatric complications of alpha-interferon, including personality disorders and mood disorders. It does not evaluate fluvoxamine |

---

## US Market Information

The license records contain no approved-indication text. The 5 main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA091482 | Fluvoxamine Maleate | Capsule, extended release | AvKARE |
| NDA021519 | fluvoxamine maleate | Tablet, coated | ANI Pharmaceuticals, Inc. |
| ANDA219055 | Fluvoxamine Maleate | Capsule, extended release | Ajanta Pharma USA Inc. |
| ANDA212182 | Fluvoxamine Maleate | Capsule, extended release | Bionpharma Inc. |
| ANDA091482 | Fluvoxamine Maleate | Capsule, extended release | Actavis Pharma, Inc. |

All products are oral (capsule, tablet, coated tablet, film-coated tablet).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials, and the two papers do not evaluate fluvoxamine for paranoid personality disorder. No plausible mechanistic link is supported by the data.

**To proceed, the following is needed:**
- Fluvoxamine-specific clinical studies in paranoid personality disorder (none currently exist in the pack)
- A mechanistic rationale beyond the graph association
- The package insert warnings and contraindications, which are currently missing
- Approved-indication text for the US license records

**Other predictions in the same pack are better supported:**

| Predicted Indication | Evidence Level | Pack Recommendation |
|------|------|------|
| Anxiety disorder | L1 | Proceed with Guardrails |
| Endogenous depression | L2 | Proceed with Guardrails |
| Agoraphobia | L2 | Research Question |

The anxiety disorder prediction is best treated as label-scope confirmation, because fluvoxamine is already marketed for OCD and social anxiety. Its guardrails are to specify the anxiety subtype, account for CYP1A2/CYP2C19 inhibition, and heed pediatric suicidality warnings.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


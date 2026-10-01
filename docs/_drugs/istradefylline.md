---
layout: default
title: Istradefylline
parent: Model Prediction Only (L5)
nav_order: 818
evidence_level: L5
indication_count: 1
---

# Istradefylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Istradefylline: From Parkinson's Disease (Adjunctive Therapy) to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Istradefylline (brand name NOURIANZ) is marketed in the US as an oral tablet. From general pharmacology, its approved use is as add-on therapy for Parkinson's disease, though the supplied data does not record an indication.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but **0 clinical trials** and **0 publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease, adjunctive therapy (from general knowledge; the license records list no indication text) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both records carry the same number, NDA022075) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not in the supplied record. From general pharmacology (not from the supplied data), istradefylline is a selective adenosine A2A receptor antagonist. It is used in Parkinson's disease to improve motor control, and the supplied data does not confirm any original indication.

Rasmussen encephalitis is a rare, chronic, usually one-sided neuroinflammatory disease. It involves T-cell-mediated damage, activation of microglia and astrocytes, and drug-resistant focal seizures. A2A receptors are found on microglia, astrocytes and lymphocytes, so a role in neuroinflammation or seizure modulation is biologically conceivable.

This link is only a hypothesis:
- Preclinical studies of A2A modulation in epilepsy give mixed results.
- There is no evidence of istradefylline being used in autoimmune or epileptic encephalitis.
- The approved Parkinson's use does not overlap with this indication.

A high model score alone does not establish efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022075 | NOURIANZ (Kyowa Kirin, Inc.) | Tablet, film coated (oral) | Not listed in the source data |

The two license records are identical, so they appear once here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a TxGNN score of 99.02%. There are no clinical trials, no publications, and no recorded mechanism data (Evidence Level L5). The mechanistic link is plausible but unproven, and the approved use does not overlap with this indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed for safety screening
- Mechanism of action data from DrugBank, to test the A2A neuroinflammation hypothesis
- Preclinical evidence of A2A antagonism in models of Rasmussen encephalitis or T-cell-mediated neuroinflammation
- A literature and trial search, including case reports and rare-disease registries, to look for any prior signal
- An assessment of the drug's brain penetration and dosing route for this rare pediatric-onset disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


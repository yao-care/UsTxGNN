---
layout: default
title: Lonafarnib
parent: Model Prediction Only (L5)
nav_order: 868
evidence_level: L5
indication_count: 1
---

# Lonafarnib
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

# Lonafarnib: From Hutchinson-Gilford Progeria Syndrome to Leprosy

## One-Sentence Summary

Lonafarnib is an oral farnesyltransferase inhibitor marketed in the US as Zokinvy, used for Hutchinson-Gilford progeria syndrome and processing-deficient progeroid laminopathies.
The TxGNN model predicts it may be effective for **leprosy**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hutchinson-Gilford progeria syndrome and processing-deficient progeroid laminopathies (from general drug knowledge; the supplied license data lists no indication text) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both records carry the same number, NDA213969) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied data. From general knowledge, lonafarnib is a farnesyltransferase inhibitor (FTI). It blocks prenylation, the lipid modification that lets certain proteins, such as Ras and Rho GTPases, attach to cell membranes. This is how it helps in progeria, where an abnormal, permanently farnesylated protein accumulates.

No direct link between lonafarnib and *Mycobacterium leprae* biology or leprosy pathogenesis is documented in the supplied data. One plausible but unverified hypothesis is that blocking host prenylation-dependent signaling could modulate how macrophages and Schwann cells respond to infection, or dampen inflammation. This is speculation, not established evidence.

The score of 0.991 comes from a graph-based model. The drug's original indication (a rare genetic aging disorder) and leprosy (a chronic bacterial infection) are biologically very different, and no clinical or experimental data corroborate the prediction. Treat it as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA213969 | Zokinvy (Sentynl Therapeutics, Inc.) | Capsule (oral) |

The source data lists NDA213969 twice with identical details, so it is shown once here. No approved indication text is provided in the source data.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried database.

Please refer to the package insert for warnings, contraindications, and other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no clinical trials, no literature, and no documented mechanistic link between farnesyltransferase inhibition and leprosy. The safety package is also incomplete.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, to assess any biological link to leprosy
- Preclinical evidence, such as in vitro or animal studies of lonafarnib in *M. leprae* infection or host-cell response models
- Targeted literature review for prenylation or farnesyltransferase involvement in mycobacterial disease
- The FDA package insert (warnings, contraindications, interactions) to complete a safety screen
- Comparison against current leprosy standard of care to judge whether a new agent is worth pursuing

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


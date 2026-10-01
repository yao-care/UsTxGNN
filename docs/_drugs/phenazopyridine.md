---
layout: default
title: Phenazopyridine
parent: Model Prediction Only (L5)
nav_order: 1036
evidence_level: L5
indication_count: 1
---

# Phenazopyridine
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

# Phenazopyridine: From Urinary Tract Pain Relief to Bronchitis

## One-Sentence Summary

Phenazopyridine is an oral urinary tract analgesic, sold over the counter in the US as "urinary pain relief" tablets.
The TxGNN model predicts it may be effective for **bronchitis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract pain relief (inferred from product names; no approved indication text in the data) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenazopyridine is a urinary tract analgesic azo dye that acts locally on the urinary mucosa, and its exact mechanism is not well characterized.

**No mechanistic link between phenazopyridine and bronchitis is supported by the data provided.** Nothing connects it to bronchial inflammation, infection or mucus pathology. The original indication (urinary pain) and the predicted indication (an airway disease) involve different organ systems and different disease processes.

The high TxGNN score (0.992) should be read cautiously. It may reflect knowledge-graph neighborhood effects, such as shared symptom or analgesic-related nodes, rather than a real pharmacological relationship. It is not biological support for the prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The source data lists 20 products, all oral tablets. Authorization numbers and approved indication text are not provided. The 5 main products are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not provided | Preferred Urinary Pain Relief (Reese Pharmaceutical Co) | Tablet | Not provided |
| Not provided | Quality Choice Maximum Strength Urinary Pain Relief (Chain Drug Marketing Association) | Tablet | Not provided |
| Not provided | Cheeky Bonsai UTI Pain Relief (IXXA, INC) | Tablet | Not provided |
| Not provided | Phenazopyridine Hydrochloride (REMEDYREPACK INC.) | Tablet | Not provided |
| Not provided | Dollar General Maximum Strength Urinary Pain Relief (Dolgencorp, Inc.) | Tablet | Not provided |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanistic link to bronchitis. The evidence level is L5 and the candidate is still at the initial screening stage (S0).

**To proceed, the following is needed:**
- The US package insert (warnings and contraindications), which is required before any safety screening
- Mechanism of action data for phenazopyridine (for example from DrugBank)
- A targeted literature and trial search for phenazopyridine in respiratory conditions
- A route compatibility assessment, since the current products are oral tablets for urinary use
- A pharmacological review of why the model links this drug to bronchitis, to rule out a knowledge-graph artifact

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


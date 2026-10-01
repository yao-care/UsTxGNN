---
layout: default
title: Methsuximide
parent: Model Prediction Only (L5)
nav_order: 914
evidence_level: L5
indication_count: 10
---

# Methsuximide
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

# Methsuximide: From Epilepsy (Absence Seizures) to Insomnia

## One-Sentence Summary

Methsuximide is a succinimide anticonvulsant. The supplied US records do not state an approved indication, so the epilepsy use is inferred from the drug class.
The TxGNN model predicts it may be effective for **insomnia**, but this is a model-only signal with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / absence seizures (inferred from drug class; label text is blank in the supplied records) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Methsuximide is a succinimide anticonvulsant. Drugs in this class are generally associated with absence seizures, plausibly through T-type calcium channel modulation. The drug is also sedating, which is the only conceptual bridge to a sleep indication.

No direct mechanistic link to sleep initiation or maintenance is documented in the input. The prediction currently rests on graph proximity in the TxGNN knowledge graph, not on demonstrated pharmacology.

Two other predictions in the list are closely tied to this one:
- **Sleep disorder, initiating and maintaining sleep** (score 99.70%) is essentially the same phenotype as insomnia, so the two predictions are not independent.
- **Restless legs syndrome** (score 99.39%) is the only other prediction with any literature. That literature suggests an adverse-effect association, not a benefit (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for insomnia.

Only one other predicted indication, restless legs syndrome, has any literature. It is indirect and does not support efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3145164](https://pubmed.ncbi.nlm.nih.gov/3145164/) | 1988 | Case report | Clin Neurol Neurosurg | Two patients with complex partial and secondarily generalized seizures developed restless legs while taking methsuximide and phenytoin. This points to an adverse association, not a treatment effect. |
| [23205958](https://pubmed.ncbi.nlm.nih.gov/23205958/) | 2012 | Review | Epilepsia | General review of how phenobarbital's structure shaped later antiepileptic drugs. It does not address restless legs efficacy. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA010596 | Celontin | Capsule (oral) | Parke-Davis Div of Pfizer Inc |
| ANDA217213 | Methsuximide | Capsule (oral) | ANI Pharmaceuticals, Inc. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction is a model-only signal (L5) with no trials, no literature, and no documented mechanism. The remaining top-10 predictions are also L5, except restless legs (L4), which is possibly adverse. Several of them look like graph-proximity artifacts, for example the opposing conditions nephrogenic SIAD and nephrogenic diabetes insipidus.

**To proceed, the following is needed:**
- The package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Mechanism of action data (e.g., from DrugBank) to test whether a sleep-related mechanism is plausible
- A targeted literature and trial search on methsuximide or succinimides in insomnia and sleep disturbance
- Confirmation of the original indication against the US label, since the empty indication records suggest a data gap and not a true repurposing case
- Route and dose compatibility assessment (oral capsule only at present)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


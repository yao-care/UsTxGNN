---
layout: default
title: Baricitinib
parent: Model Prediction Only (L5)
nav_order: 438
evidence_level: L5
indication_count: 2
---

# Baricitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Baricitinib: From Immune-Mediated Inflammatory Conditions to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Baricitinib is an oral JAK1/JAK2 inhibitor marketed in the US as Olumiant, used in immune-mediated inflammatory conditions. The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare congenital developmental disorder. There are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license records (3 share NDA207924; 1 has no listed number) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Baricitinib is a JAK1/JAK2 inhibitor, and its known use is in immune-mediated inflammatory conditions. The input lists no original indications, so that context comes from the drug class rather than from label text.

No established mechanistic link connects JAK-STAT inhibition to this syndrome. The syndrome causes ocular and skeletal malformations from disrupted development, and it has no known JAK-STAT-driven pathology. Structural congenital defects are also unlikely to be reversed by an immunomodulator in adults.

The very high score (99.94%) cannot be traced to a biological rationale. It may reflect knowledge-graph topology, such as shared gene or phenotype neighbours, rather than a true therapeutic signal. It needs independent validation, for example pathway-level or gene-level analysis, before any clinical interpretation.

A second prediction, **brachydactyly-syndactyly syndrome** (score 99.94%, also L5), shows the same pattern. It is a congenital limb malformation with no evidence linking it to JAK1/JAK2 inhibition, and no trials or literature exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA207924 | Olumiant | Film-coated tablet (oral) | Eli Lilly and Company |
| No number listed | Baricitinib | Film-coated tablet (oral) | Eli Lilly and Company |

The NDA207924 entry appears three times in the source data. It is shown once here. No approved indication text was provided for any record.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has the highest score tier but no trials, no literature, and no plausible mechanism. The syndrome is a congenital structural disorder with no known inflammatory driver, so the score looks like a knowledge-graph artefact rather than a real signal.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) for baricitinib
- Package insert warnings and contraindications, which block safety screening
- Pathway- or gene-level analysis testing whether JAK-STAT signalling is involved in this syndrome
- Any preclinical or case-level evidence supporting the link

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


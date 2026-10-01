---
layout: default
title: Teprotumumab
parent: Model Prediction Only (L5)
nav_order: 1210
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: From Thyroid Eye Disease to Monosomy X

## One-Sentence Summary

Teprotumumab is an IGF-1R inhibitory antibody marketed in the US as TEPEZZA. Its original indication is thyroid eye disease, taken from public labeling because the Evidence Pack has no indication text.
The TxGNN model predicts it may be effective for **monosomy X (Turner syndrome)** with a score of 99.79%, but **0 clinical trials** and **0 publications** support this. The prediction is model-only and biologically questionable.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thyroid eye disease (not in the Evidence Pack; the license record's indication text is empty) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761143) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Teprotumumab is characterized as an IGF-1R inhibitory antibody, and that is the only mechanistic information available.

Monosomy X (Turner syndrome) causes short stature and gonadal dysgenesis, and the GH/IGF-1 axis is therapeutically relevant to it. Inhibiting IGF-1R would oppose growth-promoting therapy, so the biological direction is questionable. The high score most likely reflects graph proximity in the knowledge graph rather than a real mechanistic signal.

The other top predictions show the same pattern:
- **Closely related Turner-spectrum and sex-development terms** (Turner syndrome due to structural X anomalies, mosaic monosomy X, mixed gonadal dysgenesis, sex chromosome disorder of sex development, X chromosome number anomaly). These appear to inherit their scores from the monosomy X node and add no independent evidence.
- **Esophageal varices with and without bleeding**. These two entries have identical scores, which suggests duplicates in the knowledge graph. No link between IGF-1R blockade and portal hypertension is established, and standard care is well established.
- **Varicose disease and mitochondrial oxidative phosphorylation disorder**. No plausible mechanism is identified for varicose disease. The mitochondrial link is only indirect preclinical biology, and the direction of effect for an inhibitor is unclear.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761143 | TEPEZZA (Horizon Therapeutics USA, Inc.) | Injection, powder, lyophilized, for solution | Not provided in the record |

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records.
- **Population-specific concerns** (from the prediction rationale): IGF-1R inhibition carries risks of hyperglycemia and hearing impairment. These would need careful assessment in a pediatric and young-adult Turner syndrome population.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or publications. The mechanism is biologically questionable, since IGF-1R inhibition runs counter to growth-supportive management in Turner syndrome. The high score looks like a graph-proximity artifact.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Preclinical or mechanistic evidence that IGF-1R inhibition could benefit monosomy X, or an explanation of why the score is high
- A safety assessment for hyperglycemia and hearing impairment in pediatric and young-adult patients
- Route compatibility and similarity-to-original analyses, both currently pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


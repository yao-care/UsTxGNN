---
layout: default
title: Mecasermin
parent: Model Prediction Only (L5)
nav_order: 891
evidence_level: L5
indication_count: 5
---

# Mecasermin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Mecasermin: From Recombinant IGF-1 Therapy to Monosomy X

## One-Sentence Summary

Mecasermin is recombinant human IGF-1 (insulin-like growth factor 1) and is currently marketed in the United States as an injectable product.
The TxGNN model predicts it may be useful for **monosomy X (Turner syndrome)**, with a score of 99.59%.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output and general pharmacology alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied regulatory data |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Mecasermin is recombinant human IGF-1, and IGF-1 is a central mediator of growth-hormone-driven growth. The mechanistic link below is inferred from general pharmacology, not from the supplied data, which contain no original indication or MOA.

Monosomy X (Turner syndrome) is characterized by short stature. The growth axis is therefore a biologically plausible target for an IGF-1 replacement drug. This is a hypothesis to test, not evidence of benefit. The TxGNN score is a computational prediction and has not been checked against any trial or publication.

TxGNN also ranked four other candidates. Their supporting evidence is equally absent, and their rationale is weaker:

- **Growth hormone insensitivity syndrome with immune dysregulation 2 (score 99.06%):** Mecasermin acts downstream of the GH receptor, so it could in principle bypass GH insensitivity. However, it would not address the immune dysregulation, and its safety in this population is unassessed. This is a research question.
- **Wolman disease with hypolipoproteinemia and acanthocytosis (99.09%):** This is a lysosomal acid lipase deficiency, and IGF-1 does not address the lipid storage defect. The score is likely a knowledge-graph artifact. Hold.
- **Esophageal varices, with and without bleeding (99.03% each):** These arise from portal hypertension, and Mecasermin is not expected to lower portal pressure. The identical scores suggest one shared graph signal rather than independent evidence. Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA021839 | Increlex (Eton Pharmaceuticals, Inc.) | Injection | Not listed in the supplied data |
| Not provided | GUNA-IGF (Guna spa) | Solution / drops | Not listed in the supplied data |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Monosomy X prediction has a high model score but no trials, no literature and no mechanism data. Its rationale is a plausible inference from general pharmacology and is not backed by supplied data. Safety information is also missing, so the candidate cannot yet pass a safety screen.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap), obtained from the FDA label
- Original indication and mechanism of action, for example from the DrugBank API
- A systematic search of ClinicalTrials.gov and PubMed for IGF-1 or Mecasermin in Turner syndrome
- A route and formulation compatibility assessment, since none has been done yet

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Erdafitinib
parent: Model Prediction Only (L5)
nav_order: 665
evidence_level: L5
indication_count: 6
---

# Erdafitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Erdafitinib: From Oncology Use (FGFR Kinase Inhibitor) to Pulmonary Hypertension

## One-Sentence Summary

Erdafitinib is an oral pan-FGFR kinase inhibitor marketed in the US as BALVERSA. The supplied data does not list its approved indication.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it remains a computational hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (the approved-indication text is empty) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 license records (all under NDA212018) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Erdafitinib is known as a pan-FGFR (FGFR1-4) tyrosine kinase inhibitor. That description comes from general drug-class knowledge, not from the supplied data.

FGF/FGFR signaling, especially FGFR1, has been linked in preclinical pulmonary arterial hypertension models to pulmonary vascular smooth muscle proliferation and remodeling. Blocking this pathway could therefore plausibly reduce vascular remodeling.

This link is **plausible but unvalidated**. FGFR signaling also has protective roles in some vascular contexts, so the direction of effect is uncertain. The very high TxGNN score reflects a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212018 | BALVERSA (Janssen Products LP) | Tablet, film coated (oral) | Not provided in the supplied data |

The record contains three identical entries for this NDA; they are shown once here.

## Cytotoxicity

Erdafitinib is an oncology kinase inhibitor, so it is covered here. This classification is based on general drug-class knowledge, since no DrugBank category data was supplied.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Serum phosphate (hyperphosphatemia), ocular examinations and nail changes; see the package insert for the full list |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. No warnings or contraindications were supplied, and no drug interactions were found in the queried data.

For chronic non-oncology use, the expected class-related toxicities (hyperphosphatemia, ocular and nail toxicity) would need to be weighed against any benefit. This comes from the candidate's mechanistic review, not from label data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and an unvalidated mechanism. It is best treated as a research question, not a development candidate. The package insert has not been reviewed, so safety screening cannot start.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap)
- Mechanism of action data from DrugBank
- Preclinical evidence that FGFR inhibition improves pulmonary vascular remodeling, including the direction of effect
- An assessment of long-term safety in a non-oncology setting

**Other predictions (all L5, Hold):** kyphoscoliotic heart disease, amenorrhea, rheumatoid arthritis, amyotrophic lateral sclerosis and brachydactyly-syndactyly syndrome. Each has a weak or doubtful mechanistic rationale. The only retrieved paper, for rheumatoid arthritis, is a general review of kinase inhibitors with no disease-specific efficacy data.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Iopromide
parent: Model Prediction Only (L5)
nav_order: 806
evidence_level: L5
indication_count: 10
---

# Iopromide
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

# Iopromide: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iopromide is an iodinated radiographic contrast agent used in diagnostic imaging (marketed in the US as Ultravist).
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility**, but this rests on the graph model alone, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic contrast imaging (the approved indication text is not listed in the source data) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 records (all under NDA020220) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iopromide is an iodinated contrast agent. It helps visualize tissues on imaging and is not a disease-modifying drug. It has no documented anti-inflammatory, chondroprotective or immunomodulatory pharmacology.

The link between the original use and the predicted indication is therefore weak. The high TxGNN score (0.996) appears to reflect shared neighbors in the knowledge graph rather than a therapeutic rationale. The same pattern appears in the other top predictions: osteoarthritis, rheumatoid arthritis, several rare skeletal dysplasias, alopecia and myosclerosis. All of them lack a plausible mechanism.

The only nearby literature signals are indirect. A 2009 study used contrast-enhanced CT to image synovitis in rheumatoid arthritis, which is diagnostic use, not treatment. A case report describes a cerebral vaso-occlusive event after low-osmolar contrast in a sickle cell patient, which is a possible harm signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020220 | Ultravist (Bayer HealthCare Pharmaceuticals Inc.) | Injection | Not listed in the source data |

The source data contains four identical Ultravist injection records under this NDA.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found.
- **Contrast-agent caution**: One case report (PMID 16628721) describes a cerebral vaso-occlusive event after low-osmolar intravenous contrast in a patient with sickle cell disease. This is a single case and not a confirmed risk, but it calls for caution in some populations.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). No trials or literature support it, and there is no plausible pharmacological mechanism for a diagnostic contrast agent in osteoarthritis. The mechanism of action and package-insert safety data are also missing, so the candidate cannot advance past the initial screening stage.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and the approved indication text
- Package insert warnings and contraindications
- A biological rationale connecting iodinated contrast agents to joint or cartilage pathology
- Preclinical or observational evidence in osteoarthritis
- A route-of-administration assessment, since only the injectable form is marketed

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


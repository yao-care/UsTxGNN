---
layout: default
title: Avatrombopag
parent: Model Prediction Only (L5)
nav_order: 431
evidence_level: L5
indication_count: 10
---

# Avatrombopag
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

# Avatrombopag: From a Thrombopoietin Receptor Agonist to Marcothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Avatrombopag is a thrombopoietin (TPO) receptor agonist that stimulates platelet production, and it is currently marketed in the United States.
The TxGNN model predicts it may be effective for **marcothrombocytopenia with mitral valve insufficiency**, with a top score of 99.995%.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a research question, not an evidence-backed candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Marcothrombocytopenia with mitral valve insufficiency |
| TxGNN Prediction Score | 99.995% (model rank 254) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

The evidence pack contains no approved-indication text for either NDA, so the original indication is not listed here.

---

## Why is This Prediction Reasonable?

Avatrombopag is a TPO receptor agonist. It stimulates megakaryocyte proliferation and platelet production. Detailed DrugBank mechanism-of-action data are not available in the evidence pack, so this description comes from the mechanistic notes attached to the predictions.

Raising platelet count is a plausible strategy for a condition defined by low platelets. However, marcothrombocytopenia is likely genetic in origin, and the response to a TPO receptor agonist would depend on the specific defect. No supporting data were provided, so the mechanistic link is **not verified**.

The other nine predictions are weaker:
- **Thrombocytopenia-related (ranks 2–3):** "Hereditary thrombocytopenia with normal platelets" is plausible in principle, but the disease name is ambiguous and the mapping should be checked. "Transient neonatal thrombocytopenia" is self-limiting, and no neonatal safety data were provided, so the risk-benefit balance is unfavorable.
- **Dense granule disease (rank 4):** This is a platelet function defect, not a low platelet count. A TPO receptor agonist would not be expected to correct it, and the score looks like a knowledge-graph proximity artifact.
- **Motor neuron and cortical disorders (ranks 5–10):** These include ALS, its susceptibility entry, lower motor neuron syndrome, Mills syndrome, monomelic amyotrophy and polymicrogyria. No mechanistic link to TPO receptor agonism was found, and they likely reflect graph-structure artifacts. The ALS-related entries overlap and should not be counted as independent support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA210238 | DOPTELET | Tablet, film coated (oral) | AkaRx, Inc. |
| NDA219696 | Doptelet Sprinkle | Granule | AkaRx, Inc. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (L5), and the mechanistic link to this ultra-rare, likely genetic condition is unverified. Blocking safety gaps also remain, because package insert warnings and contraindications have not been retrieved.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap)
- DrugBank mechanism-of-action data
- Confirmation of the disease definition and ontology mapping for "marcothrombocytopenia with mitral valve insufficiency", and of the ambiguous "hereditary thrombocytopenia with normal platelets"
- A targeted literature and trial search (PubMed, ClinicalTrials.gov, ICTRP) for TPO receptor agonists in inherited thrombocytopenias
- Genetic-subtype analysis to decide whether a TPO receptor agonist could plausibly work
- Route compatibility assessment, which is still pending
- For the neonatal indication, neonatal safety data before any further consideration

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


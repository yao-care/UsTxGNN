---
layout: default
title: Tagraxofusp
parent: Model Prediction Only (L5)
nav_order: 1194
evidence_level: L5
indication_count: 10
---

# Tagraxofusp
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

# Tagraxofusp: From Blastic Plasmacytoid Dendritic Cell Neoplasm to Esotropia

## One-Sentence Summary

Tagraxofusp (Elzonris) is a CD123-directed cytotoxic fusion protein, originally used to treat blastic plasmacytoid dendritic cell neoplasm (BPDCN).
The TxGNN model predicts it may be effective for **esotropia**, but this rests on the graph score alone: **0 clinical trials** and **0 publications** support it, and no plausible mechanism links the drug to the condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | BPDCN (from trial descriptions; the US license record has no indication text) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| US Market Status | Marketed |
| Number of NDAs | 1 (BLA761116) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known information, tagraxofusp is a fusion of interleukin-3 (IL-3) and a diphtheria toxin fragment. It binds CD123 (the IL-3 receptor alpha chain) on cells and kills CD123-expressing cells. This explains its use in BPDCN, where tumor cells strongly express CD123.

Esotropia is an eye-alignment disorder caused by problems with the eye muscles and their nerve control. It has no known CD123-driven disease process, so the mechanism does not carry over from the original indication.

The 99.73% score is a knowledge-graph association, not a biological rationale. On this evidence the prediction is most likely a false positive. Systemic cytotoxic therapy would also be a poor risk-benefit fit for a non-malignant functional eye condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761116 | Elzonris (Stemline Therapeutics, Inc.) | Injection, solution | Not listed in the record (BPDCN per trial descriptions) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CD123-directed diphtheria toxin fusion protein) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; capillary leak syndrome is a known risk and needs monitoring |
| Handling Protection | Follow institutional handling rules for cytotoxic and biologic antineoplastic agents |

## Safety Considerations

- **Key Risk**: Capillary leak syndrome is a known risk of this systemic cytotoxic fusion protein.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The esotropia prediction has no trials, no literature and no plausible CD123-related mechanism. Given the drug's toxicity, it does not justify further investment.

**To proceed, the following is needed:**
- A new mechanistic hypothesis for CD123 or IL-3 involvement in esotropia. Without one, this candidate should be closed.
- Package insert warnings and contraindications (blocking gap DG001).
- DrugBank mechanism of action data (gap DG002).

**Note on other candidates:** Among the ten predictions, the only one with direct drug trials is rank 2, "pre-malignant neoplasm" (evidence level L3, Research Question). Its five trials cover myelofibrosis, AML, pediatric hematologic malignancies and high-risk MDS. All are early-phase (Phase 1 or 1/2, with one Early Phase 1) and none has results. They enroll established malignancies rather than pre-malignant states, so the label is a loose match. If the team wants to pursue a lead, this one is the better place to start, for example as clonal myeloid disorders such as MDS or myelofibrosis. It would still need a more precise disease definition.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


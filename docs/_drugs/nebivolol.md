---
layout: default
title: Nebivolol
parent: Model Prediction Only (L5)
nav_order: 958
evidence_level: L5
indication_count: 5
---

# Nebivolol
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

# Nebivolol: From Approved Antihypertensive Use to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Nebivolol is an oral, highly beta-1-selective blocker with nitric oxide-mediated vasodilation, marketed in the US as tablets.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (NDA and ANDA authorizations) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general pharmacology, nebivolol combines beta-1 blockade with endothelial nitric oxide-mediated vasodilation. That profile is biologically plausible for severe hypertension and hypertension-related renal injury.

The link between nebivolol's antihypertensive use and this new indication is only indirect. Malignant hypertensive renal disease is a consequence of severe, uncontrolled hypertension. Blood pressure lowering could therefore be relevant in principle. However, nebivolol is an oral agent and not a standard therapy for hypertensive emergencies, which usually call for rapidly titratable, often intravenous treatment. The high score most likely reflects the drug's general antihypertensive associations in the knowledge graph, not disease-specific evidence.

Other predictions follow the same pattern:
- **Malignant renovascular hypertension** (99.42%): Beta-1 blockade reduces renin release, which is plausible but unverified.
- **Pulmonary hypertension** (two entries, 99.39%): The link is weak, and beta-blockers are generally used cautiously in this setting.
- **Braddock syndrome** (99.14%): No mechanistic rationale could be established.

All are L5 with no supporting trials.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this indication.

The 20 publications retrieved for the pulmonary hypertension prediction are general hypoxia biology papers (brain aging, cancer, altitude, multiple sclerosis). None studies nebivolol, so they do not count as supporting evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021742 | Bystolic (Allergan, Inc.) | Tablet | Not listed in source data |
| ANDA203966 | nebivolol (Torrent Pharmaceuticals Limited) | Tablet | Not listed in source data |
| ANDA203659 | Nebivolol (Golden State Medical Supply, Inc.) | Tablet | Not listed in source data |
| ANDA212682 | NEBIVOLOL (A-S Medication Solutions) | Tablet | Not listed in source data |
| ANDA203825 | Nebivolol (Camber Pharmaceuticals, Inc.) | Tablet | Not listed in source data |

All listed products are oral tablets. 5 of 20 authorizations are shown.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or literature. Nebivolol is an oral agent and is not a standard option for hypertensive emergencies. Safety data are also missing, so it cannot yet proceed to safety screening.

**To proceed, the following is needed:**
- The FDA package insert, to obtain warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- A targeted literature search for nebivolol in malignant or severe hypertension and hypertensive nephropathy
- An assessment of whether an oral beta-blocker fits the acute setting of this indication
- Confirmation of the approved indications on the US labels

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


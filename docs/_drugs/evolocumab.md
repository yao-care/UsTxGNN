---
layout: default
title: Evolocumab
parent: Model Prediction Only (L5)
nav_order: 688
evidence_level: L5
indication_count: 6
---

# Evolocumab
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

# Evolocumab: From LDL-Cholesterol Lowering to Symptomatic Hemophilia in Female Carriers

## One-Sentence Summary

Evolocumab (marketed as REPATHA) is a PCSK9-neutralizing monoclonal antibody that lowers LDL cholesterol.
The TxGNN model predicts it may be effective for **symptomatic hemophilia in female carriers**, but **0 clinical trials** and **0 publications** support this direction.
It is a model-only prediction with no plausible mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license records (LDL-C lowering, based on the drug's mechanism class) |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 (all records under BLA125522) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Evolocumab is a monoclonal antibody that neutralizes PCSK9. This increases LDL receptor recycling and lowers LDL-C.

Hemophilia in female carriers is a coagulation disorder caused by reduced factor VIII or IX production or function. Evolocumab has no known role in coagulation factor synthesis, activity, or replacement, so **no plausible mechanistic link was identified**.

The high TxGNN score (0.998) reflects a knowledge-graph pattern only, and it is likely an artifact. No trial or publication supports it. The other five predictions are also unsupported:

- Familial apolipoprotein C-II deficiency (99.50%) is the most biologically adjacent, as a lipid-metabolism disorder. Evolocumab mainly lowers LDL-C and does not address the lipoprotein lipase activation defect.
- Thrombocytopenic purpura, factor XI deficiency and hemophilia A with vascular abnormality have no mechanistic link.
- "Disease of catalytic activity" is a non-specific ontology category, not an actionable indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125522 | REPATHA (Amgen USA Inc.) | Injection, solution | Not listed in the record |

Four license records exist under this BLA. They are identical in the data, so they are shown once.

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried database.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no trials or literature. Evolocumab's PCSK9 mechanism has no plausible connection to coagulation factor deficiency. Its marketed status does not offset this lack of evidence.

**To proceed, the following is needed:**
- A mechanistic hypothesis linking PCSK9 inhibition to coagulation, supported by preclinical data
- A systematic literature and trial search showing any signal for this indication
- Package insert warnings and contraindications, plus mechanism of action data, to complete the record
- If a lipid-related direction is pursued, re-evaluating familial apolipoprotein C-II deficiency first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


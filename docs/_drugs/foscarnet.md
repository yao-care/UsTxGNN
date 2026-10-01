---
layout: default
title: Foscarnet
parent: Model Prediction Only (L5)
nav_order: 736
evidence_level: L5
indication_count: 4
---

# Foscarnet
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Foscarnet: From Antiviral Therapy to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome

## One-Sentence Summary

Foscarnet is an injectable antiviral that inhibits viral DNA polymerase, and it is marketed in the US.
The TxGNN model predicts it may be effective for **autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome**, a rare inherited vascular disorder.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records; the mechanism (viral DNA polymerase inhibitor) points to antiviral use |
| Predicted New Indication | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome |
| TxGNN Prediction Score | 99.56% (model rank 10,857) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 8 licenses (NDA and ANDA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Foscarnet is a pyrophosphate analog that inhibits viral DNA polymerase, reverse transcriptase and herpesvirus DNA polymerases.

The predicted disease is a heritable vascular and basement-membrane disorder with no viral cause. There is no plausible mechanistic link between foscarnet's antiviral action and this condition. The high score (0.996) comes from graph-based patterns in the TxGNN knowledge graph, not from biological or clinical evidence.

Foscarnet is known to be nephrotoxic, which is a further concern in a condition that involves hematuria. At present this prediction is a hypothesis with no support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The record lists 8 licenses; the 5 below are the main ones. The records give no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020068 | Foscavir (Clinigen Limited) | Injection, solution | Not stated |
| ANDA216602 | Foscarnet Sodium (Amneal Pharmaceuticals LLC) | Injection | Not stated |
| ANDA212483 | Foscarnet (Fresenius Kabi USA, LLC) | Injection, solution | Not stated |
| ANDA213001 | Foscarnet Sodium (Gland Pharma Limited) | Injection, solution | Not stated |
| ANDA213987 | Foscarnet Sodium (Hikma Pharmaceuticals USA Inc.) | Injection, solution | Not stated |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were retrieved.

The evidence pack's own assessment notes that foscarnet's nephrotoxicity is a concern for a condition involving hematuria.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it and no plausible mechanism, since the disease is a non-viral inherited vascular disorder and foscarnet is an antiviral. Its nephrotoxicity works against use in a disease with hematuria.

The other top-ranked predictions in the pack (brain small vessel disease, rheumatoid arthritis, diabetic nephropathy) reached the same conclusion. Their retrieved trials and literature do not show foscarnet benefit, and the diabetic nephropathy prediction adds a kidney safety concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking foscarnet to this disease. Without it, the prediction should not advance beyond model output.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


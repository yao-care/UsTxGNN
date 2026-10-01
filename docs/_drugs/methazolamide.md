---
layout: default
title: Methazolamide
parent: Model Prediction Only (L5)
nav_order: 907
evidence_level: L5
indication_count: 3
---

# Methazolamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Methazolamide: From Carbonic Anhydrase Inhibition to Primary Hereditary Glaucoma

## One-Sentence Summary

Methazolamide is an oral carbonic anhydrase inhibitor. The supplied record lists no original indication.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but currently **0 clinical trials** and **0 publications** support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied record (approved indication text is blank in all licenses) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (generic ANDA authorizations) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Methazolamide is a carbonic anhydrase inhibitor. Blocking carbonic anhydrase in the ciliary epithelium reduces aqueous humor secretion and lowers intraocular pressure, which is biologically plausible for glaucoma.

Because the record lists no original indication, it is unclear whether this is true repurposing. Carbonic anhydrase inhibitors are already widely used in glaucoma, so this may simply reflect the drug's existing use. That should be checked against the US label. The high score (0.998) is a computational prediction, and no trial or publication in the dataset supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA207438 | Methazolamide | Tablet | Bausch & Lomb Incorporated |
| ANDA207438 | Methazolamide | Tablet | Micro Labs Limited |
| ANDA040001 | Methazolamide | Tablet | Bryant Ranch Prepack |
| ANDA217408 | Methazolamide | Tablet | Ajanta Pharma USA Inc. |
| ANDA040001 | Methazolamide | Tablet | NorthStar Rx LLC |

Only oral tablets are authorized. The approved indication text is blank in the supplied records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the record has no original indication or mechanism data. Glaucoma is already a plausible use for this drug class, so it is unclear whether this counts as repurposing at all.

Two other predictions exist. Congestive heart failure (score 99.43%) reaches L4, supported by class-level reviews and preclinical studies (PMID 17124262, 35043173), but has no human trials, so it is a research question only. Acute pulmonary heart disease (score 99.28%) has no evidence at all (L5).

**To proceed, the following is needed:**
- Retrieve the US package insert, covering approved indications, warnings and contraindications. This is currently a blocking data gap.
- Fill in the original indication and mechanism of action (DrugBank).
- Confirm whether glaucoma is already a labeled use. If so, reclassify the prediction as existing use rather than repurposing.
- For heart failure, check for human clinical data before any further evaluation.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


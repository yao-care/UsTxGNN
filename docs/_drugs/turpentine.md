---
layout: default
title: Turpentine
parent: Model Prediction Only (L5)
nav_order: 1272
evidence_level: L5
indication_count: 1
monitor_inn: "TURPENTINE"
predicted_indications: ["multiple endocrine neoplasia"]
last_modified_at: 2026-10-14
description: "Turpentine: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not recorded"
---

# Turpentine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Turpentine: From No Recorded Indication to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Turpentine is a mixture of terpenes (mainly alpha- and beta-pinene) that has been used as a solvent and historically as a topical counterirritant, but no approved indication is recorded for it in the data compiled for this report.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but **no clinical trials** and **no publications** currently support this direction.
The prediction rests solely on a computational score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (no approved indication text in the license data) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no valid licenses) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Turpentine is a complex mixture of terpenes, used as a solvent and historically as a topical counterirritant. No original indication is recorded, so no link between an established use and the predicted one can be drawn.

No mechanistic link to multiple endocrine neoplasia can be established from the data compiled for this report. These syndromes are driven by germline mutations in MEN1 (menin), RET, or CDKN1B, and turpentine has no known target or pathway relevant to them.

The very high TxGNN score (0.996) is a computational prediction, not biological or clinical evidence. It may reflect knowledge-graph artifacts such as sparse drug connectivity or shared neighbouring nodes, and it should not be read as a biological signal.

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
| Not available | Terebinthina (Boiron) | Pellet | Not recorded (cancelled) |
| M017 | Ling Nam Hak Kwai Oil (Ling Nam Medicine Factory (H.K.) Ltd.) | Oil | Not recorded (cancelled) |
| M014 | ARTREX (Bioved Pharmaceuticals) | Cream | Not recorded (cancelled) |

All three authorizations are cancelled, so no valid licenses remain.

---

## Safety Considerations

- **Known toxicity profile (general knowledge, not from label data):** turpentine is associated with aspiration hazard, CNS effects, renal effects and dermal effects.

The package insert warnings and contraindications were not available, and no drug-interaction records were found. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a computational score, with no clinical trials, no literature, no mechanistic rationale and no valid US market authorization. Together with turpentine's known toxicity, this does not justify advancing the candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, to test whether any plausible link to MEN1, RET or CDKN1B biology exists
- Preclinical or mechanistic evidence for activity in multiple endocrine neoplasia
- Review of the knowledge-graph prediction to rule out artifacts from sparse connectivity
- Assessment of route compatibility and a safety plan, given turpentine's toxicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Tiopronin
parent: 僅模型預測 (L5)
nav_order: 1231
evidence_level: L5
indication_count: 10
---

# Tiopronin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Tiopronin: From Cystinuria to Renal Tubular Acidosis

## One-Sentence Summary

> Tiopronin is a thiol-containing compound whose established clinical use, based on its known pharmacology, is cystinuria (formal regulatory indication data was not retrievable for this evidence pack).
> The TxGNN model predicts it may be effective for **Renal Tubular Acidosis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only inference.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in regulatory license data; known pharmacological use is cystinuria (per mechanistic rationale in this evidence pack) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for tiopronin (flagged as a High-severity data gap). Based on known pharmacological information, tiopronin (2-mercaptopropionylglycine) is a free-thiol compound that acts through thiol–disulfide exchange reactions, forming soluble mixed disulfides with cystine. This mechanism underlies its established clinical use in cystinuria, a hereditary renal tubular amino-acid transporter defect.

Renal tubular acidosis (RTA) and cystinuria share a superficial anatomical link — both are renal tubular disorders — but their underlying pathophysiology differs substantially. RTA is primarily caused by defective HCO3⁻/H⁺ transport at the tubular epithelium, a mechanism that thiol chemistry does not directly address. The evidence pack itself characterizes this link as "theoretical analogy" (理論類推), explicitly noting the absence of direct molecular evidence connecting tiopronin's thiol-exchange activity to acid-base transporter function.

In short, the prediction is driven by knowledge-graph similarity between two renal tubular conditions rather than a validated shared mechanism. Without confirmatory mechanistic, preclinical, or clinical data, this should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Currently not marketed; no license records are available for tiopronin in the reviewed jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA-specific warnings and contraindications could not be retrieved for this candidate (data gap DG001, severity: Blocking). This gap currently prevents a formal S1 safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (renal tubular acidosis) is supported only by a TxGNN similarity score, with zero clinical trials or literature and an explicitly weak, non-validated mechanistic rationale. Combined with the absence of Taiwan/US market presence and a blocking safety data gap, there is currently insufficient evidence to advance this candidate.

**To proceed, the following is needed:**
- TFDA (or equivalent) warning/contraindication data for tiopronin (resolves blocking gap DG001)
- Confirmed mechanism of action data via DrugBank or primary literature (resolves gap DG002)
- Preclinical or mechanistic studies directly linking thiol-exchange chemistry to renal tubular acid-base (HCO3⁻/H⁺) transport
- Clinical or case-level evidence specific to tiopronin use in renal tubular acidosis
- A regulatory feasibility assessment given the drug's current non-marketed status

*Note: Nine additional lower-ranked predictions (adult polyglucosan body disease, multiple glycogen branching enzyme deficiency subtypes, TCA cycle disorder, pyruvate metabolism disorder, fatty acid oxidation disorder, and disease of transporter activity) were also reviewed. All carry evidence level L4–L5 with either no supporting literature or only indirect/mechanistic-tool-use citations, and share the same "Hold" recommendation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Nimodipine
parent: 僅模型預測 (L5)
nav_order: 967
evidence_level: L5
indication_count: 2
---

# Nimodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Nimodipine: From Cerebral Vasospasm to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Nimodipine is a dihydropyridine calcium channel blocker classically used to prevent cerebral vasospasm following subarachnoid hemorrhage. The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, but this prediction is currently **unsupported by any clinical trials or published literature** — it is a pure model-driven signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no TW/US license records; drug is not currently marketed in this jurisdiction) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on general pharmacological knowledge, nimodipine is a highly brain-selective L-type calcium channel blocker, clinically used to reduce cerebral vasospasm after subarachnoid hemorrhage.

Homozygous Familial Hypercholesterolemia is caused by dysfunction in the LDLR/APOB/PCSK9 pathway, which impairs LDL cholesterol clearance. There is no known mechanistic overlap between vascular smooth-muscle calcium channel blockade and LDL receptor-mediated cholesterol metabolism.

The TxGNN score for this candidate is high (99.29%), but with zero supporting clinical trials, zero literature records, and no plausible mechanistic bridge identified from available data, this should be treated as a pure knowledge-graph association rather than a biologically grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5) with no clinical trials, no literature, and no identifiable mechanistic link between nimodipine's calcium-channel activity and HoFH's lipid-metabolism pathology. The drug is also not currently marketed in this jurisdiction, so there is no existing regulatory or safety baseline to build on.

**To proceed, the following is needed:**
- TFDA/US package insert data (key warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Preclinical or mechanistic studies linking calcium channel blockade to LDL receptor pathway or lipid metabolism
- At minimum, case reports or observational data before considering any further evaluation stage

*Note: A second TxGNN candidate, nephrogenic syndrome of inappropriate antidiuresis (score 99.05%), is also flagged in this evidence pack with the same L5/Hold status and no supporting evidence — not detailed here per report scope, but subject to the same data gaps.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Disopyramide
parent: 僅模型預測 (L5)
nav_order: 615
evidence_level: L5
indication_count: 10
---

# Disopyramide
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

# Disopyramide: From Cardiac Arrhythmia to Tourette Syndrome

## One-Sentence Summary

> Disopyramide is a Class Ia antiarrhythmic (sodium channel blocker) historically used for ventricular and atrial arrhythmias.
> The TxGNN model's top-ranked prediction suggests it may be effective for **Tourette Syndrome**,
> but this direction currently has **0 clinical trials** and **0 publications** supporting it —
> the model's own mechanistic assessment flags this as a likely knowledge-graph artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular/atrial cardiac arrhythmias (Class Ia antiarrhythmic) — inferred from known drug classification; no Taiwan license/indication text available (drug not marketed in Taiwan) |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` is unrecorded). Based on the drug-level information that is available, disopyramide is a Class Ia antiarrhythmic that blocks cardiac sodium channels, and its efficacy in ventricular/atrial arrhythmias is well established.

However, the repurposing rationale supplied alongside this specific prediction is explicit that **no plausible mechanistic link exists** between sodium channel blockade and Tourette syndrome. Tourette syndrome pathophysiology centers on dopaminergic and cortico-striato-thalamo-cortical circuit dysfunction, a pathway disopyramide is not known to act on. The model itself notes that its high score likely reflects an indirect association captured in the knowledge graph (e.g., co-occurring drug–gene–disease nodes) rather than a real pharmacological relationship.

Given the absence of any supporting mechanism, clinical trials, or literature, this specific top-ranked prediction should be treated as a low-confidence, exploratory signal only — not as a candidate ready for further clinical assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Disopyramide currently has no registered marketing authorizations in Taiwan (market status: 未上市 / Not Marketed; 0 total licenses on file), so no NDA/license table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: The TFDA label warnings/contraindications for this drug are flagged as a **Blocking** data gap (DG001) — this data must be obtained before any safety (S1) evaluation can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a very high TxGNN score, but there is no clinical trial, literature, or mechanistic evidence to support it, and the model's own analysis suggests the score may be a spurious knowledge-graph association rather than a genuine pharmacological relationship. This places the candidate firmly at evidence level L5 with no basis to advance to further evaluation stages.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Blocking gap, DG001) — required before any safety (S1) evaluation can begin
- Detailed mechanism of action (MOA) data from DrugBank (High-priority gap, DG002)
- Any preclinical or mechanistic studies specifically linking sodium channel blockade to tic disorders or dopaminergic pathways, if this direction is pursued further
- Independent pharmacological review to confirm or rule out the knowledge-graph noise hypothesis before committing further resources

**Note on alternative candidates:** Two lower-ranked predictions in this evidence pack — *idiopathic neonatal atrial flutter* (rank 7) and *multifocal atrial tachycardia* (rank 9) — carry substantially stronger mechanistic plausibility, since both are cardiac arrhythmias consistent with disopyramide's known Class Ia antiarrhythmic action, and are already staged at "Research Question" (L4) rather than "Hold." These may warrant prioritization over the top-scored but mechanistically unsupported Tourette syndrome prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


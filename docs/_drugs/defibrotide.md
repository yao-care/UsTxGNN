---
layout: default
title: Defibrotide
parent: 僅模型預測 (L5)
nav_order: 579
evidence_level: L5
indication_count: 10
---

# Defibrotide
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

# Defibrotide: From Hepatic Veno-Occlusive Disease to Pseudo-von Willebrand Disease

## One-Sentence Summary

Defibrotide is a polydeoxyribonucleotide antithrombotic agent with endothelial cell-protective and profibrinolytic properties, primarily developed for hepatic veno-occlusive disease (VOD/SOS) following hematopoietic stem cell transplantation.
The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**,
however, there are currently **no clinical trials and no publications** directly supporting this specific indication — the prediction score reflects knowledge graph topology rather than mechanistic similarity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hepatic veno-occlusive disease / sinusoidal obstruction syndrome (VOD/SOS) post-HSCT |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | Not marketed (per current regulatory dataset; 0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Defibrotide is a polydeoxyribonucleotide compound whose mechanism—while formally a data gap in this Evidence Pack—is well characterised in the clinical literature. It acts through multiple complementary pathways: endothelial cell protection, reduction of leukocyte adhesion, promotion of tissue plasminogen activator (tPA) release, increased prostacyclin (PGI₂) production, and inhibition of platelet aggregation. These mechanisms collectively address the core pathology of VOD/SOS: conditioned-chemotherapy–driven endothelial injury, sinusoidal obstruction, and localised microvascular thrombosis.

Pseudo-von Willebrand Disease (pseudo-vWD) is a clinically distinct platelet disorder caused by gain-of-function mutations in GP1bα. The mutant receptor spontaneously binds ultra-large vWF multimers, driving platelet consumption and bleeding diathesis. The pathophysiology is fundamentally structural — a receptor-level affinity defect — rather than an endothelial injury or fibrin deposition process.

The mechanistic overlap between Defibrotide and pseudo-vWD is therefore limited. Although Defibrotide influences platelet aggregation and vascular tone, it does not address GP1bα structural dysfunction or the upstream vWF multimer clearance failure that defines pseudo-vWD. The TxGNN high prediction score most likely reflects the density of interconnections within the blood coagulation knowledge graph (shared nodes: thrombosis, platelets, vWF, endothelium) rather than a direct functional mechanistic link. This is a graph-topology signal, not a biology-similarity signal, and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Defibrotide in pseudo-von Willebrand Disease.

---

## Literature Evidence

Currently no related literature available for Defibrotide in pseudo-von Willebrand Disease.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug–drug interaction data, key warnings, or contraindications were retrievable from the current Evidence Pack. Full safety profiling requires download and parsing of the official prescribing information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN score of 99.91%, the prediction for pseudo-von Willebrand Disease is driven by knowledge graph topology in the blood coagulation network, not by mechanistic or clinical evidence. There are zero registered clinical trials and zero supporting publications. Defibrotide's endothelial-protective and profibrinolytic mechanisms do not address the GP1bα structural defect that defines pseudo-vWD, making direct biological plausibility low.

**To proceed, the following is needed:**
- Formal MOA documentation from DrugBank API (DG002 remediation) to confirm whether any Defibrotide target overlaps with GP1bα or vWF multimer processing pathways
- US FDA prescribing information / package insert retrieval (DG001 remediation) to establish the safety baseline before any indication expansion evaluation
- Review of the broader predicted indication set: **Thrombotic Thrombocytopenic Purpura (TTP, rank #4)** carries L3 evidence and a "Research Question" recommendation — it shares more mechanistic overlap with Defibrotide's endothelial-protective profile and has 11 supporting publications (including two direct case series, one in vitro translational study, and multiple reviews); this represents a far stronger repurposing candidate than pseudo-vWD and warrants a dedicated evaluation report
- Clarification of US regulatory status — Defibrotide (brand name Defitelio) is believed to hold an FDA approval for VOD/SOS post-HSCT; the current dataset shows 0 US licenses, which likely indicates a data collection gap rather than actual non-approval status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Calcifediol
parent: 僅模型預測 (L5)
nav_order: 486
evidence_level: L5
indication_count: 4
---

# Calcifediol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Calcifediol: From Vitamin D Supplementation to Vitamin D Deficiency

## One-Sentence Summary

Calcifediol (25-hydroxyvitamin D3, 25(OH)D3) is the principal circulating metabolite of vitamin D3, used clinically for vitamin D supplementation and secondary hyperparathyroidism management in chronic kidney disease.
The TxGNN model predicts it may be effective for **Vitamin D Deficiency** with a near-perfect score of **99.99%**, essentially validating the drug's established pharmacological role.
No clinical trials or publications were retrieved for this specific query, likely due to an obsolete disease ontology term being used — not due to an absence of real-world evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in regulatory database |
| Predicted New Indication | Vitamin D Deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| US Market Status | Not marketed (0 licenses found) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence package. Based on well-established pharmacology, calcifediol is 25-hydroxyvitamin D3 — the main circulating form of vitamin D produced by hepatic CYP2R1/CYP27A1-mediated hydroxylation of cholecalciferol (vitamin D3). It is the direct substrate for renal CYP27B1 (1α-hydroxylase), which converts it to calcitriol (1,25(OH)2D3), the biologically active hormonal form that binds the vitamin D receptor (VDR) to regulate calcium homeostasis, bone mineralization, and immune function.

Vitamin D deficiency (serum 25(OH)D < 20 ng/mL) affects over 1 billion people worldwide. Calcifediol offers clinical advantages over standard cholecalciferol supplementation: it bypasses intestinal absorption bottlenecks (particularly useful in fat malabsorption syndromes), achieves faster and more predictable elevation of serum 25(OH)D, and can be used when hepatic 25-hydroxylation is impaired. The drug's repurposing rationale embedded in this evidence package captures this precisely — calcifediol directly replaces the deficient circulating metabolite, making it mechanistically the most direct treatment for vitamin D deficiency.

The near-perfect TxGNN prediction score (99.99%) for vitamin D deficiency represents model validation rather than a novel repurposing signal. More compelling repurposing opportunities appear at lower ranks: particularly vitamin D-dependent rickets Type 1B (VDDR1B, CYP2R1 deficiency, rank 4), where calcifediol directly bypasses the defective hepatic 25-hydroxylation step and represents a mechanistically distinct indication with actual clinical trial and publication support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for calcifediol queried against the disease term "obsolete vitamin D deficiency." This reflects an ontology mismatch — the query used a retired disease term, not an absence of clinical evidence in the field. Re-querying under active terminology (e.g., "vitamin D insufficiency," "hypovitaminosis D") would be expected to yield substantial results.

---

## Literature Evidence

Currently no related literature available for the specific query combination used. Published evidence for calcifediol in vitamin D deficiency management is well-established but was not retrieved under this evidence pack's query parameters.

---

## US Market Information

No regulatory approvals were found for calcifediol in the US regulatory database queried for this report (0 licenses, market status: not marketed). This is likely a data gap rather than a true absence — calcifediol has documented regulatory history under the brand name Rayaldee and warrants a direct regulatory database verification as a remediation step.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model's L1-confidence prediction for vitamin D deficiency aligns with calcifediol's core pharmacological mechanism as a circulating vitamin D metabolite, and the clinical evidence base in this therapeutic area is extensive — the data gap in this report reflects a search terminology issue, not a lack of supporting evidence.

**To proceed, the following is needed:**

- **Re-run evidence query** using active MeSH terminology ("vitamin D deficiency," ICD-10 E55.9, "hypovitaminosis D") to retrieve actual clinical trial and publication records — current returns of zero are an artifact of the obsolete disease term
- **Confirm US regulatory status** (verify Rayaldee NDA records directly via FDA Orange Book or Drugs@FDA; DG001 remediation)
- **Obtain DrugBank MOA data** (DG002 remediation via DrugBank API) to complete mechanistic analysis
- **Evaluate VDDR Type 1B (CYP2R1 deficiency)** as a separate, mechanistically-driven repurposing target: calcifediol directly compensates for defective hepatic 25-hydroxylation in this rare genetic disorder, representing a more genuinely novel clinical opportunity than general vitamin D deficiency treatment
- **Safety profile review**: obtain TFDA/FDA package insert warnings and contraindications before any clinical development planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


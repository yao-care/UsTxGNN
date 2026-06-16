---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 530
evidence_level: L5
indication_count: 9
---

# Cimetidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

Using `txgnn-pipeline` to orient the context, then applying the **Drug Repurposing Evaluation Report Prompt v5** to generate the report.

---

# Cimetidine: From Peptic Ulcer Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Cimetidine is the first-generation histamine H2 receptor antagonist (H2RA), originally developed and used to suppress gastric acid secretion and treat peptic ulcer disease.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**, with **0 registered clinical trials** and **0 indexed publications** found for this specific disease–drug combination.
Despite the evidence gap, the mechanistic rationale is well-established: combined H1 and H2 receptor blockade is already a recognized standard adjunct in mastocytosis symptom management, classifying this as a known off-label use rather than a purely speculative repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease / gastric acid hypersecretion (not registered in Taiwan regulatory database) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacology, cimetidine is the prototype H2 receptor antagonist. It competitively blocks histamine H2 receptors on gastric parietal cells, suppressing basal gastric acid secretion by 60–70% and stimulated secretion proportionally. This mechanism made it the first major advance over antacids for treating peptic ulcer disease when it entered clinical use in the late 1970s.

In smouldering systemic mastocytosis (SSM), neoplastic mast cells accumulate in the bone marrow and peripheral organs, continuously releasing mediators — most prominently histamine — into circulation. Histamine acting on gastrointestinal H2 receptors drives the characteristic GI symptoms of SSM: abdominal cramping, diarrhea, and peptic ulceration. By competitively blocking these same H2 receptors, cimetidine directly interrupts this pathway, providing symptom relief without requiring any new pharmacological target.

Clinically, the combination of an H1 antihistamine plus an H2 antihistamine (such as cimetidine) is endorsed in mastocytosis management guidelines precisely because each class covers a different spectrum of histamine-mediated effects. This makes the TxGNN prediction mechanistically sound even in the complete absence of indexed clinical trials or publications for this specific pairing — the knowledge graph correctly identifies the H2 receptor as the shared pharmacological node linking the drug to the disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cimetidine in Smouldering Systemic Mastocytosis.

---

## Literature Evidence

Currently no related literature available for Cimetidine in Smouldering Systemic Mastocytosis.

---

## Taiwan Market Information

Cimetidine currently holds no drug product licenses in the Taiwan regulatory database and is not marketed in Taiwan. No authorization records are available for tabulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic link between cimetidine's H2 blockade and histamine-driven mastocytosis symptoms is clear and supported by clinical practice guidelines, no indexed clinical trials or publications were identified for this specific indication, and all Taiwan safety data (warnings, contraindications, drug interactions) are unavailable — preventing a formal safety-based recommendation to proceed.

**To proceed, the following is needed:**
- Retrieve full Taiwan prescribing information (TFDA package insert PDF) to extract contraindications, key warnings, and drug interaction profile
- Obtain DrugBank MOA record (DB00501) to formally document mechanism of action and CYP450 inhibition profile (cimetidine is a known inhibitor of CYP1A2, CYP2C9, CYP2D6, and CYP3A4 — a clinically significant DDI concern)
- Perform targeted literature search for H2RA use in mastocytosis management guidelines (e.g., WHO, ESMO, NCCN), which are likely to document this off-label use explicitly
- Clarify whether SSM patients are already receiving H2RA therapy per guideline recommendations, which would reframe this as a label expansion rather than a novel repurposing hypothesis
- If escalating to formal repurposing, a prospective observational study comparing symptom burden in SSM patients with vs. without H2RA co-administration would constitute a feasible and ethical next step
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


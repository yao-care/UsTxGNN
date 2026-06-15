---
layout: default
title: Ascorbic Acid
parent: 僅模型預測 (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
---

# Ascorbic Acid
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

# Ascorbic Acid: From Vitamin C Deficiency to Non-Syndromic Esophageal Malformation

## One-Sentence Summary

Ascorbic acid (Vitamin C) is an essential water-soluble nutrient classically used to prevent and treat vitamin C deficiency (scurvy), supporting collagen synthesis, immune function, and antioxidant defense.
The TxGNN model predicts it may be effective for **Non-Syndromic Esophageal Malformation**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin C deficiency (scurvy) prevention and treatment |
| Predicted New Indication | Non-Syndromic Esophageal Malformation |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | No US approval records found in dataset |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the system. Based on known information, ascorbic acid is an essential cofactor for prolyl hydroxylase and lysyl hydroxylase — the enzymes responsible for hydroxylating proline and lysine residues during collagen synthesis. Without adequate Vitamin C, these enzymes cannot function, collagen triple helices become unstable, and connective tissues throughout the body deteriorate. This is the molecular basis of scurvy.

Non-syndromic esophageal malformation is a rare congenital structural defect of the esophagus (most often esophageal atresia ± tracheoesophageal fistula). Normal esophageal morphogenesis during embryogenesis requires intact collagen scaffolding for epithelial-mesenchymal patterning. In theory, severe gestational Vitamin C deficiency could impair collagen deposition during this critical developmental window and contribute to structural esophageal anomalies.

However, this mechanistic link is highly speculative. No preclinical embryology studies, animal models, or human data have tested this hypothesis. The extremely high TxGNN score (99.96%, rank 1,513 out of all predictions) most plausibly reflects broad knowledge-graph connectivity between the "ascorbic acid" node and esophageal-structure nodes via collagen/connective-tissue pathways — a topology artifact rather than validated therapeutic signal. This prediction should not be interpreted as clinical repurposing evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No US NDA-level authorization records were found for ascorbic acid in this dataset.

> **Note:** Ascorbic acid (Vitamin C) is one of the most widely used nutrients globally and is available in numerous OTC supplement products and compounded injectable formulations. The absence of records in this dataset likely reflects a data gap in the NDA query rather than a genuine non-marketed status.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Non-syndromic esophageal malformation is a rare congenital structural defect with zero clinical or preclinical evidence linking ascorbic acid to its prevention or treatment. The high TxGNN score reflects indirect knowledge-graph topology (collagen synthesis → connective tissue → esophageal structure), not a validated therapeutic mechanism, and should not trigger further development resources at this stage.

**To proceed, the following is needed:**
- Preclinical embryology studies testing whether gestational Vitamin C deficiency alters esophageal morphogenesis in animal models
- Epidemiological data examining maternal Vitamin C status and rates of congenital esophageal anomalies
- Mechanistic studies confirming collagen-pathway involvement in esophageal atresia/malformation pathogenesis
- Resolution of MOA data gap (DrugBank API query recommended) and US market/label data gap (NDA query or OTC monograph review)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


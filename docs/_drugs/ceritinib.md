---
layout: default
title: Ceritinib
parent: Model Prediction Only (L5)
nav_order: 513
evidence_level: L5
indication_count: 10
---

# Ceritinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ceritinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib is an oral ALK/ROS1 tyrosine kinase inhibitor, used for ALK-rearranged non-small cell lung cancer.
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **0 clinical trials** and **0 publications** currently support this prediction.
It is a graph-based prediction only, and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive non-small cell lung cancer (from the supplied literature; the US license record has no indication text) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ceritinib inhibits the receptor tyrosine kinases ALK and ROS1. Its established use is in ALK-rearranged non-small cell lung cancer, a malignancy driven by ALK fusion. Literature in the pack also describes activity against IGF1R and FAK in CNS tumor studies.

The supplied data do not document a mechanistic link between ALK/ROS1 signaling and gingival fibromatosis, a benign overgrowth of gum tissue. The TxGNN score (99.86%, rank 4,356) reflects a pattern in the knowledge graph, not biological or clinical evidence. Detailed mechanism-of-action data from DrugBank is also not currently available, so a mechanistic bridge cannot be built at this stage.

Gingival fibromatosis is a non-malignant, fibrotic condition, while ceritinib is an oncology drug whose benefit depends on an ALK-driven tumor. This difference in disease biology, plus the drug's toxicity profile, makes the prediction hard to justify without supporting data.

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
| NDA211225 | ZYKADIA (Novartis Pharmaceuticals Corporation) | Tablet, film coated (oral) | Not listed in the record |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions. Literature notes gastrointestinal toxicity, which is reduced with the 450 mg with-food regimen (ASCEND-8) |
| Monitoring Items | ECG for QT prolongation (flagged in the literature); other laboratory monitoring per the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

The Evidence Pack contains no package insert warnings, contraindications, or drug interaction data. Published literature on ceritinib in its approved setting flags the following:

- **QT prolongation**: reported for ceritinib and other lung cancer TKIs, with ECG screening advised in higher-risk patients.
- **Hypersensitivity and lung toxicity**: a case report describes diffuse infiltrative lung disease, pericarditis and pleural effusion with ceritinib hypersensitivity.
- **Gastrointestinal toxicity**: dose- and food-dependent, as shown in ASCEND-8.
- **Thromboembolism**: a network meta-analysis addresses its incidence with ALK-TKIs in lung cancer.

Please refer to the package insert for complete safety information. Because gingival fibromatosis is benign, this risk profile would weigh heavily in any risk-benefit assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials, no publications, and no documented mechanistic link between ALK/ROS1 inhibition and gingival fibromatosis. Ceritinib's toxicity profile is difficult to justify in a benign condition without supporting evidence.

Among the other predictions in the pack, lung hilum carcinoma and pulmonary sulcus neoplasm are the most biologically plausible, since both are lung malignancies that may be ALK-positive. Neither has any trial or literature evidence yet.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking ALK, ROS1, or a related kinase pathway to gingival fibromatosis
- Mechanism-of-action data for ceritinib (DrugBank)
- Package insert warnings, contraindications, and drug interaction data
- A risk-benefit assessment for a benign, non-life-threatening indication

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


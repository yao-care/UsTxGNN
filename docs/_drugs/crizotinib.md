---
layout: default
title: Crizotinib
parent: Model Prediction Only (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK-Positive Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Crizotinib is an oral kinase inhibitor targeting ALK, ROS1 and MET, and the literature in this pack describes it as approved for ALK-positive non-small cell lung cancer.
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the graph model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the license data. The literature describes approval for ALK-positive NSCLC. |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 license records (2 unique NDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Literature elsewhere in the pack describes crizotinib as an ATP-competitive inhibitor of the receptor tyrosine kinases c-Met, ALK and ROS1. It is established in ALK- and ROS1-driven lung cancer.

The prediction does not have a clear mechanistic bridge. The data supplied document no link between ALK, ROS1 or MET inhibition and hereditary gingival fibromatosis, which is a benign overgrowth of gum tissue. Nothing supports the 99.81% score beyond the model itself, so it should be read as a hypothesis-generation signal. A mechanism would have to be worked out before any further investment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA217581 | Xalkori (Pfizer) | Capsule, coated pellets |
| NDA202570 | Xalkori (Pfizer) | Capsule |

Both products are oral. The five license records in the source contain only these two unique NDAs, and none includes an approved-indication text.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/MET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Literature reports hepatotoxicity, cardiac effects (bradycardia, QT prolongation) and drug-induced lung injury, so liver function, heart rate/ECG and respiratory symptoms are relevant. CBC is also advisable. |
| Handling Protection | Please refer to the package insert and institutional hazardous-drug handling policy |

## Safety Considerations

No package insert warnings, contraindications or drug-interaction data were available in the source record. Please refer to the package insert for safety information.

The pack's literature for other predicted indications reports these crizotinib safety signals:
- A case of fatal fulminant liver failure
- Multiple cardiac toxicities in one patient (bradycardia, QT prolongation, ventricular arrhythmia, pericarditis)
- Drug-induced organizing pneumonia and lung injury
- A multisystem toxicity review covering hepatotoxicity, cardiotoxicity and interstitial lung disease

These are relevant if crizotinib were ever considered for a benign condition, where the risk-benefit balance is much tighter than in advanced cancer.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only prediction (L5) with no trials, no literature and no documented mechanistic link, for a benign condition in which the known toxicity profile of crizotinib weighs heavily.

**To proceed, the following is needed:**
- A plausible mechanistic link between ALK/ROS1/MET signaling and gingival fibromatosis, shown by preclinical or genetic evidence
- Original indication and mechanism of action data, plus package insert warnings and contraindications (currently missing)
- A benefit-risk assessment given the reported hepatic, cardiac and pulmonary toxicity

For prioritization: in the same prediction list, lung hilum carcinoma and lung germ cell tumor have some supporting evidence (L4, Research Question), though still case-report or tumor-agnostic level.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


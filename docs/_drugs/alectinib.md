---
layout: default
title: Alectinib
parent: Model Prediction Only (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Alectinib
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

# Alectinib: From ALK-Positive Non-Small-Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Alectinib is an oral ALK/RET tyrosine kinase inhibitor, approved for ALK-positive non-small-cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis**, a rare benign gum overgrowth disorder.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive NSCLC (taken from the evidence pack's rationale text; the license record has no indication text) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.97% (model rank 1477) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the database. From the pack's rationale text, alectinib is an ALK/RET tyrosine kinase inhibitor. Its proven benefit is in ALK-rearranged lung cancer, where ALK is the driver of tumor growth.

This prediction has no supporting mechanism. The supplied data documents no ALK or RET involvement in gingival fibromatosis. That disease is a benign, non-malignant tissue overgrowth, and it is biologically distant from ALK-driven lung cancer.

The score of about 0.9997 comes from graph-based prediction only. The other top candidates for this drug score almost identically, so the score does not help rank them. It should be read as a hypothesis-generation signal, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA208434 | ALECENSA | Capsule (oral) | Genentech, Inc. |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/RET kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate. Anemia is a known effect, and a published case report describes alectinib-induced hemolytic anemia (PMID 36604860) |
| Emetogenicity Classification | Low (typical for oral kinase inhibitors; not from the supplied data) |
| Monitoring Items | CBC, liver function. Please refer to the package insert for the full list |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature and no mechanistic link (Evidence Level L5). A benign gum disorder is a poor fit for a drug developed for ALK-driven cancer. A weak benefit would also have to be weighed against the safety profile of a systemic oncology drug.

**To proceed, the following is needed:**
- A plausible biological link between ALK/RET signaling and gingival fibromatosis, for example from preclinical or expression data
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Detailed MOA data from DrugBank
- A benefit-risk assessment for a benign, non-life-threatening condition

**Other candidates for this drug:**
- **Lung germ cell tumor (rank 7)** is the only candidate with trial and case-report evidence, at Evidence Level L4. The literature is case reports of ALK-fusion-positive lung neuroendocrine tumors that responded to alectinib, none of it on germ cell tumors. Two trials are registered:
  - NCT04644315 was terminated after 1 participant.
  - NCT05770037 (DETERMINE, n=30) is still recruiting.
  - This candidate is better suited to a molecularly stratified research question, with ALK testing required, than to a repurposing decision.
- **Lung benign neoplasm (rank 5)** has 20 papers, but all concern ALK-positive NSCLC, which is malignant. This looks like a disease-term mapping artifact and is not evidence for the predicted indication.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


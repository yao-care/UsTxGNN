---
layout: default
title: Ponatinib
parent: Model Prediction Only (L5)
nav_order: 1064
evidence_level: L5
indication_count: 2
---

# Ponatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Ponatinib: From a Multi-Kinase Inhibitor to Gingival Fibromatosis

## One-Sentence Summary

Ponatinib is an oral multi-kinase inhibitor marketed in the US as Iclusig. The TxGNN model predicts it may be effective for **gingival fibromatosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license records (all under NDA203469) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied data. Ponatinib is described as a multi-kinase inhibitor that targets BCR-ABL, FGFR, PDGFR, VEGFR and SRC-family kinases.

Gingival fibromatosis is a fibroblast-driven overgrowth of gum tissue. In theory, PDGFR and FGFR signaling could contribute to it, and ponatinib inhibits both. This link is speculative. The supplied data contain no trials, literature or mechanistic studies connecting ponatinib to this condition, and the high score is a model output, not evidence. The score's rank of 20,750 also suggests it should not be read as a strong signal.

**Other prediction:** The second-ranked prediction, liposarcoma (score 99.00%), has one supporting paper. It is a preclinical kinase-profiling and drug-screening study (PMID 29132397, *J Hematol Oncol*, 2017). It has not been confirmed that ponatinib itself was tested in that study. Liposarcoma is a more biologically plausible direction for a kinase inhibitor and may be worth a separate evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA203469 | Iclusig | Film-coated tablet (oral) | Takeda Pharmaceuticals America, Inc. |

The four license records are identical in the supplied data and are shown once. No approved-indication text was provided.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Boxed warnings (from the evidence pack's rationale text, not a label extract):** arterial occlusive events, venous thromboembolism, heart failure and hepatotoxicity. These must be verified against the current US package insert.
- **Drug interactions:** no interaction data were found.

The serious cardiovascular and hepatic risks would be hard to justify for a benign condition such as gingival fibromatosis without strong efficacy evidence.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, preclinical or mechanistic support in the supplied data. It is also blocked by missing package insert safety data (blocking gap DG001), and ponatinib's boxed warnings weigh heavily against use in a non-life-threatening condition.

**To proceed, the following is needed:**
- The full US package insert, including warnings, contraindications and approved indications (blocking gap)
- Mechanism of action data from DrugBank
- A literature and trial search for ponatinib or other FGFR/PDGFR inhibitors in gingival fibromatosis and related fibroproliferative conditions
- Preclinical evidence that PDGFR/FGFR signaling drives gingival fibromatosis
- A benefit-risk assessment against the boxed warnings
- Consideration of prioritizing the liposarcoma prediction, after checking the full text of PMID 29132397 to see whether ponatinib was tested

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


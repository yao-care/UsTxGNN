---
layout: default
title: Alectinib
parent: Model Prediction Only (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
monitor_inn: "ALECTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa"]
last_modified_at: 2026-10-14
description: "Alectinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung carcinoma (lung cancer)"
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

# Alectinib: From Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Alectinib is an oral ALK inhibitor originally used to treat non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **no clinical trials and no publications** currently support this prediction.
This is a model-only signal and is not backed by any real-world evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma (lung cancer) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From general knowledge, alectinib is a selective inhibitor of anaplastic lymphoma kinase (ALK), with activity against RET as well. Its efficacy in ALK-positive NSCLC is well established.

For gingival fibromatosis, the link is weak. Hereditary gingival fibromatosis is not known to be driven by ALK or RET signalling, and no mechanistic rationale has been established. The very high TxGNN score reflects a pattern in the knowledge graph rather than a biological or clinical finding. The other top-ranked predictions show the same pattern: none has a plausible ALK-dependent mechanism, apart from tumour types that overlap with the existing lung cancer use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

For context, the only trial found among the top 10 predictions is NCT04644315, a Phase 2 study of alectinib in ALK-positive solid tumours, linked to the lung germ cell tumour prediction. It was terminated after enrolling 1 participant and gives no usable efficacy data. It is not related to gingival fibromatosis.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208434 | ALECENSA (Genentech, Inc.) | Capsule (oral) | Not listed; status: cancelled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/RET tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (published reports note anaemia, including a case of haemolytic anaemia) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; published reports suggest attention to blood counts, liver function, triglycerides/pancreatitis, weight and cardiac conduction |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 92 interactions were recorded in the interaction database. Most of those listed are Moderate. One is Major: **aminolevulinic acid** (a photosensitising agent). Moderate examples include dolasetron, naltrexone, mefloquine, quinine, atazanavir, bedaquiline, methoxsalen, and several beta-blockers (acebutolol, atenolol, betaxolol, bisoprolol). The full list should be reviewed before any clinical use.
- **Safety signals from published case reports**: hypertriglyceridaemia-induced pancreatitis, haemolytic anaemia, DRESS syndrome, erythema multiforme, and weight gain.

Package insert warnings and contraindications were not available for this report; please refer to the package insert for them.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature, and no plausible ALK/RET-related mechanism in gingival fibromatosis. The only NDA on record is cancelled, and the interaction burden is substantial. None of the other top-10 predictions offers a stronger signal. Those with abundant literature (such as lung benign neoplasm) are driven by existing NSCLC studies and do not transfer to the predicted indication.

**To proceed, the following is needed:**
- A mechanistic rationale showing ALK or RET involvement in gingival fibromatosis, or a related fibroproliferative pathway
- Mechanism of action data (MOA) and FDA package insert warnings and contraindications
- Preclinical evidence in a relevant model
- Clarification of the cancelled US regulatory status and of available formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


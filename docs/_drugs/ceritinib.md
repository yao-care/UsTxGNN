---
layout: default
title: Ceritinib
parent: Model Prediction Only (L5)
nav_order: 513
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ceritinib: predicted new indication Gingival fibromatosis (evidence level L5). Approved use: Non-small cell lung cancer (NSCLC)"
monitor_inn: "CERITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "junctional epidermolysis bullosa"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ceritinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis
{: .text-alpha }

## One-Sentence Summary

Ceritinib is an oral ALK inhibitor originally used to treat ALK-positive non-small cell lung cancer.
The TxGNN model predicts it may be effective for **gingival fibromatosis**,
but **no clinical trials and no publications** specific to this indication were found, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (NSCLC) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ceritinib inhibits ALK, ROS1 and IGF-1R. Its efficacy in ALK-rearranged NSCLC is well established, including a Phase 3 trial of first-line ceritinib versus platinum chemotherapy (ASCEND-4). The data compiled for this report do not include a detailed mechanism-of-action entry, so the mechanistic discussion relies on the known targets above.

No mechanistic link has been identified between these targets and gingival fibromatosis, a condition of gingival tissue overgrowth. A lung cancer drug acting on ALK-driven tumors has no obvious basis for treating it. The very high TxGNN score is a computational association from a knowledge graph, with no trial or literature support, and should be treated with caution.

Other high-scoring predictions for ceritinib include lung hilum carcinoma and pulmonary sulcus (Pancoast) neoplasm. These are biologically plausible because they are lung cancers, but they largely overlap with the existing NSCLC indication rather than representing true repurposing. Many other top predictions (for example fibroma of lung, hamartoma of lung, inclusion body myopathy with Paget disease, and junctional epidermolysis bullosa) have no identified mechanistic basis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211225 | ZYKADIA (Novartis Pharmaceuticals Corporation) | Tablet, film coated | Not listed in the compiled data; status: cancelled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/IGF-1R tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Published reports also discuss QT prolongation and cardiac toxicity, renal effects, and hypersensitivity with ALK inhibitors; liver function and ECG monitoring are commonly considered. |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. The listed ones include **Major** interactions with triamcinolone and budesonide. Moderate interactions include acid-suppressing drugs (famotidine, ranitidine, rabeprazole, omeprazole), corticosteroids (hydrocortisone, dexamethasone, betamethasone), antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, canagliflozin, albiglutide), and others such as loperamide, aprepitant and bisacodyl.
- **Other published safety signals (in NSCLC use)**: QT prolongation and cardiac toxicity, renal effects, and hypersensitivity reactions with ceritinib have been described in the literature compiled for this report.

Label warnings and contraindications were not available in the compiled data. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No clinical trials or literature address gingival fibromatosis, no mechanistic link to ceritinib's targets is known, and the only US license is cancelled. The evidence level is L5.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis linking ALK, ROS1 or IGF-1R signaling to gingival fibromatosis, supported by preclinical data
- Mechanism-of-action data and FDA package insert warnings and contraindications (currently unavailable)
- Clarification of the commercial and regulatory availability of ceritinib, given the cancelled NDA
- A safety plan for a non-oncology population, since ceritinib is an oncology drug with notable toxicities and many drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


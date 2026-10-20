---
layout: default
title: Brigatinib
parent: Model Prediction Only (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Brigatinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung cancer"
monitor_inn: "BRIGATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Brigatinib
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

# Brigatinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Brigatinib is an oral kinase inhibitor, originally used to treat non-small cell lung cancer (ALK-positive disease).
The TxGNN model predicts it may be effective for **Gingival Fibromatosis** (the top-ranked prediction), but **no clinical trials and no publications** currently support this specific indication.
This is a purely computational prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (from the knowledge graph; the US label text is not available in the data compiled for this report) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single NDA is recorded as cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, brigatinib is a next-generation ALK inhibitor that also inhibits other tyrosine kinases (including EGFR and FAK). Its efficacy in ALK-positive non-small cell lung cancer has been established in the Phase 3 ALTA-1L trial.

For gingival fibromatosis, no plausible ALK-, EGFR- or FAK-driven mechanism has been established. The high TxGNN score (0.999) reflects a computational association only, and there is no trial or publication to support it. The prediction should be treated as a hypothesis, not a signal for development.

**Other predictions of note (for context):**
- **Lung-related labels** (fibroma of lung, hamartoma of lung, lung hilum carcinoma, pulmonary sulcus neoplasm, lung benign neoplasm): there is no distinct repurposing signal. ALK-positive carcinomas are already covered by the approved indication, and the benign-lesion labels have no supporting evidence. The literature matched to "lung benign neoplasm" concerns ALK-positive NSCLC and is likely a lexical artifact.
- **NF2-related schwannomatosis** (retrieved under the label of rank 10, a rare syndrome): this is the most credible repurposing lead in the data. Brigatinib inhibits multiple tyrosine kinases, including FAK signaling in NF2-deficient cells. It shrank meningioma and schwannoma in preclinical models (PMID 34264955), and a clinical study in progressive tumors has been published (PMID 38904277). The disease label itself appears to be a mismatch and should be re-mapped before any decision.
- **Lung germ cell tumor:** only indirect case-level and preclinical ALK-related findings (neuroblastoma, lung large cell neuroendocrine carcinoma, pheochromocytoma). There is no germ-cell-tumor-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

For reference, the highest-quality evidence for the closest alternative lead (NF2-related schwannomatosis) is shown below:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38904277](https://pubmed.ncbi.nlm.nih.gov/38904277/) | 2024 | Clinical study | New England Journal of Medicine | Brigatinib in NF2-related schwannomatosis with progressive tumors |
| [34264955](https://pubmed.ncbi.nlm.nih.gov/34264955/) | 2021 | Preclinical | PLoS One | Tumor shrinkage in NF2-deficient meningioma and schwannoma through inhibition of multiple tyrosine kinases, but not ALK |
| [34987411](https://pubmed.ncbi.nlm.nih.gov/34987411/) | 2021 | Case report | Frontiers in Pharmacology | Fatal tumor lysis syndrome with brigatinib in a lung adenocarcinoma patient |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208772 | Alunbrig (Takeda Pharmaceuticals America, Inc.) | Tablet, film coated | Indication text not available; status: cancelled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions:** The interaction screen returned 100 interacting drugs. Examples of **Major** interactions: aprepitant, dexamethasone and clarithromycin. Examples of **Moderate** interactions: acid-reducing agents (famotidine, ranitidine, rabeprazole, cimetidine), antidiabetic agents (metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin), loperamide, morphine, and cisapride.
- **Literature safety signals:** A fatal tumor lysis syndrome case (PMID 34987411) and cardiovascular toxicity analyses in ALK-positive lung cancer are reported. A benign indication such as gingival fibromatosis would require a high risk-benefit bar for a kinase inhibitor with pulmonary toxicity.

For label warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gingival fibromatosis prediction has a high model score but no trials, no literature and no plausible mechanism (Evidence Level L5). Brigatinib's US NDA is also recorded as cancelled. The benign nature of the condition makes the safety bar high for a kinase inhibitor.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic rationale linking brigatinib's targets to gingival fibromatosis
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Re-mapping of the rank 10 label to NF2-related schwannomatosis, and a separate evaluation of that indication, which has the strongest supporting evidence in the data
- Clarification of the cancelled US market status and the original approved indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


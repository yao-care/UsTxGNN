---
layout: default
title: Ponatinib
parent: Model Prediction Only (L5)
nav_order: 1064
evidence_level: L5
indication_count: 2
monitor_inn: "PONATINIB"
predicted_indications: ["fibromatosis, gingival", "liposarcoma"]
last_modified_at: 2026-10-30
description: "Ponatinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Chronic myelogenous leukemia, BCR-ABL1 positive"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ponatinib: From Chronic Myelogenous Leukemia (BCR-ABL1 Positive) to Fibromatosis, Gingival
{: .text-alpha }

## One-Sentence Summary

Ponatinib was originally used to treat BCR-ABL1-positive chronic myelogenous leukemia.
The TxGNN model predicts it may be effective for **Gingival Fibromatosis**, but **no clinical trials and no publications** currently support this prediction.
The second-ranked prediction, liposarcoma, is supported by only **1 preclinical publication**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukemia, BCR-ABL1 positive |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 0.9904 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, ponatinib is a multi-targeted tyrosine kinase inhibitor acting on BCR-ABL, FGFR, PDGFR, VEGFR, SRC and KIT. Its efficacy in BCR-ABL1-positive chronic myelogenous leukemia is established, and in theory its kinase profile could affect fibroproliferative signaling.

However, no mechanism specific to gingival fibromatosis is documented in the available data, so the link is speculative. Gingival fibromatosis is a benign, non-life-threatening condition, and ponatinib's known cardiovascular and thrombotic toxicity would weigh heavily against its use there.

**Second prediction (for reference):** Liposarcoma (TxGNN score 0.9900, Evidence Level L4, "Research Question"). One 2017 preclinical study profiled kinases in liposarcoma and identified druggable targets. The data do not show whether ponatinib was among the active agents, so the link remains plausible but unconfirmed.

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis (or for liposarcoma in the data compiled for this report).

## Literature Evidence

For gingival fibromatosis: currently no related literature available.

For the second prediction, liposarcoma:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/) | 2017 | Preclinical (in vitro kinase profiling / RNAi and drug screening) | Journal of Hematology & Oncology | Kinase profiling of liposarcomas identified druggable kinase targets; whether ponatinib was among the active agents is not shown |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203469 (cancelled) | Iclusig (Takeda Pharmaceuticals America, Inc.) | Film-coated tablet | Not specified in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically CBC, liver function, and cardiovascular monitoring) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. The first 20 entries reviewed include:
  - **Major**: Acetylsalicylic acid, Clarithromycin
  - **Moderate**: Loperamide, Aprepitant, Dexamethasone, Naldemedine, Naltrexone, Metronidazole, Miconazole
  - **Minor**: Famotidine, Ranitidine, Cimetidine, Nizatidine, Rabeprazole, Omeprazole, Lansoprazole, Dexlansoprazole, Pantoprazole, Magnesium oxide, Naloxegol
- **Other safety information**: Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert. Ponatinib is generally known to carry cardiovascular and thrombotic toxicity warnings, which weigh heavily against use in a benign condition.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for gingival fibromatosis is a high model score, with no clinical trials, no literature, and no documented mechanistic link. Given ponatinib's serious toxicity profile and the benign nature of the condition, the risk-benefit balance is unfavorable. The liposarcoma prediction (L4) is better treated as a research question than as a development candidate.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (e.g., from DrugBank)
- Preclinical evidence of ponatinib activity in gingival fibromatosis fibroblast models, or confirmation of ponatinib activity in the liposarcoma kinase screen
- A risk-benefit assessment given the cardiovascular and thrombotic safety profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


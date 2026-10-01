---
layout: default
title: Mitomycin
parent: Model Prediction Only (L5)
nav_order: 936
evidence_level: L5
indication_count: 10
---

# Mitomycin
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

# Mitomycin: From Cytotoxic Cancer Chemotherapy to Solid Pseudopapillary Carcinoma of the Pancreas

## One-Sentence Summary

Mitomycin is a DNA cross-linking cytotoxic agent that is marketed in the US as an injectable chemotherapy. The TxGNN model predicts it may be effective for **solid pseudopapillary carcinoma of the pancreas**, but this prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text is blank in all listed licenses) |
| Predicted New Indication | Solid pseudopapillary carcinoma of pancreas |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDAs, i.e. generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Mitomycin is generally described as a bioreductive alkylating agent that cross-links DNA and inhibits DNA synthesis. This general cytotoxic activity is the only mechanistic basis for the prediction.

The link to this rare pancreatic subtype is weak. The same score (99.86%) is assigned to another rare pancreatic subtype, osteoclastic giant cell tumor of the pancreas. This suggests the score was propagated from a parent "pancreatic carcinoma" node in the knowledge graph rather than learned from subtype-specific evidence.

The original indication is also missing from the source data. Mitomycin has historically been used in gastrointestinal adenocarcinomas, including pancreatic adenocarcinoma. If so, part of the predicted pancreatic set may already fall under existing labeling and would not be true repurposing. This must be checked against the current label.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this indication.

Indirect items were found only for neighboring pancreatic predictions, and none shows mitomycin efficacy in a pancreatic subtype:
- **Malignant exocrine pancreas neoplasm** (rank 8, the broadest category and the most plausible): PMID 2140281 (1990) is a review of exocrine pancreatic cancer chemotherapy and may cover mitomycin-containing regimens. PMID 8361472 concerns tamoxifen and is not relevant.
- **Pancreatic intraductal papillary-mucinous neoplasm and carcinoma** (ranks 4 and 9): PMID 15983445 (2005) is a case report of pseudomyxoma peritonei with IPMN, and no mitomycin use is shown in the title.
- **Undifferentiated pancreatic carcinoma** (rank 7): PMID 2695183 (1989) is a general review of unknown primary tumors.

All of these need full-text review before they can be counted as evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA215687 | Mitomycin (Fresenius Kabi USA) | Lyophilized powder for injection | Not provided |
| ANDA216732 | Mitomycin (BluePoint Laboratories) | Lyophilized powder for injection | Not provided |
| ANDA202670 | Mitomycin (Bryant Ranch Prepack) | Lyophilized powder for injection | Not provided |
| ANDA064144 | Mitomycin (BluePoint Laboratories) | Lyophilized powder for injection | Not provided |

ANDA216732 appeared twice in the source data and is listed once here. Only injectable forms are listed.

## Cytotoxicity

The pack contains no toxicity data. The entries below reflect general knowledge of this drug class and should be checked against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating, DNA cross-linking) |
| Myelosuppression Risk | High (typically delayed and cumulative; both leukopenia and thrombocytopenia are expected) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential and platelets, renal function (watch for hemolytic uremic syndrome), liver function, pulmonary symptoms |
| Handling Protection | Must follow cytotoxic drug handling regulations. It is also a vesicant, so extravasation precautions apply. |

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found for mitomycin in the drug interaction query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or publications behind it. The score is tied with another rare subtype, which points to ontology propagation rather than subtype-specific signal. The regulatory and mechanism data needed for safety screening are also missing.

**To proceed, the following is needed:**
- The current US package insert, to confirm the approved indications (including any existing pancreatic labeling) and the warnings and contraindications
- Detailed mechanism of action data (MOA), for example from DrugBank
- Full-text review of PMID 2140281 and PMID 15983445 for any mitomycin-specific content
- A targeted search for mitomycin in pancreatic neuroendocrine or pseudopapillary tumors, since the broad "malignant exocrine pancreas neoplasm" entry is the only one with a plausible link
- Evaluation of route compatibility and similarity to the original indication (both still pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


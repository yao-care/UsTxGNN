---
layout: default
title: Capmatinib
parent: Model Prediction Only (L5)
nav_order: 493
evidence_level: L5
indication_count: 2
---

# Capmatinib
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

# Capmatinib: From Non-Small Cell Lung Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Capmatinib is an oral MET kinase inhibitor marketed in the US as TABRECTA. The Evidence Pack does not list its approved indication; from general knowledge of the label it is used for MET-driven non-small cell lung cancer.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are currently **0 clinical trials** and only **1 general review article** behind this direction. This is a model prediction without direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in the Evidence Pack (general knowledge: MET-driven non-small cell lung cancer) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both entries are NDA213591) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Capmatinib is known to be a selective MET tyrosine kinase inhibitor.

Preclinical literature suggests HGF/MET signaling may contribute to synovial angiogenesis and to the invasion of fibroblast-like synoviocytes in rheumatoid arthritis. Blocking MET could therefore plausibly dampen these processes.

However, no capmatinib-specific rheumatoid arthritis data were found. The high TxGNN score (0.994) is probably driven by similarity to other kinase inhibitors and is not clinical evidence. Because the original indication and MOA fields are missing, the mechanistic link cannot be validated further.

A second prediction, brachydactyly-syndactyly syndrome (score 99.03%), has no trials, no literature and no plausible mechanism. It is a congenital limb malformation, and a kinase inhibitor is unlikely to reverse it after birth. It is not pursued here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | Update on the properties of 62 FDA-approved small-molecule protein kinase inhibitors. It is a general class review and contains no capmatinib-specific rheumatoid arthritis data. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213591 | TABRECTA (Novartis Pharmaceuticals Corporation) | Tablet, film coated (oral) | Not listed in the data provided |

The Evidence Pack contains two identical entries for this NDA, shown once here.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MET tyrosine kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

No drug interactions were found in the queried data. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score and a general kinase-inhibitor review. There are no capmatinib-specific trials or literature for rheumatoid arthritis, so the evidence level is L5. The mechanism is plausible but unverified.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Preclinical or in vitro evidence of capmatinib activity on MET signaling in synoviocytes or arthritis models
- A benefit-risk comparison against existing rheumatoid arthritis therapies, since capmatinib is an oncology drug with its own safety profile

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


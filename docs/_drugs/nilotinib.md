---
layout: default
title: Nilotinib
parent: Model Prediction Only (L5)
nav_order: 966
evidence_level: L5
indication_count: 1
monitor_inn: "NILOTINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
last_modified_at: 2026-10-28
description: "Nilotinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L4). Approved use: Chronic myelogenous leukemia, BCR-ABL1 positive"
---

# Nilotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Nilotinib: From BCR-ABL1-Positive Chronic Myelogenous Leukemia to Dermatofibrosarcoma Protuberans
{: .text-alpha }

## One-Sentence Summary

Nilotinib is a tyrosine kinase inhibitor originally used to treat BCR-ABL1-positive chronic myelogenous leukemia.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**,
but currently there are **0 registered clinical trials** and **1 publication** (a review) supporting this direction, so the evidence is still at the hypothesis stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukemia, BCR-ABL1 positive |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 8) |
| Number of NDAs | 8 (authorizations of all types, including NDAs and ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of nilotinib's kinase profile, it is a BCR-ABL tyrosine kinase inhibitor that also inhibits PDGFR and KIT.

DFSP is typically driven by the COL1A1-PDGFB fusion, which causes constitutive autocrine activation of PDGFRB. Because nilotinib inhibits PDGFR, it plausibly blocks this driver pathway. This is the same class rationale that supports imatinib, which is established in unresectable or metastatic DFSP. The high TxGNN score (0.9931) is consistent with this shared-target logic.

Note that this link rests on general pharmacological knowledge rather than on mechanism data supplied for this report, and no clinical studies of nilotinib in DFSP were identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews small-molecule PDGFR inhibitors in neoplastic disorders, providing a general rationale for targeting the PDGFR pathway; it does not report nilotinib-specific DFSP data |

## US Market Information

Eight valid authorizations are listed. Approved indication text was not available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022068 | Tasigna (Novartis) | Capsule | Not available |
| NDA219293 | DANZITEN (Azurity) | Tablet | Not available |
| NDA218922 | Nilotinib (Cipla USA) | Capsule | Not available |
| ANDA209651 | Nilotinib (Camber) | Capsule | Not available |
| ANDA218544 | Nilotinib (Novadoz) | Capsule | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (thrombocytopenia and neutropenia appear among the knowledge-graph contraindication-linked conditions) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC, liver function, electrolytes (potassium, magnesium), blood glucose, ECG/QT interval |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: long QT syndrome (including familial), torsades de pointes, hypertension, liver disease, gallbladder disease, pancreatitis, thrombocytopenia, neutropenia, agranulocytosis, anemia, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disorders, hypophosphatemia, hyperbilirubinemia, and Gilbert syndrome.
- **Drug Interactions**: 100 interactions were identified; the 20 reviewed here include:
  - **Major**: dexamethasone, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes)
  - **Moderate**: acid-reducing agents (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole), other corticosteroids (hydrocortisone, betamethasone, budesonide, triamcinolone), pioglitazone, loperamide, bupropion, aprepitant, bisacodyl, and saxagliptin

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (PDGFR inhibition, analogous to imatinib in DFSP) is plausible and the TxGNN model (deep learning) score is high (0.9931). However, there are no registered clinical trials, only one general review, no nilotinib-specific DFSP data, and no available label safety data. The evidence is L4. The drug is marketed in the US with 8 valid authorizations.

**To proceed, the following is needed:**
- Obtain and review the FDA package insert (warnings, contraindications, indications), which is a blocking gap for safety screening
- Obtain detailed mechanism of action data from DrugBank
- Search for nilotinib-specific DFSP evidence (case series, preclinical PDGFRB-fusion models, imatinib-resistant DFSP)
- Clarify the approved indications for the 8 valid US authorizations
- Assess the QT-prolongation, hepatic, and metabolic risks, and the major DDIs, for the target DFSP population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


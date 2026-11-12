---
layout: default
title: Nilotinib
parent: Model Prediction Only (L5)
nav_order: 966
evidence_level: L5
indication_count: 1
monitor_inn: "NILOTINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
last_modified_at: 2026-11-12
description: "Nilotinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). Approved use: Chronic myelogenous leukemia, BCR-ABL1 positive"
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
| US Market Status | Marketed (active FDA-approved applications: 9 of 10) |
| Number of FDA Applications | 10 (active: 9) |
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

Approved indication text was not available for any of them.

<!-- review:begin us-lic-20261106-nilotinib-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Eight valid authorizations are listed. Approved indication text was not available for any of them." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 10 FDA applications or NDC listings for this drug, 9 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-nilotinib-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA203640 | NILOTINIB HYDROCHLORIDE | APOTEX | Capsule; oral | Valid |
| ANDA209651 | NILOTINIB HYDROCHLORIDE | HETERO LABS LTD V | Capsule; oral | Valid |
| ANDA218350 | NILOTINIB HYDROCHLORIDE | DR REDDYS | Capsule; oral | Valid |
| ANDA218532 | NILOTINIB HYDROCHLORIDE | TORRENT | Capsule; oral | Valid |
| ANDA218544 | NILOTINIB HYDROCHLORIDE | MSN | Capsule; oral | Valid |

Showing 5 of 10 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

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
The mechanistic rationale (PDGFR inhibition, analogous to imatinib in DFSP) is plausible and the TxGNN model (deep learning) score is high (0.9931). However, there are no registered clinical trials, only one general review, no nilotinib-specific DFSP data, and no available label safety data. The evidence is L4. The drug is marketed in the US.

<!-- review:begin us-lic-20261106-nilotinib-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US with 8 valid authorizations." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 10 FDA applications or NDC listings for this drug, 9 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-nilotinib-2 -->

**To proceed, the following is needed:**
- Obtain and review the FDA package insert (warnings, contraindications, indications), which is a blocking gap for safety screening
- Obtain detailed mechanism of action data from DrugBank
- Search for nilotinib-specific DFSP evidence (case series, preclinical PDGFRB-fusion models, imatinib-resistant DFSP)
- Clarify the approved indications
- Assess the QT-prolongation, hepatic, and metabolic risks, and the major DDIs, for the target DFSP population

<!-- review:begin us-lic-20261106-nilotinib-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarify the approved indications for the 8 valid US authorizations" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 10 FDA applications or NDC listings for this drug, 9 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-nilotinib-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Eight valid authorizations are listed" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 8 valid authorizations" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "for the 8 valid US authorizations" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


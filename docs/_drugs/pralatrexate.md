---
layout: default
title: Pralatrexate
parent: Model Prediction Only (L5)
nav_order: 1073
evidence_level: L5
indication_count: 10
monitor_inn: "PRALATREXATE"
predicted_indications: ["pleural adenomatoid tumor", "relapsing-remitting multiple sclerosis", "pleural biphasic mesothelioma", "pleural epithelioid mesothelioma", "lymphohistiocytoid mesothelioma", "pericardium cancer", "pleural sarcomatoid mesothelioma", "malignant peritoneal mesothelioma", "well differentiated papillary mesothelioma", "pleural mesothelioma"]
last_modified_at: 2026-11-12
description: "Pralatrexate: predicted new indication Pleural mesothelioma . The rank 1 prediction, pleural adenomatoid tumor, has no evidence. (pleural adenomatoid tumor) (evidence level L5). Approved use: Not rec…"
---

# Pralatrexate
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

## Pralatrexate: Pleural mesothelioma (rank 10, best evidence). The rank 1 prediction, pleural adenomatoid tumor, has no evidence. (pleural adenomatoid tumor)
{: .text-alpha }

## One-Sentence Summary

Pralatrexate is an antifolate chemotherapy originally used for peripheral T-cell lymphoma and related non-Hodgkin lymphomas.
The TxGNN model's top-ranked prediction is *pleural adenomatoid tumor*, which has no supporting evidence. The best-supported prediction is **pleural mesothelioma** (including the epithelioid subtype), backed by **0 registered clinical trials** and **2 publications** (one Phase II trial and one review).

> Note: Because the top-ranked prediction has no supporting evidence, this report focuses on the best-supported prediction, pleural mesothelioma (rank 10, score 0.9985). The epithelioid subtype (rank 4) rests on the same Phase II study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pleural mesothelioma (rank 10, best evidence). The rank 1 prediction, pleural adenomatoid tumor, has no evidence. (pleural adenomatoid tumor) |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 (one single-arm Phase II study and one review; details not verified) |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, pralatrexate is an antifolate that inhibits dihydrofolate reductase (DHFR). It enters cells efficiently through the reduced folate carrier (RFC-1) and is retained through polyglutamylation. Its efficacy in T-cell lymphoma is established.

Malignant pleural mesothelioma is known to respond to antifolates, and pemetrexed is a standard therapy. Pralatrexate shares the antifolate mechanism, so it is plausible that it could act similarly. The epithelioid subtype is the most common and the most antifolate-responsive, which makes it the most reasonable subtype target.

The remaining predictions are much weaker:
- Other mesothelioma subtypes (biphasic, sarcomatoid, lymphohistiocytoid, peritoneal, pericardial, well-differentiated papillary) have no subtype-specific evidence. Sarcomatoid disease is generally more chemoresistant, and well-differentiated papillary disease is indolent and usually managed without cytotoxic therapy.
- Pleural adenomatoid tumor is a benign lesion usually treated by surgical excision, so there is no clear rationale for a cytotoxic drug.
- Relapsing-remitting multiple sclerosis has only a loose conceptual link through methotrexate's immunosuppressive use. Pralatrexate's mucositis and myelosuppression risk, together with established disease-modifying therapies, makes the benefit-risk profile unfavorable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17409804](https://pubmed.ncbi.nlm.nih.gov/17409804/) | 2007 | Phase II trial (single-arm; details unverified) | J Thorac Oncol | Pralatrexate in unresectable malignant pleural mesothelioma. The background notes that mesothelioma responds to antifolates, that pralatrexate's toxicity is mainly stomatitis, and that it showed antitumor activity in mesothelioma cell lines and xenografts. Outcomes were not available in the compiled data. |
| [21301589](https://pubmed.ncbi.nlm.nih.gov/21301589/) | 2010 | Review | Cancer Manag Res | Review of antifolates targeting folic acid synthesis, giving mechanistic context for DHFR inhibitors in cancer chemotherapy. |

---

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA206183 | PRALATREXATE | DR REDDYS | Solution; intravenous | Valid |
| NDA022468 | FOLOTYN | ACROTECH BIOPHARMA | Solution; intravenous | Valid |

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate class) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, renal function, and oral mucosa assessment (stomatitis is the main toxicity noted in the literature) |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindication-related conditions (from knowledge graph, not label text)**: thrombocytopenia, neutropenia, agranulocytosis, anemia, macrocytic anemia, impaired renal function, and stomatitis.
- **Drug Interactions**: 100 interactions were identified; the 20 shown in the compiled data include:
  - **Major**: deferiprone, samarium (153Sm) lexidronam
  - **Moderate**: NSAIDs (acetylsalicylic acid, ibuprofen, flurbiprofen, diclofenac, ketorolac), chloramphenicol, zidovudine, pyrimethamine, palifermin, glucarpidase, naltrexone, sapropterin, roflumilast, strontium-89 chloride, and a tetanus toxoid vaccine

Label warnings and contraindications were not available in the compiled data. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is a 2007 single-arm Phase II study in pleural mesothelioma, which was assessed from limited information only, and there are no registered trials. The top-ranked prediction (pleural adenomatoid tumor) and most other predictions have no evidence. Pralatrexate has a significant toxicity profile, which limits practical development. It is marketed in the US, with 2 of 2 licenses valid. Pleural mesothelioma, particularly the epithelioid subtype, is the only prediction worth a follow-up research question.

**To proceed, the following is needed:**
- Full text of the Phase II study (PMID 17409804): response rate, survival, histology breakdown, and toxicity
- Current mesothelioma standard-of-care comparison (e.g., pemetrexed-based regimens) to define a possible niche
- Mechanism of action data and FDA package insert warnings and contraindications
- Clarification of the regulatory and commercial status
- Any later trials or preclinical data for pralatrexate in mesothelioma

<!-- review:begin us-lic-20261106-pralatrexate-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the regulatory and commercial status of the cancelled US licenses" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 2 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-pralatrexate-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "of the cancelled US licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


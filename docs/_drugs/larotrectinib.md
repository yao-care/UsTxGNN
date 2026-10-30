---
layout: default
title: Larotrectinib
parent: Model Prediction Only (L5)
nav_order: 837
evidence_level: L5
indication_count: 2
monitor_inn: "LAROTRECTINIB"
predicted_indications: ["multiple endocrine neoplasia", "HER2 positive breast carcinoma"]
last_modified_at: 2026-10-30
description: "Larotrectinib: predicted new indication Multiple endocrine neoplasia (evidence level L3). Approved use: Not available in the compiled data"
---

# Larotrectinib
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

## Larotrectinib: From NTRK Fusion-Positive Solid Tumours to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Larotrectinib (US brand name VITRAKVI) is a selective TRK kinase inhibitor, but the data compiled for this report contain no approved-indication text for it.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**,
and so far this is supported by only **1 broad, non-specific clinical trial** and **2 publications** (a review and a resistance-mechanism report), none showing efficacy in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (US license records contain no indication text) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of FDA Applications | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From the available analysis, larotrectinib is a selective pan-TRK inhibitor (TRKA/B/C). Its original indication could not be confirmed from the license records.

Multiple endocrine neoplasia type 2 (MEN2) is driven by activating germline RET mutations, which underlie medullary thyroid carcinoma and pheochromocytoma. Larotrectinib has no established direct RET activity, so the link is indirect. It rests on shared receptor tyrosine kinase signalling (RAS/MAPK, PI3K/AKT) and on TRK fusions occurring in a small subset of thyroid cancers.

A 2024 report on off-target resistance to selective RET inhibition suggests that bypass pathways could involve TRK signalling. This hypothesis has not been validated clinically. The high TxGNN score is a computational prediction and does not demonstrate efficacy in this disease.

A second prediction, HER2-positive breast carcinoma (score 0.9914), has only preclinical evidence with a different TRK inhibitor (entrectinib) and a case report of secretory breast carcinoma. That carcinoma carries the ETV6-NTRK3 fusion and is typically HER2-negative. It is not evaluated further here.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6452 | NCI-MATCH: genetically directed treatment in advanced, refractory solid tumours, lymphomas and myelomas. It is a non-randomised, tumour-agnostic basket trial with no data specific to multiple endocrine neoplasia, so it is only weak, indirect support. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Kinase inhibitor therapy for advanced thyroid cancer. Approvals are mostly antiangiogenic multikinase inhibitors, plus mutation-specific indications. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Preclinical/mechanistic | NPJ Precision Oncology | Off-target resistance mechanisms in a medullary thyroid carcinoma patient with a RET mutation treated with selpercatinib. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210861 | VITRAKVI | Capsule | Not available (status: valid) |
| NDA211710 | VITRAKVI | Solution, concentrate | Not available (status: valid) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (TRK kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interacting drugs were identified in the interaction screen (the 20 most prominent entries are in the compiled data). The one **Major** interaction is **clarithromycin**. Most others are **Moderate**, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), omeprazole, cimetidine, aprepitant, pioglitazone, saxagliptin, cisapride, clotrimazole, dolasetron, dronabinol, eliglustat, naldemedine and naltrexone. Naloxegol is **Minor**.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting trial is a non-specific basket study, and the literature is a review and a resistance-mechanism report, with no efficacy data in multiple endocrine neoplasia. The mechanistic link (TRK inhibitor in a RET-driven disease) is indirect, and the high TxGNN score is a prediction only. Both US licences are cancelled, and package-insert safety data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the original approved indications
- Preclinical evidence of TRK-pathway involvement in RET-driven MEN2 tumours
- Review of NCI-MATCH sub-protocol results for any MEN-relevant patients
- Clinical interpretation of the clarithromycin interaction and other CYP-related interaction risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Everolimus
parent: Model Prediction Only (L5)
nav_order: 687
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From Its Approved Uses to Liposarcoma

## One-Sentence Summary

Everolimus is an mTOR inhibitor already marketed in the United States as an oral tablet, but the source data do not list its approved indications.
The TxGNN model predicts it may be effective for **liposarcoma**.
Support so far is **1 Phase 2 clinical trial** (a combination with ribociclib) and **5 publications**, of which only one is a clinical trial report.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Liposarcoma (mainly dedifferentiated liposarcoma) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 (per the Evidence Pack, at the weak end: the only trial is a single-arm combination Phase 2 and is not yet completed) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Everolimus inhibits mTORC1, a central node of the Akt-mTOR pathway that drives cell growth and proliferation. Detailed mechanism data from DrugBank are not currently available, so this description comes from the Evidence Pack's repurposing rationale.

A study of 99 dedifferentiated liposarcoma specimens found activation of the Akt-mTOR and MAPK pathways (PMID 26518767). That gives a biological reason to expect an mTOR inhibitor to act on this tumor type.

Dedifferentiated liposarcoma is also characterized by CDK4 amplification. The one clinical trial therefore pairs everolimus with the CDK4/6 inhibitor ribociclib. Because everolimus was tested only in combination, its own contribution cannot be separated from ribociclib's.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma (DDL) and leiomyosarcoma (LMS) after at least 1 prior systemic therapy. Two cohorts, each measuring anti-tumor activity. Appears single-arm; efficacy results are not in the provided data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 trial report | Clin Cancer Res | Ribociclib + everolimus in advanced DDL and LMS. Rationale: CDK4/6 targeting in DDL, mTOR targeting in LMS, and synergy in tumor models. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Preclinical tissue analysis | Tumour Biol | Akt-mTOR and MAPK pathways are activated in dedifferentiated liposarcoma (99 specimens); an mTOR inhibitor was also tested in vitro. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (preclinical) | Front Oncol | Sarcoma PDOX mouse models used to find combinations with the CDK inhibitor palbociclib. Indirect evidence. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Res | Eribulin combinations with other anticancer agents. Indirect evidence. |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Preclinical | Oncogene | XPO1 inhibitor KPT-330 in dedifferentiated liposarcoma. Indirect evidence. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA207486 | Everolimus (Hikma Pharmaceuticals USA Inc.) | Tablet |
| NDA022334 | Afinitor (Novartis Pharmaceuticals Corporation) | Tablet |
| ANDA214138 | Everolimus (Ascend Laboratories, LLC) | Tablet |
| ANDA217640 | Everolimus (Breckenridge Pharmaceutical, Inc.) | Tablet, for suspension |

The Evidence Pack lists 20 authorizations in total and includes 5 records here; NDA022334 appears twice, so 4 unique authorizations are shown. Approved-indication text was not provided.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is one not-yet-completed, single-arm Phase 2 combination trial with ribociclib, and no efficacy results are available. Everolimus's own contribution cannot be separated from ribociclib's. Package insert safety data are also missing, which the Evidence Pack flags as blocking for safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap)
- Efficacy and safety results from NCT03114527 and the PMID 37967116 report, to judge everolimus's contribution
- Detailed mechanism of action data from DrugBank
- Confirmation of the currently approved indications, to check overlap with the predicted use

Other predicted indications (rank 2 to 10) have little support. Rhabdomyosarcoma has three trials, including one Phase 2 single-agent study with unknown status. The remaining entities have no everolimus-specific evidence. This report evaluates only the top prediction, liposarcoma.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


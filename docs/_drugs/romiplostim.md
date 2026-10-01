---
layout: default
title: Romiplostim
parent: Moderate Evidence (L3-L4)
nav_order: 1132
evidence_level: L4
indication_count: 10
---

# Romiplostim
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Romiplostim: From Its Marketed Thrombopoietin-Receptor Agonist Use to Primary Release Disorder of Platelets

## One-Sentence Summary

Romiplostim is a thrombopoietin receptor (MPL) agonist that raises platelet production, and it is marketed in the US as Nplate. The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but only **1 registered trial** (an observational study that did not test romiplostim) and **2 background publications** are linked to this prediction. These do not show benefit for the disease, so the prediction rests almost entirely on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (all records are BLA125268) |
| Recommended Decision | Hold |

The supplied data contain no approved-indication text for the original use, so that row is omitted.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the drug record. The candidate-level analysis describes romiplostim as an MPL agonist that increases megakaryocyte proliferation and platelet count.

That mechanism fits conditions where too few platelets are made. A release disorder is a functional defect: platelets are present but do not degranulate or secrete normally. Raising platelet numbers is therefore unlikely to fix the underlying problem.

The two linked papers are general background. One reviews megakaryocyte and platelet production. The other is an in vitro study of how autoantibodies in immune thrombocytopenia impair platelet formation. Neither shows that romiplostim helps a platelet release disorder. The high TxGNN score should be read as a model-derived hypothesis, not as clinical support.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Completed | 10,039 | Observational study of risk factors for thrombosis in immune thrombocytopenia. It does not test romiplostim for the predicted condition. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | British Journal of Haematology | Overview of megakaryocyte and platelet production, with thrombopoietin as the main growth factor. General background only. |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Preclinical / in vitro | Haematologica | Antiplatelet autoantibodies from immune thrombocytopenia patients inhibited proplatelet formation and impaired platelet production in vitro. No romiplostim treatment data. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125268 (3 records) | Nplate (Amgen, Inc) | Injection, powder, lyophilized, for solution | Not listed in the supplied record |

## Safety Considerations

Please refer to the package insert for safety information. No warning, contraindication or drug-interaction data were available in the supplied data.

One class-level signal appears in the wider candidate data. A cohort study (PMID [21902682](https://pubmed.ncbi.nlm.nih.gov/21902682/)) found increased bone marrow reticulin in ITP patients treated with thrombopoietin receptor agonists. This should be considered in any long-term use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism does not match the disease, because raising platelet count is unlikely to correct a platelet functional defect. No romiplostim study exists for this condition. The very high model score is not clinical evidence.

**To proceed, the following is needed:**
- The package insert (warnings and contraindications), which is currently a blocking gap for safety screening
- Detailed mechanism-of-action data from DrugBank, and the approved-indication text for Nplate
- Any case series, mechanistic or preclinical work showing that thrombopoietin-receptor agonism improves platelet secretion or release function
- Review of the rank 8 candidate, platelet-type bleeding disorder, which has eight romiplostim trials (one Phase 3 randomized trial). Those trials appear to address thrombocytopenia settings rather than platelet function disorders, so the indication mapping needs confirmation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


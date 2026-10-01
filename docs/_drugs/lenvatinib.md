---
layout: default
title: Lenvatinib
parent: Model Prediction Only (L5)
nav_order: 846
evidence_level: L5
indication_count: 10
---

# Lenvatinib
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

# Lenvatinib: From a Marketed Multi-Kinase Inhibitor to Liposarcoma

## One-Sentence Summary

Lenvatinib is an oral multi-kinase inhibitor marketed in the US as Lenvima, and the source data does not list its original indications.
The TxGNN model predicts it may be effective for **liposarcoma**.
Support is limited: **1 completed Phase Ib/II single-arm trial** (30 patients, lenvatinib plus eribulin) and **4 publications**, of which only one reports on that trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L2 (lower edge: the Phase Ib/II study is single-arm and small, with no randomized comparator) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (all records under NDA206947) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not available in the drug record. The evidence review describes lenvatinib as a multi-kinase inhibitor acting on VEGFR1-3, FGFR1-4, PDGFRα, RET and KIT. Its main action is against tumor angiogenesis, meaning the blood vessels that feed a tumor.

The tested regimen pairs lenvatinib with eribulin, a chemotherapy that blocks cell division (mitosis). The rationale is that one drug starves the tumor of blood supply while the other attacks dividing cancer cells directly.

The completed Phase Ib/II LEADER study gives a clinical signal in advanced adipocytic sarcoma (liposarcoma). It was single-arm and small (n=30), so it is not confirmatory. The other liposarcoma-related predictions (for example ovarian myxoid liposarcoma) have no entity-specific evidence. Myxoid liposarcoma also differs biologically from the dedifferentiated and well-differentiated subtypes, so extrapolation is uncertain.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | Completed | 30 | LEADER study: single-arm test of lenvatinib plus eribulin in inoperable or metastatic adipocytic sarcoma and leiomyosarcoma. Started July 2018 and completed October 2025. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase Ib/II single-arm trial | Clin Cancer Res | Publication of the LEADER study (NCT03526679) on lenvatinib plus eribulin in advanced liposarcoma and leiomyosarcoma. The retrieved abstract excerpt gives no efficacy or safety figures. |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclinical / biomarker study | Exp Hematol Oncol | CDK4 as a prognostic biomarker in soft tissue sarcoma, with synergy from CDK4 inhibition in sequential treatment of dedifferentiated liposarcoma. Does not test lenvatinib directly. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical study | Anticancer Res | Eribulin shows broad anticancer activity in xenograft models when combined with mechanistically different agents. Supports the combination partner, not lenvatinib itself. |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case report | Case Rep Oncol | Reduced tumor size in a patient with dedifferentiated liposarcoma and lung metastasis after individualized targeted, surgical and chemotherapy treatment. Anecdotal. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA206947 (5 records) | Lenvima (Eisai Inc.) | Capsule (oral) | Indication text not provided in the source data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor). The eribulin partner in the tested regimen is a conventional cytotoxic agent. |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood pressure, urine protein, liver function and immune-related events (from the evidence review). Add blood counts when combined with eribulin. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

The evidence review recommends monitoring for hypertension, proteinuria, hepatotoxicity and immune-related events.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is one small (n=30), single-arm Phase Ib/II study, with no randomized data in liposarcoma. Package insert warnings and contraindications are also missing, which blocks safety screening.

The strongest evidence in this pack is for renal carcinoma, with Phase 3 CLEAR RCT support (L1). That is an established, marketed use, so it validates the model rather than counting as a new repurposing finding.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, downloaded and parsed from the FDA website (blocking gap)
- Mechanism-of-action data from DrugBank
- Efficacy and safety results of the LEADER study (PMID 36129471), and ideally a randomized or larger confirmatory study in liposarcoma
- Confirmation of lenvatinib's labeled indications from the US NDA records
- Subtype-specific data before extending to myxoid or other rare liposarcoma variants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


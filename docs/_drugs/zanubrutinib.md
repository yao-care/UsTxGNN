---
layout: default
title: Zanubrutinib
parent: Model Prediction Only (L5)
nav_order: 1302
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Zanubrutinib: From B-Cell Malignancies (CLL/SLL) to Myeloid Leukemia

## One-Sentence Summary

Zanubrutinib is an oral BTK inhibitor marketed in the US as BRUKINSA. The retrieved literature shows it is used for B-cell malignancies such as CLL/SLL and Waldenström's macroglobulinemia.
The TxGNN model predicts it may be effective for **myeloid leukemia**, but evidence for this is thin. The **2 clinical trials** retrieved do not test zanubrutinib as a treatment for myeloid disease, and the **8 publications** concern lymphoid malignancies or safety.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data. The literature points to B-cell malignancies (CLL/SLL, Waldenström's macroglobulinemia) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 (preclinical or mechanism-level only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Zanubrutinib is a covalent inhibitor of Bruton's tyrosine kinase (BTK), a key node in B-cell receptor signalling. It is described in the literature as more selective than ibrutinib or acalabrutinib.

BTK signalling has been proposed to play a role in AML blasts, but this evidence is preclinical. The high TxGNN score most likely reflects graph proximity to approved B-cell/CLL leukemia indications rather than a true myeloid signal. CLL is a lymphoid leukemia driven by B-cell receptor signalling, whereas myeloid leukemia has different biology. The prediction is therefore a hypothesis, not a direct extension of the existing indication.

The other five predictions (vertebral anomalies with endocrine and T-cell dysfunction, ganglioneuroblastoma, retroperitoneal neoplasm, Ewing sarcoma, neuroblastoma) have scores of 99.2–99.4% but no identifiable BTK-related mechanism. They have no supporting trials, and the only retrieved publication is an unrelated drug-synthesis review. They are all Level L5 (model prediction only) and Hold.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Dose-escalation study of PRT2527 (CDK9 inhibitor) alone or combined with zanubrutinib or venetoclax in relapsed/refractory hematologic malignancies. Zanubrutinib is only a possible combination partner, so this gives no direct evidence in myeloid leukemia (relevance grade C). |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1a/b | Terminated | 45 | CG-806 (luxeptinib, a FLT3/BTK multi-kinase inhibitor) in relapsed/refractory AML or higher-risk MDS. It is a different drug and the trial was terminated, so it offers only class-level, hypothesis-generating support for BTK-pathway targeting in AML (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA (Phase 3): median 5-year follow-up of zanubrutinib vs bendamustine + rituximab in treatment-naïve CLL/SLL. |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Adv | Phase 2 single-arm study: zanubrutinib was well tolerated and effective in CLL/SLL patients intolerant of ibrutinib or acalabrutinib. |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Pooled analysis | Blood Adv | Zanubrutinib efficacy and safety in CLL/SLL with del(17p) and/or TP53 mutation (N = 301), pooled across SEQUOIA, ALPINE and other studies. |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | Phase 2 open-label study in B-cell malignancies intolerant of prior BTK inhibitors, assessing whether zanubrutinib reduces toxicity-related discontinuations. |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | Tyrosine kinase inhibitors in chronic leukemias (CML and CLL). It covers the chronic myeloid and lymphoid settings, not zanubrutinib in AML. |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | Managing Waldenström's macroglobulinemia with BTK inhibitors. |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | Hepatitis B virus reactivation in patients receiving BTK inhibitors (ibrutinib, acalabrutinib, zanubrutinib). |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case report | Front Immunol | Rare coexistence of Waldenström's macroglobulinemia and B-cell ALL. |

All 8 publications are lymphoid or safety-related; none addresses myeloid leukemia. (PMID 38288815, a review of FDA-approved anticancer drug synthesis, was also retrieved but has no bearing on efficacy.)

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA218785 | BRUKINSA (BeOne Medicines USA, Inc.) | Tablet, film coated | Not stated in source data |
| NDA213217 | BRUKINSA (BeOne Medicines USA, Inc.) | Capsule | Not stated in source data |

Both products are oral.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (covalent BTK inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; a CBC and liver and renal function are standard for oncology therapy |
| Handling Protection | Please refer to the package insert and institutional handling policy for oral antineoplastics |

## Safety Considerations

- **Literature-reported signal**: Hepatitis B virus reactivation has been described in patients receiving BTK inhibitors, including zanubrutinib (PMID 37150651).

No warnings, contraindications, or drug-interaction records were retrieved, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.65% score is likely driven by proximity to CLL/lymphoid leukemia indications. Neither retrieved trial tests zanubrutinib in myeloid leukemia, and the literature is entirely lymphoid or safety-related. The evidence is at most preclinical (L4), and the package-insert safety review is still outstanding.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence of BTK dependence in AML or other myeloid models, and any clinical data for zanubrutinib in AML/MDS
- Licensed indication text for both NDAs, to confirm the original indication
- A review of how the CG-806 (a different BTK-pathway inhibitor) AML trial was terminated, as context for class-level feasibility

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


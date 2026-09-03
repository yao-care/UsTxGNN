---
layout: default
title: Zanubrutinib
parent: 僅模型預測 (L5)
nav_order: 1302
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Zanubrutinib: From B-Cell Malignancies (CLL/SLL) to Myeloid Leukemia

## One-Sentence Summary

> Zanubrutinib is a next-generation covalent BTK inhibitor established for B-cell malignancies such as chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) and Waldenström macroglobulinemia.
> The TxGNN model predicts it may also be effective for **Myeloid Leukemia**,
> but this direction is currently supported only by **2 indirect clinical trials** and **9 publications**, none of which study zanubrutinib specifically in myeloid leukemia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma (CLL/SLL), Waldenström Macroglobulinemia, and other B-cell malignancies (approved in other jurisdictions; not on the local market per this evidence pack) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.65% (KG rank 9,102) |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data was not retrievable from DrugBank for this candidate (flagged as data gap DG002). Based on well-established pharmacology, however, zanubrutinib is a highly selective, next-generation covalent **Bruton's tyrosine kinase (BTK) inhibitor**. Its therapeutic effect depends on blocking B-cell receptor (BCR) signaling, and all of its currently confirmed indications — CLL/SLL, Waldenström macroglobulinemia, and other B-cell lymphomas — are diseases of the **lymphoid** lineage.

Myeloid leukemia, in contrast, arises from the **myeloid** lineage, and BTK is not considered a key driver kinase in myeloid malignancies. The mechanistic overlap between zanubrutinib's known pharmacology and myeloid leukemia biology is therefore weak. A plausible explanation for the high TxGNN score is that the knowledge graph's "leukemia" disease node may not cleanly separate lymphoid and myeloid subtypes, producing a category-level association rather than a true mechanistic signal.

Consistent with this, the clinical trials retrieved for this indication do not actually test zanubrutinib as the primary agent in myeloid leukemia — they test other kinase inhibitors (PRT2527, CG-806/luxeptinib) in AML, with zanubrutinib appearing only as a combination arm or reference comparator in a broader hematologic-malignancy study. The literature evidence pool is similarly composed of zanubrutinib data in its established lymphoid indications (CLL/SLL, Waldenström) rather than myeloid disease. Taken together, this is best interpreted as a graph-level signal requiring independent mechanistic and preclinical validation before any clinical consideration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Dose-escalation study of PRT2527 (a CDK9 inhibitor), tested as monotherapy and in combination with zanubrutinib or venetoclax in relapsed/refractory hematologic malignancies. Zanubrutinib is a combination partner, not the primary study drug (relevance grade C — disease-domain overlap only). |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1a/b | Terminated | 45 | Evaluated CG-806 (luxeptinib, a FLT3/multi-kinase inhibitor) in relapsed/refractory AML or higher-risk MDS. Zanubrutinib is not the study drug; trial was terminated, limiting evidentiary value (relevance grade C). |

**Note:** No trial in this evidence pack directly evaluates zanubrutinib as monotherapy for myeloid leukemia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | 5-year follow-up of SEQUOIA (Phase 3): zanubrutinib vs bendamustine+rituximab in treatment-naïve CLL/SLL — establishes efficacy in lymphoid, not myeloid, disease. |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Advances | Updated results of BGB-3111-215: zanubrutinib well tolerated and effective in CLL/SLL patients intolerant of ibrutinib/acalabrutinib. |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | Phase 2 single-arm study: zanubrutinib in B-cell malignancies intolerant of prior BTK inhibitors — again a lymphoid B-cell population. |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Review | Blood Advances | Pooled analysis of zanubrutinib in del(17p)/TP53-mutated CLL/SLL across SEQUOIA and ALPINE trials. |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | Review of tyrosine kinase inhibitors in chronic leukemias (CML/CLL); discusses BCR-ABL1 (myeloid) and BCR pathway (lymphoid) separately — supports the lineage distinction relevant to this prediction. |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | Review of BTK inhibitors, including zanubrutinib, in Waldenström macroglobulinemia management. |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | HBV reactivation risk in patients receiving BTK inhibitors (ibrutinib, acalabrutinib, zanubrutinib) — a safety-relevant review, not disease-efficacy evidence. |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anticancer Agents Med Chem | Broad review of synthetic methodology for FDA-approved anticancer drugs (2018–2021); mentions zanubrutinib only in passing as one of many approved agents. |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case Report | Front Immunol | Case report of coexisting Waldenström macroglobulinemia and B-ALL with KMT2D/MECOM mutations — a rare co-occurrence case, not zanubrutinib efficacy data. |

**None of the above directly address zanubrutinib use in myeloid leukemia.**

---

## US Market Information

Zanubrutinib is currently **not marketed** under the regulatory records covered by this evidence pack (market status: 未上市 / Not Marketed; 0 authorizations on file). No license or approved-indication text is available to summarize.

---

## Cytotoxicity

Zanubrutinib's established use in B-cell malignancies qualifies it as an antineoplastic agent, so this section is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (covalent BTK inhibitor) |
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
The mechanistic rationale for zanubrutinib in myeloid leukemia is weak — BTK is not a recognized driver kinase in myeloid disease, and the high TxGNN score likely reflects a knowledge-graph category effect rather than a true signal. No retrieved trial or publication studies zanubrutinib specifically in myeloid leukemia; the two available trials test unrelated drugs, and all substantive literature concerns zanubrutinib's established lymphoid indications. Safety and labeling data (TFDA warnings/contraindications) are also unavailable, which is a blocking gap for any further safety assessment.

**To proceed, the following is needed:**
- TFDA package insert / label data (warnings, contraindications) — currently blocking (DG001)
- Structured DrugBank mechanism-of-action data to formally assess target relevance (DG002)
- Dedicated preclinical or mechanistic studies testing BTK inhibition (or off-target kinase activity) in myeloid leukemia models
- Any future clinical trial data using zanubrutinib as the primary agent in a myeloid leukemia population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


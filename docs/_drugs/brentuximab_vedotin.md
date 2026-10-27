---
layout: default
title: Brentuximab Vedotin
parent: Model Prediction Only (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Brentuximab Vedotin: predicted new indication Follicular lymphoma (evidence level L5). Approved use: Hodgkin lymphoma (classic Hodgkin lymphoma and related subtypes)"
monitor_inn: "BRENTUXIMAB VEDOTIN"
predicted_indications: ["follicular lymphoma", "myeloid leukemia", "acute lymphoblastic/lymphocytic leukemia", "B-cell neoplasm", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "Richter syndrome", "mantle cell lymphoma", "ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction"]
---

# Brentuximab Vedotin
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

## Brentuximab Vedotin: From Hodgkin Lymphoma to Follicular Lymphoma
{: .text-alpha }

## One-Sentence Summary

Brentuximab vedotin is an anti-CD30 antibody-drug conjugate originally used to treat Hodgkin lymphoma.
The TxGNN model predicts it may be effective for **follicular lymphoma**, but the supporting evidence is thin: **6 clinical trials** have been linked (3 withdrawn with zero enrollment, 2 terminated early, 1 still recruiting), and the 20 publications returned are mostly about peripheral T-cell lymphoma rather than follicular lymphoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma (classic Hodgkin lymphoma and related subtypes) |
| Predicted New Indication | Follicular lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 (as assigned in the compiled data; see note below) |
| US Market Status | Cancelled only (1 BLA, cancelled) |
| Number of NDAs | 1 (BLA125388) |
| Recommended Decision | Hold |

**Note on evidence level:** The compiled data labels this indication L2, but no completed Phase 2/3 RCT exists for follicular lymphoma. The only directly relevant trial (NCT04587687) is a single-arm Phase 2 that is still recruiting. By the rules above, the evidence is closer to L4–L5, and I treat it that way in the decision below.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, brentuximab vedotin is an antibody-drug conjugate. The antibody targets CD30 and delivers a cytotoxic payload (vedotin, MMAE) into CD30-positive cells. Its efficacy in CD30-positive Hodgkin lymphoma is established.

The link to follicular lymphoma is weak. Follicular lymphoma is generally CD30-low or negative, so any benefit would depend on a CD30-expressing subset or on bystander effects of the payload. The high TxGNN score reflects network-level similarity between lymphoid diseases and should not be read as evidence of CD30-driven activity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | Brentuximab vedotin + bendamustine in relapsed/refractory follicular lymphoma. Directly relevant; no results yet. |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | Brentuximab vedotin + rituximab as frontline therapy in CD30+ and/or EBV+ lymphomas. Follicular lymphoma is only one included subtype. |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomized rituximab + bendamustine with or without brentuximab vedotin in CD30+ DLBCL. Terminated early, which limits interpretation. |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | Withdrawn | 0 | Rituximab + brentuximab vedotin ± bendamustine in post-transplant lymphoproliferative disorders. No data. |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | Withdrawn | 0 | Brentuximab vedotin + bendamustine + rituximab in CD30+ relapsed/refractory B-cell NHL. No data. |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | Withdrawn | 0 | Brentuximab vedotin + pembrolizumab in peripheral T-cell lymphoma. No data. |

---

## Literature Evidence

None of the publications below reports efficacy of brentuximab vedotin in follicular lymphoma. They mainly concern peripheral T-cell lymphoma (PTCL).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Cohort (Phase 2) | Blood Adv | Brentuximab vedotin + gemcitabine in relapsed/refractory CD30+ PTCL (LYSA study). |
| [33320379](https://pubmed.ncbi.nlm.nih.gov/33320379/) | 2021 | Cohort | Eur J Haematol | Brentuximab vedotin added to ICE in relapsed/refractory PTCL. |
| [38364196](https://pubmed.ncbi.nlm.nih.gov/38364196/) | 2024 | RCT | J Clin Oncol | Ro-CHOP vs CHOP in untreated PTCL; brentuximab vedotin not studied. |
| [40517441](https://pubmed.ncbi.nlm.nih.gov/40517441/) | 2025 | Review | Hematol Oncol | Overview of PTCL management. |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | Treatment of common nodal PTCL subtypes, including brentuximab vedotin + CHP. |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | Review | Hematology (ASH Educ) | Incorporating brentuximab vedotin and novel agents into PTCL management. |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leuk Res Rep | Immunotherapy in indolent NHL, including follicular lymphoma. |
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case report | Gulf J Oncol | Grade I follicular lymphoma transformed to CD30+ ALK− anaplastic large cell lymphoma, with complete response to brentuximab vedotin and high-dose methotrexate. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125388 | ADCETRIS (SEAGEN INC.) | Injection, powder, lyophilized, for solution | Not listed in the compiled data; status: cancelled |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate (anti-CD30 antibody with MMAE, a microtubule-disrupting cytotoxic payload) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; routine CBC and liver and renal function monitoring is generally appropriate for cytotoxic agents |
| Handling Protection | Follow institutional cytotoxic drug handling procedures |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. The ones listed are all Moderate severity, and most are antidiabetic agents: acarbose, albiglutide, alogliptin, metformin, pioglitazone, acetohexamide, canagliflozin, dapagliflozin, dulaglutide, empagliflozin, ertugliflozin, exenatide, glimepiride, glipizide and chlorpropamide. Other moderate interactions include bupropion, chenodeoxycholic acid, clarithromycin, clotrimazole and eliglustat. The full list should be reviewed before any clinical use.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is weak because follicular lymphoma is generally CD30-low or negative. The only directly relevant trial (NCT04587687) is small, single-arm, and has no results, and the other linked trials were withdrawn or terminated early. The literature does not address follicular lymphoma. In addition, the single US license (BLA125388) is listed as cancelled in the compiled data, and package-insert safety data is missing.

**To proceed, the following is needed:**
- Results from NCT04587687, plus data on CD30 expression in follicular lymphoma to define any responsive subset
- Package insert warnings and contraindications, and mechanism-of-action data
- Verification of current US marketing status, since the compiled data shows only a cancelled license
- Other candidates in this prediction set may be stronger. For example, CD30-positive diffuse large B-cell lymphoma (listed under B-cell neoplasm) has Phase 2 data and recent publications, and could be evaluated separately.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Bendamustine
parent: High Evidence (L1-L2)
nav_order: 444
evidence_level: L1
indication_count: 10
---

# Bendamustine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Bendamustine: From Chronic Lymphocytic Leukemia and Indolent B-cell Lymphoma to Mantle Cell Lymphoma

## One-Sentence Summary

Bendamustine is an alkylating chemotherapy agent. It is described in the retrieved literature as indicated for chronic lymphocytic leukemia (CLL) and rituximab-refractory indolent B-cell non-Hodgkin lymphoma (NHL).
The TxGNN model predicts it may be effective for **mantle cell lymphoma (MCL)**, with **50 clinical trials** and **20 publications** supporting this direction.
Three completed Phase 3 randomized trials use bendamustine plus rituximab (BR) in MCL, so the evidence is strong.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CLL and rituximab-refractory indolent B-cell NHL (from PMID 25829094; the US license records contain no indication text) |
| Predicted New Indication | Mantle cell lymphoma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 15 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank. The evidence review describes bendamustine as a bifunctional alkylating agent with purine-analog-like properties. It causes DNA cross-linking and is active in B-cell malignancies.

Its original indications (CLL and indolent B-cell NHL) are also B-cell cancers. MCL is an aggressive B-cell lymphoma that responds to the same alkylator-plus-anti-CD20 approach. Bendamustine plus rituximab (BR) is a chemoimmunotherapy backbone in MCL. Several Phase 3 trials use it as the control arm or as the backbone to which a targeted drug is added. It also appears in the 2025 EHA-EU MCL guidelines.

Bendamustine is therefore already part of routine MCL practice, and the prediction is supported by clinical use rather than by model output alone. Its US label status for MCL is not shown in the provided data and should be confirmed.

---

## Clinical Trial Evidence

The table shows 10 of the 50 retrieved MCL trials, prioritizing Phase 3 studies with bendamustine in the regimen, then completed Phase 2 studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01776840](https://clinicaltrials.gov/study/NCT01776840) | Phase 3 | Completed | 523 | Randomized, double-blind: ibrutinib vs placebo added to BR in newly diagnosed MCL, patients aged 65 or older |
| [NCT02972840](https://clinicaltrials.gov/study/NCT02972840) | Phase 3 | Active, not recruiting | 635 | Randomized, double-blind: acalabrutinib vs placebo added to BR in untreated MCL |
| [NCT00991211](https://clinicaltrials.gov/study/NCT00991211) | Phase 3 | Completed | 549 | First-line non-inferiority comparison of BR vs R-CHOP (rituximab plus CHOP) in low-grade lymphomas and MCL, with progression-free survival as the endpoint |
| [NCT01456351](https://clinicaltrials.gov/study/NCT01456351) | Phase 3 | Completed | 230 | Recurrent low-grade NHL and MCL: BR vs fludarabine plus rituximab, with event-free survival as the endpoint |
| [NCT06363994](https://clinicaltrials.gov/study/NCT06363994) | Phase 3 | Recruiting | 476 | Randomized, double-blind: orelabrutinib plus BR vs placebo plus BR in treatment-naive MCL |
| [NCT06496308](https://clinicaltrials.gov/study/NCT06496308) | Phase 3 | Recruiting | 78 | Open-label: orelabrutinib plus BR vs BR in transplant-ineligible, intermediate- to high-risk MCL |
| [NCT00992134](https://clinicaltrials.gov/study/NCT00992134) | Phase 2 | Completed | 41 | Rituximab-bendamustine-cytarabine (R-BAC) in MCL patients unfit for intensive regimens |
| [NCT01662050](https://clinicaltrials.gov/study/NCT01662050) | Phase 2 | Completed | 57 | Age-adjusted R-BAC as induction in older MCL patients. An interim analysis noted good activity but considerable hematological toxicity |
| [NCT01737177](https://clinicaltrials.gov/study/NCT01737177) | Phase 2 | Completed | 42 | Bendamustine, lenalidomide and rituximab (R2-B) for first relapsed or refractory MCL, followed by lenalidomide maintenance |
| [NCT03834688](https://clinicaltrials.gov/study/NCT03834688) | Phase 2 | Completed | 33 | Venetoclax plus BR as induction in untreated MCL over age 60 |

Results are not reported in the source data. Three completed Phase 3 randomized trials (NCT01776840, NCT00991211, NCT01456351) meet the L1 threshold.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | RCT (Phase 3) | Lancet | Open-label non-inferiority trial of BR vs R-CHOP as first-line treatment in indolent lymphoma and MCL |
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | RCT | N Engl J Med | Ibrutinib plus BR followed by rituximab maintenance in older patients with untreated MCL (SHINE) |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | RCT | J Clin Oncol | Acalabrutinib plus BR in untreated MCL. Ibrutinib plus BR had prolonged progression-free survival without an overall survival gain, likely because of toxicity |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | RCT (Phase 2/3) | Lancet | ENRICH: chemotherapy-free ibrutinib plus rituximab vs standard immunochemotherapy (R-CHOP or BR) in patients aged 60 or older |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | Cohort follow-up | J Clin Oncol | BRIGHT 5-year follow-up: BR vs R-CHOP or R-CVP in treatment-naive indolent NHL or MCL |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Phase 2 pooled analysis | Blood Adv | Rituximab/bendamustine alternating with rituximab/high-dose cytarabine, then autologous transplant, in transplant-eligible MCL |
| [32985902](https://pubmed.ncbi.nlm.nih.gov/32985902/) | 2021 | RCT design paper | Future Oncol | Phase 3 design of zanubrutinib plus rituximab vs BR in transplant-ineligible untreated MCL |
| [36919283](https://pubmed.ncbi.nlm.nih.gov/36919283/) | 2023 | Network meta-analysis | Eur J Haematol | Three RCTs (1,459 subjects) compared in ineligible-for-intensive-therapy MCL. The title reports ibrutinib plus BR as superior |
| [41132246](https://pubmed.ncbi.nlm.nih.gov/41132246/) | 2025 | Guideline | HemaSphere | EHA-EU MCL network guidelines for diagnosis and treatment |
| [36456154](https://pubmed.ncbi.nlm.nih.gov/36456154/) | 2022 | Retrospective | Anticancer Res | Korean multicenter retrospective analysis of BR in MCL |

---

## US Market Information

Fifteen licenses are recorded. Five are listed below. The source data contains no approved-indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA 022249 | TREANDA (Cephalon) | Lyophilized powder for injection | Not provided |
| ANDA 205574 | Bendamustine hydrochloride (BluePoint) | Lyophilized powder for injection | Not provided |
| NDA 212209 | VIVIMUSTA (Slayback Pharma) | Injection | Not provided |
| NDA 212209 | VIVIMUSTA (Azurity) | Injection | Not provided |
| NDA 208194 | Bendeka (Teva) | Injection, solution | Not provided |

All listed products are injectables.

---

## Cytotoxicity

This section reflects general knowledge of the alkylating-agent class. The Evidence Pack contains no DrugBank toxicity data, so verify each item against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (bifunctional alkylating agent) |
| Myelosuppression Risk | High. Prolonged lymphopenia is a recognized concern, and the evidence review notes prolonged cytopenias. Trials of bendamustine-containing regimens report considerable hematological toxicity |
| Emetogenicity Classification | Moderate (class-based estimate) |
| Monitoring Items | CBC with differential and lymphocyte counts, liver and renal function, infection surveillance, long-term surveillance for secondary malignancy |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Guardrails from the evidence review**: monitor for prolonged lymphopenia, opportunistic infection and secondary malignancy. A retrieved claims-database study (PMID 36792059) addresses second cancer and infection risk after first-line BR in indolent B-cell lymphoma.
- **Cardiac safety**: a completed Phase 3 study (NCT01073163) assessed the effect of BR on the QT interval in patients with indolent NHL or MCL.

Please refer to the package insert for warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 randomized trials, a 2013 Lancet RCT, and 2022 and 2025 randomized trials of add-on agents on a BR backbone support bendamustine in MCL. Bendamustine appears in current European guidelines. Safety data are still missing from the provided records, so the recommendation stays conditional on safety guardrails.

**To proceed, the following is needed:**
- The package insert warnings and contraindications, which are a blocking data gap
- Confirmation of the US labeled indication for MCL (the license records contain no indication text)
- Detailed mechanism-of-action data from DrugBank
- Extraction of actual efficacy results (PFS, response rates) from the Phase 3 trials
- A monitoring plan for prolonged lymphopenia, infection and secondary malignancy

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Brentuximab Vedotin: From Hodgkin Lymphoma / sALCL to Follicular Lymphoma

## One-Sentence Summary

Brentuximab vedotin (Adcetris) is a CD30-directed antibody-drug conjugate (ADC), globally approved for classical Hodgkin lymphoma (cHL) and systemic anaplastic large cell lymphoma (sALCL), though not yet registered in the current Taiwan/US dataset.
The TxGNN model predicts it may be effective for **follicular lymphoma**,
with **6 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Classical Hodgkin lymphoma / Systemic anaplastic large cell lymphoma (global approvals; not retrieved in current dataset) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| US Market Status | Not retrieved (0 licenses in current dataset; likely data retrieval gap) |
| Number of NDAs | 0 |
| Recommended Decision | Research Question (Proceed with Guardrails) |

---

## Why is This Prediction Reasonable?

Brentuximab vedotin (BV) is an antibody-drug conjugate composed of an anti-CD30 monoclonal antibody (brentuximab) conjugated to the microtubule-disrupting cytotoxin monomethyl auristatin E (MMAE) via a protease-cleavable linker. Detailed MOA data was not retrieved in this Evidence Pack; however, the mechanism is well-characterized in the literature: upon binding to CD30-expressing tumor cells, the antibody-drug complex is internalized, MMAE is released intracellularly, and cell cycle arrest and apoptosis ensue. This mechanism is the foundation of BV's established activity in cHL and sALCL, both of which universally or near-universally express CD30.

Follicular lymphoma (FL) is a CD20-positive indolent B-cell lymphoma. While FL cells generally express CD30 at low levels, CD30 expression is notably upregulated in transformed FL — particularly in cases undergoing transformation to ALCL (CD30+ ALK-) or other high-grade lymphomas. This creates a biologically plausible niche for CD30-targeted therapy in selected FL subpopulations, especially in the relapsed/refractory setting where transformation events are more prevalent. A published case report (PMID 32476657) documents complete response with BV in exactly this scenario: Grade I FL transformed to CD30+ ALK1− ALCL.

Multiple Phase 2 trials have been designed to explore BV in R/R FL directly — the most active being NCT04587687 (BV + bendamustine, actively recruiting, n=23). However, the pattern of other FL-targeted BV trials being withdrawn or terminated early (primarily due to recruitment difficulties) highlights that CD30-low expression in bulk FL tumors creates real-world patient selection challenges. The TxGNN score of 99.89% reflects the knowledge graph proximity between BV's established lymphoma biology and FL's shared lymphoid ontogeny, rather than a guarantee of broad clinical efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | Directly tests BV + bendamustine in R/R follicular lymphoma; most representative active evidence for FL-specific BV application |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase I/II | Terminated | 20 | BV + rituximab as frontline therapy for CD30+ and/or EBV+ lymphomas including FL subgroup; terminated, limited data |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomized: rituximab + bendamustine ± BV for R/R CD30+ DLBCL; partial data available despite early termination |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | Withdrawn | 0 | Risk-stratified sequential BV-based treatment for post-transplant lymphoproliferative disorders with CD20/CD30 expression; no data |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | Withdrawn | 0 | BV + bendamustine + rituximab in R/R CD30+ B-cell NHL; withdrawn before enrollment, no data |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | Withdrawn | 0 | BV + pembrolizumab in recurrent systemic PTCL; not FL-specific, withdrawn with no data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case Report | The Gulf Journal of Oncology | Complete response with BV + high-dose methotrexate in Grade I FL transformed to CD30+ ALK1− ALCL; direct proof-of-concept for BV in transformed FL |
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Clinical Trial | Blood Advances | Phase 2 LYSA study: BV + gemcitabine in R/R PTCL (≥5% CD30+); provides BV activity benchmark in CD30-low settings relevant to FL |
| [34797505](https://pubmed.ncbi.nlm.nih.gov/34797505/) | 2022 | Prospective Study | Advances in Therapy | Real-world study of BV + CEP in CD30+ NHL subtypes including TFH-phenotype PTCL; establishes BV activity in lymphomas with shared CD30 biology |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leukemia Research Reports | Immunotherapy in indolent NHL including FL; discusses emerging role of novel agents and CD30 targeting in FL context |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | Current treatment approaches to PTCL subtypes; BV incorporation in CD30+ frontline regimens informs biomarker selection strategy applicable to FL |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | Review | Hematology (ASH Education Program) | Reviews BV incorporation into PTCL management and CD30 biomarker thresholds; relevant for designing FL patient selection criteria |
| [40517441](https://pubmed.ncbi.nlm.nih.gov/40517441/) | 2025 | Review | Hematological Oncology | Comprehensive PTCL landscape review; positions BV in CD30+ disease and discusses cross-subtype applicability |
| [28340875](https://pubmed.ncbi.nlm.nih.gov/28340875/) | 2017 | Review | Hematology/Oncology Clinics of North America | Angioimmunoblastic T-cell lymphoma review; discusses TFH-origin biology shared with FL microenvironment and BV relevance |
| [33320379](https://pubmed.ncbi.nlm.nih.gov/33320379/) | 2021 | Retrospective/Case Series | European Journal of Haematology | BV + ICE in R/R PTCL; provides efficacy and safety data for BV combination strategies in relapsed CD30+ lymphoid malignancies |
| [28967896](https://pubmed.ncbi.nlm.nih.gov/28967896/) | 2018 | Review | Bone Marrow Transplantation | Post-ASCT maintenance review covering BV consolidation in lymphoma including FL context; supports BV utility in maintenance settings |

---

## US Market Information

No FDA-licensed products for BRENTUXIMAB VEDOTIN were retrieved in the current dataset (0 records, query date 2026-03-24). This almost certainly reflects a data retrieval gap rather than an actual absence of US approval — brentuximab vedotin (Adcetris®, Seagen/Pfizer) holds multiple FDA-approved indications for CD30-positive lymphomas. A direct query to the FDA Orange Book or Drugs@FDA is recommended to complete this section.

---

## Cytotoxicity

Brentuximab vedotin is an antineoplastic agent (antibody-drug conjugate; original indication is CD30+ lymphoma).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Antibody-Drug Conjugate (ADC); MMAE payload is a conventional cytotoxin (microtubule inhibitor, auristatin class) |
| Myelosuppression Risk | Moderate-to-High — neutropenia is the most common grade ≥3 adverse event; thrombocytopenia and anemia also reported |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (each cycle), peripheral neuropathy assessment (early and ongoing), liver function tests, renal function, pulmonary symptoms monitoring |
| Handling Protection | Must be prepared and handled per cytotoxic drug handling regulations; MMAE is a highly potent cytotoxin requiring appropriate protective measures |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question (Proceed with Guardrails)**

**Rationale:**
There is one actively recruiting Phase 2 trial (NCT04587687) directly testing BV + bendamustine in R/R FL, providing an initial evidence signal; however, the high rate of trial withdrawal and termination across other FL-targeted BV studies indicates that low CD30 expression prevalence in FL creates substantial patient selection barriers before broader clinical development is warranted.

**To proceed, the following is needed:**

- **CD30 IHC profiling** of FL tumor samples (IHC ≥10% threshold): must be confirmed before patient recruitment — this is the rate-limiting step and likely explains prior trial recruitment failures
- **MOA data retrieval** from DrugBank (DG002: High severity gap) to complete mechanistic rationale documentation
- **Safety data from FDA/TFDA package insert** (DG001: Blocking gap) — required to initiate formal S1 safety screening
- **Await NCT04587687 results** (Phase 2, BV + bendamustine in R/R FL, n=23, completion expected 2026-12): current trial provides the cleanest direct evidence; interim data should be reviewed before designing new studies
- **Epidemiological estimate of CD30+ FL prevalence**: quantify the eligible patient subpopulation to assess commercial and clinical feasibility
- **Data linkage to transformed FL registry**: the case with BV response (PMID 32476657) suggests transformed FL may be the highest-yield subpopulation; a retrospective chart review of transformed FL CD30 rates should be conducted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


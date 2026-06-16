---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 556
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cyclophosphamide: From Transplant Conditioning to Myeloid Leukemia

## One-Sentence Summary

Cyclophosphamide (DB00531) is a classical DNA alkylating agent with a decades-long history of use in hematopoietic stem cell transplantation (HSCT) conditioning regimens and post-transplant graft-versus-host disease (GvHD) prophylaxis.
The TxGNN model predicts it may be effective for **Myeloid Leukemia** as an extended therapeutic indication,
with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal TFDA registration records available |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known clinical information, cyclophosphamide is a nitrogen mustard alkylating chemotherapy agent that forms DNA interstrand crosslinks, disrupting DNA replication and triggering apoptosis in rapidly proliferating cells — a mechanism that makes it particularly effective against hematopoietic malignancies.

In myeloid leukemia treatment, cyclophosphamide plays two clinically distinct roles. First, as a cornerstone of myeloablative conditioning regimens (Bu/Cy: busulfan + cyclophosphamide; or Cy/TBI: cyclophosphamide + total body irradiation), it eradicates residual leukemia cells and creates marrow space for donor engraftment before HSCT. Second, as post-transplant cyclophosphamide (PTCy, administered at 50 mg/kg on Day +3 and +4), it selectively eliminates alloreactive T cells while sparing regulatory T cells and memory lymphocytes, becoming the current standard GvHD prophylaxis strategy for haploidentical transplantation in AML.

The TxGNN high-confidence prediction is well grounded: Bu/Cy and PTCy regimens are validated across large EBMT and CIBMTR registry studies encompassing thousands of AML patients. The network meta-analysis of MAC regimens (PMID 36357773, n > 1,000) positions Bu/Cy as the reference standard conditioning regimen for AML undergoing allo-HSCT, and the emergence of PTCy as universal GvHD prophylaxis extends cyclophosphamide's therapeutic footprint directly into the myeloid leukemia management pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02065154](https://clinicaltrials.gov/study/NCT02065154) | Phase 2 | Completed | 39 | Direct assessment of post-transplant cyclophosphamide (PTCy) for GvHD prophylaxis in matched and mismatched unrelated donor HSCT; primary endpoint was incidence of Grade II–IV acute GvHD following cyclophosphamide on Day +3/+4 |
| [NCT00723099](https://clinicaltrials.gov/study/NCT00723099) | Phase 2 | Completed | 73 | Umbilical cord blood transplant with reduced-intensity conditioning including cyclophosphamide for hematological malignancies; multi-center study completed over a decade of follow-up |
| [NCT01947322](https://clinicaltrials.gov/study/NCT01947322) | Phase 1/2 | Completed | 10 | Haploidentical NK cell adoptive immunotherapy for poor-prognosis AML; cyclophosphamide used for immune depletion before NK infusion, with direct AML cytoreductive intent |
| [NCT00003340](https://clinicaltrials.gov/study/NCT00003340) | Phase 2 | Completed | N/A | Cyclophosphamide followed by topotecan directly for refractory or relapsed acute myelogenous leukemia — the most direct evidence of cyclophosphamide as standalone cytoreductive agent in AML |
| [NCT00005804](https://clinicaltrials.gov/study/NCT00005804) | Phase 2 | Completed | N/A | Bone marrow transplantation from HLA-incompatible unrelated donors for hematologic malignancies; cyclophosphamide as standard conditioning component with myeloablative intent |
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | Completed | 202 | Randomized comparison of G-CSF + Decitabine + Bu/Cy vs Bu/Cy alone as myeloablative conditioning for RAEB-1, RAEB-2, and AML secondary to MDS — largest randomized study directly evaluating cyclophosphamide-based conditioning |
| [NCT03766126](https://clinicaltrials.gov/study/NCT03766126) | Phase 1 | Active, not recruiting | 22 | Anti-CD123 CAR-T cell therapy for refractory/relapsed AML; cyclophosphamide administered as preconditioning lymphodepletion, demonstrating mechanistic synergy with cellular immunotherapy |
| [NCT03326921](https://clinicaltrials.gov/study/NCT03326921) | Phase 1 | Recruiting | 24 | HA-1 TCR-redirected CD8+/CD4+ T cell adoptive immunotherapy for relapsed AML post-HSCT; cyclophosphamide used for lymphodepletion to facilitate T cell engraftment |
| [NCT02120157](https://clinicaltrials.gov/study/NCT02120157) | Phase 2 | Completed | 35 | Multi-institutional pediatric haploidentical BMT with post-transplant cyclophosphamide for high-risk leukemia; myeloid leukemia subgroup received busulfan-based myeloablative conditioning |
| [NCT06802315](https://clinicaltrials.gov/study/NCT06802315) | Phase 2 | Recruiting | 38 | Intensity-modulated total marrow irradiation (9 Gy) combined with Flu/Bu4 conditioning and PTCy (Day +3/+4) for high-risk AML, CML, and MDS — represents the next-generation HSCT platform incorporating PTCy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic Review / Network Meta-Analysis | Bone Marrow Transplantation | Bayesian network meta-analysis of MAC regimens in adult AML undergoing allo-HSCT in complete remission; Bu/Cy positioned as the reference standard against which all other conditioning regimens are compared |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | RCT / Retrospective Comparison | Future Oncology | BuCy vs FluBu for allo-HSCT in AML; BuCy (the cyclophosphamide-containing standard regimen) compared for efficacy and toxicity against the emerging cyclophosphamide-free alternative |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Phase 2 Trial | Transplant Immunology | Cladribine + BuCy as intensified conditioning for relapsed/refractory AML undergoing allo-HSCT; demonstrates cyclophosphamide-based conditioning can be augmented for higher-risk disease |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Prospective Cohort | Cytotherapy | Prognostic factors in haploidentical HCT with PTCy specifically for AML; confirms that PTCy is effective GvHD suppression for AML in the haplo-HCT setting |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Retrospective Cohort | Bone Marrow Transplantation | Largest PTCy-AML dataset to date: 1,823 AML patients in CR1 receiving HSCT with PTCy; analyzes impact of conditioning intensity by cytogenetic/molecular risk — defines PTCy standard of care |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Retrospective Cohort | European Journal of Haematology | MAC vs RIC in AML patients <65 years receiving ATG + PTCy-based GvHD prophylaxis; evaluates whether higher-intensity cyclophosphamide-containing conditioning improves disease control |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Comparative Cohort | International Journal of Molecular Sciences | First published data on PTCy for pediatric AML after matched-donor (related and unrelated) HSCT; fills a critical evidence gap for cyclophosphamide use in pediatric myeloid disease |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Registry Analysis | Haematologica | 217 AML patients in complete remission receiving myeloablative HCT with PTCy-based GvHD prophylaxis; 2-year OS 77%, EFS 72% — confirms durable outcomes across genetic risk categories |
| [32428903](https://pubmed.ncbi.nlm.nih.gov/32428903/) | 2021 | Prospective Cohort | Acta Haematologica | PTCy (50 mg/kg Day +3/+4) combined with ATG for GvHD prophylaxis in high-risk AML and MDS; compared against alternative prophylaxis regimens, supporting PTCy combination strategies |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | Retrospective Case Series | Leukemia & Lymphoma | High-dose cyclophosphamide (60 mg/kg) as direct cytoreduction in 27 AML patients presenting with hyperleukocytosis or leukostasis; demonstrates standalone cytoreductive use of cyclophosphamide outside the transplant context |

---

## Taiwan Market Information

No Taiwan FDA (TFDA) registration records are available for cyclophosphamide in this evidence pack. The drug is currently not listed as a marketed product in the queried TFDA database.

> **Note:** The absence of TFDA registration data may reflect database coverage limitations or off-label/hospital formulary use patterns. Clinical use in Taiwan may occur through special import mechanisms. Verification with the current TFDA database and hospital procurement records is recommended before any regulatory or access pathway decisions.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent (Nitrogen mustard class; prodrug activated by hepatic CYP2B6 and CYP3A4 to 4-hydroxycyclophosphamide) |
| Myelosuppression Risk | High — Dose-dependent leukopenia, neutropenia, thrombocytopenia, and anemia; nadir typically at Day 10–14 post-administration; high-dose regimens (≥50 mg/kg) used in HSCT conditioning require growth factor support |
| Emetogenicity Classification | Moderate to High (dose-dependent: oral metronomic dosing is low emetogenic; standard-dose IV is moderate; high-dose HSCT conditioning is highly emetogenic, requiring prophylactic 5-HT3 antagonist + NK1 antagonist) |
| Monitoring Items | CBC with differential (at least weekly during treatment and post-HSCT); serum creatinine and BUN; liver enzymes (ALT, AST); urinalysis and urine dipstick for hematuria (hemorrhagic cystitis monitoring); electrolytes (SIADH risk at high doses) |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system drug transfer devices (CSTD) required during preparation; preparation in a certified biological safety cabinet (BSC); double-glove, gown, and eye protection; waste disposed as hazardous cytotoxic waste |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for myeloid leukemia is supported by Level 1 evidence, including a network meta-analysis spanning thousands of AML patients, multiple completed Phase 2/3 transplant trials, and a large EBMT registry cohort (n = 1,823) — all confirming cyclophosphamide's central, well-established role in AML management through Bu/Cy conditioning and PTCy GvHD prophylaxis.

**To proceed, the following is needed:**
- Obtain formal mechanism of action documentation by querying the DrugBank API (Data Gap DG002) to complete mechanistic analysis
- Clarify the target therapeutic context: distinguish between (a) Bu/Cy myeloablative HSCT conditioning, (b) PTCy post-transplant GvHD prophylaxis, and (c) direct cytoreductive use in non-transplant AML — each requires distinct clinical protocols and risk stratification
- Verify current TFDA regulatory approval pathway or identify the appropriate special access mechanism for cyclophosphamide in Taiwan
- Establish a safety monitoring protocol addressing: MESNA co-administration for hemorrhagic cystitis prevention (mandatory at doses ≥10 mg/kg), myelosuppression management plan, and gonadotoxicity counseling for patients of reproductive age
- Download and parse the TFDA package insert PDF (Data Gap DG001) to complete the formal safety profile assessment before clinical implementation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


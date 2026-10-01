---
layout: default
title: Belinostat
parent: Model Prediction Only (L5)
nav_order: 441
evidence_level: L5
indication_count: 3
---

# Belinostat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Belinostat: From T-Cell Lymphoma to Myeloid Leukemia

## One-Sentence Summary

Belinostat is an intravenous histone deacetylase (HDAC) inhibitor. Published literature describes it as approved for T-cell lymphomas.
The TxGNN model predicts it may be effective for **myeloid leukemia**, and **6 clinical trials** and **20 publications** are linked to this prediction.
Most of that evidence is early-phase combination studies and preclinical work, so efficacy is not yet established.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | T-cell lymphomas (per literature; the US license record supplied has no indication text) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L2 (as assigned in the Evidence Pack; the one completed Phase 2 study is single-arm, not randomized) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From general knowledge, belinostat is a pan-HDAC inhibitor. HDAC inhibition can reactivate silenced tumor suppressor genes and promote apoptosis and differentiation in cancer cells. Its efficacy in T-cell lymphoma is established, and mechanistically it may also apply to myeloid leukemia.

Both T-cell lymphoma and acute myeloid leukemia (AML) are blood cancers with abnormal epigenetic regulation. Preclinical work supports this: belinostat has anti-leukemic activity in acute promyelocytic leukemia cells and primary AML cells.

The data also suggest that combinations are more promising than monotherapy. Published studies show synergy with:

- proteasome inhibition (bortezomib)
- NEDD8 inhibition (pevonedistat)
- WEE1 inhibition (adavosertib)

Consistent with this, PMID 39821392 notes that belinostat and pevonedistat each showed only limited single-agent activity in blood cancers.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00357032](https://clinicaltrials.gov/study/NCT00357032) | Phase 2 | Completed | 12 | Belinostat (PXD101) alone in relapsed/refractory AML, or newly diagnosed AML in patients over 60. Highest-phase direct evidence, but efficacy outcomes are not in the provided data. |
| [NCT00878722](https://clinicaltrials.gov/study/NCT00878722) | Phase 1/2 | Completed | 41 | Belinostat plus idarubicin in AML patients unsuitable for standard intensive therapy. Two schedules tested for safety and early efficacy. |
| [NCT01075425](https://clinicaltrials.gov/study/NCT01075425) | Phase 1 | Completed | 41 | Belinostat plus bortezomib in relapsed/refractory acute leukemia or MDS. Dose finding and safety. |
| [NCT00351975](https://clinicaltrials.gov/study/NCT00351975) | Phase 1 | Completed | 56 | Belinostat plus azacitidine in advanced hematologic malignancies. Broader population, so the match to myeloid leukemia is partial. |
| [NCT03772925](https://clinicaltrials.gov/study/NCT03772925) | Phase 1 | Terminated | 18 | Pevonedistat plus belinostat in relapsed/refractory AML or MDS. Early termination limits interpretation. |
| [NCT02381548](https://clinicaltrials.gov/study/NCT02381548) | Phase 1 | Terminated | 20 | Adavosertib plus belinostat in relapsed/refractory myeloid malignancies. Early termination limits interpretation. |

No Phase 3 trials exist.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [24369094](https://pubmed.ncbi.nlm.nih.gov/24369094/) | 2014 | Phase 2 trial | Leuk Lymphoma | Belinostat 1000 mg/m² IV on days 1-5 of a 21-day cycle in relapsed/refractory AML or newly diagnosed AML over age 60. Primary endpoint was complete response rate. Results are not in the excerpt provided. |
| [39821392](https://pubmed.ncbi.nlm.nih.gov/39821392/) | 2025 | Phase 1 trial | Cancer Chemother Pharmacol | Belinostat plus pevonedistat in relapsed/refractory AML or high-risk MDS, following preclinical synergy data. |
| [36864346](https://pubmed.ncbi.nlm.nih.gov/36864346/) | 2023 | Phase 1 trial | Cancer Chemother Pharmacol | Belinostat plus adavosertib in relapsed/refractory myeloid malignancies. Preclinical synergy was shown in AML lines and xenografts. |
| [33356689](https://pubmed.ncbi.nlm.nih.gov/33356689/) | 2021 | Phase 1 trial | Leuk Lymphoma | Belinostat plus bortezomib in 38 patients. QTc prolongation was the only dose-limiting toxicity. Recommended Phase 2 doses were bortezomib 1.3 mg/m² and belinostat 1000 mg/m². |
| [26851293](https://pubmed.ncbi.nlm.nih.gov/26851293/) | 2016 | Preclinical | Blood | Pevonedistat plus belinostat synergistically induced AML cell apoptosis, including cells with p53 deficiency or FLT3-ITD, by disrupting the DNA damage response. |
| [21375523](https://pubmed.ncbi.nlm.nih.gov/21375523/) | 2011 | Preclinical | Br J Haematol | Belinostat plus bortezomib sharply increased apoptosis in AML and ALL cell lines and primary blasts, linked to NF-κB and Bim changes. |
| [24800886](https://pubmed.ncbi.nlm.nih.gov/24800886/) | 2014 | Preclinical | Anti-Cancer Drugs | Characterizes belinostat's epigenetic and molecular effects in acute promyelocytic leukemia cells, alone and combined with all-trans retinoic acid. |
| [25864732](https://pubmed.ncbi.nlm.nih.gov/25864732/) | 2015 | Preclinical | J Cell Mol Med | Belinostat has anti-leukemic effects in acute promyelocytic leukemia cells via chromatin remodelling. |
| [17982680](https://pubmed.ncbi.nlm.nih.gov/17982680/) | 2007 | Preclinical | Int J Oncol | HDAC inhibitors including PXD101 inhibited proliferation and increased apoptosis in primary cells from 59 AML patients. Patient subgroups differed in susceptibility. |
| [26447190](https://pubmed.ncbi.nlm.nih.gov/26447190/) | 2015 | Preclinical | Blood | Genetic and pharmacological dissection of HDAC dependencies in mouse lymphoid and myeloid leukemias. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA206256 | Beleodaq (Acrotech Biopharma Inc) | Lyophilized powder for injection | Indication text not included in the provided record |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/epigenetic therapy (HDAC inhibitor), used within cytotoxic combination regimens |
| Myelosuppression Risk | Medium (general knowledge for HDAC inhibitors; confirm against the package insert) |
| Emetogenicity Classification | Low to medium (general knowledge; confirm against the package insert) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, ECG/QTc (QTc prolongation was the only dose-limiting toxicity in the belinostat plus bortezomib Phase 1) |
| Handling Protection | Follow institutional cytotoxic drug handling regulations. Please refer to the package insert warnings and precautions. |

---

## Safety Considerations

- **QTc prolongation**: it was the only dose-limiting toxicity in the belinostat plus bortezomib Phase 1 study (PMID 33356689). Cardiac monitoring is therefore relevant in combination regimens.

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted score is high and there is a plausible mechanism and preclinical synergy. However, the clinical evidence is limited to small Phase 1 and Phase 2 studies, and half of the combination trials were terminated early. There is no randomized or Phase 3 evidence, and efficacy outcomes are missing from the provided data. The package insert warnings and contraindications are also missing, which the pack marks as a blocking gap for safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap DG001)
- Efficacy results (response rates) from the published NCT00357032 and NCT00878722 studies (PMIDs 24369094 and others)
- Confirmed mechanism of action from DrugBank (DG002)
- US indication text for NDA206256, to confirm the original indication
- A randomized or controlled trial design, most likely a combination regimen rather than monotherapy

**Other predicted indications:** plasma cell myeloma (score 99.27%) has only two small Phase 2 trials, one terminated after 4 patients and the other enrolling 25, with no efficacy data. Indolent plasma cell myeloma (99.08%) has no trials or literature and is on Hold.

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


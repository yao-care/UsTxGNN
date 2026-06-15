---
layout: default
title: Belinostat
parent: 僅模型預測 (L5)
nav_order: 441
evidence_level: L5
indication_count: 3
---

# Belinostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

The txgnn-pipeline skill covers infrastructure and pipeline management, which doesn't override the report-writing instructions already in my system prompt. I'll proceed directly with generating the report from the Evidence Pack.

---

# Belinostat: From Peripheral T-cell Lymphoma to Myeloid Leukemia

## One-Sentence Summary

Belinostat is an intravenous pan-HDAC inhibitor clinically approved for relapsed or refractory peripheral T-cell lymphoma (PTCL).
The TxGNN model predicts it may be effective for **Myeloid Leukemia**, with **6 clinical trials** and **20 publications** currently supporting this direction.
The overall evidence level reaches **L2**, driven by multiple completed Phase 1/2 studies directly enrolling AML patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peripheral T-cell Lymphoma (PTCL) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed (0 TFDA licenses) |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on market status**: While belinostat has no Taiwan (TFDA) registration, it is FDA-approved in the United States under the brand name **Beleodaq** (Spectrum Pharmaceuticals) for relapsed/refractory PTCL. Taiwan market entry would require a separate TFDA submission.

---

## Why is This Prediction Reasonable?

Belinostat is a pan-HDAC inhibitor that targets Class I (HDAC1, 2, 3, 8) and Class II (HDAC4–10) histone deacetylase enzymes. Although detailed MOA documentation is not available in this Evidence Pack, clinical trial records and published literature consistently describe its mechanism: by blocking HDAC enzymes, belinostat prevents the removal of acetyl groups from histone proteins, restoring an open chromatin state and reactivating epigenetically silenced tumor suppressor genes. This leads to cell cycle arrest, induction of apoptosis via the mitochondrial pathway, and promotion of myeloid differentiation.

In acute myeloid leukemia (AML), HDACs are frequently overexpressed, and this overexpression is a core driver of leukemogenesis—epigenetically silencing genes that would otherwise halt malignant proliferation or trigger differentiation. This makes HDAC inhibition a mechanistically direct strategy in AML, not a peripheral one. Preclinical studies have shown that belinostat restores gene expression, induces apoptosis, and promotes differentiation in primary AML cells and established AML cell lines.

Several rationally designed combination strategies further strengthen the case. Belinostat demonstrates additive or synergistic anti-AML effects when paired with hypomethylating agents such as azacitidine (via "epigenetic priming"), with the proteasome inhibitor bortezomib (via NF-κB suppression and Bim upregulation), with the anthracycline idarubicin, and with the NAE/neddylation inhibitor pevonedistat (by disrupting the DNA damage response, independently of p53 or FLT3-ITD status). This breadth of mechanistically validated partners indicates that belinostat acts on a foundational AML vulnerability rather than a narrow target.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00357032](https://clinicaltrials.gov/study/NCT00357032) | Phase 2 | Completed | 12 | Single-agent belinostat (1000 mg/m² IV, Days 1–5 every 21 days) in R/R AML or newly diagnosed AML in patients over age 60; primary endpoint was complete response rate |
| [NCT00878722](https://clinicaltrials.gov/study/NCT00878722) | Phase 1/2 | Completed | 41 | Belinostat + idarubicin in AML patients unsuitable for standard intensive chemotherapy; two dosing schedules assessed for safety and early efficacy |
| [NCT01075425](https://clinicaltrials.gov/study/NCT01075425) | Phase 1 | Completed | 41 | Belinostat + bortezomib in R/R acute leukemia and MDS; QTc prolongation identified as the dose-limiting toxicity; recommended Phase 2 doses established |
| [NCT00351975](https://clinicaltrials.gov/study/NCT00351975) | Phase 1 | Completed | 56 | Belinostat + azacitidine in advanced hematologic malignancies including AML; largest enrollment in this indication, established tolerability baseline |
| [NCT03772925](https://clinicaltrials.gov/study/NCT03772925) | Phase 1 | Terminated | 18 | Belinostat + pevonedistat (NAE inhibitor) in R/R AML or MDS; terminated early but results published in 2025 (PMID 39821392); most recent combination data |
| [NCT02381548](https://clinicaltrials.gov/study/NCT02381548) | Phase 1 | Terminated | 20 | Belinostat + adavosertib (Wee1 inhibitor, AZD1775) in R/R myeloid malignancies and untreated AML; terminated early; published 2023 (PMID 36864346) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [24369094](https://pubmed.ncbi.nlm.nih.gov/24369094/) | 2014 | Phase 2 Clinical Trial | Leukemia & Lymphoma | Open-label Phase 2 study (NCT00357032) of belinostat monotherapy in R/R AML and newly diagnosed AML ≥60; defines single-agent activity and tolerability profile |
| [39821392](https://pubmed.ncbi.nlm.nih.gov/39821392/) | 2025 | Phase 1 Clinical Trial | Cancer Chemotherapy and Pharmacology | Belinostat + pevonedistat in R/R AML/MDS; despite early termination, provides 2025 combination safety and preliminary efficacy data |
| [36864346](https://pubmed.ncbi.nlm.nih.gov/36864346/) | 2023 | Phase 1 Clinical Trial | Cancer Chemotherapy and Pharmacology | Belinostat + adavosertib (Wee1 inhibitor) in R/R myeloid malignancies; preclinical synergy confirmed in AML xenograft models; early clinical translation |
| [33356689](https://pubmed.ncbi.nlm.nih.gov/33356689/) | 2021 | Phase 1 Clinical Trial | Leukemia & Lymphoma | Belinostat + bortezomib in R/R acute leukemia/MDS; one complete response observed in MLL-rearranged biphenotypic AML with complex karyotype |
| [26851293](https://pubmed.ncbi.nlm.nih.gov/26851293/) | 2016 | Preclinical / Mechanistic | Blood | Synergistic AML apoptosis with pevonedistat + belinostat via DDR disruption; efficacy maintained regardless of p53 status or FLT3-ITD mutation |
| [27151736](https://pubmed.ncbi.nlm.nih.gov/27151736/) | 2016 | Editorial / Review | Blood | Commentary on NEDD8 and HDAC co-targeting in AML; validates mechanistic rationale of the pevonedistat + belinostat combination |
| [21375523](https://pubmed.ncbi.nlm.nih.gov/21375523/) | 2011 | In vitro / Preclinical | British Journal of Haematology | Bortezomib + belinostat synergistic apoptosis in AML and ALL cell lines and primary blasts; mediated via NF-κB suppression and Bim upregulation |
| [28192098](https://pubmed.ncbi.nlm.nih.gov/28192098/) | 2017 | In vitro / Preclinical | European Journal of Pharmacology | Anti-leukemic activity of belinostat + HMT inhibitor 3-deazaneplanocin A in acute promyelocytic leukemia (APL) cells; dual epigenetic targeting |
| [25864732](https://pubmed.ncbi.nlm.nih.gov/25864732/) | 2015 | In vitro / Preclinical | Journal of Cellular and Molecular Medicine | Belinostat induces antileukemic effects in APL via chromatin remodelling; studied as monotherapy and in combination |
| [24800886](https://pubmed.ncbi.nlm.nih.gov/24800886/) | 2014 | Preclinical / Mechanistic | Anti-cancer Drugs | Epigenetic and molecular mechanisms of belinostat antileukemic activity in APL; potential for differentiation therapy including combination with ATRA |

---

## Cytotoxicity

Belinostat is an antineoplastic agent (pan-HDAC inhibitor, hydroxamate class) used in the treatment of hematological malignancies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted epigenetic therapy — pan-HDAC inhibitor (hydroxamate class); not classical cytotoxic chemotherapy |
| Myelosuppression Risk | Moderate — thrombocytopenia and neutropenia are reported across multiple clinical trials; dose-limiting in some combinations |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly during Cycle 1, then each cycle), liver function tests (AST/ALT/bilirubin), renal function, QTc interval (ECG monitoring before and during treatment) |
| Handling Protection | Must follow cytotoxic drug handling regulations; IV preparation should use a closed-system drug transfer device |

---

## Safety Considerations

No Taiwan-specific safety data (TFDA package insert warnings or contraindications) is available in this Evidence Pack. Drug-drug interaction data was not retrievable at the time of query.

Please refer to the **Beleodaq (belinostat) US FDA package insert** (Spectrum Pharmaceuticals) for comprehensive safety information, including hematologic toxicity, serious infections, hepatotoxicity, QTc prolongation, tumor lysis syndrome risk, and embryo-fetal toxicity.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 1/2 clinical trials have directly studied belinostat in AML populations with published results, establishing both a credible efficacy signal and a characterized safety profile. The mechanistic basis—HDAC overexpression driving epigenetic silencing in AML—is well-established, and the drug's FDA approval for PTCL confirms clinical-grade tolerability. The evidence level (L2) and TxGNN score (99.53%) together justify moving forward under appropriate monitoring conditions.

**To proceed, the following is needed:**

- **Full safety documentation**: Obtain and formally review the Beleodaq US FDA label; assess transferability to Taiwan (TFDA bridging requirements)
- **MOA documentation**: Retrieve complete DrugBank mechanistic data (DrugBank ID: DB05015) to formally document target engagement rationale
- **Efficacy data compilation**: Extract and summarize response rates (CR/PR/ORR) from NCT00357032 and NCT00878722 to define the therapeutic benchmark for a repurposing trial
- **Combination strategy decision**: Select the most clinically relevant combination partner for the intended AML patient population (e.g., azacitidine for frontline unfit patients, or idarubicin for intensification)
- **Taiwan regulatory pathway assessment**: Evaluate whether a new TFDA NDA submission or a bridging study is required for Taiwan market entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


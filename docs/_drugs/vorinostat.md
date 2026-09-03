---
layout: default
title: Vorinostat
parent: 僅模型預測 (L5)
nav_order: 1296
evidence_level: L5
indication_count: 2
---

# Vorinostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Vorinostat: From Cutaneous T-Cell Lymphoma to Primary Cutaneous B-Cell Lymphoma

## One-Sentence Summary

Vorinostat is an oral HDAC (histone deacetylase) inhibitor originally developed for cutaneous T-cell lymphoma (CTCL); no confirmed original-indication text is on file in this evidence pack.
The TxGNN model's top prediction is **primary cutaneous B-cell lymphoma (PCBCL)**, currently supported by **8 clinical trials (none disease-specific)** and **1 mechanistic publication**.
A second, substantially stronger candidate — **Sézary syndrome** — is also flagged in this pack, backed by a completed Phase 3 RCT (MAVORIC, n=372) and 20 publications; it is reported separately below because its evidence tier (L1) differs markedly from the primary prediction (L4).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this pack (data gap). Literature context indicates vorinostat is marketed as Zolinza® for cutaneous T-cell lymphoma (CTCL). |
| Predicted New Indication | Primary Cutaneous B-Cell Lymphoma (PCBCL) |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (0 licenses on file — see note below) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (original_moa = Data Gap). Based on evidence collected from the linked trials and literature, vorinostat is a histone deacetylase (HDAC) inhibitor that induces chromatin remodeling in malignant lymphocytes, leading to cell-cycle arrest (p21 induction) and apoptosis via caspase activation. It is an approved oral therapy for cutaneous T-cell lymphoma (CTCL).

The mechanistic rationale for PCBCL is that HDAC inhibition could theoretically induce apoptosis in malignant B-cells through epigenetic reprogramming, analogous to its established effect in T-cell lymphoma. However, the only mechanistic literature identified (PMID 21652541) demonstrates this effect in **mantle cell lymphoma** — a nodal/systemic B-cell neoplasm — not in **primary cutaneous** B-cell lymphoma. These two entities differ substantially in clinical course and tumor microenvironment, so the mechanistic extrapolation from mantle cell lymphoma to PCBCL is indirect and currently unproven in disease-specific models or trials.

No clinical trial in this pack directly enrolled PCBCL patients; the eight trials listed are either off-target populations (solid tumors, GVHD, mixed lymphoid malignancies) or use a different investigational drug. This is consistent with the L4 evidence tier (mechanism/preclinical only, no disease-specific clinical data).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01567709](https://clinicaltrials.gov/study/NCT01567709) | Phase 1 | Completed | 34 | Alisertib + vorinostat combination in relapsed lymphoid malignancies (Hodgkin, B-NHL, PTCL); not PCBCL-specific |
| [NCT00499811](https://clinicaltrials.gov/study/NCT00499811) | Phase 1 | Completed | 15 | PK study of vorinostat in solid tumors/lymphoma with hepatic dysfunction |
| [NCT00045006](https://clinicaltrials.gov/study/NCT00045006) | Phase 1 | Completed | N/A | Early oral SAHA (vorinostat) dose-finding in advanced solid tumors and hematologic malignancies |
| [NCT01789255](https://clinicaltrials.gov/study/NCT01789255) | Phase 2 | Completed | 12 | Vorinostat + tacrolimus + methotrexate for GVHD prevention — indication unrelated to PCBCL |
| [NCT00007345](https://clinicaltrials.gov/study/NCT00007345) | Phase 2 | Completed | 131 | Depsipeptide (not vorinostat) in CTCL/PTCL — drug mismatch |
| [NCT01500538](https://clinicaltrials.gov/study/NCT01500538) | Phase 2 | Terminated | 1 | Vorinostat + eltrombopag in lymphoma; terminated, no statistical power |
| [NCT00005634](https://clinicaltrials.gov/study/NCT00005634) | Phase 1 | Completed | N/A | Early SAHA pharmacology study in advanced solid tumors |
| [NCT02943642](https://clinicaltrials.gov/study/NCT02943642) | Phase 2 | Unknown | 162 | Resimmune vs. oral vorinostat in mycosis fungoides — different drug and disease |

No trial in this pack specifically enrolled or reported outcomes for primary cutaneous B-cell lymphoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21652541](https://pubmed.ncbi.nlm.nih.gov/21652541/) | 2011 | Mechanistic (in vitro) | Clinical Cancer Research | Vorinostat induces apoptosis in mantle cell lymphoma via acetylation of proapoptotic BH3-only gene promoters; mechanism study, not PCBCL-specific |

---

## US Market Information

No marketing authorization records are present in this evidence pack (0 licenses, market_status = "Not Marketed"). Vorinostat is internationally known as Zolinza® (approved for CTCL in some jurisdictions); the absence of license records here should be treated as a data gap pending regulatory-source verification, not confirmation of non-approval.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HDAC inhibitor); classified within antineoplastic agents |
| Myelosuppression Risk | Moderate — trial-level evidence (NCT01500538) notes thrombocytopenia (low platelet counts) commonly observed early in treatment |
| Emetogenicity Classification | Low to moderate (class-based; no drug-specific toxicity data in this pack) |
| Monitoring Items | CBC with differential and platelets, electrolytes, renal and hepatic function, ECG (QT interval) |
| Handling Protection | Please refer to the package insert warnings and precautions; no drug-specific handling protocol available in this pack |

---

## Safety Considerations

Please refer to the package insert for safety information. All structured safety fields (key warnings, contraindications, drug interactions) are marked as data gaps in this evidence pack.

---

## Conclusion and Next Steps (Primary Cutaneous B-Cell Lymphoma)

**Decision: Hold**

**Rationale:**
No PCBCL-specific clinical trials exist, and the only supporting literature is a mechanistic study in a different B-cell neoplasm (mantle cell lymphoma). Evidence level L4 does not support progression beyond hypothesis stage.

**To proceed, the following is needed:**
- Confirmed original MOA and original indication documentation
- PCBCL-specific preclinical or case-series data
- TFDA/regulatory label data (currently a Blocking data gap per meta.data_gaps)
- Vorinostat safety/DDI profile from an authoritative source

---

# Additional Predicted Indication: Sézary Syndrome (Stronger Evidence — L1)

This evidence pack also identifies **Sézary syndrome** as a TxGNN candidate with substantially stronger clinical support than the primary prediction above, and is reported here for decision completeness.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Sézary Syndrome |
| TxGNN Prediction Score | 99.07% |
| Evidence Level | L1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Sézary syndrome is the leukemic, aggressive variant of cutaneous T-cell lymphoma (CTCL). Vorinostat's original approved indication (CTCL) and Sézary syndrome sit on the same disease spectrum rather than representing a mechanistic extrapolation — the HDAC-inhibition mechanism (chromatin remodeling, cell-cycle arrest, apoptosis in malignant T-lymphocytes) is directly applicable, and vorinostat has in fact been used clinically as an active comparator in Sézary syndrome trials.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01728805](https://clinicaltrials.gov/study/NCT01728805) | Phase 3 | Completed | 372 | **MAVORIC trial** — mogamulizumab vs. vorinostat in relapsed/refractory CTCL (including Sézary syndrome); vorinostat used as active comparator, direct disease-specific RCT data |
| [NCT00091559](https://clinicaltrials.gov/study/NCT00091559) | Phase 2b | Completed | 74 | Multicenter trial of oral SAHA (vorinostat) in advanced CTCL, stage IB+, post-progression on ≥2 prior therapies |
| [NCT01567709](https://clinicaltrials.gov/study/NCT01567709) | Phase 1 | Completed | 34 | Alisertib + vorinostat in relapsed lymphoid malignancies including CTCL-related entities |
| [NCT00601718](https://clinicaltrials.gov/study/NCT00601718) | Phase 1/2 | Completed | 29 | Vorinostat + rituximab/ifosfamide/carboplatin/etoposide in relapsed lymphoid malignancies |
| [NCT00499811](https://clinicaltrials.gov/study/NCT00499811) | Phase 1 | Completed | 15 | PK study of vorinostat in solid tumors/lymphoma with hepatic dysfunction |
| [NCT00045006](https://clinicaltrials.gov/study/NCT00045006) | Phase 1 | Completed | N/A | Early oral SAHA dose-finding in advanced solid tumors/hematologic malignancies |
| [NCT00005634](https://clinicaltrials.gov/study/NCT00005634) | Phase 1 | Completed | N/A | Early SAHA pharmacology study in advanced solid tumors |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30100375](https://pubmed.ncbi.nlm.nih.gov/30100375/) | 2018 | RCT | Lancet Oncology | MAVORIC Phase 3 RCT: mogamulizumab vs. vorinostat in previously treated CTCL/Sézary syndrome; establishes vorinostat efficacy/safety benchmark in this population |
| [31366601](https://pubmed.ncbi.nlm.nih.gov/31366601/) | 2019 | Regulatory Summary | Clinical Cancer Research | FDA approval summary for mogamulizumab, detailing MAVORIC trial design with vorinostat as comparator arm (n=372) |
| [40072489](https://pubmed.ncbi.nlm.nih.gov/40072489/) | 2025 | Review | J Cutaneous Medicine and Surgery | Oral systemic therapies for MF/Sézary syndrome, including vorinostat |
| [35444765](https://pubmed.ncbi.nlm.nih.gov/35444765/) | 2022 | Review | Mediterranean J Hematology and Infectious Diseases | Treatment of advanced-stage MF/Sézary syndrome, hematologist's perspective |
| [31192214](https://pubmed.ncbi.nlm.nih.gov/31192214/) | 2019 | Review | Frontiers in Medicine | Novel and future therapeutic drugs for advanced MF/Sézary syndrome |
| [39315857](https://pubmed.ncbi.nlm.nih.gov/39315857/) | 2025 | Post-hoc analysis (Phase 3) | J European Academy of Dermatology and Venereology | Post-hoc HRQL analysis of MAVORIC Phase 3 trial in MF/Sézary syndrome |
| [35993803](https://pubmed.ncbi.nlm.nih.gov/35993803/) | 2023 | Post-hoc analysis (Phase 3) | J European Academy of Dermatology and Venereology | Blood involvement impact on efficacy/time-to-response in MAVORIC (mogamulizumab vs. vorinostat) |
| [35678206](https://pubmed.ncbi.nlm.nih.gov/35678206/) | 2022 | Post-hoc analysis | J Comparative Effectiveness Research | Crossover-adjusted overall survival analysis of MAVORIC trial |
| [33618592](https://pubmed.ncbi.nlm.nih.gov/33618592/) | 2021 | Subgroup analysis (Phase 3) | Leukemia & Lymphoma | MAVORIC subgroup analysis in Black patients with MF/Sézary syndrome |
| [21455551](https://pubmed.ncbi.nlm.nih.gov/21455551/) | 2011 | Clinical study | J Drugs in Dermatology | Vorinostat + IFN-alpha + extracorporeal photopheresis combination in late-stage MF and Sézary syndrome |

## Cytotoxicity

Same class-level profile as above (HDAC inhibitor, targeted therapy). Note: PMID 38170178 (mechanistic study) reports that *S. aureus* infection can induce HDAC-inhibitor drug resistance in Sézary syndrome malignant T-cells — relevant for monitoring infection status during treatment.

## Conclusion and Next Steps (Sézary Syndrome)

**Decision: Proceed with Guardrails**

**Rationale:**
Vorinostat has completed Phase 3 RCT data (MAVORIC, n=372) directly in the Sézary syndrome/CTCL population as an active comparator, supported by regulatory documentation and multiple post-hoc/subgroup analyses. This meets the L1 evidence bar (≥1 completed Phase 3 RCT with disease-specific data), but vorinostat itself was the *inferior* arm in MAVORIC (vs. mogamulizumab), so guardrails on expected efficacy and sequencing after other therapies are warranted.

**To proceed, the following is needed:**
- Confirmed regulatory/label status (market_status currently shows "Not Marketed" — verify against authoritative source)
- Drug-drug interaction and contraindication data (currently data gaps)
- Positioning guidance relative to mogamulizumab and other approved CTCL therapies, given vorinostat's inferior PFS in the MAVORIC comparator arm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


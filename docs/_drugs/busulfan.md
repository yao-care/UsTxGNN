---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: From Chronic Myeloid Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is a bifunctional alkylating agent historically used as myeloablative conditioning prior to allogeneic hematopoietic stem cell transplantation (allo-HSCT) for hematologic malignancies, with its earliest approved indication being chronic myeloid leukemia (CML).
The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**,
with **50 clinical trials** and **20 publications** currently supporting this direction — confirming busulfan-based conditioning as an established cornerstone of curative therapy in MDS.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic myeloid leukemia / myeloablative conditioning for hematopoietic stem cell transplantation (no regulatory licenses on file in queried database) |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| US Market Status | Not marketed (0 licenses found in regulatory database) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved from the DrugBank query. Based on established clinical pharmacology, busulfan is a bifunctional sulfonyloxy-alkane alkylating agent that forms DNA interstrand cross-links by covalently alkylating the N7 position of guanine residues. This DNA damage preferentially destroys rapidly dividing hematopoietic progenitor cells, resulting in profound, intentional myeloablation — the very property that makes busulfan indispensable as a transplant conditioning agent.

Myelodysplastic syndrome (MDS) is a clonal hematopoietic stem cell disorder characterized by ineffective hematopoiesis, progressive cytopenias, and risk of transformation to acute myeloid leukemia. Allogeneic HSCT remains the only potentially curative treatment for eligible patients. Busulfan-based conditioning regimens — most commonly BuFlu (busulfan + fludarabine) and BuCy (busulfan + cyclophosphamide) — achieve two goals simultaneously: they eradicate the dysplastic clone from the host marrow and create engraftment space for healthy donor hematopoietic stem cells. The mechanistic logic is direct and compelling: eliminating the defective clone is a prerequisite for disease cure.

Multiple Phase 3 randomized controlled trials have established busulfan as the reference standard in this indication. The landmark MC-FludT.14/L trial (*Lancet Haematology*, 2020, n=476) used reduced-intensity busulfan as the comparator arm for older and comorbid AML/MDS patients. A 2023 Phase 3 trial (*Lancet Haematology*, n=202) demonstrated that adding G-CSF and decitabine to the BuCy backbone significantly reduced relapse in high-risk MDS. These trials do not simply include busulfan as a footnote — they position it as the established benchmark against which newer regimens must prove themselves, confirming busulfan's central role in the current MDS transplant standard of care.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | Completed | 202 | Prospective RCT comparing G-CSF+Decitabine+BuCy vs BuCy alone as conditioning for RAEB-1/RAEB-2 and AML secondary to MDS undergoing allo-HSCT; busulfan is the conditioning backbone in both arms |
| [NCT00469014](https://clinicaltrials.gov/study/NCT00469014) | Phase 2 | Completed | 72 | Randomized Phase II directly studying busulfan as primary conditioning component in combination with fludarabine and clofarabine for refractory AML, MDS, and CML; Grade A relevance |
| [NCT06829472](https://clinicaltrials.gov/study/NCT06829472) | Phase 3 | Recruiting | 120 | Phase III RCT comparing melphalan 100 vs 140 mg/m² with busulfan-fludarabine (MBF) conditioning for adult AML/MDS; seeks to optimize toxicity while preserving busulfan-based efficacy |
| [NCT05457556](https://clinicaltrials.gov/study/NCT05457556) | Phase 3 | Active, not recruiting | 435 | Multi-center Phase III trial of MUD vs haploidentical myeloablative HCT for children, adolescents, and young adults with acute leukemia or MDS; busulfan-based myeloablative conditioning used |
| [NCT06802315](https://clinicaltrials.gov/study/NCT06802315) | Phase 2 | Recruiting | 38 | Phase II evaluating intensity-modulated total marrow irradiation (IM-TMI 9 Gy) added to standard myeloablative FluBu4 (fludarabine + targeted busulfan) for high-risk AML, CML, and MDS |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | Unknown | 242 | Prospective comparison of G-CSF+DAC+BUCY vs G-CSF+DAC+BF conditioning for high-risk MDS undergoing allo-HSCT; large-scale evaluation of busulfan regimen optimization |
| [NCT05823714](https://clinicaltrials.gov/study/NCT05823714) | Phase 2 | Unknown | 70 | Venetoclax + azacitidine bridge followed by modified BUCY conditioning for high-risk MDS and relapsed/refractory AML undergoing allo-HSCT; combining novel agents with busulfan backbone |
| [NCT00346359](https://clinicaltrials.gov/study/NCT00346359) | Phase 2 | Completed | 40 | Fludarabine plus targeted IV busulfan as reduced-intensity conditioning with thymoglobulin/tacrolimus/methotrexate GVHD prophylaxis in myeloid malignancies including MDS |
| [NCT00445744](https://clinicaltrials.gov/study/NCT00445744) | N/A | Completed | 52 | Cyclophosphamide followed by IV busulfan as conditioning specifically for myelofibrosis, AML, or MDS undergoing HCT; direct MDS indication |
| [NCT00024050](https://clinicaltrials.gov/study/NCT00024050) | Phase 2 | Completed | N/A | Phase II trial of chemotherapy followed by peripheral blood stem cell transplantation specifically for "less advanced" myelodysplastic syndrome patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | Phase 3 RCT | *Lancet Haematology* | MC-FludT.14/L trial (n=476): treosulfan+fludarabine vs reduced-intensity busulfan+fludarabine for older/comorbid AML/MDS; establishes busulfan as the reference standard for allo-HSCT conditioning |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Phase 3 RCT (final analysis) | *American Journal of Hematology* | Final 476-patient analysis confirming treosulfan's non-inferiority to busulfan-based RIC for AML/MDS; validates busulfan as the long-standing benchmark conditioning regimen |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Phase 3 RCT | *Lancet Haematology* | Multicentre Phase 3 trial: G-CSF+decitabine+BuCy vs BuCy for MDS (RAEB) and secondary AML undergoing allo-HSCT; epigenetic augmentation of the busulfan backbone significantly reduced relapse |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | Phase 3 RCT | *Journal of Clinical Oncology* | Phase III RCT comparing myeloablative vs reduced-intensity conditioning for AML/MDS; busulfan regimens central to both arms, defining optimal conditioning intensity |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Systematic review | *American Journal of Hematology* | Contemporary review confirming allo-HCT as the only potentially curative therapy for MDS; busulfan-based conditioning (BuFlu, BuCy) embedded in current transplant decision algorithms |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Meta-analysis | *Frontiers in Oncology* | Systematic review and meta-analysis of treosulfan vs busulfan conditioning for MDS/AML before allo-HCT; confirms comparable long-term outcomes with busulfan as established comparator |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Propensity score-matched cohort | *Transplantation and Cellular Therapy* | Single-center retrospective comparison of treosulfan vs busulfan conditioning in 138 adults with MDS/CMML undergoing allo-HCT; direct evidence of busulfan conditioning outcomes in MDS |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Registry analysis | *Bone Marrow Transplantation* | Japanese nationwide registry propensity-matched analysis of Flu/Bu4 vs Bu4/Cy as myeloablative conditioning specifically for adult MDS patients |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Prospective cohort | *Transplantation and Cellular Therapy* | Myeloablative busulfan+fludarabine with in vivo T-cell depletion for AML/MDS; demonstrates safety and efficacy without strict upper age or comorbidity cutoffs |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Registry analysis | *Transplantation and Cellular Therapy* | Japanese nationwide registry comparing myeloablative (Flu/Bu4) vs reduced-intensity (Flu/Bu2) conditioning for MDS; guides busulfan dose-intensity decisions in transplant-eligible patients |

---

## Regulatory Market Information

No licenses for busulfan were identified in the queried regulatory database (market status: not marketed; 0 regulatory licenses on file).

> **Note for clinical context:** Busulfan is commercially available internationally as **Busulfex®** (intravenous busulfan, PDL BioPharma / Otsuka) and **Myleran®** (oral tablets, Aspen Pharmacare), both with regulatory approvals in major markets including the United States and European Union. The absence of records likely reflects the scope or indexing of the regulatory database queried rather than a true absence of marketed products.

---

## Cytotoxicity

Busulfan qualifies as an antineoplastic cytotoxic agent based on its established use in myeloablative conditioning for hematologic malignancies and its classification as a bifunctional alkylating agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent (bifunctional sulfonyloxy-alkane class) |
| Myelosuppression Risk | **High** — Profound, prolonged pancytopenia is the intended pharmacological endpoint; nadir typically occurs 10–20 days post-conditioning; full hematopoietic recovery depends on successful donor engraftment |
| Emetogenicity Classification | Low to moderate (IV formulation: low-moderate with standard antiemetic prophylaxis; oral formulation: moderate) |
| Monitoring Items | CBC with differential (daily during conditioning and engraftment phase), liver function tests (hepatic veno-occlusive disease/sinusoidal obstruction syndrome risk), renal function, plasma busulfan AUC levels (TDM mandatory for IV formulation; target AUC 900–1350 μmol·min/L per cycle), seizure prophylaxis monitoring (phenytoin or levetiracetam required during high-dose busulfan) |
| Handling Protection | Must follow cytotoxic drug handling regulations: closed-system drug transfer devices, appropriate PPE (gloves, gown, eye protection), dedicated pharmacy compounding area per institutional cytotoxic handling policy |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Busulfan-based conditioning is already the established standard of care for MDS patients undergoing allogeneic HSCT, confirmed by multiple completed Phase 3 randomized controlled trials and a large body of registry and prospective cohort data (Evidence Level L1, TxGNN score 99.62%). The TxGNN prediction accurately reflects this well-validated clinical role; the key gap is not evidence of efficacy but rather regulatory registration and formal clinical protocol documentation.

**To proceed, the following is needed:**
- **Regulatory registration**: Submit registration dossier with the relevant regulatory authority (TFDA or equivalent) using the existing international evidence base; no licenses were found in the queried database
- **Safety documentation**: Retrieve and parse the full prescribing information (Busulfex®/Myleran® package insert) to complete key warnings, contraindications, and drug interaction profiles — these data are available but were not captured in the current evidence pack
- **Mechanism of action documentation**: Obtain complete MOA data from DrugBank API for the pharmacological dossier
- **Therapeutic drug monitoring (TDM) protocol**: Establish busulfan plasma level monitoring protocol — AUC-guided dosing is considered mandatory for the IV formulation to balance myeloablative efficacy against hepatotoxicity (VOD/SOS) and neurotoxicity risk
- **Pediatric pharmacokinetics consideration**: For MDS in children (especially refractory cytopenia of childhood, TxGNN rank 2, L2 evidence), weight-adjusted dosing with more frequent TDM intervals is essential due to markedly different pharmacokinetic parameters compared to adults
- **GVHD prophylaxis and conditioning regimen selection protocol**: Define patient-level decision criteria for BuFlu vs BuCy backbone and associated GVHD prophylaxis strategy (post-transplant cyclophosphamide vs calcineurin inhibitor-based) based on age, comorbidity index, and donor type
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


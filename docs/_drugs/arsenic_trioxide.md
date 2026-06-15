---
layout: default
title: Arsenic Trioxide
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Arsenic Trioxide
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

# Arsenic Trioxide: From Acute Promyelocytic Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Arsenic Trioxide (ATO) is an established anticancer agent best known for its transformative role in acute promyelocytic leukemia (APL), where the ATRA+ATO combination has become the global standard of first-line therapy.
The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)** — placing MDS-related conditions at the top of its prediction ranking across multiple subtypes —
with **24 clinical trials** and **20 publications** currently supporting this direction, including a 2023 systematic review and meta-analysis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Promyelocytic Leukemia (APL) — established international standard with ATRA (no Taiwan FDA registration found in this dataset) |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed (0 registered licenses) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Arsenic Trioxide acts through multiple converging mechanisms relevant to clonal hematologic disorders. In APL, ATO's primary established mechanism is inducing selective degradation of the PML-RARα oncoprotein, triggering differentiation and apoptosis of leukemic blasts. Beyond this APL-specific effect, ATO exerts broader pro-apoptotic activity: it inhibits the NF-κB survival pathway in MDS CD34+ cells (PMID 16105982), downregulates anti-apoptotic BCL-2/BCL-XL while upregulating pro-apoptotic BAX (PMID 22964015), and generates reactive oxygen species (ROS) that disrupt mitochondrial integrity. These mechanisms are not restricted to APL and explain why ATO has been explored across a wider spectrum of hematologic malignancies.

The biological kinship between APL and MDS makes this prediction mechanistically coherent. Both arise from myeloid hematopoietic stem cell compartment dysfunction, characterized by aberrant clonal survival and impaired differentiation. In MDS specifically, ATO demonstrates a particularly attractive synergy with hypomethylating agents (HMAs): ATO promotes DNMT3A degradation and eliminates dysplastic clones, while Decitabine or Azacitidine concurrently re-activates silenced tumor suppressor genes — a mechanistically complementary combination that has shown enhanced cell killing in MDS cell lines (PMID 30898879). Additionally, ATO modulates the immunological imbalance in the bone marrow microenvironment by adjusting the Treg/Th17/Th1 ratio and suppressing inflammatory cytokines IFN-γ and IL-17 (PMID 38816179), addressing the immune dysregulation that drives ineffective hematopoiesis in MDS.

A 2023 systematic review and component network meta-analysis (PMID 37908176) — the highest currently available evidence tier — synthesized multiple Phase 2 trials and identified hematological response benefits and overall survival signals with ATO-containing regimens in MDS. Encouragingly, two oral ATO (Arsenol®) trials are actively recruiting as of 2025 (NCT06778187, NCT06670222), signaling sustained clinical investment and the potential for a more patient-friendly administration route. The primary remaining gap is the absence of a Phase 3 RCT dedicated to MDS; most MDS-specific Phase 2 trials were terminated early due to limited single-agent signals or resource constraints, reinforcing that combination strategies and careful patient selection are keys to further development.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00195104](https://clinicaltrials.gov/study/NCT00195104) | Phase 1/2 | Completed | 87 | ATO + low-dose cytarabine in high-risk MDS and poor-prognosis AML; largest directly relevant completed MDS trial; CR rate 17%, early mortality 8%; active and tolerable regimen |
| [NCT02190695](https://clinicaltrials.gov/study/NCT02190695) | Phase 2 | Completed | 92 | Randomized comparison of Decitabine alone vs Decitabine+Carboplatin vs Decitabine+ATO in relapsed/refractory AML and MDS; provides comparative efficacy data for the ATO+HMA strategy |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2000 | Treatment development programme for older patients with AML and high-risk MDS; largest safety dataset available, establishes real-world tolerability benchmarks for ATO in hematologic malignancies |
| [NCT06778187](https://clinicaltrials.gov/study/NCT06778187) | Phase 2 | Recruiting | 30 | Oral ATO (Arsenol®) + ascorbic acid for TP53-mutated MDS, AML, and CMML; most recent trial (started Feb 2025), represents clinical translation of oral formulation in a genomically defined subgroup |
| [NCT00671697](https://clinicaltrials.gov/study/NCT00671697) | Phase 1 | Completed | 13 | Decitabine + ATO + ascorbic acid triple combination in MDS and AML; completed, provides clinical validation of mechanistically synergistic triple regimen |
| [NCT00251511](https://clinicaltrials.gov/study/NCT00251511) | Phase 2 | Terminated | 60 | ATO + Thalidomide across all IPSS risk groups in MDS; terminated but 60 patients enrolled providing meaningful safety and preliminary efficacy information |
| [NCT00274781](https://clinicaltrials.gov/study/NCT00274781) | Phase 2 | Completed | 30 | ATO + Gemtuzumab Ozogamicin (Mylotarg) in advanced MDS; completed, explores antibody-drug conjugate combination in CD33+ dysplastic clones |
| [NCT06670222](https://clinicaltrials.gov/study/NCT06670222) | Phase 1 | Recruiting | 24 | Oral ATO dose-escalation in low-risk MDS failing ESA and Luspatercept; started Jul 2025, establishes safe dose range for oral formulation in lower-risk patients |
| [NCT00093366](https://clinicaltrials.gov/study/NCT00093366) | Phase 1/2 | Completed | 32 | ATO + Etanercept (TNF-α inhibitor) in advanced-stage MDS; completed, targets the inflammatory bone marrow microenvironment alongside cytotoxic ATO activity |
| [NCT00621023](https://clinicaltrials.gov/study/NCT00621023) | Phase 2 | Completed | 7 | Decitabine + ATO + ascorbic acid pilot study in MDS; completed, confirms feasibility and provides initial safety signal for the triple combination |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37908176](https://pubmed.ncbi.nlm.nih.gov/37908176/) | 2023 | Systematic Review & Meta-Analysis | Hematology | Network meta-analysis of ATO-containing regimens in MDS; demonstrates hematological response benefit and identifies optimal combinations, including ATO+HMA; highest current evidence tier |
| [40167011](https://pubmed.ncbi.nlm.nih.gov/40167011/) | 2025 | Retrospective Study | Hematology | Decitabine + ATO in elderly high-risk MDS patients; confirms clinical activity and manageable toxicity in a fragile, treatment-limited population |
| [38816179](https://pubmed.ncbi.nlm.nih.gov/38816179/) | 2024 | Comparative Study | Immunopharmacology & Immunotoxicology | Compares immunological changes between oral realgar (arsenic disulfide) and IV ATO in MDS mouse model; characterizes immune pathway modulation and supports route-of-delivery research |
| [20956016](https://pubmed.ncbi.nlm.nih.gov/20956016/) | 2011 | Phase I/II Clinical Study | Leukemia Research | ATO + low-dose cytarabine in 49 patients with intermediate-2/high-risk MDS; CR in 17%, active regimen with manageable toxicity profile |
| [18282365](https://pubmed.ncbi.nlm.nih.gov/18282365/) | 2007 | Clinical Data Review | Clinical Lymphoma & Myeloma | Multi-trial synthesis of ATO data in leukemias and MDS; documents response patterns and contextualizes MDS findings within the broader ATO clinical experience |
| [22964015](https://pubmed.ncbi.nlm.nih.gov/22964015/) | 2012 | Translational Clinical Study | J Hematol Oncol | Ex vivo analysis of 93 apoptosis-related genes in MDS patients before and after ATO treatment; identifies BCL-2 family downregulation as a key in vivo mechanism of action |
| [16105982](https://pubmed.ncbi.nlm.nih.gov/16105982/) | 2005 | In Vitro/Mechanistic | Blood | ATO inhibits NF-κB via FLIP downregulation in MDS CD34+ cells, selectively inducing apoptosis in high-grade MDS (RAEB) while sparing normal marrow; defines subtype-specific activity |
| [30898879](https://pubmed.ncbi.nlm.nih.gov/30898879/) | 2019 | In Vitro Mechanistic Study | J Investigative Medicine | ATO + Decitabine synergistically kill MDS cells (MUTZ-1, SKM-1) via ER stress-triggered apoptosis; provides mechanistic rationale for the HMA combination strategy |
| [17920679](https://pubmed.ncbi.nlm.nih.gov/17920679/) | 2008 | Clinical Study | Leukemia Research | ATO + all-trans retinoic acid + thalidomide in higher-risk MDS; evaluates a multi-agent differentiation-plus-immunomodulation approach in a clinical cohort |
| [31775455](https://pubmed.ncbi.nlm.nih.gov/31775455/) | 2019 | Retrospective Clinical Study | Zhonghua Nei Ke Za Zhi | Low-dose subcutaneous Decitabine + ATO in 11 intermediate/high-risk MDS patients; CR in 3 (27%), hematological improvement in 6 (55%); supports low-dose combination feasibility |

---

## US Market Information

No registered drug licenses for Arsenic Trioxide were found in the Taiwan FDA (TFDA) database queried for this report.

> **Note**: Arsenic Trioxide (brand name Trisenox®, Teva) is FDA-approved in the United States for APL since September 2000. The absence of Taiwan registrations in this dataset may reflect a lack of formal TFDA registration rather than a global non-approval status. Clinicians in Taiwan may access the drug through named-patient or compassionate use pathways.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (arsenic-based agent) — acts via ROS generation, mitochondrial pathway apoptosis, NF-κB inhibition, and targeted oncoprotein degradation (PML-RARα in APL) |
| Myelosuppression Risk | Moderate — leukocytosis and APL differentiation syndrome in APL setting; neutropenia, thrombocytopenia, and anemia reported in MDS/hematologic malignancy trials |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | QTc interval by ECG before and during each cycle (critical — QT prolongation risk), CBC with differential, serum electrolytes (potassium ≥4 mEq/L, magnesium ≥1.8 mg/dL mandatory), liver function tests (AST/ALT/bilirubin), serum creatinine |
| Handling Protection | Must follow cytotoxic drug handling regulations (NIOSH guidelines); appropriate PPE required during preparation and administration |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical known risks**: Arsenic Trioxide carries FDA black-box warnings for **QT interval prolongation** (risk of fatal arrhythmias, particularly torsades de pointes) and **APL differentiation syndrome** (potentially fatal pulmonary/vascular complication). Electrolyte correction and baseline ECG assessment are mandatory before initiating therapy. Co-administration with other QT-prolonging agents must be avoided or carefully managed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A 2023 systematic review and meta-analysis (PMID 37908176), multiple completed Phase 2 trials including randomized and multi-center designs (NCT02190695, N=92; NCT00195104, N=87), and two actively recruiting oral ATO trials in MDS (NCT06778187, NCT06670222 — both started in 2025) together constitute L2-level evidence supporting ATO's clinical activity in MDS. The mechanistic synergy with hypomethylating agents is documented at both the preclinical and clinical levels, and the emergence of oral ATO (Arsenol®) addresses historical barriers related to IV administration burden.

**To proceed, the following is needed:**
- A dedicated Phase 3 RCT comparing ATO+HMA (e.g., Decitabine or Azacitidine) versus HMA alone in MDS — this is the critical missing piece for regulatory-grade evidence
- Results from the two active oral ATO trials (NCT06778187, NCT06670222) before committing to an IV-only development strategy
- Patient selection biomarkers to identify MDS subtypes most likely to respond (e.g., TP53-mutated disease, high-risk IPSS-R category, HMA-refractory patients)
- Formal QT monitoring protocol and mandatory electrolyte management plan embedded in any MDS trial design
- Mechanism of action (MOA) documentation from DrugBank or literature review to complete the pharmacological profile for regulatory submissions
- TFDA registration pathway assessment, given zero existing Taiwan licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


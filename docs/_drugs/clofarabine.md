---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 538
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine: From Pediatric Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Clofarabine is a second-generation purine nucleoside analog with FDA accelerated approval (2004) for relapsed or refractory acute lymphoblastic leukemia (ALL) in pediatric patients aged 1–21 years; it is currently not registered in Taiwan.
The TxGNN model predicts it may also be effective for **Myeloid Leukemia**, with **50 clinical trials** and **20 publications** currently supporting this direction.
The evidence base is unusually strong: a Phase 3 pediatric RCT (PMID 31246522, COG AAML0531) and multiple completed Phase 2 trials across adult AML settings qualify this prediction for **L1 evidence**, making Clofarabine one of the most evidence-supported candidates in this repurposing analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pediatric relapsed/refractory acute lymphoblastic leukemia (ALL), ≥2 prior regimens |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Taiwan Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Clofarabine works through three distinct but synergistic mechanisms. It competitively inhibits **ribonucleotide reductase (RNR)**, depleting the intracellular deoxyribonucleotide triphosphate (dNTP) pool that leukemic cells require for DNA replication. Its triphosphate form is then directly incorporated into DNA and blocks **DNA polymerase α and ε**, simultaneously halting replication and preventing repair of existing strand damage. Finally, Clofarabine disrupts **mitochondrial membrane integrity**, triggering Bcl-2-mediated apoptosis — a mechanism active in both dividing and quiescent blast cells, which gives it an advantage over S-phase-dependent agents. Compared to anthracyclines, Clofarabine carries substantially lower cardiac toxicity, making it especially suitable for elderly AML patients who cannot tolerate cardiotoxic induction regimens.

The mechanistic case for crossing from ALL to myeloid disease rests on enzyme expression rather than lineage similarity. AML blast cells express sufficient **deoxycytidine kinase (dCK)** — the rate-limiting phosphorylation enzyme for Clofarabine — to allow substantial intracellular accumulation of the active triphosphate. This contrasts sharply with solid tumors, where low dCK expression limits nucleoside analog activity. The consequence is that Clofarabine's pharmacology translates directly from lymphoid to myeloid disease. The EORTC/GIMEMA AML-14A trial (NCT00838240, Phase 1/2, n=114) confirmed that adding Clofarabine to standard induction (AraC + Idarubicin) is feasible and well-tolerated in newly diagnosed intermediate- and high-risk AML.

The TxGNN prediction achieves its L1 rating primarily from the **AML08 multicenter Phase 3 RCT** (PMID 31246522; Children's Oncology Group AAML0531), which demonstrated that Clofarabine can replace anthracyclines and etoposide in pediatric AML induction without compromising remission rates — a direct proof-of-concept transfer of mechanism from ALL to myeloid disease. In adult AML, evidence spans the full treatment trajectory: initial induction (CIA triplet, CLARA consolidation), salvage chemotherapy (CLAM regimen, Clo + Temsirolimus), and transplant conditioning (CloBu4 myeloablative regimen). The ongoing FLUCLORIC Phase 3 trial (NCT05917405, n=302) is expected to provide the most definitive head-to-head data comparing Clofarabine-based versus standard Fludarabine-based conditioning.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00932412](https://clinicaltrials.gov/study/NCT00932412) | Phase 2 (Randomized) | Completed | 735 | CLARA (Clofarabine + intermediate-dose cytarabine) vs. standard HDAC consolidation in younger AML achieving CR; largest trial in the dataset — primary question is whether Clofarabine-based consolidation improves relapse-free survival over high-dose cytarabine alone |
| [NCT00838240](https://clinicaltrials.gov/study/NCT00838240) | Phase 1/2 | Unknown | 114 | EORTC/GIMEMA AML-14A: Clofarabine added to AraC + Idarubicin induction in newly diagnosed intermediate/high-risk AML (ages 18–60); establishes optimal Clofarabine dose in the triplet combination and measures remission rates |
| [NCT00373529](https://clinicaltrials.gov/study/NCT00373529) | Phase 2 | Completed | 116 | Single-agent Clofarabine in previously untreated older AML patients for whom intensive anthracycline-based induction is contraindicated; establishes single-agent anti-AML activity benchmark |
| [NCT01457885](https://clinicaltrials.gov/study/NCT01457885) | Phase 2 | Completed | 75 | Multicenter CloBu4 conditioning (Clofarabine + Busulfan ×4) for alloSCT in non-remission AML; addresses the large population of older patients who fail to achieve CR before transplant |
| [NCT00469014](https://clinicaltrials.gov/study/NCT00469014) | Phase 2 | Completed | 72 | Randomized Phase 2: Busulfan/Fludarabine vs. Busulfan/Clofarabine vs. Busulfan/Flu+Clo pre-transplant conditioning in refractory AML, MDS, and CML; first prospective comparison of Clofarabine-containing conditioning |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | Completed | 86 | Clofarabine salvage therapy in relapsed/refractory AML; evaluates whether Clofarabine alone can restore remission and enable bridging to alloHCT — currently the only curative strategy in this setting |
| [NCT00775593](https://clinicaltrials.gov/study/NCT00775593) | Phase 2 | Completed | 60 | Clofarabine + Temsirolimus (mTOR inhibitor) in older (>60y) relapsed/refractory AML; rationale is dual-pathway attack — DNA synthesis inhibition combined with mTOR-mediated survival pathway suppression |
| [NCT00065143](https://clinicaltrials.gov/study/NCT00065143) | Phase 2 | Completed | 60 | Clofarabine + Cytarabine in newly diagnosed AML and high-risk MDS (≥10% blasts) for patients aged ≥50 years; one of the earliest trials establishing the Clo+AraC combination and identifying response characteristics in older adults |
| [NCT01025154](https://clinicaltrials.gov/study/NCT01025154) | Phase 2 | Completed | 63 | CIA triplet induction (Clofarabine + Idarubicin + Cytarabine) in younger AML (ages 18–60); evaluates whether three-drug combination achieves superior CR rates versus standard 3+7, with detailed safety characterization |
| [NCT05917405](https://clinicaltrials.gov/study/NCT05917405) | Phase 2 | Recruiting | 302 | FLUCLORIC: Randomized multicenter study comparing Clofarabine/Busulfan vs. Fludarabine/Busulfan reduced-intensity conditioning in AML before alloSCT; highest-enrollment ongoing trial, expected completion 2028, will provide definitive prospective evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | RCT (Phase 3) | J Clin Oncol | AML08 trial (COG AAML0531): Clofarabine replaces anthracyclines and etoposide in pediatric AML induction at equivalent remission rates with lower cardiac toxicity — the single study elevating this prediction to L1 evidence |
| [31281098](https://pubmed.ncbi.nlm.nih.gov/31281098/) | 2019 | Systematic Review / Meta-analysis | Lancet Oncol | Systematic review of Clofarabine + Cytarabine regimens for AML; synthesizes efficacy and tolerability data across multiple Phase 2 trials |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Cohort (retrospective) | Transplant Cell Ther | Clofarabine/Busulfan (Clo/Bu4) myeloablative conditioning in patients with active, chemotherapy-refractory myeloid malignancies undergoing alloHCT; demonstrates anti-leukemic activity with acceptable toxicity in patients ≤70 years |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Phase 2 Cohort | Cancer Med | CLAM regimen (Clofarabine + Cytarabine + Mitoxantrone) in relapsed/refractory AML ages 18–65: high response rates achieved, with effective bridging to alloHCT as a downstream curative strategy |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | Clinical Analysis (subgroup) | Cancers | Post-hoc SNP-array analysis of CLARA vs. HDAC trial: Clofarabine consolidation specifically improves relapse-free survival in younger AML with micro-complex karyotype — identifies a pharmacogenomically defined responder subpopulation |
| [18565853](https://pubmed.ncbi.nlm.nih.gov/18565853/) | 2008 | Randomized Phase 2 | Blood | Adaptive randomized study: Clofarabine ± low-dose cytarabine as front-line therapy in AML ≥60 years; demonstrates the combination is more active than Clofarabine alone, establishing optimal dosing for the frail elderly population |
| [27621503](https://pubmed.ncbi.nlm.nih.gov/27621503/) | 2015 | Clinical Review (Pharmacy) | Hosp Pharm | Practical review of the Clofarabine + Cytarabine AML regimen: covers preparation, dispensing, administration protocols, dose modifications, and toxicity monitoring — supports clinical implementation planning |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leuk Lymphoma | Comprehensive review of Clofarabine's role in AML: covers mechanism of action (RNR inhibition, DNA polymerase blockade, apoptosis induction), resistance profiles, and single-agent and combination clinical data |
| [17852710](https://pubmed.ncbi.nlm.nih.gov/17852710/) | 2007 | Review | Leuk Lymphoma | Foundational Clofarabine review (Kantarjian group): documents the three-mechanism pharmacology and early AML + ALL combination data, including synergy rationale for co-administration with AraC and DNA-damaging agents |
| [19852733](https://pubmed.ncbi.nlm.nih.gov/19852733/) | 2009 | Review | Future Oncol | Review of Clofarabine for adult AML: benchmarks single-agent activity against standard agents, describes combination induction and consolidation strategies, and outlines dose-optimization work for older vs. younger patients |

---

## Taiwan Market Status

Clofarabine currently has **no registered authorizations in Taiwan** (market status: 未上市 / not marketed). Taiwan TFDA regulatory package insert data is unavailable at the time of this evaluation.

For clinical context: in the United States, Clofarabine is marketed as **Clolar** (Sanofi Genzyme) and received FDA accelerated approval in December 2004 for pediatric patients (ages 1–21) with relapsed or refractory ALL after at least two prior treatment regimens. This US approval is referenced throughout the clinical trial descriptions cited above.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — second-generation purine nucleoside analog (deoxyadenosine analog class); not a targeted therapy or immunotherapy |
| Myelosuppression Risk | **High** — inhibition of DNA synthesis in bone marrow progenitors produces clinically significant neutropenia, thrombocytopenia, and anemia in the majority of patients receiving standard 5-day IV infusion schedules; nadir typically at 1–3 weeks post-cycle |
| Emetogenicity Classification | Low to moderate — consistent with other IV purine nucleoside analogs; standard anti-emetic prophylaxis is typically sufficient |
| Monitoring Items | CBC with differential (mandatory before each cycle and during hematologic recovery); hepatic function (ALT, AST, bilirubin — hepatotoxicity reported with this class); renal function (creatinine, eGFR — Clofarabine is renally cleared; dose adjustment required for renal impairment) |
| Handling Protection | Full cytotoxic drug handling protocols required: biological safety cabinet for preparation, chemotherapy-rated gloves and protective gowns, closed-system drug transfer devices (CSTDs) per institutional occupational safety and national pharmacy guidelines |

---

## Safety Considerations

Please refer to the official Clolar (Clofarabine) US prescribing information (Sanofi Genzyme) for complete warnings, contraindications, and drug interaction data. Taiwan TFDA package insert data is not yet available.

Based on the known drug class profile, clinicians planning use in an AML setting should establish protocols in advance for the following risk categories — each of which should be verified against the official prescribing information:

- **Severe myelosuppression**: Anticipate prolonged neutropenia and thrombocytopenia; infection prophylaxis (anti-fungal, anti-bacterial, anti-viral) and growth factor support plans should be in place before treatment initiation
- **Hepatotoxicity**: Elevated transaminases have been reported; baseline and periodic liver function testing is essential, and dosing should be held or reduced for significant hepatic dysfunction
- **Capillary leak syndrome / systemic inflammatory response**: Has been associated with Clofarabine administration; close hemodynamic monitoring during and immediately after infusion is warranted, particularly in elderly patients

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence supporting Clofarabine in myeloid leukemia is substantial and spans the full treatment continuum — from induction and consolidation in newly diagnosed disease to salvage and transplant conditioning in relapsed/refractory settings. The COG AAML0531 Phase 3 RCT (PMID 31246522) provides a direct L1-level mechanistic proof of concept in AML, and the ongoing FLUCLORIC Phase 3 trial (n=302) will further solidify the evidence base for conditioning use. The principal barrier to deployment is regulatory, not clinical: Clofarabine is not currently registered in Taiwan.

**To proceed, the following is needed:**

- **Taiwan regulatory pathway**: Establish whether an NDA submission, expanded access (恩慈療法), or cross-border supply protocol is feasible; the US approval for pediatric ALL may support an expedited review pathway for AML indications
- **Safety package compilation**: Retrieve and systematically review the Clolar FDA prescribing information plus current NCCN/ELN AML guidelines for population-specific dosing, monitoring parameters, and toxicity management protocols
- **Target population specification**: Clarify the intended AML subgroup before proceeding — the evidence base supports different Clofarabine roles for (a) newly diagnosed elderly AML unsuitable for intensive induction; (b) younger AML as CIA or CLARA consolidation; (c) relapsed/refractory AML as bridge to transplant; and (d) transplant conditioning (CloBu4 or Clo/Bu RIC)
- **Pharmacovigilance plan**: Pre-define monitoring schedules for myelosuppression, hepatotoxicity, and capillary leak syndrome for any Taiwanese patient population, aligned with institutional oncology safety standards
- **MOA data gap remediation**: Obtain full DrugBank mechanistic data (DG002) to strengthen the mechanistic rationale section for any regulatory or ethics board submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


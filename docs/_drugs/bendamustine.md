---
layout: default
title: Bendamustine
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Bendamustine
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

# Bendamustine: From Chronic Lymphocytic Leukemia / Indolent B-Cell NHL to Mantle Cell Lymphoma

## One-Sentence Summary

Bendamustine is a bifunctional alkylating agent with a unique dual mechanism — inducing DNA alkylating cross-links while also bearing a benzimidazole ring that confers partial antimetabolite properties — and has been established clinically for chronic lymphocytic leukemia (CLL) and rituximab-refractory indolent B-cell non-Hodgkin lymphoma (NHL).
The TxGNN model predicts it may be highly effective for **Mantle Cell Lymphoma (MCL)**,
with **multiple completed and ongoing Phase 3 clinical trials** and **20 publications** currently supporting this direction — evidence level **L1**, the highest tier available.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic lymphocytic leukemia; Rituximab-refractory indolent B-cell non-Hodgkin lymphoma (based on clinical literature; no US NDA records found in database) |
| Predicted New Indication | Mantle Cell Lymphoma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 (multiple completed Phase 3 RCTs) |
| US Market Status | Not found in database (0 records retrieved; potential data collection gap) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal MOA data is not populated in this Evidence Pack. However, multiple publications within the evidence pack itself provide mechanistic context. Bendamustine is a **bifunctional alkylating agent** structurally unique among its class: the nitrogen mustard moiety generates DNA interstrand cross-links and double-strand breaks, while the benzimidazole ring mimics purine nucleosides and interferes with DNA synthesis — a partial antimetabolite effect. This dual mechanism produces only partial cross-resistance with conventional alkylating agents such as cyclophosphamide or cisplatin, explaining activity in tumors refractory to standard chemotherapy (PMID 11368287, 25829094).

MCL is a biologically aggressive mature B-cell lymphoma driven by t(11;14)-mediated cyclin D1 overexpression, constitutive BCR signaling, and — especially in high-risk variants — defects in the ATM/TP53 DNA damage response pathway. Cells with impaired DNA repair are precisely the most vulnerable to agents inducing double-strand breaks. The repurposing rationale in this evidence pack states explicitly: *"MCL is highly dependent on BCR signaling and DNA repair defects, conferring high sensitivity to alkylating agents."* Bendamustine's purine analog scaffold may additionally bypass resistance mechanisms that limit classical alkylators in these cells.

Importantly, this TxGNN prediction does not represent a speculative future use — it identifies a direction that is already well-established in clinical practice. The Phase 3 StiL trial (Rummel 2013, Lancet) and the SHINE trial (Wang 2022, NEJM) have firmly positioned BR (bendamustine + rituximab) as a standard first-line chemotherapy backbone for MCL. Current EHA guidelines (2025, HemaSphere) endorse BR for transplant-ineligible patients, and multiple ongoing Phase 3 trials continue to use BR as the control arm against which novel agents are tested. The TxGNN model correctly capturing this as a top-ranked indication validates the algorithm's ability to reflect real-world clinical consensus.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01776840](https://clinicaltrials.gov/study/NCT01776840) | Phase 3 | Completed | 523 | SHINE trial: Ibrutinib + BR vs placebo + BR in untreated MCL (≥65 years). Pivotal double-blind RCT establishing BR as the standard chemotherapy backbone for older MCL patients; IBR significantly prolonged PFS |
| [NCT00991211](https://clinicaltrials.gov/study/NCT00991211) | Phase 3 | Completed | 549 | StiL trial: BR vs R-CHOP as first-line therapy for indolent NHL and MCL. Demonstrated BR is non-inferior to R-CHOP in PFS with improved tolerability; landmark trial defining BR standard of care |
| [NCT02972840](https://clinicaltrials.gov/study/NCT02972840) | Phase 3 | Active, Not Recruiting | 635 | Acalabrutinib + BR vs placebo + BR in previously untreated MCL. Double-blind Phase 3 RCT; confirms BR as active control and evaluates next-generation BTKi combination |
| [NCT06363994](https://clinicaltrials.gov/study/NCT06363994) | Phase 3 | Recruiting | 476 | Orelabrutinib + BR vs BR in treatment-naïve MCL. Double-blind Phase 3 RCT; BR serves as randomized control arm, further cementing its standard role |
| [NCT06084936](https://clinicaltrials.gov/study/NCT06084936) | Phase 3 | Recruiting | 182 | Glofitamab monotherapy vs investigator's choice (BR or R-Lenalidomide) in R/R MCL. BR is designated standard-of-care comparator arm for relapsed/refractory setting |
| [NCT06496308](https://clinicaltrials.gov/study/NCT06496308) | Phase 3 | Recruiting | 78 | Orelabrutinib + BR vs BR in transplant-ineligible intermediate/high-risk MCL. Directly compares BR ± BTK inhibitor in a defined high-risk subpopulation |
| [NCT00992134](https://clinicaltrials.gov/study/NCT00992134) | Phase 2 | Completed | 41 | R-BAC (Rituximab + Bendamustine + Cytarabine) in MCL patients ≥65 years or ineligible for intensive therapy. Directly demonstrates bendamustine-containing regimen efficacy and safety in this population |
| [NCT01662050](https://clinicaltrials.gov/study/NCT01662050) | Phase 2 | Completed | 57 | Age-adjusted R-BAC induction in older MCL patients. Evaluates tolerability-optimized bendamustine dosing; supports dose individualization in elderly patients |
| [NCT06136351](https://clinicaltrials.gov/study/NCT06136351) | Phase 2 | Recruiting | 23 | Zanubrutinib + BR in elderly or TP53-mutated newly diagnosed MCL. Addresses the high-risk subgroup where cytotoxic backbone remains essential |
| [NCT04127916](https://clinicaltrials.gov/study/NCT04127916) | N/A (Retrospective) | Unknown | 40 | Korean multicenter retrospective analysis of BR in R/R MCL. Real-world efficacy and safety data from Asian clinical practice |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | Phase 3 RCT | New England Journal of Medicine | SHINE trial: Ibrutinib + BR prolonged median PFS (80.6 vs 52.9 months) vs BR alone in older untreated MCL; confirms BR as the foundational backbone against which all novel agents are measured |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | Phase 3 RCT | Journal of Clinical Oncology | Acalabrutinib + BR in untreated MCL; next-generation BTKi + BR demonstrates favorable efficacy-toxicity profile compared to ibrutinib-based combination |
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | Phase 3 RCT | Lancet | StiL trial: BR non-inferior to R-CHOP in first-line MCL and indolent lymphoma, with significantly lower rates of alopecia, infections, and peripheral neuropathy; landmark trial that redefined MCL first-line therapy |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | Phase 3 / Prospective Cohort | Journal of Clinical Oncology | BRIGHT 5-year follow-up: BR maintains durable remission vs R-CHOP/R-CVP in treatment-naïve indolent NHL and MCL; confirms long-term efficacy of BR backbone |
| [41132246](https://pubmed.ncbi.nlm.nih.gov/41132246/) | 2025 | Clinical Guideline | HemaSphere | EHA-EU MCL network guidelines: BR endorsed as standard first-line chemoimmunotherapy for transplant-ineligible patients; current consensus document from European experts |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | Phase 2/3 RCT | Lancet | ENRICH trial: Ibrutinib-rituximab (chemotherapy-free) vs immunochemotherapy (R-CHOP or BR) in older untreated MCL; BR remains one of two standard comparator regimens |
| [36919283](https://pubmed.ncbi.nlm.nih.gov/36919283/) | 2023 | Network Meta-analysis | European Journal of Haematology | Network meta-analysis of 3 RCTs (n=1,459): Ibrutinib + BR ranked superior to BR alone in PFS for transplant-ineligible untreated MCL; quantifies incremental benefit of BTKi addition over BR |
| [36456154](https://pubmed.ncbi.nlm.nih.gov/36456154/) | 2022 | Retrospective Cohort | Anticancer Research | Korean multicenter retrospective: BR demonstrates high efficacy in both treatment-naïve and R/R MCL in real-world Asian clinical practice; confirms generalizability beyond trial populations |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Retrospective Cohort | Blood Advances | Pooled analysis of two Phase 2 trials: alternating RB + RC (rituximab/bendamustine + rituximab/high-dose cytarabine) followed by ASCT in transplant-eligible MCL; bendamustine induction is effective pre-transplant bridge |
| [26755518](https://pubmed.ncbi.nlm.nih.gov/26755518/) | 2016 | Review | Journal of Clinical Oncology | Comprehensive MCL disease review: identifies bendamustine maintenance rituximab and BR combination as key advances improving outcomes in older patients over the prior decade |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Bifunctional alkylating agent (nitrogen mustard derivative with benzimidazole ring; exhibits partial antimetabolite activity through purine analog structural mimicry) |
| Myelosuppression Risk | **High** — Neutropenia, thrombocytopenia, and profound lymphopenia are well-documented; prolonged T-cell depletion (CD4+ and CD8+) persists for months after treatment, substantially increasing risk of opportunistic infections including Pneumocystis jirovecii pneumonia and viral reactivation (HSV, VZV, CMV) |
| Emetogenicity Classification | Low to moderate (MASCC/ESMO classification: minimal to low emetogenic potential; oral 5-HT₃ antagonist prophylaxis generally sufficient) |
| Monitoring Items | CBC with differential (before each cycle and as clinically indicated); hepatic function (AST, ALT, bilirubin); renal function (serum creatinine); signs and symptoms of infection; CD4+ lymphocyte count in high-risk patients for opportunistic infection prophylaxis guidance |
| Handling Protection | Cytotoxic drug handling regulations apply in all settings; preparation must be performed in a biological safety cabinet (Class II or higher); closed-system drug transfer devices (CSTDs) are strongly recommended; personnel must wear appropriate PPE per institutional cytotoxic handling policy |

---

## Safety Considerations

Please refer to the package insert for safety information.

> No key warnings, contraindications, or drug interaction data were retrieved in this Evidence Pack. The safety data fields for TFDA package insert content and DDI records returned no results. Full safety review requires downloading and parsing the originator product label (Treanda®/Bendeka®) from the US FDA website.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (including the landmark StiL trial and SHINE trial) directly establish BR as a standard-of-care backbone for MCL, endorsed by current EHA guidelines (2025). The mechanistic link is sound — MCL's DNA repair deficiency renders it highly sensitive to the double-strand break-inducing activity of bendamustine — and the TxGNN prediction at 99.63% is fully consistent with established clinical consensus. Evidence quality reaches the highest tier (L1).

**To proceed, the following is needed:**
- **US FDA NDA verification**: Database returned 0 records for bendamustine, which is inconsistent with known Treanda® (NDA 022249) and Bendeka® (NDA 207491) approvals; data pipeline for US regulatory records requires investigation and correction
- **Formal MOA documentation**: DrugBank API query should be re-run to populate the `original_moa` field and complete the mechanistic analysis section
- **Package insert safety review**: Obtain and parse the FDA-approved labeling for bendamustine (Treanda/Bendeka) to populate key warnings, contraindications, black box warnings (myelosuppression, infection, secondary malignancies, embryo-fetal toxicity), and drug interaction data
- **Opportunistic infection prophylaxis protocol**: Given profound T-cell lymphopenia, a monitoring and prophylaxis plan (PCP prophylaxis, antiviral prophylaxis, CMV monitoring) should be established before clinical deployment
- **Taiwan regulatory pathway assessment**: Bendamustine is not registered in Taiwan (未上市); if deployment in Taiwan is planned, a regulatory strategy for local approval or special access program is required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


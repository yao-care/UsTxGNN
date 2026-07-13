---
layout: default
title: Teriflunomide
parent: 僅模型預測 (L5)
nav_order: 633
evidence_level: L5
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Teriflunomide: From No Registered Indication to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Teriflunomide (Aubagio®) is an oral immunomodulator — the active metabolite of leflunomide — that selectively inhibits lymphocyte proliferation via mitochondrial DHODH enzyme blockade, and currently holds no registered local indication in this market.

The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis (RRMS)**, with **28 clinical trials** and **19 publications** currently supporting this direction — including multiple completed Phase 3 pivotal trials that establish it as a benchmark comparator for emerging MS therapies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No locally registered indication |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis (RRMS) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| Market Status | Not Marketed (0 registered licenses) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Teriflunomide is the active metabolite of leflunomide, exerting its therapeutic effect by selectively and reversibly inhibiting **dihydroorotate dehydrogenase (DHODH)**, a mitochondrial enzyme essential for the *de novo* synthesis of pyrimidines. Because rapidly proliferating lymphocytes — unlike most resting cells — depend heavily on this biosynthetic pathway, teriflunomide preferentially suppresses the expansion of autoreactive T and B cells without broad immunosuppression. In the context of RRMS, this mechanism directly addresses the pathological cycle of immune-mediated demyelination and inflammatory lesion formation in the central nervous system.

The biological rationale connecting teriflunomide to RRMS is not speculative but mechanistically established. RRMS is driven by episodic activation and clonal expansion of myelin-reactive lymphocytes that breach the blood–brain barrier and trigger focal inflammatory attacks. By depleting the pyrimidine pool selectively in dividing cells, teriflunomide attenuates this cascade at the source — reducing relapse frequency, suppressing new MRI lesion formation, and slowing disability accumulation, as demonstrated in multiple Phase 3 trials.

Although the evidence pack records the local MOA field as unavailable, the DHODH-inhibition mechanism is comprehensively established in the international literature. Multiple pivotal trials (including NCT00134563 with n = 1,088) confirm approximately 31–36% relapse rate reduction versus placebo, and the drug now serves as the standard active comparator in Phase 3 trials for next-generation MS therapies including ofatumumab, ublituximab, ponesimod, evobrutinib, and tolebrutinib. The TxGNN model score of 99.24% reflects this robust mechanistic-epidemiological alignment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|------------|--------------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1,088 | Pivotal RCT evaluating teriflunomide (7 mg and 14 mg) vs. placebo in relapsing MS. Primary endpoint: annualized relapse rate. Secondary: EDSS disability progression, MRI lesion burden, patient-reported fatigue. Represents core L1 registration evidence (~31–36% relapse reduction). |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | Randomized rater-blinded multicenter study comparing two doses of teriflunomide vs. interferon beta-1a on time to treatment failure in relapsing MS, with long-term extension. Assessed relapse frequency, fatigue, and patient satisfaction. |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | Long-term extension of the multinational Phase 3 EFC6049 trial. Primary objective: document long-term safety and tolerability of teriflunomide 7 mg and 14 mg. Secondary: long-term disability progression, relapse rate, and MRI parameters. |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Phase 3 | Completed | 185 | Open-label rater-blinded randomized study comparing ofatumumab 20 mg SC monthly vs. physician's choice first-line DMT (including teriflunomide) in newly diagnosed relapsing MS patients. |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Long-term extension of Phase 2 safety and efficacy study (HMR1726D/2001). Evaluated long-term safety and tolerability of teriflunomide in relapsing MS over more than a decade. |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completed | 106 | Investigator-initiated real-world effectiveness study of teriflunomide in RRMS patients treated in regular clinical practice over at least two years at a dedicated MS clinic. |
| [NCT04129736](https://clinicaltrials.gov/study/NCT04129736) | Phase 4 | Completed | 12 | Pharmacokinetic study measuring teriflunomide concentrations in serum and cerebrospinal fluid from RRMS patients on 14 mg daily dosing, informing CNS penetration and exposure-response relationships. |
| [NCT01881191](https://clinicaltrials.gov/study/NCT01881191) | N/A | Completed | 50 | Prospective single-blinded longitudinal MRI study evaluating the effect of teriflunomide (Aubagio®) on gray matter pathology over 12 months, providing imaging biomarker evidence for neuroprotective potential. |
| [NCT03561402](https://clinicaltrials.gov/study/NCT03561402) | N/A | Completed | 24 | Two-year prospective observational study assessing putative biomarkers for disease activity prediction in RRMS patients receiving teriflunomide, informing pharmacodynamic monitoring strategies. |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | Enrolling by Invitation | 323 | STATURE: Prospective multi-site study measuring treatment burden and adherence across six oral DMTs including teriflunomide, dimethyl fumarate, fingolimod, cladribine, ozanimod, and diroximel fumarate. Provides real-world comparative adherence data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network Meta-Analysis | Cochrane Database of Systematic Reviews | Updated Cochrane NMA comparing immunomodulators and immunosuppressants for RRMS. Synthesizes relative efficacy of teriflunomide vs. all available DMTs on relapse frequency and disability accumulation. |
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT (Phase 3 Head-to-Head) | New England Journal of Medicine | ASCLEPIOS I & II: Ofatumumab vs. teriflunomide in relapsing MS (n > 1,800). Ofatumumab demonstrated superior MRI and clinical outcomes; teriflunomide arm establishes benchmark comparator efficacy. |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT (Phase 3 Head-to-Head) | New England Journal of Medicine | Tolebrutinib (oral BTK inhibitor) vs. teriflunomide in relapsing MS. Demonstrates teriflunomide's continued role as active comparator in next-generation Phase 3 trial design. |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT (Phase 3 Head-to-Head) | New England Journal of Medicine | Ublituximab vs. teriflunomide in relapsing MS. Ublituximab (enhanced B-cell depletion) showed superior MRI outcomes; confirms teriflunomide's established efficacy as standard comparator. |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT (Phase 3 Head-to-Head) | The Lancet Neurology | evolutionRMS1 and evolutionRMS2: Evobrutinib vs. teriflunomide across two Phase 3 trials. Teriflunomide arm provides contemporary real-world comparator data across multinational sites. |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT (Phase 3 Head-to-Head) | JAMA Neurology | OPTIMUM trial: Ponesimod vs. teriflunomide — first Phase 3 study comparing two oral DMTs for relapsing MS. Ponesimod showed superiority on ARR; teriflunomide arm performance characterizes real-world standard-of-care. |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | Comprehensive review of MS diagnosis and treatment for 900,000 affected US patients. Summarizes current evidence base including teriflunomide's role as oral first-line DMT. |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Systematic Review / Drug Review | Drugs | Dedicated teriflunomide review: mechanism (DHODH inhibition → de novo pyrimidine synthesis blockade → selective lymphocyte antiproliferation), RCT evidence synthesis, and real-world safety profile. |
| [37691530](https://pubmed.ncbi.nlm.nih.gov/37691530/) | 2023 | Long-term Extension Study | Multiple Sclerosis | ALITHIOS extension: ofatumumab demonstrated superior efficacy and favorable safety vs. teriflunomide over 4 years in relapsing MS. Provides 4-year longitudinal teriflunomide comparator data. |
| [31898276](https://pubmed.ncbi.nlm.nih.gov/31898276/) | 2020 | Systematic Review | CNS Drugs | Narrative review comparing five oral DMTs for RRMS — fingolimod, dimethyl fumarate, teriflunomide, cladribine, and siponimod — on relative efficacy and safety. Contextualizes teriflunomide's positioning in the oral therapy landscape. |

---

## Market Information

No licenses are currently registered in the local regulatory database for teriflunomide. The drug is marketed internationally as **Aubagio®** (Sanofi) and holds regulatory approval for relapsing forms of multiple sclerosis from both the US FDA (approved 2012) and the European Medicines Agency, as evidenced by its consistent role as the active comparator across more than five global Phase 3 trials conducted between 2020 and 2025. A formal local registration application would be required before clinical availability.

---

## Safety Considerations

Local safety data (package insert warnings, contraindications, and drug interaction database) are not available in the current evidence pack.

Please refer to the internationally approved package insert (Aubagio® US Prescribing Information / EMA SmPC) for full safety information, which includes hepatotoxicity monitoring requirements, teratogenicity risk with mandatory accelerated elimination protocol, and lymphopenia management guidance.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Teriflunomide's efficacy in RRMS represents one of the most thoroughly validated drug-indication pairs in modern neurology: multiple completed Phase 3 RCTs (including a 1,088-patient pivotal trial), a Cochrane NMA, and consistent use as an active comparator across five additional Phase 3 trials published between 2020 and 2025 collectively establish L1 evidence with no meaningful scientific uncertainty about biological plausibility. The TxGNN model score of 99.24% correctly reflects this convergence. The primary barrier to deployment is regulatory and logistical rather than scientific.

**To proceed, the following is needed:**

- **Regulatory filing**: Submit a New Drug Application (or equivalent local regulatory pathway) with the pivotal trial package (NCT00134563 and NCT00883337 extension data) as core dossier
- **Local safety data collection**: Obtain and review the full Aubagio® US Prescribing Information and EMA SmPC; extract hepatotoxicity monitoring protocol, teratogenicity risk management (mandatory pregnancy prevention program and accelerated elimination procedure with cholestyramine/activated charcoal), and lymphocyte count monitoring thresholds
- **Drug interaction profile**: Conduct formal DDI review given known CYP2C8 inhibition and potential interactions with warfarin, repaglinide, and hormonal contraceptives
- **Risk management plan**: Establish a local Risk Minimization Measure (RMM) program aligned with international REMS requirements, particularly for women of childbearing potential
- **Post-marketing surveillance plan**: Define monitoring parameters for hepatic enzyme elevation (ALT/AST), lymphopenia, blood pressure, and peripheral neuropathy consistent with international labeling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


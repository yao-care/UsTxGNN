---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 1019
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

> Pegaspargase (PEG-L-asparaginase, DrugBank DB00059) is an enzyme-based antineoplastic agent with an established, FDA-approved role in acute lymphoblastic leukemia (marketed as Oncaspar).
> The TxGNN model's top-ranked prediction — **Precursor Lymphoblastic Lymphoma/Leukemia** — is the same biological disease entity as its known indication,
> supported by **53 clinical trials** and **20 publications**, functioning here primarily as a benchmark validation of the model rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukemia (established/approved use, referenced as Oncaspar in evidence base; no formal license record in this dataset) |
| Predicted New Indication | Precursor lymphoblastic lymphoma/leukemia |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Market Status | Not Marketed (0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formal DrugBank-sourced mechanism of action record is not available in this evidence pack (flagged as a High-severity data gap, DG002). However, the model's own rationale field supplies sufficient mechanistic detail: pegaspargase depletes circulating asparagine. Precursor lymphoblastic (B- or T-cell) leukemia/lymphoma cells characteristically lack sufficient **asparagine synthetase** activity to synthesize their own asparagine, so systemic depletion selectively starves and induces apoptosis in these blasts while sparing most normal tissues, which can synthesize their own supply.

Critically, "precursor lymphoblastic lymphoma/leukemia" is not a distinct new disease relative to pegaspargase's original use — it is essentially the same biological entity as classic acute lymphoblastic leukemia (ALL), which is pegaspargase's core, decades-old, guideline-standard indication (as reflected in the model's own annotation for the related candidate "acute lymphoblastic leukemia," rank 5, which explicitly cites this as the approved Oncaspar indication). This candidate therefore functions less as a discovery of a new use and more as internal validation that the TxGNN knowledge graph correctly recovers a drug's known, ground-truth indication — a useful sanity check on model calibration, but not itself a repurposing opportunity requiring new clinical development.

Supporting mechanistic literature (e.g., Fu & Sakamoto, *Expert Opin Pharmacother* 2007, PMID 17696798) confirms that L-asparaginase efficacy across nearly 40 years of leukemia therapy is attributable to this asparagine-depletion mechanism, reinforcing the biological plausibility of the prediction even though a structured MOA field is missing from the drug record.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02716233](https://clinicaltrials.gov/study/NCT02716233) | Phase 3 | Active, not recruiting | 2,044 | French national protocol for pediatric/adolescent ALL investigating optimal L-asparaginase use across treatment phases |
| [NCT03020030](https://clinicaltrials.gov/study/NCT03020030) | Phase 3 | Active, not recruiting | 560 | Large-scale treatment protocol for newly diagnosed ALL in children/adolescents with pegaspargase as an induction component |
| [NCT00003437](https://clinicaltrials.gov/study/NCT00003437) | Phase 3 | Unknown | 1,800 | UK national trial (MRC) comparing steroid/chemotherapy regimens including asparaginase-based induction in childhood ALL |
| [NCT04954326](https://clinicaltrials.gov/study/NCT04954326) | Phase 2 | Completed | 89 | Pharmacokinetic comparison of liquid vs lyophilized pegaspargase formulations during induction in newly diagnosed pediatric ALL |
| [NCT06195735](https://clinicaltrials.gov/study/NCT06195735) | N/A | Completed | 649 | Predictive modeling of PEG-asparaginase hypersensitivity to optimize outcomes across NOPHO/ALLTogether protocols |
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | Completed | 37 | MOAD regimen (methotrexate, vincristine, pegylated L-asparaginase, dexamethasone) for relapsed/refractory ALL salvage |
| [NCT00187083](https://clinicaltrials.gov/study/NCT00187083) | Phase 3 | Completed | 40 | Head-to-head comparison of native vs PEG-asparaginase during induction for relapsed/refractory pediatric ALL |
| [NCT02881086](https://clinicaltrials.gov/study/NCT02881086) | Phase 3 | Completed | 1,023 | Individualized, MRD-directed adult ALL/lymphoblastic lymphoma treatment optimization incorporating asparaginase intensification |
| [NCT00198991](https://clinicaltrials.gov/study/NCT00198991) | Phase 4 | Completed | 1,883 | GMALL 07/2003 German multicenter adult/adolescent ALL trial with risk-stratified consolidation and MRD monitoring |
| [NCT00882206](https://clinicaltrials.gov/study/NCT00882206) | Phase 2 | Terminated | 15 | Decitabine/vorinostat plus VPLD chemotherapy (including PEG-asparaginase) for relapsed/refractory ALL/lymphoblastic lymphoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | COG AALL1231 phase 3 trial testing bortezomib in newly diagnosed T-ALL/T-LL, within a standard asparaginase-containing backbone |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | COG AALL0232: dexamethasone and high-dose methotrexate improve outcomes in high-risk B-ALL |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | COG AALL0434 phase 3 trial of nelarabine in newly diagnosed T-ALL |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort | J Clin Oncol | DFCI 11-001: efficacy/toxicity comparison of pegaspargase vs calaspargase pegol in childhood ALL |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort | Blood Adv | GIMEMA LAL1913: pegaspargase-modified risk-oriented program for adult ALL |
| [31571395](https://pubmed.ncbi.nlm.nih.gov/31571395/) | 2020 | Cohort | Pediatr Blood Cancer | Rapid desensitization protocol allowing continued pegaspargase use in hypersensitive pediatric patients |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | Expert panel consensus on recognition, prevention, and management of asparaginase/pegaspargase adverse events in adults |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Review | Expert Opin Pharmacother | Foundational review of PEG-asparaginase pharmacology, mechanism, and clinical role in leukemia |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Phase 2 | Int J Hematol | Multicenter Japanese phase 2 study of pegaspargase efficacy, safety, and PK in previously untreated ALL |
| [36227415](https://pubmed.ncbi.nlm.nih.gov/36227415/) | 2022 | Cost-Utility | Clin Drug Investig | Cost-utility analysis of pegaspargase vs L-asparaginase sequencing in Greek ALL patients |

---

## US Market Information

Currently no license/authorization records are on file for this drug in the evaluated jurisdiction (0 licenses; market status: Not Marketed). Pegaspargase is independently known to be marketed elsewhere as Oncaspar for ALL, but no local regulatory data confirms this within the current evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — enzyme-based antineoplastic (L-asparagine depletion; ATC L01XX02) |
| Myelosuppression Risk | Low as a single agent (asparaginase itself is not strongly myelosuppressive); however it is typically given within multi-agent regimens (e.g., with vincristine, anthracyclines, corticosteroids) where cumulative marrow suppression risk is significant |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Hepatic function (risk of hepatotoxicity), pancreatic enzymes/lipase (risk of pancreatitis), coagulation panel (fibrinogen, antithrombin — thrombosis/bleeding risk), triglycerides and glucose (hypertriglyceridemia, hyperglycemia), and serum asparaginase activity where available; close monitoring for hypersensitivity/anaphylaxis during and after infusion |
| Handling Protection | Must follow standard cytotoxic/hazardous antineoplastic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-drug interaction data were available in this evidence pack (TFDA/local label data flagged as a **Blocking** data gap, DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 (multiple completed/active Phase 3 trials plus RCTs) strongly supports pegaspargase's role in precursor lymphoblastic leukemia/lymphoma — but this is confirmatory of its already-known indication rather than a genuine new-use discovery, and two Blocking/High-severity data gaps (local safety labeling, formal MOA) currently prevent a full S1 safety review.

**To proceed, the following is needed:**
- Local package insert / TFDA-equivalent warnings, contraindications, and DDI data (DG001, Blocking)
- Formal DrugBank-sourced mechanism-of-action record (DG002, High)
- Clarification of actual market/licensing status, since 0 licenses are currently on file despite known global marketing as Oncaspar
- Given rank-1 is essentially a validation case, prioritize independent review of higher-uncertainty candidates in this pack (e.g., "lymphoid neoplasm" and the trial set mislabeled as "Hodgkin lymphoma," which is largely evidence for extranodal NK/T-cell lymphoma — a disease-ontology mapping check is recommended before further action on that candidate)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


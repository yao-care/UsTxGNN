---
layout: default
title: Cyclophosphamide
parent: High Evidence (L1-L2)
nav_order: 556
evidence_level: L2
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **5** 
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

# Cyclophosphamide: From Its Existing Indications to Myeloid Leukemia

## One-Sentence Summary

Cyclophosphamide is a marketed alkylating chemotherapy agent in the US, with 20 license records on file. The TxGNN model predicts it may be useful for **myeloid leukemia**, and the pack lists **50 clinical trials** and **20 publications** on this direction. Most of this evidence describes cyclophosphamide as one component of stem cell transplant regimens, not as a stand-alone leukemia treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available license records |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L2 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 license records (ANDA numbers) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cyclophosphamide is a prodrug. The liver enzyme CYP2B6 converts it to phosphoramide mustard, which cross-links DNA and gives the drug both cytotoxic and lymphodepleting effects. The structured mechanism-of-action field is empty in this record, so this description comes from the candidate's mechanistic analysis.

In myeloid leukemia, cyclophosphamide is used mainly in two transplant roles:

- **Conditioning:** it is part of myeloablative regimens such as busulfan-cyclophosphamide (BuCy).
- **Post-transplant cyclophosphamide (PTCy):** it is given after transplant to prevent graft-versus-host disease (GVHD).

The prediction is therefore reasonable, but the drug acts as a backbone agent in transplantation, not as a stand-alone antileukemic. The original indication is also missing from the data, so the "repurposing" framing should be checked against the current US label before it is used.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02065154](https://clinicaltrials.gov/study/NCT02065154) | Phase 2 | Completed | 39 | PTCy for acute GVHD prevention after matched or mismatched unrelated donor transplant |
| [NCT03128359](https://clinicaltrials.gov/study/NCT03128359) | Phase 2 | Completed | 38 | High-dose PTCy with tacrolimus and mycophenolate in mismatched unrelated donor transplant for hematologic malignancies |
| [NCT01010217](https://clinicaltrials.gov/study/NCT01010217) | Phase 2 | Completed | 176 | Three-arm transplant study (haploidentical, mismatched, matched unrelated donors) using high-dose PTCy |
| [NCT02120157](https://clinicaltrials.gov/study/NCT02120157) | Phase 2 | Completed | 35 | Pediatric haploidentical bone marrow transplant with PTCy in high-risk leukemia |
| [NCT00003340](https://clinicaltrials.gov/study/NCT00003340) | Phase 2 | Completed | Not reported | Cyclophosphamide followed by topotecan in refractory or relapsed acute myelogenous leukemia; the most direct antileukemic use of cyclophosphamide in this list |
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | Completed | 202 | Randomized comparison of G-CSF + decitabine + BuCy versus BuCy conditioning in MDS-related AML |
| [NCT03256071](https://clinicaltrials.gov/study/NCT03256071) | Phase 2/3 | Unknown | 90 | Randomized comparison of low-dose decitabine + modified BuCy versus modified BuCy in high-risk AML |
| [NCT00723099](https://clinicaltrials.gov/study/NCT00723099) | Phase 2 | Completed | 73 | Reduced-intensity cord blood transplant in hematologic malignancies; conditioning commonly includes cyclophosphamide |
| [NCT00125606](https://clinicaltrials.gov/study/NCT00125606) | Phase 3 | Terminated | 30 | Randomized comparison of TBI 8 Gy/fludarabine versus TBI 12 Gy/cyclophosphamide conditioning in AML in second remission; terminated early |
| [NCT06802315](https://clinicaltrials.gov/study/NCT06802315) | Phase 2 | Recruiting | 38 | Total marrow irradiation added to fludarabine/busulfan conditioning, with PTCy for GVHD prophylaxis, in high-risk AML, CML and MDS |

Points to keep in mind:

- The cyclophosphamide-specific trials are single-arm Phase 2 studies of PTCy; none isolates cyclophosphamide's own contribution.
- The only Phase 3 trial listed here (NCT00125606) was terminated with 30 patients.
- Several other trials in the pack were withdrawn or terminated with very few patients (for example NCT03602898, withdrawn with 0 enrolled).

---

## Literature Evidence

No randomized controlled trials were retrieved. The list below is led by the systematic review, then the most relevant cohort studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic review / network meta-analysis | Bone Marrow Transplant | Compares myeloablative conditioning regimens, including Bu/Cy, in adult AML in first remission |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Cohort | Bone Marrow Transplant | 1,823 AML patients transplanted with PTCy; conditioning intensity analyzed by cytogenetic and molecular risk (EBMT) |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohort | Future Oncol | Compares BuCy, the standard myeloablative regimen, with fludarabine-busulfan in AML allogeneic transplant |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Cohort | Eur J Haematol | Reduced-intensity versus myeloablative conditioning in AML patients under 65 given ATG and PTCy |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohort | Cytotherapy | Prognostic factors in haploidentical transplant with PTCy for AML |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Cohort | Int J Mol Sci | PTCy after matched sibling and unrelated donor transplant in pediatric AML |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohort | Haematologica | 217 AML patients in remission given myeloablative conditioning and PTCy; 2-year overall survival 77% and event-free survival 72% |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Cohort | Transpl Immunol | Cladribine + busulfan + cyclophosphamide conditioning in relapsed or refractory AML |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | Case series | Leuk Lymphoma | High-dose cyclophosphamide (60 mg/kg) for cytoreduction in 27 patients with AML or blast-phase CML with hyperleukocytosis or leukostasis |
| [29039989](https://pubmed.ncbi.nlm.nih.gov/29039989/) | 2017 | Case series | Pediatr Hematol Oncol | Clofarabine + cyclophosphamide + etoposide in 17 children with relapsed or refractory AML; 7 (41%) responded |

---

## US Market Information

The 5 records provided contain only 3 unique authorizations. The approved indication text is empty for all of them, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA215892 | Cyclophosphamide | Capsule | Alembic Pharmaceuticals Inc. |
| ANDA218644 | Cyclophosphamide | Injection, powder, for solution | Epic Pharma, LLC |
| ANDA211757 | Cyclophosphamide | Injection, powder, lyophilized, for solution | XGen Pharmaceuticals DJB, Inc. |

Other dosage forms on record include tablets, injection solution and injection. Both oral and injectable routes are therefore available.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard prodrug) |
| Myelosuppression Risk | Moderate to high, dose-dependent; higher at conditioning doses |
| Emetogenicity Classification | Moderate to high for high-dose IV use; lower with oral low-dose use |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, urinalysis for hemorrhagic cystitis; cardiac monitoring at high doses |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries reflect general knowledge of the drug class, not DrugBank toxicity data. Please refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cyclophosphamide is an established backbone agent in AML transplant regimens (BuCy conditioning and PTCy), and the model score is very high. The evidence, however, is mostly single-arm Phase 2 or observational, and it does not isolate cyclophosphamide's effect from the rest of the regimen, so it should not be treated as a stand-alone antileukemic.

**To proceed, the following is needed:**
- The current US label indication text, to confirm whether myeloid leukemia is already covered (the original indication is missing from the pack)
- Package insert warnings and contraindications, which are still missing and block safety screening
- Structured mechanism-of-action data from DrugBank
- Arm-level review of the trials to confirm the cyclophosphamide-containing arms and to separate conditioning use from PTCy use
- A safety monitoring plan for high-dose use (myelosuppression, hemorrhagic cystitis, cardiotoxicity)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


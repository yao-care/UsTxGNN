---
layout: default
title: Idelalisib
parent: Model Prediction Only (L5)
nav_order: 787
evidence_level: L5
indication_count: 10
---

# Idelalisib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Idelalisib: From Relapsed CLL and Follicular Lymphoma to Mantle Cell Lymphoma

## One-Sentence Summary

Idelalisib (Zydelig) is an oral PI3K-delta inhibitor. Published reviews describe it as originally approved in the US for relapsed chronic lymphocytic leukemia (CLL), follicular lymphoma and small lymphocytic lymphoma (SLL).
The TxGNN model predicts it may be effective for **mantle cell lymphoma (MCL)**.
Support is early-stage only: **9 clinical trials** (mostly Phase 1) and **20 publications**, largely reviews and preclinical work.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed CLL, follicular lymphoma, SLL (from published literature; the US label text was not supplied) |
| Predicted New Indication | Mantle cell lymphoma |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 (the pack lists L2, but the supplied MCL trials are registered as Phase 1 only, so I rated conservatively) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 records (both NDA205858) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. From general knowledge, idelalisib selectively blocks the delta isoform of PI3K. This isoform sits in the B-cell receptor signaling pathway that many B-cell cancers depend on for survival and growth.

CLL, follicular lymphoma and MCL are all B-cell malignancies. Idelalisib's activity in the first two makes its use in MCL biologically plausible. Preclinical papers support this: idelalisib inhibits translation-regulatory signaling in MCL cells (PMID 27342398). Other studies show MCL cells can resist idelalisib, and that a p300/CBP inhibitor or propolis can restore sensitivity (PMIDs 33850273, 40466505). A 2014 Phase 1 study in relapsed/refractory MCL exists (PMID 24615778), and a commentary describes activity in heavily pretreated patients (PMID 24795031).

Important caveats:
- No Phase 3 trial or MCL approval appears in the supplied data.
- BTK inhibitors are established alternatives.
- The supplied literature notes that safety problems reduced the drug's use. A 2023 review reports Gilead voluntarily withdrew the follicular lymphoma and SLL accelerated-approval indication in 2022 (PMID 36939665).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1 (registered; the title describes a Phase I/randomized Phase II) | Completed | 106 | Idelalisib + lenalidomide vs lenalidomide alone in relapsed/refractory MCL. This is the most direct trial, and no results are in the pack. |
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Completed | 241 | Safety of idelalisib combined with chemotherapy, immunomodulators or anti-CD20 antibody in relapsed B-cell NHL, MCL or CLL. MCL cohort size is not confirmed. |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1 | Completed | 20 | BCL201 + idelalisib in follicular lymphoma and MCL. A small dose-escalation safety study. |
| [NCT02457598](https://clinicaltrials.gov/study/NCT02457598) | Phase 1 | Terminated | 203 | Tirabrutinib with other targeted agents (including idelalisib) in B-cell malignancies. Limited efficacy information. |
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Terminated | 66 | Entospletinib + idelalisib in relapsed/refractory hematologic malignancies (CLL, MCL, DLBCL, iNHL). |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Terminated | 16 | Idelalisib maintenance after allogeneic transplant in B-cell malignancies. Safety-focused, weak evidence. |
| [NCT03740529](https://clinicaltrials.gov/study/NCT03740529) | Phase 1/2 | Completed | 803 | Pirtobrutinib in CLL/SLL/NHL. Idelalisib is likely prior therapy only, so this is not evidence for idelalisib. |
| [NCT02824159](https://clinicaltrials.gov/study/NCT02824159) | N/A (observational) | Completed | 121 | Side effects vs plasma concentrations of ibrutinib and idelalisib. Safety and PK context only. |
| [NCT04985214](https://clinicaltrials.gov/study/NCT04985214) | N/A (observational) | Unknown | 464 | Quality of life with oral lymphoma therapies. No efficacy data. |

---

## Literature Evidence

No randomized controlled trials were found for this indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [24615778](https://pubmed.ncbi.nlm.nih.gov/24615778/) | 2014 | Phase 1 study | Blood | 48-week dose-escalation study of idelalisib in 40 patients with relapsed/refractory MCL. It assessed safety, dose-limiting toxicity, response and progression-free survival. |
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | Commentary | Cancer Discovery | Describes idelalisib as effective in heavily pretreated MCL patients. |
| [28775119](https://pubmed.ncbi.nlm.nih.gov/28775119/) | 2017 | Review | Haematologica | Incidence and management of ibrutinib and idelalisib toxicity in indolent B-cell malignancies, including MCL. |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Review | Br J Haematol | Current regimens and novel agents in MCL. The disease remains incurable. |
| [28295729](https://pubmed.ncbi.nlm.nih.gov/28295729/) | 2017 | Review | J Intern Med | B-cell receptor pathway inhibitors (BTK, PI3K and others) in B-cell malignancies. |
| [26637705](https://pubmed.ncbi.nlm.nih.gov/26637705/) | 2015 | Review | Hematology ASH Educ Program | BCR-pathway modulators in NHL, including combinations with chemotherapy and antibodies. |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Preclinical | Clin Cancer Res | Idelalisib impairs cell growth in MCL by inhibiting translation-regulatory mechanisms. |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Preclinical | Acta Pharmacol Sin | MCL shows intrinsic resistance to idelalisib. The p300/CBP inhibitor A-485 overcomes it in vitro and in vivo. |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Preclinical | Cancer Lett | Idelalisib enhances the anti-tumor effect of palbociclib via PLK1 in B-cell lymphoma (DLBCL and MCL). |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Preclinical | Phytomedicine | CBX5 loss drives PI3K-delta inhibitor resistance in MCL. Propolis restores sensitivity through ferroptosis. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA205858 | Zydelig | Tablet, film coated (oral) | Gilead Sciences, Inc. |

The pack lists two identical records under this NDA, shown once here. Approved-indication text was not supplied.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3K-delta kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Medium (neutropenia is a recognized effect of this class; no toxicity data supplied, so confirm against the package insert) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver enzymes and bilirubin, renal function, and clinical monitoring for diarrhea/colitis, cough or dyspnea (pneumonitis), and infection |
| Handling Protection | Follow the institution's hazardous-drug handling policy for oral antineoplastics |

---

## Safety Considerations

The package insert warnings, contraindications and interaction data were not available in the Evidence Pack. Please refer to the package insert. The supplied evidence flags the following class toxicities:

- **Serious toxicities:** hepatotoxicity, severe diarrhea/colitis, pneumonitis, serious infections and intestinal perforation.
- **Excess deaths in earlier-line use:** trials in front-line CLL and early-line indolent NHL noted an increased rate of deaths and serious adverse events with idelalisib plus standard therapies. Several Phase 3 studies were terminated as a result.
- **Colitis:** a dedicated mechanism study of idelalisib-associated colitis was registered (NCT02928510).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The MCL prediction is mechanistically plausible, and there is a Phase 1 MCL study plus a randomized idelalisib + lenalidomide trial. However, no efficacy results, Phase 3 data or MCL approval are in the supplied data. BTK inhibitors already exist, and idelalisib carries serious, partly fatal class toxicities.

**To proceed, the following is needed:**
- Results of NCT01838434 and the MCL cohorts of NCT01088048 (response rate, duration of response, progression-free survival, safety).
- The US package insert (boxed warning, contraindications, interactions) and the current approval status of Zydelig.
- Mechanism-of-action data from DrugBank.
- A comparison against BTK inhibitors and other current MCL options, with a defined patient population (for example, post-BTK-inhibitor failure).
- A safety monitoring plan (liver enzymes, colitis and pneumonitis surveillance, infection prophylaxis).

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


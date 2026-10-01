---
layout: default
title: Procarbazine
parent: Model Prediction Only (L5)
nav_order: 1087
evidence_level: L5
indication_count: 5
---

# Procarbazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Procarbazine: From Hodgkin Lymphoma to Follicular Lymphoma

## One-Sentence Summary

Procarbazine is an oral alkylating-type chemotherapy agent, established in Hodgkin lymphoma regimens such as MOPP and BEACOPP.
The TxGNN model predicts it may be effective for **follicular lymphoma**, but the supporting evidence is thin: **3 loosely related clinical trials** (none clearly testing procarbazine) and **1 case-based review** showing durable remissions in 2 patients.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma (from the mechanistic rationale; the US label indication text is not provided in the data) |
| Predicted New Indication | Follicular lymphoma |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L3 (weak: case-based review and indirect trials only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the input. Based on known information, procarbazine is an alkylating-type agent that methylates DNA. Its efficacy in Hodgkin lymphoma is well established, and mechanistically it may be applicable to B-cell non-Hodgkin lymphoma, including follicular lymphoma.

Procarbazine-containing regimens for non-Hodgkin lymphoma fell out of favor with the arrival of CHOP. A 2006 report described two patients with relapsed or refractory follicular lymphoma who achieved complete, durable remissions on prolonged daily procarbazine. This is the only procarbazine-specific clinical signal in the evidence pack, and it comes from two patients.

The very high TxGNN score is consistent with this rationale but is not proof of efficacy. No trial in the pack clearly shows a procarbazine-specific effect in follicular lymphoma.

The lower-ranked predictions are weaker still:
- **Neuroblastoma:** in vitro data only.
- **Ganglioneuroblastoma:** model prediction only.
- **Retroperitoneal neoplasm:** indirect lymphoma literature.
- **Vertebral anomalies with endocrine and T-cell dysfunction:** probably a knowledge-graph artifact.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01130194](https://clinicaltrials.gov/study/NCT01130194) | Phase 2 | Completed | 29 | Pilot of sequential chemotherapy, radioimmunotherapy and autologous transplant in follicular lymphoma. Procarbazine is not evidently part of the regimen (indirect evidence at most). |
| [NCT00577993](https://clinicaltrials.gov/study/NCT00577993) | Phase 3 | Completed | 210 | Fludarabine, mitoxantrone and dexamethasone plus rituximab in stage IV indolent lymphoma. Procarbazine is not involved; useful only as a treatment-landscape comparator. |
| [NCT00003113](https://clinicaltrials.gov/study/NCT00003113) | Phase 2 | Terminated | 6 | Oral combination chemotherapy with G-CSF in elderly patients with intermediate/high-grade NHL. The regimen likely contains procarbazine (unconfirmed). Terminated at 6 patients, so no usable efficacy signal, and the population is not follicular lymphoma-specific. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16690522](https://pubmed.ncbi.nlm.nih.gov/16690522/) | 2006 | Review (case-based) | Leuk Lymphoma | Two patients with relapsed/refractory follicular lymphoma achieved complete, durable remission on prolonged daily procarbazine. |
| [16111588](https://pubmed.ncbi.nlm.nih.gov/16111588/) | 2005 | Randomized study | Int J Radiat Oncol Biol Phys | Compared molecular response of central lymphatic irradiation vs. intensive alternating triple chemotherapy in stage I-III follicular lymphoma. Whether procarbazine is in the regimen is not stated in the abstract. |
| [22507790](https://pubmed.ncbi.nlm.nih.gov/22507790/) | 2012 | Not classified | Hematology | Describes PEP-C, a low-dose metronomic oral combination regimen for refractory/relapsed lymphoma. |
| [9156664](https://pubmed.ncbi.nlm.nih.gov/9156664/) | 1997 | Not classified | Leuk Lymphoma | Salvage treatment after initial chemotherapy failure or relapse in follicular NHL. Of 34 patients who failed initial treatment, 7 (21%) achieved CR with various salvage regimens. |
| [16230674](https://pubmed.ncbi.nlm.nih.gov/16230674/) | 2005 | Review | J Clin Oncol | New treatment options have changed survival of follicular lymphoma patients (treatment-landscape context). |
| [9336721](https://pubmed.ncbi.nlm.nih.gov/9336721/) | 1997 | Review | Hematol Oncol Clin North Am | Overview of localized low-grade lymphoma treatment. Radiotherapy may cure 40-50% of stage I/II follicular lymphoma. |
| [11672513](https://pubmed.ncbi.nlm.nih.gov/11672513/) | 2001 | Not classified | J Hematother Stem Cell Res | Chemotherapy plus interferon-alpha2b vs. chemotherapy alone in follicular lymphoma. |
| [9248325](https://pubmed.ncbi.nlm.nih.gov/9248325/) | 1997 | Not classified | Rinsho Ketsueki | 72 follicular lymphoma patients treated with combination chemotherapy: 83.3% CR and 63.7% 5-year overall survival. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA016785 | Matulane (Leadiant Biosciences, Inc.) | Capsule (oral) | Not provided in the data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating-type agent) |
| Myelosuppression Risk | Expected to be high, as with alkylating chemotherapy. Please refer to the package insert for details. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications and drug interaction data were not retrieved (interaction query returned no results).

Carcinogenicity: the retrieved literature includes an NCI animal bioassay ([PMID 12844148](https://pubmed.ncbi.nlm.nih.gov/12844148/)) and a review of nasal carcinogens ([PMID 9385384](https://pubmed.ncbi.nlm.nih.gov/9385384/)) listing procarbazine among chemicals that produced tumors in rodents. Older pediatric oncology reports also associate MOPP-containing regimens (which include procarbazine) with azoospermia and secondary neoplasms.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high and the alkylator mechanism is plausible. However, the only procarbazine-specific follicular lymphoma evidence is two case reports, and none of the listed trials clearly tests procarbazine. Follicular lymphoma has many effective modern options, and the safety review is blocked by missing package insert data. The pack's own recommendation is "Research Question" (stage S1).

**To proceed, the following is needed:**
- Obtain the FDA package insert (warnings, contraindications, indication text). This is a blocking gap for safety screening.
- Obtain mechanism of action data from DrugBank.
- Confirm whether NCT00003113 and PMIDs 16111588 and 22507790 actually used procarbazine, and extract response data.
- Run a systematic search for procarbazine-containing regimens in follicular or indolent lymphoma, to see if evidence beyond case reports exists.
- Define a comparison against current standard follicular lymphoma therapy and a safety plan (myelosuppression, secondary malignancy, fertility).

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


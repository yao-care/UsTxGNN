---
layout: default
title: Vinblastine
parent: Moderate Evidence (L3-L4)
nav_order: 1292
evidence_level: L4
indication_count: 10
---

# Vinblastine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Vinblastine: From Antineoplastic Use to Rhabdomyosarcoma

## One-Sentence Summary

Vinblastine is a vinca-alkaloid chemotherapy injection marketed in the US. The label data in this pack do not state its approved indication.
The TxGNN model predicts it may be effective for **Rhabdomyosarcoma**.
Support is thin: **no registered clinical trials** and **15 publications**, mostly case reports, preclinical work, and studies of related vinca drugs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the provided label data (the approved indication text is blank) |
| Predicted New Indication | Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (ANDA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. The supporting rationale in the evidence pack is that vinblastine binds tubulin, inhibits microtubule assembly, and causes mitotic arrest in dividing cells. This is the same class mechanism as vincristine and vinorelbine, which have established or reported activity in rhabdomyosarcoma.

Preclinical work supports the idea. Microtubule-destabilizing drugs showed activity in rhabdomyosarcoma models, including a synergy with PLK1 inhibitors (PMID 26024389). Older xenograft work also examined vinca alkaloid sensitivity in human rhabdomyosarcoma (PMID 3329524).

No vinblastine-specific clinical trial in rhabdomyosarcoma is provided. The clinical signals are indirect: vinblastine appears only as part of multi-drug regimens in case reports, and the Phase 2 studies used vinorelbine, a different vinca drug. The prediction is therefore best treated as a research question, not a treatment recommendation.

Among the model's other predictions, neuroblastoma has the strongest support (evidence level L2). It has a Phase 1 vinblastine-sirolimus pediatric study and a completed single-arm Phase 2 metronomic trial (NCT02641314, n=18). Several other rhabdomyosarcoma subtypes and sites have prediction only, with no supporting studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rhabdomyosarcoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38050209](https://pubmed.ncbi.nlm.nih.gov/38050209/) | 2023 | Case report/Review | Medicine | Adult perineal rhabdomyosarcoma: a partial response was seen after nivolumab, dacarbazine, cisplatin, and vinblastine, followed by surgery. This is a combination regimen, so vinblastine's contribution is unclear. |
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase 2 (vinorelbine, indirect) | Eur J Cancer | Vinorelbine plus low-dose oral cyclophosphamide in relapsed or refractory pediatric solid tumours. The title reports good tolerance and efficacy in rhabdomyosarcoma. |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Phase 2 (vinorelbine, indirect) | Cancer | Vinorelbine in previously treated advanced childhood sarcomas showed evidence of activity in rhabdomyosarcoma. |
| [15378498](https://pubmed.ncbi.nlm.nih.gov/15378498/) | 2004 | Pilot study (vinorelbine, indirect) | Cancer | Dose-finding pilot of vinorelbine with low-dose cyclophosphamide in refractory or recurrent pediatric sarcoma. |
| [3329524](https://pubmed.ncbi.nlm.nih.gov/3329524/) | 1987 | Preclinical/Review | Anti-Cancer Drug Des | Vinca alkaloid selectivity examined in human rhabdomyosarcoma xenografts in mice. |
| [26024389](https://pubmed.ncbi.nlm.nih.gov/26024389/) | 2015 | Preclinical | Cell Death Differ | PLK1 inhibitors and microtubule-destabilizing drugs show synthetic lethality in rhabdomyosarcoma models. |
| [2451411](https://pubmed.ncbi.nlm.nih.gov/2451411/) | 1987 | Case report/Review | Hinyokika Kiyo | Refractory prostatic rhabdomyosarcoma in a child, treated with cisplatin, vinblastine, and peplomycin (PVP) after standard therapy failed. The mass reduced rapidly, but this is a single case. |
| [22156656](https://pubmed.ncbi.nlm.nih.gov/22156656/) | 2011 | Pilot study | Oncotarget | Pediatric metronomic 4-drug regimen. Vinblastine's role is unconfirmed. |
| [41216926](https://pubmed.ncbi.nlm.nih.gov/41216926/) | 2026 | Prospective trials (reclassified data) | Pediatr Blood Cancer | CWS-96 and CWS-2002P trials in non-rhabdomyosarcoma soft tissue sarcoma. Related disease area, not rhabdomyosarcoma itself. |

No randomized controlled trials were found for this indication.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA089515 | Vinblastine Sulfate (Fresenius Kabi USA, LLC) | Injection | Not stated in the provided data |

---

## Cytotoxicity

Vinblastine is a conventional cytotoxic antineoplastic. The table below is based on general knowledge of the vinca-alkaloid class; the pack contains no toxicity data.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, antimicrotubule agent) |
| Myelosuppression Risk | High (leukopenia is typical for this class) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for authoritative details.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high (99.86%), but the support is indirect: case reports, preclinical studies, and trials of vinorelbine instead of vinblastine. There are no registered trials and no vinblastine-specific clinical data in rhabdomyosarcoma. Vinblastine is also not a standard component of established rhabdomyosarcoma regimens in this record.

**To proceed, the following is needed:**
- The package insert (warnings, contraindications, approved indication) to complete the safety screen
- Mechanism-of-action data from DrugBank
- A structured review of whether vinblastine adds benefit beyond vincristine or vinorelbine in rhabdomyosarcoma
- Consideration of neuroblastoma, which has stronger evidence, as a higher-priority candidate from this drug's prediction list

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


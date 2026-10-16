---
layout: default
title: Melphalan
parent: High Evidence (L1-L2)
nav_order: 896
evidence_level: L2
indication_count: 10
monitor_inn: "MELPHALAN"
predicted_indications: ["gonadal germ cell tumor", "ovarian primitive germ cell tumor", "choriocarcinoma of ovary", "female breast carcinoma", "malignant non-epithelial tumor of ovary", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma"]
---

# Melphalan
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Melphalan: From Ovarian Cancer to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is an alkylating chemotherapy agent, originally used for ovarian cancer.
The TxGNN model predicts it may be effective for **gonadal germ cell tumor**,
with **7 clinical trials** (4 of them completed Phase 1/2 or Phase 2 studies that include melphalan or a melphalan-containing regimen) and **1 publication** currently supporting this direction. The literature support is very thin.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (including ovarian adenocarcinoma and ovarian germ cell tumor subtypes) |
| Predicted New Indication | Gonadal germ cell tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, melphalan is a bifunctional alkylating agent that cross-links DNA and so kills rapidly dividing cells. Its efficacy in ovarian cancer has been established, and mechanistically it may be applicable to gonadal germ cell tumors.

Germ cell tumors are generally highly sensitive to DNA-damaging chemotherapy. This is the rationale for high-dose regimens that include melphalan, followed by autologous stem cell rescue, in relapsed or poor-prognosis disease. Several of the original ovarian indications in the knowledge graph are themselves germ cell histologies (yolk sac tumor, malignant germ cell tumor of ovary, and others). This overlap likely explains the high prediction score.

The evidence has important limits. In the supporting trials, melphalan is almost always one part of a multi-drug high-dose regimen, so its individual contribution cannot be separated out. The one Phase 2 study that directly targets germ cell tumors (NCT00936936) was a single-arm study of 64 patients, and the data compiled for this report do not include its efficacy results.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy (first cycle: gemcitabine, docetaxel, melphalan, carboplatin; second cycle: ifosfamide, carboplatin, etoposide) in poor-prognosis relapsed germ cell tumors. Safety also assessed. |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with autologous stem cell support and amifostine cytoprotection in cancer patients. Germ cell tumors are among the eligible tumors. |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemotherapy regimens, with or without radiation, plus autologous transplant in hematologic malignancies and selected solid tumors. The germ cell subset is likely small. |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Pilot of busulfan, melphalan and topotecan followed by autologous stem cell transplant in advanced and recurrent tumors. |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | Completed | 174 | Different high-dose chemotherapy regimens, with or without total-body irradiation, before autologous transplant in hematologic cancers and solid tumors. Low specificity for germ cell tumors. |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan in recurrent neoplastic meningitis. Different route and setting, so only indirectly relevant. |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine as a chemoprotectant with autologous transplant in pediatric solid and brain tumors. Focus is supportive care, not melphalan efficacy. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Preclinical/Other | Acta - Unio Internationalis Contra Cancrum | Early report on the influence of hormonal and alkylating drugs on pituitary follicle-stimulating function. No abstract is available, and it does not provide clinical efficacy evidence for germ cell tumors. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA207155 | EVOMELA (Acrotech Biopharma) | Injection, powder, lyophilized, for solution | Not available (status: cancelled) |
| NDA217110 | IVRA (Apotex) | Injection, solution | Not available (status: cancelled) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High. The knowledge graph links melphalan to neutropenia, leukopenia, thrombocytopenia, anemia and agranulocytosis. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function. Pulmonary status should also be followed given the graph links to interstitial lung disease and pulmonary fibrosis. |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: Melphalan is linked to hematologic conditions (thrombocytopenia, anemia, leukopenia, neutropenia, agranulocytosis, hemolytic anemia, and congenital neutropenia syndromes). It is also linked to kidney disease, interstitial lung disease, pulmonary fibrosis, drug-induced liver injury and vasculitis. These links should be confirmed against the official label.
- **Drug Interactions**: 100 interactions were recorded. Moderate-level interactions include amphotericin B and its lipid, cholesteryl sulfate and liposomal formulations. Minor-level interactions include cimetidine, levofloxacin, zinc sulfate and zinc gluconate. Several others are of unknown severity (for example, PPIs, famotidine, metformin, prednisone, simvastatin and vancomycin).

Official package insert warnings and contraindications were not available, so please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Melphalan has plausible biology in chemosensitive germ cell tumors, and a completed Phase 2 trial exists in relapsed germ cell tumors. However, melphalan is only one component of a combination regimen, the supporting literature is minimal, and efficacy results are not in the compiled data. Both US NDAs are cancelled, and the label safety data are missing. A hold fits until these gaps are closed.

**To proceed, the following is needed:**
- Efficacy and safety results from NCT00936936, with the specific contribution of melphalan assessed
- Detailed mechanism of action data (MOA) and the FDA package insert warnings and contraindications
- Clarification of the current US regulatory and supply status, since both NDAs are cancelled
- A focused literature review of high-dose melphalan regimens in germ cell tumors
- A safety monitoring plan for myelosuppression, and for renal and pulmonary risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


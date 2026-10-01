---
layout: default
title: Ifosfamide
parent: Model Prediction Only (L5)
nav_order: 788
evidence_level: L5
indication_count: 10
---

# Ifosfamide
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

# Ifosfamide: From Its Labeled Indication (Not Recorded) to Female Breast Carcinoma

## One-Sentence Summary

Ifosfamide is a cytotoxic alkylating chemotherapy drug that is marketed in the US as an injection. The label indication text is not recorded in this dataset.
The TxGNN model predicts it may be useful for **female breast carcinoma**.
The evidence is **8 registered clinical trials** and **20 publications**, but all trials are early phase, terminated, of unknown status, or only loosely tied to breast cancer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (all US license records have empty indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 (the Evidence Pack assigns L2, but no completed randomized Phase 2/3 trial in breast cancer is confirmed; see below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 9 license records |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input record. Ifosfamide is an oxazaphosphorine alkylating prodrug. Liver enzymes (CYP3A4, CYP2B6, CYP2C9) convert it to 4-hydroxy-ifosfamide, which cross-links DNA and kills dividing cells. This description comes from general pharmacology, not from the input record.

The mechanism is plausible in breast cancer. Breast tumour tissue expresses the activating enzymes (PMID 14970873), and ifosfamide metabolism and DNA damage have been measured in breast cancer patients (PMID 11138456). Several older Phase 2 studies also tested ifosfamide combinations in metastatic and anthracycline-pretreated breast cancer.

No modern randomized evidence shows that ifosfamide improves outcomes in breast cancer. The original indication is also missing from the record, so the link between the original and new indication cannot be assessed.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | Unknown | 42 | Docetaxel + ifosfamide as first-line chemotherapy in metastatic breast cancer. This is the most direct match, but no results are given. |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | Intensive topotecan, ifosfamide/mesna and etoposide (TIME) with autologous stem cell rescue in metastatic breast cancer. Ifosfamide's contribution cannot be separated. |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | Unknown | N/A | Randomized comparison of multi-cycle high-dose chemotherapy versus optimized conventional-dose chemotherapy in metastatic breast cancer. The role of ifosfamide is unclear. |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Completed | 33 | Sequential high-dose cisplatin, cyclophosphamide, etoposide, ifosfamide, carboplatin and paclitaxel with stem cell support in advanced cancer. It supports feasibility, not efficacy. |
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | Unknown | 637 | Paclitaxel + carboplatin versus ifosfamide + paclitaxel in uterine, tubal, peritoneal or ovarian carcinosarcoma. It is not a breast cancer population, so it does not count as direct evidence. |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | Terminated | 7 | Activated T cells after stem cell transplant in stage IV breast cancer. Ifosfamide is not the focus. |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | Terminated | 12 | Samarium-153 with sequential autologous transplant in stage IV breast cancer. Ifosfamide is at most a background agent. |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Organoid drug-screening study in refractory solid tumours. It is hypothesis-generating and does not test ifosfamide. |

## Literature Evidence

No RCTs were retrieved. The table lists the most relevant clinical studies first, then mechanistic and PK work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Phase 2 | Cancer | Paclitaxel (24-hour infusion) + ifosfamide in anthracycline-resistant metastatic breast cancer; efficacy and tolerability study. |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Phase 2 | Tumori | Ifosfamide + etoposide in previously treated advanced breast cancer; response and toxicity evaluation. |
| [8873839](https://pubmed.ncbi.nlm.nih.gov/8873839/) | 1996 | Clinical study | J Chemother | Ifosfamide, mesna and epirubicin as second-line therapy in 16 patients: overall response 50% (6% complete, 44% partial), median remission 9.6 months. |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Clinical study | J Clin Oncol | Ifosfamide + vinorelbine as first-line chemotherapy in metastatic breast cancer. |
| [10602903](https://pubmed.ncbi.nlm.nih.gov/10602903/) | 1999 | Prospective trial | Cancer Chemother Pharmacol | Ifosfamide + vinorelbine in metastatic breast cancer after prior anthracycline. |
| [2112056](https://pubmed.ncbi.nlm.nih.gov/2112056/) | 1990 | Clinical study | Cancer Chemother Pharmacol | Ifosfamide/etoposide with mesna in 44 patients with refractory advanced breast cancer. |
| [2347057](https://pubmed.ncbi.nlm.nih.gov/2347057/) | 1990 | Clinical study | Cancer Chemother Pharmacol | Ifosfamide substituted for cyclophosphamide in CMF in 25 patients with CMF-refractory or relapsed breast cancer. |
| [39306877](https://pubmed.ncbi.nlm.nih.gov/39306877/) | 2024 | Clinical study | Curr Probl Cancer | Ifosfamide-based first-line chemotherapy in metaplastic breast cancer, a rare variant with poor response to standard therapy. |
| [7695982](https://pubmed.ncbi.nlm.nih.gov/7695982/) | 1995 | PK cohort | Eur J Cancer | Pharmacokinetics and clinical effect of ifosfamide (5 g/m², 24-hour infusion) in 15 breast cancer patients. |
| [3286879](https://pubmed.ncbi.nlm.nih.gov/3286879/) | 1988 | Review | J Natl Cancer Inst | General ifosfamide review: significant activity in soft tissue sarcoma and testicular carcinoma; efficacy in other diseases awaited further study. |

## US Market Information

The record lists 9 licenses; the table shows the main distinct authorizations. Indication text is empty in every record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019763 | IFOSFAMIDE / IFEX (Baxter Healthcare) | Injection, powder, for solution | Not listed in record |
| ANDA076619 | Ifosfamide (Hikma) | Injection | Not listed in record |
| ANDA076078 | Ifosfamide (Fresenius Kabi) | Injection, powder, lyophilized, for solution | Not listed in record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (oxazaphosphorine alkylating agent) |
| Myelosuppression Risk | High (dose-dependent) |
| Emetogenicity Classification | Moderate to high (dose-dependent) |
| Monitoring Items | CBC with differential, renal function, urinalysis for hematuria, liver function, electrolytes, neurological status |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Reported toxicities (from the retrieved literature and rationale, not the label):** nephrotoxicity, neurotoxicity including ifosfamide-induced encephalopathy (PMID 41818182), hemorrhagic cystitis requiring mesna uroprotection, myelosuppression, and secondary myeloid neoplasms (therapy-related MDS/AML).

Please refer to the package insert for warnings, contraindications and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The breast cancer support is older, mostly small Phase 2 combination studies, and the registered trials are terminated, of unknown status, or not breast-specific. No completed randomized trial isolates ifosfamide's contribution. The package insert safety review, a blocking gap, has not been done, and ifosfamide is a highly toxic drug.

**To proceed, the following is needed:**
- FDA package insert warnings, contraindications and label indications (blocking data gap)
- Mechanism of action data from DrugBank
- Verification of NCT00012311 and NCT00026078 (design, ifosfamide role, results), and of NCT00954174, which does not appear to be a breast cancer study
- A comparison against current standard breast cancer regimens, plus a toxicity monitoring plan with mesna and renal and neurological checks

**Other candidates in the same pack:** rank 7, rhabdomyosarcoma, has stronger support: a completed Phase 3 (NCT00354744) with dose-compressed ifosfamide/etoposide, and PMID 11846301 reporting ifosfamide/etoposide superior to vincristine/melphalan in metastatic disease. It is scored L1 and "Proceed with Guardrails" in the Evidence Pack, and merits a separate evaluation. The myelodysplastic syndrome, monocytic leukemia and refractory cytopenia predictions are contradicted by literature showing treatment-related myeloid neoplasms after ifosfamide-containing regimens.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Gemcitabine
parent: Model Prediction Only (L5)
nav_order: 748
evidence_level: L5
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine: From Established Oncology Use to Female Breast Carcinoma

## One-Sentence Summary

Gemcitabine is a nucleoside-analog chemotherapy injection marketed in the US under 20 authorizations. The regulatory records provided do not list its approved indications.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with a near-saturated score of 99.98%.
The search retrieved **50 clinical trial records** (many only tangentially related) and **20 publications**, including at least two completed Phase 3 trials in breast cancer.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the regulatory records provided (all approved-indication fields are empty) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (NDAs and ANDAs combined) |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* Two completed Phase 3 randomized trials in breast cancer contain gemcitabine (NCT00006459, NCT00093795), which meets the L1 rule. The upstream pipeline scored this candidate L2 because those trials had not yet been relevance-graded. The trial records supply no efficacy results, so L1 reflects trial design and status, not proven benefit.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, gemcitabine is a nucleoside analog. Its active metabolites inhibit ribonucleotide reductase and terminate DNA chain elongation, which acts on rapidly proliferating tumor cells. This description is general knowledge, not taken from the input data.

This is more of a confirmation than a novel repurposing signal. The publications describe gemcitabine as active in metastatic breast cancer, both as a single agent (response rates of 16% to 37% in one review) and in combination with taxanes, platinum, vinorelbine, anthracyclines and trastuzumab. The empty original-indication field is probably a data gap, not evidence that the drug has no established use.

Preclinical work also supports a combination rationale. Additive or synergistic effects were seen with trastuzumab in HER2-overexpressing breast cancer cell lines. Because the TxGNN score is near-saturated (0.9998), it does not separate candidates and should not be read as strong evidence on its own.

---

## Clinical Trial Evidence

The 10 most relevant of the 50 retrieved trials are listed below. The other 40 are mostly other tumor types or combination studies of novel agents.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | Not reported | Randomized: paclitaxel with or without gemcitabine in unresectable, locally recurrent or metastatic breast cancer. No results in the record. |
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Phase 3 | Completed | 4894 | Adjuvant trial in node-positive breast cancer comparing TAC, dose-dense AC→P, and dose-dense AC→P plus gemcitabine. No results in the record. |
| [NCT00440622](https://clinicaltrials.gov/study/NCT00440622) | Phase 3 | Terminated | 90 | Gemcitabine + Herceptin vs capecitabine + Herceptin in pretreated HER2-positive metastatic breast cancer. |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1206 | Neoadjuvant trial adding capecitabine or gemcitabine to docetaxel before AC, with or without bevacizumab. |
| [NCT01881230](https://clinicaltrials.gov/study/NCT01881230) | Phase 2/3 | Completed | 191 | Nab-paclitaxel with gemcitabine or carboplatin vs gemcitabine/carboplatin as first-line therapy in triple-negative metastatic breast cancer. |
| [NCT00193063](https://clinicaltrials.gov/study/NCT00193063) | Phase 2 | Completed | 41 | Weekly gemcitabine plus trastuzumab in HER2-overexpressing metastatic breast cancer. Direct drug and disease match. |
| [NCT02252887](https://clinicaltrials.gov/study/NCT02252887) | Phase 2 | Completed | 45 | Gemcitabine with trastuzumab and pertuzumab in metastatic HER2-positive breast cancer after prior HER2-directed therapy. |
| [NCT00244933](https://clinicaltrials.gov/study/NCT00244933) | Phase 2 | Completed | 19 | Gemcitabine plus genistein in stage IV breast cancer. Direct match, but the sample is small. |
| [NCT01050322](https://clinicaltrials.gov/study/NCT01050322) | Phase 2 | Completed | 142 | Randomized: lapatinib with capecitabine, vinorelbine or gemcitabine in HER2-amplified metastatic breast cancer after taxanes. |
| [NCT07528768](https://clinicaltrials.gov/study/NCT07528768) | Phase 2 | Not yet recruiting | 750 | Gemcitabine vs standard first-line chemotherapy in Caribbean women of African ancestry with metastatic triple-negative breast cancer. No results yet. |

---

## Literature Evidence

The retrieved literature contains no RCT reports, so the list prioritizes clinical studies and then reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase 1 trial | Breast Cancer Res Treat | Carboplatin, gemcitabine and mifepristone in advanced breast and recurrent ovarian cancer. |
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase 1 trial | Gynecol Oncol | Mirvetuximab soravtansine plus gemcitabine in FRα-positive tumors, including triple-negative breast cancer. |
| [25398698](https://pubmed.ncbi.nlm.nih.gov/25398698/) | 2015 | Clinical study | Cancer Chemother Pharmacol | Biweekly docetaxel, gemcitabine and bevacizumab as salvage therapy in HER2-negative metastatic breast cancer. |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase 1/2 | Tumori | Weekly docetaxel and gemcitabine dose-finding in anthracycline-pretreated metastatic breast cancer. |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine plus paclitaxel: 52% (114 of 221) of patients responded in Phase II trials. |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine and platinum combinations in metastatic breast cancer showed clinical benefit and response rates. |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine plus docetaxel: different mechanisms and partly non-overlapping toxicity. |
| [12722022](https://pubmed.ncbi.nlm.nih.gov/12722022/) | 2003 | Phase 2 report | Semin Oncol | Preliminary results of gemcitabine plus trastuzumab in heavily pretreated metastatic breast cancer. |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Semin Oncol | Single-agent response rates of 16% to 37%. About 20 Phase II trials confirm activity in metastatic breast cancer. |
| [12057039](https://pubmed.ncbi.nlm.nih.gov/12057039/) | 2002 | Preclinical | Clin Breast Cancer | Gemcitabine and trastuzumab tested in breast and lung cancer cell lines. |

---

## US Market Information

Five of the 20 authorizations are shown. The approved-indication text is empty in the records provided.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA 200795 | Gemcitabine (Hospira, Inc.) | Injection, solution | Not listed in the record |
| ANDA 210383 | Gemcitabine (Ingenus Pharmaceuticals, LLC) | Injection, solution | Not listed in the record |
| NDA 209604 | Gemcitabine (Accord Healthcare Inc.) | Injection, solution | Not listed in the record |
| ANDA 091365 | Gemcitabine (Meitheal Pharmaceuticals Inc.) | Injection, powder, lyophilized, for solution | Not listed in the record |
| ANDA 202485 | Gemcitabine (Sagent Pharmaceuticals) | Injection, powder, lyophilized, for solution | Not listed in the record |

---

## Cytotoxicity

The pack contains no toxicity data. The entries below are general pharmacology and should be confirmed against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nucleoside-analog antimetabolite) |
| Myelosuppression Risk | Medium to high. Hematologic toxicity is reported with gemcitabine/carboplatin (PMID 21980041). |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Literature signals:** Significant hematologic toxicity was reported with gemcitabine/carboplatin in breast cancer (PMID 21980041). A case report describes gemcitabine-induced retinopathy (PMID 28961673).
- **Drug Interactions:** No interaction records were found in the DDI query.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Gemcitabine is already studied in breast cancer, including at least two completed Phase 3 trials and many Phase 2 trials of combination regimens. This is a confirmatory signal, not a novel one. Safety screening cannot start until the package insert data are obtained, and the trial records give no efficacy results.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap DG001)
- Mechanism of action data from DrugBank (DG002)
- Published results and outcomes for NCT00006459 and NCT00093795 to confirm that the Phase 3 evidence is positive
- Confirmed original and approved indications, since the regulatory text is empty
- A defined breast cancer setting and subtype (for example HER2-positive, triple-negative, or metastatic vs adjuvant)
- A relevance review of the ungraded ("pending") trials, to confirm the evidence level

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


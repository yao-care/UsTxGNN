---
layout: default
title: Vandetanib
parent: Moderate Evidence (L3-L4)
nav_order: 1284
evidence_level: L3
indication_count: 10
---

# Vandetanib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Vandetanib: From Medullary Thyroid Cancer to Renal Cell Carcinoma

## One-Sentence Summary

Vandetanib is an oral multi-kinase inhibitor marketed in the US as CAPRELSA. Per the cited literature, its established use is advanced medullary thyroid cancer; the input's own indication field is empty.
The TxGNN model predicts it may be effective for **Renal Cell Carcinoma (RCC)**.
This is supported by **4 registered clinical trials** (all small or early-phase, 2 of them terminated) and **6 publications**. None of the publications reports vandetanib efficacy data in RCC.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced medullary thyroid cancer (from cited literature; the approved-indication text in the regulatory data is empty) |
| Predicted New Indication | Renal cell carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license entries (both NDA022405) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed drug-level mechanism of action data is not available in the source record. Based on the cited literature, vandetanib inhibits VEGFR-2, EGFR and RET. Its efficacy in medullary thyroid cancer is established, and it can plausibly be applied to RCC through the angiogenesis pathway.

The biological link is strongest for clear cell RCC. Loss of VHL leads to HIF accumulation and VEGF overexpression, which is the core angiogenic driver of this tumor type. Several VEGFR tyrosine kinase inhibitors are already used in RCC. In a mouse RCC model, vandetanib (ZD6474) inhibited angiogenesis and changed tumor microvascular architecture (PMID 15886878).

This remains a hypothesis. Vandetanib has no efficacy data of its own in RCC, and the only RCC-focused trials are small, terminated, or have no results available in the input.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Vandetanib in von Hippel-Lindau disease with renal tumors. This is the best mechanistic and clinical match (VHL lesions are clear cell histology). No results are included in the input. |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Vandetanib in advanced clear cell renal carcinoma. Terminated after 3 patients, so it yields no usable efficacy evidence. |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib plus metformin in HLRCC/SDH-associated kidney cancer or sporadic papillary RCC. This is a rare, biologically distinct subtype, and the evidence is minimal. |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Randomized trial of carboplatin and gemcitabine with or without vandetanib in advanced urothelial cancer. It is not an RCC efficacy trial, and its relevance is low. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Preclinical/Translational | Clin Exp Metastasis | Fumarate hydratase-deficient RCC is aggressive and has no standard regimen. Several phase 2 trials of targeted combinations are under way. |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical (mouse model) | Mol Cancer Res | TFE3 Xp11.2 translocation RCC mouse model that identifies new therapeutic targets and GPNMB as a diagnostic marker. Its link to vandetanib is unverified. |
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Phase 2 trial (different drug) | Clin Cancer Res | Guadecitabine in SDH-deficient tumors, including HLRCC-associated RCC. It does not test vandetanib. |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review (nintedanib) | OncoTargets Ther | Review of anti-angiogenic agents in solid tumors. It mentions vandetanib among approved agents. |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review (cabozantinib) | Bull Cancer | Cabozantinib targets VEGFR2, c-MET and RET, and VEGFR-pathway inhibition is relevant in RCC. |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review (thyroid cancer) | ASCO Educ Book | Vandetanib is an oral RET inhibitor approved by the FDA for medullary thyroid cancer. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022405 | CAPRELSA (Genzyme Corporation) | Film-coated tablet (oral) | Not listed in the source data (the same NDA appears twice) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: VEGFR-2, EGFR, RET) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | QT prolongation is a known vandetanib risk. VEGFR-TKI class meta-analyses also flag hepatic toxicity and proteinuria, so cardiac (ECG), liver function and urine protein monitoring are worth considering. Confirm against the package insert. |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Known vandetanib risk**: QT prolongation. Long-term follow-up safety data exist in medullary thyroid cancer (PMID 32691271).
- **VEGFR-TKI class signals (meta-analyses)**: hepatic toxicity (PMID 23981115), proteinuria (PMID 32105149) and treatment-related mortality (PMID 22651902).
- **Other**: A 2012 Prescrire review (PMID 23185843) titled "too dangerous in medullary thyroid cancer" raises a tolerability concern relevant to any new use.

Package-insert warnings and contraindications were not available in the input. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RCC prediction is mechanistically plausible, but vandetanib has no usable RCC efficacy evidence. The direct trials were terminated with 3 and 7 patients, and the only completed RCC-relevant trial (VHL, n=37) has no results in the input. Package-insert safety data is also missing, which blocks safety screening. Established VEGFR-TKIs already exist for RCC, so the case for vandetanib must rest on clear differentiation.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications for CAPRELSA, to complete safety screening
- Results of NCT00566995 (VHL renal tumors, n=37) and any available data from the terminated RCC trials
- Detailed mechanism-of-action data from DrugBank
- Confirmation of the original approved indication text from the label
- A rationale for choosing vandetanib over approved VEGFR-TKIs, especially given the QT risk

Other RCC-related predictions are weaker. Clear cell RCC and umbrella "renal carcinoma" are at L3 with the same trials. Unclassified RCC, RCC associated with neuroblastoma, TFE3-fusion RCC and childhood kidney carcinoma are L5 model predictions only. Renal pelvis carcinoma is L4. Angiolipoma and familial spontaneous pneumothorax are likely knowledge-graph artifacts with no therapeutic rationale.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


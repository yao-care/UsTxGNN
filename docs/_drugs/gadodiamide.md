---
layout: default
title: Gadodiamide
parent: 僅模型預測 (L5)
nav_order: 743
evidence_level: L5
indication_count: 2
---

# Gadodiamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Gadodiamide: From MRI Contrast Imaging to Rheumatoid Arthritis

## One-Sentence Summary

Gadodiamide (DrugBank DB00225) is a gadolinium-based paramagnetic contrast agent used to enhance MRI imaging; it is not currently marketed in Taiwan and has no on-file therapeutic indication.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this is supported by **0 clinical trials** and **10 publications**, all of which describe using gadodiamide as an imaging tool to visualize joint inflammation — not as a treatment.
The drug's own repurposing rationale flags this as a likely false positive: the model appears to have mistaken "used diagnostically in RA patients" for "treats RA."

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no Taiwan license records exist; publicly known globally as an MRI contrast agent (not a therapeutic drug) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for gadodiamide from the standard data sources queried. Based on known information, gadodiamide is a gadolinium-based paramagnetic MRI contrast agent — its pharmacological action is to shorten proton T1 relaxation time to enhance image contrast. It has no known anti-inflammatory, immunomodulatory, or synovial-pathology-related pharmacology.

The literature link to rheumatoid arthritis comes entirely from a diagnostic context: contrast-enhanced MRI is a well-established method for visualizing synovitis and pannus in RA patients, so gadodiamide co-occurs frequently with RA in the literature simply because it is the imaging agent used to *study* the disease, not to *treat* it.

Given this, the evidence pack's own assessment concludes there is no credible mechanistic basis for a treatment hypothesis, and classifies this as a likely case of the TxGNN model conflating "diagnostic co-occurrence" with "therapeutic association." The same reasoning applies to the second-ranked candidate, osteoarthritis susceptibility, which has no supporting literature or trials at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17935920](https://pubmed.ncbi.nlm.nih.gov/17935920/) | 2009 | Methodology/Imaging | European journal of radiology | Distribution pattern of ultrasound-guided intra-articular injection in RA wrist joints |
| [18286282](https://pubmed.ncbi.nlm.nih.gov/18286282/) | 2008 | Diagnostic imaging | Skeletal radiology | Contrast-enhanced MRI analysis of hands/wrists in psoriatic arthritis |
| [17289759](https://pubmed.ncbi.nlm.nih.gov/17289759/) | 2008 | Diagnostic imaging | Annals of the rheumatic diseases | MRI and bone scintigraphy for differential diagnosis of unclassified arthritis |
| [17340197](https://pubmed.ncbi.nlm.nih.gov/17340197/) | 2007 | Methodology | Annals of biomedical engineering | Kinetic modeling of contrast-enhanced MRI to assess RA wrist inflammation |
| [11454641](https://pubmed.ncbi.nlm.nih.gov/11454641/) | 2001 | Diagnostic imaging | Annals of the rheumatic diseases | Low-field dedicated MRI in untreated recent-onset RA |
| [11976868](https://pubmed.ncbi.nlm.nih.gov/11976868/) | 2002 | Diagnostic imaging | European radiology | MRI features predicting bone erosion progression at 1-year follow-up |
| [11669155](https://pubmed.ncbi.nlm.nih.gov/11669155/) | 2001 | Diagnostic imaging | The Journal of rheumatology | MRI of wrist/finger joints across inflammatory joint disease groups |
| [11419149](https://pubmed.ncbi.nlm.nih.gov/11419149/) | 2001 | Methodology | European radiology | Comparison of low-field extremity MRI vs high-field MRI in arthritic small joints |
| [11868082](https://pubmed.ncbi.nlm.nih.gov/11868082/) | 2002 | Methodology | European radiology | Synovial membrane volume: manual vs stereologic MRI measurement methods |
| [11274835](https://pubmed.ncbi.nlm.nih.gov/11274835/) | 2001 | Diagnostic imaging | European journal of radiology | Gadolinium enhancement patterns at atlantoaxial joints in normal subjects |

**Note:** All 10 publications describe gadodiamide-enhanced MRI as an imaging/diagnostic tool for assessing joint disease — none evaluate gadodiamide as a therapeutic agent for RA.

---

## US Market Information

Not currently marketed in Taiwan — no license records on file (0 NDAs).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic basis, no clinical trial evidence, and no treatment-related literature supporting gadodiamide as a therapy for rheumatoid arthritis — all identified literature reflects its use as an imaging contrast agent, not a drug candidate. The second candidate (osteoarthritis susceptibility) is even weaker, with zero supporting trials or publications. Both should be treated as likely false-positive predictions arising from diagnostic co-occurrence in the underlying knowledge graph rather than genuine drug-repurposing signals.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) — currently blocking even a baseline safety review
- Confirmed mechanism of action data from DrugBank
- Independent pharmacological rationale for any anti-inflammatory or immunomodulatory activity, if this candidate is to be pursued further
- Given the diagnostic-vs-therapeutic confound identified here, consider flagging this candidate type (imaging/diagnostic agents predicted against disease-with-imaging-literature) for automatic down-weighting in future TxGNN evidence packs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


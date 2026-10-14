---
layout: default
title: Fludrocortisone
parent: Model Prediction Only (L5)
nav_order: 716
evidence_level: L5
indication_count: 8
---

# Fludrocortisone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Fludrocortisone: From Mineralocorticoid Replacement to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

> Fludrocortisone is a synthetic corticosteroid with predominantly mineralocorticoid activity. The data compiled for this report do not include its original approved indication text.
> The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (approved indication text is blank in all US licenses) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 (all ANDA generic applications, all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known pharmacology, fludrocortisone is a corticosteroid dominated by mineralocorticoid effects, with some glucocorticoid activity.

Glucocorticoids can induce apoptosis in lymphoid cells, and topical corticosteroids are used in early-stage cutaneous T-cell lymphoma. This offers a loose conceptual link. However, fludrocortisone's activity is mainly mineralocorticoid, and no data connect it to this disease. The high TxGNN score is a prediction only and has no clinical or literature support.

Other top-ranked predictions (cystic teratoma, spinal cord dermoid cyst, dermoid cyst of ovary, exostosis) have no plausible mechanistic rationale and likely reflect knowledge-graph topology artifacts. The broad "eye disease" prediction has only limited preclinical support (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for primary cutaneous T-cell lymphoma.

None of the eight predicted indications has registered clinical trials in the compiled data.

---

## Literature Evidence

Currently no related literature available for primary cutaneous T-cell lymphoma.

For reference, the only prediction with literature was the broad category "eye disease" (rank 6). The most relevant items are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34509498](https://pubmed.ncbi.nlm.nih.gov/34509498/) | 2021 | Preclinical study | Experimental Eye Research | Fludrocortisone showed anti-inflammatory and neuroprotective effects on Müller cell cytokine responses in retinal degeneration models |
| [36161841](https://pubmed.ncbi.nlm.nih.gov/36161841/) | 2022 | Phase 1B study | BMJ Open Ophthalmology | Safety and tolerability of single-dose intravitreal fludrocortisone acetate (1 mg and 2 mg) in geographic atrophy secondary to AMD |
| [11008895](https://pubmed.ncbi.nlm.nih.gov/11008895/) | 1999 | Clinical study | International Ophthalmology | Hemodynamic effects of fludrocortisone for systemic hypotension in primary open-angle glaucoma patients |
| [17998043](https://pubmed.ncbi.nlm.nih.gov/17998043/) | 2007 | Review | Survey of Ophthalmology | Discusses non-IOP-lowering glaucoma approaches, including fludrocortisone to avoid blood pressure dips |
| [23430676](https://pubmed.ncbi.nlm.nih.gov/23430676/) | 2013 | Review | Klinische Monatsblätter für Augenheilkunde | Non-IOP-lowering glaucoma therapy, including fludrocortisone and salt |
| [25354755](https://pubmed.ncbi.nlm.nih.gov/25354755/) | 2015 | Diagnostic study | Rheumatology (Oxford) | Furosemide plus fludrocortisone urinary acidification test for distal renal tubular acidosis in Sjögren's syndrome |

Most other retrieved papers concern orthostatic hypotension, adrenal insufficiency, or systemic conditions with ocular associations, so they are indirect evidence.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040431 | Fludrocortisone Acetate (NCS HealthCare of KY, Vangard Labs) | Tablet | Not available (cancelled) |
| ANDA215279 | Fludrocortisone Acetate (Novitium Pharma) | Tablet | Not available (cancelled) |
| ANDA219251 | Fludrocortisone Acetate (Viona Pharmaceuticals) | Tablet | Not available (cancelled) |
| ANDA040425 | Fludrocortisone Acetate (Bryant Ranch Prepack) | Tablet | Not available (cancelled) |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified; the 20 listed in the compiled data are mostly Moderate. One is Major:
  - **Bupropion** (Major)
  - Moderate examples include antidiabetic agents (acarbose, pioglitazone, alogliptin, linagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, and GLP-1 agonists such as albiglutide and dulaglutide), amphotericin B, aspirin, clarithromycin, aprepitant, anabolic steroids (oxandrolone, oxymetholone), and laxatives (bisacodyl, picosulfuric acid).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by a model score, with no clinical trials or literature (Evidence Level L5). The mechanistic link is weak, because the drug is mainly mineralocorticoid. The US market status is "Cancelled only", and key label safety data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data
- Any mechanistic or preclinical evidence for fludrocortisone in cutaneous T-cell lymphoma
- Comparison with established corticosteroids and standard therapies for this disease
- Optional research direction: the ocular signal (retinal degeneration/geographic atrophy, PMIDs 34509498 and 36161841) is a more evidence-backed research question than the top-ranked prediction, though "eye disease" is too broad to be an indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Gadodiamide
parent: Model Prediction Only (L5)
nav_order: 743
evidence_level: L5
indication_count: 2
---

# Gadodiamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Gadodiamide: From MRI Contrast Imaging to Rheumatoid Arthritis

## One-Sentence Summary

Gadodiamide is a gadolinium-based contrast agent marketed in the US as OMNISCAN and used as a diagnostic imaging agent, not a treatment.
The TxGNN model predicts it may be relevant to **rheumatoid arthritis**, but there are **0 clinical trials** and **10 publications**, all of which use it to visualize joint inflammation on MRI rather than to treat disease.
This looks like a knowledge-graph artifact, not a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the record; gadodiamide is a diagnostic MRI contrast agent, not a therapy |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 for therapeutic use (the 10 papers are diagnostic imaging studies only; the source pack labels this L4) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Gadodiamide is a gadolinium-based contrast agent injected to enhance MRI images. It has no known disease-modifying mechanism.

The link to rheumatoid arthritis appears to come from imaging. In the linked papers, contrast-enhanced MRI is used to see inflamed synovium (the joint lining), bone marrow oedema and erosions in the wrist and finger joints. None of them reports that the drug improves RA. The high TxGNN score most likely reflects that the drug and disease frequently appear together in the literature, not a therapeutic relationship.

The second prediction, **osteoarthritis susceptibility** (score 99.11%), has no trials or publications at all. It is a susceptibility phenotype rather than a treatable condition, so it is even less plausible.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17935920](https://pubmed.ncbi.nlm.nih.gov/17935920/) | 2009 | Diagnostic imaging study | Eur J Radiol | Used contrast to assess how ultrasound-guided injections distribute within the wrist joint in RA patients |
| [18286282](https://pubmed.ncbi.nlm.nih.gov/18286282/) | 2008 | Diagnostic imaging study | Skeletal Radiol | Detailed contrast-enhanced MRI analysis of hand and wrist soft tissue, tendons, joints and bone in psoriatic arthritis (not RA) |
| [17289759](https://pubmed.ncbi.nlm.nih.gov/17289759/) | 2008 | Diagnostic imaging study | Ann Rheum Dis | Assessed the value of hand MRI and bone scintigraphy for differential diagnosis of unclassified arthritis |
| [17340197](https://pubmed.ncbi.nlm.nih.gov/17340197/) | 2007 | Imaging methods study | Ann Biomed Eng | Kinetic modeling of contrast-enhanced MRI as an automated way to assess inflammation in the RA wrist |
| [11976868](https://pubmed.ncbi.nlm.nih.gov/11976868/) | 2002 | Diagnostic imaging cohort | Eur Radiol | 84 patients with inflammatory joint disease; tested whether MRI synovial volume and bone marrow oedema predict bone erosion progression at 1 year |
| [11868082](https://pubmed.ncbi.nlm.nih.gov/11868082/) | 2002 | Imaging methods comparison | Eur Radiol | Compared stereological and manual measurement of synovial volume on post-contrast finger-joint MRI |
| [11454641](https://pubmed.ncbi.nlm.nih.gov/11454641/) | 2001 | Diagnostic imaging study | Ann Rheum Dis | Compared low-field extremity MRI with X-ray and clinical exam for inflammation and erosions in untreated early RA |
| [11669155](https://pubmed.ncbi.nlm.nih.gov/11669155/) | 2001 | Diagnostic imaging study | J Rheumatol | Described MRI features of wrist and finger joints across early RA, established RA, other arthritis and arthralgia |
| [11419149](https://pubmed.ncbi.nlm.nih.gov/11419149/) | 2001 | Diagnostic imaging comparison | Eur Radiol | 103 patients; compared 0.2 T extremity MRI with 1.5 T high-field MRI in arthritic small joints, including patient acceptance |
| [11274835](https://pubmed.ncbi.nlm.nih.gov/11274835/) | 2001 | Imaging study in normal subjects | Eur J Radiol | Described normal gadolinium enhancement patterns of the atlantoaxial joints in healthy volunteers |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020123 | OMNISCAN (GE Healthcare Inc.) | Injection | Not specified in the record |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Gadodiamide is a diagnostic imaging agent with no known therapeutic mechanism. All 10 linked papers use it to visualize joint inflammation, none reports a treatment effect, and there are no clinical trials. The TxGNN score is high, but it is best read as a knowledge-graph artifact, not a real repurposing signal.

**To proceed, the following is needed:**
- Any evidence of a therapeutic effect (preclinical or clinical), not diagnostic use
- Mechanism of action data, to test whether a plausible therapeutic link exists
- The FDA package insert (warnings and contraindications), which is required before any safety screening
- The approved indication text for NDA020123, to confirm the original use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Gadodiamide
parent: Moderate Evidence (L3-L4)
nav_order: 743
evidence_level: L4
indication_count: 2
---

# Gadodiamide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Gadodiamide: From Contrast-Enhanced MRI Imaging to Rheumatoid Arthritis

## One-Sentence Summary

Gadodiamide is a gadolinium-based contrast agent for magnetic resonance imaging (MRI), marketed in the US as OMNISCAN.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but there are **0 clinical trials** and only **3 publications**, all of which use the drug as an imaging aid rather than as a treatment.
This prediction is most likely a computational artifact and is not supported as a therapeutic direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (a diagnostic MRI contrast agent) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no active license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Gadodiamide is a gadolinium-based MRI contrast agent. It enhances image contrast and has no known therapeutic target or anti-inflammatory activity.

The three retrieved publications used gadolinium-enhanced MRI to visualize inflamed joints in rheumatoid arthritis and other inflammatory joint diseases, for example to assess synovitis and predict bone erosions. They support a **diagnostic or imaging-assessment role**, not treatment of the disease.

The high TxGNN score (0.99) probably reflects network associations in the knowledge graph (the drug appears frequently alongside rheumatoid arthritis in imaging studies), not a pharmacological effect. No disease-modifying mechanism is supported. The model also ranked a second prediction, "osteoarthritis susceptibility" (score 99.11%), which has no trials or literature and is a susceptibility phenotype rather than a treatable disease, so it is likely a knowledge-graph artifact as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11669155](https://pubmed.ncbi.nlm.nih.gov/11669155/) | 2001 | Cohort (diagnostic imaging) | The Journal of Rheumatology | MRI features of wrist and finger joints compared across early RA, established RA, other arthritis and arthralgia |
| [11976868](https://pubmed.ncbi.nlm.nih.gov/11976868/) | 2002 | Cohort (longitudinal imaging) | European Radiology | In 84 patients, MRI synovial volume and bone marrow oedema were assessed for predicting bone erosion progression at 1 year |
| [11419149](https://pubmed.ncbi.nlm.nih.gov/11419149/) | 2001 | Comparative imaging study | European Radiology | Low-field extremity MRI (0.2 T) compared with high-field MRI (1.5 T) in 103 patients with arthritic small joints, including patient acceptance |

All three studies concern imaging diagnosis, not therapeutic efficacy.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020123 | OMNISCAN (GE Healthcare Inc.) | Injection | Not listed (license status: cancelled) |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. Most are of unknown severity, and one is rated Moderate (acebutolol). Others listed include calcitriol, pantoprazole, omeprazole, vancomycin, prednisone, simvastatin and dexamethasone. The clinical significance of these entries is not established.
- **Class-level concern**: Gadolinium retention and nephrogenic systemic fibrosis risk are known concerns for gadolinium-based agents and would weigh heavily against any chronic therapeutic use.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Gadodiamide is a diagnostic contrast agent with no known therapeutic mechanism. The available literature supports only an imaging role in rheumatoid arthritis, there are no clinical trials, and the license is cancelled. The high TxGNN score is probably a knowledge-graph artifact.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, and any evidence of a therapeutic pharmacological effect in inflammatory arthritis
- Preclinical evidence of anti-inflammatory or disease-modifying activity
- A risk assessment of gadolinium retention and nephrogenic systemic fibrosis for any therapeutic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Iohexol
parent: Model Prediction Only (L5)
nav_order: 805
evidence_level: L5
indication_count: 2
---

# Iohexol
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

# Iohexol: From Radiographic Contrast Imaging to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic, iodinated radiographic contrast agent used for diagnostic imaging.
The TxGNN model predicts it may be effective for **insomnia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction with no supporting evidence, and the mechanistic rationale is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available U.S. license records (iohexol is generally used as a radiographic contrast agent) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iohexol is a non-ionic, iodinated contrast agent. It is considered pharmacologically inert and has no known activity on sleep-regulating pathways such as GABAergic, orexinergic, melatonergic or histaminergic signalling.

There is no clear relationship between its original use (imaging) and insomnia. The very high TxGNN score (99.87%) is a knowledge-graph prediction only. It is not supported by any clinical trial or publication, and it likely reflects network artifacts, such as the large number of drug-drug interaction relationships (100 recorded), rather than a true pharmacological effect.

A second prediction, **anxiety** (score 99.25%), shows the same pattern. The retrieved publications deal with iohexol as a contrast agent, and anxiety appears only as a procedural or side-effect context, not as a therapeutic target.

## Clinical Trial Evidence

Currently no related clinical trials registered for insomnia (or for the second prediction, anxiety).

## Literature Evidence

No related literature is available for insomnia.

For the second predicted indication (anxiety), four publications were retrieved. None shows therapeutic benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/) | 1996 | RCT | Academic Radiology | Double-blind comparison of iodixanol vs iohexol in extremity phlebography (efficacy, safety, injection discomfort); not relevant to anxiety treatment |
| [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/) | 1990 | Observational | Neuroradiology | Side effects (headache, nausea, dizziness, minor mental symptoms such as anxiety or depression) after lumbar iohexol myelography in 200 patients |
| [2125805](https://pubmed.ncbi.nlm.nih.gov/2125805/) | 1990 | Clinical physiological study | Acta Neurochirurgica | Cerebral haemodynamics during angiography monitored by transcranial Doppler; not relevant to anxiety treatment |
| [39861464](https://pubmed.ncbi.nlm.nih.gov/39861464/) | 2025 | Observational / Review | Nutrients | Nutrition and physical activity in onco-nephrology; not relevant to iohexol or anxiety treatment |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018956 | OMNIPAQUE (GE Healthcare Inc.) | Injection, solution | Not stated; status: cancelled |
| ANDA217737 | Iohexol (Amneal Pharmaceuticals Private Limited) | Injection, solution | Not stated; status: cancelled |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded, and most of those listed are rated Major. Examples include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
  - Metformin
  - Amphotericin B (including the lipid complex formulation)
  - Aminoglycosides and glycopeptides: vancomycin, kanamycin, neomycin
  - Levofloxacin
  - Bupropion
  - Metoclopramide
  - Morphine
  - Mesalazine and balsalazide
  - Appetite suppressants and related agents: phentermine, diethylpropion, dronabinol
  - Mannitol is rated Moderate.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions (insomnia and anxiety) are supported only by the TxGNN model score. There are no clinical trials, no relevant literature and no plausible pharmacological mechanism. The drug has no currently valid U.S. license, and key safety and mechanism data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (needed for any safety screening)
- Mechanism of action data, to test whether any biologically plausible link to sleep or anxiety pathways exists
- Any preclinical or clinical signal for insomnia, otherwise the prediction should be treated as a likely knowledge-graph artifact
- Clarification of the original approved indication, since the license records contain none
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


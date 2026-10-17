---
layout: default
title: Ioversol
parent: Model Prediction Only (L5)
nav_order: 807
evidence_level: L5
indication_count: 10
monitor_inn: "IOVERSOL"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
last_modified_at: 2026-10-14
description: "Ioversol: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not stated in the data compiled for this report (ioversol is an iodin…"
---

# Ioversol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Ioversol: From Radiographic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Ioversol is an iodinated radiographic contrast agent given by injection, sold in the US as Optiray.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility**, but **no clinical trials** and **no directly relevant publications** support this prediction.
The result is a graph-based prediction with no mechanistic or clinical backing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (ioversol is an iodinated contrast agent for diagnostic imaging) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorization) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ioversol is an iodinated radiographic contrast agent. It makes tissues visible on imaging and has no known disease-modifying pharmacology.

Honestly, this prediction is not well supported. "Osteoarthritis susceptibility" describes a genetic risk concept rather than a treatable clinical condition, and a contrast agent has no plausible way to act on it. The high TxGNN score (99.67%) most likely reflects proximity in the knowledge graph rather than a real biological link.

The related prediction of **osteoarthritis** itself is also weak. The only literature found is a trial of genicular artery embolization for knee osteoarthritis using an iodinated oil-based embolic (Lipiodol). Ioversol would at most appear as an imaging contrast agent during such a procedure. That is a procedural association, not evidence that ioversol treats the disease.

Other top-ranked predictions include rheumatoid arthritis, brachyolmia, hemoglobinopathy, acromesomelic dysplasia, myosclerosis and alopecia. None has a plausible mechanism or clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for osteoarthritis susceptibility. The publication below was found for the closely related prediction of osteoarthritis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Clinical trial (single-arm, interventional procedure) | Diagnostic and Interventional Imaging | LipioJoint-1 trial: safety and efficacy of transient genicular artery embolization using an ethiodized oil-based emulsion for knee osteoarthritis. It does not test ioversol as a therapy, so it is indirect evidence at best. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019710 (cancelled) | Optiray | Injection | Not listed in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interactions in total. The main ones rated Major are:
  - Metformin
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Aminoglycosides: kanamycin, neomycin, streptomycin
  - Vancomycin
  - Polymyxin B
  - Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine
  - Mannitol is rated Moderate.

  Several of these (such as aminoglycosides, amphotericin B, polymyxin B and vancomycin) are nephrotoxic agents. Metformin is also a concern with iodinated contrast because of kidney function. Interactions with atropine, famotidine, acetylsalicylic acid, morphine and omeprazole are rated Unknown.

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no clinical trials, no direct literature, and no plausible mechanism for a contrast agent to treat osteoarthritis susceptibility or any other top-ranked condition. The only US authorization is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking ioversol to the target condition
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Direct preclinical or clinical evidence of therapeutic effect, not just use as an imaging agent
- Reconsideration of whether "susceptibility" is a suitable treatment target, or evaluation of a different predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


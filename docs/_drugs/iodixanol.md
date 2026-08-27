---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 804
evidence_level: L5
indication_count: 3
---

# Iodixanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Iodixanol: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iodixanol is a non-ionic, iso-osmolar iodinated contrast medium used for diagnostic imaging, with no marketed therapeutic indication on record in this dataset. The TxGNN model predicts a possible link to **Osteoarthritis Susceptibility**, but this top-ranked prediction currently has **zero supporting clinical trials and zero literature citations**, and the only literature found for closely related terms (osteoarthritis, rheumatoid arthritis) describes iodixanol's use *as an imaging/research tool*, not as a therapeutic agent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not a therapeutic indication — iodixanol is a non-ionic, iso-osmolar iodinated radiographic contrast agent used for diagnostic imaging; no approved/marketed indication is on record |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for iodixanol is not available (blocking data gap). Based on known information, iodixanol is a contrast medium — its pharmacology is limited to physicochemical properties (iso-osmolality, non-ionic dimer structure) that make it visible on CT/radiographic imaging; it has no known receptor, enzyme, or pathway target relevant to disease treatment.

Reviewing the actual evidence attached to this candidate makes the prediction's basis clear: the literature returned under "osteoarthritis" (7 papers, see below) is entirely composed of imaging and biomechanics studies that use iodixanol as a diffusible tracer to study cartilage permeability and joint imaging technique — not studies testing iodixanol as a treatment for osteoarthritis. Similarly, the single paper under "rheumatoid arthritis" is a case report about desensitization to a *different* contrast agent (iohexol) in a patient who happened to have RA-related amyloidosis, again unrelated to therapeutic use.

This pattern strongly suggests the TxGNN score reflects **knowledge-graph co-occurrence** (iodixanol frequently appears alongside "cartilage" and "osteoarthritis" in imaging-research contexts) rather than a genuine treat-relationship. For the top-ranked prediction, "osteoarthritis susceptibility," there is no evidence at all — not even this kind of indirect, non-therapeutic literature — making it the weakest of the three ranked candidates in this evidence pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction (osteoarthritis susceptibility).

### Related Predictions (Context Only — Not Therapeutic Evidence)

The evidence pack also scored two closely related terms, both with the same L5/Hold status. Their literature is included here for transparency, since it explains the apparent knowledge-graph signal:

**Osteoarthritis** (TxGNN score 99.07%, rank 20119) — 7 papers, all describing iodixanol as an imaging/research reagent, not a treatment:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Imaging/Technical | Annals of Biomedical Engineering | Dual-contrast photon-counting CT for assessing articular cartilage health |
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Imaging/Technical | Annals of Biomedical Engineering | Nanoparticle diffusion CT/finite element study of cartilage function |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Ex vivo biomechanics | Journal of Biomechanics | Uses iodixanol (~1550 Da) as a neutral diffusing CT contrast agent to study osteochondral interface permeability |
| [28518064](https://pubmed.ncbi.nlm.nih.gov/28518064/) | 2017 | Ex vivo biomechanics | Journal of Visualized Experiments | Protocol for tracking neutral/charged solute transport across cartilage |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Ex vivo biomechanics | Journal of Biomechanics | Finite element model of solute transport across the osteochondral interface |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro | Journal of Experimental Orthopaedics | Iodine contrast agents do not affect platelet-rich plasma function in vitro |
| [30145230](https://pubmed.ncbi.nlm.nih.gov/30145230/) | 2018 | Animal ex vivo biomechanics | Osteoarthritis and Cartilage | Aging effects on mandibular condylar cartilage stiffness (uses contrast-based diffusion imaging) |

**Rheumatoid arthritis** (TxGNN score 99.00%, rank 21444) — 1 paper, unrelated to treatment:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/) | 2022 | Case report | Cureus | Desensitization to contrast agent iohexol (not iodixanol) in a patient with RA-related amyloidosis; concerns contrast allergy management, not RA therapy |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data for iodixanol were not available in this dataset — TFDA label data is a blocking gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three ranked predictions (osteoarthritis susceptibility, osteoarthritis, rheumatoid arthritis) are Evidence Level L5 with no clinical trials and no therapeutic-use literature. The available literature indicates iodixanol's association with these disease terms stems from its use as an imaging/research contrast agent, not from any demonstrated therapeutic effect — there is currently no biological plausibility supporting repurposing.

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Any preclinical or pharmacological studies testing iodixanol as a therapeutic (not diagnostic) agent in osteoarthritis or rheumatoid arthritis
- Re-evaluation of the TxGNN prediction methodology to filter out non-therapeutic co-occurrence signals (e.g., drug-as-research-tool literature) for contrast media and similar diagnostic agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


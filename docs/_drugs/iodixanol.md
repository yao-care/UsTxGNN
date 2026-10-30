---
layout: default
title: Iodixanol
parent: Model Prediction Only (L5)
nav_order: 804
evidence_level: L5
indication_count: 2
monitor_inn: "IODIXANOL"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-10-30
description: "Iodixanol: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not available"
---

# Iodixanol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Iodixanol: From Radiographic Contrast Imaging to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Iodixanol is an iodinated, non-ionic, iso-osmolar contrast agent used in diagnostic radiographic imaging. The TxGNN model predicts it may be effective for **osteoarthritis**, but the data compiled for this report contain **0 clinical trials** and **5 publications**, none of which test a therapeutic effect. The publications describe iodixanol as an imaging or research tool for cartilage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the US licence records contain no approved-indication text) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9907 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of FDA Applications | 2 (valid: 2) |
| Number of approvals | 1 NDA and 1 ANDA |
| Recommended Decision | Hold |

*Evidence level note:* the cited studies use iodixanol as an imaging or transport probe in cartilage. None evaluates it as a treatment for osteoarthritis, so the level is capped at L5 and not the L4 label shown in the source data.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available. Iodixanol is understood to be a non-ionic, iso-osmolar iodinated contrast agent. It has no known disease-modifying pharmacology.

The retrieved literature concerns its use as a diagnostic or research tool:
- contrast-enhanced CT of articular cartilage
- diffusion and solute transport across the cartilage and subchondral bone interface
- an in vitro check that iodine contrast agents do not impair platelet-rich plasma function

These findings support a diagnostic role in joint imaging. They do not support a therapeutic effect on osteoarthritis. The high TxGNN score most likely reflects network proximity, such as shared use in joint imaging contexts, and not a plausible treatment mechanism. The same applies to the second-ranked prediction, rheumatoid arthritis (score 0.9900). Its only retrieved publication is a case report on desensitization to a different contrast agent (iohexol), and no mechanistic rationale links iodixanol to that disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Preclinical imaging study | Ann Biomed Eng | Nanoparticle diffusion CT with finite element modelling used to reveal cartilage function |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Preclinical imaging study | Ann Biomed Eng | Dual-contrast agent in photon-counting CT to assess articular cartilage health |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Ex vivo / computational study | J Biomech | Iodixanol used as a diffusing CT contrast agent to study permeability of the cartilage and subchondral bone interface |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Computational model | J Biomech | Finite element model of neutral solute transport across the osteochondral interface |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro study | J Exp Orthop | Iodine contrast agents did not affect platelet-rich plasma function at an early time point |

Literature for the second prediction (rheumatoid arthritis): [36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/) (2022, Cureus) is a case report of desensitization to iohexol in a patient with rheumatoid arthritis-related amyloidosis. It is unrelated to treatment of the disease.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA214271 | Iodixanol (Fresenius Kabi USA, LLC) | Injection, solution | Not listed in the compiled records |
| NDA020351 | Visipaque (GE Healthcare Inc.) | Injection, solution | Not listed in the compiled records |

---

## Safety Considerations

The compiled data contain no label warnings or contraindications. Please refer to the package insert for safety information.

**Drug Interactions:** the interaction query returned 100 records. The main ones are listed below.
- **Major:** metformin, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, and the aminoglycosides and polymyxins kanamycin, neomycin, streptomycin and polymyxin B
- **Moderate:** mannitol

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Iodixanol has no known therapeutic mechanism in osteoarthritis. No clinical trials exist, and the available publications only use it as an imaging or research tool. The high TxGNN score is not backed by biological or clinical evidence.

**To proceed, the following is needed:**
- A plausible therapeutic mechanism for osteoarthritis, with mechanism of action data
- Preclinical or clinical studies that test iodixanol as a treatment, not as an imaging agent
- The FDA package insert warnings and contraindications, which are currently missing
- A review of the major interactions, particularly with nephrotoxic drugs and metformin, if any therapeutic use is explored
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


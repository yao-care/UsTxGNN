---
layout: default
title: Iodixanol
parent: Model Prediction Only (L5)
nav_order: 804
evidence_level: L5
indication_count: 3
monitor_inn: "IODIXANOL"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-10-14
description: "Iodixanol: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not available"
---

# Iodixanol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Iodixanol: From Diagnostic Imaging Contrast Agent to Osteoarthritis Susceptibility
{: .text-alpha }

## One-Sentence Summary

Iodixanol is an iodinated contrast agent used in diagnostic imaging; the data compiled for this report do not list a specific approved indication text.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility** (top-ranked), with **0 clinical trials** and **0 publications** supporting this specific prediction.
The next two predictions, osteoarthritis and rheumatoid arthritis, have only imaging-method or unrelated case-report literature, with no therapeutic evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the approved indication text on the listed licenses is empty) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, iodixanol is an iodinated, iso-osmolar contrast agent used for imaging, not a drug with known disease-modifying activity.

The top prediction, "osteoarthritis susceptibility", is a genetic susceptibility phenotype rather than a treatable disease state. No mechanistic link is supported by the data, so the high score (99.16%) should be interpreted cautiously.

For the closely related prediction of **osteoarthritis** (score 99.07%), the literature connects iodixanol only to imaging. Contrast-enhanced CT is used to study solute transport and diffusion in cartilage. The score likely reflects frequent co-occurrence with joint and cartilage imaging studies, not a therapeutic effect. For **rheumatoid arthritis** (score 99.00%), the only retrieved paper is a hypersensitivity desensitization case report for a different contrast agent (iohexol).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top-ranked prediction (osteoarthritis susceptibility). The following publications relate to the second prediction, osteoarthritis, and are all methodological or in vitro studies:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Imaging methodology study | Annals of Biomedical Engineering | CT nanoparticle diffusion imaging combined with finite element modeling to reveal cartilage function |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Computational modeling | Journal of Biomechanics | Finite element model of neutral solute transport across the cartilage–subchondral bone interface using CT |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Imaging methodology study | Annals of Biomedical Engineering | Dual-contrast agent photon-counting CT for assessing articular cartilage health |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Biophysical study | Journal of Biomechanics | Iodixanol (~1550 Da) used as a CT contrast agent to study permeability of the osteochondral interface |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro study | Journal of Experimental Orthopaedics | Iodine contrast agents did not affect platelet-rich plasma function at an early time point |

For rheumatoid arthritis, one case report exists ([36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/), 2022, Cureus), describing desensitization to iohexol in a patient with amyloidosis secondary to rheumatoid arthritis. It concerns hypersensitivity management with a different agent and is not evidence of efficacy.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA214271 | Iodixanol (Fresenius Kabi USA, LLC) | Injection, solution | Not available (status: cancelled) |
| NDA020351 | Visipaque (GE Healthcare Inc.) | Injection, solution | Not available (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. Most listed interactions are rated **Major**, including metformin, several amphotericin B formulations, vancomycin, and the aminoglycosides and related antibiotics kanamycin, neomycin, streptomycin and polymyxin B. Mesalazine, balsalazide, olsalazine and sulfasalazine are also rated Major. Mannitol is rated Moderate. Famotidine, acetylsalicylic acid, morphine, omeprazole and prednisone have an unknown severity level. Many of these pairings involve nephrotoxic or renally cleared drugs, so kidney function monitoring is a likely concern.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predictions (osteoarthritis susceptibility, osteoarthritis, rheumatoid arthritis) are supported only by model scores. Iodixanol appears in the literature as an imaging tool, not as a therapy, and no clinical trials exist. The top-ranked prediction is a susceptibility phenotype, not a treatable condition. In addition, all US licenses are cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Any preclinical or clinical evidence that iodixanol has a therapeutic effect in a joint disease, such as cartilage protection, pain relief or functional benefit
- Clarification of the current US regulatory and supply status, given that both licenses are cancelled
- A review of whether a high-scoring prediction that reflects imaging co-occurrence should be excluded from further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


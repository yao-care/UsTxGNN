---
layout: default
title: Filgrastim
parent: Model Prediction Only (L5)
nav_order: 707
evidence_level: L5
indication_count: 10
monitor_inn: "FILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "fetal and neonatal alloimmune thrombocytopenia", "platelet-type bleeding disorder"]
last_modified_at: 2026-10-30
description: "Filgrastim: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Not recorded in the local data"
---

# Filgrastim
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

## Filgrastim: Primary release disorder of platelets
{: .text-alpha }

## One-Sentence Summary

Filgrastim (a recombinant G-CSF) was originally used to treat neutropenia conditions, including constitutional neutropenia, severe congenital neutropenia, cyclic hematopoiesis, and chronic familial neutropenia.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this is a computational prediction only. **No clinical trials or publications** directly support it, and the mechanistic rationale is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 6) |
| Number of FDA Applications | 6 (all are BLAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Based on known pharmacology, filgrastim is a granulocyte colony-stimulating factor (G-CSF). It acts on the G-CSF receptor of the neutrophil lineage to promote neutrophil production, which is why it suits neutropenic conditions.

The predicted indication is a different kind of problem. Platelet release disorders are intrinsic platelet functional defects, and G-CSF would not be expected to correct them. The high TxGNN score is therefore best read as a computational association, not a biologically grounded signal. The other top-ranked predictions show the same pattern:

- Pseudo-von Willebrand disease (GPIb-alpha gain of function)
- Glanzmann thrombasthenia (integrin αIIbβ3 defect)
- Scott syndrome (TMEM16F/ANO6 defect)
- Collagen receptor defects
- C1 inhibitor deficiency
- Serpinopathies
- Fetal and neonatal alloimmune thrombocytopenia (antibody-mediated destruction)

None has an established link to G-CSF signaling. Only constitutional thrombocytopenia has a conceivable indirect overlap through hematopoietic stem cell mobilization, and even that has no direct evidence.

## Clinical Trial Evidence

No trials are registered for the top-ranked indication. The data compiled for this report links 7 trials to the lower-ranked prediction "platelet-type bleeding disorder" (score 0.9969). All are stem cell transplant studies in hematologic malignancies, where filgrastim is likely a supportive or mobilization component. None tests filgrastim as a treatment for a platelet disorder, and all were graded low relevance.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00296023](https://clinicaltrials.gov/study/NCT00296023) | NA | Completed | 25 | Low-dose allogeneic PBSC transplant for high-risk low-grade hematologic malignancies |
| [NCT00004232](https://clinicaltrials.gov/study/NCT00004232) | Phase 1 | Completed | Not reported | CD34-enriched peripheral blood stem cells to augment bone marrow in allogeneic transplant |
| [NCT00054236](https://clinicaltrials.gov/study/NCT00054236) | Phase 1 | Completed | 55 | Multiple umbilical cord blood unit transplant after non-myeloablative conditioning |
| [NCT00301912](https://clinicaltrials.gov/study/NCT00301912) | Phase 2 | Withdrawn | 0 | Busulfan/fludarabine conditioning before matched unrelated donor transplant; no data |
| [NCT00295997](https://clinicaltrials.gov/study/NCT00295997) | NA | Unknown | 35 | Non-myeloablative matched unrelated donor transplant |
| [NCT00080925](https://clinicaltrials.gov/study/NCT00080925) | Phase 1 | Completed | 20 | T-cell depleted reduced-intensity haploidentical transplant |
| [NCT00004904](https://clinicaltrials.gov/study/NCT00004904) | Phase 1 | Completed | Not reported | T-cell depleted partially matched related donor transplant with CD34 "veto" cells |

## Literature Evidence

Currently no related literature available.

## US Market Information

The approved indication text is not available in the data compiled for this report. All six licenses are listed as valid.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103353 | NEUPOGEN (Amgen) | Injection, solution | Not available |
| BLA125553 | ZARXIO (Sandoz) | Injection, solution | Not available |
| BLA761080 | Nivestym (Pfizer) | Injection, solution | Not available |
| BLA125294 | GRANIX (Cephalon) | Injection, solution | Not available |
| BLA761126 | NYPOZI (Cipla) | Injection | Not available |

One further license, BLA761082 (RELEUKO, Amneal, injection, solution), is also listed as cancelled.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the DDI screening. The 20 shown in the data are all rated Moderate. They include:
  - Radiopharmaceuticals and radioimmunotherapies: iobenguane (I-131), fludeoxyglucose (18F), ibritumomab tiuxetan, tositumomab
  - Cytotoxic and myelosuppressive agents: paclitaxel, mercaptopurine, azacitidine, bendamustine, trimetrexate, arsenic trioxide, altretamine
  - Targeted and biologic agents: abemaciclib, acalabrutinib, avapritinib, alemtuzumab, aldesleukin, belantamab mafodotin
  - Others: levamisole, asparaginase

Key warnings and contraindications from the package insert were not available. Please refer to the package insert for them.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No trials or literature address filgrastim for platelet release disorders, and the mechanism (G-CSF acting on neutrophils) does not plausibly correct an intrinsic platelet defect. The only linked trials are transplant studies in which filgrastim plays a supportive role.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data, and a biological argument linking G-CSF to platelet function
- Preclinical or clinical evidence specific to platelet disorders
- Clarification of the cancelled status of all six US licenses and their approved indication text
- A review of whether a more plausible prediction should be prioritized, such as constitutional thrombocytopenia in the setting of stem cell mobilization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Flucytosine
parent: Model Prediction Only (L5)
nav_order: 714
evidence_level: L5
indication_count: 1
monitor_inn: "FLUCYTOSINE"
predicted_indications: ["bone Paget disease"]
last_modified_at: 2026-10-31
description: "Flucytosine: predicted new indication Bone Paget disease (evidence level L5). Approved use: Not listed in the compiled US license data"
---

# Flucytosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Flucytosine: From Antifungal Therapy to Bone Paget Disease
{: .text-alpha }

## One-Sentence Summary

Flucytosine is an oral antifungal prodrug that is converted to 5-fluorouracil inside fungal cells.
The TxGNN model predicts it may be effective for **bone Paget disease**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the compiled US license data |
| Predicted New Indication | Bone Paget disease |
| TxGNN Prediction Score | 0.9904 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 6) |
| Number of FDA Applications | at least 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, flucytosine is a fluorinated pyrimidine antifungal prodrug. Fungal cytosine deaminase converts it to 5-fluorouracil (5-FU), which disrupts fungal RNA and DNA synthesis.

Mammalian cells have very little cytosine deaminase activity, so this mechanism has no clear link to Paget disease of bone. That disease involves overactive osteoclasts and abnormal bone remodeling. The only support for the prediction is the high TxGNN model (deep learning) score, and no biological rationale was supplied. Any connection, for example through pyrimidine metabolism or a 5-FU-related cytotoxic pathway, would be speculative and would need independent validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017001 | ANCOBON (Bausch Health US LLC) | Capsule | Not listed; status valid |
| ANDA212632 | Flucytosine (Heritage/Avet) | Capsule | Not listed; status valid |
| ANDA201566 | Flucytosine (Sigmapharm) | Capsule | Not listed; status valid |
| ANDA204652 | Flucytosine (AvPAK) | Capsule | Not listed; status valid |
| ANDA213665 | Flucytosine (Aurobindo) | Capsule | Not listed; status valid |

One further license (ANDA218005, Laurus Labs, capsule) is also cancelled. All six licenses are for oral capsules.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): kidney disease, liver disease, gallbladder disease, pyoureter, potassium deficiency, thrombocytopenia, and a broad group of blood-cell disorders including leukopenia, agranulocytosis, neutropenia (acquired and congenital forms), and aplastic anemia. These point mainly to renal, hepatic, and bone marrow toxicity concerns.
- **Drug Interactions**: 85 interactions were found in total. The 20 reviewed include one Major interaction, with **deferiprone**. The rest are Moderate, including:
  - Amphotericin B (conventional, lipid complex, cholesteryl sulfate, and liposomal forms)
  - Aminoglycosides and related antibiotics: kanamycin, neomycin, streptomycin, vancomycin, polymyxin B, bacitracin
  - Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine
  - Others: deferasirox, pentamidine, ibuprofen, iobenguane (I-131), strontium chloride Sr-89

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5). There are no clinical trials or publications, and no plausible mechanistic link between an antifungal prodrug and Paget disease of bone. The drug is marketed in the US with 6 valid licenses, and bone marrow, kidney, and liver toxicity are noted as safety concerns.

**To proceed, the following is needed:**
- A biological rationale for Paget disease, such as preclinical or mechanistic studies
- Detailed mechanism of action data
- FDA package insert warnings and contraindications, so safety screening can proceed
- A literature and trial search for any real-world or preclinical signal
- A benefit-risk assessment, given the myelosuppression and renal and hepatic risks, against existing Paget disease treatments
- Clarification of current US availability (marketed, 6 valid licenses)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Pentostatin
parent: Model Prediction Only (L5)
nav_order: 1030
evidence_level: L5
indication_count: 7
monitor_inn: "PENTOSTATIN"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "parameningeal embryonal rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "liver sarcoma"]
last_modified_at: 2026-10-14
description: "Pentostatin: predicted new indication Botryoid-type embryonal rhabdomyosarcoma of the vagina (evidence level L5). Approved use: Hairy cell leukemia"
---

# Pentostatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Pentostatin: From Hairy Cell Leukemia to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Pentostatin was originally used to treat hairy cell leukemia, a rare lymphoid malignancy.
The TxGNN model predicts it may be effective for **botryoid-type embryonal rhabdomyosarcoma of the vagina**,
but **no clinical trials** and **no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hairy cell leukemia (hairy cell leukemia variant is also listed; the US license record contains no indication text) |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Pentostatin is known as an adenosine deaminase (ADA) inhibitor that disrupts purine metabolism, and it is approved for hairy cell leukemia. Detailed mechanism-of-action data were not available in the data compiled for this report, so the mechanism described here comes from general pharmacological knowledge and could not be verified against the supplied data.

No trial, publication, or mechanistic data link ADA inhibition to the biology of embryonal rhabdomyosarcoma. The high score (0.995) most likely reflects knowledge-graph proximity to other cytotoxic oncology agents rather than disease-specific evidence. The prediction should be treated as a hypothesis only.

Several other top predictions are closely related rhabdomyosarcoma entries (parameningeal embryonal, the parent "rhabdomyosarcoma" category, bile duct subtypes, prostate embryonal), plus liver sarcoma. They share nearly identical scores (0.994–0.995) and are probably propagated from the parent rhabdomyosarcoma node, so they should not be counted as independent evidence. Before any further consideration, a preclinical rationale, such as ADA dependence in rhabdomyosarcoma cell lines, would be needed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020122 (cancelled) | Nipent (Hospira, Inc.) | Injection, powder, lyophilized, for solution | Not stated in the available record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine analogue / ADA inhibitor class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph links the drug to neutropenia, thrombocytopenia, leukopenia, anemia and agranulocytosis as contraindicated conditions, which suggests hematologic risk |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function (the knowledge graph flags kidney and liver disease), infection surveillance |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindicated conditions (knowledge-graph associations, not label text)**: kidney disease, pyoureter, liver disease, gallbladder disease, thrombocytopenia, infectious disease, neutropenia, agranulocytosis, hypotensive disorder, anemia, macrocytic anemia, leukopenia, pulmonary edema.
- **Drug Interactions**: 100 interactions were recorded. Examples of the 20 reviewed:
  - **Major**: deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib
  - **Moderate**: mercaptopurine, zidovudine, chloramphenicol, azathioprine, alemtuzumab, aldesleukin, palifermin, roflumilast, strontium chloride Sr-89, anakinra, alefacept, and several vaccines (tetanus toxoid, anthrax)
  - **Minor**: levofloxacin, allopurinol

  The major interactions mostly involve additive myelosuppression or immunosuppression, which is consistent with the hematologic risks above.

Package insert warnings and contraindications were not available, so please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials, literature, or verified mechanism (Evidence Level L5). The US license is cancelled, and the knowledge graph shows substantial hematologic, hepatic, and renal safety concerns. There is no basis to advance.

**To proceed, the following is needed:**
- Preclinical evidence of ADA or purine-metabolism dependence in rhabdomyosarcoma models
- Mechanism-of-action data from DrugBank to allow a verifiable mechanistic link
- Package insert warnings and contraindications, so that safety screening can proceed
- A literature and trial search specific to pentostatin in rhabdomyosarcoma or other soft-tissue sarcomas
- Clarification of whether the cancelled US status affects drug supply or formulation availability, and of route compatibility, which is currently pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


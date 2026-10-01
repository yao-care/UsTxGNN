---
layout: default
title: Pentostatin
parent: Model Prediction Only (L5)
nav_order: 1030
evidence_level: L5
indication_count: 7
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

# Pentostatin: From Its Marketed Use to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Pentostatin is a marketed injectable (Nipent) whose approved indication is not recorded in the Evidence Pack.
The TxGNN model predicts it may be effective for **botryoid-type embryonal rhabdomyosarcoma of the vagina**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided data |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the Evidence Pack. Pentostatin is generally known as an adenosine deaminase inhibitor with lymphocyte-selective toxicity. That comes from general knowledge, not from the provided data. Any link to a solid mesenchymal tumor is therefore hypothetical.

This is a rare anatomical subtype of embryonal rhabdomyosarcoma. The high score (99.54%) most likely reflects proximity to the parent disease, rhabdomyosarcoma, in the knowledge graph rather than independent evidence. The other six predictions in this pack are related rhabdomyosarcoma subtypes (parameningeal, prostate, extrahepatic bile duct), the parent rhabdomyosarcoma node, and liver sarcoma. All are also L5, with scores between 99.42% and 99.54%. They appear to share the same graph-derived signal rather than adding independent support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020122 | Nipent (Hospira, Inc.) | Injection, powder, lyophilized, for solution | Not listed in the provided data |

## Cytotoxicity

Pentostatin is treated here as an antineoplastic because the predicted indications are all malignancies. No DrugBank category or toxicity data were provided.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine-analogue antimetabolite type), based on general drug-class knowledge |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically CBC, liver and renal function) |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no registered trials or publications. The mechanism is unverified, and the score likely propagates from the parent rhabdomyosarcoma node. Package insert safety data are also missing, so the candidate cannot advance to safety screening.

**To proceed, the following is needed:**
- The FDA package insert (approved indication, warnings, contraindications), which is currently blocking safety screening
- Mechanism of action data from DrugBank
- A targeted literature and trial search (PubMed, ClinicalTrials.gov, ICTRP) for pentostatin in rhabdomyosarcoma and sarcoma
- Preclinical evidence (for example, cell-line sensitivity of rhabdomyosarcoma to adenosine deaminase inhibition), which would be the minimum step toward L4
- A route and dosing compatibility assessment, since route compatibility is still pending

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Garlic
parent: Model Prediction Only (L5)
nav_order: 746
evidence_level: L5
indication_count: 10
---

# Garlic
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Garlic: From Marketed Garlic Products (No Stated Indication) to Gastrin Secretion Abnormality

## One-Sentence Summary

Garlic (*Allium sativum*, DrugBank DB10532) is marketed in the US, mainly as pellet products, but no approved indication text is listed in the supplied data.
The TxGNN model predicts it may be relevant to **gastrin secretion abnormality**, with a very high score (99.96%).
There are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Gastrin secretion abnormality |
| TxGNN Prediction Score | 99.96% (model rank 1549) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Garlic is a natural product with many marketed forms, but no approved indication is recorded in the supplied data. The link between garlic and gastrin secretion abnormality is therefore not supported by any mechanistic or clinical information here.

The prediction comes from the TxGNN knowledge-graph model alone. No trials or publications were retrieved, and the supplied data documents no mechanism connecting garlic to gastrin regulation.

Because the score is high but the evidence is empty, this should be treated as a hypothesis for further study, not a supported repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Allium Sativum (Hahnemann Laboratories, INC.) | Pellet | Not stated |
| Not listed | Allium sativum (Boiron) | Pellet | Not stated |
| Not listed | Allium Sativum (Hahnemann Laboratories, INC.) | Pellet | Not stated |
| Not listed | Allium Sativum (Hahnemann Laboratories, INC.) | Pellet | Not stated |
| Not listed | Allium sativum (Boiron) | Pellet | Not stated |

The 20 authorizations in total also include other forms: injection (solution), solution, liquid, ointment and solution/drops.

---

## Safety Considerations

Please refer to the package insert for safety information.

The supplied drug-interaction query returned no records. However, literature retrieved for other predicted indications (for example HIV) reports that garlic supplements can lower exposure to some antiretrovirals, such as saquinavir. Garlic may also affect platelet function. Any future study should assess interaction and bleeding risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials, no publications and no documented mechanism. The evidence level is L5, and package-insert safety information is missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action data (for example from DrugBank)
- A literature and trial search specific to gastrin secretion abnormality
- Identification of which garlic product and route would be studied

**Note on other predicted indications for garlic:**
- **Cerebral infarction** has the most preclinical support (L4), from rodent ischemia models and reviews, but no registered trials. It is better suited to a research question than to this indication.
- **HIV infectious disease** has interaction-safety signals that outweigh any efficacy signal.
- **Endometriosis** has only one in vitro study.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


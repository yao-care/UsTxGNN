---
layout: default
title: Ramucirumab
parent: Model Prediction Only (L5)
nav_order: 1108
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab: From an Unrecorded Original Indication to Uterine Ligament Adenocarcinoma

## One-Sentence Summary

Ramucirumab is a marketed antibody product (CYRAMZA, Eli Lilly), but the Evidence Pack does not record its original approved indication.
The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma**, along with several rare cervical and uterine ligament adenocarcinoma subtypes.
Currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both entries carry the same number, BLA125477) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Ramucirumab is generally known as a VEGFR2-blocking antibody with anti-angiogenic activity. That is background knowledge, not something the supplied data verifies. Angiogenesis is plausibly relevant to adenocarcinoma biology, which gives the prediction a possible but unconfirmed mechanistic link.

The original indication is not recorded, so the relationship between the original and new indications cannot be assessed here. The high score most likely reflects knowledge-graph proximity to related cervical and uterine carcinoma nodes rather than disease-specific evidence. This is especially likely for the rare histologies among the predictions.

The nine other top-ranked predictions all have the same evidence profile: L5, no trials, no literature.

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 2 | Endocervical carcinoma | 99.95% |
| 3 | Adenoid cystic carcinoma of the cervix uteri | 99.95% |
| 4 | Uterine ligament serous adenocarcinoma | 99.94% |
| 5 | Signet ring cell variant cervical mucinous adenocarcinoma | 99.94% |
| 6 | Cervical adenosquamous carcinoma, glassy cell variant | 99.94% |
| 7 | Uterine ligament endometrioid adenocarcinoma | 99.94% |
| 8 | Uterine ligament clear cell adenocarcinoma | 99.94% |
| 9 | Uterine ligament mucinous adenocarcinoma | 99.94% |
| 10 | Intestinal variant cervical mucinous adenocarcinoma | 99.94% |

Of these, endocervical carcinoma is the only one with a commonly studied anti-VEGF class rationale. That rationale comes from background knowledge, not from evidence in the pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125477 | CYRAMZA | Solution | Eli Lilly and Company |

The two license entries are identical (same number, product, form and manufacturer), so only one is listed. The approved indication text is empty in the source data.

---

## Cytotoxicity

Ramucirumab is an anti-angiogenic antibody and is being evaluated here for cancer indications. It is treated as an antineoplastic.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR2-blocking antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (99.95%). No clinical trials or publications were found, and the evidence level is L5. Safety data, mechanism of action and original indication are all missing, so the candidate cannot move past the initial stage.

**To proceed, the following is needed:**
- The FDA package insert (warnings and contraindications), which is currently a blocking gap
- Mechanism of action data, for example from DrugBank
- The original approved indication text
- A literature and trial search for ramucirumab or anti-VEGF agents in cervical and uterine adenocarcinoma
- Route compatibility assessment (currently pending)
- Prioritization among the ten predictions. Endocervical carcinoma is the most tractable, and the rare histologies are likely model artefacts.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


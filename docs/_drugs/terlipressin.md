---
layout: default
title: Terlipressin
parent: Model Prediction Only (L5)
nav_order: 1216
evidence_level: L5
indication_count: 7
monitor_inn: "TERLIPRESSIN"
predicted_indications: ["open-angle glaucoma", "primary hereditary glaucoma", "pulmonary hypertension", "kyphoscoliotic heart disease", "esotropia", "glaucoma 1, open angle", "headache disorder"]
last_modified_at: 2026-10-31
description: "Terlipressin: predicted new indication Pulmonary hypertension (evidence level L3). Approved use: Not available in the data compiled for this report"
---

# Terlipressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Terlipressin: From an Unspecified Original Indication to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Terlipressin is a synthetic vasopressin analogue (a V1 receptor agonist) with an FDA-licensed injectable product, but the data compiled for this report do not list its approved indication.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, supported by **0 registered clinical trials** and **20 publications**, most of which are small physiologic studies, case reports, or papers about portal hypertension.
The evidence is early-stage and the direction of effect is uncertain.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Pulmonary hypertension (the highest-scoring prediction was open-angle glaucoma, but it has no supporting evidence, so this report focuses on the best-supported prediction) |
| TxGNN Prediction Score | 0.9956 (open-angle glaucoma, the top-ranked prediction: 0.9978) |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold (treat as a research question) |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known information, terlipressin is a prodrug of lysine-vasopressin and acts on vasopressin V1 receptors, producing systemic vasoconstriction.

Several small human studies in patients with cirrhosis and pulmonary hypertension suggest that terlipressin may lower pulmonary vascular resistance and pulmonary pressures while raising systemic vascular resistance. This differential effect on the pulmonary and systemic circulations is the main reason the prediction is plausible. A case report also describes rescue use in a preterm infant with persistent pulmonary hypertension and refractory shock.

However, vasopressin-class drugs can also cause pulmonary vasoconstriction, so the direction of effect is uncertain and safety needs careful evaluation. Most of the retrieved papers concern portal hypertension, which is a different disease and should not be counted as evidence for pulmonary hypertension.

The other predictions (open-angle glaucoma, primary hereditary glaucoma, kyphoscoliotic heart disease, esotropia, headache disorder) have no trials or literature and appear to be computational artifacts. Headache, for example, is a known adverse effect of vasopressin analogues rather than a therapeutic target.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The table lists the publications most relevant to pulmonary hypertension. Papers on portal hypertension, shock, or hepatorenal syndrome are omitted because they do not bear directly on this indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22893473](https://pubmed.ncbi.nlm.nih.gov/22893473/) | 2012 | Cohort | Hepatobiliary Pancreat Dis Int | First 2 mg dose in 7 cirrhotic patients with pulmonary hypertension (variceal bleeding or hepatorenal syndrome) decreased pulmonary vascular resistance |
| [21733953](https://pubmed.ncbi.nlm.nih.gov/21733953/) | 2012 | Cohort | Angiology | Echo study of cirrhosis with and without pulmonary hypertension; terlipressin had differential effects on pulmonary and systemic hemodynamics |
| [18280605](https://pubmed.ncbi.nlm.nih.gov/18280605/) | 2008 | Case report | J Hepatol | Significant reduction in pulmonary arterial pressure after 1 week of terlipressin in portopulmonary hypertension |
| [15259082](https://pubmed.ncbi.nlm.nih.gov/15259082/) | 2004 | Echo study | World J Gastroenterol | Effect of terlipressin on systolic pulmonary artery pressure in cirrhotic patients |
| [30971593](https://pubmed.ncbi.nlm.nih.gov/30971593/) | 2019 | Comparative study | Ann Card Anaesth | Terlipressin vs norepinephrine to counter milrinone-induced hypotension in cardiac surgery patients with pulmonary hypertension, hypothesized not to raise pulmonary resistance |
| [32999121](https://pubmed.ncbi.nlm.nih.gov/32999121/) | 2020 | Case report | Indian Pediatrics | Rescue treatment for persistent pulmonary hypertension and refractory shock in a preterm infant |
| [21292065](https://pubmed.ncbi.nlm.nih.gov/21292065/) | 2011 | Case report | J Pediatr Surg | Rescue therapy for refractory pulmonary hypertension in a neonate with congenital diaphragmatic hernia |
| [19624374](https://pubmed.ncbi.nlm.nih.gov/19624374/) | 2009 | Case report/series | Paediatr Anaesth | Role of terlipressin in severe pulmonary hypertension in congenital diaphragmatic hernia |
| [34179513](https://pubmed.ncbi.nlm.nih.gov/34179513/) | 2021 | Review (protocol) | BMJ Paediatr Open | Protocol for a systematic review of vasopressin and terlipressin in preterm neonates with hypotension or persistent pulmonary hypertension |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022231 | Terlivaz (Mallinckrodt Hospital Products Inc.; status: valid) | Injection, powder, lyophilized, for solution | Not available in the data compiled for this report |

## Safety Considerations

Please refer to the package insert for safety information.

Points based on the mechanism and the prediction analysis:
- Systemic vasoconstriction may be a concern for optic nerve head perfusion (relevant to the glaucoma predictions) and may worsen right heart strain (relevant to kyphoscoliotic heart disease).
- Vasopressin-class drugs can cause pulmonary vasoconstriction, so the safety of terlipressin in pulmonary hypertension needs formal evaluation.
- Headache is a known adverse effect of vasopressin analogues.

No drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction is the only one with any supporting human data (L3), but that data consists of small physiologic studies and case reports, mostly in cirrhosis-related or neonatal settings, with no registered trials. The direction of effect is uncertain, and the package insert safety information is missing. The remaining predictions are purely computational (L5).

**To proceed, the following is needed:**
- The FDA package insert (approved indication, warnings, contraindications), which is currently blocking safety screening
- Detailed mechanism-of-action data
- Controlled studies of pulmonary hemodynamics and safety in pulmonary hypertension, outside the portopulmonary and neonatal settings
- Route and dosage compatibility assessment for pulmonary hypertension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


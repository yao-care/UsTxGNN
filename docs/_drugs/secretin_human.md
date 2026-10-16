---
layout: default
title: Secretin Human
parent: Model Prediction Only (L5)
nav_order: 1149
evidence_level: L5
indication_count: 10
monitor_inn: "SECRETIN HUMAN"
predicted_indications: ["open-angle glaucoma", "primary hereditary glaucoma", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Secretin Human
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

# Human Secretin: From Pancreatic Diagnostic Use to Open-Angle Glaucoma

## One-Sentence Summary

Human secretin is a gastrointestinal peptide hormone, marketed in the US as the injectable product ChiRhoStim. The TxGNN model predicts it may be effective for **open-angle glaucoma**, but **0 clinical trials** and **0 publications** currently support this prediction. It is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report |
| Predicted New Indication | Open-angle glaucoma |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, human secretin is a gastrointestinal peptide hormone that acts on secretin receptors (Gs-coupled, raising cAMP) in pancreatic ductal cells. No approved indication text was available in the data compiled for this report, so the relationship between the original use and glaucoma cannot be assessed.

The data do not establish a mechanistic link to open-angle glaucoma. The score appears to come from knowledge-graph proximity rather than a biological rationale, and any ocular relevance would be speculative.

The other top predictions point the same way. They include other glaucoma types, hair disorders (hypotrichosis, alopecia, and also its opposite, hypertrichosis), and congenital malformation syndromes. This clustering suggests the model is capturing generic neighborhood effects rather than directional pharmacology. All ten top predictions have Evidence Level L5 and a "Hold" recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021256 | ChiRhoStim (ChiRhoClin, Inc.) | Injection, powder, lyophilized, for solution | Not listed; status: cancelled |

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: The TxGNN knowledge graph links human secretin with contraindication edges for pancreatitis, liver disease, fatty liver disease, gallbladder disease, asthma (including intrinsic and allergic asthma), and substance abuse/dependence.
- **Drug Interactions**: 10 interactions were found, all rated Minor. They involve anticholinergic and antispasmodic agents: hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, mepenzolate, methscopolamine, propantheline, scopolamine, and belladonna.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN score, with no clinical trials, no literature, and no mechanistic link in the available data. The only US license is cancelled, and label safety information is missing, so the candidate cannot move to safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap)
- Mechanism of action data, for example from DrugBank
- Preclinical or mechanistic evidence connecting secretin signaling to intraocular pressure or optic nerve biology
- A route and formulation assessment, since the only known form is a systemic injection and the target is ocular
- Review of whether the lower-ranked predictions offer any better-supported direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


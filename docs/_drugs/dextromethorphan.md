---
layout: default
title: Dextromethorphan
parent: Model Prediction Only (L5)
nav_order: 599
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Dextromethorphan: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "DEXTROMETHORPHAN"
predicted_indications: ["faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Dextromethorphan: From Allergic Rhinitis and Common Cold to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan was originally used for upper respiratory conditions such as allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold and headache disorder.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (from the knowledge graph; no approved indication text on the US licenses) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 5 licenses in total (4 OTC monograph or ANDA entries and 1 NDA; all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. From general pharmacology, dextromethorphan is an NMDA receptor antagonist and sigma-1 agonist with central antitussive (cough-suppressing) activity. It does not have an established direct effect on nasal mucosal disease.

The high score most likely reflects proximity in the knowledge graph. Dextromethorphan is already linked to allergic rhinitis, vasomotor rhinitis and rhinitis, all of which are nasal cavity conditions. The prediction therefore looks like an extension of existing rhinitis-related uses rather than a newly identified mechanism. Any benefit would probably be symptomatic (for example, cough relief), not disease-modifying.

Other predicted indications show a similar pattern:

- **Acute laryngopharyngitis (99.98%)**: Likely driven by overlap with pharyngitis and common cold; at most symptomatic cough relief.
- **Faucial diphtheria (99.36%)**: Implausible as a therapeutic target. It is a bacterial toxin-mediated infection, and dextromethorphan has no antibacterial or antitoxin activity.
- **Trigeminal autonomic cephalalgia (99.32%)**: A plausible but unverified hypothesis via NMDA antagonism and central sensitization in trigeminal pain pathways.
- **Cervical disc degenerative disorder (99.30%)**: Only an indirect link, through possible modulation of neuropathic pain.
- **Allergic urticaria (99.25%)**: No established antihistaminic or mast-cell activity; likely proximity to allergic rhinitis in the graph.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M012 | Childrens Giltuss Honey DM Cough | Liquid | Not stated (cancelled) |
| M010 | RoboCough | Liquid | Not stated (cancelled) |
| ANDA091135 | cough dm | Suspension | Not stated (cancelled) |
| M013 | Dextabs | Tablet | Not stated (cancelled) |
| NDA018658 | DELSYM | Suspension, extended release | Not stated (cancelled) |

All five US authorizations are cancelled, so no single-ingredient or combination product is currently valid in this dataset.

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for safety information.

**Contraindication-related conditions (knowledge graph, not label text):** The knowledge graph links dextromethorphan to contraindications in several disease areas. These should be verified against the label before any development:
- Cardiovascular: hypertension, hypotensive disorder, long QT syndrome (including familial), torsades de pointes
- Hepatic, renal and digestive: liver failure, liver disease, kidney disease, pancreatitis, gallbladder disease, peptic and gastric ulcer, inflammatory bowel disease
- Neurological and respiratory: epilepsy, COPD, bronchitis
- Endocrine and metabolic: diabetes mellitus, diabetic ketoacidosis, hypothyroidism, adrenocortical insufficiency, potassium deficiency
- Other: thrombocytopenia, benign prostatic hyperplasia, dermatitis herpetiformis

**Drug Interactions:** 100 interactions were identified. The major ones are:
- **Serotonergic agents** (serotonin syndrome and related concerns): dexfenfluramine, fenfluramine, lorcaserin, sibutramine
- **5-HT3 antagonists** (listed as major): dolasetron, granisetron, ondansetron, palonosetron

Notable moderate interactions include bupropion, cimetidine, morphine (including liposomal), opium, metoclopramide, dronabinol, nabilone, eliglustat, mazindol, phentermine and glycerol phenylbutyrate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has the highest model score but no clinical trial or literature support (Evidence Level L5). It most likely reflects proximity to existing rhinitis indications rather than a new mechanism. Because all US licenses are cancelled and no label safety data were available, there is no basis to advance.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data to assess a plausible link to nasal mucosal disease
- A literature and trial search specific to nasal cavity disease, to determine whether any real-world evidence exists
- Clarification of the cancelled regulatory status and of route compatibility for any intranasal or other new formulation
- A safety assessment covering the knowledge-graph contraindications (cardiac QT risk in particular) and serotonergic interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


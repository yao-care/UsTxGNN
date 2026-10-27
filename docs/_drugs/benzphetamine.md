---
layout: default
title: Benzphetamine
parent: Model Prediction Only (L5)
nav_order: 451
evidence_level: L5
indication_count: 4
monitor_inn: "BENZPHETAMINE"
predicted_indications: ["hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "obsolete hypertelorism (disease)", "frontorhiny"]
last_modified_at: 2026-10-14
description: "Benzphetamine: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder"
---

# Benzphetamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Benzphetamine: From Obesity to Hypervitaminosis
{: .text-alpha }

## One-Sentence Summary

Benzphetamine is a sympathomimetic amine anorectic, originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be effective for **Hypervitaminosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction without supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active authorizations) |
| Number of NDAs | 2 (both cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, benzphetamine is a sympathomimetic amine anorectic whose efficacy in obesity is established, but nothing in the data compiled for this report connects it mechanistically to vitamin excess or vitamin clearance.

The high TxGNN score (99.98%) is a graph-based inference only. It is not backed by any clinical trial or publication, so it should be treated as a hypothesis-generating signal rather than a rationale for development.

**Other predictions reviewed**

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Proximal 16p11.2 microdeletion syndrome | 99.98% | The only plausible link. This deletion is a known genetic cause of severe early-onset obesity, which overlaps with benzphetamine's original indication. Any benefit would be limited to symptomatic weight management, not treatment of the underlying syndrome. Safety in patients with neurodevelopmental comorbidities (autism, epilepsy, psychiatric features) is uncharacterized for a stimulant-like agent. |
| 3 | Hypertelorism (obsolete term) | 99.96% | A craniofacial structural anomaly. No pharmacological mechanism of an anorectic could plausibly alter it. Likely a knowledge-graph artifact. |
| 4 | Frontorhiny | 99.93% | A rare congenital craniofacial malformation. No mechanistic rationale; the link is graph-based inference only. |

All four predictions are at evidence level L5 with no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090968 | Benzphetamine hydrochloride (Calvin Scott & Co., Inc.) | Tablet | Not listed; status cancelled |
| ANDA090346 | Benzphetamine Hydrochloride (Epic Pharma, LLC) | Tablet, film coated | Not listed; status cancelled |

Both authorizations are cancelled, so there is currently no active US marketed product among the records compiled for this report.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (graph-derived associations, not label text): hypertension and hypertensive disorders; cardiovascular disease, heart disease, sudden cardiac arrest, heart conduction disease, and heart valve disease; arteriosclerosis and atherosclerosis; pulmonary hypertension; bipolar disorder, major affective disorder, psychotic disorders, schizophreniform and schizoaffective disorders, and mental disorder in general; diabetes mellitus and diabetic ketoacidosis; glaucoma; hyperthyroidism, Graves disease, and thyrotoxicosis; substance-related disorders and substance abuse/dependence.
- **Drug Interactions** (100 interactions recorded; examples of the 20 reviewed):
  - **Major:** bupropion, lorcaserin, dexfenfluramine, diethylpropion (other anorectics and serotonergic or stimulant agents).
  - **Moderate:** antidiabetic agents (e.g., acarbose, metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, chlorpropamide, acetohexamide, albiglutide, dulaglutide), epinephrine, isometheptene, aprepitant, ascorbic acid, aluminum hydroxide, and calcium carbonate.

Please refer to the package insert for official warnings and contraindications, as label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (hypervitaminosis) has no mechanistic link, no clinical trials, and no literature, and the drug has no active US authorization. The knowledge graph also flags a broad set of cardiovascular, psychiatric, and metabolic contraindications.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank) to support any mechanistic-link analysis
- A credible biological rationale for hypervitaminosis; otherwise deprioritize it
- If pursuing the 16p11.2 microdeletion syndrome prediction, a literature review of weight-management evidence and a safety assessment in patients with neurodevelopmental and psychiatric comorbidities
- Clarification of the regulatory pathway given that both US authorizations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


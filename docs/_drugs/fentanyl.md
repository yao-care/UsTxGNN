---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 700
evidence_level: L5
indication_count: 2
monitor_inn: "FENTANYL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
last_modified_at: 2026-10-14
description: "Fentanyl: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not specified in the available data"
---

# Fentanyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Fentanyl: From Opioid Analgesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent mu-opioid receptor agonist, and the data compiled for this report do not list a specific approved indication for it.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available data |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active authorizations) |
| Number of NDAs | 6 (all cancelled; 1 NDA and 5 ANDAs) |
| Recommended Decision | Hold |

A second prediction, Tourette syndrome (score 99.05%), was also evaluated. It likewise has no supporting trials or literature, and its recommendation is also Hold (see the conclusion).

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Fentanyl is generally known as a mu-opioid receptor agonist, but this report does not rely on any more detailed mechanistic data.

**The mechanistic link is weak.** Opioids can influence vasopressin (ADH) release and may cause antidiuresis through central mechanisms. NSIAD, however, is caused by gain-of-function variants in the vasopressin V2 receptor (AVPR2) or, in some cases, GNAS-related signaling. In this condition ADH is low or undetectable and the defect lies in the kidney. Modulating central ADH release with an opioid would not be expected to correct a constitutively active receptor. Opioid-induced antidiuresis would be an adverse effect, not a therapeutic benefit.

The high TxGNN score (0.995) is a computational prediction only. No trial or publication in the data supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019101 (Hikma), cancelled | Fentanyl Citrate | Injection | Not listed |
| ANDA077449 (Ingenus), cancelled | Fentanyl | Extended-release patch | Not listed |
| ANDA210762 (Fresenius Kabi), cancelled | Fentanyl Citrate | Injection, solution | Not listed |
| ANDA076258 (Mylan), cancelled | Fentanyl | Patch | Not listed |
| ANDA077154 (SpecGx), cancelled | Fentanyl Transdermal | Extended-release patch | Not listed |

One further authorization (ANDA212086, Fresenius Kabi, injection solution) is also cancelled. All six authorizations are cancelled.

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text).** The TxGNN knowledge graph links fentanyl to the following conditions through contraindication edges. These come from the graph, not from package insert text:
- **Cardiovascular:** hypertension, hypotensive disorder, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, long QT syndrome (including familial), torsades de pointes
- **Respiratory:** COPD (including severe early onset), asthma (intrinsic and allergic)
- **Hepatic, renal and gastrointestinal:** liver failure, liver disease, kidney disease, pyoureter, pancreatitis, gallbladder disease, inflammatory bowel disease
- **Neurological and psychiatric:** basal ganglia disease, focal hand dystonia, blepharospasm, anxiety disorder, neurotic disorder, dysthymic disorder, substance abuse/dependence
- **Other:** potassium deficiency disease, benign prostatic hyperplasia

**Drug interactions.** The interaction query returned 100 records, and 20 are shown in the data compiled for this report.
- **Major:** alvimopan, aprepitant, bupropion, clarithromycin, clotrimazole, dexamethasone, dexfenfluramine, dolasetron, fenfluramine, granisetron, lorcaserin
- **Moderate:** atropine, cimetidine, clidinium, dicyclomine, dronabinol, eluxadoline, glycerol phenylbutyrate, glycopyrronium, hyoscyamine

Please refer to the package insert for formal warnings and contraindications. These were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). No clinical trials or literature support it, and the proposed mechanism is not plausible. NSIAD is a receptor-level defect in the kidney, and opioid-related antidiuresis would be an adverse effect. Fentanyl also carries high risks of respiratory depression, dependence and abuse, and all six US authorizations are cancelled.

The second prediction, Tourette syndrome, is also held. The link there is speculative. Small studies have explored opioid antagonists or partial agonists, not full mu agonists like fentanyl, and no supporting trials or literature were provided.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- Any preclinical or clinical evidence linking fentanyl to NSIAD, such as AVPR2 or GNAS signaling studies
- A clear original indication from the approval records
- A risk-benefit assessment given the abuse liability and the cancelled market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


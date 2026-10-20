---
layout: default
title: Olodaterol
parent: Moderate Evidence (L3-L4)
nav_order: 988
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-14
description: "Olodaterol: predicted new indication Bronchitis (evidence level L4). Approved use: Chronic obstructive pulmonary disease (COPD)"
monitor_inn: "OLODATEROL"
predicted_indications: ["bronchitis"]
---

# Olodaterol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Olodaterol: From Chronic Obstructive Pulmonary Disease to Bronchitis

## One-Sentence Summary

Olodaterol is an inhaled, once-daily long-acting β2-agonist originally used for maintenance treatment of chronic obstructive pulmonary disease (COPD).
The TxGNN model predicts it may be useful for **bronchitis**, but the evidence is thin: **0 clinical trials** and **2 publications** are linked to this prediction, and both are about COPD rather than bronchitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic obstructive pulmonary disease (COPD) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (the single NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for olodaterol is not available in the data compiled for this report. However, it is a long-acting β2-adrenergic agonist. It relaxes airway smooth muscle and produces sustained bronchodilation over a 24-hour dosing interval.

Chronic bronchitis is a clinical phenotype of COPD, which is olodaterol's established indication. This overlap makes the prediction plausible on the surface. The very high TxGNN score most likely reflects how closely bronchitis and COPD are related in the knowledge graph, rather than independent repurposing evidence.

Several points weaken the case:
- The two supporting publications focus on COPD and do not evaluate bronchitis as a separate indication.
- Acute bronchitis is usually viral and self-limiting, and there is no established rationale for LABA therapy in it.
- Any realistic benefit would be limited to chronic bronchitis within COPD, which is already covered by the existing indication.

In practice, this prediction is better read as a restatement of the original indication than as a genuinely new use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Review | Am J Health Syst Pharm | Reviews the pharmacology, pharmacokinetics, efficacy and safety of olodaterol as a once-daily LABA for COPD |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline | Basic Clin Pharmacol Toxicol | Finnish national guideline on the diagnosis and pharmacotherapy of stable COPD; bronchitis is not evaluated separately |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203108 (cancelled) | Striverdi Respimat (Boehringer Ingelheim) | Metered spray | Not specified in the available data |

---

## Safety Considerations

**Drug Interactions:** The interaction screen returned 100 records. The sample reviewed lists only moderate-level interactions. Main examples include:
- Sympathomimetics and stimulants: epinephrine (including ophthalmic and topical forms), ephedrine (including nasal), isometheptene, phentermine, diethylpropion, fenfluramine
- QT-relevant or related agents: clarithromycin, cisapride, dolasetron, palonosetron, granisetron
- Antidiabetic and weight-management agents: canagliflozin, ertugliflozin, semaglutide, albiglutide
- Others: famotidine, loperamide

For other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials address bronchitis, and the two linked publications are COPD-focused. The high TxGNN score appears to come from the ontological closeness of bronchitis and COPD, not from new evidence. Acute bronchitis has no established rationale for LABA therapy. The US market status is "Cancelled only", which should be verified.

**To proceed, the following is needed:**
- Studies that evaluate bronchitis as a distinct endpoint, separating chronic bronchitis within COPD from acute bronchitis
- Detailed mechanism of action data
- Package insert warnings and contraindications
- Verification of the US market status of the single NDA (cancelled)
- Clarification of whether this prediction adds anything beyond the existing COPD indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


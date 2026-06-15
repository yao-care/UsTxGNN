---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 9
---

# Alteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Alteplase: From Acute Thrombolysis to Posterolateral Myocardial Infarction

## One-Sentence Summary

Alteplase is a recombinant tissue plasminogen activator (rt-PA) used as a thrombolytic agent for acute ischemic stroke, massive pulmonary embolism, and ST-elevation myocardial infarction (STEMI).
The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction** (top-ranked prediction, score 99.79%), with **0 registered clinical trials** and **3 publications** currently providing direct support for this specific anatomical subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute thrombolysis (ischemic stroke, pulmonary embolism, STEMI — based on known pharmacology; US regulatory data not collected in this dataset) |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| US Market Status | Data not available in this dataset |
| Number of NDAs | 0 (data not collected) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Alteplase is a recombinant human tPA that works by selectively binding to fibrin within a thrombus and converting clot-bound plasminogen to plasmin. The resulting plasmin directly cleaves fibrin strands, dissolving the occlusive thrombus and restoring arterial flow. This mechanism is not indication-specific — it acts on fibrin regardless of the anatomical location of the thrombus.

Posterolateral myocardial infarction typically results from occlusion of the left circumflex artery (LCx) or a distal branch of the right coronary artery (RCA). Because the underlying pathophysiology (acute fibrin-rich coronary thrombus) is identical to that of anterior or inferior STEMI, the fibrinolytic mechanism of Alteplase is mechanistically well-suited for this location. Indeed, the large landmark thrombolysis trials (e.g., GUSTO, TAMI) enrolled mixed STEMI populations that would have included posterolateral infarcts, though without anatomically stratified primary endpoints for this subtype.

The gap identified here is not mechanistic plausibility — that is strong — but the absence of any clinical trial explicitly designed for posterolateral MI as the primary indication. The existing literature consists of a case report of cerebral embolism during late fibrinolysis in a posterolateral MI patient, a case report of primary PCI facilitated by intracoronary reteplase (a tPA variant), and an observational study evaluating ST elevation in posterior leads (V7–V9) as a diagnostic and thrombolysis-benefit marker. These provide indirect mechanistic support rather than direct efficacy evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Alteplase in posterolateral myocardial infarction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9502627](https://pubmed.ncbi.nlm.nih.gov/9502627/) | 1998 | Observational / Diagnostic | Journal of the American College of Cardiology | ST elevation in posterior chest leads (V7–V9) during acute inferior MI identifies concomitant posterior infarction; patients with posterior extension may derive greater benefit from thrombolysis |
| [8480981](https://pubmed.ncbi.nlm.nih.gov/8480981/) | 1993 | Case Report | Annales de cardiologie et d'angeiologie | Cerebral embolism with rapid resolution during late fibrinolysis with tPA in a posterolateral MI patient; highlights risk of systemic embolism from left intraventricular thrombi during fibrinolytic therapy |
| [21351226](https://pubmed.ncbi.nlm.nih.gov/21351226/) | 2011 | Case Report | Catheterization and Cardiovascular Interventions | Primary PCI for unprotected left main occlusion presenting as posterolateral MI facilitated by intracoronary reteplase (tPA class agent); describes fibrinolytic use in the acute setting indirectly |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** This dataset contains no collected TFDA/FDA label warnings, contraindications, or drug–drug interaction data for Alteplase. Collecting the full prescribing information (particularly bleeding risk, contraindications in recent surgery/stroke, and interactions with anticoagulants) is a blocking prerequisite before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While Alteplase's fibrinolytic mechanism is directly applicable to all coronary thrombus subtypes — including posterolateral MI — the evidence base for this specific anatomical designation consists solely of case reports and one observational/diagnostic study, placing it at Evidence Level L4. There are no clinical trials designed with posterolateral MI as a primary endpoint, and the safety dataset is absent, making progression to a formal research proposal premature.

**To proceed, the following is needed:**

- **Safety data collection:** Download and parse the FDA prescribing information (Activase/Cathflo Activase package inserts) to populate key warnings, contraindications, and DDI profile — currently a blocking gap
- **Subgroup analysis search:** Conduct a systematic search of large STEMI thrombolysis trials (GUSTO-I/III, TAMI 1–5, ISIS-3) for posterolateral MI subgroup outcomes with rt-PA; these may already contain indirect efficacy data at higher evidence tiers
- **Regulatory data correction:** Confirm US FDA approval status for Alteplase (Activase, NDA 103172; Cathflo Activase, NDA 125274) — the current dataset erroneously shows 0 licenses; correcting this is necessary to properly populate the Quick Overview and US Market Information sections
- **Differentiation from established use:** Clarify whether "posterolateral MI" in this context represents a truly novel indication or a subtype already covered by the existing STEMI approval; if the latter, this prediction may represent model noise rather than a repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


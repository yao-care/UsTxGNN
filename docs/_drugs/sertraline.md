---
layout: default
title: Sertraline
parent: 僅模型預測 (L5)
nav_order: 1157
evidence_level: L5
indication_count: 8
---

# Sertraline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sertraline: From Depression to Paranoid Personality Disorder

## One-Sentence Summary

Sertraline is a well-known selective serotonin reuptake inhibitor (SSRI), a drug class established for treating depression and multiple anxiety-related disorders. The TxGNN model predicts it may be effective for **Paranoid Personality Disorder**, but this specific indication is currently supported only by **4 loosely related publications** and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no TFDA/local license record found (drug is not marketed in this jurisdiction); sertraline is broadly known as an SSRI antidepressant |
| Predicted New Indication | Paranoid Personality Disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap, severity: High). Based on general pharmacological knowledge, sertraline is a selective serotonin reuptake inhibitor (SSRI) that increases synaptic serotonin concentration by blocking presynaptic reuptake; this class of drugs is broadly used across mood and anxiety disorders.

However, the link between sertraline's known efficacy and paranoid personality disorder is weak. Existing literature focuses mostly on **borderline personality disorder** or **personality disorders comorbid with major depression**, not on the core symptoms of paranoid PD (pervasive suspicion and distrust). No study directly examines a serotonergic mechanism specific to paranoid ideation or distrust as a treatment target.

As a result, this prediction should be regarded as an indirect, model-driven inference rather than a mechanistically grounded hypothesis. The evidence pack itself classifies this candidate as **L4 (preclinical/mechanistic-level at best)** with a **Hold** recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9817625](https://pubmed.ncbi.nlm.nih.gov/9817625/) | 1998 | Cohort/Comparative | International Clinical Psychopharmacology | 308 depressed patients assessed for personality disorder comorbidity; treated 24 weeks with sertraline or citalopram — general personality disorder findings, not paranoid-PD-specific |
| [18848360](https://pubmed.ncbi.nlm.nih.gov/18848360/) | 2008 | Open-label augmentation study (borderline PD) | Psychiatry Research | Aripiprazole augmentation in 21 sertraline-resistant borderline PD outpatients; not paranoid PD |
| [36853245](https://pubmed.ncbi.nlm.nih.gov/36853245/) | 2023 | Review (borderline PD) | JAMA | General review of borderline personality disorder epidemiology and management; does not address paranoid PD |
| [11686052](https://pubmed.ncbi.nlm.nih.gov/11686052/) | 2001 | Review (unrelated topic) | L'Encéphale | Review of interferon-alpha-induced psychiatric disorders; not related to sertraline or paranoid PD |

---

## Market Information

No license records are available — sertraline is currently **not marketed** in this jurisdiction (0 NDAs on file), so product/dosage-form details cannot be reported.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-interaction data are flagged as a Blocking data gap — DG001 — pending TFDA label retrieval and parsing.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for sertraline in paranoid personality disorder is indirect — drawn from studies on borderline PD or general PD/depression comorbidity — with no trials or mechanistic studies targeting paranoid PD's core symptoms (suspicion, distrust). Combined with a Blocking safety data gap (no TFDA warnings/contraindications available), this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action (DG001/DG002 remediation via DrugBank API)
- Any preclinical or mechanistic study directly addressing paranoid-spectrum symptoms and serotonergic modulation
- Reassessment if new clinical trials or targeted literature emerge

**Note for portfolio review:** within this same evidence pack, a different predicted indication for sertraline — **agoraphobia** (linked to panic disorder) — has substantially stronger support (Evidence Level L1, multiple completed Phase 4 RCTs including a 321-patient double-blind trial, plus systematic reviews/meta-analyses), and is scored "Proceed with Guardrails." If prioritizing sertraline repurposing candidates, agoraphobia/panic disorder is the far stronger near-term opportunity compared to paranoid personality disorder.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


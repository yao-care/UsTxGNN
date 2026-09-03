---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 1091
evidence_level: L5
indication_count: 5
---

# Propofol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Propofol: From General Anesthesia to Migraine Disorder

## One-Sentence Summary

> Propofol is a well-established intravenous general anesthetic/sedative agent, most familiar as an induction and maintenance agent for procedural and general anesthesia.
> The TxGNN model predicts it may be effective for **Migraine Disorder**,
> with **5 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia / procedural sedation *(formal indication text not available in evidence pack — see Data Gap DG002)* |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism-of-action data for propofol is not available in this evidence pack (flagged as Data Gap DG002, High severity). Based on the pharmacology literature underlying the repurposing rationale, propofol is a **GABA-A receptor agonist** with central nervous system depressant and possible antinociceptive effects. Preclinical (animal) models further show that propofol inhibits **cortical spreading depression (CSD)** — a core pathophysiological mechanism believed to underlie migraine aura and headache generation. This provides a plausible mechanistic bridge from propofol's known CNS-depressant/anesthetic action to a potential antimigraine effect.

The connection between the original use (general anesthesia/sedation) and the new indication is supported by real-world clinical observation: at **subanesthetic ("low") doses**, propofol has long been used off-label in emergency department settings — particularly in pediatric patients — as an abortive agent for acute and refractory migraine, distinct from its standard anesthetic dosing.

Mechanistically, this is coherent: GABA-A agonism at low doses may dampen central pain signaling and cortical hyperexcitability without inducing full anesthesia, while CSD suppression directly targets a proposed trigger for migraine pain. This dual action — sub-anesthetic sedation plus CSD inhibition — is the biological rationale most consistently cited across the clinical trial and literature evidence below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Completed | 74 | Low-dose propofol as abortive therapy for pediatric migraine in the ED; based on prior retrospective experience suggesting safety and possible superiority to standard treatment. |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | Completed | 40 | Prospective study evaluating efficacy, safe dosing limits, and duration of effect of low-dose propofol infusion as an abortive agent in pediatric migraine. |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | Terminated | 12 | Low-dose propofol for severe refractory migraine in the ED; stopped early, small sample limits interpretability. |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | NA | Unknown | 130 | Compares propofol vs. sevoflurane for anesthesia maintenance and postoperative headache incidence; propofol hypothesized to have a protective effect in migraine patients. |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | NA | Completed | 315 | Electroacupuncture analgesia study in cardiac surgery; propofol used only as background anesthetic, not a core study variable. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Arch Acad Emerg Med | Double-blind RCT comparing propofol+granisetron vs. propofol+metoclopramide for acute migraine symptom management. |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | J Emerg Med | Prospective RCT: low-dose propofol for pediatric migraine, favorable side-effect profile and potentially shorter ED length of stay. |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | RCT (pilot) | Emerg Med Australas | Pilot RCT testing IV propofol at procedural sedation dose vs. standard therapy for initial migraine management in the ED. |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Arch Acad Emerg Med | RCT comparing sumatriptan+placebo vs. sumatriptan+propofol combination for acute migraine. |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Systematic Review | Acad Emerg Med | Systematic review of propofol's safety and efficacy as an acute migraine therapy in the ED. |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Review (Guideline) | Headache | AHS 2025 guideline update on parenteral pharmacotherapy for acute migraine treatment in the ED. |
| [32705803](https://pubmed.ncbi.nlm.nih.gov/32705803/) | 2020 | Review | Emerg Med Australas | Editorial/review: "Propofol for migraine: just because we can, should we?" — discusses evidence and appropriateness. |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Cohort | Expert Rev Neurother | Describes the drug profile of sub-anesthetic dose propofol in managing super-refractory migraine headaches. |
| [23872997](https://pubmed.ncbi.nlm.nih.gov/23872997/) | 2013 | Review (BET) | Emerg Med J | Best Evidence Topic review: propofol may be safe and effective for acute migraine treatment. |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | Case Report | Headache | Early report describing unique effectiveness of IV propofol in treating intractable migraine at an outpatient headache center. |

---

## US Market Information

Currently no marketing authorization records are available in this evidence pack — propofol is registered as **Not Marketed** (0 licenses) under this regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information. *(No key warnings, contraindications, or drug-interaction data were available in this evidence pack; TFDA label warnings/contraindications are flagged as a Blocking data gap — DG001.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction (migraine disorder) is supported by one completed Phase 2/3 RCT (NCT01604785) plus multiple additional RCTs and systematic reviews (L2 evidence), and a plausible mechanistic pathway (GABA-A agonism, CSD suppression). However, formal safety labeling data (warnings/contraindications) is missing and flagged as **Blocking**, so the drug cannot yet proceed to a full safety pre-assessment.

**To proceed, the following is needed:**
- TFDA-equivalent product label (warnings, contraindications) — resolve Blocking gap DG001
- Confirmed, sourced mechanism-of-action documentation from DrugBank — resolve High-severity gap DG002
- A formal safety monitoring protocol for sub-anesthetic dosing outside standard anesthesia settings (airway/respiratory monitoring given propofol's sedative-anesthetic class)
- Regulatory pathway assessment, since the product currently holds no marketing authorization in this jurisdiction (0 NDAs, "Not Marketed" status)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


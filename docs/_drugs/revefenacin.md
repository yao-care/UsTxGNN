---
layout: default
title: Revefenacin
parent: 僅模型預測 (L5)
nav_order: 1118
evidence_level: L5
indication_count: 2
---

# Revefenacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Revefenacin: From Chronic Obstructive Pulmonary Disease (COPD) to Bronchitis

## One-Sentence Summary

> Revefenacin (YUPELRI®) is a long-acting muscarinic antagonist (LAMA), first approved by the US FDA in 2018 as a once-daily nebulized bronchodilator for chronic obstructive pulmonary disease (COPD).
> The TxGNN model predicts it may also be effective for **Bronchitis**, but this signal is currently supported by only **1 clinical trial** — and that trial is itself a COPD study, not a bronchitis-specific one — with **no dedicated literature** yet available.
> Evidence level is **L3**, meaning this is still a research-stage hypothesis rather than a validated repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Obstructive Pulmonary Disease (COPD) — per literature (PMID 30560478); no formal indication text on file in regulatory license data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available (flagged as a data gap pending a DrugBank API query). Based on the available literature, Revefenacin is a lung-selective, long-acting muscarinic antagonist (LAMA) that blocks acetylcholine binding to M3 muscarinic receptors on airway smooth muscle, producing sustained bronchodilation. It is delivered once daily via standard jet nebulizer and was the first once-daily nebulized LAMA approved (US FDA, November 2018) for maintenance treatment of COPD.

Bronchitis — particularly the chronic bronchitis phenotype — shares substantial pathophysiology with COPD, including airway smooth muscle constriction mediated by acetylcholine. Since chronic bronchitis is one of the recognized clinical phenotypes within the COPD spectrum, a bronchodilator mechanism effective in COPD is biologically plausible for bronchitis as well.

However, this mechanistic plausibility has not yet been tested in a bronchitis-specific trial population. The single trial currently linked to "bronchitis" (NCT01704404) enrolled COPD patients only and is duplicated under the "obstructive lung disease" indication in this evidence pack — it was not designed to evaluate bronchitis as a distinct condition. By contrast, the model's second-ranked prediction, "obstructive lung disease," is supported by an extensive Phase 3 program (multiple completed trials with 200–1,060 participants) that reflects revefenacin's actual approved COPD use, underscoring that the bronchitis signal is comparatively much weaker and largely inferred by mechanistic overlap rather than direct evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01704404](https://clinicaltrials.gov/study/NCT01704404) | Phase 2 | Completed | 62 | Dose-response, safety/tolerability, and PK study of multiple doses in COPD patients over 7 days; not a bronchitis-specific trial, included here due to phenotype overlap with COPD |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Revefenacin is currently **not marketed** in this jurisdiction — no authorizations (NDAs/licenses) are on file (0 total licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction is backed by only one trial — itself a COPD study rather than a bronchitis-specific trial — and no supporting literature, placing it at evidence level L3 (a "Research Question" stage per the model's own scoring). A blocking data gap on TFDA warnings/contraindications also prevents completion of the initial safety screening (S1) required before any further evaluation.

**To proceed, the following is needed:**
- TFDA package insert data — warnings and contraindications (blocking data gap, DG001)
- Confirmed mechanism-of-action detail from DrugBank (DG002)
- A bronchitis-specific clinical trial or dedicated literature evidence (none currently exists)
- Clarification of market/regulatory status, since revefenacin is approved elsewhere (US, as YUPELRI®) for COPD but shows 0 licenses in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


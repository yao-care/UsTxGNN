---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 1075
evidence_level: L5
indication_count: 10
---

# Prasugrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using no additional skill — this is a direct content-generation task against a fully specified report template; I'll follow the prompt spec exactly against the supplied Evidence Pack.

# Prasugrel: From Antiplatelet Therapy to Pulmonary Hypertension

## One-Sentence Summary

> Prasugrel is a thienopyridine-class, irreversible P2Y12 receptor antagonist used as antiplatelet therapy (evidence in this pack references its established role alongside clopidogrel following PCI in acute coronary syndrome).
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**,
> but currently only **2 clinical trials** and **2 publications** are linked to this prediction, and neither directly studies prasugrel in pulmonary hypertension.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Taiwan regulatory data (drug is not marketed in Taiwan; no NDA/license records). Globally, prasugrel is a P2Y12 inhibitor used for antiplatelet therapy after PCI in ACS (referenced indirectly via literature PMID 21241206) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on information available in this evidence pack, prasugrel is an **irreversible P2Y12 receptor antagonist (thienopyridine-class antiplatelet drug)**, the same pharmacological class as clopidogrel.

The mechanistic link to pulmonary hypertension is weak and subtype-specific at best. Only the **chronic thromboembolic pulmonary hypertension (CTEPH)** subtype involves thrombotic pathology, where antiplatelet/anticoagulant mechanisms could theoretically play a role. However, idiopathic and most other pulmonary hypertension subtypes are driven primarily by pulmonary vascular remodeling rather than platelet-mediated thrombosis, so P2Y12 inhibition does not have a clear, disease-modifying rationale for the broader pulmonary hypertension category.

Consistent with this, the retrieved clinical trials and literature do not actually study prasugrel in pulmonary hypertension patients — they were flagged by the evaluators as **Grade C relevance** (background co-occurrence in antithrombotic/anticoagulant research areas only). This supports classifying the evidence level as L5 (model prediction only, no direct supporting studies).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study on cancer-associated venous thromboembolism, evaluating eligibility for the CARAVAGGIO trial. Does not involve prasugrel or pulmonary hypertension; relevance graded C (background anticoagulation population overlap only). |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational, cross-sectional description of NOAC management in elderly non-valvular atrial fibrillation patients in Spain. Not prasugrel-specific and not a pulmonary hypertension study; relevance graded C. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Curr Med Res Opin | Evaluates factors affecting clopidogrel/prasugrel adherence after PCI in ACS patients; establishes prasugrel's established antiplatelet indication context but does not address pulmonary hypertension. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | ACTIV SARS-CoV-2 registry analysis of background chronic-disease therapy on COVID-19 outcomes; not specific to prasugrel or pulmonary hypertension. |

---

## Taiwan Market Information

Currently not marketed in Taiwan — no NDA or license records are available (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are currently unavailable in this evidence pack — TFDA label warnings/contraindications retrieval is flagged as a **Blocking** data gap that must be resolved before any safety screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 — the pulmonary hypertension prediction is currently supported only by TxGNN's model score, with no clinical trials or literature directly studying prasugrel in this indication. The mechanistic rationale is also non-specific, applying at best to a single pulmonary hypertension subtype (CTEPH) rather than the disease category as a whole.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, Blocking — required before any S1 safety evaluation)
- Detailed mechanism of action data from DrugBank (DG002, High severity)
- Confirmation of prasugrel's original approved indication and any future Taiwan license/market status
- Targeted preclinical or clinical studies of prasugrel specifically in CTEPH or other pulmonary hypertension populations, since current evidence is indirect and non-specific
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


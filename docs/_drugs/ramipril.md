---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 1107
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: From Hypertension/RAAS Therapy to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

> Ramipril is an angiotensin-converting enzyme (ACE) inhibitor that suppresses the renin-angiotensin-aldosterone system (RAAS); its original approved indication is not recorded in this evidence pack.
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia**,
> but currently **0 clinical trials** and **20 publications** support this direction — and none of the 20 publications actually studies ramipril or ACE inhibitors in pulmonary hypertension.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no `original_indications` or `licenses` records; flagged as data gap DG001) |
| Predicted New Indication | Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available for this candidate (flagged as data gap DG002, High severity). However, information embedded in this evidence pack's own trial and literature records confirms ramipril's pharmacological class: it is referenced as an **ACE inhibitor** (see clinical trial NCT00005928, "Angiotensin Converting Enzyme Inhibitor Therapy... trade name Ramipril") that acts by suppressing the RAAS pathway.

The mechanistic hypothesis for pulmonary hypertension is that RAAS inhibition could theoretically reduce hypoxia-induced pulmonary vascular remodeling, since angiotensin II contributes to vascular smooth muscle proliferation and fibrosis under chronic hypoxic stress. This is a plausible, but currently *unproven*, extension of ramipril's known cardiovascular pharmacology.

Critically, all 20 literature records retrieved for this indication are basic hypoxia biology papers — covering topics such as brain aging, cognitive impairment, tumor hypoxia signaling, and altitude physiology — **none of which mention ramipril or ACE inhibitors, and none study pulmonary hypertension treatment directly**. The mechanistic link therefore remains theoretical, not evidence-based.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

**Note:** The 20 retrieved publications are general hypoxia-biology background literature and do not directly study ramipril, ACE inhibitors, or pulmonary hypertension treatment. They are listed below for transparency but do not constitute drug-specific evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hypoxia's role in brain aging and neurodegeneration (general biology, not drug-specific) |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Clinical and molecular mechanisms of hypoxia-induced cognitive impairment |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Basic Research | Advanced Science | Hypoxia tolerance via NAT10/SEPT9/HIF-1α feedback loop in gastric cancer |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | J Cellular Biochemistry | General review of hypoxia-mediated cellular and organismal responses |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Basic Research | Trends in Cancer | Deubiquitinases regulate HIF stability in hypoxic tumor environments |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Review of the physiological mechanisms of hypoxemia |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Therapeutic modification of tumor hypoxia for radiotherapy resistance |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Rev Med Inst Mex Seguro Soc | Physiology of altitude-related (hypobaric) hypoxia |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Commentary | J Applied Physiology | Perspective on hypoxia research translation |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Role of hypoxia in multiple sclerosis pathology |

---

## US Market Information

Ramipril currently has no market authorization records within the scope of this evidence pack (market status: **Not Marketed**, 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack (all flagged as data gaps; DDI query returned "not found").

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but evidence level is L5 — no clinical trials and no drug-specific literature support ramipril's use in pulmonary hypertension owing to lung disease/hypoxia. The mechanistic rationale (RAAS inhibition reducing hypoxic vascular remodeling) is plausible but entirely theoretical given the retrieved evidence. Additionally, TFDA label safety data (DG001, Blocking) and MOA confirmation (DG002, High) are both missing, which independently blocks progression to a safety pre-assessment (S1) regardless of efficacy evidence.

**To proceed, the following is needed:**
- Package insert / label data on warnings and contraindications (DG001 — blocking, required for S1 safety pre-assessment)
- Confirmed mechanism of action from DrugBank or equivalent source (DG002)
- Drug-specific (ramipril or ACE-inhibitor class) preclinical or clinical studies in pulmonary hypertension models/patients
- Re-run literature search using drug + indication-specific search terms rather than generic hypoxia-biology terms, which returned only background/off-target results

**Note for portfolio review:** Other candidate indications for this same drug within the evidence pack carry meaningfully stronger, drug-specific evidence and may warrant separate evaluation — notably *cerebral artery occlusion* (rank 10, evidence level L3, includes a human comparative study of ramipril vs. enalapril on cerebral blood flow, PMID 8797135) and *intracerebral hemorrhage* (rank 8, evidence level L4, includes ramipril-specific animal mechanistic data, PMID 15721222).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


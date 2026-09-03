---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 1130
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Rivaroxaban: From Anticoagulation (VTE/AF) to Rheumatoid Arthritis

## One-Sentence Summary

> Rivaroxaban is a Factor Xa inhibitor, established clinically for venous thromboembolism treatment/prevention and stroke prevention in atrial fibrillation (as referenced throughout the supporting trial and literature titles in this evidence pack).
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
> but currently there are **0 clinical trials** and only **4 tangential publications** — none of which directly test rivaroxaban's efficacy in RA — supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the current regulatory dataset (0 Taiwan licenses on file); established clinical use is anticoagulation (VTE treatment/prevention, stroke prevention in AF) as a Factor Xa inhibitor |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for rivaroxaban is currently a data gap in this evidence pack (DG002). Based on the pharmacological context embedded in the supporting evidence, rivaroxaban is a direct Factor Xa inhibitor, and its efficacy in venous thromboembolism and atrial-fibrillation-related stroke prevention is well established.

The proposed link to rheumatoid arthritis rests on an indirect mechanistic hypothesis: thrombin and Factor Xa can activate PAR-2 receptors, which theoretically may promote synovial inflammation — suggesting FXa inhibition could have an anti-inflammatory effect relevant to RA. However, this is a biological plausibility argument rather than a confirmed pharmacological pathway.

Critically, none of the four literature items retrieved for this indication actually studies rivaroxaban's therapeutic effect in RA patients. They instead cover VTE diagnosis/treatment reviews, thrombin generation assays in autoimmune disease, DOAC adherence in atrial fibrillation, and a case report of a stroke in an RA patient on anticoagulation. These represent "RA patients who happen to use anticoagulants" comorbidity contexts, not evidence of RA treatment efficacy. The prediction should therefore be regarded as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | General review of lower-extremity VTE diagnosis and treatment; incidence and recurrence rates of DVT — not RA-specific |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | Compares rivaroxaban vs. apixaban adherence in non-valvular atrial fibrillation patients — no RA relevance |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Mechanistic/Lab study | La Revue de médecine interne | Thrombin generation assay used to assess hypercoagulability in autoimmune disease (e.g., antiphospholipid syndrome), not RA treatment |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | Describes a perioperative embolic stroke in an 88-year-old woman with AF who was also on oral steroids for RA — anticoagulant failure case, not an RA efficacy signal |

---

## US Market Information

Rivaroxaban currently has no marketing authorization on record in this regulatory dataset (market status: Not Marketed; total licenses: 0). No NDA/license table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are not currently available in this dataset; the missing TFDA label/warnings data is flagged as a blocking data gap — see Next Steps.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L4 with no clinical trials directly testing rivaroxaban in RA; all four supporting publications describe comorbidity/anticoagulation-safety contexts rather than RA treatment efficacy. Combined with the absence of TFDA-equivalent safety labeling, the candidate cannot advance past S0.

**To proceed, the following is needed:**
- TFDA (or equivalent) label warnings and contraindications — currently a **blocking** data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Preclinical or mechanistic studies specifically testing FXa/PAR-2 inhibition in RA synovial inflammation models
- Any prospective clinical trial directly evaluating rivaroxaban (or class) in RA patients, rather than incidental anticoagulation use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


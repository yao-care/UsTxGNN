---
layout: default
title: Palbociclib
parent: 僅模型預測 (L5)
nav_order: 1008
evidence_level: L5
indication_count: 4
---

# Palbociclib
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

# Palbociclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

> Palbociclib is a CDK4/6 inhibitor established in the treatment of HR+/HER2-negative metastatic breast cancer (per contextual literature in this evidence pack; formal regulatory/MOA fields were not populated in this dataset).
> Among four TxGNN-predicted indications in this batch, **rheumatoid arthritis** is the only one with corroborating human and preclinical evidence — **1 case report** and **3 mechanistic/preclinical studies** currently support this direction, though no dedicated clinical trial exists yet.
> Note: the single highest-scoring TxGNN prediction in this batch (hyperthyroidism, score 99.44%) has **zero supporting evidence** and is separately flagged as unsupported below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer (HR+/HER2-negative) — inferred from literature context; not present in formal regulatory data for this dataset |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 (preclinical/mechanistic studies + 1 case report) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold (Research Question — hypothesis-generating stage) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset (flagged as a High-severity data gap — DG002, remediation: query DrugBank API). Based on information recoverable from the supporting literature, palbociclib is a CDK4/6 inhibitor that blocks retinoblastoma protein (Rb) phosphorylation, arresting cells in the G1 phase of the cell cycle. It is established in HR+/HER2-negative metastatic breast cancer, where uncontrolled cell-cycle progression drives tumour growth.

Rheumatoid arthritis (RA) pathology is likewise driven by pathological proliferation — synovial fibroblast hyperplasia and abnormal lymphocyte proliferation drive joint destruction. Preclinical work identifies a CDK6-dependent (but CDK4-independent) mechanism of synovial hyperplasia in arthritic mice, and separate work shows CDK inhibition combined with cytokine blockade ameliorates arthritis in animal models without increasing immunosuppression — providing a plausible, mechanism-consistent rationale for repurposing.

A single human signal exists: a case report describes amelioration of RA in a breast cancer patient who was concurrently treated with palbociclib. This is hypothesis-generating only — one patient, confounded by concurrent methotrexate history — but it is consistent with the preclinical mechanism above. No prospective trial has tested palbociclib specifically for RA.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Review | The Oncologist | Investigates prevalence of autoimmune disease in HR+/HER2- breast cancer patients on CDK4/6 inhibitors + endocrine therapy; explores immune-modulatory effects of CDK4/6i |
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Case Report | Modern Rheumatology Case Reports | RA amelioration observed in a breast cancer patient treated with palbociclib, after prior methotrexate |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclinical (animal model) | Annals of the Rheumatic Diseases | CDK inhibition of synovial fibroblasts + cytokine blockade ameliorates arthritis in animal models without increasing immunosuppression |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclinical/Mechanistic | International Journal of Molecular Sciences | Identifies CDK6-dependent, CDK4-independent synovial hyperplasia mechanism in arthritic mice; discusses palbociclib as an explored RA treatment option |

---

## US Market Information

Not currently marketed in this jurisdiction (market status: Not Marketed; 0 licenses on file). No authorization records are available to summarize.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | High — neutropenia is a well-documented, dose-limiting adverse event across CDK4/6 inhibitors per pharmacovigilance data referenced in this evidence pack (FAERS disproportionality analyses) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (neutrophil count) each cycle; liver function tests; monitor for interstitial lung disease; monitor for thromboembolic events (see safety note below) |
| Handling Protection | Standard oral oncology drug handling precautions per institutional cytotoxic/hazardous drug policy |

---

## Safety Considerations

Formal safety fields (key warnings, contraindications, DDI) are marked as data gaps in this dataset and are flagged as **Blocking** (DG001 — TFDA label warnings/contraindications not yet retrieved). Please refer to the package insert for definitive safety information.

**Additional pharmacovigilance signal identified during this evidence review (not from formal safety fields):** Literature gathered against a separate candidate indication (thrombotic disease) shows a consistent real-world and FAERS-based association between CDK4/6 inhibitors and **thromboembolic events** (venous and arterial), including case reports of cerebral venous sinus thrombosis with a class-related agent. This is an **adverse-event signal, not a therapeutic opportunity**, and should be tracked as a safety consideration for any future palbociclib development, independent of the repurposing question addressed in this report.

---

## Other TxGNN-Predicted Indications in This Batch

For transparency, this evidence pack scored four candidate indications for palbociclib. Rheumatoid arthritis (above) was selected as the lead candidate because it is the only one with corroborating evidence. The other three are summarized below:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 1 | Hyperthyroidism | 99.44% | L5 | Hold | Highest raw TxGNN score in the batch, but **zero** clinical trials or literature support it; no biological plausibility established. Pure knowledge-graph association. |
| 3 | Thrombotic disease | 99.32% | L5 | Hold | Literature direction is **inverted** — CDK4/6 inhibitors are consistently associated with *increased* thromboembolic risk (an AE signal), not therapeutic benefit. Should be tracked as a safety issue, not a repurposing lead. |
| 4 | Resistance to thyroid hormone (THRB mutation) | 99.30% | L5 | Hold | Rare genetic disease; no evidence linking CDK4/6 pathway to thyroid hormone receptor signaling. Pure knowledge-graph association. |

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Rheumatoid arthritis is a mechanistically plausible and preclinically supported repurposing hypothesis, but it rests on only a single human case report plus two preclinical/mechanistic studies — insufficient for progression beyond hypothesis-generation. Meanwhile, essential drug-level data (TFDA label warnings/contraindications, formal MOA) are missing and are flagged as blocking gaps, preventing any safety evaluation regardless of indication.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse TFDA label for warnings/contraindications before any Stage 1 safety review can occur
- Resolve DG002 (High): obtain formal MOA data via DrugBank API to substantiate the mechanistic rationale
- Design a hypothesis-generating study (e.g., retrospective cohort of RA patients incidentally exposed to palbociclib during breast cancer treatment) before considering prospective trial investment
- Separately track and monitor the thromboembolic risk signal (rank 3) as a safety surveillance item, independent of this repurposing evaluation
- No further action recommended on hyperthyroidism or thyroid hormone resistance candidates absent new evidence — both are pure knowledge-graph artifacts with no supporting data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


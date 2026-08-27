---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 582
evidence_level: L5
indication_count: 2
---

# Denosumab
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

# Denosumab: From Osteoporosis/Bone Loss to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a RANKL-targeting monoclonal antibody whose original approved indications are not recorded in this evidence pack (Taiwan/US license data absent — see market status below), but it is globally established for treating osteoporosis and cancer-related bone loss. The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**, but this is currently a **pure knowledge-graph prediction with zero supporting clinical trials or literature** — the only related evidence in this pack (1 indirect trial, 2 indirect papers) pertains to the broader, related category "diabetic retinopathy," not to the specific severe-NPDR stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no Taiwan/US license records; original_indications empty). Denosumab is generally known as a RANKL inhibitor indicated for osteoporosis/bone loss. |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known information, Denosumab is a fully human monoclonal antibody that binds RANKL (receptor activator of nuclear factor kappa-B ligand), blocking RANK/RANKL signaling and thereby inhibiting osteoclast formation and activity. Its efficacy in reducing bone resorption is well established and forms the basis of its approved osteoporosis/bone-loss use.

The proposed link to diabetic retinopathy rests on the RANKL/RANK/osteoprotegerin (OPG) axis. OPG is known to be elevated in patients with diabetic microvascular complications, and this system has theoretical involvement in vascular inflammation and pathological neovascularization — both central features of diabetic retinopathy pathology. On this basis, TxGNN's knowledge graph surfaced a mechanistic hypothesis that RANKL inhibition could modulate this pathway.

However, this link is currently **inference-only**: no clinical trial or publication in this pack directly or indirectly evaluates Denosumab for severe NPDR itself, and the evidence pack's own rationale explicitly flags that this could reflect a bone–vascular comorbidity confounder within the knowledge graph rather than a true causal mechanism. A related but distinct prediction in this pack — the broader category "diabetic retinopathy" (rank 2, TxGNN score 99.23%, evidence level L4) — has some indirect supporting signals worth noting: (1) a Phase 3 osteoporosis trial that incidentally monitored an unrelated ocular safety endpoint (lens opacification, not retinopathy) in a population likely to include diabetic patients, and (2) real-world cohort data showing Denosumab use is associated with lower incident type 2 diabetes, reduced foot ulceration risk, and lower all-cause mortality — suggestive of a broader protective metabolic/vascular effect, but without any direct measurement of retinopathy outcomes. These are useful directional signals for the disease category as a whole but do not constitute direct evidence for severe NPDR specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

*Related indirect evidence: the broader "diabetic retinopathy" prediction (rank 2) in this evidence pack includes one trial, listed here for context since it is mechanistically and categorically adjacent:*

| Trial Number | Phase | Status | Enrollment | Key Findings | Relevance |
|---------|------|------|------|---------|---------|
| [NCT00925600](https://clinicaltrials.gov/study/NCT00925600) | Phase 3 | Completed | 769 | Double-blind, placebo-controlled trial evaluating new/worsening lens opacification (cataract-related) in men with non-metastatic prostate cancer receiving Denosumab for androgen-deprivation-therapy-induced bone loss — an incidental ocular safety endpoint, not a retinopathy efficacy trial | Grade C (indirect; different ocular pathology from retinopathy) |

---

## Literature Evidence

Currently no related literature available for severe nonproliferative diabetic retinopathy.

*Related indirect evidence: the broader "diabetic retinopathy" prediction (rank 2) includes two publications, listed here for context:*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Cohort / Meta-analysis | Diabetes, Obesity & Metabolism | Real-world cohort analysis found Denosumab (vs. bisphosphonates) associated with reduced incidence of type 2 diabetes, lower foot ulceration risk, and lower all-cause mortality; retinopathy was tracked as one of several microvascular outcomes, but no retinopathy-specific effect size is reported in the abstract |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Cross-sectional / Tool Evaluation | Cureus | Evaluates fracture risk assessment (FRAX) in adults with type 2 diabetes on anti-osteoporotic therapy; not focused on retinopathy or Denosumab efficacy specifically |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA labeling — warnings and contraindications — is currently unavailable and is flagged as a Blocking-severity data gap in this evidence pack, preventing initial safety screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The primary predicted indication, severe nonproliferative diabetic retinopathy, is supported only by a TxGNN model score (L5) with no clinical trials or literature directly or indirectly addressing it. Combined with a blocking data gap on TFDA safety labeling, there is insufficient evidence to advance this candidate past hypothesis stage.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) to close the blocking safety data gap (DG001)
- Confirmed mechanism-of-action detail via DrugBank API to properly assess the RANKL/OPG–retinopathy mechanistic link (DG002)
- Preclinical or mechanistic studies specifically testing RANKL inhibition in diabetic retinal vascular pathology
- A retrospective cohort study leveraging existing Denosumab osteoporosis registries to directly measure retinopathy incidence/progression as an outcome (building on the related rank-2 "diabetic retinopathy" signal, which merits a hypothesis-generating research question rather than immediate clinical evaluation)
- Clarification of Denosumab's original approved indications and dosage forms, since this evidence pack currently contains no license or regulatory record for this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


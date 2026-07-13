---
layout: default
title: Technetium Tc-99M Sestamibi
parent: 僅模型預測 (L5)
nav_order: 622
evidence_level: L5
indication_count: 10
---

# Technetium Tc-99M Sestamibi
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

# Technetium Tc-99m Sestamibi: From Myocardial Perfusion Imaging to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Technetium Tc-99m Sestamibi (Tc-99m MIBI) is a lipophilic cationic radiopharmaceutical diagnostic agent, widely used clinically for myocardial perfusion imaging (MPI/SPECT) and parathyroid scintigraphy.
The TxGNN model predicts it may be applicable to **Homozygous Familial Hypercholesterolemia (HoFH)**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No regulatory licensing records in dataset (clinically used for myocardial perfusion imaging and parathyroid scintigraphy) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| US Market Status | No records in dataset |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological properties, Tc-99m Sestamibi is a lipophilic cationic complex that passively crosses cell membranes and accumulates in tissues with high mitochondrial density and large negative transmembrane potential — particularly myocardial cells, parathyroid adenoma cells, and certain tumor cells. It functions exclusively as a diagnostic imaging tracer, not as a therapeutic agent.

Homozygous Familial Hypercholesterolemia (HoFH) is a rare autosomal codominant disorder caused by biallelic loss-of-function mutations in the LDL receptor pathway, resulting in severely elevated LDL-C (typically >400 mg/dL from birth). The consequence is dramatically accelerated atherosclerosis, with patients developing symptomatic coronary artery disease in childhood or early adulthood. Because myocardial ischemia is the dominant end-organ threat in HoFH, Tc-99m MIBI myocardial perfusion imaging is a clinically relevant tool for risk stratification in these patients — exactly what the single supporting publication (PMID 26298359) describes.

The TxGNN high score most likely reflects an indirect knowledge-graph pathway: HoFH → extreme hypercholesterolemia → premature atherosclerosis → myocardial ischemia → MPI diagnostic application. This is a **diagnostic applicability** rather than a new therapeutic repurposing. The prediction does not suggest MIBI can treat HoFH or modify its disease course; it reflects the established role of MPI in cardiac risk assessment for high-risk lipid disorder patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26298359](https://pubmed.ncbi.nlm.nih.gov/26298359/) | 2015 | Case Report | International Journal of Cardiology | Combined use of ¹⁸F-FDG PET and Tc-99m MIBI MPI in a patient with delayed-diagnosed HoFH; illustrates how cardiac perfusion imaging characterizes atherosclerotic and ischemic burden in HoFH patients |

---

## US Market Information

No US FDA licensing records are available in the current dataset. This likely reflects a data retrieval gap rather than actual non-approval status — Tc-99m Sestamibi (Cardiolite®, Lantheus Medical Imaging) holds US FDA approval for cardiac perfusion imaging. A dataset update against FDA NDA records is recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole supporting publication is a case report describing use of Tc-99m MIBI MPI *within* the clinical workup of an HoFH patient — this documents an existing diagnostic application, not a novel repurposing indication. There are no clinical trials and no mechanistic studies linking MIBI to HoFH pathophysiology beyond the indirect cardiovascular imaging pathway. As a diagnostic radiopharmaceutical with no therapeutic effect, framing this as a "drug repurposing" opportunity for HoFH requires conceptual clarification.

**Note on higher-priority finding:** The rank-2 prediction — **Multiple Endocrine Neoplasia (MEN)** — carries substantially stronger evidence (L3, 1 clinical trial, 20 publications, recommendation: Proceed with Guardrails) and reflects a well-established, 30-year-old clinical application of Tc-99m MIBI SPECT/CT for parathyroid adenoma localization in MEN1/MEN2A/MEN4 patients. A dedicated evaluation report for MEN is strongly recommended as the higher-priority target.

**To proceed with HoFH, the following is needed:**
- Clarification of framing: is the goal diagnostic utilization or therapeutic repurposing? (Tc-99m MIBI has no therapeutic mechanism relevant to lipid metabolism)
- US FDA NDA record retrieval for Cardiolite® to confirm approved indications and safety labeling
- Mechanism of action data from DrugBank (DB09161)
- TFDA prescribing information for formal safety assessment (Data Gap DG001)
- Prospective registry or observational data on MPI yield specifically in HoFH cohorts to establish diagnostic evidence beyond the current single case report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


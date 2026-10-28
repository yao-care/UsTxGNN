---
layout: default
title: Ioversol
parent: Model Prediction Only (L5)
nav_order: 807
evidence_level: L5
indication_count: 9
monitor_inn: "IOVERSOL"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
last_modified_at: 2026-10-23
description: "Ioversol: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the available licence text (ioversol is an iodinated co…"
---

# Ioversol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ioversol: From Diagnostic Contrast Imaging to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Ioversol is an iodinated radiographic contrast agent, marketed in the US as Optiray injection. The TxGNN model predicts it may be effective for **osteoarthritis**, but there are **no registered clinical trials** and only **1 loosely related publication** (which studies a different iodinated oil, not ioversol), so the prediction is essentially a model output without real supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence text (ioversol is an iodinated contrast agent for imaging) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Number of approvals | 1 NDA |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ioversol is a non-ionic, iodinated contrast agent used for imaging, not a drug with a known therapeutic pharmacological effect on joint disease.

The only linked publication (LipioJoint-1) tested genicular artery embolization with an ethiodized oil-based emulsion (Lipiodol) for knee osteoarthritis. That is a different product and a procedural intervention, not ioversol therapy. Any relationship is indirect. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Because no cited study directly examines ioversol in osteoarthritis, the evidence level is capped at L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Clinical trial (single-arm) | Diagnostic and Interventional Imaging | LipioJoint-1: evaluated safety and efficacy of transient genicular artery embolization with an ethiodized oil-based emulsion in knee osteoarthritis. It does not involve ioversol. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019710 | Optiray (Liebel-Flarsheim Company LLC) | Injection | Not listed in available data |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded in the interaction database. Those flagged as Major include metformin, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, kanamycin, neomycin, streptomycin and polymyxin B. Mannitol is rated Moderate. Several others (e.g. atropine, famotidine, acetylsalicylic acid, morphine, omeprazole) have an unknown severity level.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ioversol has no known pharmacological anti-osteoarthritis mechanism, no clinical trials exist, and the sole linked publication studies a different embolic agent. The high TxGNN score appears to be a TxGNN model (deep learning) artifact, so the evidence supports only a research question at this stage.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently missing, which blocks safety screening)
- Mechanism of action data for ioversol
- Any direct preclinical or clinical study of ioversol in osteoarthritis
- A clear hypothesis for a therapeutic (not imaging or procedural) role
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


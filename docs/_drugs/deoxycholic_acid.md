---
layout: default
title: Deoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 583
evidence_level: L5
indication_count: 3
---

# Deoxycholic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Deoxycholic Acid: From Secondary Bile Acid to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome

## One-Sentence Summary

Deoxycholic acid is a secondary bile acid produced by intestinal bacteria, with known pharmacological actions including bile acid receptor signaling (FXR/TGR5) and cytolytic disruption of adipocyte cell membranes.
The TxGNN model predicts it may be effective for **autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome**,
with **0 clinical trials** and **0 publications** currently supporting this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication recorded in current dataset |
| Predicted New Indication | Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (per current dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacological information, deoxycholic acid is a secondary bile acid naturally produced by gut bacteria through dehydroxylation of primary bile acids. It is known to act as a ligand for the G protein-coupled receptor TGR5 and as a weak agonist of the nuclear bile acid receptor FXR (Farnesoid X Receptor). At cytolytic concentrations, it disrupts phospholipid bilayers, causing direct destruction of adipocytes — the mechanism underlying its use in submental fat reduction (marketed as Kybella® in the United States).

Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome is a rare hereditary disorder caused by mutations in **COL4A3/COL4A4** genes, which encode type IV collagen alpha chains essential for basement membrane integrity. The syndrome manifests as hematuria, retinal arteriolar tortuosity, and joint contractures — consequences of structural basement membrane defects rather than any dysregulated metabolic or inflammatory signaling pathway.

There is **no established mechanistic link** between deoxycholic acid's known actions (bile acid receptor signaling, membrane lipid disruption) and the collagen biosynthesis defect underlying this syndrome. The high TxGNN prediction score (0.9949) reflects structural proximity within the knowledge graph topology rather than a demonstrated biological relationship. This prediction is most likely an artifact of graph-based inference and should not be taken as a genuine therapeutic hypothesis without substantial additional evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No market authorization records were found in the current dataset.

> **⚠️ Possible Data Gap:** Deoxycholic acid injection (Kybella®/Belkyra®) has been FDA-approved in the United States since 2015 for the reduction of submental fullness. The absence of records in this dataset likely reflects a gap in the query pipeline rather than actual non-approval status. Please verify directly against the FDA Orange Book before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic rationale, no registered clinical trial evidence, and no published literature directly linking deoxycholic acid to autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome. This syndrome is driven by a genetic collagen defect that falls entirely outside the known pharmacological scope of bile acid signaling or membrane-disrupting agents.

**To proceed, the following is needed:**
- Establish whether any biological pathway connects FXR/TGR5 bile acid signaling to COL4A3/COL4A4 collagen homeostasis or basement membrane biology
- Retrieve complete mechanism of action (MOA) data from DrugBank API (Data Gap DG002)
- Obtain full safety profile from US package insert, including known cytotoxicity and dose-dependent adverse effects (Data Gap DG001)
- **Strongly recommend redirecting analytical focus to the Rank 3 predicted indication — diabetic nephropathy (L4, Research Question):** Multiple preclinical studies support FXR/TGR5 bile acid signaling as a renoprotective pathway, including a Tier-1 FXR/TGR5 dual agonist animal RCT (PMID 29089371) and human metabolomic evidence linking bile acid dysregulation to diabetic kidney disease progression (PMID 39384774). This indication merits formal mechanistic review and S1 safety assessment before advancing further.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


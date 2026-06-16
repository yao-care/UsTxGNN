---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 499
evidence_level: L5
indication_count: 5
---

# Carfilzomib
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

# Carfilzomib: From Multiple Myeloma to Melanoma

## One-Sentence Summary

Carfilzomib is an irreversible proteasome inhibitor approved by the US FDA for relapsed/refractory multiple myeloma, but currently not marketed in Taiwan.
The TxGNN model's top-5 predictions all cluster around **melanoma and its subtypes** — with CMM7 (a melanoma susceptibility locus) scoring highest at 99.37%, and **melanoma** (rank 5) carrying the only actual evidence: **5 preclinical publications** and **0 clinical trials**.
Overall evidence strength is at the preclinical stage only (**L4**); the top-4 predictions (CMM7, pediatric leptomeningeal, uveal, vulvar melanoma) are all L5 with no supporting data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma (relapsed/refractory) — US FDA-approved; no Taiwan license |
| Predicted New Indication | Melanoma (all 5 TxGNN predictions cluster around melanoma entities) |
| TxGNN Prediction Score | 99.37% (CMM7, rank 1) → 99.03% (Melanoma, rank 5) |
| Evidence Level | L4 (melanoma, rank 5); L5 (ranks 1–4, no evidence) |
| Taiwan Market Status | ✗ Not marketed in Taiwan |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not available in the Evidence Pack. Based on established medical knowledge, Carfilzomib (Kyprolis®) is a selective, irreversible inhibitor of the 20S proteasome's chymotrypsin-like activity (β5 subunit). By blocking the ubiquitin-proteasome system (UPS), it causes accumulation of pro-apoptotic proteins (BIM, NOXA, PUMA), prevents IκB degradation thereby suppressing NF-κB survival signaling, and triggers ER stress → unfolded protein response (UPR) → CHOP-mediated apoptosis. Its irreversible binding distinguishes it from bortezomib and provides more sustained proteasome inhibition.

The mechanistic bridge between multiple myeloma and melanoma is UPS dependency: both are cancers with high protein synthesis and turnover rates, making them vulnerable to proteasome blockade. PMID 33671902 directly demonstrated that Carfilzomib combined with Bortezomib enhances apoptotic cell death in B16-F1 melanoma cells in vitro through caspase 3, 8, 9, and 12 activation — confirming the rationale is not purely theoretical.

However, the prediction carries significant caveats. The top-ranked entity, CMM7 (*Cutaneous Malignant Melanoma susceptibility locus 7*), is a genetic risk locus — not an actionable disease entity or treatment target. Predictions 2–4 (pediatric leptomeningeal, uveal, and vulvar melanoma) are rare subtypes with distinct molecular drivers (GNAQ/GNA11, KIT mutations) and specific barriers: poor blood-brain barrier penetration (high MW, P-gp substrate) limits CNS activity, and mucosal/ocular subtypes have not been studied preclinically with proteasome inhibitors. Only the rank-5 prediction (melanoma broadly) is supported by any evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Carfilzomib in melanoma or any of its predicted subtypes.

---

## Literature Evidence

All publications are preclinical; no RCTs or clinical studies identified.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro preclinical | Biology | Carfilzomib + Bortezomib combination directly enhances apoptosis in B16-F1 melanoma cells via caspase 3/8/9/12 activation; Annexin V flow cytometry confirmed cell death |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational / in silico | J Biomol Struct Dyn | Molecular docking and MD simulations evaluated Carfilzomib against 18 kinase targets across 10 cancer types including melanoma; identifies potential off-target activity |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical mechanistic | Matrix Biology | Carfilzomib and Bortezomib activate NF-κB to upregulate heparanase in myeloma cells; relevant mechanistic caveat: proteasome inhibitors may paradoxically promote pro-tumorigenic heparanase in some contexts |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Mechanistic / molecular biology | Mol Cancer Res | AIRAP/AIRAPL (UPS regulators) govern proteasome-mediated cell survival in human melanoma; implicates proteasome pathway as a regulatory axis in melanoma biology |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Chemical biology / PROTAC | Leukemia | BRD4-targeting PROTACs require functional proteasome for degradation; Carfilzomib co-treatment data contextualize UPS biology across cancer types including beyond myeloma |

---

## Taiwan Market Information

Carfilzomib is not approved or marketed in Taiwan. No TFDA licenses found.

> **Note:** Carfilzomib (Kyprolis®) holds US FDA approval for relapsed/refractory multiple myeloma in combination regimens (e.g., with lenalidomide/dexamethasone or daratumumab). Taiwan market entry would require a separate TFDA regulatory submission.

---

## Cytotoxicity

Carfilzomib is an antineoplastic agent (proteasome inhibitor class — targeted oncology).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — irreversible proteasome inhibitor (non-classical cytotoxic; not a DNA-damaging agent) |
| Myelosuppression Risk | Moderate — thrombocytopenia and anemia reported in myeloma trials; less pronounced neutropenia compared to classical cytotoxics |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential; serum creatinine and eGFR (renal); cardiac function (LVEF by ECHO before and during treatment); blood pressure monitoring each cycle; liver enzymes (ALT/AST) |
| Handling Protection | Please refer to the package insert warnings and precautions; cardiac toxicity (cardiomyopathy, heart failure) is the primary safety concern and requires cardiac screening prior to use |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Package insert warnings, contraindications, and drug interaction data were not available in the current Evidence Pack. Resolution of data gaps DG001 and DG002 is required before any formal safety assessment can be completed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five TxGNN predictions center on melanoma entities, but the evidence base is limited to in vitro preclinical studies only (L4 at best for general melanoma; L5 for all specific subtypes). CMM7 — the highest-scored prediction — is a genetic susceptibility locus rather than a disease indication, and cannot serve as a clinical target. No animal model data or clinical trials exist to support advancement at this time.

**To proceed, the following is needed:**

- **Resolve data gaps first:** Retrieve TFDA package insert (DG001) for warnings/contraindications; query DrugBank API for full MOA data (DG002)
- **In vivo validation:** Xenograft or syngeneic mouse melanoma models with Carfilzomib monotherapy or combination to confirm anti-tumor activity beyond cell culture
- **PK/PD assessment:** Tumor penetration studies in cutaneous melanoma; separate CNS penetration assessment before considering leptomeningeal indications
- **Subtype prioritization:** Determine which melanoma molecular subtype (BRAF-mutant, BRAF-WT, NRAS-mutant) shows greatest sensitivity to proteasome inhibition — this will define the actionable patient population
- **Mechanistic safety clarification:** PMID 27016342 raises a concern that Carfilzomib may upregulate heparanase via NF-κB in some tumor contexts; this potential pro-metastatic effect should be evaluated in melanoma models before clinical development
- **Regulatory pathway:** Given zero Taiwan licensing, any clinical development would require de novo TFDA IND application; US Phase 1 basket trial including melanoma cohort would be the recommended entry point
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 1241
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: From Unspecified Original Indication to Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)

## One-Sentence Summary

> The original approved indication of Tolvaptan is not specified in the current evidence pack.
> The TxGNN model predicts it may be effective for **Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)**,
> with **0 registered clinical trials** but **20 supporting publications**, including two pivotal Phase 3 randomized controlled trials (NEJM, 2012 and 2017), currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no `original_indications` or Taiwan license data available) |
| Predicted New Indication | Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease) |
| TxGNN Prediction Score | 99.99% (0.99987) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs identified in literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug-level fields for Tolvaptan (`original_moa: [Data Gap]`). However, the literature included in this evidence pack consistently identifies Tolvaptan as a **vasopressin V2-receptor antagonist** (e.g., PMID 23121377, PMID 16672911). Preclinical and clinical studies cited in the literature indicate that V2-receptor blockade inhibits renal cyst growth and slows the decline of kidney function, which is the mechanistic basis for its use in cystic kidney disease.

The predicted new indication — polycystic kidney disease 3 with or without polycystic liver disease — is mechanistically and clinically closely related to Autosomal Dominant Polycystic Kidney Disease (ADPKD), the condition studied in the pivotal trials referenced here (TEMPO 3:4, PMID 23121377; REPRISE, PMID 29105594). Multiple review articles and consensus statements in the evidence pack (PMID 35134221, PMID 40126492) confirm that Tolvaptan's cyst-growth-inhibiting mechanism is directly applicable to this disease group, including its hepatic (polycystic liver disease) manifestations (PMID 35487607, PMID 29175241).

Given that the mechanistic rationale (V2-receptor antagonism → reduced cyst growth) is well documented across independent literature sources, and that two large Phase 3 RCTs directly support efficacy in a closely related/overlapping disease phenotype, this TxGNN prediction is biologically and clinically well grounded — even though the evidence pack itself does not register formal `clinical_trials` entries for this exact disease term.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Note: Two pivotal Phase 3 RCTs for the closely related ADPKD phenotype are documented in the Literature Evidence section below, but are not indexed as structured `clinical_trials` entries in this evidence pack.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT (Phase 3, TEMPO 3:4) | New England Journal of Medicine | Tolvaptan (V2-receptor antagonist) slowed the increase in total kidney volume and decline in eGFR in ADPKD patients |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT (Phase 3, REPRISE) | New England Journal of Medicine | Confirmed efficacy and safety of Tolvaptan in later-stage ADPKD (lower baseline eGFR population) |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review / Meta-analysis | Nefrologia | Pooled analysis confirms efficacy and safety of Tolvaptan in delaying ADPKD progression to ESRD |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Evaluates disease-modifying agents, including Tolvaptan, for preventing ADPKD progression |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus Statement | Nephrology Dialysis Transplantation | ERA/European Rare Kidney Disease Network consensus on evidence-based Tolvaptan initiation in ADPKD |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT (Pediatric) | Pediatric Nephrology | Tolvaptan safety and pharmacodynamics evaluated in pediatric ADPKD patients (NCT02964273) |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive review of ADPKD confirming Tolvaptan as the primary disease-modifying therapy |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | Tolvaptan slows deterioration of renal function and cyst growth in ADPKD with hepatic involvement |
| [35328738](https://pubmed.ncbi.nlm.nih.gov/35328738/) | 2022 | Review | International Journal of Molecular Sciences | Reviews cystogenesis pathophysiology and treatment advances, including Tolvaptan's role |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Current Opinion in Nephrology and Hypertension | Notes Tolvaptan as the only FDA-approved disease-modifying ADPKD therapy; reviews emerging alternatives |

---

## US Market Information

Currently not marketed in the target jurisdiction; no NDA/license records are available in the evidence pack (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI data are flagged as a Blocking data gap — DG001 — pending TFDA label acquisition.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic and literature evidence for this indication is strong (L1, supported by two pivotal Phase 3 RCTs and a Cochrane systematic review), but a **Blocking** data gap (DG001) on TFDA warnings and contraindications currently prevents entry into the S1 safety initial evaluation stage. The drug is also not currently marketed in the target jurisdiction, so regulatory pathway feasibility is unconfirmed.

**To proceed, the following is needed:**
- TFDA (or equivalent local regulator) approved label with warnings/contraindications (DG001, remediation: download and parse official label PDF)
- Confirmed drug mechanism of action from DrugBank API (DG002)
- Confirmation of Tolvaptan's actual original approved indication(s) and any existing local market authorization
- Formal drug-drug interaction (DDI) review, currently returning no data (`query_status: not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


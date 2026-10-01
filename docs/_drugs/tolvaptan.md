---
layout: default
title: Tolvaptan
parent: Model Prediction Only (L5)
nav_order: 1241
evidence_level: L5
indication_count: 10
---

# Tolvaptan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tolvaptan: From Hyponatremia to Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)

## One-Sentence Summary

Tolvaptan is an oral vasopressin V2 receptor antagonist. The US license records in the Evidence Pack carry no indication text, so the original indication comes from the product names (SAMSCA, JYNARQUE) rather than from the data.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**, but there are **0 registered clinical trials** in the pack. Support comes from **20 publications**, including **2 Phase 3 RCT reports in general ADPKD**, none specific to this subtype.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records (product names suggest SAMSCA for hyponatremia and JYNARQUE for ADPKD) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (based on two Phase 3 RCT publications in general ADPKD; not subtype-specific) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 17 (all US license records, NDAs and ANDAs) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Tolvaptan is a selective vasopressin V2 receptor antagonist. Blocking V2 lowers cyclic AMP (cAMP) in kidney cells. In polycystic kidney disease, cAMP drives cyst fluid secretion and cyst cell growth. Detailed mechanism-of-action data is not available in the pack, so this explanation rests on the pack's rationale notes and the retrieved literature.

The predicted disease belongs to the same polycystic kidney family as ADPKD, where tolvaptan is already an approved therapy. The Phase 3 evidence (TEMPO 3:4 and REPRISE) comes from the general ADPKD population, mainly PKD1/PKD2 patients, and not from the PKD3 (GANAB) subtype. Extending it to PKD3 rests on the shared cAMP-driven cyst mechanism.

This is therefore not a true repurposing case. It is an extension of an approved ADPKD therapy to a related genetic subtype. Benefit for polycystic liver disease is not demonstrated in the retrieved literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | N Engl J Med | Landmark tolvaptan trial in ADPKD (TEMPO 3:4); tested whether V2 blockade slows cyst growth and kidney function decline |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | N Engl J Med | Tolvaptan in later-stage ADPKD; the earlier trial showed slower kidney volume growth and eGFR decline, with more liver enzyme and bilirubin elevations |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | Randomized trial (post hoc baseline analysis) | Pediatr Nephrol | Rapid-progression risk estimated in children aged 5–17 from the tolvaptan safety and pharmacodynamics trial (NCT02964273) |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic review / meta-analysis | Nefrologia | Evaluates the efficacy and safety of tolvaptan in ADPKD; it delays progression to end-stage renal disease |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Reviews interventions that prevent ADPKD progression, including disease-modifying agents |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus statement | Nephrol Dial Transplant | ERA/ERKNet/PKD International guidance on starting and managing tolvaptan, given long-term use and side effects |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Overview of ADPKD, the most common inherited kidney disorder (5–10% of kidney failure in the US and Europe) |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | Tolvaptan remains the only FDA-approved therapy targeting ADPKD progression; a pipeline of new agents is emerging |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Polycystic liver disease is the most common extrarenal manifestation of ADPKD; discusses tolvaptan's role in slowing kidney decline |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Clinical practice guideline | J Hepatol | EASL guidance on managing cystic liver diseases, including polycystic liver disease |

## US Market Information

The pack lists 17 US licenses; the 5 main ones are shown. The records contain no approved-indication text, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA204441 | JYNARQUE | Tablet | Otsuka America Pharmaceutical, Inc. |
| NDA022275 | SAMSCA | Tablet | Otsuka America Pharmaceutical, Inc. |
| ANDA206119 | Tolvaptan | Tablet | Endo USA, Inc. |
| ANDA216949 | TOLVAPTAN | Tablet | Novadoz Pharmaceuticals LLC |
| ANDA207605 | tolvaptan | Tablet | Apotex Corp. |

## Safety Considerations

- **Liver toxicity**: The 2017 trial abstract (PMID 29105594) notes more aminotransferase and bilirubin elevations with tolvaptan. Liver enzyme monitoring and a restricted-access program are required.

Please refer to the package insert for other safety information, including warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two Phase 3 RCT reports in general ADPKD, plus a meta-analysis, a Cochrane review and consensus guidance, support tolvaptan in polycystic kidney disease. However, no evidence is specific to the PKD3 (GANAB) subtype, and no benefit is shown for polycystic liver disease. Liver toxicity requires strict monitoring.

The other nine predictions (ranks 2–10) have little or no tolvaptan-specific evidence and should stay on Hold. Rank 5, Joubert syndrome with renal defect, is a research question only.

**To proceed, the following is needed:**
- The package insert's warnings and contraindications, which are currently missing
- Mechanism-of-action data from DrugBank
- Evidence, or a trial, in the PKD3 (GANAB) subtype, and clarity on whether the polycystic liver component benefits
- A liver-enzyme monitoring plan and access to the restricted-access program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


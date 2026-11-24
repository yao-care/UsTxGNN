---
layout: default
title: Hydroxocobalamin
parent: Model Prediction Only (L5)
nav_order: 779
evidence_level: L5
indication_count: 2
monitor_inn: "HYDROXOCOBALAMIN"
predicted_indications: ["esophageal varices with bleeding", "esophageal varices without bleeding"]
last_modified_at: 2026-11-24
description: "Hydroxocobalamin: predicted new indication Esophageal varices with bleeding (evidence level L5). In the US: 6 FDA applications (2 active), plus 1 OTC monograph/unapproved NDC listing"
---

# Hydroxocobalamin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Hydroxocobalamin: Esophageal varices with bleeding
{: .text-alpha }

## One-Sentence Summary

Hydroxocobalamin is a form of vitamin B12, originally used to treat vitamin B12 deficiency, pernicious anemia, and cyanide poisoning.
The TxGNN model predicts it may be effective for **esophageal varices with bleeding** (and the closely related **esophageal varices without bleeding**), but currently there are **0 clinical trials** and **0 publications** supporting this direction. The prediction comes from the TxGNN model (deep learning) alone and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Esophageal varices with bleeding |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 6; OTC monograph / unapproved listings: 1) |
| Number of FDA Applications | 6 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for hydroxocobalamin: "Cyanide is an extremely toxic poison. In the absence of rapid and adequate treatment, exposure to a high dose of cyanide can result in death within minutes due to the inhibition of cytochrome oxidase resulting in arrest of cellular respiration. […] Each hydroxocobalamin molecule can bind one cyanide ion by substituting it for the hydroxo ligand linked to the trivalent cobalt ion, to form cyanocobalamin, which is then excreted in the urine." ([DailyMed: Cyanokit (hydroxocobalamin) prescribing information, BTG INTERNATIONAL INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d56fcc8d-bd64-46ab-b0c0-2124bd745a6b), label version 2023-04-27; accessed 2026-11-19.) Based on known information, hydroxocobalamin is a vitamin B12 form. Its established actions are acting as a cofactor for methionine synthase and methylmalonyl-CoA mutase, and binding cyanide to form cyanocobalamin. Its efficacy in B12 deficiency and cyanide poisoning is well recognized.

These actions have no recognized role in portal hypertension, variceal formation, or hemostasis. The two predicted indications (with and without bleeding) have identical scores of 0.9923. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

One indirect route is possible in theory: hydroxocobalamin can scavenge nitric oxide, which might affect splanchnic vasodilation in portal hypertension. This hypothesis is speculative and untested, and no clinical data in this report support it. Standard care for esophageal varices (non-selective beta-blockers and endoscopic band ligation) is well established, so there is no evident unmet need that would justify prioritizing this candidate without supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA085998 | HYDROXOCOBALAMIN | ACTAVIS | Injectable; injection | Valid |
| NDA022041 | CYANOKIT | BTG INTL | Injectable; injection | Valid |
| ANDA080778 | ALPHAREDISOL | MERCK | Injectable; injection | Discontinued in Drugs@FDA |
| ANDA084629 | HYDROXOMIN | BEL MAR | Injectable; injection | Discontinued in Drugs@FDA |
| ANDA084921 | HYDROXOCOBALAMIN | ABRAXIS PHARM | Injectable; injection | Discontinued in Drugs@FDA |

Showing 5 of 7 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Knowledge-graph contraindications**: The knowledge graph links hydroxocobalamin to a contraindication with hypertensive disorder / hypertension. This comes from graph edges, not from label text, and should be verified against the package insert. It is also relevant here because portal hypertension management often involves blood pressure and hemodynamic considerations.
- **Drug Interactions**: 32 potential interactions were identified. Most are of unknown severity. The ones rated **Moderate** are:
  - Arsenic trioxide
  - Chloramphenicol
  - Iodide I-131
  - Iodide I-123

  Other listed interacting drugs (severity unknown) include omeprazole, lansoprazole, simvastatin, prednisolone, ranitidine, acetylsalicylic acid, budesonide, folic acid, valsartan, ramipril, lorazepam, citalopram, acetaminophen, mirtazapine, and levothyroxine.

Please refer to the package insert for key warnings and label-based contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (0.9923) but no clinical trials, no literature, and no plausible established mechanism. Evidence is at the lowest level (L5).

**To proceed, the following is needed:**
- Detailed mechanism of action data, and a mechanistic assessment of the nitric oxide scavenging hypothesis in portal hypertension
- A literature and trial search specific to hydroxocobalamin in portal hypertension and esophageal varices, as well as preclinical studies
- Package insert warnings and contraindications (including the hypertension-related signal)
- Review of the regulatory pathway
- Route compatibility assessment (currently only injectable forms exist)
- Evidence of an unmet need relative to current standard care (beta-blockers, endoscopic band ligation)

<!-- review:begin us-lic-20261106-hydroxocobalamin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Review of the regulatory pathway, given that both US authorizations are cancelled" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-hydroxocobalamin-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "given that both US authorizations are cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cyanokit (hydroxocobalamin) prescribing information, BTG INTERNATIONAL INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d56fcc8d-bd64-46ab-b0c0-2124bd745a6b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


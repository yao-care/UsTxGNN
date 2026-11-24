---
layout: default
title: Bumetanide
parent: Model Prediction Only (L5)
nav_order: 476
evidence_level: L5
indication_count: 1
monitor_inn: "BUMETANIDE"
predicted_indications: ["acute pulmonary heart disease"]
last_modified_at: 2026-11-24
description: "Bumetanide: predicted new indication Acute pulmonary heart disease (evidence level L5). In the US: 26 FDA applications (22 active)"
---

# Bumetanide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Bumetanide: Acute pulmonary heart disease
{: .text-alpha }

## One-Sentence Summary

Bumetanide is a loop diuretic that is marketed in the United States as tablets, injections and a nasal spray.
The TxGNN model predicts it may be useful for **acute pulmonary heart disease**, but no clinical trials are registered and no study has tested bumetanide in this disease, so the evidence level is **L5** (model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acute pulmonary heart disease |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 22 of 26) |
| Number of FDA Applications | 26 (active: 22) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for bumetanide: "Bumetanide primarily inhibits the reabsorption of sodium and chloride in the proximal and distal tubules and in the loop of Henle. The high degree of diuresis is largely due to the unique site of action. The action on the distal tubule is independent of any inhibitory effect on carbonic anhydrase and aldosterone." ([DailyMed: Enbumyst (bumetanide) prescribing information, Corstasis USA LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d6f752c5-d2bd-4f77-9611-ca2110066d1f), label version 2026-08-27; accessed 2026-11-19.) Based on the known pharmacology of the drug class, bumetanide inhibits the Na-K-2Cl cotransporter (NKCC2) in the thick ascending limb of the loop of Henle. This produces rapid sodium and water excretion and reduces intravascular volume and cardiac preload.

In acute pulmonary heart disease (acute cor pulmonale), right ventricular overload and venous congestion could in principle be relieved by lowering preload. Haemodynamic studies of bumetanide in left-sided acute and chronic heart failure show reduced preload and lower left ventricular volume. This is an indirect and plausible link to right-sided congestion.

The mechanism is not specific to this disease, however. Over-diuresis can reduce right ventricular preload and cardiac output in acute right ventricular failure (for example in massive pulmonary embolism), so any benefit depends on the patient's volume status. The studies below address left-sided heart failure or diuretics in general, not acute pulmonary heart disease itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Clinical haemodynamic study | Br J Clin Pharmacol | IV bumetanide in 24 patients with acute exercise-induced or chronic heart failure reduced cardiac index and pulmonary artery occluded pressure; left-sided failure, not acute pulmonary heart disease |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Review | Am J Ther | Review of acute heart failure management; most patients are managed with diuretics |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Review | Ann Pharmacother | Comparison of loop diuretics (pharmacokinetics, safety, efficacy, cost) and the role of furosemide |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Review | Drugs | Bumetanide is a potent loop diuretic for oedema of cardiac, hepatic and renal origin and acute pulmonary congestion |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Cohort | Am J Emerg Med | Epidemiology of heart failure presentations to US emergency departments, 2016–2023 |

## US Market Information

The records are single-ingredient products.

<!-- review:begin us-lic-20261105-bumetanide-1 -->

> **Review correction (2026-11-05)**: Originally stated: "The local data list 11 US records, all currently valid, and the list may be partial. The records are single-ingredient products." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-bumetanide-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA074225 | BUMETANIDE | HERITAGE PHARMA | Tablet; oral | Valid |
| ANDA074441 | BUMETANIDE | SAGENT | Injectable; injection | Valid |
| ANDA074700 | BUMETANIDE | SANDOZ | Tablet; oral | Valid |
| ANDA079196 | BUMETANIDE | WEST-WARD PHARMS INT | Injectable; injection | Valid |
| ANDA202900 | BUMETANIDE | ZYDUS PHARMS | Tablet; oral | Valid |

Showing 5 of 26 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

Package insert warnings and contraindications are not available in the data compiled for this report; please refer to the package insert.

**Drug Interactions**: The interaction screen returned 100 entries. Examples from the first 20 listed:
- Moderate: acarbose, rabeprazole, omeprazole, hydrocortisone, dexamethasone, triamcinolone, betamethasone, beclomethasone dipropionate, metformin, alogliptin, albiglutide, acetohexamide, amphotericin B (including lipid complex and cholesteryl sulfate forms), bupropion, morphine, bisacodyl
- Minor: doxycycline, acetylsalicylic acid

Several of these combinations (corticosteroids, amphotericin B, bisacodyl) may add to potassium loss, and antidiabetic drugs may need glucose monitoring.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9958), but the only supporting literature concerns left-sided heart failure and general diuretic use. No study tests bumetanide in acute pulmonary heart disease, and diuresis may be harmful in acute right ventricular failure. The evidence level is L5.

**To proceed, the following is needed:**
- Studies or case series of loop diuretics in acute right ventricular failure or acute cor pulmonale, stratified by volume status
- Mechanism of action data and package insert safety information
- A safety plan covering over-diuresis, electrolyte loss and haemodynamic monitoring

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "The local data list 11 US records, all currently valid, and the list may be partial" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Enbumyst (bumetanide) prescribing information, Corstasis USA LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d6f752c5-d2bd-4f77-9611-ca2110066d1f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Tiopronin
parent: Model Prediction Only (L5)
nav_order: 1231
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "TIOPRONIN"
predicted_indications: ["renal tubular acidosis", "adult polyglucosan body disease", "tricarboxylic acid cycle disorder", "disease of transporter activity", "pyruvate metabolism disorder", "inborn disorder of fatty acid oxidation and ketone body metabolism"]
description: "Tiopronin: predicted new indication Renal tubular acidosis (evidence level L5). In the US: 9 FDA applications (7 active)"
---

# Tiopronin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Tiopronin: Renal tubular acidosis
{: .text-alpha }

## One-Sentence Summary

Tiopronin is a thiol compound originally used for cystinuria.
The TxGNN model predicts it may be effective for **Renal Tubular Acidosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 7 of 9) |
| Number of FDA Applications | 9 (active: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for tiopronin: "The goal of therapy is to reduce urinary cystine concentration below its solubility limit. Tiopronin is an active reducing agent which undergoes thiol-disulfide exchange with cystine to form a mixed disulfide of tiopronin-cysteine." ([DailyMed: Venxxiva (tiopronin) prescribing information, Cycle Pharmaceuticals Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=02e24443-04c6-4b98-a395-49aec4a468de), label version 2025-12-22; accessed 2026-11-19.) Based on known chemistry, tiopronin is a thiol compound that forms soluble mixed disulfides with cysteine. This is the basis for its use in cystinuria, a renal tubular transport disorder.

Renal tubular acidosis (RTA) also involves renal tubular dysfunction, so the model may be linking the two through a shared tubular-disease space. However, the thiol-exchange mechanism does not address the bicarbonate reabsorption or acid secretion defects that cause RTA. The high score (0.9963) is a computational output only, with no supporting clinical or literature evidence, so the mechanistic link should be considered weak.

The other five top predictions are adult polyglucosan body disease, disease of transporter activity, and broad metabolic categories such as tricarboxylic acid cycle disorder, pyruvate metabolism disorder, and inborn disorders of fatty acid oxidation and ketone body metabolism. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The "disease of transporter activity" prediction likely reflects the already established cystinuria association rather than a new indication. None has trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA214326 | TIOPRONIN | TEVA PHARMS USA INC | Tablet; oral | Valid |
| ANDA216456 | TIOPRONIN | TEVA PHARMS INC | Tablet, delayed release; oral | Valid |
| ANDA216990 | VENXXIVA | TORRENT | Tablet, delayed release; oral | Valid |
| ANDA217219 | TIOPRONIN | PH HEALTH | Tablet, delayed release; oral | Valid |
| NDA019569 | THIOLA | MISSION PHARMA | Tablet; oral | Valid |

Showing 5 of 9 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

Two further licenses are not shown: ANDA216278 (Amneal, delayed-release tablet) and ANDA214326 (Teva, sugar-coated tablet).

<!-- review:begin us-lic-20261105-tiopronin-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Two further licenses are not shown: ANDA216278 (Amneal, delayed-release tablet) and ANDA214326 (Teva, sugar-coated tablet). All 7 licenses are valid." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-tiopronin-1 -->

## Safety Considerations

No label-based warnings or contraindications were available. The following comes from knowledge-graph drug-disease contraindication associations and is not label text:

- **Kidney and urinary conditions:** kidney disease, pyoureter, nephrotic syndrome (including familial forms and lipoid nephrosis), proteinuria, anti-glomerular basement membrane disease, granulomatosis with polyangiitis
- **Liver and gallbladder conditions:** liver disease, gallbladder disease
- **Blood disorders:** thrombocytopenia, leukopenia, agranulocytosis, neutropenia (including cyclic and congenital forms), aplastic anemia
- **Neuromuscular conditions:** myasthenia gravis, neuromuscular junction disease

No drug interaction data were found. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. The knowledge-graph contraindications (renal, hepatic, hematologic) are also a concern for patients with tubular or metabolic disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A literature and trial search for tiopronin in renal tubular acidosis, with preclinical evidence of a plausible mechanism
- Confirmation of current availability of the 7 valid US licenses
- Route and dosage-form compatibility assessment for the proposed indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All 7 licenses are valid" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Venxxiva (tiopronin) prescribing information, Cycle Pharmaceuticals Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=02e24443-04c6-4b98-a395-49aec4a468de) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


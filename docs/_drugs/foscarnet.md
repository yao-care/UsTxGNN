---
layout: default
title: Foscarnet
parent: Model Prediction Only (L5)
nav_order: 736
evidence_level: L5
indication_count: 4
monitor_inn: "FOSCARNET"
predicted_indications: ["autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "rheumatoid arthritis", "diabetic nephropathy"]
last_modified_at: 2026-11-24
description: "Foscarnet: predicted new indication autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome (evidence level L5). Approved use: Not stated in the available data (approved-indication tex…"
---

# Foscarnet
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Foscarnet: From Cytomegalovirus Infection to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome
{: .text-alpha }

## One-Sentence Summary

Foscarnet is an injectable antiviral that inhibits viral DNA polymerase. The data compiled for this report do not list its original approved indication.
The TxGNN model (deep learning) predicts it may be effective for **autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome**, but **no clinical trials and no publications** support this prediction. The score comes from the TxGNN model alone and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available data (approved-indication text is blank in all authorizations) |
| Predicted New Indication | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome |
| TxGNN Prediction Score | 0.9956 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 7 of 8) |
| Number of FDA Applications | 8 (active: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for foscarnet: "Foscarnet exerts its antiviral activity by a selective inhibition at the pyrophosphate binding site on virus-specific DNA polymerases at concentrations that do not affect cellular DNA polymerases. Foscarnet does not require activation (phosphorylation) by thymidine kinase or other kinases." ([DailyMed: Foscavir (foscarnet sodium) prescribing information, Clinigen Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=90e3da4e-3b1f-428b-99ca-e4bed1c80028), label version 2025-12-11; accessed 2026-11-19.) From general pharmacology, foscarnet is a pyrophosphate analog that inhibits viral DNA polymerase and reverse transcriptase, so its activity is antiviral.

The predicted condition is a rare inherited vascular and basement-membrane disorder (COL4A1-related) with no known viral cause. No mechanistic link between foscarnet and this syndrome was identified. The high TxGNN score (0.9956) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. With no supporting trials or literature, the prediction should be treated as a hypothesis only.

Other top-ranked predictions are equally weak:
- **Brain small vessel disease 1 with or without ocular anomalies**: a COL4A1-related genetic disorder with no viral component. Four retrieved papers concern CMV retinitis and appear only through ocular keyword overlap.
- **Rheumatoid arthritis**: foscarnet has no known immunomodulatory effect. The literature concerns CMV/EBV infections, with RA appearing only incidentally.
- **Diabetic nephropathy**: foscarnet is nephrotoxic, so this is a safety concern rather than a therapeutic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the predicted indication.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA212483 | FOSCARNET SODIUM | FRESENIUS KABI USA | Solution; intravenous | Valid |
| ANDA213001 | FOSCARNET SODIUM | GLAND | Solution; intravenous | Valid |
| ANDA213807 | FOSCARNET SODIUM | AVET LIFESCIENCES | Solution; intravenous | Valid |
| ANDA213987 | FOSCARNET SODIUM | SCIECURE | Solution; intravenous | Valid |
| ANDA216602 | FOSCARNET SODIUM | AMNEAL | Solution; intravenous | Valid |

Showing 5 of 8 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for these.

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): long QT syndrome and torsades de pointes, epilepsy, kidney disease, neutropenia and related congenital neutropenias, anemia, and electrolyte or mineral disorders (potassium deficiency, hypercalcemia, nephrocalcinosis, hyperphosphatemia, hypophosphatemia, phosphorus metabolism disease).
- **Drug Interactions**: 100 interactions were recorded. Major-level interactions include:
  - Amphotericin B (including the lipid complex)
  - Dolasetron
  - Bupropion

  Moderate-level examples include famotidine, omeprazole, rabeprazole, dexamethasone, hydrocortisone, clarithromycin, and loperamide.
- **Nephrotoxicity and electrolyte disturbance**: the compiled assessment notes dose-limiting renal impairment and electrolyte disturbances (hypomagnesemia, hypocalcemia, hypokalemia). This is especially relevant for the kidney-related predicted indications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials, no relevant literature, and no plausible mechanism. Foscarnet is an antiviral, and the predicted condition is a non-viral genetic disorder. The drug is marketed in the US, and it carries significant renal and electrolyte toxicity.

<!-- review:begin us-lic-20261106-foscarnet-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with 6 of 6 licenses valid, and it carries significant renal and electrolyte toxicity." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-foscarnet-1 -->

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- FDA package insert warnings and contraindications, which block safety screening
- Original approved indication text
- A biological hypothesis linking foscarnet to COL4A1-related disease, supported by preclinical evidence
- Review of the other top-ranked predictions, none of which currently has supporting evidence either

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "with 6 of 6 licenses valid" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Foscavir (foscarnet sodium) prescribing information, Clinigen Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=90e3da4e-3b1f-428b-99ca-e4bed1c80028) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


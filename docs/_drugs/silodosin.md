---
layout: default
title: Silodosin
parent: Model Prediction Only (L5)
nav_order: 1160
evidence_level: L5
indication_count: 6
monitor_inn: "SILODOSIN"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
last_modified_at: 2026-11-24
description: "Silodosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
---

# Silodosin
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

## Silodosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita
{: .text-alpha }

## One-Sentence Summary

Silodosin is a drug originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 10 of 14) |
| Number of FDA Applications | 14 (active: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for silodosin: "Silodosin is a selective antagonist of post-synaptic alpha-1 adrenoreceptors, which are located in the human prostate, bladder base, bladder neck, prostatic capsule, and prostatic urethra. Blockade of these alpha-1 adrenoreceptors can cause smooth muscle in these tissues to relax, resulting in an improvement in urine flow and a reduction in BPH symptoms." ([DailyMed: silodosin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=94bca72c-c74a-4181-8b6a-a0a2f654a0a7), label version 2026-10-30; accessed 2026-11-19.) Based on its known pharmacology, silodosin is a selective alpha-1A adrenergic receptor antagonist. It relaxes smooth muscle in the prostate and bladder neck, which is how it relieves urinary symptoms of BPH.

The link to the predicted indication is weak. Ambras syndrome is a rare congenital disorder associated with genomic rearrangements affecting regulation of the *TRPS1* gene. This pathway is unrelated to alpha-1A adrenergic signaling. The very high TxGNN score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions for this drug follow the same pattern, and none has a credible mechanism:

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Hypertrichosis | 0.9999 | Alpha-1A blockade is not known to stimulate hair growth. This score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Hypertrichosis would be an adverse effect rather than a therapeutic goal. |
| 3 | Malformation syndrome with odontal and/or periodontal component | 0.9999 | Congenital structural defects are not expected to respond to an alpha-1A antagonist. |
| 4 | Syndrome with a Dandy-Walker malformation as major feature | 0.9998 | A congenital brain malformation is not expected to be reversed by silodosin. |
| 5 | Isolated genetic hair shaft abnormality | 0.9998 | The cause is structural gene defects, with no known role for alpha-1A antagonism. |
| 6 | Familial isolated trichomegaly | 0.9923 | A rare, mostly benign trait with no link to alpha-1A antagonists. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The approved indication text is not available in the data compiled for this report.

<!-- review:begin us-lic-20261106-silodosin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "All nine US authorizations are generic (ANDA) silodosin oral capsules and all are listed as cancelled. The approved indication text is not available in the data compiled for this report." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-silodosin-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA204726 | SILODOSIN | CHARTWELL RX | Capsule; oral | Valid |
| ANDA204793 | SILODOSIN | HETERO LABS LTD V | Capsule; oral | Valid |
| ANDA206541 | SILODOSIN | LUPIN | Capsule; oral | Valid |
| ANDA209029 | SILODOSIN | PRINSTON | Capsule; oral | Valid |
| ANDA209745 | SILODOSIN | AMNEAL PHARMS CO | Capsule; oral | Valid |

Showing 5 of 14 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

Four more cancelled ANDAs are also on record: Ajanta, Lupin, Camber and PD-Rx.

## Safety Considerations

**Contraindication-related conditions (from TxGNN model (deep learning) predictions, which may reflect similarities the model learned between related diseases, not biological evidence, and not label text):**
- Multiple system atrophy
- Postural orthostatic tachycardia syndrome
- Orthostatic hypotension
- Liver failure
- Kidney disease
- Pyoureter
- Intraoperative floppy iris syndrome

**Drug Interactions:** 99 interactions were identified. Examples:
- **Major:** Clarithromycin
- **Moderate:** Cimetidine, Bupropion, Aprepitant, Morphine, Dexamethasone, Miconazole, Clotrimazole, Rolapitant, Opium, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin and ertugliflozin

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (Evidence Level L5) and no plausible mechanistic link between alpha-1A adrenergic antagonism and a congenital hair disorder. The drug is currently marketed in the US.

<!-- review:begin us-lic-20261106-silodosin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is currently marketed in the US, with 9 valid licenses." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-silodosin-2 -->

**To proceed, the following is needed:**
- Complete mechanism of action data
- FDA package insert warnings and contraindications, needed for safety screening
- Preclinical or mechanistic evidence linking alpha-1A antagonism to hair follicle biology or *TRPS1* pathways
- Clarification of whether the hypertrichosis signal reflects an adverse effect rather than a therapeutic opportunity
- Confirmation of the regulatory pathway

<!-- review:begin us-lic-20261106-silodosin-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Confirmation of the regulatory pathway, given that 9 US licenses are currently valid" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-silodosin-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "All nine US authorizations are generic (ANDA) silodosin oral capsules and all are listed as cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 9 valid licenses" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "given that 9 US licenses are currently valid" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: silodosin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=94bca72c-c74a-4181-8b6a-a0a2f654a0a7) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Moxifloxacin
parent: Model Prediction Only (L5)
nav_order: 944
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
monitor_inn: "MOXIFLOXACIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "hematopoietic and lymphoid system neoplasm"]
description: "Moxifloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). In the US: 31 FDA applications (23 active)"
---

# Moxifloxacin
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

## Moxifloxacin: Polyclonal hyperviscosity syndrome
{: .text-alpha }

## One-Sentence Summary

Moxifloxacin is a fluoroquinolone antibiotic originally used for bacterial infections such as pneumonia, conjunctivitis, peritonitis and plague.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 23 of 31) |
| Number of FDA Applications | 31 (active: 23) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the FDA-approved prescribing information for moxifloxacin: "Moxifloxacin Tablet is a member of the fluoroquinolone class of antibacterial agents. […] The bactericidal action of moxifloxacin results from inhibition of the topoisomerase II (DNA gyrase) and topoisomerase IV required for bacterial DNA replication, transcription, repair, and recombination." ([DailyMed: Moxifloxacin (moxifloxacin hydrochloride) prescribing information, Kesin Pharma Corportation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5a6d3ff1-e853-a3d8-e063-6394a90a18f5), label version 2026-11-06; accessed 2026-11-19.) Moxifloxacin belongs to the fluoroquinolone class, which is generally understood to act by inhibiting bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial infections is established.

On this basis, **no plausible mechanistic link** to polyclonal hyperviscosity syndrome can be identified. The condition involves raised serum viscosity from excess polyclonal immunoglobulins. An antibacterial has no known effect on serum viscosity or immunoglobulin levels. The very high TxGNN score is a computational association only. It should not be read as evidence of benefit, and no trial or publication backs it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The drug is marketed in the US. The five main ones are listed below. Approved indication text was not available.

<!-- review:begin us-lic-20261106-moxifloxacin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with 10 valid authorizations." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 31 FDA applications or NDC listings for this drug, 23 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-moxifloxacin-1 -->

<!-- review:begin us-lic-20261106-moxifloxacin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Approved indication text was not available for these entries." Removed: it conflicted with the FDA application data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 31 FDA applications or NDC listings for this drug, 23 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-moxifloxacin-2 -->

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202632 | Moxifloxacin Hydrochloride (Bryant Ranch Prepack) | Tablet, film coated | Not specified |
| ANDA212616 | Moxifloxacin Hydrochloride (Upsher-Smith) | Solution | Not specified |
| NDA205572 | Moxifloxacin (Hp Halden Pharma AS) | Injection, solution | Not specified |
| NDA021598 | Moxifloxacin Ophthalmic Solution (Sandoz) | Solution/drops | Not specified |
| ANDA208682 | Moxifloxacin Hydrochloride Tablets, 400 mg (Novadoz) | Tablet, film coated | Not specified |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not package insert text)**: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial ischemia, coronary artery disease, epilepsy, cirrhosis of the liver, drug-induced liver injury, potassium deficiency, tendinitis, peripheral neuropathy and other peripheral nervous system disease, myasthenia gravis and other neuromuscular junction disease, *Clostridium difficile* colitis, and perinatal necrotizing enterocolitis.
- **Drug Interactions**: 100 interactions were identified, and the first 20 retrieved are summarized here.
  - **Major**: hydrocortisone, dexamethasone, betamethasone, triamcinolone (corticosteroids), bupropion, chlorpropamide.
  - **Moderate**: antidiabetic agents (acarbose, alogliptin, albiglutide, canagliflozin, metformin, pioglitazone), famotidine, loperamide, aspirin, balsalazide, bisacodyl, and calcium and potassium salts (calcium phosphate, calcium acetate, potassium citrate).
- Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism (L5). In this case, repurposing is not justified without new evidence.

**To proceed, the following is needed:**
- Preclinical or mechanistic data showing any effect on serum viscosity or immunoglobulin-related pathology
- Mechanism of action data and package insert warnings and contraindications to complete the safety screening
- Confirmation of current US availability

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "with 10 valid authorizations" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "for these entries" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Moxifloxacin (moxifloxacin hydrochloride) prescribing information, Kesin Pharma Corportation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5a6d3ff1-e853-a3d8-e063-6394a90a18f5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


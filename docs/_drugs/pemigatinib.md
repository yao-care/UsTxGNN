---
layout: default
title: Pemigatinib
parent: Model Prediction Only (L5)
nav_order: 1026
evidence_level: L5
indication_count: 9
monitor_inn: "PEMIGATINIB"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "HER2 positive breast carcinoma", "cytomegalovirus infection", "infectious bovine rhinotracheitis", "malignant catarrh", "amyotrophic lateral sclerosis", "amyotrohpic lateral sclerosis type 22", "axial spondylometaphyseal dysplasia"]
last_modified_at: 2026-11-24
description: "Pemigatinib: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available in the compiled data"
---

# Pemigatinib
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

## Pemigatinib: From an Unspecified Original Indication to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Pemigatinib is an oral FGFR1-3 kinase inhibitor, marketed in the US as PEMAZYRE tablets. The label indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia** with a very high score, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for pemigatinib: "Pemigatinib is a small molecule kinase inhibitor that targets FGFR1, 2 and 3 with IC 50 values of less than 2 nM. Pemigatinib also inhibited FGFR4 in vitro at a concentration approximately 100 times higher than those that inhibit FGFR1, 2, and 3." ([DailyMed: Pemazyre (pemigatinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9e1f2222-1d89-4e63-989c-ccebe2ab1eb4), label version 2026-06-09; accessed 2026-11-19.) Pemigatinib is known to be an FGFR1-3 inhibitor, a targeted kinase-inhibitor class used in oncology. Because the original MOA entry is empty, this mechanism could not be cross-checked against the data.

The link to multiple endocrine neoplasia is weak. These syndromes are typically driven by MEN1 or RET alterations, and the compiled data shows no direct connection between FGFR signaling and these syndromes. The high TxGNN score (0.9971) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. A high score alone should not be read as evidence of efficacy.

For context, the other top-ranked predictions are also unsupported. Several are implausible for an FGFR inhibitor or are not relevant to human medicine: amenorrhea, cytomegalovirus infection, and two bovine diseases (infectious bovine rhinotracheitis and malignant catarrhal fever). The two bovine diseases share an identical score (0.9943), which may reflect similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence. Among the others, HER2-positive breast carcinoma and axial spondylometaphyseal dysplasia have some biological plausibility via FGFR signaling, but none has trial or disease-specific literature support in the data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA213736 | PEMAZYRE | INCYTE CORP | Tablet; oral | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 50 potential interactions. The 20 listed in the data compiled for this report include these **Major** interactions:
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Cobicistat
  - Lumacaftor
  - Chloramphenicol
  - Erythromycin
  - Ketoconazole
  - Fluconazole

  The pattern, with many CYP3A-related agents such as macrolides, azoles, and cobicistat, suggests that strong CYP3A inhibitors and inducers need careful management. Moderate interactions include cimetidine, clotrimazole, deferasirox, ivacaftor, zafirlukast, griseofulvin, elagolix, osilodrostat, metreleptin, glycerol phenylbutyrate, and troglitazone.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The safety review also cannot proceed without the label warnings and contraindications.

<!-- review:begin us-lic-20261031-pemigatinib-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction is model-only (L5), with no clinical trials or literature, no demonstrated mechanistic link between FGFR inhibition and multiple endocrine neoplasia, and the only US license is cancelled. The safety review also cannot proceed without the label warnings and contraindications." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-10-31). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-pemigatinib-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication text
- A mechanistic rationale, or preclinical data, linking FGFR signaling to multiple endocrine neoplasia
- Consideration of better-supported alternatives, such as HER2-positive breast carcinoma, where FGFR-mediated resistance is biologically plausible, though disease-specific evidence is still lacking

<!-- review:begin us-lic-20261106-pemigatinib-2 -->

> **Review correction (2026-11-06)**: Originally stated: "A mechanistic rationale, or preclinical data, linking FGFR signaling to multiple endocrine neoplasia / Review of the cancelled NDA status and its implications for any development path" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-pemigatinib-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The prediction is model-only (L5), with no clinical trials or literature, no demonstrated mechanistic link between FGFR inhibition and multi" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "Review of the cancelled NDA status and its implications for any development path" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Pemazyre (pemigatinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9e1f2222-1d89-4e63-989c-ccebe2ab1eb4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Guaifenesin
parent: Model Prediction Only (L5)
nav_order: 763
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "GUAIFENESIN"
predicted_indications: ["nasal cavity disease", "faucial diphtheria", "cervical disc degenerative disorder", "papillary conjunctivitis"]
description: "Guaifenesin: predicted new indication Nasal cavity disease (evidence level L5). In the US: 29 FDA applications (24 active), plus 1063 OTC monograph/unapproved NDC listings"
---

# Guaifenesin
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

## Guaifenesin: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Guaifenesin is an expectorant originally associated with upper respiratory conditions such as allergic rhinitis, vasomotor rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be useful for **nasal cavity disease**,
but there are currently **no registered clinical trials** and only **1 publication** (a narrative review), so the prediction rests mainly on the model score and biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 24 of 29; OTC monograph / unapproved listings: 1063) |
| Number of FDA Applications | 29 (active: 24) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of guaifenesin as: Unknown ([ChEMBL CHEMBL980 (guaifenesin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL980), CC BY-SA 3.0; accessed 2026-11-19.) Based on general knowledge, guaifenesin is an expectorant that thins and loosens airway mucus. This could plausibly relieve mucus retention in the nose and upper airway.

The original indications (allergic rhinitis, vasomotor rhinitis, rhinitis, nasopharyngitis, common cold) are closely related upper respiratory conditions that involve the nasal cavity. This anatomical and clinical proximity makes the predicted indication biologically plausible.

This link is inferred from the drug class and has not been confirmed. The very high TxGNN score is a computational prediction only and does not establish efficacy.

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|---|---|---|---|---|
| 3 | Faucial diphtheria | 0.9954 | L5 | Toxin-mediated bacterial infection; guaifenesin has no antibacterial or antitoxin activity, so the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |
| 4 | Cervical disc degenerative disorder | 0.9950 | L5 | No plausible mechanistic link identified; any signal is speculative |
| 5 | Papillary conjunctivitis | 0.9927 | L5 | No clear ocular mechanism; may reflect association with allergic rhinitis |

All four have a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | Discusses treatment of hidden respiratory allergies in voice users. Notes that antihistamines are generally avoided, that decongestants containing guaifenesin may be useful, and that steroids (nasal, inhaled or systemic) are helpful, especially for perennial allergic symptoms. |

This is a narrative review with indirect relevance, not controlled evidence of efficacy in nasal cavity disease.

## US Market Information

The drug is marketed in the US. Approved indication text is not available in the compiled data.

<!-- review:begin us-lic-20261106-guaifenesin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with 8 valid licences. Approved indication text is not available in the compiled data." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-guaifenesin-2 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA078912 | GUAIFENESIN | PERRIGO R AND D | Tablet, extended release; oral | Valid |
| ANDA091009 | GUAIFENESIN | ACTAVIS LABS FL | Tablet, extended release; oral | Valid |
| ANDA207342 | GUAIFENESIN | AMNEAL PHARMS | Tablet, extended release; oral | Valid |
| ANDA209215 | GUAIFENESIN | GUARDIAN DRUG | Tablet, extended release; oral | Valid |
| ANDA209254 | GUAIFENESIN | OHM LABS INC | Tablet, extended release; oral | Valid |

Showing 5 of 1092 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

Package insert warnings, contraindications and drug interaction data are not available in the compiled data. Please refer to the package insert for safety information.

<!-- review:begin us-lic-20261106-guaifenesin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Three further cancelled licences are not listed here, including NDA021282 (Mucinex, Bryant Ranch Prepack)." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-guaifenesin-1 -->

The knowledge graph lists the following conditions as contraindication-related associations for guaifenesin. These come from graph edges, not label text, and should be verified against the official label before any use:
- **Cardiovascular:** hypertension
- **Hepatic and renal:** liver failure, liver disease, cirrhosis of liver, kidney disease
- **Respiratory:** chronic obstructive pulmonary disease
- **Gastrointestinal and biliary:** gastric ulcer, peptic ulcer disease, inflammatory bowel disease, pancreatitis, gallbladder disease
- **Neuropsychiatric:** epilepsy, insomnia, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder
- **Metabolic and endocrine:** inherited porphyria / porphyria, hypothyroidism, myxedema, congenital hypothyroidism, adrenocortical insufficiency, Addison disease
- **Haematological:** thrombocytopenia
- **Other:** pyoureter

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible because guaifenesin is a mucus-thinning agent and nasal cavity disease is closely related to its original indications. However, there are no clinical trials, only one indirect narrative review, and no mechanism of action or label safety data. The drug is marketed in the US. The evidence does not yet support moving forward.

<!-- review:begin us-lic-20261106-guaifenesin-3 -->

> **Review correction (2026-11-06)**: Originally stated: "However, there are no clinical trials, only one indirect narrative review, and no mechanism of action or label safety data. The drug is marketed in the US with 8 valid licences." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-guaifenesin-3 -->

**To proceed, the following is needed:**
- Obtain the FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Obtain mechanism of action data from DrugBank
- Clarify which specific nasal cavity conditions are targeted, and search for controlled studies in them
- Clarify the reasons for licence cancellation and the current regulatory pathway (e.g., OTC availability)
- Verify the knowledge-graph contraindication associations against the official label

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Three further cancelled licences are not listed here, including NDA021282 (Mucinex, Bryant Ranch Prepack)" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 8 valid licences" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 8 valid licences" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL980 (guaifenesin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL980) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


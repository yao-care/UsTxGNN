---
layout: default
title: Gefitinib
parent: Model Prediction Only (L5)
nav_order: 747
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "GEFITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "pulmonary sulcus neoplasm", "lung germ cell tumor", "junctional epidermolysis bullosa"]
description: "Gefitinib: predicted new indication Fibromatosis, gingival (evidence level L5). In the US: 7 FDA applications (4 active)"
---

# Gefitinib
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

## Gefitinib: Fibromatosis, gingival
{: .text-alpha }

## One-Sentence Summary

Gefitinib is an EGFR tyrosine kinase inhibitor, originally used to treat non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis** (score 0.9989),
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 4 of 7) |
| Number of FDA Applications | 7 (active: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for gefitinib: "The epidermal growth factor receptor (EGFR) is expressed on the cell surface of both normal and cancer cells and plays a role in the processes of cell growth and proliferation. Some EGFR activating mutations (exon 19 deletion or exon 21 point mutation L858R) within NSCLC cells have been identified as contributing to the promotion of tumor cell growth, blocking of apoptosis, increasing the production of angiogenic factors and facilitating the processes of metastasis. […] Gefitinib reversibly inhibits the kinase activity of wild-type and certain activating mutations of EGFR, preventing autophosphorylation of tyrosine residues associated with the receptor, thereby inhibiting further downstream signaling and blocking EGFR-dependent proliferation." ([DailyMed: Iressa (gefitinib) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=827d60e8-7e07-41b7-c28b-49ef1c4a5a41), label version 2023-02-28; accessed 2026-11-19.) Based on general knowledge, gefitinib selectively inhibits EGFR tyrosine kinase, a pathway that regulates cell proliferation, survival and angiogenesis. Its efficacy in EGFR-mutant NSCLC is well established.

The link to gingival fibromatosis is speculative. EGFR signaling could plausibly influence fibroblast proliferation, but no studies, trials or mechanistic data were found to support this. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so the prediction should be treated as a hypothesis only.

Other top-ranked predictions show a similar pattern:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Fibroma of lung | 0.9986 | L5 | No trials or literature; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |
| 3 | Inclusion body myopathy with Paget disease and/or frontotemporal dementia | 0.9986 | L5 | No clear rationale for EGFR inhibition in this VCP-related disease |
| 4 | Hamartoma of lung | 0.9986 | L5 | No trials or literature |
| 6 | Lung benign neoplasm | 0.9985 | L4 | Literature concerns malignant NSCLC, not benign tumours |
| 7 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 0.9984 | L5 | Literature mainly describes gefitinib toxicities |
| 8 | Pulmonary sulcus neoplasm | 0.9984 | L5 | Indirect literature only |
| 9 | Lung germ cell tumor | 0.9984 | L5 | One unrelated phase I trial; literature is general |
| 10 | Junctional epidermolysis bullosa | 0.9984 | L5 | No plausible rationale; potential skin toxicity concern |

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA208913 | GEFITINIB | ACTAVIS LABS FL INC | Tablet; oral | Valid |
| ANDA211591 | GEFITINIB | QILU PHARM HAINAN | Tablet; oral | Valid |
| ANDA212827 | GEFITINIB | NATCO | Tablet; oral | Valid |
| NDA206995 | IRESSA | ASTRAZENECA | Tablet; oral | Valid |
| ANDA209532 | GEFITINIB | APOTEX | Tablet; oral | Discontinued in Drugs@FDA |

Showing 5 of 7 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function and respiratory symptoms (based on the knowledge-graph contraindications below); other items per the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report.

- **Knowledge-graph contraindication signals** (not label text): liver disease, gallbladder disease, interstitial lung disease, pulmonary fibrosis, postinflammatory pulmonary fibrosis. The literature also documents gefitinib-induced pneumonitis/ILD (including a fatal case), QT prolongation, cutaneous toxicities and a case of recurrent myocardial infarction.
- **Drug Interactions**: 100 interactions were identified. Among those listed, most are moderate:
  - Acid-suppressing agents: famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole and rabeprazole
  - CYP-related agents: clarithromycin, aprepitant, miconazole, clotrimazole, dexamethasone
  - Others: naltrexone, troglitazone
  - Interactions with calcitriol and glimepiride have an unknown severity level.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no trials or literature for gingival fibromatosis, the mechanistic link is speculative, the drug is marketed, and package insert safety data are missing. The other top-ranked predictions are likewise unsupported or only indirectly supported, mostly overlapping with the original lung cancer indication.

<!-- review:begin us-lic-20261106-gefitinib-1 -->

> **Review correction (2026-11-06)**: Originally stated: "There are no trials or literature for gingival fibromatosis, the mechanistic link is speculative, the drug is marketed with 4 of 4 US licenses valid, and package insert safety data are missing." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-gefitinib-1 -->

**To proceed, the following is needed:**
- Obtain the FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Obtain detailed mechanism-of-action data (e.g., from DrugBank)
- Preclinical or mechanistic studies showing that EGFR inhibition affects gingival fibroblast proliferation or fibrosis
- Assessment of whether a systemic or local route is appropriate for a gingival condition, weighed against the known skin, lung, liver and QT-related safety signals
- Clarify the US regulatory pathway

<!-- review:begin us-lic-20261106-gefitinib-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarify the US regulatory pathway, since 4 of 4 licenses are currently valid" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-gefitinib-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "with 4 of 4 US licenses valid" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "since 4 of 4 licenses are currently valid" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Iressa (gefitinib) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=827d60e8-7e07-41b7-c28b-49ef1c4a5a41) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 784
evidence_level: L5
indication_count: 7
monitor_inn: "IBUPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-11-24
description: "Ibuprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In the US: 272 FDA applications (120 active), plus 13 OTC monograph/unapproved NDC listings"
---

# Ibuprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Ibuprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Ibuprofen is a non-steroidal anti-inflammatory drug (NSAID) originally used for arthritis, headache and patent ductus arteriosus.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 120 of 272; OTC monograph / unapproved listings: 13) |
| Number of FDA Applications | 272 (active: 120) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for ibuprofen: "Ibuprofen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of CALDOLOR, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684), label version 2026-01-29; accessed 2026-11-19.) Ibuprofen is a well-known non-selective cyclooxygenase (COX) inhibitor that reduces prostaglandin synthesis, giving analgesic and anti-inflammatory effects. Its benefit in arthritis and arthropathy is symptomatic.

Hunter-Thompson type acromesomelic dysplasia is a rare skeletal dysplasia caused by loss-of-function variants in GDF5 (BMP signalling). No plausible mechanism by which COX inhibition would correct this underlying defect has been established. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At best, ibuprofen might offer symptomatic relief of joint pain.

Other top-ranked predictions show the same pattern: brachyolmia-amelogenesis imperfecta syndrome (0.9971), myosclerosis (0.9968), brachyolmia (0.9967), brachydactyly-syndactyly syndrome (0.9966), pseudoachondroplasia (0.9966) and colobomatous microphthalmia-rhizomelic dysplasia syndrome (0.9960). All are rare genetic skeletal or developmental disorders with no supporting trials or literature. Pseudoachondroplasia has the most plausible symptom-level rationale (secondary joint pain and osteoarthritis), but it too would not address the primary COMP pathology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA071267 | IBUPROFEN | CONTRACT PHARMACAL | Tablet; oral | Valid |
| ANDA071268 | IBUPROFEN | CONTRACT PHARMACAL | Tablet; oral | Valid |
| ANDA071334 | IBUPROFEN | AMNEAL PHARMS NY | Tablet; oral | Valid |
| ANDA071335 | IBUPROFEN | AMNEAL PHARMS NY | Tablet; oral | Valid |
| ANDA071935 | IBUPROFEN | AMNEAL PHARMS NY | Tablet; oral | Valid |

Showing 5 of 285 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

Approved-indication text is not available for these entries.

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for these.

- **Contraindication-related conditions (knowledge graph, not label text)**: Cardiovascular and cerebrovascular conditions (hypertension, hypotension, myocardial infarction, stroke, cerebral infarction); liver and kidney disease or failure; peptic ulcer disease and inflammatory bowel disease; blood coagulation disorders and thrombocytopenia; chronic obstructive pulmonary disease; epilepsy; diabetes mellitus and diabetic ketoacidosis; hypothyroidism; systemic lupus erythematosus; potassium deficiency; benign prostatic hyperplasia; gallbladder disease; and substance abuse/dependence.
- **Drug Interactions**: 100 interactions were identified. Of those listed, the main one at **Major** level is **acetylsalicylic acid**. **Moderate** interactions include corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), exenatide, fenfluramine and dexfenfluramine, aprepitant, balsalazide, kanamycin and levofloxacin. **Minor** interactions include famotidine, ranitidine and cimetidine.
- **Developmental concern**: Prenatal NSAID exposure is a safety concern for congenital limb or skeletal malformation contexts such as brachydactyly-syndactyly syndrome.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (Evidence Level L5). There are no clinical trials or publications, and no plausible mechanism links COX inhibition to the GDF5/BMP defect. The drug is marketed in the US, but label safety data are missing.

<!-- review:begin us-lic-20261106-ibuprofen-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US with 14 valid licenses, but label safety data are missing." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-ibuprofen-1 -->

**To proceed, the following is needed:**
- Mechanism of action data and a credible mechanistic link between prostaglandin inhibition and GDF5/BMP signalling, or a clear rationale limited to symptomatic pain relief
- Preclinical or observational evidence in acromesomelic dysplasia or related skeletal dysplasias
- FDA package insert warnings and contraindications, to allow safety screening
- Clarification of the current regulatory and market status, since the drug is marketed

<!-- review:begin us-lic-20261106-ibuprofen-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the current regulatory and market status, since the drug is marketed with 14 valid licenses" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-ibuprofen-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "with 14 valid licenses" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 14 valid licenses" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


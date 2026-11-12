---
layout: default
title: Leflunomide
parent: Model Prediction Only (L5)
nav_order: 842
evidence_level: L5
indication_count: 2
monitor_inn: "LEFLUNOMIDE"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-11-12
description: "Leflunomide: predicted new indication Brachydactyly-Syndactyly Syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
---

# Leflunomide
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

## Leflunomide: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome
{: .text-alpha }

## One-Sentence Summary

Leflunomide was originally used to treat rheumatoid arthritis and psoriatic arthritis.
The TxGNN model predicts it may be effective for **Brachydactyly-Syndactyly Syndrome**,
but currently **0 clinical trials** and **0 publications** support this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis; psoriatic arthritis |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 10 of 13) |
| Number of FDA Applications | 13 (active: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Leflunomide is an immunomodulatory antimetabolite whose efficacy in rheumatoid arthritis and psoriatic arthritis is established. As general background (not drawn from the compiled data), it acts through its active metabolite teriflunomide, which inhibits dihydroorotate dehydrogenase (DHODH) and pyrimidine synthesis.

No mechanistic link between leflunomide and the pathways underlying brachydactyly-syndactyly syndrome, a rare limb malformation disorder, has been established. The high TxGNN score (0.9993) is a computational prediction only and is not corroborated by any clinical or preclinical evidence. DHODH inhibition is also associated with teratogenic risk, which argues for particular caution in developmental disorders. This is general pharmacological background, not a finding from the compiled data.

A second prediction, colobomatous microphthalmia-rhizomelic dysplasia syndrome (score 0.9993), is likewise a rare congenital developmental syndrome with no supporting trials or literature, and the same concerns apply.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin us-lic-20261106-leflunomide-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Four additional ANDA authorizations (Bryant Ranch Prepack, KVK-Tech, Alembic, Burel Pharmaceuticals) are also listed as cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 13 FDA applications or NDC listings for this drug, 10 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-leflunomide-1 -->

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020905 | Arava (sanofi-aventis U.S. LLC) | Tablet, film coated | Not specified; status valid |
| ANDA211863 | Leflunomide (Lupin Pharmaceuticals) | Tablet, film coated | Not specified; status valid |
| ANDA212308 | Leflunomide (Zydus Pharmaceuticals USA) | Tablet, film coated | Not specified; status valid |
| ANDA213652 | Leflunomide (Aurobindo Pharma) | Tablet, film coated | Not specified; status valid |
| ANDA077090 | Leflunomide (AvPAK) | Tablet | Not specified; status valid |

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: The knowledge graph links leflunomide to contraindications in the following groups:
  - Liver: liver failure, liver disease, gallbladder disease, chronic hepatitis B and C virus infection
  - Kidney: kidney disease, pyoureter
  - Blood: thrombocytopenia, neutropenia (including congenital forms), agranulocytosis, pancytopenia, anemia, macrocytic anemia
  - Nerve: peripheral neuropathy, peripheral nervous system disease
  - Lung and infection: interstitial lung disease, pneumocystosis, aspergillosis
- **Drug Interactions**: 100 interactions were identified. Major-level examples include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Antidiabetics: acarbose, pioglitazone
  - Antibiotics: clarithromycin, minocycline
  - Others: bupropion, acetylsalicylic acid, naltrexone, chenodeoxycholic acid, oxandrolone, oxymetholone

  Moderate-level examples include metronidazole, chlorpropamide, and acetohexamide. Minor-level examples include zinc sulfate and zinc acetate.
- **Developmental risk**: Teratogenicity is a general pharmacological concern for this drug class, which is especially relevant for congenital developmental disorders.

Please refer to the package insert for complete warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a computational basis (L5), with no clinical trials, literature, or established mechanistic link. Leflunomide's known teratogenic risk and the rare congenital nature of the predicted conditions further weaken the case. The drug is marketed in the US.

<!-- review:begin us-lic-20261106-leflunomide-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with 9 valid licenses." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 13 FDA applications or NDC listings for this drug, 10 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-leflunomide-2 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical or mechanistic evidence connecting DHODH or pyrimidine synthesis inhibition to limb malformation pathways
- A developmental and teratogenicity risk assessment for the proposed indication
- Route compatibility and similarity-to-original-indication analyses (currently pending)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Four additional ANDA authorizations (Bryant Ranch Prepack, KVK-Tech, Alembic, Burel Pharmaceuticals) are also listed as cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 9 valid licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


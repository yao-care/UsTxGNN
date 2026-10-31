---
layout: default
title: Rivaroxaban
parent: Model Prediction Only (L5)
nav_order: 1130
evidence_level: L5
indication_count: 4
monitor_inn: "RIVAROXABAN"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
last_modified_at: 2026-10-31
description: "Rivaroxaban: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not available in the compiled data"
---

# Rivaroxaban
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

## Rivaroxaban: From Thromboembolic Disorders to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Rivaroxaban is an oral factor Xa inhibitor (anticoagulant). The data compiled for this report do not include an original indication text.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **0 registered clinical trials** and **4 publications** for this indication, none of which shows that rivaroxaban modifies rheumatoid arthritis activity or outcomes.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the approved-indication text is empty for all licenses) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 8) |
| Number of FDA Applications | at least 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge, rivaroxaban is a direct factor Xa inhibitor used for anticoagulation. Its efficacy in venous thromboembolism and atrial fibrillation is established outside this dataset, but the compiled data do not state the original indication.

The only mechanistic link is a loose one. Rheumatoid arthritis is associated with a prothrombotic state, and inflammation-driven coagulation activation (for example, increased thrombin generation) gives a rationale for factor Xa inhibition. At most, this supports thromboprophylaxis in patients who also have rheumatoid arthritis. It does not support disease-modifying activity, and no evidence shows that rivaroxaban changes rheumatoid arthritis activity or outcomes. The high TxGNN score is a network-based prediction and should be read with caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of diagnosis and treatment of lower extremity venous thromboembolism. Reports DVT incidence of 88 to 112 per 100,000 person-years and recurrence of 20% to 36% over 10 years. Not specific to rheumatoid arthritis. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Thrombin generation assay as a tool to assess hypercoagulability in autoimmune disease. Provides background on the prothrombotic state, with no rivaroxaban efficacy data. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | Adherence to rivaroxaban versus apixaban in non-valvular atrial fibrillation. Not related to rheumatoid arthritis. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | Recurrent embolic events despite anticoagulation in an 88-year-old woman with atrial fibrillation, chronic kidney disease, and rheumatoid arthritis on oral steroids. A comorbidity report only. |

## US Market Information

All 9 licenses are valid, and the approved-indication text is not available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022406 | Xarelto (Cardinal Health 107, LLC) | Film-coated tablet | Not available |
| NDA215859 | Xarelto (Janssen Pharmaceuticals, Inc.) | Granule for suspension | Not available |
| ANDA218445 | Rivaroxaban (Indoco Remedies Limited) | Film-coated tablet | Not available |
| ANDA210301 | Rivaroxaban (Alembic Pharmaceuticals Inc.) | Film-coated tablet | Not available |
| ANDA217810 | Rivaroxaban (Apotex Corp.) | Film-coated tablet | Not available |

## Safety Considerations

Package insert warnings and contraindications are not available in the compiled data. Please refer to the package insert for these.

- **Disease associations from the knowledge graph** (network-derived contraindication edges, not label text): liver failure, kidney disease, pyoureter, liver disease, gallbladder disease, and blood coagulation disease.
- **Drug Interactions**: 100 interactions were found in total. The first 20 returned include these main ones:
  - **Major**: acetylsalicylic acid (aspirin), cobicistat, deferasirox, ibritumomab tiuxetan, tositumomab (I-131).
  - **Moderate**: aprepitant, dexamethasone, cimetidine, clarithromycin, eliglustat, miconazole, clotrimazole, fenfluramine, dexfenfluramine, rolapitant, sibutramine, troglitazone, sugammadex, iodide I-131, iodide I-123.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is a model output only. There are no clinical trials and no literature showing that rivaroxaban affects rheumatoid arthritis. In addition, the drug is marketed in the US with 9 valid licenses, but the package insert safety information is missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap)
- Mechanism of action data and the original approved indications
- Preclinical or exploratory clinical evidence that factor Xa inhibition modifies rheumatoid arthritis activity
- Clarification of the cancelled US licensing status

---

*Other predicted indications were also evaluated and all are on Hold:*
- **Gout** (score 0.9951, L5): no clinical trials, and the retrieved literature does not show efficacy.
- **HIV infectious disease** (score 0.9917, L4): the evidence concerns anticoagulant safety and drug interactions with boosted antiretrovirals, not treatment of HIV. The one Phase 2 trial (NCT00786422) is a venous thromboembolism study.
- **Brachydactyly-syndactyly syndrome** (score 0.9910, L5): no trials or literature, and no plausible mechanism. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


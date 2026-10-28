---
layout: default
title: Ocrelizumab
parent: Model Prediction Only (L5)
nav_order: 981
evidence_level: L5
indication_count: 5
monitor_inn: "OCRELIZUMAB"
predicted_indications: ["HER2 positive breast carcinoma", "progesterone-receptor positive breast cancer", "normal breast-like subtype of breast carcinoma", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer"]
last_modified_at: 2026-10-28
description: "Ocrelizumab: predicted new indication HER2 positive breast carcinoma (evidence level L5). Approved use: Progressive multiple sclerosis"
---

# Ocrelizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ocrelizumab: From Progressive Multiple Sclerosis to HER2 positive breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Ocrelizumab is an anti-CD20 antibody originally used to treat progressive multiple sclerosis.
The TxGNN model predicts it may be effective for **HER2-positive breast carcinoma**,
but there are currently **0 clinical trials** and **0 publications** that specifically support this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Progressive multiple sclerosis |
| Predicted New Indication | HER2-positive breast carcinoma |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ocrelizumab is a humanized anti-CD20 monoclonal antibody that depletes CD20-expressing B cells. Its efficacy in multiple sclerosis is well established. The publications compiled for this report describe B-cell depletion as the basis of its action in that disease.

The data compiled for this report do not support a mechanistic link to HER2-positive breast carcinoma. HER2-driven tumour biology is not obviously connected to CD20-mediated B-cell depletion. The high TxGNN score (0.9989) is a computational prediction only, and no trials or publications back it.

The other top-ranked predictions are also breast cancer subtypes: progesterone-receptor positive (0.9981), normal breast-like subtype (0.9981), luminal A or B (0.9981) and progesterone-receptor negative (0.9980). The first two share an identical score, which comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Hormone-receptor signalling is not a known target of anti-CD20 therapy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for HER2-positive breast carcinoma.

For the fourth-ranked prediction (luminal A or B breast tumour), the search returned 18 publications (the 10 listed below are the most relevant to the drug). All concern multiple sclerosis or general B-cell and autoimmune topics, and none evaluates ocrelizumab in breast cancer. They appear to have been retrieved by drug name only and **should not be counted as supporting evidence** for any breast cancer indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28002688](https://pubmed.ncbi.nlm.nih.gov/28002688/) | 2017 | RCT (MS) | N Engl J Med | Ocrelizumab vs placebo in primary progressive MS (ORATORIO) |
| [28002679](https://pubmed.ncbi.nlm.nih.gov/28002679/) | 2017 | RCT (MS) | N Engl J Med | Ocrelizumab vs interferon beta-1a in relapsing MS (OPERA I/II) |
| [40245351](https://pubmed.ncbi.nlm.nih.gov/40245351/) | 2025 | RCT (MS) | Neurology | Phase 3 OCARINA II: subcutaneous vs IV ocrelizumab exposure in MS |
| [22047971](https://pubmed.ncbi.nlm.nih.gov/22047971/) | 2011 | RCT (MS) | Lancet | Phase 2 placebo-controlled trial in relapsing-remitting MS |
| [37307006](https://pubmed.ncbi.nlm.nih.gov/37307006/) | 2023 | Cohort | JAMA Neurol | Rituximab vs ocrelizumab in relapsing-remitting MS |
| [35192158](https://pubmed.ncbi.nlm.nih.gov/35192158/) | 2022 | Review | Drugs | Review of ocrelizumab in MS |
| [37033984](https://pubmed.ncbi.nlm.nih.gov/37033984/) | 2023 | Review | Front Immunol | Anti-CD20 therapies in MS, from pathology to clinic |
| [35176351](https://pubmed.ncbi.nlm.nih.gov/35176351/) | 2022 | Review/Guidance | J Allergy Clin Immunol | Diagnosis and management of secondary hypogammaglobulinemia |
| [38642912](https://pubmed.ncbi.nlm.nih.gov/38642912/) | 2024 | Review | Clin Exp Immunol | B- and T-cell collaboration in autoimmune disease: T-cell engagers vs CAR T |
| [39339212](https://pubmed.ncbi.nlm.nih.gov/39339212/) | 2024 | Review | Pharmaceutics | Biologics in systemic lupus erythematosus |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761053 | OCREVUS (Genentech, Inc.) | Injection | Status: valid |
| BLA761371 | Ocrevus Zunovo (Genentech, Inc.) | Injection, solution | Status: valid |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. The ones listed are mostly Moderate.
  - Corticosteroids (Moderate): hydrocortisone, triamcinolone (including ophthalmic), dexamethasone, betamethasone, budesonide, prednisolone, prednisone.
  - Radiopharmaceuticals and radioimmunotherapies (Moderate): iobenguane (I-131), ibritumomab tiuxetan, tositumomab (including I-131), samarium (153Sm) lexidronam.
  - Anti-infectives (Moderate): albendazole, pentamidine, levamisole.
  - Zinc salts (Minor): sulfate, acetate, gluconate, chloride.
- **Related literature note**: One review in the compiled literature covers secondary hypogammaglobulinemia, a known concern with B-cell-depleting immunosuppressive therapy.

For key warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no clinical trials or breast-cancer-specific publications, and no supported mechanistic link between CD20 B-cell depletion and HER2-positive breast carcinoma. All US licences for the drug are also listed as cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A mechanistic rationale connecting CD20-targeted B-cell depletion to HER2-positive breast cancer, for example the role of tumour-infiltrating B cells
- Preclinical or early-phase clinical evidence in breast cancer
- Clarification of the current US marketing status, since both BLA records show as cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


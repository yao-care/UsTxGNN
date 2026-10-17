---
layout: default
title: Enfortumab Vedotin
parent: Model Prediction Only (L5)
nav_order: 653
evidence_level: L5
indication_count: 9
monitor_inn: "ENFORTUMAB VEDOTIN"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "malignant catarrh", "infectious bovine rhinotracheitis"]
last_modified_at: 2026-10-14
description: "Enfortumab Vedotin: predicted new indication Leprosy (evidence level L5). Approved use: Urothelial carcinoma"
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: From Urothelial Carcinoma to Leprosy

## One-Sentence Summary

Enfortumab vedotin is a Nectin-4-directed antibody-drug conjugate (with an MMAE payload) marketed as PADCEV for urothelial carcinoma.
The TxGNN model predicts it may be effective for **leprosy**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction is purely computational.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urothelial carcinoma (from general drug knowledge; the US license record in the compiled data has no indication text) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA761137) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, enfortumab vedotin is an antibody-drug conjugate that targets Nectin-4 and delivers monomethyl auristatin E (MMAE), a microtubule-disrupting cytotoxic agent. Its efficacy has been established in urothelial carcinoma.

No plausible mechanistic link to leprosy was identified. Leprosy is a *Mycobacterium leprae* infection, and a cytotoxic payload aimed at Nectin-4-expressing tumour cells has no known antibacterial activity. The high TxGNN score is best read as a model output, not as biological support. Immunosuppression and cytotoxicity would also be a safety concern in this setting.

Other top-ranked predictions show the same pattern, with no supporting data or plausible mechanism:
- Multiple endocrine neoplasia (99.43%): Nectin-4 expression in these tumours is not established.
- Cytomegalovirus infection (99.36%): the only linked paper is a case report of an adverse event (esophagitis), not a therapeutic benefit.
- Candidiasis (99.30%): the only linked paper is a pharmacovigilance study of ADC risk signals, not a therapeutic effect.
- Cerebral infarction, HIV infection, homozygous familial hypercholesterolemia, malignant catarrh and infectious bovine rhinotracheitis: all prediction-only. The last two are veterinary diseases and likely ontology-mapping artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for leprosy.

For reference, the two papers linked to other predicted indications report safety signals, not benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42647281](https://pubmed.ncbi.nlm.nih.gov/42647281/) | 2026 | Case report | Reports (MDPI) | Severe diffuse ulcerative esophagitis after enfortumab vedotin plus pembrolizumab in metastatic urothelial carcinoma (linked to cytomegalovirus infection) |
| [41341429](https://pubmed.ncbi.nlm.nih.gov/41341429/) | 2025 | Pharmacovigilance cohort | Clinical Epidemiology | Real-world FAERS analysis of ADC risk signals in bladder cancer (linked to candidiasis) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761137 | PADCEV (Seagen Inc.) | Lyophilized powder for injection solution | Not listed in the compiled data (status: cancelled) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic payload (MMAE, microtubule inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (neutropenia is a concern per the payload class) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, blood glucose (hyperglycemia is a known toxicity), liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the DDI screen. The entries listed are mainly Moderate, and one is Major:
  - **Major**: Clarithromycin
  - **Moderate**: Many antidiabetic agents, including metformin, pioglitazone, acarbose, albiglutide, alogliptin, saxagliptin, linagliptin, dulaglutide, exenatide, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, and the sulfonylureas (chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide), plus aprepitant.
- Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanism. The cytotoxic payload also raises safety concerns for an infectious disease. The US license record is cancelled, and the package insert safety data is missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking Nectin-4 or MMAE to *M. leprae* infection
- Confirmation of the current US regulatory status and approved indication text for PADCEV
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


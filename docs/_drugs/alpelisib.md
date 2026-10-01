---
layout: default
title: Alpelisib
parent: Model Prediction Only (L5)
nav_order: 227
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Alpelisib: From Its Marketed Uses to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib is a PI3K-alpha inhibitor marketed in the US as PIQRAY and VIJOICE. The Evidence Pack does not record its approved indication text.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but **0 relevant clinical trials** and **0 supportive publications** back this direction. The only lung-related paper is a case report of alpelisib-induced interstitial lung disease, which is a safety signal rather than evidence of benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 records (3 unique NDA numbers) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Alpelisib is known as a PI3K-alpha inhibitor, and PI3K/Akt signaling plausibly plays a role in pulmonary vascular remodeling, which is a hallmark of pulmonary hypertension. This link comes from general pathway knowledge, not from the supplied data, and it remains unproven.

A high TxGNN score (99.03%) reflects a pattern in the knowledge graph, not clinical confirmation. Nothing in the supplied evidence shows that inhibiting PI3K-alpha would help patients with pulmonary hypertension. Direction of effect is also unclear, because the PI3K pathway is involved in both vascular growth and cardiac function.

The available literature raises caution rather than support. One report describes alpelisib-induced interstitial lung disease, and a preclinical study found that PI3K-alpha inhibition combined with doxorubicin caused right ventricular dysfunction. Both would need to be weighed before any pulmonary hypertension work.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Completed | 435 | Retrospective real-world study (REASSURE) of ribociclib or alpelisib in HR+/HER2- advanced or metastatic breast cancer. Not related to pulmonary hypertension (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case report | J Oncol Pharm Pract | Alpelisib-induced interstitial lung disease in a patient with advanced breast cancer. A pulmonary safety signal, not evidence of benefit. |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical study | J Am Heart Assoc | PI3K-alpha inhibition with doxorubicin caused biventricular atrophy, remodeling and right ventricular dysfunction. A cardiac toxicity model, not pulmonary hypertension. |

---

## US Market Information

The Evidence Pack lists 5 license records covering 3 unique NDAs. No approved indication text was provided.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA212526 | PIQRAY | Tablet |
| NDA215039 | VIJOICE | Tablet |
| NDA218466 | VIJOICE | Granule |

All are held by Novartis Pharmaceuticals Corporation.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3K-alpha kinase inhibitor). Classified from the drug class and the breast cancer context of the retrieved trial and literature, since no indication text was provided. |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried database.
- **Signals from the literature**: A case report links alpelisib to interstitial lung disease. A preclinical study shows right ventricular dysfunction under PI3K-alpha inhibition combined with doxorubicin. Both are relevant to a pulmonary hypertension population.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no relevant clinical trials and no supportive literature. The available lung and cardiac signals point toward possible harm, and the drug's mechanism and label safety data are missing from the record.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank)
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for each NDA, to establish the original indication
- Preclinical evidence on PI3K-alpha inhibition in pulmonary hypertension models, including direction of effect
- A pulmonary and right-heart safety assessment (interstitial lung disease and right ventricular function)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


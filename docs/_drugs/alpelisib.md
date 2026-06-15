---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Alpelisib: From Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib is a selective PI3Kα inhibitor used in the treatment of PIK3CA-mutated HR+/HER2− advanced or metastatic breast cancer.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with a prediction score of 99.03%; however, the supporting evidence consists of **1 clinical trial** (grade C, unrelated to pulmonary hypertension) and **2 publications** — neither of which directly demonstrates clinical efficacy for this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | PIK3CA-mutated HR+/HER2− advanced/metastatic breast cancer (inferred from retrieved evidence; no Taiwan license on record) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (0 licenses) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on the retrieved evidence, alpelisib is a selective inhibitor of PI3Kα (phosphoinositide 3-kinase alpha), the catalytic subunit encoded by *PIK3CA*. It blocks the PI3K/AKT/mTOR signaling cascade, which is constitutively activated in PIK3CA-mutated breast cancers.

The mechanistic link to pulmonary hypertension rests on the known role of the PI3Kα/AKT/mTOR axis in pulmonary arterial smooth muscle cell (PASMC) proliferation and vascular remodeling. Pathological PASMC hyperproliferation is a hallmark of pulmonary arterial hypertension (PAH), and preclinical studies have implicated PI3K signaling in driving this process. TxGNN derived this prediction computationally via knowledge graph traversal, connecting alpelisib's PI3Kα target to disease nodes associated with pulmonary vascular pathology.

Critically, however, the retrieved evidence raises a safety concern rather than a therapeutic signal: one preclinical paper (PMID 31039672) demonstrates that PI3Kα pathway inhibition combined with doxorubicin causes biventricular atrophy and **right ventricular dysfunction** — the very organ system most vulnerable in pulmonary hypertension. This suggests the drug's mechanism could be harmful rather than beneficial in this context, and no human clinical data exists to support its use in PH.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A (Observational) | Completed | 435 | Real-world retrospective cohort of HR+/HER2− advanced/metastatic breast cancer patients treated with ribociclib or alpelisib (2018–2021). **Relevance grade C — no connection to pulmonary hypertension.** This trial provides no evidence for the predicted indication. |

> ⚠️ The sole retrieved trial is entirely unrelated to pulmonary hypertension. Its inclusion reflects a broad database query; it does not constitute supporting evidence for this repurposing hypothesis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical (Animal) | J Am Heart Assoc | PI3Kα inhibition combined with doxorubicin causes biventricular atrophy and **right ventricular dysfunction** in animal models. Mechanistically relevant but suggests cardiac harm, not therapeutic benefit, in pulmonary hypertension. |
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | J Oncol Pharm Pract | Reports alpelisib-induced **interstitial lung disease (ILD)** as an adverse event in an advanced breast cancer patient. Demonstrates alpelisib has pulmonary toxicity potential; does not support its use in pulmonary hypertension. |

> ⚠️ Neither publication provides efficacy evidence for alpelisib in pulmonary hypertension. Both raise safety concerns relevant to this indication (pulmonary toxicity and right ventricular dysfunction).

---

## Taiwan Market Information

Alpelisib has **no approved licenses** in Taiwan. No product name, dosage form, or approved indication data is available.

---

## Cytotoxicity

Alpelisib is an antineoplastic targeted therapy (PI3Kα inhibitor class) used in oncology.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective PI3Kα inhibitor (kinase inhibitor class) |
| Myelosuppression Risk | Low (kinase inhibitors generally have lower myelosuppression than conventional cytotoxics; specific data not available in this pack) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Blood glucose (hyperglycemia is a class effect of PI3K inhibitors), CBC, liver and renal function, pulmonary function if respiratory symptoms develop |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: All safety fields (key warnings, contraindications, drug-drug interactions) are marked as data gaps in this Evidence Pack. The TFDA package insert and DrugBank records should be retrieved before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure TxGNN model prediction (Evidence Level L5) with no direct clinical evidence supporting alpelisib in pulmonary hypertension. The only retrieved clinical trial is irrelevant (grade C, breast cancer observational study), and both retrieved publications describe adverse effects — pulmonary toxicity and right ventricular dysfunction — that are particularly concerning given that right heart failure is the primary cause of death in pulmonary hypertension patients.

**To proceed, the following is needed:**

- **MOA data gap resolution**: Obtain full DrugBank MOA entry to formally characterize PI3Kα inhibition relevance to PASMC biology
- **Safety data gap resolution**: Retrieve Taiwan package insert (TFDA) and DrugBank warnings/contraindications before any S1 safety screen can proceed
- **Dedicated PH preclinical literature search**: Conduct a targeted PubMed search for alpelisib + pulmonary arterial hypertension / PASMC / vascular remodeling to establish whether any preclinical PH efficacy data exists
- **Cardiac safety clarification**: The RV dysfunction signal (PMID 31039672) must be assessed for clinical relevance at therapeutic doses before this hypothesis can advance
- **Regulatory pathway assessment**: Since alpelisib is not marketed in Taiwan, confirm US FDA approval status (Piqray/Vijoice) and consult international labeling for safety reference
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


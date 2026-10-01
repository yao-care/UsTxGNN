---
layout: default
title: Thiamine
parent: Model Prediction Only (L5)
nav_order: 1221
evidence_level: L5
indication_count: 4
---

# Thiamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Thiamine: From Vitamin B1 Supplementation to Hyperthyroidism

## One-Sentence Summary

Thiamine (vitamin B1) is marketed in the US as an injectable product, and the Evidence Pack contains no approved-indication text for it.
The TxGNN model predicts it may be relevant to **hyperthyroidism**, with **1 small clinical trial** and **20 publications** (mostly case reports) supporting this direction.
The evidence points to correcting a thiamine deficiency that accompanies hyperthyroidism, not to treating the thyroid disease itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hyperthyroidism |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 (weak: one small pilot trial plus case reports) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the licenses listed are ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Thiamine is a cofactor for pyruvate dehydrogenase and transketolase, so it supports energy metabolism. This comes from the literature, not from the Evidence Pack's MOA field.

Hyperthyroidism raises metabolic rate and thiamine turnover. Relative thiamine deficiency is documented in hyperthyroid patients. It appears as beriberi-like high-output heart failure and as Wernicke's encephalopathy, especially with vomiting, pregnancy or bariatric surgery. Thiamine could therefore help as adjunct therapy for a comorbid deficiency and for cardiovascular function.

There is no evidence that thiamine treats the thyroid disease itself. The very high TxGNN score reflects proximity in the knowledge graph, not clinical proof.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02767245](https://clinicaltrials.gov/study/NCT02767245) | NA | Completed | 12 | Pilot study of thiamine supplementation in severe hyperthyroidism. It measures thiamine deficiency prevalence and cardiovascular function. No results are available in the pack. |

The trial tests thiamine directly in hyperthyroid patients. It is small, has no formal phase, and its endpoint is cardiovascular function rather than thyroid control. It cannot support a higher evidence level.

---

## Literature Evidence

No randomized trials or systematic reviews were found. The most relevant publications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32983708](https://pubmed.ncbi.nlm.nih.gov/32983708/) | 2020 | Case report | Cureus | Wernicke's encephalopathy with transient gestational hyperthyroidism and hyperemesis |
| [18026802](https://pubmed.ncbi.nlm.nih.gov/18026802/) | 2008 | Case report | J Gen Intern Med | Thyrotoxicosis-associated Wernicke's encephalopathy |
| [36176825](https://pubmed.ncbi.nlm.nih.gov/36176825/) | 2022 | Case report | Cureus | Hyperthyroidism presenting as Wernicke's encephalopathy with severe neurological consequences |
| [25148818](https://pubmed.ncbi.nlm.nih.gov/25148818/) | 2014 | Case report | Endocr Pract | Gestational thyrotoxicosis with Wernicke's encephalopathy |
| [26567494](https://pubmed.ncbi.nlm.nih.gov/26567494/) | 2015 | Case report / clinical review | Crit Care Nurs Clin North Am | High-output heart failure caused by thyrotoxicosis and wet beriberi |
| [34995426](https://pubmed.ncbi.nlm.nih.gov/34995426/) | 2021 | Case report | S D Med | Visual disturbances from Wernicke encephalopathy in a Graves' disease patient after sleeve gastrectomy |
| [36593922](https://pubmed.ncbi.nlm.nih.gov/36593922/) | 2023 | Case report | Radiol Case Rep | Wernicke-Korsakoff syndrome in a pregnant woman with pre-gestational hyperthyroidism |
| [32934066](https://pubmed.ncbi.nlm.nih.gov/32934066/) | 2020 | Case report | Clin Med (Lond) | Wernicke's encephalopathy at 17 weeks of pregnancy after hyperemesis and thyrotoxicosis |
| [22436368](https://pubmed.ncbi.nlm.nih.gov/22436368/) | 2013 | Case report | Neurologia | Wernicke's encephalopathy secondary to hyperthyroidism and thiaminase-rich products |
| [13305517](https://pubmed.ncbi.nlm.nih.gov/13305517/) | 1955 | Small physiological study | Endocrinol Sci Cost | Urinary thiamine after intravenous cocarboxylase load in hyperthyroid and normal subjects |

---

## US Market Information

The Evidence Pack has no approved-indication text for these products. The 5 main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA217181 | Thiamine Hydrochloride | Injection, solution | OneSource Specialty Pharma Limited |
| ANDA215692 | Thiamine | Injection, solution | Caplin Steriles Limited |
| ANDA080571 | Thiamine Hydrochloride injection, solution | Injection, solution | HF Acquisition Co LLC, DBA HealthFirst |
| ANDA206106 | Thiamine Hydrochloride | Injection, solution | Sagent Pharmaceuticals |
| ANDA215692 | Thiamine | Injection, solution | NorthStar Rx LLC |

Only injectable and solution forms appear in the pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is one small (n=12) pilot trial without available results, plus case reports linking hyperthyroidism to thiamine deficiency. The plausible role is correcting a comorbid deficiency, not treating hyperthyroidism. The other predicted indications (thyroid hormone resistance, hereditary glaucoma, open-angle glaucoma) have no or only indirect evidence and are not worth pursuing now. This remains a research question.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data and the original approved indications (for example from DrugBank)
- Results of NCT02767245, or a new randomized trial of thiamine in hyperthyroid patients with confirmed deficiency, with cardiovascular and neurological endpoints
- A clear framing of the target: thiamine-deficiency comorbidity, not the thyroid disease itself

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Propylthiouracil
parent: Moderate Evidence (L3-L4)
nav_order: 1095
evidence_level: L4
indication_count: 3
---

# Propylthiouracil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Propylthiouracil: From Hyperthyroidism (Antithyroid Therapy) to Resistance to Thyroid Hormone (THRB Mutation)

## One-Sentence Summary

Propylthiouracil (PTU) is an established antithyroid drug that lowers thyroid hormone production. The TxGNN model predicts it may be effective for **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (RTH-beta)**. However, this direction has **0 clinical trials** and **6 publications** (case reports and animal studies), none of which reports PTU as a treatment for the condition.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 8 (the listed authorizations are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this record. Based on the evidence pack's analysis, PTU inhibits thyroid peroxidase and blocks peripheral conversion of T4 to T3, which lowers circulating thyroid hormone.

The high TxGNN score most likely reflects graph proximity between PTU and thyroid hormone pathway nodes, not a therapeutic relationship. In RTH-beta, T4 and T3 are elevated to compensate for reduced receptor sensitivity. Lowering hormone levels would likely raise TSH and can enlarge the goiter. The mechanism therefore points to potential **harm** rather than benefit.

The literature agrees. In the Thai patient (PMID 10724359), goiter became more enlarged after nine months of PTU given for a mistaken diagnosis of thyrotoxicosis. This prediction is best treated as a model artifact, and it should not be pursued as a therapeutic hypothesis without new supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18561095](https://pubmed.ncbi.nlm.nih.gov/18561095/) | 2009 | Case Report | Exp Clin Endocrinol Diabetes | P453A THRB mutation in a Turkish family (mother and son); describes the RTH-beta phenotype, no PTU treatment reported |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case Report | Endocr J | De novo L330S mutation in a Thai woman. She was treated with PTU for 9 months under a mistaken thyrotoxicosis diagnosis, and her goiter enlarged |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case Report | Clin Endocrinol | M313T mutation family with neonatal thyrotoxicosis features and maternal infertility |
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | Preclinical/Mechanistic | Endocrinology | Role of the TR-beta isoform in thyroid hormone resistance in the heart of a mouse model |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Preclinical (mouse model) | Endocrinology | Role of TSH in spontaneous thyroid carcinoma in mice with a single mutated THRB allele |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Preclinical (mouse model) | Oncogene | Thyroid hormone activates tumor cell proliferation in a mouse model of follicular thyroid carcinoma |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA080016 | Propylthiouracil | Tablet | Chartwell RX, LLC |
| ANDA080154 | Propylthiouracil | Tablet | Quagen Pharmaceuticals LLC |
| ANDA080172 | Propylthiouracil | Tablet | Teva Pharmaceuticals, Inc. |
| ANDA208867 | Propylthiouracil | Tablet | Macleods Pharmaceuticals Limited |
| ANDA080154 | Propylthiouracil | Tablet | Bryant Ranch Prepack |

All listed products are oral tablets. Approved indication text is not included in the source data.

## Safety Considerations

- **Hepatotoxicity**: The evidence pack's analysis notes that PTU carries a boxed warning for hepatotoxicity.

No other structured safety data is available. Please refer to the package insert for complete warnings, contraindications, and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is at L4 (case reports and mouse models only). There are no clinical trials, and the mechanism suggests PTU could worsen RTH-beta by lowering hormone levels and raising TSH.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap for safety screening)
- Confirmed original indications and mechanism-of-action data from DrugBank
- Any evidence that lowering thyroid hormone benefits RTH-beta patients, which is currently absent

**Note:** For the same drug, the lower-ranked prediction **neonatal thyrotoxicosis** (L3) is better supported. It has a Phase 3 trial of thionamides in Graves' disease and several pregnancy-related reviews and cohorts. It is more plausible mechanistically, but because PTU is already an established antithyroid drug, it may not be true repurposing.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


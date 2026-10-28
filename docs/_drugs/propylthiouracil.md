---
layout: default
title: Propylthiouracil
parent: Moderate Evidence (L3-L4)
nav_order: 1095
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "PROPYLTHIOURACIL"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
description: "Propylthiouracil: predicted new indication Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (evidence level L4). Approved use: Not recorded in the local data"
---

# Propylthiouracil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

## Propylthiouracil: Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta
{: .text-alpha }

## One-Sentence Summary

Propylthiouracil (PTU) is an antithyroid drug originally used to treat hyperthyroidism, Graves disease, thyrotoxicosis and thyroid crisis.
The TxGNN model predicts it may be effective for **resistance to thyroid hormone due to a THRB mutation**, but **no clinical trials** and only **4 publications** (case reports and mouse studies, none testing PTU as a treatment) are available.
The prediction comes from the TxGNN model (deep learning) and is not supported by clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L4 |
| US Market Status | Marketed (valid licenses: 5 of 5) |
| Number of NDAs | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, PTU inhibits thyroid peroxidase, which reduces thyroid hormone synthesis, and it also blocks peripheral conversion of T4 to T3. This is why it works in hyperthyroidism and Graves disease.

The predicted indication is a different kind of problem. In resistance to thyroid hormone (RTH beta), mutations in the THRB gene make tissues respond poorly to circulating thyroid hormone. Hormone levels are high, but the defect lies in the receptor. Lowering hormone levels is therefore mechanistically questionable. It could worsen hypothyroidism in resistant tissues and push TSH higher, which may enlarge the goitre. One published case in the compiled literature fits this concern: a patient with RTH was treated with PTU for presumed thyrotoxicosis, and her goitre became larger.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases (shared thyroid-hormone biology), not biological evidence that PTU helps these patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Animal study (mouse) | Endocrinology | In mice carrying a THRB mutation (RTH model), TSH drives the development of asymmetrical thyroid carcinoma. PTU was not tested as therapy. |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Animal study (mouse) | Oncogene | In a mouse model of follicular thyroid carcinoma with a dominant-negative THRB mutation, thyroid hormone activates tumour cell proliferation. |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case report | Clinical Endocrinology | Family with RTH (M313T mutation): neonatal thyrotoxicosis in an infant and maternal infertility. |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case report | Endocrine Journal | A Thai woman with a de novo L330S THRB mutation was treated with PTU for presumed thyrotoxicosis, and her goitre became more enlarged. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA080016 | Propylthiouracil (Chartwell RX, LLC) | Tablet | Not available (valid) |
| ANDA080154 | Propylthiouracil (Quagen Pharmaceuticals LLC) | Tablet | Not available (valid) |
| ANDA080172 | Propylthiouracil (Teva Pharmaceuticals, Inc.) | Tablet | Not available (valid) |
| ANDA208867 | Propylthiouracil (Macleods Pharmaceuticals Limited) | Tablet | Not available (valid) |
| NDA006188 | Propylthiouracil (American Health Packaging) | Tablet | Not available (valid) |

All five authorizations are oral tablets and all are listed as cancelled.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Knowledge-graph contraindications** (not label text): thrombocytopenia, hypothyroidism, myxedema, congenital hypothyroidism, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), interstitial lung disease, drug-induced liver injury, and leukopenia, pancytopenia, agranulocytosis and neutropenia (including several congenital neutropenia syndromes).
  - The hypothyroidism-related entries are directly relevant to RTH, where lowering hormone levels may be harmful.
- **Drug interactions**: 83 interactions were identified. The main ones are:
  - **Major**: deferiprone.
  - **Moderate**: naltrexone, iodide I-131, iodide I-123, macimorelin, warfarin, dicoumarol, theophylline, aminophylline, oxtriphylline.
  - Many others (e.g., omeprazole, pantoprazole, corticosteroids, clopidogrel, rosuvastatin) have no assigned severity level.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials and the literature consists only of case descriptions and mouse models, none testing PTU as therapy. The mechanism points the wrong way: reducing thyroid hormone in patients whose tissues already respond poorly to it may cause harm. All 5 US authorizations are valid, and the drug is marketed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap)
- Mechanism of action data from DrugBank
- A clear mechanistic rationale for lowering hormone synthesis in THRB-mutation RTH, supported by preclinical data
- Any clinical evidence of PTU benefit in RTH, as opposed to the reported goitre enlargement

---

*Other predictions of lower priority, for context:*

- **Neonatal thyrotoxicosis**: This is mechanistically close to PTU's original use. The evidence is mostly reviews on maternal hyperthyroidism in pregnancy, where PTU is used, plus one cohort study (PMID 25747892). Direct treatment of the neonate is not established, and a case report (PMID 2090674) describes neonatal hepatitis after placental PTU transfer. It is best framed as a research question.
- **Hyperthyroxinemia** (score 0.9908, L4): This is a laboratory finding with many causes. Antithyroid treatment is plausible only when it reflects true hormone overproduction, and it could harm patients with binding-protein abnormalities or hormone resistance. The evidence is case reports and animal studies, so the recommendation is Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


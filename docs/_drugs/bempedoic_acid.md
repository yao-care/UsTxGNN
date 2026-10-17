---
layout: default
title: Bempedoic Acid
parent: Model Prediction Only (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bempedoic Acid: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Not available"
monitor_inn: "BEMPEDOIC ACID"
predicted_indications: ["hyperthyroidism", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "infectious bovine rhinotracheitis", "malignant catarrh", "cytomegalovirus infection", "hyperthyroxinemia", "drug-induced osteoporosis", "multiple endocrine neoplasia", "pregnancy associated osteoporosis"]
---

# Bempedoic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Bempedoic Acid: From Lipid Lowering (Original Indication Not Recorded) to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Bempedoic acid is an oral lipid-lowering drug that inhibits ATP-citrate lyase in the liver. The data compiled for this report do not include an approved-indication text for it.
The TxGNN model's top-ranked prediction is **hyperthyroidism**, but that prediction has no supporting evidence. The best-supported prediction is **homozygous familial hypercholesterolemia (HoFH)**, which has **0 clinical trials** and **18 publications** (mostly reviews, plus one real-world cohort study).

This report therefore focuses on HoFH (TxGNN rank 6 of the 10 predictions), because it is the only prediction with any literature support. The top-ranked prediction, hyperthyroidism, is addressed briefly below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the license records contain no indication text) |
| Predicted New Indication | Homozygous familial hypercholesterolemia (best-supported prediction; the top-ranked prediction is hyperthyroidism) |
| TxGNN Prediction Score | 99.48% for HoFH (99.61% for hyperthyroidism) |
| Evidence Level | L3 (observational and review literature only; no registered trials) |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 2 |
| Recommended Decision | Hold (HoFH is a research question; the other nine predictions have no supporting evidence) |

## Why is This Prediction Reasonable?

Bempedoic acid inhibits ATP-citrate lyase (ACL), an enzyme that acts upstream of HMG-CoA reductase, the statin target. Blocking it reduces cholesterol synthesis in the liver and increases LDL receptor expression, which lowers LDL cholesterol. The mechanism of action field in the compiled data is empty, so this description comes from the mechanistic rationale in the prediction analysis.

HoFH is a rare genetic disorder with extremely high LDL cholesterol, and it is a lipid-lowering target. The mechanistic fit is therefore strong. A key limitation is that bempedoic acid depends on residual LDL receptor function, which is often severely impaired in HoFH, so its efficacy may be limited. One real-world study (PMID 41274797) evaluated bempedoic acid in HoFH patients, but the data compiled here include only its objective, not its results.

The other nine predictions are weak:
- **Hyperthyroidism, hyperthyroxinemia, and thyroid hormone resistance (beta receptor mutation):** There is no established mechanistic link. For thyroid hormone resistance, an indirect overlap through hepatic cholesterol handling is only speculative.
- **Infectious bovine rhinotracheitis and malignant catarrh:** These are veterinary herpesvirus diseases and are likely knowledge-graph artifacts.
- **Cytomegalovirus infection:** Only a hypothetical link through host lipid and acetyl-CoA metabolism.
- **Drug-induced osteoporosis, pregnancy-associated osteoporosis, and multiple endocrine neoplasia:** No identified link. Use in pregnancy would also raise safety concerns.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The data compiled for this report contain 18 publications for HoFH. The table lists those with the most relevant study types, and abstracts are truncated, so findings are summarized only at the level the data allow.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Cohort | J Clin Lipidol | Real-world evaluation of bempedoic acid efficacy and tolerability in HoFH patients (results not available in the compiled data) |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Review (consensus) | J Clin Lipidol | National Lipid Association expert consensus update on familial hypercholesterolemia |
| [42761917](https://pubmed.ncbi.nlm.nih.gov/42761917/) | 2026 | Review | Methodist DeBakey Cardiovasc J | Overview of familial hypercholesterolemia, a monogenic disorder with severely elevated LDL-C |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Review | Exp Mol Pathol | Innovative therapies for managing HoFH |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Review | Am J Prev Cardiol | Importance of sustained LDL-C lowering in ASCVD prevention |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Traditional and novel non-statin lipid-lowering drugs |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Review | Cardiol Rev | Evinacumab for HoFH, with bempedoic acid among the other options discussed |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Review | J Atheroscler Thromb | Advancements in HoFH treatment; management centers on aggressive LDL-C reduction |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | Emerging LDL-C-lowering therapies, including bempedoic acid and inclisiran |
| [34081216](https://pubmed.ncbi.nlm.nih.gov/34081216/) | 2021 | Review | Curr Cardiol Rep | Updates in management of familial and refractory hypercholesterolemias |

No literature was provided for the other nine predicted indications.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211616 | Nexletol (Esperion Therapeutics) | Film-coated tablet | Not available; license status: cancelled |
| NDA211617 | Nexlizet (Esperion Therapeutics) | Film-coated tablet | Not available; license status: cancelled |

Both licenses are recorded as cancelled, so the data show no currently valid US license. Both are oral products.

## Safety Considerations

- **Drug Interactions:** The data list 23 interactions in total, of which 20 are itemized.
  - **Major:** Simvastatin, levofloxacin, and a group of corticosteroids (hydrocortisone, prednisone, prednisolone, methylprednisolone, dexamethasone, betamethasone, triamcinolone, budesonide, deflazacort, fludrocortisone).
  - **Moderate:** Rosuvastatin, empagliflozin, glyburide, repaglinide, rifaximin, selexipag, fexofenadine, revefenacin.

Please refer to the package insert for warnings and contraindications, as none are available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only HoFH has any supporting literature, and that is limited to one real-world cohort and reviews, with no registered trials. The mechanism is plausible but may be limited by impaired LDL receptor function in HoFH. The remaining nine predictions, including the top-ranked hyperthyroidism, rest on model scores alone. Package-insert safety data are missing, and the US licenses are cancelled.

**To proceed, the following is needed:**
- Full review of the HoFH real-world study (PMID 41274797) for efficacy and tolerability results
- Prospective controlled trial data in HoFH, ideally stratified by residual LDL receptor function
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmation of the original approved indication and the reason for license cancellation
- Detailed mechanism of action data from DrugBank
- Drug interaction management plan, especially for statins and corticosteroids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


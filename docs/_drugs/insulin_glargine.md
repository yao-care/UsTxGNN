---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 799
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Insulin Glargine: From Diabetes Mellitus to Pancreatic Agenesis

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin analog used for diabetes mellitus. Among 10 TxGNN-predicted new indications, the top-ranked candidates by raw score (e.g., autoimmune oophoritis, stiff person syndrome) carry **no supporting clinical trials or literature** and are flagged in the evidence pack's own rationale as likely model noise. The only candidate with actual supporting evidence is **Pancreatic Agenesis**, backed by **6 publications** (no clinical trials), where insulin replacement is mechanistically a near-direct extension of its known use rather than a novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (general pharmacological knowledge — not verifiable from this evidence pack; drug not marketed in Taiwan, no license text available) |
| Predicted New Indication | Pancreatic Agenesis |
| TxGNN Prediction Score | 99.43% (rank 118 of predictions) |
| Evidence Level | L4 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for insulin glargine in this evidence pack (Data Gap). Based on known pharmacology, insulin glargine is a long-acting basal insulin analog whose efficacy in diabetes mellitus — replacing deficient or absent endogenous insulin — is well established and forms the standard of care for insulin-deficient states.

Pancreatic agenesis is a rare congenital condition (associated with mutations such as *PTF1A* or *GATA6*) in which the pancreas fails to develop normally, resulting in absolute deficiency of insulin-producing beta cells and consequent neonatal or permanent diabetes mellitus. Mechanistically, this is not a distant repurposing target: exogenous insulin is the direct, physiologically necessary replacement therapy for the insulin deficiency caused by the malformed pancreas, analogous to its established role in Type 1 diabetes. The TxGNN model's high score for this indication likely reflects this direct causal relationship rather than a novel biological hypothesis — it is best understood as an established clinical practice extension rather than a true "new use."

By contrast, several higher-scoring predictions in this evidence pack (autoimmune oophoritis, thiamine-responsive dysfunction syndrome, stiff person/stiff limb syndrome, opsismodysplasia, and the lipodystrophy cluster) either lack any plausible mechanistic link to insulin, or — in the case of the lipodystrophy predictions — appear to represent the model mistaking a known **adverse effect** of insulin injection (localized lipohypertrophy/lipoatrophy) for a treatment relationship. None of these are pursued further in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11727406](https://pubmed.ncbi.nlm.nih.gov/11727406/) | 2001 | Review | Endocrinology and Metabolism Clinics of North America | Reviews insulin therapy in type 2 diabetes, including intensive glucose control benefits shown in UKPDS |
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | Journal of the American Pharmaceutical Association | Reviews practical aspects of initiating insulin therapy in type 2 diabetes |
| [19322513](https://pubmed.ncbi.nlm.nih.gov/19322513/) | 2009 | Review | Acta Diabetologica | Reviews secondary diabetes from endocrinopathies causing insulin resistance and impaired glucose tolerance |
| [25818213](https://pubmed.ncbi.nlm.nih.gov/25818213/) | 2015 | Cohort (Veterinary) | Journal of Veterinary Internal Medicine | Evaluates pancreatic enzyme markers in diabetic cats without clinically apparent pancreatitis |
| [32871938](https://pubmed.ncbi.nlm.nih.gov/32871938/) | 2020 | Case Report | Medicine | MODY type 5 (pancreatic dysfunction) case treated with GLP-1 receptor agonist, not insulin glargine |
| [18518815](https://pubmed.ncbi.nlm.nih.gov/18518815/) | 2008 | Case Report (Veterinary) | Journal of the American Veterinary Medical Association | Chronic pancreatitis with secondary diabetes in a sea lion treated with insulin |

**Note:** None of these publications directly study insulin glargine in human pancreatic agenesis; they support the mechanistic rationale (insulin deficiency → insulin therapy) rather than disease-specific efficacy.

---

## US Market Information

Insulin glargine is currently not marketed in Taiwan and no license records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pancreatic agenesis causes an absolute insulin deficiency for which exogenous insulin is a physiologically direct and clinically established replacement, giving this prediction strong mechanistic plausibility. However, no clinical trials or disease-specific studies test insulin glargine in pancreatic agenesis patients — the supporting literature addresses general insulin therapy and related conditions only, placing this at evidence level L4 (mechanism/preclinical reasoning).

**To proceed, the following is needed:**
- TFDA labeling data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action detail from DrugBank — currently a High-severity data gap (DG002)
- Disease-specific dosing and safety data for neonatal/pediatric permanent diabetes populations, since pancreatic agenesis typically presents in infancy
- Regulatory pathway assessment given insulin glargine is not currently marketed in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Romiplostim
parent: Model Prediction Only (L5)
nav_order: 1132
evidence_level: L5
indication_count: 10
monitor_inn: "ROMIPLOSTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "platelet-type bleeding disorder", "autosomal dominant macrothrombocytopenia", "Ehlers-Danlos syndrome, fibronectinemic type"]
---

# Romiplostim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Romiplostim: From Aplastic Anemia and Autoimmune Thrombocytopenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Romiplostim is a thrombopoietin (TPO) receptor agonist, originally associated with idiopathic aplastic anemia, aplastic anemia, and autoimmune thrombocytopenia (immune thrombocytopenic purpura, ITP).
The TxGNN model ranks **primary release disorder of platelets** as its top prediction, but there are **0 clinical trials** and only **1 publication** (a mechanistic study of ITP, not of this disease), so the evidence is weak.
The prediction is best treated as a model artifact until disease-specific evidence appears.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic aplastic anemia, aplastic anemia, autoimmune thrombocytopenia (from the knowledge graph; no approved-indication text is available in the licence record) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.99983% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA125268) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From the pharmacology data, romiplostim is a peptide that targets the thrombopoietin receptor (MPL). It stimulates megakaryocyte proliferation and platelet production, and it is used to raise platelet counts in chronic ITP. The FDA permits its use in pediatric ITP patients aged 1 year and older.

The predicted disease is a **qualitative** platelet function defect, in which platelets fail to release their granule contents. Raising platelet count would not be expected to correct this. The literature found (PMID 25682608) studies antiplatelet autoantibodies that impair platelet production in ITP, which is a different disease mechanism. The very high TxGNN score most likely reflects network proximity to ITP rather than disease-specific evidence.

**Other top predictions (all without clinical trials):**

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Pseudo-von Willebrand disease | 99.99977% | L5 | No rationale; more platelets could theoretically worsen platelet-vWF aggregation |
| 3 | Glanzmann thrombasthenia | 99.99954% | L5 | Platelet count is normal; the defect is functional |
| 4 | Fetal and neonatal alloimmune thrombocytopenia | 99.98730% | L4 | Immune-mediated, partly analogous to ITP; only indirect support; the most plausible candidate |
| 5 | Scott syndrome | 99.96656% | L5 | Qualitative defect; unlikely to respond |
| 6 | Hemorrhagic disorder due to constitutional thrombocytopenia | 99.95290% | L5 | Plausible only for specific genetic subtypes |
| 7 | Bleeding diathesis due to a collagen receptor defect | 99.95080% | L5 | Receptor function defect; unlikely to respond |
| 8 | Platelet-type bleeding disorder | 99.93190% | L5 | Generic, mostly functional category |
| 9 | Autosomal dominant macrothrombocytopenia | 99.88074% | L5 | Some TPO-agonist responses reported in related conditions, but no evidence for this entry |
| 10 | Ehlers-Danlos syndrome, fibronectinemic type | 99.84516% | L5 | No plausible pathway |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top prediction (primary release disorder of platelets):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Basic/mechanistic study | Haematologica | Antiplatelet autoantibodies from ITP patients inhibit proplatelet formation by megakaryocytes and impair platelet production in vitro; it does not address this disease |

For the most plausible alternative (fetal and neonatal alloimmune thrombocytopenia), the literature is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31239245](https://pubmed.ncbi.nlm.nih.gov/31239245/) | 2019 | Review | Blood Advances | Romiplostim in pediatric ITP: drug development and current practice; FDA approval for pediatric ITP in December 2018 |
| [34711622](https://pubmed.ncbi.nlm.nih.gov/34711622/) | 2021 | Case report | BMJ Case Reports | Management of refractory ITP in pregnancy |
| [20410910](https://pubmed.ncbi.nlm.nih.gov/20410910/) | 2010 | Perspective | Journal of Perinatology | Whether novel thrombopoietic agents could reduce platelet transfusions in neonates |
| [23822831](https://pubmed.ncbi.nlm.nih.gov/23822831/) | 2013 | Case report | European Journal of Haematology | Complete remission of refractory ITP after a short course of romiplostim |
| [27605856](https://pubmed.ncbi.nlm.nih.gov/27605856/) | 2016 | Case report | Asian Journal of Transfusion Science | Refractory ITP in pregnancy managed with eltrombopag (a different TPO agonist) |
| [23257464](https://pubmed.ncbi.nlm.nih.gov/23257464/) | 2012 | Review | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Advances in thrombopoietic drugs for childhood ITP |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125268 | Nplate (Amgen, Inc) | Injection, powder, lyophilized, for solution | Not stated in the licence record; status: cancelled |

---

## Safety Considerations

- **Drug Interactions**:
  - Carfilzomib: **Major** interaction (DDInter).
  - Thrombopoietin receptor (MPL): this is the pharmacological target, not an interaction in the usual sense.

For label warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials, and its only publication concerns a different disease mechanism. Romiplostim raises platelet count and would not be expected to fix a platelet function defect. Fetal and neonatal alloimmune thrombocytopenia is a more plausible research question (L4), but its support is only indirect and safety in pregnancy and neonates is unresolved.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Disease-specific evidence (case series or trials) for the top predictions, or a decision to prioritize the fetal and neonatal alloimmune thrombocytopenia question
- Subtype-specific evaluation if inherited thrombocytopenias are pursued
- Clarification of the US marketing status, since the licence record shows "Cancelled only"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


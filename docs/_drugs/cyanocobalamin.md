---
layout: default
title: Cyanocobalamin
parent: Model Prediction Only (L5)
nav_order: 553
evidence_level: L5
indication_count: 1
monitor_inn: "CYANOCOBALAMIN"
predicted_indications: ["biotin metabolic disease"]
last_modified_at: 2026-10-31
description: "Cyanocobalamin: predicted new indication Biotin metabolic disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Cyanocobalamin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Cyanocobalamin: Biotin metabolic disease
{: .text-alpha }

## One-Sentence Summary

Cyanocobalamin (vitamin B12) was originally used to treat vitamin B12 deficiency and related anemias, including pernicious anemia.
The TxGNN model predicts it may be effective for **Biotin Metabolic Disease**,
but currently there are **0 clinical trials** and only **1 publication** (a general review that does not directly address this indication), so the evidence is essentially model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of FDA Applications | at least 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cyanocobalamin is a form of vitamin B12, and its efficacy in vitamin B12 deficiency is established. It is a cofactor for methionine synthase and methylmalonyl-CoA mutase.

Biotin is a cofactor for carboxylases such as propionyl-CoA carboxylase, which feeds into the methylmalonyl-CoA pathway. A plausible link is therefore shared propionate, branched-chain amino acid, and odd-chain fatty acid metabolism, along with a possible overlap in vitamin-dependent inborn errors of metabolism.

This is a hypothesis only. The prediction score is high, but no clinical or mechanistic evidence in the data compiled for this report supports it. Any benefit would also need to be distinguished from standard care for biotinidase or holocarboxylase synthetase deficiency, which is biotin supplementation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review | Journal of Chemical Technology and Biotechnology | Overview of biotechnological (fermentation and bioconversion) production of vitamins and coenzymes. It addresses manufacturing, not treatment of biotin metabolic disease. |

---

## US Market Information

The drug is marketed in the US, with 11 valid licenses. The data compiled for this report provides no approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA214655 | cyanocobalamin (Zydus Lifesciences) | Injection, solution | Not available |
| ANDA206503 | cyanocobalamin (Asclemed USA) | Injection | Not available |
| ANDA080737 | Cyanocobalamin (American Regent) | Injection, solution | Not available |
| ANDA217839 | Cyanocobalamin (Lifestar Pharma) | Injection, solution | Not available |
| ANDA212458 | cyanocobalamin (Padagis Israel) | Spray | Not available |

Six further ANDAs (all cancelled) cover injectable forms from other manufacturers.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. The sample reviewed shows mostly **Minor** interactions with acid-suppressing drugs (famotidine, ranitidine, cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole) and with potassium chloride. These agents may reduce B12 absorption with long-term use. Several others are of **Unknown** severity (metformin, glimepiride, acarbose, rosiglitazone, mesalazine, doxycycline, morphine, sucralfate).

Please refer to the package insert for warnings and contraindications, as this information was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9960), but there are no registered clinical trials, and the single publication is unrelated to treatment. The proposed mechanistic link is hypothetical. In addition, standard biotin therapy already exists for biotin-related disorders, and the drug is marketed in the US with 11 valid licenses.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- Mechanistic or preclinical evidence linking cobalamin to biotin-dependent pathways
- Case reports or studies in biotinidase or holocarboxylase synthetase deficiency
- Clarification of the US regulatory and market status
- Route and formulation compatibility assessment for the proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


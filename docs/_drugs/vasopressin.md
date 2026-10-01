---
layout: default
title: Vasopressin
parent: Moderate Evidence (L3-L4)
nav_order: 1285
evidence_level: L4
indication_count: 2
---

# Vasopressin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Vasopressin: From a Marketed Injectable to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vasopressin is a marketed injectable product in the United States, but the source data does not record its original indication.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but there are **0 clinical trials** and **3 publications**, and none of the publications address prothrombin. Evidence is very weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for vasopressin is not available in the source data, and neither are its original indications. The only plausible link is indirect. Vasopressin and its analog desmopressin (DDAVP) raise plasma factor VIII and von Willebrand factor by releasing endothelial stores through V2 receptors.

This mechanism does not act on prothrombin (factor II), so there is no plausible direct benefit in prothrombin deficiency. The very high TxGNN score (99.63%) most likely reflects graph proximity to other coagulation factor deficiencies, not a pharmacological rationale. The retrieved literature concerns factor VIII and factor V deficiency, and none of it addresses prothrombin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Acquired hemophilia A (autoantibodies against factor VIII): diagnosis, causes, clinical spectrum and treatment options. Not about prothrombin. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki (Japanese J Clin Hematol) | DDAVP given to a 43-year-old man with congenital combined factor V and factor VIII deficiency. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki (Japanese J Clin Hematol) | Cesarean section managed with factor VIII concentrate replacement in a pregnant woman with combined factor V and factor VIII deficiency. |

---

## US Market Information

Five of the 20 authorizations are listed below. The source data does not include approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| NDA217569 | Vasopressin in 0.9% Sodium Chloride | Injection | Baxter Healthcare Corporation |
| ANDA213206 | Vasopressin | Injection, solution | Fresenius Kabi USA, LLC |
| ANDA214314 | Vasopressin | Injection | Eugia US LLC |
| ANDA216963 | Vasopressin | Injection | Gland Pharma Limited |
| ANDA214314 | Vasopressin | Injection | ProPharma Distribution |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no on-target literature. The known mechanism (raising factor VIII and von Willebrand factor) does not act on prothrombin, so the high model score is not supported by pharmacology.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently blocking the safety screening)
- Original indications and mechanism of action data for vasopressin
- Evidence that vasopressin or desmopressin affects prothrombin levels or bleeding in prothrombin deficiency
- Alternative explanation of the TxGNN score, such as the graph path behind the prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Vasopressin
parent: Moderate Evidence (L3-L4)
nav_order: 1285
evidence_level: L4
indication_count: 2
monitor_inn: "VASOPRESSIN"
predicted_indications: ["congenital prothrombin deficiency", "drug-induced osteoporosis"]
last_modified_at: 2026-10-14
description: "Vasopressin: predicted new indication Congenital prothrombin deficiency (evidence level L4). Approved use: Not available in the compiled data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Vasopressin: From Vasodilatory Shock to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vasopressin is a synthetic form of the natural antidiuretic hormone, supplied as an injectable. The approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but there are **0 registered clinical trials** and only **3 loosely related publications** (all reviews or case reports, none about vasopressin or prothrombin deficiency directly). The prediction is therefore supported only by a computational score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (all listed authorizations are cancelled) |
| Number of NDAs | 9 (authorizations listed, including NDAs and ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, vasopressin and its analog desmopressin (DDAVP) raise plasma factor VIII and von Willebrand factor by stimulating V2-receptor-mediated release from endothelial cells. This is a plausible route for some rare bleeding disorders.

However, prothrombin (factor II) is not known to be released through this pathway, so the mechanistic link to congenital prothrombin deficiency is weak. The supplied literature concerns factor VIII and factor V deficiencies and acquired hemophilia A, not prothrombin deficiency. The very high TxGNN score most likely reflects a shared coagulation-disorder neighborhood in the knowledge graph rather than a direct mechanism.

One caveat: the cited case reports concern desmopressin, a distinct analog, not vasopressin itself. Their findings cannot be assumed to transfer.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Overview of acquired hemophilia A: autoantibodies against factor VIII, diagnosis, causes, clinical spectrum and treatment options. Not specific to vasopressin or prothrombin deficiency. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki (Japanese Journal of Clinical Hematology) | Desmopressin (DDAVP) given to a 43-year-old man with congenital combined factor V and factor VIII deficiency. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki (Japanese Journal of Clinical Hematology) | Cesarean section managed with factor VIII replacement in a pregnant woman with combined factor V and VIII deficiency. Relevance to vasopressin is unclear. |

No clinical trials are registered for this indication, so the clinical trial section is omitted.

## US Market Information

All nine authorizations in the compiled data are cancelled, and approved indication text is not available for any of them.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA217569 | Vasopressin in 0.9% Sodium Chloride (Baxter Healthcare) | Injection | Cancelled |
| ANDA213206 | Vasopressin (Fresenius Kabi USA) | Injection, solution | Cancelled |
| ANDA214314 | Vasopressin (Eugia US) | Injection | Cancelled |
| ANDA216963 | Vasopressin (Gland Pharma) | Injection | Cancelled |
| NDA204485 | Vasostrict (Par Health USA) | Injection | Cancelled |

Four additional cancelled authorizations are on record (Amneal, Civica, Amphastar, Long Grove).

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total, and 20 are in the data compiled for this report. Most are Moderate. Major-level interactions include:
  - Dolasetron
  - Cisapride
  - Papaverine
  - Macimorelin

  Moderate interactions include epinephrine, heparin, cilostazol, clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, promethazine, famotidine, loperamide and chlorpropamide. Several are linked to QT prolongation or cardiovascular effects, so any new use would need a review of the full list.

Package insert warnings and contraindications were not available. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.63%), but there are no clinical trials and the literature is only weakly related, covering other factor deficiencies and a different drug (desmopressin). Prothrombin is not known to be released through the vasopressin/V2 pathway. The evidence supports only an L4 level, and a critical safety data gap remains.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which block safety screening
- Mechanism of action data, such as from DrugBank
- Original approved indication text, and clarification of why all US authorizations are cancelled
- Evidence of a direct biological link between vasopressin and prothrombin (factor II) levels or activity
- Evidence specific to vasopressin, not desmopressin, in congenital prothrombin deficiency
- A review of the full drug interaction list for the intended patient population

**Note on the second prediction:** The model also predicted **drug-induced osteoporosis** (score 99.62%, evidence level L5). No clinical trials or literature support it, and vasopressin would not be expected to treat this condition. Its vasoconstrictive and antidiuretic effects raise safety concerns for chronic use. The recommendation for this indication is also Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


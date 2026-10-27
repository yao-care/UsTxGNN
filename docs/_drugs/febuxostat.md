---
layout: default
title: Febuxostat
parent: Moderate Evidence (L3-L4)
nav_order: 693
evidence_level: L4
indication_count: 3
monitor_inn: "FEBUXOSTAT"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
last_modified_at: 2026-10-14
description: "Febuxostat: predicted new indication Renal hypouricemia (evidence level L4). Approved use: Hyperuricemia"
---

# Febuxostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

## Febuxostat: From Hyperuricemia to Renal Hypouricemia
{: .text-alpha }

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor originally used to treat hyperuricemia (gout).
The TxGNN model predicts it may be effective for **renal hypouricemia**, but the supporting evidence is thin: **1 clinical trial** (of doubtful relevance) and **2 publications**, none of which show proven benefit.
Because renal hypouricemia is a condition of already low uric acid, the high model score is likely a network-proximity artifact rather than a true therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia (the approved indication text was not available in the compiled data; the original indication comes from the knowledge graph) |
| Predicted New Indication | Renal hypouricemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 (all cancelled; 1 NDA and 9 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known pharmacology, febuxostat is a non-purine selective xanthine oxidase inhibitor that lowers serum uric acid, and its efficacy in hyperuricemia is established.

Renal hypouricemia, however, is the opposite problem. It is caused by loss-of-function of urate transporters (URAT1/GLUT9), which leaves serum urate already low. Lowering urate further is mechanistically counterproductive and could be harmful. The high TxGNN score most likely reflects shared urate-metabolism nodes in the knowledge graph rather than real therapeutic benefit.

The only plausible link is indirect. A 2023 case report (PMID 36754409) describes a young football player with familial renal hypouricemia and recurrent exercise-induced acute kidney injury, and discusses xanthine oxidoreductase inhibitors as a possible preventive measure. This is a hypothesis-level proposal, not demonstrated clinical efficacy.

Two other lower-ranked predictions are mechanistically more coherent, although both rest on case-level evidence only:
- **Partial HPRT deficiency** (score 99.98%): the purine overproduction and hyperuricemia can plausibly be controlled by xanthine oxidase inhibition. Allopurinol is the standard, and febuxostat could be an alternative in allopurinol-intolerant patients.
- **Lesch-Nyhan syndrome** (score 99.68%): febuxostat could control hyperuricemia and prevent urate nephropathy, but it does not address the neurobehavioral features, which are the main unmet need.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Studies the effect of uric acid control on stone recurrence and renal function in patients with calculi and hyperuricemia. This is likely a hyperuricemia study matched through the drug and has no usable evidence for renal hypouricemia. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case report (classified as Review) | Internal Medicine | Proposes non-purine selective xanthine oxidoreductase inhibitors (febuxostat) to prevent exercise-induced acute kidney injury in a 16-year-old with familial renal hypouricemia (URAT1 mutations) where hydration alone failed. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia (serum urate < 2 mg/dL), its causes and clinical handling for rheumatologists. It is background information and does not test febuxostat. |

---

## US Market Information

All 10 US authorizations are cancelled, and the approved indication text was not available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021856 | ULORIC (Takeda Pharmaceuticals America) | Tablet | Not available |
| ANDA205443 | Febuxostat (Zydus Lifesciences) | Tablet | Not available |
| ANDA205467 | Febuxostat (Sun Pharmaceutical Industries) | Tablet, film coated | Not available |
| ANDA210461 | Febuxostat (Aphena Pharma Solutions) | Tablet, film coated | Not available |
| ANDA206266 | Febuxostat (Solco Healthcare) | Tablet | Not available |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): stroke disorder, cerebrovascular disorder, cerebral infarction, myocardial infarction, coronary thrombosis, and hemoglobinopathy.
- **Drug Interactions**: 22 interactions were recorded. The **Major** ones are:
  - Mercaptopurine
  - Azathioprine
  - Leflunomide
  - Teriflunomide

  Moderate interactions include methotrexate, theophylline and related xanthines (aminophylline, dyphylline, oxtriphylline), tioguanine, clofarabine, epirubicin, trabectedin, asparaginase, pegaspargase, brentuximab vedotin, naltrexone, and interferon beta products.
- **Additional considerations for the predicted indications**: xanthine accumulation and the risk of xanthine nephrolithiasis require monitoring in HPRT-related disorders. Safety in children is not established.

Please refer to the package insert for label warnings and contraindications, which were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Further urate lowering in renal hypouricemia is mechanistically counterproductive. The only supporting evidence is a single hypothesis-level case report, and the one registered trial is unrelated to the condition. The data are limited to the model prediction plus weak literature (L4). Market status is cancelled only, and the knowledge graph flags cardiovascular and cerebrovascular contraindication signals.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Evidence beyond single case reports that xanthine oxidase inhibition prevents exercise-induced acute kidney injury in renal hypouricemia
- Safety assessment, including cardiovascular risk, for this population
- Consideration of the HPRT deficiency or Lesch-Nyhan indications as alternative research questions, where the mechanism is more coherent, though pediatric safety and access (cancelled licenses) must be resolved first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


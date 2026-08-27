---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 693
evidence_level: L5
indication_count: 3
---

# Febuxostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Febuxostat: From Hyperuricemia/Gout to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor whose established use is lowering serum urate in hyperuricemia/gout (Taiwan-specific regulatory indication text is not on file). The TxGNN model predicts a paradoxical new application — preventing exercise-induced acute kidney injury in patients with **Renal Hypouricemia** — supported so far by **1 clinical trial of uncertain relevance** and **2 review-level publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from Taiwan regulatory data (no licenses on file); known drug-class use is hyperuricemia associated with gout |
| Predicted New Indication | Renal Hypouricemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for febuxostat in this evidence pack. Based on known pharmacological information, febuxostat is a non-purine selective xanthine oxidase (XO) inhibitor; its efficacy in lowering serum urate in its original indication (hyperuricemia/gout) is well established, and mechanistically it may extend to other disorders of purine/urate metabolism.

The predicted indication here, however, runs in the **opposite direction** from the drug's typical use. Renal hypouricemia (URAT1/GLUT9 transporter defects) causes chronically *low* baseline uric acid, but affected patients can experience a post-exercise surge in urate generation/excretion imbalance, causing intratubular urate crystallization and exercise-induced acute kidney injury (EIAKI). In this context, an XO inhibitor is used prophylactically to blunt the post-exercise urate overshoot — the same pharmacologic lever (urate production inhibition) applied to a very different clinical scenario. The supporting literature (PMID 36754409) itself frames this as a "possible use," i.e., still hypothesis-stage rather than confirmed practice.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Registered as a study of uric acid control on stone recurrence/renal function in hyperuricemia-associated calculi (Shanghai Xu-hui Central Hospital, Urology). Title/summary do not confirm this trial actually targets renal hypouricemia or EIAKI prevention — relevance graded **C (uncertain)**; original registry record should be checked before citing as support. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review (case-based) | Internal Medicine (Tokyo) | Reports a 16-year-old with familial renal hypouricemia (URAT1 compound heterozygous mutation) and recurrent EIAKI; proposes non-purine selective XO inhibitors (febuxostat) as possible prophylaxis when exercise-intensity reduction alone fails. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | General narrative review of hypouricemia etiology and management for rheumatologists; not febuxostat-specific. |

## US Market Information

Febuxostat currently has no licenses or NDAs on file (`total_licenses = 0`); the drug is marked **not marketed**. No approved-indication text is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or DDI data are available for febuxostat in this evidence pack; the missing TFDA label/warning data is flagged as a blocking gap — see Conclusion.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for febuxostat in renal hypouricemia rests on a single trial of uncertain relevance (grade C) and review/case-level literature only — no RCT or prospective cohort directly targeting this population exists yet. Compounding this, the TFDA label/safety data required for even an initial safety screen (S1) is a **blocking data gap** (DG001), and formal MOA confirmation is also missing (DG002).

**To proceed, the following is needed:**
- TFDA-equivalent label data (warnings, contraindications) to clear the blocking safety gap
- Confirmed mechanism of action documentation for febuxostat
- Verification of NCT04398251's actual relevance to renal hypouricemia/EIAKI (check original trial registry, not just title)
- Prospective clinical data on febuxostat prophylaxis specifically in confirmed URAT1/GLUT9-deficient patients

**Note:** Two other TxGNN-predicted indications for febuxostat in this evidence pack — HPRT partial deficiency and Lesch-Nyhan syndrome — carry a stronger internal recommendation ("Proceed with Guardrails") because their mechanism (purine-salvage failure → uric acid overproduction) directly matches febuxostat's established XO-inhibition pathway, unlike the paradoxical renal hypouricemia case above. These may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

